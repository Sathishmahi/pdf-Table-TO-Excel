import os
from src.pdf_to_table.components.text_extractor import TextExtractor
from src.pdf_to_table.config.configuration import Configuration


configuration =  Configuration()
pdf_saver_config = configuration.get_text_extractor_config()
csv_dir_name = pdf_saver_config.csv_dir_name
excel_file_name = pdf_saver_config.excel_file_name

def test_table_detector():
    
    test_extractor  =  TextExtractor()
    test_extractor.get_text_bboxs()
    assert os.path.exists(csv_dir_name) and os.path.exists(excel_file_name)
    assert len(os.listdir(csv_dir_name))>0