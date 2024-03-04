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

# 🐍 Setting up Python for scientific image analysis

Python can be used to process, analyze, and visualize your images. There are several ways of installing and setting up Python on your computer. If you have never used Python before, we recommend that you follow the steps below to get started.

## Install Python using `conda`

If you haven't yet installed Python, Anaconda, or Miniconda on your machine, we recommend you install `Miniconda` which is based on the [conda package manager](https://docs.conda.io/en/latest/). Click on the link below to download the installer:

**Miniconda**: https://docs.conda.io/en/latest/miniconda.html

Once you have downloaded the installer, run it to install `conda`.

`````{tab-set}
````{tab-item} Windows
1. Run the executable file you just downloaded (`Miniforge3-Windows-x86_64.exe`) and follow the instructions.
2. Launch the *Anaconda Prompt* terminal from the start menu.
```{image} ../images/anaconda_prompt.jpeg
:align: center
:width: 250px
```
````
````{tab-item} Mac / Linux
1. Open your Terminal (you can search for it in spotlight - `cmd` + `space`)
2. Navigate to the folder you downloaded the installer to using `cd`. For example:
```bash
cd ~/Downloads
```
1. Execute the installer with the command below. You can use your arrow keys to scroll up and down to read it/agree to it.
```bash
bash Miniforge3-MacOSX-x86_64.sh -b
```
2. To verify that your installation worked, close your terminal window and open a new one. You should see `(base)` to the left of your prompt.
3. Finally, initialize miniforge with the command below. This ensures that your terminal is set up correctly for your Python installation.
```bash
conda init
```
````
`````

```{admonition} Verify your installation
:class: tip
Verify that you have **conda** installed by typing `conda -V` in your terminal. This should print out a version number.
```

## Create a Python virtual environment

A virtual environments lets you isolate the packages and dependencies that you need for a specific project. Using virtual environments will ensure that these dependencies do not create conflicts between the different Python projects you may be working on.

Type the following commands in your terminal to create a virtual environment (named `project-env`) using `conda`:

```bash
conda create -n project-env python=3.9
```

The `-n` parameter specifies the name of the virtual environment (here, *project-env*). We also specify the Python version to be 3.9. Python is constantly evolving and new versions are regularly released. At the time of writing, modern versions include 3.8 to 3.11.

```{tip}
Print a list of the virtual environments available on your machine by typing `conda env list`.
```

## Activate your environment

Let’s install a few Python packages into your *project-env* environment. To do that, you first have to *activate* the environment. Use the following command:

```bash
conda activate project-env
```

If you successfully activated the environment, you should see `(project-env)` to the left of your command prompt. To *deactivate* your environment and switch back to the `(base)` environment, you can use the `conda deactivate` command.

## Install packages

Once you have activated your environment, you can install packages in it. Many packages are available for scientific computing, image processing and analysis in Python. For example, take a look at the projects below:

````{grid} 1 1 2 3
```{grid-item-card}
:link: https://scikit-image.org/
:img-top: https://img.stackshare.io/service/1294/897180.png
:text-align: center
Scikit-image
```
```{grid-item-card}
:link: https://opencv.org/
:img-top: https://research.shu.ac.uk/aces/guardians/opencv_logo.png
:text-align: center
OpenCV
```
```{grid-item-card}
:link: https://scipy.org/
:img-top: https://scipy.org/images/logo.svg
:text-align: center
Scipy
```
````

You can install packages using your terminal and a **package manager** program. By default, Python includes a package manager called `pip` which lets you install packages from the official Python Package Index, also known as [PyPI](https://pypi.org/).

Let's install Scikit-image in your `project-env` virtual environment. To do so, type the following command in your terminal:

```
pip install scikit-image
```

To check that your installation was successful, you can type `pip list` in your terminal to list all the packages installed in your environment. If you search for it, you should see `scikit-image` in the list!

## Install Jupyter lab

[Jupyter lab](https://jupyter.org/) is a powerful web appliation that you can use to edit and execute Python code. You can install it in your environment just like a regular Python package, using [pip](https://pip.pypa.io/en/stable/). Type the following command in your terminal:

```bash
pip install jupyterlab
```

````{admonition} Check your installation
Type `jupyter lab` in your terminal. This should start the Jupyter lab application in your web browser. To stop Jupyter lab, press `Ctrl+C` in your terminal window.

```{image} ../images/jlab-3.gif
:align: center
:width: 95%
```
````

One of the main features of Jupyter Lab is to enable viewing and editing `Jupyter notebooks`, which are interactive documents that combine code, visualizations, and narrative text, and are used by scientists to experiment with code and and demonstrate workflows. To have a better idea of what notebooks looks like, take a look at our [Tutorials](../getting_started/tutorials.md) gallery.

## Install Napari

[Napari](https://www.napari.org/) is a multi-dimensional image viewer for Python. It is used to visualize scientific images and the data associated with them, including segmentation masks, bounding boxes, and keypoints.

With Napari, you can

- visualize timeseries, 2D, 3D, and multi-channel images.
- create interactive visualizations tailored to your needs.
- set up visualizations in a Python script or a [Jupyter notebook](https://jupyter.org/).
- annotate data (draw masks, polygons, etc.).
- use [plugins from the community](https://www.napari-hub.org/) or develop and share your own plugin.

We recommend that you install [Napari](https://napari.org/stable/) by typing the following command:

```bash
pip install "napari[all]"
```

````{admonition} Check your installation
With your virtual environment activated, type `napari` in your terminal. The Napari viewer should open **in a separate window**.
```{image} ../images/napari_terminal.gif
:align: center
:width: 95%
```
````

You can also find the official Napari installation instructions [here](https://napari.org/stable/tutorials/fundamentals/installation.html#installation).

## Install a code editor

Code editors provide many useful features, including syntax highlighting, a file system manager, integrated terminals, and code auto-completion. You can also interact with Jupyter notebooks directly in your code editor instead of using your web browser.

We recommend that you try and pick one of the code editors below.

````{grid} 1 1 2 3
```{grid-item-card}
:link: https://code.visualstudio.com/
:img-top: https://static-00.iconduck.com/assets.00/file-type-vscode-icon-256x254-n2qz4hp8.png
:text-align: center
Visual Studio Code
```
```{grid-item-card}
:link: ./sections/starter_packs/packs/image-data-visualization/page.html
:img-top: https://upload.wikimedia.org/wikipedia/commons/1/1d/PyCharm_Icon.svg
:text-align: center
PyCharm
```
```{grid-item-card}
:link: ./sections/starter_packs/packs/performance-optimization/page.html
:img-top: https://static-00.iconduck.com/assets.00/spyder-icon-512x512-0mcgxvrr.png
:text-align: center
Spyder
```
````

## Summary

Setting up Python for working on your image analysis project typically involves the following steps.

- Installing Python, which you can do (for example) via *conda*, which you can obtain by installing **Miniconda**.
- Creating a **virtual environment** for your project.
- Installing packages in your virtual environment using *pip*.
- Installing a program to develop code, such as **Jupyter lab** or a **code editor**.
