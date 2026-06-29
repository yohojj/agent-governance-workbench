# Release Gates

A public release must pass these gates:

1. Clean-room gate: no original private repository history.
2. File inventory gate: only intended files are present.
3. Secret gate: no token, password, key, or secret-like value.
4. Personal-data gate: no private names, paths, logs, or task histories.
5. License gate: only content the maintainer has the right to publish.
6. Asset gate: public images under `docs/assets/` must use synthetic data only and receive visual review.
7. Review gate: independent reviewer returns PASS.
8. Approval gate: human approver explicitly approves the release.
