import pooch

DATASET = pooch.create(
    path=pooch.os_cache("field-guide"),  # default path
    base_url="https://zenodo.org/record/8099852/files/",
    registry={
        "drosophila_trachea.tif": "md5:d595ac271779936e255afd0508cca43f",
        "crystallites.tif": "md5:18d619a8f70114f2e5437e4713e45166",
        "lungs_ct.tif": "md5:80b294dc0a09fae7f861d0fa2bc7ab3c",
    },
    env="SHARED_DATA",  # if exists, will overwrite `path`
)