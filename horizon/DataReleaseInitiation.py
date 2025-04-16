from datetime import datetime
from enum import Enum
import os

from pydantic import BaseModel, HttpUrl

from .CatalogedResource import UsgsAssetTypeEnum, AccessRightsEnum
from .Dataset import UsgsDataSource, UsgsMissionArea, VersionHistory, RelatedIdentifier, AlternateIdentifier
from .License import License
from .Entity import Entity, Creator, Contributor
from .Distribution import Distribution
from .DataRelease import StatusEnum, UsgsReleaseTypeEnum

COLLECTION_ID = os.getenv("GLOBUS_COLLECTION_ID", "0be095a6-c4e9-4db2-aec0-3310f11dddc7")

class DataReleaseInitiationForm(BaseModel):
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
    qualifiedAttribution: Contributor | None = None
    versionHistory: VersionHistory | None = None


class DataReleaseInitiation(DataReleaseInitiationForm):
    """Basic metadata schema for initiating a data release.

    Fields
    ------
    
    usgsAssetType: The type of asset cataloged: data, model, publication, software
    usgsCreated: Date and time that the resource's record was created in the catalog
    usgsModified: Date and time that the resource's record was last modified
    identifier: A unique identifier of the resource being described or cataloged.
        This identifier should be represented by a URI.
    usgsIdentifier: Identifier used to internally identify a resource within a particular system
    accessRights: Information about who can access the resource or an indication of its security status.
    publisher: The entity responsible for making the resource available.
    distribution: An available distribution of the dataset.
    
    """
    
    usgsAssetType: UsgsAssetTypeEnum = UsgsAssetTypeEnum.data
    usgsCreated: datetime = datetime.now()
    usgsModified: datetime = datetime.now()
    identifier: HttpUrl | None = None
    usgsIdentifier: str
    accessRights: AccessRightsEnum = AccessRightsEnum.public
    publisher: Entity = Entity(
        entity_id="https://ror.org/035a68863",
        name="United States Geological Survey",
        nameType="Organizational",
        nameIdentifier="https://ror.org/035a68863",
        email=None,
    )
    
    distribution: list[Distribution] = [
        Distribution(
            title="Data Release",
            description="Data Release",
            accessURL=HttpUrl(identifier),
            format="HTML",
            mediaType="text/html"
        ),
        Distribution(
            title="Globus Guest Collection",
            description="Globus guest collection for accessing data via Globus transfer",
            accessURL=HttpUrl(f"https://app.globus.org/file-manager?origin_id={COLLECTION_ID}&origin_path=%2F{usgsIdentifier}&two_pane=false"),
            format="HTML",
            mediaType="text/html"
        )
    ]
    
    status: StatusEnum = StatusEnum.created
    usgsReleaseType: UsgsReleaseTypeEnum = UsgsReleaseTypeEnum.dataRelease


