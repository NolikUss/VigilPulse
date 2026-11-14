from pathlib import Path
import yaml

CONFIG_PATH = Path("CONFIG.yml")

with CONFIG_PATH.open("r", encoding="utf-8") as file:
    config = yaml.safe_load(file)