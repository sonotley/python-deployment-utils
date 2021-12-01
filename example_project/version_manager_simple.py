"""Script to apply versions in projects using Poetry

This simple version is actually less functional than calling `poetry version`
but shows how I create `version.txt` in each package
"""
import sys
import subprocess
import re
import os

short_version_pattern = re.compile(r"^\d+\.\d+$")
long_version_pattern = re.compile(r"^\d+\.\d+\.\d+(\.\d+)?$")


def version_to_str(version):
    return ".".join(str(x) for x in version)


def write_version_to_pyproject(version):
    subprocess.run(["poetry", "version", version_to_str(version)])


def write_version_to_packages(version):
    dir_list = next(os.walk('.'))[1]
    for d in dir_list:
        if d[0] not in (".", "_") and os.path.exists(os.path.join(d, "__init__.py")):
            target_path = os.path.join(d, "version.txt")
            with open(target_path, 'w') as f:
                f.write(version_to_str(version))


if len(sys.argv) > 2:
    print("Too many arguments")

elif long_version_pattern.match(sys.argv[1]):
    v = sys.argv[1].split(".")
    version = tuple(v)
else:
    print(f"Invalid argument '{sys.argv[1]}'")
    exit(1)
write_version_to_pyproject(version)
write_version_to_packages(version)


