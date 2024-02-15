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
# 💡 Jupyter notebooks

Browse our collection of Jupyter notebooks to learn more about scientific image processing and analysis in Python.

````{admonition} Launch the notebooks
If you are in EPFL, you can launch the notebooks to run them interactively on our `Jupyter Hub` by clicking on the rocket icon (🚀) at the top of this page.
```{image} ../../../images/jupyterhub.png
:align: center
```
````

## Tutorials

```{code-cell} ipython3
:tags: [remove-input]

from itables import init_notebook_mode

init_notebook_mode(all_interactive=True, connected=True)

import sys
from pathlib import Path

sys.path.append(str(Path.cwd().parents[2]))

from helpers import DATAFRAME_NOTEBOOK_CASE_STUDIES, show_notebook_case_studies

df = DATAFRAME_NOTEBOOK_CASE_STUDIES.copy()

df["Image"] = [
    '<img src="../../../_images/{}" alt="Image" width="500">'.format(image)
    for image in df["Image"]
]

df["Title"] = [
    '<a href="{}">{}</a>'.format(str(link).replace('/src/', '/src/_build/html/'), name)
    for link, name in zip(df["Link"], df["Title"])
]

# Create the tutorials table
df_tutorials = df[df['Keywords'].str.contains('Tutorial')].copy()

df_tutorials.drop(['Link', 'Description', 'Keywords'], axis='columns', inplace=True)

show_notebook_case_studies(df_tutorials)
```

## Case studies from EPFL

```{code-cell} ipython3
:tags: [remove-input]

# Create the case studies table
df_case_studies = df[~(df['Keywords'].str.contains('Tutorial'))].copy()

df_case_studies["Title"] = [
    '<a href="{}">{}</a>'.format(str(link).replace('/src/', '/src/_build/html/'), name)
    for link, name in zip(df_case_studies["Link"], df_case_studies["Title"])
]

df_case_studies.drop(['Link', 'Description', 'Keywords'], axis='columns', inplace=True)

show_notebook_case_studies(df_case_studies)
```