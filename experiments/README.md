# 实验目录

| 目录 | 用途 |
|---|---|
| `baseline/` | 基线方法：实现、配置与结果 |
| `exp01/` | 实验 1（待命名） |
| `exp02/` | 实验 2（待命名） |

## 每个实验内部建议结构

```
exp01/
├── README.md        # 实验说明：目的、设置、结论
├── config.yaml      # 本次实验配置
├── main.py / run.sh # 运行入口
└── output/          # 输出结果（小文件可提交）
```

## 规则

- 新实验按 `exp01`、`exp02`… 递增编号，与 [docs/03-design/experiment_design.md](../docs/03-design/experiment_design.md) 的实验矩阵对应。
- 每次实验至少记录：配置、命令、关键结果、与基线的对比。
- 体积大的输出放到 `results/`（不入库），实验目录只留可复现的脚本与小结。
