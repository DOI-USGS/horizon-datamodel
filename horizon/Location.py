from pydantic import BaseModel


class BoundingBox(BaseModel):
    """The spatial limits of a bounding box.

    Fields
    ------
    westBoundLongitude: float
        Western longitudinal dimension of the bounding box: -180 -180
    eastBoundLongitude: float
        Eastern longitudinal dimension of the bounding box: -180 -180
    southBoundLatitude: float
        Southern latitudinal dimensions of the bounding box: -90 -90
    northBoundLatitude: float
        Northern latitudinal dimensions of the bounding box: -90 -90

    """

    westBoundLongitude: float
    eastBoundLongitude: float
    southBoundLatitude: float
    northBoundLatitude: float


class Centroid(BaseModel):
    """The longitude and latitude coordinates of the Location's centroid

    Fields
    ------
    point_longitude: float
        Longitude decimal degrees: -180 -180

    point_latitude: float
        Latitude decimal degrees: -90 -90

    """

    pointLongitude: float
    pointLatitude: float


class Location(BaseModel):
    """A spatial region of named place

    Fields
    ------
    geometry: Geometry
        Not included in initial schema. Could be added in the future
    bbox: BoundingBox
        The spatial limits of a bounding box.
    centroid: Centroid
        The longitude and latitude coordinates of the Location's centroid
    """

    bbox: BoundingBox | None
    centroid: Centroid | None
