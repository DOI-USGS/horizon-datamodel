from datetime import datetime

import pydantic

from .CatalogedResource import UsgsAssetTypeEnum, AccessRightsEnum
from .DataRelease import StatusEnum, UsgsReleaseTypeEnum
from .Dataset import UsgsDataSource, UsgsMissionArea, VersionHistory, RelatedIdentifier, AlternateIdentifier, Keyword
from .Distribution import Distribution
from .Entity import Entity, Creator, Contributor
from .License import License


class DataReleaseInitiationForm(pydantic.BaseModel):
    """Basic metadata schema for user-required input for initiating and updating a data release.

    Fields
    ------
    usgsApprovalIdentifier: The identifier associated with the original record of approval for the data release.
    title: A name given to the resource.
    creator: The entity responsible for producing the resource.
    license: A legal document under which the resource is made available.
    usgsDataSource: The USGS Science Center or Program responsible for managing the resource.
    usgsMissionArea: The USGS Mission Area responsible for managing the resource.
    relation: A resource with a relationship to the cataloged resource.
        This property includes DCAT sub-properties hasPart, isReferencedBy, previousVersion, replaces.
    alternateIdentifier: An identifier or identifiers other than the primary Identifier applied to the resource being registered.
    qualifiedAttribution: Link to an Agent having some form of responsibility for the resource
    versionHistory: Description of versions of the dataset described within a given identifier.
    """
    usgsApprovalIdentifier: str
    title: str
    creator: list[Creator]
    license: License
    usgsDataSource: UsgsDataSource
    usgsMissionArea: UsgsMissionArea | None = None
    relation: list[RelatedIdentifier] | None = None
    alternateIdentifier: list[AlternateIdentifier] | None = None
    qualifiedAttribution: list[Contributor] | None = None
    versionHistory: list[VersionHistory] | None = None
    systemKeyword: list[Keyword] | None = None


class DataReleaseInitiation(DataReleaseInitiationForm):
    """Basic metadata schema for initiating a data release.

    Fields
    ------
    
    usgsIdentifier: Identifier used to internally identify a resource within a particular system

    identifier: A unique identifier of the resource being described or cataloged.
        This identifier should be represented by a URI.

    usgsAssetType: The type of asset cataloged: data, model, publication, software
    usgsHasPart: Indicates whether the resource has a part or parts that are
        cataloged separately. If true, the resource has parts that are cataloged.
    usgsCreated: Date and time that the resource's record was created in the catalog
    usgsCreatedBy: The entity responsible for creating the resource's record
        in the catalog.
    usgsModified: Date and time that the resource's record was last modified
    usgsModifiedBy: The entity responsible for modifying the resource's record
        in the catalog.
    accessRights: Information about who can access the resource or an indication of its security status.
    publisher: The entity responsible for making the resource available.
    distribution: An available distribution of the dataset.
    """

    usgsIdentifier: str

    identifier: pydantic.HttpUrl | None = None

    usgsAssetType: UsgsAssetTypeEnum = UsgsAssetTypeEnum.data
    usgsHasPart: bool | None = False
    usgsCreated: datetime = pydantic.Field(default_factory=datetime.now)
    usgsCreatedBy: Entity | None = None
    usgsModified: datetime = pydantic.Field(default_factory=datetime.now)
    usgsModifiedBy: Entity | None = None
    accessRights: AccessRightsEnum = AccessRightsEnum.public

    publisher: Entity | None = None
    distribution: list[Distribution] | None = None

    status: StatusEnum = StatusEnum.created
    usgsReleaseType: UsgsReleaseTypeEnum = UsgsReleaseTypeEnum.dataRelease
