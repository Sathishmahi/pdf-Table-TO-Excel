import os
from src.pdf_to_table.components.table_detector import TableDetector
from src.pdf_to_table.config.configuration import Configuration


configuration =  Configuration()
pdf_saver_config = configuration.get_table_detector_config()
table_imgs_dir_name = pdf_saver_config.table_imgs_dir_name

def test_table_detector():
    
    table_detector  =  TableDetector()
    table_detector.get_bb_points()
    assert os.path.exists(table_imgs_dir_name)
    assert len(os.listdir(table_imgs_dir_name))>0