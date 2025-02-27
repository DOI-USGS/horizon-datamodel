from pydantic import BaseModel, HttpUrl


class License(BaseModel):
    """A legal document under which the resource is made available.

    licenseIdentifier: str | None
        A short, standardized version of the license name.
    license: str
        The full version of the license name or free text description of the license or rights associated with the resource.
    licenseUri: str | None
        The URI of the license.
    licenseIdentifierScheme: str | None
        The name of the license identifier scheme
    schemeUri: str | None
        The URI of the licenseIdentifierScheme
    """

    licenseIdentifier: str | None
    license: str
    licenseUri: HttpUrl | None
    licenseIdentifierScheme: str | None
    schemeUri: HttpUrl | None
