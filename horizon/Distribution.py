from datetime import datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl

from .Entity import Entity

# Placeholder for Distribution Schema Definition


class CloudAssetStructureEnum(str, Enum):
    """Describes how the asset is organized in object storage.

    object: Single object/file (e.g., Cloud Optimized GeoTIFF, GeoParquet,
        NetCDF)
    partitioned-collection: Multiple independently readable data objects
        (e.g., Hive-partitioned Parquet, a directory of per-tile COGs)
    chunked-store: Multiple interdependent objects comprising one logical
        dataset; individual objects are not meaningful on their own
        (e.g., Zarr)
    """

    single_object = "object"
    partitioned_collection = "partitioned-collection"
    chunked_store = "chunked-store"


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
    title: Type of distribution (e.g., Data Landing Page,
        Data Release Metadata, Data File, Data Service, Globus Guest Collection, etc.)
    name: filename for downloadable files
    description: User added free text description of the distribution.
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
    allowPublicCloudAccess: Indicates whether the distribution is approved for
        public access in cloud object storage. If True, accessURL provides the
        URL of the publicly accessible cloud asset. If True and accessURL is
        None, the asset has not yet been published to public cloud storage
        (publication is in process and the asset is not yet available).
        If False, the distribution is not to be made publicly accessible in
        cloud storage. None means not applicable or not yet determined.
    cloudAssetStructure: Describes how the asset is organized in object storage.
        For "object", accessURL points to the object itself. For
        "partitioned-collection" and "chunked-store", accessURL points to a
        metadata or manifest file that describes the collection or store.
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
    allowPublicCloudAccess: bool | None = None
    cloudAssetStructure: CloudAssetStructureEnum | None = None
    byteSize: int | None = None
    checksum: Checksum | None = None
    modifiedBy: Entity | None = None
    modified: datetime | None = None
    useForPreview: bool | None = None
