# AI 测试作品集

> 6 年通信协议测试工程师 → AI 测试的项目作品集
> 主题：AAA 认证协议（RADIUS / TACACS+ / 802.1X / CoA / 计费）知识库助手的质量保障

## 项目结构

| 项目 | 定位 | 状态 |
|---|---|---|
| `project-a-rag-qa/` | 主项目：AAA 认证协议知识库助手测试体系 | 进行中（第 1 周） |
| `project-b-protocopilot/` | 差异化：AI 辅助协议测试工具 | 待开始（第 2 周） |
| `project-c-8021x-framework/` | 亮点：802.1X 测试框架设计（脱敏） | 待开始 |

## 主项目：AAA 知识库助手测试体系

目标：为一个 AAA 认证协议知识库问答服务建立可重复的质量保障体系，证明能为 AI 系统设计测试与评估流程。

核心能力：
- 测试数据设计（等价类、边界、负向、领域场景 → AI 测例）
- 确定性断言 + LLM rubric 评估
- RAG 检索/生成归因与失败案例分析
- Agent / 工具调用测试
- 红队安全测试（注入、越权、PII、幻觉）
- CI 回归门禁

数据与文档均来自公开标准（RFC 2865/2866/3576、IEEE 802.1X 等），不含任何前公司资料。

## 本地运行

```bash
# 首次配置
python -m venv .venv
.venv\Scripts\python.exe -m pip install pytest

# 运行测试（在 project-a-rag-qa 目录下）
cd project-a-rag-qa
../.venv\Scripts\python.exe -m pytest -q
```

当前状态：22 passed（D1 脚手架）。

## 路线图

详见桌面 `AI测试工程师8周详细计划.md`（8 周，从 Python/pytest 基础到作品集发布）。
