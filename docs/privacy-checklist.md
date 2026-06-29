# Privacy Checklist

Before publishing any adapted workbench:

- Use a clean-room directory.
- Do not copy private task history.
- Do not include local environment files.
- Do not include logs, notebooks, exports, or binary files unless reviewed.
- Keep public screenshots and social images under `docs/assets/`, use synthetic data only, and visually review them before release.
- Replace real teams, people, clients, projects, and paths with synthetic names.
- Run a secret scan.
- Run a personal-data scan.
- Review the staged file list before pushing.

## Blocking examples

- API keys or access tokens
- Local absolute paths
- Customer or personal data
- Private operational logs
- Internal task histories
- Unlicensed third-party content
