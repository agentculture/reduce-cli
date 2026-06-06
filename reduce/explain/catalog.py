"""Markdown catalog for ``reduce-cli explain <path>``.

Each entry is verbatim markdown. Keys are command-path tuples. The empty tuple
and ``("reduce-cli",)`` both resolve to the root entry.

Keep bodies self-contained: an agent reading one entry should get enough
context without chaining reads.
"""

from __future__ import annotations

_ROOT = """\
# reduce-cli

A clonable template for AgentCulture mesh agents. It carries an agent-first CLI
(cited from the teken `python-cli` reference), a mesh identity (`culture.yaml` +
`CLAUDE.md`), the canonical guildmaster skill kit under `.claude/skills/`, and a
buildable/deployable package baseline. Clone it, rename the package, edit
`culture.yaml`, and you have a new agent.

## Verbs

- `reduce-cli whoami` — identity probe from `culture.yaml`.
- `reduce-cli learn` — structured self-teaching prompt.
- `reduce-cli explain <path>` — markdown docs for any noun/verb.
- `reduce-cli overview` — descriptive snapshot of the agent.
- `reduce-cli doctor` — check the agent-identity invariants.
- `reduce-cli cli overview` — describe the CLI surface.

## Exit-code policy

- `0` success
- `1` user-input error
- `2` environment / setup error
- `3+` reserved

## See also

- `reduce-cli explain whoami`
- `reduce-cli explain doctor`
"""

_WHOAMI = """\
# reduce-cli whoami

Reports the agent's identity from `culture.yaml`: nick (`suffix`), backend,
served model, and the package version. Read-only.

## Usage

    reduce-cli whoami
    reduce-cli whoami --json
"""

_LEARN = """\
# reduce-cli learn

Prints a structured self-teaching prompt covering purpose, command map,
exit-code policy, `--json` support, and the `explain` pointer.

## Usage

    reduce-cli learn
    reduce-cli learn --json
"""

_EXPLAIN = """\
# reduce-cli explain <path>

Prints markdown documentation for any noun/verb path. Unlike `--help` (terse,
positional), `explain` is global and addressable by path.

## Usage

    reduce-cli explain reduce-cli
    reduce-cli explain whoami
    reduce-cli explain --json <path>
"""

_OVERVIEW = """\
# reduce-cli overview

Read-only descriptive snapshot of the agent: identity (from `culture.yaml`), the
verb surface, and the sibling-pattern artifacts the template carries. Accepts an
ignored `target` so a stray path never hard-fails.

## Usage

    reduce-cli overview
    reduce-cli overview --json
"""

_DOCTOR = """\
# reduce-cli doctor

Checks the agent-identity invariants `steward doctor` verifies:
prompt-file-present and backend-consistency (`claude` → `CLAUDE.md`), plus a
skills-present check. Exits 1 when unhealthy.

## Usage

    reduce-cli doctor
    reduce-cli doctor --json
"""

_CLI = """\
# reduce-cli cli

Noun group for CLI-surface introspection. `cli overview` describes the CLI
itself (distinct from the global `overview`, which describes the agent).

## Usage

    reduce-cli cli overview
    reduce-cli cli overview --json
"""


ENTRIES: dict[tuple[str, ...], str] = {
    (): _ROOT,
    ("reduce-cli",): _ROOT,
    ("whoami",): _WHOAMI,
    ("learn",): _LEARN,
    ("explain",): _EXPLAIN,
    ("overview",): _OVERVIEW,
    ("doctor",): _DOCTOR,
    ("cli",): _CLI,
    ("cli", "overview"): _CLI,
}
