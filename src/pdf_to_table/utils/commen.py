import os
from pathlib import Path
from pdf_to_table import logging

def make_dirs(dir_list:Path)->None:

    try:
        for dir in dir_list:
            os.makedirs(dir,exist_ok=True)
            logging.info(f" dir created {dir} ")
    except Exception as e:
        logging.exception(e)
        raise e