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
    algorithm: Identifies the algorithm used to produce the subject Checksum
        (should use SPDX)
    checksumValue: The checksumValue property provides a lowercase hexadecimal
        encoded digest value produced using a specific algorithm
    """

    algorithm: str
    checksumValue: str


class Distribution(BaseModel):
    """A specific representation of a dataset.

    Fields
    ------
    title: User added free text description of the distribution. We could use
        this field for filename and description for user-provided free text
    name: filename for downloadable files
    description: Description of the type of distribution (e.g., Landing Page,
        Original Metadata, WMS Service)
    format: Should only be used if IANA Media Type is not available
        https://www.iana.org/assignments/media-types/media-types.xhtml
        If IANA Media Type is available mediaType property should be used.
    mediaType: Must be from https://www.iana.org/assignments/media-types/media-types.xhtml
    conformsTo: An established standard to which the distribution conforms.
        Used to indicate the model, schema, ontology, view or profile that this
        representation of a dataset conforms to.
        Example: "https://www.fgdc.gov/schemas/metadata/"
    downloadURL: The URL of the downloadable file in a given format.
    accessURL: A URL of the resource that gives access to a distribution of the dataset.
    byteSize: The size of a distribution in bytes.
    checksum: Checksum value and algorithm that enables integrity checks of the
        contents of a file.
    modifiedBy: The person or service that last modified the distribution
        information or uploaded the file.
    modified: The timestamp of when the distribution was last modified
    useForPreview: Boolean indication if an image file should be used as a
        preview image. We may need a special preview class to make this work.
    """

    title: str | None = None
    name: str | None = None
    description: str | None = None
    format: str | None = None
    mediaType: str | None = None
    conformsTo: HttpUrl | None = None
    downloadURL: HttpUrl | None = None
    accessURL: HttpUrl | None = None
    byteSize: int | None = None
    checksum: Checksum | None = None
    modifiedBy: Entity | None = None
    modified: datetime | None = None
    useForPreview: bool | None = None
