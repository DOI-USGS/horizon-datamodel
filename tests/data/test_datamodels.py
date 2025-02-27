from datetime import datetime as dt
import json

from pydantic import ValidationError
import pytest

from horizon.CatalogedResource import CatalogedResource
from horizon.Dataset import (
    Dataset,
    UsgsMissionArea,
    VersionHistory,
    UsgsDataSource,
    PeriodOfTime,
    Distribution,
    AlternateIdentifier,
    RelatedIdentifier,
    Keyword,
    RelatedIdentifierTypeEnum,
)
from horizon.Entity import Entity, Creator, Contributor
from horizon.License import License
from horizon.Location import Location, BoundingBox, Centroid


data = {
    "title": "test",
    "usgsAssetType": "Model",
    "description": "...",
    "usgsCreated": dt.now(),
    "usgsModified": dt.now(),
    "identifier": "https://doi.org/10.123",
    "usgsIdentifier": "1234ab",
    "accessRights": "Public",
}


def test_CatalogedResource_validation():
    # Test with valid data
    try:
        m = CatalogedResource(**data)
    except ValidationError:
        pytest.fail("Valid data raised ValidationError")

    # Test with invalid data
    invalid_data = data.copy()
    invalid_data["usgsCreated"] = "invalid_date"
    with pytest.raises(ValidationError):
        CatalogedResource(**invalid_data)
