import sys
from pathlib import Path

# Ensure the repo root (parent of scripts/) is importable so `horizon`
# resolves regardless of the current working directory.
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

import erdantic as erd

from horizon.CatalogedResource import CatalogedResource
from horizon.Entity import Entity
from horizon.DataRelease import DataRelease
from horizon.License import License
from horizon.Location import Location
from horizon.Distribution import Distribution
from horizon.Dataset import Dataset
from horizon.DataReleaseInitiation import DataReleaseInitiation
from horizon.DataReleaseComponent import DataReleaseComponent
from horizon.DataReleaseCSDGM import DataReleaseCSDGM

# Write diagrams to the diagrams/ directory at the repo root, regardless of
# the current working directory.
diagrams_dir = repo_root / "diagrams"
diagrams_dir.mkdir(exist_ok=True)

models = [
    Entity,
    License,
    Location,
    Distribution,
    Dataset,
    DataRelease,
    CatalogedResource,
    DataReleaseInitiation,
    DataReleaseComponent,
    DataReleaseCSDGM,
]

for model in models:
    out = diagrams_dir / f"{model.__name__}-diagram.png"
    erd.draw(model, out=str(out))
