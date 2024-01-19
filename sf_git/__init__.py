from pathlib import Path

from dotenv import load_dotenv

__version__ = "1.3"

HERE = Path(__file__).parent
dotenv_path = HERE / "sf_git.conf"

if dotenv_path.is_file():
    load_dotenv(dotenv_path=dotenv_path)
