from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_LAKE = PROJECT_ROOT / "data_lake"

BRONZE_PATH = DATA_LAKE / "bronze"
SILVER_PATH = DATA_LAKE / "silver"
GOLD_PATH = DATA_LAKE / "gold"

LOG_PATH = PROJECT_ROOT / "logs"

MODEL_PATH = PROJECT_ROOT / "models"