# 上游验收与正式包闸门

| 成果 | 实际路径 | 证据 | 状态 |
|---|---|---|---|
| 来源及理解 | docs/SOURCE_MANIFEST.json、digest.md、reading-coverage.json | 版权/目录及关键正文原页核验；选定语义窗口如实记录 | passed，限定范围 |
| 任务及候选 | docs/tasks.md、candidates.json、coverage-audit.md | 12任务去向，29候选四分流守恒 | passed |
| 能力契约 | skills/mind_skill/references/五张方法卡 | R/I/A1/A2/E/B、来源及条件、自包含 | passed |
| 示例 | examples/integrated.md | 合成身份、替代解释及权限边界 | passed |
| 评测 | evaluation/cases.json、outputs.md、report.md | 13例演练及13程序测试；非盲评 | passed，自检范围 |
| 正式包 | skills/mind_skill | 独立复制、引用检查与显式读取演练 | passed；名称例外 |
| 自动发现 | 未实施 | 用户未要求本机安装；仅支持显式读取 | not_applicable于本次安装，自动发现未测 |
| TeX/PDF/数学全族证明 | 未启用 | 用户任务不要求这些交付 | not_applicable |
| 未读与待核内容 | docs/coverage-audit.md | 未混入active | isolated |
| 冻结与远端 | publication/PUBLIC_MANIFEST.json及本地回执 | 冻结后逐文件核验 | 见回执 |

正式包以前述已验收的限定方法、资源和演练为输入；哈希快照由PUBLIC_MANIFEST绑定。未声明全文审校、自动发现或独立盲评通过。
