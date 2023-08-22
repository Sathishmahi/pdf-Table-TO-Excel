# import os
# from pdf_to_table.config import Configuration
# from pdf_to_table.entity.config_entity import LayoutParserConfig
# from pdf_to_table.config import Configuration
# import subprocess
# from pdf_to_table import logging
# import wget
# STAGE_NAME = "LAYOUT PARSER DOWNLOAD"

# layout_config = Configuration().get_layout_config()


# def to_download_layout_parser(layout_config: LayoutParserConfig = layout_config):

#     try:
#         whl_url = layout_config.whl_url
#         file_name = layout_config.file_name
#         if not os.listdir(layout_config.root_dir):
#             file_name = wget.download(whl_url, out=file_name)
#             logging.info(f" layout parser whl path   {file_name} ")
#             subprocess.run(["pip", "install", file_name])
#             print(" sucessfully installed layoutparser ")
#     except Exception as e:
#         logging.exception(e)
#         raise e


# if __name__ == "__main__":
#     print(f"  >>>>>>>>  START   {STAGE_NAME}   >>>>>>>>")
#     to_download_layout_parser()
#     print(f"  >>>>>>>>  END   {STAGE_NAME}   >>>>>>>>")





# Import necessary libraries and modules
import os
import subprocess
import wget
from pdf_to_table.config import Configuration
from pdf_to_table.entity.config_entity import LayoutParserConfig
from pdf_to_table import logging

# Define a constant for the stage name
STAGE_NAME = "LAYOUT PARSER DOWNLOAD"

# Get the layout configuration from the Configuration class
layout_config = Configuration().get_layout_config()

# Define a function to download and install the Layout Parser library
def to_download_layout_parser(layout_config: LayoutParserConfig = layout_config):
    try:
        # Get the URL and file name from the layout configuration
        whl_url = layout_config.whl_url
        file_name = layout_config.file_name

        # Check if the root directory is empty
        if not os.listdir(layout_config.root_dir):
            # Download the Layout Parser wheel file
            file_name = wget.download(whl_url, out=file_name)

            # Log the path to the downloaded wheel file
            logging.info(f" layout parser whl path   {file_name} ")

            # Install the downloaded wheel file using pip
            subprocess.run(["pip", "install", file_name])

            # Print a success message
            print("Successfully installed layoutparser")

    except Exception as e:
        # Log any exceptions and re-raise them
        logging.exception(e)
        raise e

if __name__ == "__main__":
    # Print a start message
    print(f"  >>>>>>>>  START   {STAGE_NAME}   >>>>>>>>")

    # Call the to_download_layout_parser function to download and install Layout Parser
    to_download_layout_parser()

    # Print an end message
    print(f"  >>>>>>>>  END   {STAGE_NAME}   >>>>>>>>")
