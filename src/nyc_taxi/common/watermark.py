from __future__ import annotations

import json
from pathlib import Path
from typing import Optional


def _wm_path(state_dir: Path) -> Path:
    state_dir.mkdir(parents=True, exist_ok=True)
    return state_dir / "watermark.json"


def get_last_loaded_month(state_dir: Path, dataset: str) -> Optional[str]:
    p = _wm_path(state_dir)
    if not p.exists():
        return None
    obj = json.loads(p.read_text(encoding="utf-8"))
    return obj.get(dataset)


def set_last_loaded_month(state_dir: Path, dataset: str, month: str) -> None:
    p = _wm_path(state_dir)
    obj = {}
    if p.exists():
        obj = json.loads(p.read_text(encoding="utf-8"))
    obj[dataset] = month
    p.write_text(json.dumps(obj, indent=2), encoding="utf-8")