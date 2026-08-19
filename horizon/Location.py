from pydantic import BaseModel
from typing import Literal, Union

class BoundingBox(BaseModel):
    """The spatial limits of a bounding box.

    Fields
    ------
    westBoundLongitude: Western longitudinal dimension of the bounding box: -180 to 180
    eastBoundLongitude: Eastern longitudinal dimension of the bounding box: -180 to 180
    southBoundLatitude: Southern latitudinal dimensions of the bounding box: -90 to 90
    northBoundLatitude: Northern latitudinal dimensions of the bounding box: -90 to 90

    """

    westBoundLongitude: str
    eastBoundLongitude: str
    southBoundLatitude: str
    northBoundLatitude: str


class Centroid(BaseModel):
    """The longitude and latitude coordinates of the Location's centroid

    Fields
    ------
    pointLongitude: Longitude decimal degrees: -180 to 180
    poinLatitude: Latitude decimal degrees: -90 to 90

    """

    pointLongitude: str
    pointLatitude: str



class PolygonGeometry(BaseModel):
    """
    A GeoJSON Polygon geometry.

    Fields
    ------
    type: Polygon
    coordinates: A list of linear rings, each a list of [lon, lat] pairs. The first ring is the outer boundary.
    """

    type: Literal["Polygon"]
    coordinates: list[list[list[float]]]


class MultiPolygonGeometry(BaseModel):
    """
    A GeoJSON MultiPolygon geometry.

    Fields
    ------
    type: MultiPolygon
    coordinates: A list of polygons, each a list of linear rings, each a list of [lon, lat] pairs.
    """

    type: Literal["MultiPolygon"]
    coordinates: list[list[list[list[float]]]]


# Union type for geometry field
Geometry = Union[PolygonGeometry, MultiPolygonGeometry]


class Location(BaseModel):
    """A spatial region of named place

    Fields
    ------
    
    bbox: The spatial limits of a bounding box.
    centroid: The longitude and latitude coordinates of the Location's centroid
    geometry: A GeoJSON geometry object representing the spatial extent (e.g., Polygon or MultiPolygon).
    """

    bbox: BoundingBox | None = None
    centroid: Centroid | None = None
    geometry: Geometry | None = None
