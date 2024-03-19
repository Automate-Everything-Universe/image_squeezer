import shutil
import subprocess
from pathlib import Path

import pytest

TEST_FOLDER = Path(__file__).parents[0]
MAIN = Path(__file__).parents[1] / "src/main.py"
BACKUP_DIR = TEST_FOLDER / "backup"

HEIC_IMG = "01_knife.HEIC"
PNG_IMG = "20245201_155204_electrical_outlet_IMG_5354.png"
JPEG_IMG = "20244701_164722_electrical_outlet_20240301_174539.jpeg"


@pytest.fixture
def heic_img() -> Path:
    return TEST_FOLDER / HEIC_IMG


@pytest.fixture
def png_img() -> Path:
    return TEST_FOLDER / PNG_IMG


@pytest.fixture
def jpeg_img() -> Path:
    return TEST_FOLDER / JPEG_IMG


@pytest.fixture
def expected_backup_folder() -> Path:
    return BACKUP_DIR


@pytest.fixture
def expected_heic() -> Path:
    return BACKUP_DIR / "01_knife.png"  # heic will be converted to png


@pytest.fixture
def expected_png() -> Path:
    return BACKUP_DIR / PNG_IMG


@pytest.fixture
def expected_jpeg() -> Path:
    return BACKUP_DIR / JPEG_IMG


def test_cli(expected_backup_folder, expected_heic, expected_png, expected_jpeg):
    command = ["python", str(MAIN), "--folder", str(TEST_FOLDER)]

    result = subprocess.run(
        command, capture_output=True, check=True, timeout=180, cwd=TEST_FOLDER
    )

    assert result.returncode == 0, f"Script failed with errors: {result.stderr}"

    assert expected_backup_folder.exists(), "Backup folder does not exist"

    assert expected_heic.exists(), "Heic resized image does not exist"
    assert expected_png.exists(), "Png resized image does not exist"
    assert expected_jpeg.exists(), "Jpeg resized image does not exist"

    # Clean up
    shutil.rmtree(expected_backup_folder)
