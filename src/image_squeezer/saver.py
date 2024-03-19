"""
Module which handles saving the picture
"""

from pathlib import Path
from typing import Union

from PIL import Image


class SavePic:
    """
    Class to save the Pillow image object
    """

    def __init__(self, img: Image):
        self._image = img
        self._image_path = None

    def save_image(self, path: Path, suffix: Union[str, None] = None) -> None:
        try:
            file = Path(self._image.filename)
            filename, extension = file.name.split(".")
            if suffix:
                image_name = f"{file}_{suffix}.{extension}"
                output_path = path / image_name
            else:
                image_name = file.name
                output_path = path / image_name
            if extension.lower() == "heic":
                image_name = f"{file.stem}.png"
                output_path = path / image_name
                self._image.save(output_path, "png")
                self._image_path = output_path
            else:
                self._image.save(output_path)
                self._image_path = output_path
        except OSError as exc:
            raise OSError(f"Error saving image: {exc}") from exc
        except ValueError as exc:
            raise ValueError(f"Invalid image: {exc}") from exc

    @property
    def image_path(self) -> Path:
        if self._image_path is None:
            raise AttributeError("Image has not been saved yet.")
        return self._image_path
