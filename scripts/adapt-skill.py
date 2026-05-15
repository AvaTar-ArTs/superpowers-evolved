#!/usr/bin/env python3
"""Adapt a SKILL.md from Claude Code / generic format to Cline-native format.

Usage:
  python adapt-skill.py path/to/SKILL.md                    # print to stdout
  python adapt-skill.py path/to/SKILL.md -o adapted.md      # write to file
  python adapt-skill.py path/to/skills/ --batch              # adapt all SKILL.md in dir
"""

import argparse, json, re, sys
from pathlib import Path

TOOL_MAP: dict[str, str] = {
    "Read": "read_files",
    "Write": "editor",
    "Edit": "editor",
    "Bash": "run_commands",
    "Grep": "search_codebase",
    "Glob": "search_codebase",
    "Task": "spawn_agent",
    "Skill": "skills",
    "WebFetch": "fetch_web_content",
    "WebSearch": "fetch_web_content",
    "LS": "run_commands",
}

PATH_MAP: dict[str, str] = {
    "~/.claude": "~/.cline",
    ".claude-plugin": ".cline/skills",
    "CLAUDE.md": "CLINE.md",
    "claude-code": "cline",
    "Claude Code": "Cline",
}

PHRASE_MAP: list[tuple[str, str]] = [
    ("Claude Skill tool", "Cline skills tool"),
    ("Claude Code", "Cline"),
    ("Claude instance", "Cline agent"),
    ("Task tool", "spawn_agent tool"),
    ("Bash tool", "run_commands tool"),
    ("Read tool", "read_files tool"),
    ("Write tool", "editor tool"),
    ("Edit tool", "editor tool"),
    ("Grep tool", "search_codebase tool"),
    ("Glob tool", "search_codebase tool"),
    ("WebFetch", "fetch_web_content"),
    ("WebSearch", "fetch_web_content"),
    ("activate via the Claude", "activate via the Cline"),
    ("in Claude", "in Cline"),
    ("for Claude", "for Cline"),
    ("another Claude", "another Cline agent"),
    ("to Claude", "to Cline"),
    ("Claude's", "Cline's"),
    ("CLAUDE_PLUGIN_ROOT", "CLINE_SKILL_ROOT"),
    (".claude-plugin/plugin.json", ".cline/skills/manifest.json"),
    (".claude-plugin", ".cline/skills"),
    ("/skills:", "skills tool with skill:"),
]


def adapt(text: str) -> str:
    """Return *text* with Claude Code references swapped for Cline."""
    for old, new in PHRASE_MAP:
        text = text.replace(old, new)
    return text


def process_file(path: Path, output: Path | None = None) -> str:
    """Adapt one SKILL.md. Return adapted text."""
    original = path.read_text(encoding="utf-8")
    adapted = adapt(original)

    # Add adaptation banner if not already present
    if "Adapted for Cline" not in adapted:
        banner = (
            "<!-- Adapted for Cline — "
            "original Claude Code references mapped to Cline equivalents. "
            "See references/cline-tools.md for the full mapping. -->\n"
        )
        # Insert after frontmatter if present
        if adapted.startswith("---"):
            parts = adapted.split("---", 2)
            if len(parts) >= 3:
                adapted = f"---{parts[1]}---\n{banner}---{parts[2]}"
            else:
                adapted = banner + adapted
        else:
            adapted = banner + adapted

    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(adapted, encoding="utf-8")

    return adapted


def main() -> None:
    p = argparse.ArgumentParser(description="Adapt SKILL.md from Claude Code to Cline")
    p.add_argument("path", help="SKILL.md file or directory of skills")
    p.add_argument("-o", "--output", help="Output file or directory (default: stdout)")
    p.add_argument("--batch", action="store_true", help="Process all SKILL.md in directory")
    args = p.parse_args()

    src = Path(args.path)

    if args.batch or src.is_dir():
        skill_files = list(src.rglob("SKILL.md"))
        if not skill_files:
            print(f"No SKILL.md files found in {src}", file=sys.stderr)
            sys.exit(1)
        out_dir = Path(args.output) if args.output else src.parent / "adapted"
        for sf in skill_files:
            rel = sf.relative_to(src)
            out = out_dir / rel
            process_file(sf, out)
            print(f"  ✓ {rel}")
        print(f"\n{len(skill_files)} skills adapted → {out_dir}")
    else:
        adapted = process_file(src, Path(args.output) if args.output else None)
        if not args.output:
            print(adapted)
        else:
            print(f"  ✓ {args.output}")


if __name__ == "__main__":
    main()
