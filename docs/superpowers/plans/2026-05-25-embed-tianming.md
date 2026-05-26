# Tianming Mother Project Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the repository into a Tianming mother project where `/tianming setup [book-name]` creates new book directories.

**Architecture:** The root contains the shared agent contract and embedded `.tianming/` rules. Book knowledge bases live in generated child directories.

**Tech Stack:** Markdown documentation and shell validation.

---

### Task 1: Validate Mother Project Layout

**Files:**
- Modify: `tests/validate-embedded-layout.sh`

- [ ] Require `.tianming/SKILL.md`, `AGENTS.md`, and `.tianming/kb-templates/world-stone.template.md`.
- [ ] Require `/tianming setup` to appear in `AGENTS.md`, `README.md`, and `.tianming/SKILL.md`.
- [ ] Require `5 个开书问题` and `第一版知识库` to appear in `AGENTS.md`, `README.md`, and `.tianming/SKILL.md`.
- [ ] Require directory validation before interview and project-root `AGENTS.md` repair rules.
- [ ] Reject root-level `世界基石.md`, `世界观规则.md`, `角色档案.md`, `档案事件.md`, and `文风样本.md`.
- [ ] Run `bash tests/validate-embedded-layout.sh` and expect it to pass.

### Task 2: Add Protocol Setup Command

**Files:**
- Modify: `.tianming/SKILL.md`
- Modify: `AGENTS.md`

- [ ] Add `/tianming setup [书名]` to the command router.
- [ ] Define setup validation rules for safe single-level directory names.
- [ ] Require setup to create or repair project-root `AGENTS.md`.
- [ ] Require setup to ask 5 setup questions before creating files unless the user already answered all five in the same message.
- [ ] Define first-version knowledge base quality requirements and template mappings.
- [ ] Define active book directory behavior.

### Task 3: Update User Documentation

**Files:**
- Modify: `README.md`

- [ ] Describe the repository as a Tianming mother project.
- [ ] Document `git clone`, `cd tianming`, and `/tianming setup 我的新书`.
- [ ] Document the 5 setup questions and first-version knowledge base flow.
- [ ] Show the generated book directory structure.
- [ ] Remove instructions that put the five production knowledge-base files at the repository root.

### Task 4: Verify

**Commands:**

```bash
bash tests/validate-embedded-layout.sh
bash -n tests/validate-embedded-layout.sh
python3 .tianming/scripts/conflict-score.py --demo
git diff --check
```

If PowerShell is available:

```powershell
pwsh .tianming/scripts/reference-linter.ps1 -SkillPath .tianming
```
