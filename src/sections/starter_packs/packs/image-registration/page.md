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
![registration](../../../../images/registration_lg.png)

# 📐 Image registration

Image registration can be used to align multiple images onto one another, to stabilize a sequence of images by compensating camera movement, to track the movement and deformation of objects, and for image stitching of multiple fields of view, for example.

```{code-cell} ipython3
:tags: [remove-input]
tags = ["Image registration"]
```

## 🎓 Learning resources

```{code-cell} ipython3
:tags: [remove-input]

from itables import init_notebook_mode
from pathlib import Path
import sys
sys.path.append(str(Path.cwd().parents[3]))
from helpers import *

init_notebook_mode(all_interactive=True, connected=True)

df = filter_online_resources(tags)
show_online_resources(df, dom="tr")
```

## 💡 Jupyter notebooks

### Tutorials

```{code-cell} ipython3
:tags: [remove-input]

df = filter_notebook_case_studies(tags)

df_tutorials = df[df['Keywords'].str.contains('Tutorial')].copy()
df_tutorials.drop('Keywords', axis='columns', inplace=True)

show_notebook_case_studies(df_tutorials)
```

### Case studies from EPFL

```{code-cell} ipython3
:tags: [remove-input]

df = filter_notebook_case_studies(tags)

df_case_studies = df[~(df['Keywords'].str.contains('Tutorial'))].copy()
df_case_studies.drop('Keywords', axis='columns', inplace=True)

show_notebook_case_studies(df_case_studies)
```

## 🛠️ Software tools

```{code-cell} ipython3
:tags: [remove-input]

df = filter_software_tools(tags)
show_software_tools(df)
```