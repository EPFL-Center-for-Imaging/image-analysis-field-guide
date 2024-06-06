import pooch

DATASET = pooch.create(
    path=pooch.os_cache("field-guide"),  # default path
    base_url="https://zenodo.org/record/8099852/files/",
    registry={
        "deepslide.png": "md5:67d2dac6f327e2d3749252d46799861a",
    },
    env="SHARED_DATA",  # if exists, will overwrite `path`
    # # Specify custom URLs for some of the files in the registry.
    urls={
    },
)
