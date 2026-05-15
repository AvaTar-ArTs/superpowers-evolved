# References — Cross-Platform Tool Mappings

Maintained from `~/.qwen/skills/superpowers-using-superpowers/references/`.

## Claude Code (Anthropic)

| Capability | Tool |
|-----------|------|
| Read files | `Read` |
| Write files | `Write` |
| Edit files | `Edit` |
| Run commands | `Bash` |
| Search code | `Grep`, `Glob` |
| Web fetch | `WebFetch`, `WebSearch` |
| Spawn agent | `Task` |
| List files | `LS` |
| Skills | `/skills:name` or extension UI |

## Cursor

| Capability | Tool |
|-----------|------|
| Read files | `read_file` |
| Write files | `write_to_file` |
| Edit files | `replace_in_file` |
| Search | `codebase_search`, `grep_search` |
| Run commands | `run_terminal_command` |
| Skills | `/skills:name` via extension |

## Gemini (Google)

| Capability | Tool |
|-----------|------|
| Read files | `read_file` |
| Write files | `write_file` |
| Search | `search_codebase` |
| Run commands | `run_command` |
| Skills | Extension `.gemini-extension.json` |

## Codex (OpenAI)

| Capability | Tool |
|-----------|------|
| Filesystem | `read`, `write`, `edit`, `glob`, `grep` |
| Shell | `bash` |
| Web | `web_fetch`, `web_search` |
| Skills | Loaded via `superpowers` symlink |

## Cline

| Capability | Tool |
|-----------|------|
| Filesystem | `read_files`, `editor`, `search_codebase` |
| Shell | `run_commands` |
| Web | `fetch_web_content` |
| Agent teams | `spawn_agent`, `team_*` tools |
| Skills | `skills` tool with SKILL.md format |
