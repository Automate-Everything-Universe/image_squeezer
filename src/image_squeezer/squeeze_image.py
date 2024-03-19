from pathlib import Path
from typing import Tuple, Union

from .extensions import ALLOWED_EXTENSIONS
from .folder_utlis import load_image
from .saver import SavePic
from .sizer import AspectRatioSizer


class Squeezer:
    def __init__(
        self,
        folder: Path,
        width: int = 640,
        extensions: Tuple[str] = ALLOWED_EXTENSIONS,
        suffix: Union[str, None] = None,
        backup: bool = True,
    ):
        self._folder = folder
        self._width = width
        self._extensions = extensions
        self._suffix = suffix
        self._backup = backup

    def rescale_images(self):
        images = [
            img
            for img in self._folder.iterdir()
            if img.suffix.lower() in self._extensions
        ]
        for img in images:
            image_object = load_image(picture=img)
            if self._backup:
                save_folder = Path(self._folder) / "backup"
                if not save_folder.exists():
                    save_folder.mkdir(parents=True, exist_ok=True)
            else:
                save_folder = Path(self._folder)
            scaler = AspectRatioSizer(img=image_object, width=self._width)
            image_object = scaler.resize()
            image_saver = SavePic(img=image_object)
            image_saver.save_image(path=save_folder, suffix=self._suffix)
