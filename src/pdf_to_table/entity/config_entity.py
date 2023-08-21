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