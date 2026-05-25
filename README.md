## 交流群

- [点击链接加入群聊【天命-智能创作（BUG收集）】](https://qm.qq.com/q/YWivpFjKou)

群号：414086347

> ## 寻找软件版？
>
> 如果你更喜欢开箱即用的桌面应用体验，请移步：[天命-智能小说创作软件](https://github.com/zy-zmc/tianming-novel-ai-writer)
>
> 无需任何提示词知识，下载即用，内置完整天命系统。

---

# 天命 · 新书项目模板

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

> **TianMing** 是一个可直接复制为新书项目的长篇小说协同创作模板。
> 项目根目录是新书工作区，`.tianming/` 是内置天命规则系统。

---

## 一、这个项目是什么

「天命」是一个为长篇小说创作而设计的结构化 AI 协同写作系统。

- **执笔者（用户）** 负责创意、世界观、人物烙印、文风样本
- **天命（系统）** 负责保证跨章节的世界观一致性、伏笔回收、节奏控制、文风稳定

本仓库已经从单独的 Skill 包重构为“新书项目模板 + 内置规则包”：

- 根目录用于存放新书知识库、`AGENTS.md` 和项目说明
- `.tianming/` 存放完整天命规则、协议、模板和维护脚本
- AI AGENTS 进入项目后必须先读 `AGENTS.md`，再按 `.tianming/SKILL.md` 的规则执行

---

## 二、快速开始

### 1. 复制为新书项目

把本仓库复制成你的新书目录，例如：

```text
我的新书/
├── AGENTS.md
├── README.md
├── .tianming/
└── examples/
```

### 2. 填写根目录知识库

根目录已经放置 5 个可直接填写的知识库文件。新开书时先填写它们；如需重置，可从 `.tianming/kb-templates/` 重新复制模板。

```text
我的新书/
├── 世界基石.md           ← 由系统自动维护，初始可为空模板
├── 世界观规则.md         ← 必填
├── 角色档案.md           ← 必填
├── 档案事件.md           ← 同人/前传必填，原创可选填
└── 文风样本.md           ← 必填，越完整越好
```

根目录文件与模板来源：

| 目标文件 | 模板来源 |
|---|---|
| `世界基石.md` | `.tianming/kb-templates/world-stone.template.md` |
| `世界观规则.md` | `.tianming/kb-templates/world-rules.template.md` |
| `角色档案.md` | `.tianming/kb-templates/character-archive.template.md` |
| `档案事件.md` | `.tianming/kb-templates/archive-events.template.md` |
| `文风样本.md` | `.tianming/kb-templates/style-sample.template.md` |

### 3. 启动 AI 会话

在新书项目根目录开启 AI 会话。AI AGENTS 必须：

1. 读取 `AGENTS.md`
2. 读取 `.tianming/SKILL.md`
3. 按 `.tianming/SKILL.md` 的指令路由加载协议
4. 从项目根目录读取真实知识库

### 4. 初始化

输入：

```text
初始化
```

系统会执行 `.tianming/core/boot-sequence.md` 的启动规则，检查协议绑定状态与知识库连接状态，并返回标准化报告。

### 5. 开始创作

按以下指令顺序推进：

| 步骤 | 指令 | 产出 |
|---|---|---|
| 1 | `「天命：大纲」` | 【战略宏图】 + 【宏观节奏宪章】 |
| 2 | `「天命：规划」` | 【全书战役总蓝图】 + 【指令序列】 |
| 3 | `「天命：目录 | 卷1 第1-30章」` | 详细章节目录 |
| 4 | `「天命：草案 | 卷1 第1章」` | 可选章节骨架蓝图 |
| 5 | `「天命：正文 | 卷1，第1章」` | 完整章节正文 |
| 6 | 重复 4-5 直到本卷完成 | 持续创作 |
| 7 | `「天命：体检」` | 《世界基石.md》健康报告 |
| 8 | `「天命：存档」` | 结构化更新补丁 |

---

## 三、目录结构

```text
新书项目/
├── AGENTS.md                         ← AI AGENTS 入口规则
├── README.md                         ← 本文件
├── LICENSE
├── 世界基石.md                       ← 新书动态核心，根目录初始模板
├── 世界观规则.md                     ← 新书静态基石，根目录初始模板
├── 角色档案.md                       ← 新书静态基石，根目录初始模板
├── 档案事件.md                       ← 新书静态基石，根目录初始模板
├── 文风样本.md                       ← 新书静态基石，根目录初始模板
│
├── .tianming/                        ← 内置天命规则系统
│   ├── SKILL.md                      ← 主入口（路由表 + 启动清单）
│   ├── core/                         ← 系统内核
│   ├── codex/                        ← 绝对法典
│   ├── protocols/                    ← 运行协议
│   ├── aesthetic/                    ← 天书铁律
│   ├── constants/                    ← 全局常数
│   ├── kb-templates/                 ← 知识库模板
│   └── scripts/                      ← 维护工具脚本
│
├── examples/
│   └── mini-volume/                  ← 5 章极简样例卷《镜中之约》
└── tests/
    └── validate-embedded-layout.sh   ← 内置结构校验
```

---

## 四、术语速查表

### 系统术语

| 术语 | 含义 |
|---|---|
| **执笔者** | 你（用户） |
| **天命** | 系统本身 |
| **统一知识库核心** | 《世界基石.md》+ 四件静态基石的总称 |
| **战略宏图** | 故事的最高纲领，由 `「天命：大纲」` 生成 |
| **战役总蓝图** | 全书的战略推演，由 `「天命：规划」` 生成 |
| **战术执行目录** | 详细章节目录，由 `「天命：目录」` 生成 |
| **显化蓝图草案** | 章节骨架，由 `「天命：草案」` 生成 |
| **当前章之绝对蓝图** | 正文协议从目录中锁定的当前章信息 |
| **精修初稿** | 4500-5500 字的预渲染稿，待打磨成最终成品 |

### 引用规范

| 格式 | 含义 |
|---|---|
| `[ID:xxx]` | 当前协议的唯一标识符 |
| `[REF:xxx]` | 引用其他协议（普通调用） |
| `[KERNEL_REF:xxx]` | 强制注入其他协议（内核级、不可协商） |
| `[VAR:xxx]` | 引用 `.tianming/constants/global-constants.md` 的常数 |
| `[元标签:...]` | 协议的功能分类标签 |

### 叙事术语

| 术语 | 含义 |
|---|---|
| **Tier-1 战略级** | 影响主角命运/世界结局的伏笔 |
| **Tier-2 战役级** | 影响当前卷/派系的伏笔 |
| **Tier-3 战术级** | 影响局部冲突的伏笔 |
| **峰值章节** | 冲突值不低于四星的章节 |
| **奇点事件** | 临时挂起力量上限的破格章节 |
| **载体 DNA** | 悬念钩子的语义指纹 |
| **缓冲-代价** | 用于代价清算的缓冲章 |
| **缓冲-对话** | 用于关系演变的缓冲章 |
| **缓冲-线索** | 用于伏笔/信息揭露的缓冲章 |

---

## 五、维护工具

### 内置结构校验

```bash
bash tests/validate-embedded-layout.sh
```

退出码 `0` 表示新书模板结构满足内置规则包要求。

### 引用完整性 Lint

```powershell
# 从项目根目录检查内置规则系统
pwsh .tianming/scripts/reference-linter.ps1 -SkillPath .tianming

# 从 .tianming 目录内检查
pwsh .tianming/scripts/reference-linter.ps1

# 输出 JSON 报告
pwsh .tianming/scripts/reference-linter.ps1 -SkillPath .tianming -Json | Out-File lint-report.json
```

退出码 `0` = 通过；`1` = 发现问题。

### 冲突值量化

```bash
# 交互式输入
python3 .tianming/scripts/conflict-score.py

# 跑内置示例
python3 .tianming/scripts/conflict-score.py --demo

# 从 JSON 输入 + 输出 JSON
python3 .tianming/scripts/conflict-score.py --json input.json --output json
```

依赖：Python 3.7+，无第三方依赖。

---

## 六、故障排查

### 系统报告 `FATAL_ERROR: Blueprint_Mismatch`

**原因**：`「天命：正文」` 或 `「天命：草案」` 指令的章序，在《世界基石.md》的【战术执行目录】中找不到对应条目。

**解决**：

1. 先执行 `「天命：目录」` 生成该章的目录条目
2. 或检查指令中卷号/章号是否正确

### 系统报告 `FATAL_ERROR: Causality_Chain_Broken`

**原因**：当前章节要发生的重大事件，在前文找不到逻辑先导。

**解决**：

1. 回到目录协议，在前面章节补充铺垫
2. 或修改当前章节的核心事件，使其能从前文推导

### 系统报告 `FATAL_ERROR: Temporal_Anomaly_Detected`

**原因**：草稿中出现了不属于当前时代的实体，例如卷一出现卷三才该出现的角色。

**解决**：

1. 检查《档案事件.md》中该实体的时间锚点是否正确
2. 或在目录协议阶段拒绝该实体的提前出现

### 系统报告 `FATAL_ERROR: Singularity_Quota_Exceeded`

**原因**：本卷的「奇点事件」使用次数已超过 `.tianming/constants/global-constants.md` 中的配额。

**解决**：

1. 不允许在本卷再使用「奇点事件」标记
2. 或修改 `.tianming/constants/global-constants.md` 中的配额，不推荐

### 输出字数始终低于下限

**原因**：正文渲染触发了最高优先级扩写，但仍未达标。

**解决**：

1. 检查《文风样本.md》是否提供了足够多的高密度样本
2. 检查目录中该章的【核心事件】是否过于贫瘠

---

## 七、版本与维护

- **基础版本**：基于 2025 年初版「天命提示词.md」（995 行）拆分而成
- **拆分日期**：2026 年
- **模板化重构**：2026 年，将独立 Skill 包改为新书项目内置 `.tianming/` 结构
- **维护策略**：
  - 协议层（`.tianming/protocols/`、`.tianming/codex/`、`.tianming/aesthetic/`）按 semver 独立迭代
  - 常数层（`.tianming/constants/`）变更必须触发会话重启
  - 知识库模板层（`.tianming/kb-templates/`）更新不影响已使用的真实知识库

---

## 八、致谢与版权

本系统的设计哲学来源于 2025 年的「天命」长 Prompt 系统。
所有核心法典、协议、戒律均保留原作者意图，仅做结构化重组、引用规范化与内置模板化改造。

> **商用须知**：本项目基于 CC BY-NC-SA 4.0 协议开源，禁止未经授权的商业用途（包括但不限于二次包装售卖、商业 SaaS 部署、嵌入付费产品等）。任何商业用途请先联系原作者获得授权。
>
> 联系方式：子夜（QQ：229164036）

---

## 致谢

感谢真诚、友善、团结、专业的 Linuxdo 社区，让我学到了那么多有关 AI 相关知识。

[![LinuxDo community](https://img.shields.io/badge/LinuxDo-community-blue)](https://linux.do/)

- [LinuxDo](https://linux.do/) 学 ai, 上 L 站!
