import pooch

DATASET = pooch.create(
    path=pooch.os_cache("field-guide"),  # default path
    base_url="https://zenodo.org/record/8099852/files/",
    registry={
    },
    env="SHARED_DATA",  # if exists, will overwrite `path`
)