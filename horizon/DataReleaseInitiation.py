from datetime import datetime
import os
import urllib

import pydantic

from .CatalogedResource import UsgsAssetTypeEnum, AccessRightsEnum
from .DataRelease import StatusEnum, UsgsReleaseTypeEnum
from .Dataset import UsgsDataSource, UsgsMissionArea, VersionHistory, RelatedIdentifier, AlternateIdentifier
from .Distribution import Distribution
from .Entity import Entity, Creator, Contributor
from .License import License


COLLECTION_ID = os.getenv("GLOBUS_COLLECTION_ID", "0be095a6-c4e9-4db2-aec0-3310f11dddc7")


def globus_access_url(usgsIdentifier: str) -> str:
    """
    Helper function which constructs globus collection access url from usgsIdentifier.

    Example use:
        usgsIdentifier = 'USGS:1234-5678-9012-3456'
        globus_access_url(usgsIdentifier) == 'https://app.globus.org/file-manager?origin_id=0be095a6-c4e9-4db2-aec0-3310f11dddc7&origin_path=%2FUSGS%3A1234-5678-9012-3456&two_pane=false'
    """
    base = "https://app.globus.org/file-manager"
    query = {
        "origin_id": COLLECTION_ID,
        "origin_path": "/" + usgsIdentifier,
        "two_pane": "false",
    }
    query_string = "?" + urllib.parse.urlencode(query)
    return urllib.parse.urljoin(base, query_string)


def default_distribution(data: dict) -> list[Distribution]:
    """
    Default factory for DataReleaseInitiation.distribution
    """

    usgsIdentifier = data["usgsIdentifier"]
    identifier = data.get("identifier")

    distribution = [
        Distribution(
            title="Globus Guest Collection",
            description="Globus guest collection for accessing data via Globus transfer",
            accessURL=pydantic.HttpUrl(globus_access_url(usgsIdentifier)),
            format="HTML",
            mediaType="text/html",

            # TODO: Fix this, we probably want modifiedBy to be something other
            # than the publisher. Using publisher for now because it is
            # available.
            modifiedBy=data['publisher'],
            modified=datetime.now(),  # TODO: verify this assumption
            useForPreview=False,      # TODO: verify this assumption
        )
    ]

    if identifier:
        distribution.append(
            # TODO: Update the following distribution. It is missing required
            # fields modifiedBy, modified, and useForPreview.
            Distribution(
                title="Data Release",
                description="Data Release",
                accessURL=pydantic.HttpUrl(identifier),
                format="HTML",
                mediaType="text/html",
            )
        )

    return distribution


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
    versionHistory: VersionHistory | None = None


class DataReleaseInitiation(DataReleaseInitiationForm):
    """Basic metadata schema for initiating a data release.

    Fields
    ------
    
    usgsIdentifier: Identifier used to internally identify a resource within a particular system

    identifier: A unique identifier of the resource being described or cataloged.
        This identifier should be represented by a URI.

    usgsAssetType: The type of asset cataloged: data, model, publication, software
    usgsCreated: Date and time that the resource's record was created in the catalog
    usgsModified: Date and time that the resource's record was last modified
    accessRights: Information about who can access the resource or an indication of its security status.
    publisher: The entity responsible for making the resource available.
    distribution: An available distribution of the dataset.
    """
    
    usgsIdentifier: str

    identifier: pydantic.HttpUrl | None = None

    usgsAssetType: UsgsAssetTypeEnum = UsgsAssetTypeEnum.data
    usgsCreated: datetime = pydantic.Field(default_factory=datetime.now)
    usgsModified: datetime = pydantic.Field(default_factory=datetime.now)
    accessRights: AccessRightsEnum = AccessRightsEnum.public

    publisher: Entity = Entity(
        entity_id="https://ror.org/035a68863",
        name="United States Geological Survey",
        nameType="Organizational",
        nameIdentifier="https://ror.org/035a68863",
        email=None,
    )
    
    distribution: list[Distribution] = pydantic.Field(
        default_factory=default_distribution,
    )
    
    status: StatusEnum = StatusEnum.created
    usgsReleaseType: UsgsReleaseTypeEnum = UsgsReleaseTypeEnum.dataRelease
