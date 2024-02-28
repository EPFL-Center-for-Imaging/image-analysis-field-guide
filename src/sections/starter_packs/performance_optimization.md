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
![performance](../../images/performance_lg.jpeg)

# 🔋 Performance optimization

Once an image analysis pipeline is working, it may be time to think about  making it run faster.

```{code-cell} ipython3
:tags: [remove-input]
tags = ["Optimization"]
```

## 🎓 Learning resources

Here is our curated list of free online resources on the topic of performance optimization.

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

Check out our tutorial notebooks related to performance optimization.

```{nblinkgallery}
:glob:
../exploring_further/notebook_case_studies/notebooks/tutorials/performance_*
```

## 🛠️ Software tools

Take a look at these software tools to help you solve your performance optimization problems.

```{code-cell} ipython3
:tags: [remove-input]

df = filter_software_tools(tags)
show_software_tools(df)
```