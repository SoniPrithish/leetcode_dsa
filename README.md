# LeetCode DSA

Personal archive of accepted LeetCode submissions, kept in sync from my account.

## What this repository is

- **Solutions only**: source files for problems I solved and submitted on [LeetCode](https://leetcode.com).
- **Generated layout**: folders, indexes, and per-solution metadata files are produced by a small sync tool; I do not hand-maintain the full tree.
- **No full problem statements**: README snippets list title, number, difficulty, tags, language, and submission time—not copied statement text.

## Layout

| Path | Purpose |
| --- | --- |
| `solutions/` | Solutions grouped by primary topic (e.g. Arrays, Trees). |
| `solutions/README.md` | Master index of everything synced. |
| `solutions/<topic>/README.md` | Index for that topic (when topic indexes are enabled). |
| `notes/` | Optional short notes I write myself; merged into generated READMEs when present. |
| `.leetcode-sync/` | Local sync state (processed submission IDs, caches). Listed in `.gitignore` so it is not committed. |

Typical filenames look like `0001-two-sum.py` plus a small metadata file such as `0001-two-sum.python3.md`.

## How it stays updated

Sync runs from [`SoniPrithish/leetcode_github`](https://github.com/SoniPrithish/leetcode_github) (scheduler and manual workflow). That repo holds the tooling and config; **this** repo is the destination for written files and commits.

## License and reuse

This is personal practice code. If you fork or copy anything, you are responsible for complying with LeetCode’s terms and for not republishing restricted content.
