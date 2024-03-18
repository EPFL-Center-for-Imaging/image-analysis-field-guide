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

Dive into our curated selection of software tools for scientific image analysis.

<!-- ## ⭐ Favourites -->

```{code-cell} ipython3
:tags: [remove-input]

from itables import init_notebook_mode

init_notebook_mode(all_interactive=True, connected=True)

import sys
from pathlib import Path

sys.path.append(str(Path.cwd().parents[0]))

from helpers import DATAFRAME_SOFTWARE_TOOLS, show_software_tools

df_favourites = DATAFRAME_SOFTWARE_TOOLS[DATAFRAME_SOFTWARE_TOOLS['Favourite']].copy()
df_favourites.drop(['Favourite'], axis='columns', inplace=True)

show_software_tools(df_favourites)
```

<!--
## ⬇ More tools

```{code-cell} ipython3
:tags: [remove-input]

df_non_favourites = DATAFRAME_SOFTWARE_TOOLS[~(DATAFRAME_SOFTWARE_TOOLS['Favourite'])].copy()
df_non_favourites.drop(['Favourite'], axis='columns', inplace=True)

show_software_tools(df_non_favourites)
```
-->
