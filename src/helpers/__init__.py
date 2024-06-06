from itables import show
from functools import partial
from typing import List

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


def filter_software_tools(tags: List[str]):
    df = DATAFRAME_SOFTWARE_TOOLS.copy()
    mask = df['Used for'].str.contains('|'.join(tags), na=False) | df['Keywords'].str.contains('|'.join(tags), na=False)
    filtered_df = df[mask].copy()
    filtered_df.drop(['Used for', 'Keywords', 'Favourite'], axis='columns', inplace=True)

    return filtered_df


if __name__ == '__main__':
    print(DATAFRAME_SOFTWARE_TOOLS.head())
    print(DATAFRAME_ONLINE_RESOURCES.head())