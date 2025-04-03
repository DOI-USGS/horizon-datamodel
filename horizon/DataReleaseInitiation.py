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
    title: str
        A name given to the resource.
    creator: Creator
        The entity responsible for producing the resource.
    license: License
        A legal document under which the resource is made available.
    usgsDataSource: UsgsDataSource
        The USGS Science Center or Program responsible for managing the resource.
    usgsMissionArea: UsgsMissionArea | None
        The USGS Mission Area responsible for managing the resource.
    relation: list[RelatedIdentifier] | None
        A resource with a relationship to the cataloged resource.
        This property includes DCAT sub-properties hasPart, isReferencedBy, previousVersion, replaces.
    alternateIdentifier: list[AlternateIdentifier] | None
        An identifier or identifiers other than the primary Identifier applied to the resource being registered.
    qualifiedAttribution: Contributor | None
        Link to an Agent having some form of responsibility for the resource
    versionHistory: VersionHistory | None
        Description of versions of the dataset described within a given identifier.
    """
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
    
    usgsAssetType: UsgsAssetTypeEnum
        The type of asset cataloged: data, model, publication, software
    usgsCreated: datetime
        Date and time that the resource's record was created in the catalog
    usgsModified: datetime
        Date and time that the resource's record was last modified
    identifier: HttpUrl
        A unique identifier of the resource being described or cataloged.
        This identifier should be represented by a URI.
    usgsIdentifier: str
        Identifier used to internally identify a resource within a particular system
    accessRights: AccessRightsEnum
        Information about who can access the resource or an indication of its security status.
    publisher: Entity
        The entity responsible for making the resource available.
    distribution: list[Distribution]
        An available distribution of the dataset.
    
    """
    
    usgsAssetType: UsgsAssetTypeEnum = UsgsAssetTypeEnum.data
    usgsCreated: datetime = datetime.now()
    usgsModified: datetime = datetime.now()
    identifier: HttpUrl
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


