# Issue Roadmap Drafts

These are draft GitHub issues for the public roadmap. Review labels and scope before creating them remotely.

## 1. Add dashboard preview GIF to README

Labels: `documentation`, `good first issue`

Acceptance criteria:

- GIF uses only bundled synthetic data.
- GIF is stored under `docs/assets/`.
- README embeds the preview near the dashboard section.
- No browser chrome, local paths, real people, or private task histories are visible.
- `python3 scripts/privacy_scan.py .` passes.

## 2. Add static dashboard screenshot fallback

Labels: `documentation`, `help wanted`

Acceptance criteria:

- A PNG fallback exists under `docs/assets/`.
- Screenshot uses only synthetic bundled data.
- README includes clear alt text.
- No local paths or private data are visible.
- `python3 scripts/privacy_scan.py .` passes.

## 3. Add Docker quick start

Labels: `enhancement`, `developer-experience`

Acceptance criteria:

- Dockerfile or Compose setup runs the Streamlit app locally.
- README includes concise Docker usage.
- The container does not require secrets or external APIs.
- Existing local quick start remains available.

## 4. Add stricter privacy scanner profile

Labels: `security`, `enhancement`

Acceptance criteria:

- Scanner can optionally flag local absolute paths, common private-directory names, binary files, and large exports.
- Current default scanner behavior remains usable for the clean demo repo.
- Documentation explains when to use the stricter profile.
- Tests or sample commands show expected pass and fail cases.

## 5. Add example governance packs

Labels: `examples`, `help wanted`

Acceptance criteria:

- At least one new synthetic governance pack is added for research, coding, or content workflows.
- All names, tasks, and evidence are fictional.
- README or docs explain how to adapt a pack safely.
- `python3 scripts/privacy_scan.py .` passes.

## 6. Export dashboard snapshot to static HTML

Labels: `enhancement`

Acceptance criteria:

- A documented local export path or script exists.
- Exported output excludes secrets, private paths, and real task histories.
- Release checklist documents how to review exported snapshots before publishing.
- The feature works without external APIs.
