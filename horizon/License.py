from pydantic import BaseModel, HttpUrl


class License(BaseModel):
    """A legal document under which the resource is made available.

    licenseIdentifier: str | None = None
        A short, standardized version of the license name.
    license: str
        The full version of the license name or free text description of the license or rights associated with the resource.
    licenseUri: str | None = None
        The URI of the license.
    licenseIdentifierScheme: str | None = None
        The name of the license identifier scheme
    schemeUri: str | None = None
        The URI of the licenseIdentifierScheme
    """

    licenseIdentifier: str | None = None
    license: str
    licenseUri: HttpUrl | None = None
    licenseIdentifierScheme: str | None = None
    schemeUri: HttpUrl | None = None
