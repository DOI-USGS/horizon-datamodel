from datetime import datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl


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
    title: str
        A name given to the resource.
    usgsAssetType: UsgsAssetTypeEnum
        The type of asset cataloged: data, model, publication, software
    description: str
        A free-text account of the resource.
    usgsCreated: datetime
        Date and time that the resource's record was created in the catalog
    usgsModified: datetime
        Date and time that the resource's record was last modified
    identifier: HttpUrl | None = None
        A unique identifier of the resource being described or cataloged.
        This identifier should be represented by a URI.
    usgsIdentifier: str
        Identifier used to internally identify a resource within a particular system
    accessRights: AccessRightsEnum
        Information about who can access the resource or an indication of its security status.

    """

    title: str
    usgsAssetType: UsgsAssetTypeEnum
    description: str
    usgsCreated: datetime
    usgsModified: datetime
    identifier: HttpUrl | None = None
    usgsIdentifier: str
    accessRights: AccessRightsEnum
