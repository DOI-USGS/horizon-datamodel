from datetime import date

from pydantic import BaseModel, HttpUrl

from .Dataset import PeriodOfTime, Location, Keyword
from .Entity import Entity


class DataReleaseCSDGM(BaseModel):
    """Basic metadata schema for information translated from a Content Standard for Digital Geospatial Metadata record.

    Fields
    ------
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
    # Identification Information
    identifier: HttpUrl | None = None
    title: str
    description: str

    # Dates
    issued: date
    temporal: PeriodOfTime | None = None

    # Contacts
    contactPoint: Entity
    usgsMetadataContactPoint: Entity

    # Additional Descriptors
    usgsPurpose: str | None = None
    keyword: list[Keyword] | None = None
    spatial: Location | None = None
