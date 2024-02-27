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
![segmentation](../../images/segmentation_lg.png)

# ✂️ Image segmentation

Image segmentation aims to produce a segmentation mask that identifies a particular class or object. Image segmentation can be approached by classical techniques such as thresholding, weakly supervised learning, or deep learning.

```{code-cell} ipython3
:tags: [remove-input]
tags = ["Image segmentation"]
```

## 🎓 Learning resources

Here is our curated list of free online resources on the topic of image segmentation.

```{code-cell} ipython3
:tags: [remove-input]

from itables import init_notebook_mode
from pathlib import Path
import sys
sys.path.append(str(Path.cwd().parents[1]))
from helpers import *

init_notebook_mode(all_interactive=True, connected=True)

df = filter_online_resources(tags)
show_online_resources(df, dom="tr")
```

## 💡 Tutorials

Check out our tutorial notebooks related to image segmentation.

```{nblinkgallery}
:glob:
../exploring_further/notebook_case_studies/notebooks/tutorials/segmentation_*
```

## 🛠️ Software tools

Take a look at these software tools to help you solve your image segmentation problems.

```{code-cell} ipython3
:tags: [remove-input]

df = filter_software_tools(tags)
show_software_tools(df)
```