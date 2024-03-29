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
# ⭐ Short list

Dive into our curated selection of online resources on scientific image analysis.

```{code-cell} ipython3
:tags: [remove-input]

from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)

import sys
from pathlib import Path

sys.path.append(str(Path.cwd().parents[0]))

from helpers import DATAFRAME_ONLINE_RESOURCES, show_online_resources

df_favourites = DATAFRAME_ONLINE_RESOURCES[DATAFRAME_ONLINE_RESOURCES['Favourite']].copy()
df_favourites.drop(['Favourite'], axis='columns', inplace=True)

show_online_resources(df_favourites, dom='lfrtip')
```