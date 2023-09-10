import argparse
import json
import yaml

from pathlib import Path


def parse_dockerfile_path(file_path):
    if not file_path.name == "Dockerfile":
        return None

    file_path_parts = file_path.parts
    if len(file_path_parts) == 4:
        # e.g. platforms/n64/ido6.0/Dockerfile
        _, platform, compiler_id, _ = file_path_parts
        return [platform, compiler_id, None]

    if len(file_path_parts) == 5:
        # e.g. platforms/n64/gcc2.7.2kmc/darwin/Dockerfile
        _, platform, compiler_id, arch, _ = file_path_parts
        return [platform, compiler_id, arch]

    raise Exception(f"We do not know how to handle this path: {file_path}")


def process_dockerfile(platform, compiler_id, arch, base_dir="platforms"):
    # image names must be lowercase and "+" is not a valid character
    clean_compiler_id = compiler_id.lower().replace("+", "plus")

    return dict(
        platform=platform,
        compiler_id=compiler_id,
        clean_compiler_id=clean_compiler_id,
        dockerfile=f"platforms/{platform}/{compiler_id}{'/' + arch if arch else ''}/Dockerfile",
        image=f"{platform}/{clean_compiler_id}{'/' + arch if arch else ''}",
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        type=argparse.FileType("r"),
        help="Configuration file, e.g. `values.yaml`",
    )
    parser.add_argument(
        "--dockerfiles",
        "--filepaths",
        type=argparse.FileType("r"),
        help="Path to file containing list of Dockerfiles to filter on, e.g. `--dockerfiles files.txt`",
    )
    parser.add_argument(
        "--platforms",
        type=str,
        nargs="+",
        help="List of platforms to filter on, e.g. `--platforms n64 ps2`",
    )
    args = parser.parse_args()

    values = yaml.safe_load(args.filename)

    local_dockerfiles = []
    for compiler in values.get("compilers", []):
        local_dockerfiles.append(
            [
                compiler["platform"],
                compiler["id"],
                compiler.get("arch"),
            ]
        )

    if args.dockerfiles:
        allowed_dockerfiles = []
        lines = [x.strip() for x in args.dockerfiles.readlines()]
        for line in lines:
            path = Path(line)
            res = parse_dockerfile_path(path)
            if res is not None:
                allowed_dockerfiles.append(res)

        if len(allowed_dockerfiles) > 0:
            local_dockerfiles = filter(
                lambda x: x in allowed_dockerfiles, local_dockerfiles
            )
        else:
            # no Dockerfiles were modified
            local_dockerfiles = []

    if args.platforms:
        local_dockerfiles = filter(
            lambda x: x[0] in args.platforms, local_dockerfiles
        )

    includes = [process_dockerfile(p, c, a) for (p, c, a) in local_dockerfiles]
    matrix = dict(include=includes)
    print(json.dumps(matrix, separators=(",", ":")))


if __name__ == "__main__":
    main()
