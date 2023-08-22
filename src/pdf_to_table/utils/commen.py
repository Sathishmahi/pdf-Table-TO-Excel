import os
import yaml
from pathlib import Path
from pdf_to_table import logging
from pdf_to_table.constant import CONFIG_YAML_FILE_PATH


def make_dirs(dir_list: Path) -> None:
    try:
        for dir in dir_list:
            os.makedirs(dir, exist_ok=True)
            logging.info(f" dir created {dir} ")
    except Exception as e:
        logging.exception(e)
        raise e


def read_yaml(yaml_file_path: Path = CONFIG_YAML_FILE_PATH) -> dict:
    if not os.path.exists(CONFIG_YAML_FILE_PATH):
        logging.exception(e)
        raise FileNotFoundError(f" yaml file not found {CONFIG_YAML_FILE_PATH} ")
    with open(CONFIG_YAML_FILE_PATH) as yf:
        content = yaml.safe_load(yf)
    return content
