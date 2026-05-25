## 交流群

- [点击链接加入群聊【天命-智能创作（BUG收集）】](https://qm.qq.com/q/YWivpFjKou)

群号：414086347

> ## 寻找软件版？
>
> 如果你更喜欢开箱即用的桌面应用体验，请移步：[天命-智能小说创作软件](https://github.com/zy-zmc/tianming-novel-ai-writer)
>
> 无需任何提示词知识，下载即用，内置完整天命系统。

---

# 天命 · 小说母项目

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

> **TianMing** 是一个可拉到本地后持续开书的小说母项目。
> 根目录保存 `AGENTS.md` 和 `.tianming/` 规则系统；每本新书通过 `/tianming setup 书名` 生成独立目录。

---

## 一、这个项目是什么

「天命」是一个为长篇小说创作而设计的结构化 AI 协同写作系统。

- **执笔者（用户）** 负责创意、世界观、人物烙印、文风样本
- **天命（系统）** 负责保证跨章节的世界观一致性、伏笔回收、节奏控制、文风稳定

本仓库现在采用“母项目 + 多新书目录”结构：

- 根目录用于存放 `AGENTS.md`、`.tianming/` 和多个新书目录
- `.tianming/` 存放完整天命规则、协议、模板和维护脚本
- 新书目录只存小说知识库，不复制 `.tianming/`
- AI AGENTS 进入项目后必须先读 `AGENTS.md`，再按 `.tianming/SKILL.md` 的规则执行

---

## 二、快速开始

### 1. 拉到本地

```bash
git clone git@github.com:njacknot/tianming.git
cd tianming
```

### 2. 用协议式命令一键开书

在 AI 会话中输入：

```text
/tianming setup 我的新书
```

AI AGENT 必须按 `AGENTS.md` 与 `.tianming/SKILL.md` 的开书协议，在根目录生成：

```text
我的新书/
├── README.md
├── 世界基石.md
├── 世界观规则.md
├── 角色档案.md
├── 档案事件.md
└── 文风样本.md
```

### 3. 填写新书知识库

先填写：

- `我的新书/世界观规则.md`
- `我的新书/角色档案.md`
- `我的新书/文风样本.md`

可按需要填写：

- `我的新书/档案事件.md`

`我的新书/世界基石.md` 是动态核心，通常由 `「天命：大纲」`、`「天命：规划」`、`「天命：目录」`、`「天命：存档」` 逐步维护。

### 4. 初始化

开书并填写基础知识库后，在 AI 会话中输入：

```text
初始化
```

系统会执行 `.tianming/core/boot-sequence.md` 的启动规则，检查协议绑定状态与当前新书目录的知识库连接状态。

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
| 7 | `「天命：体检」` | 当前新书《世界基石.md》健康报告 |
| 8 | `「天命：存档」` | 结构化更新补丁 |

---

## 三、目录结构

```text
tianming/
├── AGENTS.md                         ← AI AGENTS 入口规则
├── README.md                         ← 本文件
├── LICENSE
│
├── .tianming/                        ← 内置天命规则系统
│   ├── SKILL.md                      ← 主入口（路由表 + 开书协议 + 启动清单）
│   ├── core/                         ← 系统内核
│   ├── codex/                        ← 绝对法典
│   ├── protocols/                    ← 运行协议
│   ├── aesthetic/                    ← 天书铁律
│   ├── constants/                    ← 全局常数
│   ├── kb-templates/                 ← 新书知识库模板
│   └── scripts/                      ← 维护工具脚本
│
├── 我的新书/                         ← 由 /tianming setup 生成
│   ├── README.md
│   ├── 世界基石.md
│   ├── 世界观规则.md
│   ├── 角色档案.md
│   ├── 档案事件.md
│   └── 文风样本.md
│
├── examples/
│   └── mini-volume/                  ← 5 章极简样例卷《镜中之约》
└── tests/
    └── validate-embedded-layout.sh   ← 母项目结构校验
```

---

## 四、协议式开书规则

`/tianming setup 书名` 是正式 Skill 命令，不依赖脚本。

AI AGENT 必须：

1. 校验 `书名` 是安全的单层目录名。
2. 禁止覆盖已有非空目录。
3. 从 `.tianming/kb-templates/` 读取模板。
4. 在 `书名/` 内生成五个知识库文件和 `README.md`。
5. 将 `书名/` 设为当前会话的【当前新书目录】。

如果同一母项目下有多本书，后续天命指令必须明确当前书名；不能自行猜测。

---

## 五、术语速查表

| 术语 | 含义 |
|---|---|
| **执笔者** | 你（用户） |
| **天命** | 系统本身 |
| **母项目** | 保存 `.tianming/`、`AGENTS.md` 和多个新书目录的根目录 |
| **当前新书目录** | 当前会话正在创作的某一本书目录 |
| **统一知识库核心** | 当前新书目录中的《世界基石.md》+ 四件静态基石 |
| **战略宏图** | 故事的最高纲领，由 `「天命：大纲」` 生成 |
| **战役总蓝图** | 全书的战略推演，由 `「天命：规划」` 生成 |
| **战术执行目录** | 详细章节目录，由 `「天命：目录」` 生成 |
| **显化蓝图草案** | 章节骨架，由 `「天命：草案」` 生成 |
| **精修初稿** | 4500-5500 字的预渲染稿，待打磨成最终成品 |

---

## 六、维护工具

### 母项目结构校验

```bash
bash tests/validate-embedded-layout.sh
```

退出码 `0` 表示母项目结构满足内置规则包与协议式开书要求。

### 引用完整性 Lint

```powershell
# 从母项目根目录检查内置规则系统
pwsh .tianming/scripts/reference-linter.ps1 -SkillPath .tianming

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

## 七、故障排查

### `/tianming setup` 报告目录已存在

**原因**：目标新书目录已存在且非空。

**解决**：换一个书名，或手动清理旧目录后重新执行。

### 初始化报告提示知识库缺失

**原因**：当前新书目录缺少五件知识库文件，或 AI 尚未确认当前新书目录。

**解决**：先执行 `/tianming setup 书名`，或明确告诉 AI 当前书名。

### 系统报告 `FATAL_ERROR: Blueprint_Mismatch`

**原因**：`「天命：正文」` 或 `「天命：草案」` 指令的章序，在当前新书《世界基石.md》的【战术执行目录】中找不到对应条目。

**解决**：

1. 先执行 `「天命：目录」` 生成该章的目录条目
2. 或检查指令中卷号/章号是否正确

---

## 八、版本与维护

- **基础版本**：基于 2025 年初版「天命提示词.md」（995 行）拆分而成
- **拆分日期**：2026 年
- **母项目重构**：2026 年，将独立 Skill 包改为 `.tianming/` 内置规则系统，并通过 `/tianming setup` 生成新书目录
- **维护策略**：
  - 协议层（`.tianming/protocols/`、`.tianming/codex/`、`.tianming/aesthetic/`）按 semver 独立迭代
  - 常数层（`.tianming/constants/`）变更必须触发会话重启
  - 知识库模板层（`.tianming/kb-templates/`）更新只影响之后新开的书

---

## 九、致谢与版权

本系统的设计哲学来源于 2025 年的「天命」长 Prompt 系统。
所有核心法典、协议、戒律均保留原作者意图，仅做结构化重组、引用规范化与母项目化改造。

> **商用须知**：本项目基于 CC BY-NC-SA 4.0 协议开源，禁止未经授权的商业用途（包括但不限于二次包装售卖、商业 SaaS 部署、嵌入付费产品等）。任何商业用途请先联系原作者获得授权。
>
> 联系方式：子夜（QQ：229164036）

---

## 致谢

感谢真诚、友善、团结、专业的 Linuxdo 社区，让我学到了那么多有关 AI 相关知识。

[![LinuxDo community](https://img.shields.io/badge/LinuxDo-community-blue)](https://linux.do/)

- [LinuxDo](https://linux.do/) 学 ai, 上 L 站!
