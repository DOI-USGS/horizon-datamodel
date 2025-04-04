from pydantic import BaseModel


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
    point_longitude: Longitude decimal degrees: -180 to 180
    point_latitude: Latitude decimal degrees: -90 to 90

    """

    pointLongitude: str
    pointLatitude: str


class Location(BaseModel):
    """A spatial region of named place

    Fields
    ------
    geometry: Geometry
        Not included in initial schema. Could be added in the future
    bbox: The spatial limits of a bounding box.
    centroid: The longitude and latitude coordinates of the Location's centroid
    """

    bbox: BoundingBox | None = None
    centroid: Centroid | None = None
