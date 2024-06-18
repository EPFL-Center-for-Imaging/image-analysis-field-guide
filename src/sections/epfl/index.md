---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.0

---
```{code-cell} ipython3
:tags: [remove-input]
tags = ["EPFL"]
from itables import init_notebook_mode
from pathlib import Path
import sys
sys.path.append(str(Path.cwd().parents[1]))
from helpers import *
init_notebook_mode(all_interactive=True, connected=True)
```
![header](./images/header.jpeg)

# 🇨🇭 EPFL

````{margin}
```{admonition} Acknowledgements
This topic has been curated by **Mallory Wittwer**.

Contact: [✉️ Email](mailto:mallory.wittwer@epfl.ch)
```
````

EPFL (Ecole Polytechnique Federale de Lausanne) is a public research university in Lausanne, Switzerland.

## 🎓 Learning resources

Here is our curated list of online resources from EPFL.

```{code-cell} ipython3
:tags: [remove-input]

df = filter_online_resources(tags)
show_online_resources(df, dom="tr")
```

## 💡 Example projects

```{admonition} Soon!
Check out our examples of image analysis projects done in collaboration with EPFL labs.
```

```{nblinkgallery}
:glob:
./notebooks/*
```

## 🛠️ Software tools

Take a look at these software tools from EPFL.

```{code-cell} ipython3
:tags: [remove-input]

df = filter_software_tools(tags)
show_software_tools(df)
```