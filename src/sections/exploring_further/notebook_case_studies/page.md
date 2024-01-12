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

````{admonition} Launch the notebooks
Launch the notebooks to run them interactively on our `Jupyter Hub` by clicking on the rocket icon (🚀) at the top of this page (only EPFL).
```{image} ../../../images/jupyterhub.png
:align: center
```
````

```{code-cell} ipython3
:tags: [remove-input]

from itables import init_notebook_mode

init_notebook_mode(all_interactive=True, connected=True)

import sys
from pathlib import Path

sys.path.append(str(Path.cwd().parents[2]))

from helpers import DATAFRAME_NOTEBOOK_CASE_STUDIES, show_notebook_case_studies

df = DATAFRAME_NOTEBOOK_CASE_STUDIES.copy()

df["Title"] = [
    '<a href="./notebooks/{}">{}</a>'.format(link, name)
    for link, name in zip(df["Link"], df["Title"])
]

df["Image"] = [
    '<img src="../../../_images/{}" alt="Image" width="500">'.format(image)
    for image in df["Image"]
]

df.drop(['Link', 'Keywords', 'Description'], axis='columns', inplace=True)

show_notebook_case_studies(df)
```