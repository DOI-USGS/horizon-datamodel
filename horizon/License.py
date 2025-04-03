from pydantic import BaseModel, HttpUrl


class License(BaseModel):
    """A legal document under which the resource is made available.

    licenseIdentifier: A short, standardized version of the license name.
    license: The full version of the license name or free text description of
        the license or rights associated with the resource.
    licenseUri: The URI of the license.
    licenseIdentifierScheme: The name of the license identifier scheme
    schemeUri: The URI of the licenseIdentifierScheme
    """

    licenseIdentifier: str | None = None
    license: str
    licenseUri: HttpUrl | None = None
    licenseIdentifierScheme: str | None = None
    schemeUri: HttpUrl | None = None
