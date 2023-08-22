from collections import namedtuple


PdfSaverConfig = namedtuple("PdfSaverConfig", 
[
    "root_dir",
    "file_name",
    "images_dir_name"
]
)

LayoutParserConfig = namedtuple("LayoutParserConfig", [
    "root_dir",
    "whl_url",
    "file_name"
    ])


TextExtractorConfig = namedtuple("TextExtractorConfig", 
                    [
                        "root_dir",
                        "csv_dir_name",
                        "excel_file_name",
                        "table_imgs_dir_name"
                    ]
                    )

TableDetectorConfig = namedtuple("TableDetectorConfig", 
                        [
                            "root_dir",
                            "table_imgs_dir_name",
                            "images_dir_name"
                        ]
                        )


