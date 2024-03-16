from abc import ABC
from abc import abstractmethod
from pathlib import Path
from typing import Union

from PIL import Image
from pillow_heif import register_heif_opener


class ImageCreator(ABC):
    """
    Interface
    """

    def __init__(self, file: Union[Path, str]):
        self._file = file

    @abstractmethod
    def convert_image(self):
        """
        Abstract method for sizer objects.
        """


class CreatePillowImage(ImageCreator):

    def __init__(self, file: Union[Path, str]):
        super().__init__(file)

    def convert_image(self) -> Image:
        try:
            if self._file.suffix.lower() == ".heic":
                register_heif_opener()  # https://stackoverflow.com/questions/54395735/how-to-work-with-heic-image-file-types-in-python
            return Image.open(self._file)
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"The file {self._file} was not found") from exc
        except PermissionError as exc:
            raise PermissionError(f"Permission denied for file {self._file}") from exc
        except OSError as exc:
            raise OSError(f"An error occurred while opening the file {self._file}: {exc}") from exc