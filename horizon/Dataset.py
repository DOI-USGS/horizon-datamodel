from datetime import datetime, date
from enum import Enum

from pydantic import BaseModel, HttpUrl

from .CatalogedResource import CatalogedResource
from .Distribution import Distribution
from .Entity import Entity, Creator, Contributor
from .License import License
from .Location import Location


class Keyword(BaseModel):
    """A keyword or tag describing the resource.
    concept: The keyword or tag
    conceptScheme: The name of the scheme or classification code or authority
        (e.g., USGS Thesaurus)
    conceptUri: The URI of the concept
    """

    concept: str
    conceptScheme: str | None = None
    conceptUri: HttpUrl | None = None


class DataciteRelationTypeEnum(str, Enum):
    """Description of the relationship of the resource being described and the related resource."""

    IsCitedBy = "IsCitedBy"
    Cites = "Cites"
    IsSupplementTo = "IsSupplementTo"
    IsSupplementedBy = "IsSupplementedBy"
    IsContinuedBy = "IsContinuedBy"
    Continues = "Continues"
    IsNewVersionOf = "IsNewVersionOf"
    IsPreviousVersionOf = "IsPreviousVersionOf"
    IsPartOf = "IsPartOf"
    HasPart = "HasPart"
    IsReferencedBy = "IsReferencedBy"
    References = "References"
    IsDocumentedBy = "IsDocumentedBy"
    Documents = "Documents"
    IsCompiledBy = "IsCompiledBy"
    Compiles = "Compiles"
    IsVariantFormOf = "IsVariantFormOf"
    IsOriginalFormOf = "IsOriginalFormOf"
    IsIdenticalTo = "IsIdenticalTo"
    HasMetadata = "HasMetadata"
    IsMetadataFor = "IsMetadataFor"
    Reviews = "Reviews"
    IsReviewedBy = "IsReviewedBy"
    IsDerivedFrom = "IsDerivedFrom"
    IsSourceOf = "IsSourceOf"
    Describes = "Describes"
    IsDescribedBy = "IsDescribedBy"
    HasVersion = "HasVersion"
    IsVersionOf = "IsVersionOf"
    Requires = "Requires"
    IsRequiredBy = "IsRequiredBy"
    Obsoletes = "Obsoletes"
    IsObsoletedBy = "IsObsoletedBy"
    IsPublishedIn = "IsPublishedIn"


class RelatedIdentifierTypeEnum(str, Enum):
    """The type of related identifier."""

    ARK = "ARK"
    arXiv = "arXiv"
    bibcode = "bibcode"
    DOI = "DOI"
    EAN13 = "EAN13"
    EISSN = "EISSN"
    Handle = "Handle"
    IGSN = "IGSN"
    ISBN = "ISBN"
    ISSN = "ISSN"
    ISTC = "ISTC"
    LISSN = "LISSN"
    LSID = "LSID"
    PMID = "PMID"
    PURL = "PURL"
    UPC = "UPC"
    URL = "URL"
    URN = "URN"
    w3id = "w3id"


class RelatedIdentifier(BaseModel):
    """Identifier of related resource.

    Fields
    ------
    dataciteRelationType: Description of the relationship of the resource being
        described and the related resource.
    relatedIdentifier: The identifier of the related resource.
    isPrimaryRelatedIdentifier: An indication if the related resource was
        developed alongside the cataloged resource and thus critical to the
        complete understanding of the cataloged resource.
    relatedIdentifierType: The type of related identifier.
    description: A free-text description of the related resource.
    """

    dataciteRelationType: DataciteRelationTypeEnum
    relatedIdentifier: str
    isPrimaryRelatedIdentifier: bool  
    relatedIdentifierType: RelatedIdentifierTypeEnum
    description: str | None = None


class AlternateIdentifierTypeEnum(str, Enum):
    """The type of alternate identifier

    "ARK", "Servcat Number", "Genbank Accession Number",
    "IGSN", "LSID", "PURL", "Ref Seq ID", "Local Identifier",
    "Metadata Identifier", "ScienceBase Alt ID"
    """

    ARK = "ARK"
    ServcatNumber = "Servcat Number"
    GenbankAccessionNumber = "Genbank Accession Number"
    IGSN = "IGSN"
    LSID = "LSID"
    PURL = "PURL"
    RefSeqID = "Ref Seq ID"
    LocalIdentifier = "Local Identifier"
    MetadataIdentifier = "Metadata Identifier"
    ScienceBaseAltID = "ScienceBase Alt ID"


