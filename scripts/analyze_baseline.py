#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baseline 结果分析：汇总性能指标 + 粗检回答质量。

用法：
    python scripts/analyze_baseline.py results/logs/baseline_run1.jsonl
"""
import json
import re
import statistics
import sys
from collections import Counter


def main():
    if len(sys.argv) < 2:
        sys.exit("用法: python scripts/analyze_baseline.py <jsonl>")
    path = sys.argv[1]
    rows = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    n = len(rows)
    if n == 0:
        sys.exit("结果为空")

    lat = [r["total_latency_ms"] for r in rows]
    tps = [r["tokens_per_sec"] for r in rows]
    tok = [r["tokens"] for r in rows]

    print(f"题目数: {n}")
    print(f"时延(ms): avg={statistics.mean(lat):.0f} median={statistics.median(lat):.0f} "
          f"min={min(lat):.0f} max={max(lat):.0f}")
    print(f"吞吐(tok/s): avg={statistics.mean(tps):.1f} median={statistics.median(tps):.1f}")
    print(f"生成token: avg={statistics.mean(tok):.0f} median={statistics.median(tok):.0f}")

    # 粗检：英文拒答 / 过短回答 / 提及不确定
    pattern = re.compile(
        r"I'?m sorry|I apologize|don't understand|could you please|"
        r"please provide|clarify|rephrase|didn't receive|missing",
        re.I,
    )
    bad = [r for r in rows if pattern.search(r["answer"])]
    empty = [r for r in rows if len(r["answer"].strip()) < 10]
    print(f"疑似英文/拒答: {len(bad)}/{n} ({len(bad) / n * 100:.0f}%)")
    print(f"过短回答(<10字): {len(empty)}/{n}")

    print("类别分布:", dict(Counter(r["category"] for r in rows)))

    # 每类第一条的回答片段，便于人工抽查
    seen = set()
    for r in rows:
        if r["category"] in seen:
            continue
        seen.add(r["category"])
        print(f"\n[{r['category']}] {r['question'][:30]}...")
        print(f"  -> {r['answer'][:150]}")

    # 记录拒答题目 id
    if bad:
        print("\n拒答题目:", ", ".join(str(r["id"]) for r in bad))


if __name__ == "__main__":
    main()
