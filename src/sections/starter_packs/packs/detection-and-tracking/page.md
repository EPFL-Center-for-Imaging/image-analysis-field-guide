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
![tracking](../../../../images/tracking_lg.png)

# 🐾 Detection and tracking

Objects of interest can be detected via keypoints, bounding boxes, shapes (e.g. lines, circles), or segmentation masks. In timeseries (movies), following objects across frames is known as tracking.

```{code-cell} ipython3
:tags: [remove-input]
tags = ["Object detection", "Tracking"]
```

## 🌐 Online resources

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

## 💡 Notebook case studies

```{code-cell} ipython3
:tags: [remove-input]

df = filter_notebook_case_studies(tags)
show_notebook_case_studies(df)
```

## 🛠️ Software tools

```{code-cell} ipython3
:tags: [remove-input]

df = filter_software_tools(tags)
show_software_tools(df)
```