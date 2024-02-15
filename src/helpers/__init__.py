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
    filtered_df.drop(['Keywords', 'Favourite'], axis='columns', inplace=True)

    return filtered_df


def minimize(input_string: str):
    return '-'.join(input_string.lower().split())


def process_link(link):
    processed_link = str(link).replace('/src/', '/src/_build/html/')
    processed_link = processed_link.replace('/opt/src/_build/html', '')  # for docker (quick hack)
    return processed_link

def filter_notebook_case_studies(tags: List[str]):
    df = DATAFRAME_NOTEBOOK_CASE_STUDIES.copy()

    df["Title"] = [
        '<a href="{}#{}">{}</a>'.format(process_link(link), minimize(tags[0]), name)
        for link, name in zip(df["Link"], df["Title"])
    ]

    df["Image"] = [
        '<img src="../../../../_images/{}" alt="Image" width="300">'.format(image)
        for image in df["Image"]
    ]

    mask = df['Keywords'].str.contains('|'.join(tags), na=False)
    df = df[mask].copy()
    df.drop(['Link', 'Description'], axis='columns', inplace=True)

    return df


def filter_software_tools(tags: List[str]):
    df = DATAFRAME_SOFTWARE_TOOLS.copy()
    mask = df['Used for'].str.contains('|'.join(tags), na=False)
    filtered_df = df[mask].copy()
    filtered_df.drop(['Used for', 'Keywords', 'Favourite'], axis='columns', inplace=True)

    return filtered_df


if __name__ == '__main__':
    print(DATAFRAME_SOFTWARE_TOOLS.head())
    print(DATAFRAME_ONLINE_RESOURCES.head())
    print(DATAFRAME_NOTEBOOK_CASE_STUDIES.head())