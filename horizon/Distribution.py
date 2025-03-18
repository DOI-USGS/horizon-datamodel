from datetime import datetime

from pydantic import BaseModel, HttpUrl

from .Entity import Entity

# Placeholder for Distribution Schema Definition


class Checksum(BaseModel):
    """A Checksum is a value that allows to check the integrity of the contents of a file.

    Even small changes to the content of the file will change its checksum.
    This class allows the results of a variety of checksum and cryptographic message digest
    algorithms to be represented.

    Fields
    ------
    algorithm: str
        Identifies the algorithm used to produce the subject Checksum (should use SPDX)
    checksumValue: str
        The checksumValue property provides a lowercase hexadecimal
        encoded digest value produced using a specific algorithm
    """

    algorithm: str
    checksumValue: str


class Distribution(BaseModel):
    """A specific representation of a dataset.

    Fields
    ------
    title: str | None
        User added free text description of the distribution.
        We could use this field for filename and description for user-provided free text
    name: str | None
        filename for downloadable files
    description: str | None
        Description of the type of distribution (e.g., Landing Page, Original Metadata, WMS Service)
    format: str | None
        Should only be used if IANA Media Type is not available
        https://www.iana.org/assignments/media-types/media-types.xhtml
        If IANA Media Type is available mediaType property should be used.
    mediaType: str
        Must be from https://www.iana.org/assignments/media-types/media-types.xhtml
    conformsTo: HttpUrl
        An established standard to which the distribution conforms. 
        Used to indicate the model, schema, ontology, view or profile that this 
        representation of a dataset conforms to.
        Example: "https://www.fgdc.gov/schemas/metadata/"
    downloadURL: HttpUrl
        The URL of the downloadable file in a given format.
    accessURL: HttpUrl
        A URL of the resource that gives access to a distribution of the dataset.
    byteSize: int | None
        The size of a distribution in bytes.
    checksum: Checksum | None
        Checksum value and algorithm that enables integrity checks of the contents of a file.
    modifiedBy: Entity
        The person or service that last modified the distribution information or uploaded the file.
    modified: datetime
        The timestamp of when the distribution was last modified
    useForPreview: bool
        Boolean indication if an image file should be used as a preview image
        We may need a special preview class to make this work
    """

    title: str | None
    name: str | None
    description: str | None
    format: str | None
    mediaType: str | None
    conformsTo: HttpUrl | None
    downloadURL: HttpUrl | None
    accessURL: HttpUrl | None
    byteSize: int | None
    checksum: Checksum | None
    modifiedBy: Entity
    modified: datetime
    useForPreview: bool
