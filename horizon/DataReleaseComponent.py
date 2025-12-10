from datetime import datetime, date

import pydantic

from .CatalogedResource import UsgsAssetTypeEnum, AccessRightsEnum
from .Dataset import VersionHistory, RelatedIdentifier, AlternateIdentifier, PeriodOfTime, Location, Keyword
from .Distribution import Distribution
from .Entity import Entity, Creator, Contributor



class DataReleaseComponentForm(pydantic.BaseModel):
    """Basic metadata schema for user-required input for initiating and updating a component.

    Fields
    ------
    isPartOf: The identifier of the related resource in which the described resource
        is physically or logically included.
    usgsApprovalIdentifier: The identifier associated with the original record of approval for the data release.
    title: A name given to the resource.
    componentName: The short name provided for the directory that contains the component.
    creator: The entity responsible for producing the resource.
    identifier: A unique identifier of the resource being described or cataloged.
        This identifier should be represented by a URI.
    relation: A resource with a relationship to the cataloged resource.
        This property includes DCAT sub-properties hasPart, isReferencedBy, previousVersion, replaces.
    alternateIdentifier: An identifier or identifiers other than the primary Identifier applied to the resource being registered.
    qualifiedAttribution: Link to an Agent having some form of responsibility for the resource
    versionHistory: Description of versions of the dataset described within a given identifier.
    systemKeyword: Keywords used internally for system operations, queries, or application logic.
    isCatalogRecord: Indicates whether the component is intended to be cataloged in downstream catalogs (e.g., Data.gov).
        If true, the component is a catalog record.
    """
    isPartOf: str 
    title: str
    componentName: str
    description: str
    creator: list[Creator] = []
    identifier: pydantic.HttpUrl | None = None
    relation: list[RelatedIdentifier] | None = None
    alternateIdentifier: list[AlternateIdentifier] | None = None
    qualifiedAttribution: list[Contributor] | None = None
    versionHistory: list[VersionHistory] | None = None
    systemKeyword: list[Keyword] | None = None
    isCatalogRecord: bool = False


class DataReleaseComponentSystem(DataReleaseComponentForm):
    """Metadata schema that extends the user input information for a component with system generated information.

    Fields
    ------
    
    usgsIdentifier: Identifier used to internally identify a resource within a particular system

    usgsAssetType: The type of asset cataloged: data, model, publication, software
    usgsCreated: Date and time that the resource's record was created in the catalog
    usgsCreatedBy: The entity responsible for creating the resource's record
        in the catalog.
    usgsModified: Date and time that the resource's record was last modified
    usgsModifiedBy: The entity responsible for modifying the resource's record
        in the catalog.
    accessRights: Information about who can access the resource or an indication of its security status.
    distribution: An available distribution of the dataset.

    identifier: A unique identifier of the resource being described or
        cataloged. This identifier should be represented by a URI.
    title: A name given to the resource.
    description: A free-text account of the resource.

    issued: Date of formal issuance (e.g., publication) of the resource.
    temporal: The temporal period that the dataset covers.

    contactPoint: Relevant contact information for the cataloged resource.
    usgsMetadataContactPoint: The entity responsible for creating and
        maintaining the metadata for the resource.

    usgsPurpose: A summary of the intentions with which the resource was developed
    keyword: A keyword or tag describing the resource.
    spatial: The geographical area covered by the dataset.
    """

    usgsIdentifier: str

    usgsAssetType: UsgsAssetTypeEnum = UsgsAssetTypeEnum.data
    usgsCreated: datetime = pydantic.Field(default_factory=datetime.now)
    usgsCreatedBy: Entity | None = None
    usgsModified: datetime = pydantic.Field(default_factory=datetime.now)
    usgsModifiedBy: Entity | None = None
    accessRights: AccessRightsEnum = AccessRightsEnum.public

    distribution: list[Distribution] | None = None


class DataReleaseComponent(DataReleaseComponentSystem):
    """Basic metadata schema for a component.

    Fields
    ------
    
    usgsIdentifier: Identifier used to internally identify a resource within a particular system

    usgsAssetType: The type of asset cataloged: data, model, publication, software
    usgsCreated: Date and time that the resource's record was created in the catalog
    usgsCreatedBy: The entity responsible for creating the resource's record
        in the catalog.
    usgsModified: Date and time that the resource's record was last modified
    usgsModifiedBy: The entity responsible for modifying the resource's record
        in the catalog.
    accessRights: Information about who can access the resource or an indication of its security status.
    distribution: An available distribution of the dataset.

    identifier: A unique identifier of the resource being described or
        cataloged. This identifier should be represented by a URI.
    title: A name given to the resource.
    description: A free-text account of the resource.

    issued: Date of formal issuance (e.g., publication) of the resource.
    temporal: The temporal period that the dataset covers.

    contactPoint: Relevant contact information for the cataloged resource.
    usgsMetadataContactPoint: The entity responsible for creating and
        maintaining the metadata for the resource.

    usgsPurpose: A summary of the intentions with which the resource was developed
    keyword: A keyword or tag describing the resource.
    spatial: The geographical area covered by the dataset.
    """

    usgsIdentifier: str

    usgsAssetType: UsgsAssetTypeEnum = UsgsAssetTypeEnum.data
    usgsCreated: datetime = pydantic.Field(default_factory=datetime.now)
    usgsCreatedBy: Entity | None = None
    usgsModified: datetime = pydantic.Field(default_factory=datetime.now)
    usgsModifiedBy: Entity | None = None
    accessRights: AccessRightsEnum = AccessRightsEnum.public

    distribution: list[Distribution] | None = None

    # Fields Retrieved from DataReleaseCSDGM, if available

    ## Dates
    issued: date | None = None
    temporal: PeriodOfTime | None = None

    ## Contacts
    contactPoint: Entity | None = None
    usgsMetadataContactPoint: Entity | None = None

    ## Additional Descriptors
    usgsPurpose: str | None = None
    keyword: list[Keyword] | None = None
    spatial: Location | None = None
