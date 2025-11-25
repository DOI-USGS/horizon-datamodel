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
    usgsIdentifier: Identifier used to internally identify a resource within a
        particular system
    identifier: A unique identifier of the resource being described or
        cataloged. This identifier should be represented by a URI.
    title: A name given to the resource.
    usgsAssetType: The type of asset cataloged: data, model, publication, software
    usgsHasPart: Indicates whether the resource has a part or parts that are
        cataloged separately. If true, the resource has parts that are cataloged.
    isPartOf: The identifier of the related resource in which the described resource
        is physically or logically included.
    usgsCreated: Date and time that the resource's record was created in the catalog
    usgsCreatedBy: The entity responsible for creating the resource's record
        in the catalog.
    usgsModified: Date and time that the resource's record was last modified
    usgsModifiedBy: The entity responsible for modifying the resource's record
        in the catalog.

    description: A free-text account of the resource.
    accessRights: Information about who can access the resource or an
        indication of its security status.
    """
    usgsIdentifier: str
    identifier: HttpUrl | None = None
    title: str
    usgsAssetType: UsgsAssetTypeEnum
    usgsHasPart: bool | None = None
    isPartOf: str | None = None

    usgsCreated: datetime
    usgsCreatedBy: Entity | None = None
    usgsModified: datetime
    usgsModifiedBy: Entity | None = None

    description: str
    accessRights: AccessRightsEnum

