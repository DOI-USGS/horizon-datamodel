from enum import Enum

from pydantic import BaseModel


class NameTypeEnum(str, Enum):
    """The type of entity described by a name

    usgs_personal = "USGS Personal"
        USGS Federal staff or contractors
    personal = "Personal"
        Person who is not affiliated with USGS or a USGS contractor
    organizational = "Organizational"
        A government, nonprofit, research, or other organization
    service = "Service"
        Software that performs automated tasks
    """

    usgs_personal = "USGS Personal"
    personal = "Personal"
    organizational = "Organizational"
    service = "Service"


class ContributorTypeEnum(str, Enum):
    """The type of contributor of the resource.

    See DataCite Metadata Schema for definitions: https://schema.datacite.org/
    """

    ContactPerson = "Contact Person"
    DataCollector = "Data Collector"
    DataCurator = "Data Curator"
    DataManager = "Data Manager"
    Distributor = "Distributor"
    Editor = "Editor"
    HostingInstitution = "Hosting Institution"
    Producer = "Producer"
    ProjectLeader = "Project Leader"
    ProjectManager = "Project Manager"
    ProjectMember = "Project Member"
    RegistrationAgency = "Registration Agency"
    RegistrationAuthority = "Registration Authority"
    RelatedPerson = "Related Person"
    Researcher = "Researcher"
    ResearchGroup = "Research Group"
    RightsHolder = "Rights Holder"
    Sponsor = "Sponsor"
    Supervisor = "Supervisor"
    WorkPackageLeader = "Work Package Leader"
    Other = "Other"


class Entity(BaseModel):
    """Person, Organization, or Service related to a resource

    Fields
    ------
    entity_id: str | None = None
        Identifier to uniquely identify an entity within a given system
    name: str
        Name by which an entity is known
    nameType: NameTypeEnum | None = None
        The type of entity described by a name
    nameIdentifier: str | None = None
        A globally unique persistent identifier for an entity (e.g., ORCID iD, ROR ID).

    """

    entity_id: str | None = None
    name: str
    nameType: NameTypeEnum | None = None
    nameIdentifier: str | None = None
    email: str | None = None


class Creator(Entity):
    """The entity responsible for producing the resource.

    Fields
    ------
    position: int
        Position that the creator appears within a citation
    affiliation: str | None = None
        The organization with which a creator is affiliated
    affiliationIdentifier: str | None = None
        A globally unique persistent identifier for the affiliated organization.
    """

    position: int
    affiliation: str | None = None
    affiliationIdentifier: str | None = None


class Contributor(Creator):
    """The institution or person responsible for collecting, managing, distributing,
    or otherwise contributing to the development of the resource.

    Fields
    ------
    contributorType: ContributorTypeEnum
        The type of contributor of the resource.
    """

    contributorType: ContributorTypeEnum
