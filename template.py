import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, filename="loginfo.log", format="[%(asctime)s]  [%(message)s]"
)
package_name = "pdf_to_table"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/constant/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
]


###

for file_path in list_of_files:
    file_path = Path(file_path)
    file_splits = os.path.split(file_path)
    if file_splits[0] == "":
        if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
            with open(file_path, "w") as f:
                pass
            logging.info(msg=f"file created file name is {file_path}")
    else:
        os.makedirs(file_splits[0], exist_ok=True)
        if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
            with open(file_path, "w") as f:
                pass
            logging.info(msg=f"file created file name is {file_path}")