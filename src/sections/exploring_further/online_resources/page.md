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

from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)

import sys
from pathlib import Path

sys.path.append(str(Path.cwd().parents[2]))

from helpers import DATAFRAME_ONLINE_RESOURCES, show_online_resources

show_online_resources(DATAFRAME_ONLINE_RESOURCES, dom='lfrtip')
```
