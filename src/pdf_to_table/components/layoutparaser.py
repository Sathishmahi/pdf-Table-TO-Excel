import os
from pdf_to_table.config import Configuration
from pdf_to_table.entity.config_entity import LayoutParserConfig
from pdf_to_table.config import Configuration
import wget

layout_config = Configuration().get_layout_config()
def to_download_layout_parser(layout_config:LayoutParserConfig = layout_config):

    whl_url = layout_config.whl_url
    file_name = layout_config.file_name
    if not os.path.exists(file_name):
        wget.download(whl_url,out = file_name)
    



if __name__ == "__main__":
    to_download_layout_parser()