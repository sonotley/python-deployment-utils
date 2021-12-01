"""Script to generate and apply C#-style versions in projects using Poetry

If run with no arguments it will read the current version from pyproject.toml and bump the third and fourth parts
according to the time-based C# method

If run with an argument like 2.1 it will use this as the major and minor version and append the rest

If run with an argument like 2.3.54 or 4.5.7.545 it will use this directly as the version number

"""
from datetime import datetime
import sys
import subprocess
import re
import os

short_version_pattern = re.compile(r"^\d+\.\d+$")
long_version_pattern = re.compile(r"^\d+\.\d+\.\d+(\.\d+)?$")


def version_to_str(version):
    return ".".join(str(x) for x in version)


def get_time_based_micros(time_now):
    build_delta = time_now - datetime(2021, 1, 1, 0, 0, 0, 0)
    build = build_delta.days

    revision = int((time_now.hour * 3600 + time_now.minute * 60 + time_now.second)/2)

    return build, revision


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

elif len(sys.argv) == 1:
    current_version = str(subprocess.check_output(["poetry", "version"])).strip().split()[1]
    target_major, target_minor = current_version.split(".")[0:2]
    version = (target_major, target_minor, *get_time_based_micros(datetime.utcnow()))
    write_version_to_pyproject(version)
    write_version_to_packages(version)

elif len(sys.argv) == 2:
    if short_version_pattern.match(sys.argv[1]):
        target_major, target_minor = sys.argv[1].split(".")
        version = (target_major, target_minor, *get_time_based_micros(datetime.utcnow()))
    elif long_version_pattern.match(sys.argv[1]):
        v = sys.argv[1].split(".")
        version = tuple(v)
    else:
        print(f"Invalid argument '{sys.argv[1]}'")
        exit(1)
    write_version_to_pyproject(version)
    write_version_to_packages(version)


