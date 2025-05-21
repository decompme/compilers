#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "jinja2",
#     "pyyaml",
# ]
# ///
import argparse
from pathlib import Path

import yaml

from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        type=Path,
        nargs="?",
        default=Path("values.yaml"),
        help="Configuration file, e.g. `values.yaml`",
    )
    parser.add_argument(
        "--template-dir",
        "--templates-dir",
        type=Path,
        default=Path("templates"),
        help="Directory to find templates",
    )
    parser.add_argument(
        "--base-path",
        "--dockerfile-path",
        type=Path,
        default=Path("platforms"),
        help="Directory to save templated Dockerfiles",
    )
    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader(args.template_dir), autoescape=select_autoescape()
    )

    with args.filename.open("r") as f:
        values = yaml.safe_load(f)
    for compiler in values.get("compilers", []):
        if "arch" in compiler:
            target_path = (
                args.base_path
                / compiler["platform"]
                / compiler["id"]
                / compiler["arch"]
                / "Dockerfile"
            )
        else:
            target_path = (
                args.base_path / compiler["platform"] / compiler["id"] / "Dockerfile"
            )

        print(
            f"{compiler['id']}: Creating {target_path} from {compiler['template']}.j2"
        )

        template_path = compiler["template"]
        template = env.get_template(f"{template_path}.j2")
        rendered = template.render(compiler)

        target_path.parent.mkdir(parents=True, exist_ok=True)
        with target_path.open("w") as f:
            f.write(
                "# NOTE: This file is generated automatically via template.py. Do not edit manually!\n\n"
            )
            f.write("\n")
            f.write(rendered)
            f.write("\n")  # enforce trailing newline


if __name__ == "__main__":
    main()
