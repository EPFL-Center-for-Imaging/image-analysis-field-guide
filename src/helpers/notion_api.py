import requests
import os
import pandas as pd
from typing import List

from dotenv import load_dotenv

load_dotenv()

ONLINE_RESOURCES_DATABASE_ID = "b056be0b6f22499eb08c0d466c082686"
SOFTWARE_TOOLS_DATABASE_ID = "043e925d562a4d688d83fd8f6a2aad07"

def get_online_resources_dataframe() -> pd.DataFrame:
    online_resources_data = query_notion_database(ONLINE_RESOURCES_DATABASE_ID)
    items = parse_online_resources(online_resources_data)
    df = pd.DataFrame(items)

    df["Name"] = [
        '<a href="{}">{}</a>'.format(link, name)
        for link, name in zip(df["Link"], df["Name"])
    ]

    df.drop('Link', axis='columns', inplace=True)

    df["Keywords"] = [
        ''.join(['<button class="btn btn-light btn-xs" onclick="insertText(this)" style="padding: 1px; margin: 4px 2px; font-size: 12px;">{}</button>'.format(keyword) for keyword in [kw for kw in str(keywords).split(', ') if kw != 'nan']])
        for keywords in df["Keywords"]
    ]

    return df

def get_software_tools_dataframe() -> pd.DataFrame:
    software_tools_data = query_notion_database(SOFTWARE_TOOLS_DATABASE_ID)
    items = parse_software_tools(software_tools_data)
    df = pd.DataFrame(items)

    df["Software tool"] = [
        '<a href="{}">{}</a>'.format(link, name)
        for link, name in zip(df["Homepage"], df["Software tool"])
    ]

    df.drop(['Homepage'], axis='columns', inplace=True)

    df["Used for"] = [
        ''.join(['<button class="btn btn-light btn-xs" onclick="insertText(this)" style="padding: 1px; margin: 4px 2px; font-size: 12px;">{}</button>'.format(keyword) for keyword in [kw for kw in str(keywords).split(', ') if kw != 'nan']])
        for keywords in df["Used for"]
    ]

    df["Keywords"] = [
        ''.join(['<button class="btn btn-light btn-xs" onclick="insertText(this)" style="padding: 1px; margin: 4px 2px; font-size: 12px;">{}</button>'.format(keyword) for keyword in [kw for kw in str(keywords).split(', ') if kw != 'nan']])
        for keywords in df["Keywords"]
    ]

    return df

def parse_online_resources(data: dict) -> List[dict]:
    """Extract data from the raw Notion database contents."""
    items = []

    for page_contents in data.get('results'):
        page_title = page_contents['properties']['Name']['title'][0]['plain_text']
        page_url = page_contents['properties']['Name']['title'][0]['href']
        all_keywords = [keyword['name'] for keyword in page_contents['properties']['Keywords']['multi_select']]
        all_keywords = ', '.join(all_keywords)

        items.append({
            'Name': page_title,
            'Link': page_url,
            'Keywords': all_keywords
        })

    return items

def parse_software_tools(data: dict) -> List[dict]:
    """
    Extract data from the raw Notion database contents.
    """
    items = []

    for page_contents in data.get('results'):
        page_name = page_contents['properties']['Software tool']['title'][0]['plain_text']
        page_description = page_contents['properties']['Description']['rich_text'][0]['plain_text']
        page_url = page_contents['properties']['Homepage']['url']
        all_page_usage = [usage['name'] for usage in page_contents['properties']['Used for']['multi_select']]
        all_page_usage = ', '.join(all_page_usage)
        all_page_keywords = [keywords['name'] for keywords in page_contents['properties']['Keywords']['multi_select']]
        all_page_keywords = ', '.join(all_page_keywords)
        
        items.append({
            "Software tool": page_name,
            "Description": page_description,
            "Homepage": page_url,
            "Used for": all_page_usage,
            "Keywords": all_page_keywords,
        })

    return items

def query_notion_database(database_id: str) -> dict:
    """
    Query the Notion API to retreive the content of a database.
    """
    response = requests.post(
        url=f"https://api.notion.com/v1/databases/{database_id}/query",
        headers={
            "Notion-Version": "2022-06-28",
            "Authorization": f"Bearer {os.environ['NOTION_KEY']}",
            "Content-Type": "application/json"
        },
    )

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Error: {response.status_code} - {response.text}')


if __name__ == "__main__":
    # df_online_resources = get_online_resources_dataframe()
    # print(df_online_resources.head())
    # print(len(df_online_resources))

    # df_software_tools = get_software_tools_dataframe()
    # print(df_software_tools.head())
    # print(len(df_software_tools))

    import pdb; pdb.set_trace()