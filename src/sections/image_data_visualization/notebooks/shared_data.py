import pooch

DATASET = pooch.create(
    path=pooch.os_cache("field-guide"),  # default path
    base_url="https://zenodo.org/record/8099852/files/",
    registry={
        "grains.tif": "md5:38b46d0a9c1b7ca9c866c2a11138a65a",
        "drosophila_trachea.tif": "md5:d595ac271779936e255afd0508cca43f",
    },
    env="SHARED_DATA",  # if exists, will overwrite `path`
    # # Specify custom URLs for some of the files in the registry.
    urls={
    },
)
