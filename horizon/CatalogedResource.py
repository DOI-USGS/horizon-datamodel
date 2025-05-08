from datetime import datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl
from .Entity import Entity


class UsgsAssetTypeEnum(str, Enum):
    data = "Data"
    model = "Model"
    publication = "Publication"
    software = "Software"


class AccessRightsEnum(str, Enum):
    public = "Public"
    non_public = "Non Public"


class CatalogedResource(BaseModel):
    """Basic metadata schema for a cataloged resource.

    Fields
    ------
    title: A name given to the resource.
    usgsAssetType: The type of asset cataloged: data, model, publication, software
    description: A free-text account of the resource.
    usgsCreated: Date and time that the resource's record was created in the catalog
    usgsModified: Date and time that the resource's record was last modified
    identifier: A unique identifier of the resource being described or
        cataloged. This identifier should be represented by a URI.
    usgsIdentifier: Identifier used to internally identify a resource within a
        particular system
    accessRights: Information about who can access the resource or an
        indication of its security status.

    """
    usgsIdentifier: str
    identifier: HttpUrl | None = None
    title: str
    usgsAssetType: UsgsAssetTypeEnum

    usgsCreated: datetime
    usgsCreatedBy: Entity | None = None
    usgsModified: datetime
    usgsModifiedBy: Entity | None = None

    description: str
    accessRights: AccessRightsEnum
