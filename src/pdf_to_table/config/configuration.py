from pdf_to_table.utils import read_yaml,make_dirs
from pathlib import Path
from pdf_to_table.constant import ArtifactsKey,LayoutParserKey,PdfSaverKey
from pdf_to_table.entity import LayoutParserConfig,PdfSaverConfig
import os





class Configuration:
    def __init__(self):
        self.config_content = read_yaml()
        artifact_content = ArtifactsKey.ARTIFACTS_ROOT_KEY
        self.artifact_dir_name  = self.config_content.get(artifact_content).get(ArtifactsKey.ARTIFACTS_ROOT_DIR_KEY)
        make_dirs([Path(self.artifact_dir_name)])


    def get_pdf_saver_config(self)->PdfSaverConfig:

        pdf_saver_content = self.config_content.get(PdfSaverKey.PDF_SAVER_ROOT_KEY)
        root_dir = os.path.join(self.artifact_dir_name,pdf_saver_content.get(PdfSaverKey.PDF_SAVER_ROOT_DIR_KEY))
        file_name = os.path.join(root_dir,pdf_saver_content.get(PdfSaverKey.PDF_SAVER_FILE_NAME))
        images_dir_name = os.path.join(root_dir,pdf_saver_content.get(PdfSaverKey.PDF_SAVER_IMAGES_DIR_NAME))
        make_dirs([root_dir])
        return PdfSaverConfig(root_dir, file_name, images_dir_name)
        

    def get_layout_config(self)->LayoutParserConfig:

        layout_content = self.config_content.get(LayoutParserKey.LAYOUTPARSER_ROOT_KEY)
        root_dir = os.path.join(
            self.artifact_dir_name,
            layout_content.get(LayoutParserKey.LAYOUTPARSER_ROOT_DIR_KEY)
        )

        make_dirs([root_dir])
        file_name = os.path.join(root_dir,layout_content.get(LayoutParserKey.LAYOUTPARSER_WHL_FILE_NAME_KEY))
        whl_url = layout_content.get(LayoutParserKey.LAYOUTPARSER_WHL_URL_KEY)

        return LayoutParserConfig(root_dir, whl_url, file_name)