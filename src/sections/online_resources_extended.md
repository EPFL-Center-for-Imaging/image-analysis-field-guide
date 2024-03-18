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
# 🔄 Extended list

Browse our extended list of online resources on scientific image analysis.

```{admonition} Contribute
Do you want to add a resource to our list? Fill-in our [Google Form](https://forms.gle/FBDZjyRdwX1Mz3sR8) and we'll be happy to review your suggestion.
```

```{code-cell} ipython3
:tags: [remove-input]
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)

import sys
from pathlib import Path

sys.path.append(str(Path.cwd().parents[0]))

from helpers import DATAFRAME_ONLINE_RESOURCES, show_online_resources

df = DATAFRAME_ONLINE_RESOURCES.copy()
df.drop(['Favourite'], axis='columns', inplace=True)

show_online_resources(df, dom='lfrtip')
```