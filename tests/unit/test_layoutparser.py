import os
from src.pdf_to_table.components.layoutparaser import to_download_layout_parser
from src.pdf_to_table.config.configuration import Configuration


configuration =  Configuration()
layoutparser_config = configuration.get_layout_config()
file_name = layoutparser_config.file_name

def test_layoutparser():
    
    to_download_layout_parser()
    assert os.path.exists(file_name)