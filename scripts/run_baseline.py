#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baseline 评测脚本骨架：本地 LLM 直接问答（no-RAG）批量测试。

用法（PowerShell）：
    pip install requests pyyaml
    python scripts/run_baseline.py --config experiments/baseline/config.yaml `
        --questions data/samples/standard_questions.jsonl `
        --output results/logs/baseline_run1.jsonl

说明：
    - 通过 Ollama /api/generate 批量提问，记录回答、时延、token 吞吐。
    - 首 token 时延（ttft）需要流式模式，本骨架记录总时延；ttft 见 TODO。
    - 显存/内存占用请另用 nvidia-smi / 任务管理器记录。
    - RAGAS 质量评测不在本脚本内（需安装 ragas，见 evaluation/README）。
"""
import argparse
import json
import sys
import time
import urllib.request


def load_config(path):
    try:
        import yaml
    except ImportError:
        sys.exit("缺少依赖：请先执行 pip install pyyaml requests")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_questions(path):
    questions = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            questions.append(json.loads(line))
    return questions


def ask(model_name, url, prompt, temperature, max_tokens, system_prompt=""):
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False,
        "system": system_prompt,
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens,
        },
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=600) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    elapsed = time.time() - t0
    return data, elapsed


def main():
    ap = argparse.ArgumentParser(description="Baseline（no-RAG）批量评测")
    ap.add_argument("--config", required=True, help="config.yaml 路径")
    ap.add_argument("--questions", required=True, help="标准问题集 jsonl 路径")
    ap.add_argument("--output", required=True, help="输出 jsonl 路径（放 results/logs/）")
    args = ap.parse_args()

    cfg = load_config(args.config)
    model_name = cfg["model"]["name"]
    url = cfg["server"]["url"].rstrip("/") + cfg["server"]["api"]
    temperature = cfg["inference"]["temperature"]
    max_tokens = cfg["inference"]["max_tokens"]
    system_prompt = cfg["inference"].get("system_prompt", "")

    questions = load_questions(args.questions)
    print(f"共 {len(questions)} 题，模型 {model_name}")

    with open(args.output, "w", encoding="utf-8") as out:
        for i, q in enumerate(questions, 1):
            question = q.get("question", "")
            print(f"[{i}/{len(questions)}] {question[:40]}...")
            data, elapsed = ask(model_name, url, question, temperature, max_tokens, system_prompt)
            eval_count = data.get("eval_count", 0) or 0
            rec = {
                "id": q.get("id", i),
                "category": q.get("category", ""),
                "question": question,
                "answer": data.get("response", ""),
                "total_latency_ms": round(elapsed * 1000, 1),
                "tokens": eval_count,
                "tokens_per_sec": round(eval_count / max(elapsed, 1e-6), 2),
                # TODO(ttft): 需要流式模式，记录首 token 时间
                # TODO(资源): nvidia-smi / 任务管理器另记，或后续脚本补充
            }
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            out.flush()

    print(f"完成，结果写入 {args.output}")


if __name__ == "__main__":
    main()
