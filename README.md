![EPFL Center for Imaging logo](https://imaging.epfl.ch/resources/logo-for-gitlab.svg)
# The Image Analysis Field Guide

A [Jupyter Book] website 

👉 See the live website at [this URL]().

## Installation

```
pip install -r requirements.txt
```

## Build the Jupyter book

```
jupyter-book build src/
```

Then, drag and drop `_build/html/index.html` in a web browser.

To check external links:

```
jb build src --builder linkcheck
```

## Build and run with `docker`

Build the image:

```
docker build -t $(whoami)/$(basename ${PWD}) .
```

Run the jupyter book in a container on `http://localhost:8080/`.

Quick test:

```
docker run --rm -it -p 8080:80 $(whoami)/$(basename ${PWD}):latest
```

Persistent:

```
docker run -dp 8080:80 --name image-analysis-field-guide $(whoami)/$(basename ${PWD}):latest
```

## On GitHub & Pages

- Add a `NOTION_KEY` to the repository's **secrets**.
- Tag the repository as `jupyter-book` to have it appear in the official [Gallery](https://executablebooks.org/en/latest/gallery/).

## Launch button to a `JupyterHub`

Edit this part of `_config.yml`:

```yaml
launch_buttons:
  notebook_interface : jupyterlab
  jupyterhub_url: "http://frank1/"  # The URL for your JupyterHub.
```