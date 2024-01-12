---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.0
kernelspec:
  display_name: image-analysis-field-guide
  language: python
  name: python3
---
# 💡 Notebook case studies

Browse our collection of Jupyter notebooks to learn more about scientific image processing and analysis in Python.

```{code-cell} ipython3
:tags: [remove-input]

import pandas as pd
from itables import init_notebook_mode
from itables import show
from pathlib import Path

init_notebook_mode(all_interactive=True, connected=True)

import sys
sys.path.append(str(Path.cwd().parents[2]))
from helpers import DATAFRAME_NOTEBOOK_CASE_STUDIES
df = DATAFRAME_NOTEBOOK_CASE_STUDIES.copy()
# df = pd.read_csv(Path.cwd().parents[3] / 'db' / 'notebook_case_studies.csv')

df["Title"] = [
    '<a href="./notebooks/{}">{}</a>'.format(link, name)
    for link, name in zip(df["Link"], df["Title"])
]

df["Image"] = [
    '<img src="../../../_images/{}" alt="Image" width="500">'.format(image)
    for image in df["Image"]
]

df.drop(['Link', 'Keywords'], axis='columns', inplace=True)

show(
    df,
    classes="display compact", 
    columnDefs=[
        {"className": "dt-left", "targets": [0, 1]}
    ],
    paging=False,
    showIndex=False,
)
```