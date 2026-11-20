import sys
from pathlib import Path

import erdantic as erd

# Resolve paths relative to this file so the script works from any directory.
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))
diagrams_dir = repo_root / "diagrams"

from horizon.CatalogedResource import CatalogedResource
from horizon.Entity import Entity
from horizon.DataRelease import DataRelease
from horizon.License import License
from horizon.Location import Location
from horizon.Distribution import Distribution
from horizon.Dataset import Dataset

models = [
    Entity,
    License,
    Location,
    Dataset,
    DataRelease,
    CatalogedResource,
    Distribution,
]

for model in models:
    erd.draw(model, out=str(diagrams_dir / f"{model.__name__}-diagram.png"))
