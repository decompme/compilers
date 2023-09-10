# decomp.me compilers

This repository contains the build instructions for all the compilers that are used on decomp.me.

There is a GitHub Action which will "build" each compiler and upload it to the GitHub Container Registry (ghcr.io).

When decomp.me is deployed it will fetch each compiler image from the registry.

## (re-)Generating Dockerfiles from jinja templates

Due to the large amount of shared steps, the Dockerfiles are driven from jinja templates.
The values that are used to populate the templates are found in values.yaml.

Rather than modifying the Dockerfiles directly, the `.j2` template should be changed and the Dockerfiles regenerated.

```sh
python3 -m pip install Jinja2
python3 template.py
```

## Notes:

- Docker image names must be lowercase therefore compiler ids will be lowercase'd before being uploaded.
- `+` is not a valid character for Docker image names, therefore `+` will be replaced with `_` in image names before being uploaded.
