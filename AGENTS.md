# Repository guidance

Read README.md for repository context and setup.

- Compiler definitions live in `values.yaml`; Dockerfile templates live in `templates/`.
- Do not edit `platforms/**/Dockerfile` directly. Change the YAML or Jinja templates, then run `uv run template.py` from the repo root.
- Include regenerated Dockerfiles with the source changes.
- Shared templates affect multiple compilers; inspect the full diff for unintended changes.
- Follow nearby compiler entries when adding a compiler, including platform, template, and optional arch conventions.
- For changes to image naming or build selection, inspect `matrix.py` and `.github/workflows/ci.yaml`.
- Report validation performed and any checks you could not run.
