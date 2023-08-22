import time
import os
from pathlib import Path
from dataclasses import dataclass


CONFIG_YAML_FILE_PATH = Path("config/config.yaml")
PARMS_YAML_FILE_PATH = Path("params.yaml")

LOGGING_DIR_NAME = "logs"
os.makedirs(LOGGING_DIR_NAME, exist_ok=True)
CURRENT_TIME_STAMP = time.asctime().replace(" ", "_").replace(":", "_")
LOGGING_FILE_NAME = f"runing_logs_{CURRENT_TIME_STAMP}.log"


LAYOUT_PARSER_MODEL_CLASS_DICT = {0: "Text", 1: "Title", 2: "List", 3: "Table", 4: "Figure"}
LAYOUT_PARSER_MODEL_CONFIG_PATH = "lp://PubLayNet/ppyolov2_r50vd_dcn_365e_publaynet/config"


@dataclass(frozen=True)
class TextExtractorKey:
    TEXT_EXTRATOR_ROOT_KEY: str = "text_extractor"
    TEXT_EXTRATOR_ROOT_DIR_KEY: str = "root_dir"
    TEXT_EXTRATOR_CSV_DIR_KEY: str = "csv_dir_name"
    TEXT_EXTRATOR_EXCEL_FILE_NAME_KEY: str = "final_excel_file_name"


@dataclass(frozen=True)
class PdfSaverKey:
    PDF_SAVER_ROOT_KEY: str = "pdf_saver"
    PDF_SAVER_ROOT_DIR_KEY: str = "root_dir"
    PDF_SAVER_FILE_NAME: str = "file_name"
    PDF_SAVER_IMAGES_DIR_NAME: str = "images_dir_name"


@dataclass(frozen=True)
class ArtifactsKey:
    ARTIFACTS_ROOT_KEY: str = "artifact"
    ARTIFACTS_ROOT_DIR_KEY: str = "root_dir"


@dataclass(frozen=True)
class TableDetectorKey:
    TABLE_DETECTOR_ROOT_KEY: str = "teble_detector"
    TABLE_DETECTOR_ROOT_DIR_KEY: str = "root_dir"
    TABLE_DETECTOR_IMAGES_DIR_KEY: str = "teble_detector_imgs_dir_name"


@dataclass(frozen=True)
class LayoutParserKey:
    LAYOUTPARSER_ROOT_KEY: str = "layout_parser"
    LAYOUTPARSER_ROOT_DIR_KEY: str = "root_dir"
    LAYOUTPARSER_WHL_URL_KEY: str = "whl_url"

@dataclass(frozen=True)
class TableDetectorParamsKeys:
    PARAM_ROOT_KEY:str = "layout_model_params"
    PARAM_ENFORCE_CPU_KEY:str = "enforce_cpu"
    PARAM_ENALE_MKLDNN_KEY:str = "enable_mkldnn"
    PARAM_THERSOLD_KEY:str = "threshold"