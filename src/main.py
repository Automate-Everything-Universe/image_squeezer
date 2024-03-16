"""
Main entry for the CLI
"""

import argparse
from pathlib import Path

from PIL.Image import Image

from src.image_squeezer.folder_utlis import find_files, load_image
from src.image_squeezer.saver import SavePic
from src.image_squeezer.sizer import AspectRatioSizer

IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".heic")


def parse_arguments() -> argparse.Namespace:
    """
    Parses user arguments
    :return:
    """
    parser = argparse.ArgumentParser(
        prog='image_squeezer',
        description='Can do the following operations:\n'
                    '- Folder: decrease the size of all images from a folder to a 640 width (default) \n'
                    '- Keeps the original aspect ratio (default)\n'
                    '- Creates a backup folder where the original images are saved (default)\n'
                    '- File: decrease the size a specific image file\n'

    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--folder", help="Folder absolute path")
    parser.add_argument("--width",
                        help="New width", default=640)
    group.add_argument("--suffix", action="store_true",
                       help="Adds a suffix at the end of the file name (e.g. _resized)", default=False)
    group.add_argument("--backup", action="store_true", help="A backup folder with the original files will be created",
                       default=True)
    parser.add_argument('--verbose', action='store_true', help="Debug mode")
    return parser.parse_args()


def _process_image(pic: Path, user_args: argparse.Namespace) -> None:
    image_object = load_image(picture=pic)
    suffix = user_args.suffix if user_args.suffix else None

    if user_args.backup:
        save_folder = Path(user_args.folder) / "backup"
        if not save_folder.exists():
            save_folder.mkdir(parents=True, exist_ok=True)
    else:
        save_folder = Path(user_args.folder)

    scaler = AspectRatioSizer(img=image_object, width=user_args.width)
    image_object = scaler.resize()
    suffix = suffix if suffix else None
    image_saver = SavePic(img=image_object)
    image_saver.save_image(path=save_folder, suffix=suffix)


def main() -> None:
    """
    Main entry for the CLI
    :return: None
    """
    try:
        args = parse_arguments()
        folder = Path(args.folder) if args.folder else None

        start_process(args, folder)

        if args.verbose:
            print("Done!")
            return 0
    except ValueError as exc:
        print(f"Invalid value provided: {exc}")
        return 1
    except FileNotFoundError as exc:
        print(f"The file was not found: {exc}")
        return 1
    except PermissionError as exc:
        print(f"Permission denied for file: {exc}")
        return 1
    except OSError as exc:
        print(f"An error occurred while opening the file: {exc}")
        return 1
    except Exception as exc:
        print(f"An unexpected error occurred: {exc}")
        return 1


def start_process(args, folder):
    pics = find_files(path=folder, extension=IMAGE_EXTENSIONS)
    for pic in pics:
        _process_image(pic=pic, user_args=args)


if __name__ == "__main__":
    main()
