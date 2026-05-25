# Tianming Mother Project Design

## Goal

Restructure the repository into a Tianming mother project. The repository root holds `AGENTS.md` and `.tianming/`; each book is created as a separate root child directory through the protocol command `/tianming setup [book-name]`.

## Target Model

The repository root is not itself a book knowledge base. It is the shared workspace that contains:

- `AGENTS.md`
- `README.md`
- `.tianming/`
- `examples/`
- `tests/`
- zero or more generated book directories

The embedded Tianming system lives under `.tianming/`:

- `.tianming/SKILL.md`
- `.tianming/core/`
- `.tianming/codex/`
- `.tianming/protocols/`
- `.tianming/aesthetic/`
- `.tianming/constants/`
- `.tianming/kb-templates/`
- `.tianming/scripts/`

Generated book directories contain only book-facing knowledge files:

- `README.md`
- `世界基石.md`
- `世界观规则.md`
- `角色档案.md`
- `档案事件.md`
- `文风样本.md`

## Protocol Command

`/tianming setup [book-name]` is the official setup command. It is a protocol-level command, not a script dependency.

When an AI agent receives the command, it must:

1. Validate that `[book-name]` is a single safe directory name.
2. Reject path traversal, nested paths, hidden directories, and reserved names.
3. Refuse to overwrite an existing non-empty directory.
4. Create `[book-name]/`.
5. Copy the five knowledge-base templates from `.tianming/kb-templates/` into `[book-name]/` using the Chinese production filenames.
6. Generate `[book-name]/README.md`.
7. Treat `[book-name]/` as the active book directory for the current session.

## Agent Contract

`AGENTS.md` must require every AI agent to:

- Read and obey `.tianming/SKILL.md`.
- Treat `.tianming/` as the shared rule system.
- Treat generated book directories as story knowledge bases.
- Use `/tianming setup [book-name]` to create new book directories.
- Read story facts from the active book directory, not from `.tianming/`.
- Avoid guessing when multiple candidate book directories exist.
- Refuse to invent missing knowledge-base facts.

## Verification

`tests/validate-embedded-layout.sh` verifies:

- `.tianming/SKILL.md` exists.
- Root `SKILL.md` does not exist.
- Root `AGENTS.md` exists and references `.tianming/SKILL.md`.
- `AGENTS.md`, `README.md`, and `.tianming/SKILL.md` document `/tianming setup`.
- `.tianming/scripts/reference-linter.ps1` exists.
- `.tianming/kb-templates/world-stone.template.md` exists.
- Root-level production knowledge-base files do not exist; they belong inside generated book directories.
