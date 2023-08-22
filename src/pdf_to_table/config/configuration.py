from pdf_to_table.utils import read_yaml, make_dirs
from pathlib import Path
from pdf_to_table.constant import (
    TextExtractorKey,
    ArtifactsKey,
    LayoutParserKey,
    PdfSaverKey,
    TableDetectorKey,
)
from pdf_to_table.entity import (
    LayoutParserConfig,
    PdfSaverConfig,
    TableDetectorConfig,
    TextExtractorConfig,
)
import os


class Configuration:
    def __init__(self):
        self.config_content = read_yaml()
        artifact_content = ArtifactsKey.ARTIFACTS_ROOT_KEY
        self.artifact_dir_name = self.config_content.get(artifact_content).get(
            ArtifactsKey.ARTIFACTS_ROOT_DIR_KEY
        )
        make_dirs([Path(self.artifact_dir_name)])

    def get_text_extractor_config(self) -> TextExtractorConfig:
        text_extractor_content = self.config_content.get(
            TextExtractorKey.TEXT_EXTRATOR_ROOT_KEY
        )
        root_dir = os.path.join(
            self.artifact_dir_name,
            text_extractor_content.get(TextExtractorKey.TEXT_EXTRATOR_ROOT_DIR_KEY),
        )
        csv_dir_name = os.path.join(
            root_dir,
            text_extractor_content.get(TextExtractorKey.TEXT_EXTRATOR_CSV_DIR_KEY),
        )
        table_imgs_dir_name = self.get_table_detector_config().table_imgs_dir_name
        excel_file_name = os.path.join(
            root_dir,
            text_extractor_content.get(
                TextExtractorKey.TEXT_EXTRATOR_EXCEL_FILE_NAME_KEY
            ),
        )
        make_dirs([root_dir, csv_dir_name])
        return TextExtractorConfig(
            root_dir, csv_dir_name, excel_file_name, table_imgs_dir_name
        )

    def get_pdf_saver_config(self) -> PdfSaverConfig:
        pdf_saver_content = self.config_content.get(PdfSaverKey.PDF_SAVER_ROOT_KEY)
        root_dir = os.path.join(
            self.artifact_dir_name,
            pdf_saver_content.get(PdfSaverKey.PDF_SAVER_ROOT_DIR_KEY),
        )
        file_name = os.path.join(
            root_dir, pdf_saver_content.get(PdfSaverKey.PDF_SAVER_FILE_NAME)
        )
        images_dir_name = os.path.join(
            root_dir, pdf_saver_content.get(PdfSaverKey.PDF_SAVER_IMAGES_DIR_NAME)
        )
        make_dirs([root_dir, images_dir_name])
        return PdfSaverConfig(root_dir, file_name, images_dir_name)

    def get_table_detector_config(self) -> TableDetectorConfig:
        table_detector_content = self.config_content.get(
            TableDetectorKey.TABLE_DETECTOR_ROOT_KEY
        )

        root_dir = os.path.join(
            self.artifact_dir_name,
            table_detector_content.get(TableDetectorKey.TABLE_DETECTOR_ROOT_DIR_KEY),
        )
        table_imgs_dir_name = os.path.join(
            root_dir,
            table_detector_content.get(TableDetectorKey.TABLE_DETECTOR_IMAGES_DIR_KEY),
        )
        make_dirs([root_dir, table_imgs_dir_name])
        images_dir_name = self.get_pdf_saver_config().images_dir_name
        return TableDetectorConfig(root_dir, table_imgs_dir_name, images_dir_name)

    def get_layout_config(self) -> LayoutParserConfig:
        layout_content = self.config_content.get(LayoutParserKey.LAYOUTPARSER_ROOT_KEY)
        root_dir = os.path.join(
            self.artifact_dir_name,
            layout_content.get(LayoutParserKey.LAYOUTPARSER_ROOT_DIR_KEY),
        )

        make_dirs([root_dir])
        whl_url = layout_content.get(LayoutParserKey.LAYOUTPARSER_WHL_URL_KEY)
        file_name = whl_url.split("/")[-1]
        file_name = os.path.join(root_dir, file_name)

        return LayoutParserConfig(root_dir, whl_url, file_name)
