import time
import os
from pathlib import Path
from dataclasses import dataclass



CONFIG_YAML_FILE_PATH = Path("config/config.yaml")
LOGGING_DIR_NAME = "logs"
os.makedirs(LOGGING_DIR_NAME,exist_ok=True)
CURRENT_TIME_STAMP = time.asctime().replace(" ", "_").replace(":", "_")
LOGGING_FILE_NAME = f"runing_logs_{CURRENT_TIME_STAMP}.log"



@dataclass(frozen=True)
class PdfSaverKey:
    PDF_SAVER_ROOT_KEY:str =  "pdf_saver"
    PDF_SAVER_ROOT_DIR_KEY:str =  "root_dir"
    PDF_SAVER_FILE_NAME:str =  "file_name"
    PDF_SAVER_IMAGES_DIR_NAME:str =  "images_dir_name"


@dataclass(frozen=True)
class ArtifactsKey:
    ARTIFACTS_ROOT_KEY:str="artifact"
    ARTIFACTS_ROOT_DIR_KEY:str="root_dir"

@dataclass(frozen=True)
class LayoutParserKey:
    LAYOUTPARSER_ROOT_KEY:str="layout_parser"
    LAYOUTPARSER_ROOT_DIR_KEY:str="root_dir"
    LAYOUTPARSER_WHL_FILE_NAME_KEY:str="file_name"
    LAYOUTPARSER_WHL_URL_KEY:str="whl_url"



