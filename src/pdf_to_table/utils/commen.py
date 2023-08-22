# import os
# import yaml
# from pathlib import Path
# from pdf_to_table import logging
# from pdf_to_table.constant import CONFIG_YAML_FILE_PATH


# def make_dirs(dir_list: Path) -> None:
#     try:
#         for dir in dir_list:
#             os.makedirs(dir, exist_ok=True)
#             logging.info(f" dir created {dir} ")
#     except Exception as e:
#         logging.exception(e)
#         raise e


# def read_yaml(yaml_file_path: Path = CONFIG_YAML_FILE_PATH) -> dict:
#     if not os.path.exists(CONFIG_YAML_FILE_PATH):
#         logging.exception(e)
#         raise FileNotFoundError(f" yaml file not found {CONFIG_YAML_FILE_PATH} ")
#     with open(CONFIG_YAML_FILE_PATH) as yf:
#         content = yaml.safe_load(yf)
#     return content




# Import necessary libraries and modules
import os
import yaml
from pathlib import Path
from pdf_to_table import logging
from pdf_to_table.constant import CONFIG_YAML_FILE_PATH

# Define a function to create directories
def make_dirs(dir_list: Path) -> None:
    """
    Create directories specified in the dir_list if they don't already exist.

    Args:
        dir_list (Path): A list of directory paths to create.
    """
    try:
        for dir in dir_list:
            os.makedirs(dir, exist_ok=True)  # Create the directory if it doesn't exist
            logging.info(f" dir created {dir} ")  # Log that the directory was created
    except Exception as e:
        logging.exception(e)  # Log any exceptions that occur
        raise e

# Define a function to read YAML files
def read_yaml(yaml_file_path: Path = CONFIG_YAML_FILE_PATH) -> dict:
    """
    Read and parse a YAML file and return its contents as a dictionary.

    Args:
        yaml_file_path (Path): The path to the YAML file to be read.

    Returns:
        dict: The parsed contents of the YAML file as a dictionary.
    """
    if not os.path.exists(yaml_file_path):
        # Log an error if the specified YAML file does not exist
        logging.exception(e)
        raise FileNotFoundError(f" yaml file not found {yaml_file_path} ")

    with open(yaml_file_path) as yf:
        content = yaml.safe_load(yf)  # Load and parse the YAML file

    return content  # Return the parsed content as a dictionary
