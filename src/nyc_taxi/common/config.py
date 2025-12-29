from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import yaml


@dataclass(frozen=True)
class AwsConfig:
    region: str | None = None
    s3_bronze_bucket: str | None = None
    s3_bronze_prefix: str = "bronze/nyc_taxi"


@dataclass(frozen=True)
class DataConfig:
    raw_dir: Path
    bronze_dir: Path
    state_dir: Path


@dataclass(frozen=True)
class AppConfig:
    project: str
    aws: AwsConfig
    data: DataConfig


def load_config(config_path: str | Path) -> AppConfig:
    p = Path(config_path)
    obj = yaml.safe_load(p.read_text(encoding="utf-8"))

    project = obj.get("project", "nyc_taxi")

    aws_obj = obj.get("aws", {}) or {}
    aws = AwsConfig(
        region=aws_obj.get("region"),
        s3_bronze_bucket=aws_obj.get("s3_bronze_bucket"),
        s3_bronze_prefix=aws_obj.get("s3_bronze_prefix", "bronze/nyc_taxi"),
    )

    data_obj = obj.get("data", {}) or {}
    raw_dir = Path(data_obj.get("raw_dir", "data/raw"))
    bronze_dir = Path(data_obj.get("bronze_dir", "data/bronze"))
    state_dir = Path(data_obj.get("state_dir", "data/_state"))

    data = DataConfig(raw_dir=raw_dir, bronze_dir=bronze_dir, state_dir=state_dir)
    return AppConfig(project=project, aws=aws, data=data)