#!/usr/bin/env bash
set -euo pipefail

fail() {
  echo "FAIL: $1" >&2
  exit 1
}

require_text() {
  local file="$1"
  local text="$2"
  local message="$3"
  grep -Fq "$text" "$file" || fail "$message"
}

[[ -f ".tianming/SKILL.md" ]] || fail "missing .tianming/SKILL.md"
[[ ! -f "SKILL.md" ]] || fail "root SKILL.md should have moved into .tianming/"
[[ -f "AGENTS.md" ]] || fail "missing root AGENTS.md"
require_text AGENTS.md ".tianming/SKILL.md" "AGENTS.md must require .tianming/SKILL.md"
require_text README.md ".tianming/" "README.md must document the embedded .tianming directory"
require_text AGENTS.md "/tianming setup" "AGENTS.md must document /tianming setup"
require_text README.md "/tianming setup" "README.md must document /tianming setup"
require_text .tianming/SKILL.md "/tianming setup" ".tianming/SKILL.md must route /tianming setup"
require_text AGENTS.md "5 个开书问题" "AGENTS.md must require 5 setup questions"
require_text README.md "5 个开书问题" "README.md must document 5 setup questions"
require_text .tianming/SKILL.md "5 个开书问题" ".tianming/SKILL.md must require 5 setup questions"
require_text AGENTS.md "第一版知识库" "AGENTS.md must require first-version knowledge base generation"
require_text README.md "第一版知识库" "README.md must document first-version knowledge base generation"
require_text .tianming/SKILL.md "第一版知识库" ".tianming/SKILL.md must require first-version knowledge base generation"
for question in "类型与读者承诺" "一句话卖点" "主角与欲望" "世界规则与金手指" "篇幅、风格与雷区"; do
  require_text .tianming/SKILL.md "$question" ".tianming/SKILL.md must list setup question: $question"
  require_text README.md "$question" "README.md must list setup question: $question"
done
require_text .tianming/SKILL.md "先校验书名和目标目录" ".tianming/SKILL.md must validate directory before interview"
require_text AGENTS.md "先校验书名和目标目录" "AGENTS.md must validate directory before interview"
require_text README.md "先校验书名和目标目录" "README.md must validate directory before interview"
require_text .tianming/SKILL.md "同一条消息中完整回答" ".tianming/SKILL.md must allow complete same-message answers"
require_text AGENTS.md "同一条消息中完整回答" "AGENTS.md must align same-message answer behavior"
require_text .tianming/SKILL.md "创建或修复项目根 AGENTS.md" ".tianming/SKILL.md must ensure project-root AGENTS.md"
require_text AGENTS.md "创建或修复项目根 AGENTS.md" "AGENTS.md must ensure project-root AGENTS.md"
require_text README.md "创建或修复项目根 AGENTS.md" "README.md must document project-root AGENTS.md repair"
! grep -Fq "tianming-skill/" README.md || fail "README.md still documents the old standalone loading workflow"
[[ -f ".tianming/scripts/reference-linter.ps1" ]] || fail "missing embedded reference linter"
[[ -f ".tianming/kb-templates/world-stone.template.md" ]] || fail "missing embedded knowledge-base templates"
[[ ! -f "世界基石.md" ]] || fail "root 世界基石.md belongs inside a generated book directory"
[[ ! -f "世界观规则.md" ]] || fail "root 世界观规则.md belongs inside a generated book directory"
[[ ! -f "角色档案.md" ]] || fail "root 角色档案.md belongs inside a generated book directory"
[[ ! -f "档案事件.md" ]] || fail "root 档案事件.md belongs inside a generated book directory"
[[ ! -f "文风样本.md" ]] || fail "root 文风样本.md belongs inside a generated book directory"

echo "embedded layout ok"
