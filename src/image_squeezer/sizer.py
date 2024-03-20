"""
Module which handles the sizing
"""

from abc import ABC
from abc import abstractmethod

from PIL import Image, ImageOps

from .utils_validation import is_number_valid


class Sizer(ABC):
    """
    Interface for sizer objects
    """

    def __init__(self, img: Image):
        self.image = img

    @abstractmethod
    def resize(self) -> Image:
        """
        Abstract method for sizer objects.
        :return: Pillow image
        """


class AspectRatioSizer(Sizer):
    """
    Changes the picture size while keeping the aspect ratio.
    """

    def __init__(self, img: Image, width: int):
        super().__init__(img)
        self.filename = img.filename
        self._width = is_number_valid(width)

    def resize(self) -> Image:
        self.fix_img_rotation(img=self.image)
        new_height = self._calculate_height(img=self.image)
        resized_img = self.image.resize(
            size=(self._width, new_height), resample=Image.Resampling.LANCZOS
        )
        resized_img.filename = self.filename
        return resized_img

    def _calculate_height(self, img: Image):
        w_percent = self._width / float(img.size[0])
        new_height = int(float(img.size[1]) * float(w_percent))
        return new_height

    @staticmethod
    def fix_img_rotation(img: Image) -> Image:
        return ImageOps.exif_transpose(img)
