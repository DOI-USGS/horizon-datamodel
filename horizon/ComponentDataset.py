from .Dataset import Dataset


class Component(Dataset):
    """
    A component is a semantically meaningful subset of a dataset, such as a
    logical grouping of files, distributions, or data products. Components
    support modular metadata and improved discoverability within complex datasets.

    Attributes
    ----------
    isCatalogRecord: Indicates whether this component should be independently cataloged as a record.
    componentName: A system-aligned name for the component, typically matching a directory or folder name.
    """
    isCatalogRecord: bool | None = None
    componentName: str


class ComponentDataset(Dataset):
    """
    A subclass of Dataset that introduces the concept of components—distinct,
    semantically meaningful groupings of distributions or files within the dataset.
    This structure supports more granular metadata and improved discoverability of
    dataset parts.

    Fields
    ------
    isCatalogRecord: Boolean indication if the metadata should be cataloged
        independently from the Dataset
    component: A list of components or subsets of the dataset, each with its own metadata.
    A container for holding components or subsets of the overall
        Dataset that require additional metadata to be discovered and understood.
    """

    component: list[Component] | None = None
    

