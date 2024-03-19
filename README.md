# Image Squeezer
Image Squeezer is a Python tool designed to reduce the size of images to a standard width of 640 px while keeping the same aspect ratio.
It utilizes the LANCZOS resampling method from the Pillow library.

## Overview
This tool addresses the common problem of high loading time for image pre-processing tools (like label studio) in case of a high number of images.

## Key Features
- Support for both CLI and as a python library

## Installation
To install, run in the command terminal:
```shell
pip install image_squeezer
```

## Usage

### CLI
```shell
image_squeezer --folder <folder_path> [--width <width>] [--suffix <string>] [--backup <bool>]
```

### Using image_squeezer in your script
```shell
from image_squeezer import Squeezer

squeezer = Squeezer(
                    folder= "path/to/my/images",
                    width=640, # optional argument
                    extensions = () , # optional argument
                    suffix = None, # optional argument
                    backup = True # optional argument
)

squeezer.rescale_images()
```

## Requirements
- Python 3.10 or higher
- pillow
- pillow_heif

## License
MIT License. See LICENSE for details.

## Contact
Reach out at info@automate-everything-company.com for support or inquiries.
