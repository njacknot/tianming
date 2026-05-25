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
grep -Fq "/tianming setup" AGENTS.md || fail "AGENTS.md must document /tianming setup"
grep -Fq "/tianming setup" README.md || fail "README.md must document /tianming setup"
grep -Fq "/tianming setup" .tianming/SKILL.md || fail ".tianming/SKILL.md must route /tianming setup"
! grep -Fq "tianming-skill/" README.md || fail "README.md still documents the old standalone loading workflow"
[[ -f ".tianming/scripts/reference-linter.ps1" ]] || fail "missing embedded reference linter"
[[ -f ".tianming/kb-templates/world-stone.template.md" ]] || fail "missing embedded knowledge-base templates"
[[ ! -f "世界基石.md" ]] || fail "root 世界基石.md belongs inside a generated book directory"
[[ ! -f "世界观规则.md" ]] || fail "root 世界观规则.md belongs inside a generated book directory"
[[ ! -f "角色档案.md" ]] || fail "root 角色档案.md belongs inside a generated book directory"
[[ ! -f "档案事件.md" ]] || fail "root 档案事件.md belongs inside a generated book directory"
[[ ! -f "文风样本.md" ]] || fail "root 文风样本.md belongs inside a generated book directory"

echo "embedded layout ok"
