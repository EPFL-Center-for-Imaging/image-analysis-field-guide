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
tags = ["{{ cookiecutter.notion_database_tag }}"]
from itables import init_notebook_mode
from pathlib import Path
import sys
sys.path.append(str(Path.cwd().parents[1]))
from helpers import *
init_notebook_mode(all_interactive=True, connected=True)
```
![header](./images/header.jpeg)

# {{ cookiecutter.topical_pack_emoji }} {{ cookiecutter.topical_pack_name }}

````{margin}
```{admonition} Acknowledgements
This topic has been curated by **{{ cookiecutter.author_name }}**.

Contact: [✉️ Email](mailto:{{ cookiecutter.author_email }})
```
````

{{ cookiecutter.topical_pack_description }}

## 🎓 Learning resources

Here is our curated list of free online resources on the topic of {{ cookiecutter.topical_pack_name.lower() }}.

```{code-cell} ipython3
:tags: [remove-input]

df = filter_online_resources(tags)
show_online_resources(df, dom="tr")
```

## 🌱 Tutorials

Check out our tutorial notebooks on the topic of {{ cookiecutter.topical_pack_name.lower() }}.

```{nblinkgallery}
:glob:
./notebooks/*
```

## 🛠️ Software tools

Take a look at these software tools related to {{ cookiecutter.topical_pack_name.lower() }}.

```{code-cell} ipython3
:tags: [remove-input]

df = filter_software_tools(tags)
show_software_tools(df)
```