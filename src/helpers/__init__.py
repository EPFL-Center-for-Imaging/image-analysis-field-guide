from itables import show
from functools import partial
from typing import List
import os

from helpers.notion_api import get_online_resources_dataframe, get_software_tools_dataframe

DATAFRAME_ONLINE_RESOURCES = get_online_resources_dataframe()
DATAFRAME_SOFTWARE_TOOLS = get_software_tools_dataframe()

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


def process_link(ipath):
    # # Replace the extension
    processed_link = ipath.replace(".ipynb", ".html")

    # Split what is after /src/ - that is the relative path after the base URL
    base, relpath = str(processed_link).split('/src/')

    deploy_url = os.getenv("DEPLOY_URL", base+'/src/_build/html/')

    processed_link = deploy_url + relpath

    return processed_link


def filter_software_tools(tags: List[str]):
    df = DATAFRAME_SOFTWARE_TOOLS.copy()
    mask = df['Used for'].str.contains('|'.join(tags), na=False)
    filtered_df = df[mask].copy()
    filtered_df.drop(['Used for', 'Keywords', 'Favourite'], axis='columns', inplace=True)

    return filtered_df


if __name__ == '__main__':
    print(DATAFRAME_SOFTWARE_TOOLS.head())
    print(DATAFRAME_ONLINE_RESOURCES.head())