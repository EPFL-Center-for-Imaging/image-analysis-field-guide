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
# 🌐 Online resources

Browse our curated list of online resources on the topic of scientific image analysis.

```{admonition} Contribute
Do you want to add a resource to our list? Fill-in our [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSeJojbinWxZz9js-XBPnWCxLdyfQcS0CUhe437fLCIrNvDBZw/viewform?usp=sf_link) and we'll be happy to review your suggestion.
```

```{code-cell} ipython3
:tags: [remove-input]

import pandas as pd
from itables import init_notebook_mode
from itables import show
from pathlib import Path

init_notebook_mode(all_interactive=True, connected=True)

import sys
sys.path.append(str(Path.cwd().parents[2]))
from helpers import DATAFRAME_ONLINE_RESOURCES
df = DATAFRAME_ONLINE_RESOURCES.copy()
# df = pd.read_csv(Path.cwd().parents[3] / 'db' / 'online_resources.csv')

df["Name"] = [
    '<a href="{}">{}</a>'.format(link, name)
    for link, name in zip(df["Link"], df["Name"])
]

df.drop('Link', axis='columns', inplace=True)

df["Keywords"] = [
    ''.join(['<button class="btn btn-light btn-xs" onclick="insertText(this)" style="padding: 1px; margin: 4px 2px; font-size: 12px;">{}</button>'.format(keyword) for keyword in [kw for kw in str(keywords).split(', ') if kw != 'nan']])
    for keywords in df["Keywords"]
]

# show(df, classes="display compact", paging=False)
show(
    df,
    classes="display compact", 
    columnDefs=[
        {"className": "dt-left", "targets": "_all"}
    ],
    style="width:100%;margin:auto",
    paging=False,
    showIndex=False,
)
```
