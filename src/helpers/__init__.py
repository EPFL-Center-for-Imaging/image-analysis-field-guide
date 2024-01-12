from pathlib import Path
import pandas as pd
from itables import show
from functools import partial
from typing import List

from dotenv import load_dotenv
load_dotenv()

from helpers.notion_api import get_online_resources_dataframe, get_software_tools_dataframe
from helpers.generate_notebook_case_studies import get_notebook_case_studies_dataframe

DATAFRAME_ONLINE_RESOURCES = get_online_resources_dataframe()
DATAFRAME_SOFTWARE_TOOLS = get_software_tools_dataframe()
DATAFRAME_NOTEBOOK_CASE_STUDIES = get_notebook_case_studies_dataframe()

show_online_resources = partial(
    show,
    classes="display compact", 
    columnDefs=[
        {"width": "100%", "targets": [0]},
        {"className": "dt-left", "targets": [0]}
    ],
    style="width:100%;margin:auto",
    paging=False,
    showIndex=False,
)

show_notebook_case_studies = partial(
    show,
    classes="display compact", 
    columnDefs=[
        {"className": "dt-left", "targets": [0]}
    ],
    style="width:100%;margin:auto",
    paging=False,
    showIndex=False,
    dom="tr"
)

show_software_tools = partial(
    show,
    classes="display compact", 
    columnDefs=[
        {"className": "dt-left", "targets": "_all"}
    ],
    style="width:100%;margin:auto",
    paging=False,
    showIndex=False,
)


def filter_online_resources(tags: List[str]):
    df = DATAFRAME_ONLINE_RESOURCES.copy()
    mask = df['Keywords'].str.contains('|'.join(tags), na=False)
    filtered_df = df[mask].copy()
    filtered_df.drop('Keywords', axis='columns', inplace=True)

    return filtered_df


def minimize(input_string: str):
    return '-'.join(input_string.lower().split())


def filter_notebook_case_studies(tags: List[str]):
    df = DATAFRAME_NOTEBOOK_CASE_STUDIES.copy()

    df["Title"] = [
        '<a href="../../../exploring_further/notebook_case_studies/notebooks/{}#{}">{}</a>'.format(link, minimize(tags[0]), name)
        for link, name in zip(df["Link"], df["Title"])
    ]

    df["Image"] = [
        '<img src="../../../../_images/{}" alt="Image" width="300">'.format(image)
        for image in df["Image"]
    ]

    mask = df['Keywords'].str.contains('|'.join(tags), na=False)
    df = df[mask].copy()
    df.drop(['Link', 'Keywords', 'Description'], axis='columns', inplace=True)

    return df


def filter_software_tools(tags: List[str]):
    df = DATAFRAME_SOFTWARE_TOOLS.copy()
    mask = df['Used for'].str.contains('|'.join(tags), na=False)
    filtered_df = df[mask].copy()
    filtered_df.drop('Used for', axis='columns', inplace=True)

    return filtered_df


if __name__ == '__main__':
    print(DATAFRAME_SOFTWARE_TOOLS.head())
    print(DATAFRAME_ONLINE_RESOURCES.head())
    print(DATAFRAME_NOTEBOOK_CASE_STUDIES.head())