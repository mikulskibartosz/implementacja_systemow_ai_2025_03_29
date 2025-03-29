import yaml
from pathlib import Path
from pydantic import BaseModel
from src.utils.logger import setup_logger


logger = setup_logger()


class NormalizeInputConfig(BaseModel):
    train_path: Path
    test_path: Path

class NormalizeOutputConfig(BaseModel):
    train_path: Path
    test_path: Path


class NormalizeConfig(BaseModel):
    skip_columns: list[str]
    input: NormalizeInputConfig
    output: NormalizeOutputConfig


class SplitInputConfig(BaseModel):
    raw_path: Path


class SplitOutputConfig(BaseModel):
    train_path: Path
    test_path: Path


class SplitConfig(BaseModel):
    test_size: float
    random_state: int
    input: SplitInputConfig
    output: SplitOutputConfig


class LoadConfig(BaseModel):
    output_raw_path: Path
    target_column: str


class ModelConfig(BaseModel):
    name: str
    max_depth: int
    random_state: int


class TrainInputConfig(BaseModel):
    train_path: Path


class TrainOutputConfig(BaseModel):
    output_model_path: Path


class TrainConfig(BaseModel):
    input: TrainInputConfig
    model: ModelConfig
    output: TrainOutputConfig


class EvaluateInputConfig(BaseModel):
    test_path: Path
    model_path: Path


class EvaluateOutputConfig(BaseModel):
    report_path: Path
    graph_path: Path


class EvaluateConfig(BaseModel):
    input: EvaluateInputConfig
    output: EvaluateOutputConfig


class Config(BaseModel):
    load: LoadConfig
    split: SplitConfig
    normalize: NormalizeConfig
    train: TrainConfig
    evaluate: EvaluateConfig


def load_config(config_path: Path | str | None = None) -> Config:
    """
    Load configuration from a YAML file.

    Args:
        config_path: Path to the configuration file. If None, defaults to 'config/config.yaml'

    Returns:
        Config object with the loaded configuration
    """
    if config_path is None:
        config_path = Path(__file__).parent.parent.parent / "config" / "config.yaml"

    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found at {config_path}")

    with open(config_path, "r") as file:
        config_dict = yaml.safe_load(file)

    logger.info(f"Loaded configuration from {config_path}")
    logger.info(f"Configuration: {config_dict}")

    return Config(**config_dict)
