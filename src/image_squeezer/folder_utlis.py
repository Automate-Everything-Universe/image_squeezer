"""
Module to handle file operations
"""
from pathlib import Path
from PIL import Image
from typing import Union, Tuple, List

from .image_creator import CreatePillowImage


def find_files(path: Path, extension: Union[str, Tuple, None]) -> List[Path]:
    path_is_valid = validate_path(path=path)
    if not path_is_valid:
        raise ValueError("Folder path is not valid")
    elif extension:
        pics = [pic for pic in path.iterdir() if pic.suffix.lower() in extension]
        if not pics:
            raise FileNotFoundError(f"No picture was found with {extension} in folder {path}")
        return pics
    pics = [pic for pic in path.iterdir()]
    if not pics:
        raise FileNotFoundError(f"No picture was found in folder {path}")
    return pics


def validate_path(path: Path) -> bool:
    if not any((path.exists(), path.is_dir())):
        return False
    return True


def load_image(picture: Path) -> Union[Image, None]:
    try:
        if not picture.exists():
            raise FileNotFoundError(f"File {picture} not found.")
        image_creator = CreatePillowImage(file=picture)
        image_obj = image_creator.convert_image()
        return image_obj
    except OSError as exc:
        raise OSError(f"Error opening image: {exc}") from exc
