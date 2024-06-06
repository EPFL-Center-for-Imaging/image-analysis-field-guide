import pooch

DATASET = pooch.create(
    path=pooch.os_cache("field-guide"),  # default path
    base_url="https://zenodo.org/record/8099852/files/",
    registry={
        "cell_tracking_2d.tif": "md5:43f973785dcfbad38334fbf682a36d0f",
    },
    env="SHARED_DATA",  # if exists, will overwrite `path`
    # # Specify custom URLs for some of the files in the registry.
    urls={
    },
)
