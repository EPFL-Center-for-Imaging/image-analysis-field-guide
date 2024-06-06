import pooch

DATASET = pooch.create(
    path=pooch.os_cache("field-guide"),  # default path
    base_url="https://zenodo.org/record/8099852/files/",
    registry={
        "snow_3d.tif": "md5:66c5130131f7707f5796c17916d70cc2",
        "M2EA05-01-bin4.tif": "md5:d8358c14acc5ae65aee67887201c1bb1",
        "M2EA05-05-bin4.tif": "md5:5a2d68d0d8425e9da7118c921d682a5f",
        "M2EA05-01-bin4-lab.tif": "md5:6f4eef96d25ca7f16209e029a26c6828",
    },
    env="SHARED_DATA",  # if exists, will overwrite `path`
    # # Specify custom URLs for some of the files in the registry.
    urls={
        "M2EA05-01-bin4.tif": "https://zenodo.org/record/7140837/files/M2EA05-01-bin4.tif",
        "M2EA05-05-bin4.tif": "https://zenodo.org/record/7140837/files/M2EA05-05-bin4.tif",
        "M2EA05-01-bin4-lab.tif": "https://zenodo.org/record/7140837/files/M2EA05-01-bin4-lab.tif",
    },
)