class AlternateIdentifier(BaseModel):
    """An identifier or identifiers other than the primary Identifier applied to the resource being registered.

    Fields
    ------
    alternateIdentifier: An identifier or identifiers other than the primary Identifier
        applied to the resource being registered.
    alternateIdentifierType: The type of alternate identifier
    """

    alternateIdentifier: str
    alternateIdentifierType: AlternateIdentifierTypeEnum


class PeriodOfTime(BaseModel):
    """An interval of time that is named or defined by its start and end dates.
    Or a single date.
    The interval can be open. For example, it can have just a start or just an end.

    In DCAT, temporal must be a string with two iso-8601 datetimes separated by
    '/'. We retain a list here and defer the conversion to DCAT's preference in
    the serialization.

    Fields
    ------
    startDate: The start of the period.
    endDate: The end of the period.
    singleDate: A single date.
    """

    startDate: date | None = None
    endDate: date | None = None
    singleDate: date | None = None
    

class UsgsDataSource(BaseModel):
    """The USGS Science Center or Program responsible for managing the resource.

    The name and dataSourceId should come from Gluebucket.
    """

    name: str
    dataSourceId: str


class UsgsMissionArea(BaseModel):
    """The USGS Mission Area responsible for managing the resource.

    The Mission Area name and ID should come from Gluebucket service.
    """

    name: str
    missionAreaId: str


class VersionHistory(BaseModel):
    """Description of versions of the dataset described within a given identifier.


    version: The version indicator (name or identifier) of a resource.
    issued: Date of formal issuance (e.g., publication) of the resource.
    usgsApprovalIdentifier: The identifier associated with the record of approval for
        the version of the resource.
    versionNotes: A description of changes between this version and the
        previous version of the resource
    """

    version: str | None = None
    issued: date | None = None
    usgsApprovalIdentifier: str | None = None
    versionNotes: str | None = None


class Dataset(CatalogedResource):
    """A collection of data, published or curated by a single agent, and available for access or download in one or more representations.

    Fields
    ------
    usgsCitation: The recommended citation for the resource.

    issued: Date of formal issuance (e.g., publication) of the resource.
    modified: Most recent date on which the resource was changed, updated or modified.
    temporal: The temporal period that the dataset covers.

    creator: The entity responsible for producing the resource.
    contactPoint: Relevant contact information for the cataloged resource.
    usgsMetadataContactPoint: The entity responsible for creating and
        maintaining the metadata for the resource.
    usgsDataSource: The USGS Science Center or Program responsible for managing
        the resource.
    usgsMissionArea: The USGS Mission Area responsible for managing the resource.
    qualifiedAttribution: Link to an Agent having some form of responsibility
        for the resource
    publisher: The entity responsible for making the resource available.

    distribution: An available distribution of the dataset.

    license: A legal document under which the resource is made available.
    usgsPurpose: A summary of the intentions with which the resource was developed
    keyword: A keyword or tag describing the resource.
    systemKeyword: Keywords used internally for system operations, queries, or application logic.
    spatial: The geographical area covered by the dataset.
    relation: A resource with a relationship to the cataloged resource. This
        property includes DCAT sub-properties hasPart, isReferencedBy,
        previousVersion, replaces.
    alternateIdentifier: An identifier or identifiers other than the primary
        Identifier applied to the resource being registered.
    versionHistory: Description of versions of the dataset described within a
        given identifier.
    """
    usgsCitation: str

    issued: date
    modified: datetime | None = None
    temporal: PeriodOfTime | None = None

    # Contacts / Entities
    creator: list[Creator]
    contactPoint: Entity
    usgsMetadataContactPoint: Entity
    usgsDataSource: UsgsDataSource
    usgsMissionArea: UsgsMissionArea | None = None
    qualifiedAttribution: list[Contributor] | None = None
    publisher: Entity

    # Resource Access
    distribution: list[Distribution]

    # Additional descriptors
    license: License
    usgsPurpose: str | None = None
    keyword: list[Keyword] | None = None
    systemKeyword: list[Keyword] | None = None
    spatial: Location | None = None
    relation: list[RelatedIdentifier] | None = None
    alternateIdentifier: list[AlternateIdentifier] | None = None
    versionHistory: list[VersionHistory] | None = None
