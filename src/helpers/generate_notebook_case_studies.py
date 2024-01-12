"""
Generate the Notebook Case Studies data.

https://jupyterbook.org/en/stable/content/metadata.html
"""

import pandas as pd
import nbformat as nbf
import glob
import re
from pathlib import Path


def parse_cell(cell):
    """
    Extracts information from the first cell of an example notebook.
    """
    cell_source = cell['source']

    # Match the Markdown title
    title_pattern = r'\n#(\s*(.*?))\n'
    match = re.search(title_pattern, cell_source)
    title = match.group(1).strip() if match else ''

    # Match the image filename
    image_file_pattern = r'[a-zA-Z0-9_-]+\.(png|jpg|jpeg|gif)'
    match = re.search(image_file_pattern, cell_source)
    image_file = match.group() if match else ''

    # Match the description
    description_pattern = r'---(.*?)Tags:'
    match = re.search(description_pattern, cell_source, re.DOTALL)
    description = match.group(1).strip() if match else ''

    # Match the keywords
    keywords_pattern = r'Tags:(.*?)\s*$'
    match = re.search(keywords_pattern, cell_source, re.DOTALL)
    keywords = match.group(1).strip().replace('`', '') if match else ''

    return {
        'Title': title,
        'Description': description,
        'Image': image_file,
        'Keywords': keywords,
    }


def get_notebook_case_studies_dataframe():
    """
    Generates a dataframe of notebook case studies.
    """
    basedir = str(Path(__file__).parents[1] / 'sections')
    notebooks = glob.glob(f"{basedir}/**/*.ipynb", recursive=True)

    items = []
    for ipath in notebooks:
        ntbk = nbf.read(ipath, nbf.NO_CONVERT)

        parsed_info = parse_cell(ntbk.cells[0])
        parsed_info['Link'] = Path(ipath).name.replace('.ipynb', '.html')

        items.append(parsed_info)

    df = pd.DataFrame(items)


    
    return df


if __name__ == '__main__':
    df = get_notebook_case_studies_dataframe()
    print(df)