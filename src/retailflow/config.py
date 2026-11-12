"""Central, environment-neutral configuration. No DBFS root or credentials are assumed."""
from dataclasses import dataclass
from pathlib import Path
import os

@dataclass(frozen=True)
class Settings:
    project_root: Path
    data_root: Path
    storage_root: Path
    catalog: str | None = None
    schema: str = "retailflow_lab"

    @property
    def raw_path(self) -> Path: return self.data_root / "raw"
    @property
    def sample_path(self) -> Path: return self.data_root / "sample"

def get_settings() -> Settings:
    root = Path(os.environ.get("RETAILFLOW_ROOT", Path.cwd())).resolve()
    return Settings(root, root / "data", root / "storage", os.environ.get("RETAILFLOW_CATALOG"))
