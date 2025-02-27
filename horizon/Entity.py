from datetime import datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl


class NameTypeEnum(str, Enum):
    """The type of entity described by a name

    Args:
        str (_type_): _description_
        Enum (_type_): _description_
    """

    usgs_personal = "USGS Personal"
    personal = "Personal"
    organizational = "Organizational"
    service = "Service"


class ContributorTypeEnum(str, Enum):
    """The type of contributor of the resource.

    Args:
        str (_type_): _description_
        Enum (_type_): _description_
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
    entity_id: str | None
        Identifier to uniquely identify an entity within a given system
    name: str
        Name by which an entity is known
    nameType: NameTypeEnum
        The type of entity described by a name
    nameIdentifier: str | None
        A globally unique persistent identifier for an entity (e.g., ORCID iD, ROR ID).

    """

    entity_id: str | None
    name: str
    nameType: NameTypeEnum
    nameIdentifier: str | None
    email: str | None


class Creator(Entity):
    """The entity responsible for producing the resource.

    Fields
    ------
    position: int
        Position that the creator appears within a citation
    affiliation: str | None
        The organization with which a creator is affiliated
    affiliationIdentifier: str | None
        A globally unique persistent identifier for the affiliated organization.
    """

    position: int
    affiliation: str | None
    affiliationIdentifier: str | None


class Contributor(Creator):
    """The institution or person responsible for collecting, managing, distributing,
    or otherwise contributing to the development of the resource.

    Fields
    ------
    contributorType: ContributorTypeEnum
        The type of contributor of the resource.
    """

    contributorType: ContributorTypeEnum
