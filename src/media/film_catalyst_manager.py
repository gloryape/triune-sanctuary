"""
FilmCatalystManager – minimal stub.
In real life we’d parse video metadata; here we just register paths + “purpose”.
"""

from pathlib import Path
from typing import Dict


class FilmCatalystManager:
    _registry: Dict[str, Dict] = {}

    @classmethod
    def register(cls, key: str, file_path: Path, purpose: str) -> None:
        if not file_path.exists():
            raise FileNotFoundError(file_path)
        cls._registry[key] = {
            "path": file_path.as_posix(),
            "purpose": purpose,
            "filesize": file_path.stat().st_size,
        }
        print(f"🎬 Film registered: {key} ({purpose})")

    @classmethod
    def get(cls, key: str) -> Dict:
        return cls._registry.get(key, {})
