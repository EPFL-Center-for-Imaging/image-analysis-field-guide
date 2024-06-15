![EPFL Center for Imaging logo](https://imaging.epfl.ch/resources/logo-for-gitlab.svg)
![screenshot](./src/images/epfl.jpeg)
# The Image Analysis Field Guide

Essential toolkit to get started in scientific image analysis.

👉 See the live website at [this URL](https://imaging.epfl.ch/field-guide/).

**Help us improve the site**

- ✒️ Do you have any comments about our site? Don't hesitate to share them via this [Google Form](https://forms.gle/toHAP2ydydXBCndGA).

- 🤝 Contributions to our project are very welcome. See our [Contributing Guide](./CONTRIBUTING.md) for more details.

## Installation

### Option 1: Install and build the Jupyter book website locally

Install the packages required to build the jupyter book website:

```
pip install -r requirements.txt
```

Install the scientific packages required to run the notebooks:

```
pip install -r jupyterhub/sections/spawn-image/requirements.txt
```

Build the Jupyter book:

```
jupyter-book build src/
```

Then, drag and drop `_build/html/index.html` in a web browser.

To check external links:

```
jb build src --builder linkcheck
```

### Option 2: Build and run with `docker`

Build the image:

```
docker build --build-arg NOTION_KEY=$NOTION_KEY -t $(whoami)/$(basename ${PWD}) .
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

## Set up a `JupyterHub` and link it to the site

We provide a configuration to set up and run a JupyterHub for users and contributors. The JupyterHub can be linked to the website via the `jupyterhub_url` parameter in [_config.yml](./src/_config.yml). Users can run notebooks in the Jupyter Hub environment via the launch icon.

**Build and run the JupyterHub**

From the `jupyterhub/` directory:

```
docker compose up -d
```

This command will

- Build the [./jupyterhub/spawn-image/Dockerfile](spawn image).
- Build the [./jupyterhub/Dockerfile.jupyterhub](JupyterHub image).
- Run the JupyterHub on `http://localhost:8000/`.

Our JupyterHub configuration is derived from [JupyterHub Imaging](https://gitlab.com/epfl-center-for-imaging/jupyterhub-imaging).