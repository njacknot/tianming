# Embed Tianming Design

## Goal

Restructure the repository into a dual-purpose new-book project template with the Tianming rule system embedded under `.tianming/`.

## Current State

The repository is currently shaped as a standalone Claude Skill package. `SKILL.md`, `core/`, `codex/`, `protocols/`, `aesthetic/`, `constants/`, `kb-templates/`, and `scripts/` all live at the repository root. The README tells users to place the whole `tianming-skill/` directory somewhere Claude can access.

## Target Structure

The repository root becomes the new-book project surface:

- `AGENTS.md` is the mandatory AI agent entrypoint.
- `README.md` explains how to use the repository as a new-book template.
- `LICENSE` remains at the root.
- The five root knowledge-base files are present as editable starter templates.
- `examples/mini-volume/` remains at the root as a runnable sample knowledge base.

The embedded Tianming system moves into `.tianming/`:

- `.tianming/SKILL.md`
- `.tianming/core/`
- `.tianming/codex/`
- `.tianming/protocols/`
- `.tianming/aesthetic/`
- `.tianming/constants/`
- `.tianming/kb-templates/`
- `.tianming/scripts/`

## Agent Contract

`AGENTS.md` must require every AI agent to:

- Read and obey `.tianming/SKILL.md` before responding to Tianming commands.
- Treat `.tianming/` as the embedded rule system, not as user story knowledge.
- Load protocols through the command router in `.tianming/SKILL.md`.
- Read the new-book knowledge base from the project root first.
- Use `.tianming/kb-templates/` only as missing-file templates.
- Refuse to invent missing knowledge base facts.
- Keep final creative outputs free of internal `[REF]`, `[VAR]`, and `[KERNEL_REF]` markers where the Tianming rules require clean output.

## Documentation Changes

The README should stop presenting this as only a standalone Skill package. It should explain the embedded workflow:

1. Copy this repository to create a new book project.
2. Fill the five knowledge-base files in the project root, using `.tianming/kb-templates/` as templates.
3. Start an AI session in the project root.
4. The agent reads `AGENTS.md`, then `.tianming/SKILL.md`.
5. The writer uses `初始化`, `「天命：大纲」`, `「天命：规划」`, `「天命：目录」`, `「天命：草案」`, `「天命：正文」`, `「天命：体检」`, and `「天命：存档」`.

## Compatibility

Internal relative links inside `.tianming/SKILL.md` can remain relative to `.tianming/`, because agents are instructed to resolve them from that directory. User knowledge-base lookup must prioritize the project root before `.tianming/kb-templates/`.

Scripts should remain usable from either `.tianming/` or the project root. The reference linter should document examples that point at `.tianming`.

## Verification

Add a local shell check at `tests/validate-embedded-layout.sh` that verifies:

- `.tianming/SKILL.md` exists.
- Root `SKILL.md` no longer exists.
- Root `AGENTS.md` exists and references `.tianming/SKILL.md`.
- `README.md` references `.tianming/` and does not instruct users to share `tianming-skill/`.
- `.tianming/scripts/reference-linter.ps1` exists.
- `.tianming/kb-templates/world-stone.template.md` exists.
- Root `世界基石.md`, `世界观规则.md`, `角色档案.md`, `档案事件.md`, and `文风样本.md` exist.
