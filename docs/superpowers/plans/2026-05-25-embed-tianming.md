# Embed Tianming Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert this standalone Tianming Skill repository into a dual-purpose new-book template with embedded rules under `.tianming/`.

**Architecture:** The project root becomes the book workspace and agent entrypoint. `.tianming/` contains the complete rule system and remains internally self-contained through relative paths.

**Tech Stack:** Markdown documentation, shell validation, PowerShell reference linter, Python utility script.

---

### Task 1: Add Structure Validation

**Files:**
- Create: `tests/validate-embedded-layout.sh`

- [ ] **Step 1: Write the failing validation script**

```bash
#!/usr/bin/env bash
set -euo pipefail

fail() {
  echo "FAIL: $1" >&2
  exit 1
}

[[ -f ".tianming/SKILL.md" ]] || fail "missing .tianming/SKILL.md"
[[ ! -f "SKILL.md" ]] || fail "root SKILL.md should have moved into .tianming/"
[[ -f "AGENTS.md" ]] || fail "missing root AGENTS.md"
grep -Fq ".tianming/SKILL.md" AGENTS.md || fail "AGENTS.md must require .tianming/SKILL.md"
grep -Fq ".tianming/" README.md || fail "README.md must document the embedded .tianming directory"
! grep -Fq "tianming-skill/" README.md || fail "README.md still documents the old standalone loading workflow"
[[ -f ".tianming/scripts/reference-linter.ps1" ]] || fail "missing embedded reference linter"
[[ -f ".tianming/kb-templates/world-stone.template.md" ]] || fail "missing embedded knowledge-base templates"
[[ -f "世界基石.md" ]] || fail "missing root 世界基石.md"
[[ -f "世界观规则.md" ]] || fail "missing root 世界观规则.md"
[[ -f "角色档案.md" ]] || fail "missing root 角色档案.md"
[[ -f "档案事件.md" ]] || fail "missing root 档案事件.md"
[[ -f "文风样本.md" ]] || fail "missing root 文风样本.md"

echo "embedded layout ok"
```

- [ ] **Step 2: Run validation to verify it fails before migration**

Run: `bash tests/validate-embedded-layout.sh`

Expected: FAIL because `.tianming/SKILL.md` does not exist yet.

### Task 2: Move Tianming Rules Into `.tianming/`

**Files:**
- Move: `SKILL.md` to `.tianming/SKILL.md`
- Move: `core/` to `.tianming/core/`
- Move: `codex/` to `.tianming/codex/`
- Move: `protocols/` to `.tianming/protocols/`
- Move: `aesthetic/` to `.tianming/aesthetic/`
- Move: `constants/` to `.tianming/constants/`
- Move: `kb-templates/` to `.tianming/kb-templates/`
- Move: `scripts/` to `.tianming/scripts/`

- [ ] **Step 1: Create `.tianming/` and move rule assets**

Run:

```bash
mkdir -p .tianming
mv SKILL.md core codex protocols aesthetic constants kb-templates scripts .tianming/
```

- [ ] **Step 2: Verify moved files exist**

Run: `test -f .tianming/SKILL.md && test -f .tianming/protocols/main-body.md && test -f .tianming/scripts/conflict-score.py`

Expected: exit code 0.

### Task 3: Add Agent Entrypoint

**Files:**
- Create: `AGENTS.md`
- Create: `世界基石.md`
- Create: `世界观规则.md`
- Create: `角色档案.md`
- Create: `档案事件.md`
- Create: `文风样本.md`

- [ ] **Step 1: Write root agent contract**

Create `AGENTS.md` with instructions that require agents to read `.tianming/SKILL.md`, treat `.tianming/` as the embedded rule system, prioritize root knowledge-base files, and refuse invented facts.

- [ ] **Step 2: Verify required reference**

Run: `grep -F ".tianming/SKILL.md" AGENTS.md`

Expected: the command prints the required path.

- [ ] **Step 3: Create editable root knowledge-base starters**

Run:

```bash
cp .tianming/kb-templates/world-stone.template.md 世界基石.md
cp .tianming/kb-templates/world-rules.template.md 世界观规则.md
cp .tianming/kb-templates/character-archive.template.md 角色档案.md
cp .tianming/kb-templates/archive-events.template.md 档案事件.md
cp .tianming/kb-templates/style-sample.template.md 文风样本.md
```

Expected: the five knowledge-base files exist at the project root.

### Task 4: Update Embedded Skill Docs

**Files:**
- Modify: `.tianming/SKILL.md`
- Modify: `.tianming/scripts/reference-linter.ps1`
- Modify: `examples/mini-volume/README.md`

- [ ] **Step 1: Replace standalone tree names**

Update references from `tianming-skill/` to `.tianming/` where they describe the rule system location.

- [ ] **Step 2: Update examples for embedded workflow**

Update example instructions so they tell users to start from the project root and let agents read `AGENTS.md`.

### Task 5: Rewrite README For New-Book Template Use

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Replace standalone Skill quick start**

Rewrite the README around copying the repository as a new-book project, filling root knowledge-base files, and using `.tianming/` as embedded rules.

- [ ] **Step 2: Keep command workflow and copyright notices**

Preserve the Tianming command list, glossary, troubleshooting, version notes, license, and contact information.

### Task 6: Verify Migration

**Files:**
- Test: `tests/validate-embedded-layout.sh`
- Test: `.tianming/scripts/reference-linter.ps1`
- Test: `scripts/conflict-score.py` equivalent at `.tianming/scripts/conflict-score.py`

- [ ] **Step 1: Run embedded layout validation**

Run: `bash tests/validate-embedded-layout.sh`

Expected: `embedded layout ok`.

- [ ] **Step 2: Run conflict-score demo from embedded path**

Run: `python3 .tianming/scripts/conflict-score.py --demo`

Expected: exit code 0 and demo output.

- [ ] **Step 3: Run reference linter if PowerShell is available**

Run: `pwsh .tianming/scripts/reference-linter.ps1 -SkillPath .tianming`

Expected: exit code 0, or document that `pwsh` is unavailable.
