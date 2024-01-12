# 🚩 Starting a new image analysis project

In this tutorial, we will show you how to set up a simple folder structure for your project. We'll also create both a `jupyter notebook` and a `python script` to open and view one of your images.

```{admonition} Prerequisite
Make sure to have followed our instructions to [install and setup Python, Jupyter Lab, and Napari](./python_setup.md) before starting this tutorial.
```

## Create a new folder for your project

It's important to keep your project structure organized. When you start a new project, create a new folder for it and give it a meaningful name that you can easily remember.

You can use the command line to create a new empty folder on your computer:

```
mkdir my_new_project
```

## Start a `Jupyter lab` server from your project folder

Open your terminal and follow the steps below.

1. From the command-line, navigate to the folder you just created.
```
cd ./my_new_project
```
2. Activate your `Python environment`.
```
conda activate project-env
```
3. Start the `Jupyter Lab` application.
```
jupyter lab
```

Jupyter Lab will open in a web browser window where you can start working on your project.

## Add a `data` subfolder

Create a sub-folder called `data` in which to store your image(s). Move or copy your data there. You can organize that folder's structure further if you need. Keeping your data close to your code makes it easier to refer to it via *relative paths* as we'll see later in this tutorial.

## Create a new `notebook` file

Create a Jupyter notebook (the file extension is `.ipynb`) for your analysis.

Your project structure should now look like this:

```
my_project/
    ├── data/
        ├── image.tif
    analysis.ipynb
```

You can open the Jupyter notebook you just created and start working on it. A good start would be to create a `Markdown` cell to give a title to your notebook based on your analysis (you should also rename the notebook to something meaningful).

Then, you can insert a `Code` cell. Import a few libraries and load an image from your `data` subfolder. For example, you could copy the code below:

```{code} python
import skimage.io

image = skimage.io.imread('data/image.tif')

print(f'Loaded image in an array of shape: {image.shape}.')
print(f'Intensity range: [{image.min()} - {image.max()}]')
```

Notice the advantage of working with relative paths (`data/image.tif`) which are much shorter than absolute paths.

In the next cell, create a Napari viewer and open your image in it.

```
import napari

viewer = napari.view_image(image)
```

When you run this cell, Napari should open in a separate window with your image loaded in it.

## Create a new Python `script`

While jupyter notebooks are interactive (you can run cells progressively, one after the next), Python scripts are run from the top to the bottom of the file. They can take `arguments` and be used from the command-line to perform useful commands.

To test things out, you can copy your code from the Jupyter notebook into your Python script:

```python
import napari
import skimage.io

image = skimage.io.imread('data/image.tif')

print(f'Loaded image in an array of shape: {image.shape}.')
print(f'Intensity range: [{image.min()} - {image.max()}]')

viewer = napari.view_image(image)

napari.run()
```

Notice that in Python scripts you have to add a `napari.run()` call to start the Napari viewer.

Run the script from the therminal:

```
python my_script.py
```

Once again, you should see a Napari viewer appear with your image loaded in it.

## Rearrange your project's structure

As your project develops, you will probably have to create multiple `scripts` and `notebooks` to take care of different parts of your analysis. To keep things tidy, it might be useful to

- Create a `/scripts` folder for your Python scripts (and move your scripts in there)
- Create a `/notebooks` folder for your notebooks

```{note}
If you change your project's structure along the way, you may have to adjust the relative paths to your data in your files since the `data` folder is now one level above the scripts and notebooks. For example, you should change the path `./data/image.tif` to `../data/image.tif`. No big deal!
```

## Add a `README` file

The `README.md` file is usually written in [Markdown](https://www.markdownguide.org/cheat-sheet/) format. It is the landing page of your project. If you decide to host your code on GitLab or GitHub, the `README` file will get rendered on your project's page.

Useful information to include in the `README` include:

- The title and a short description of your project
- Installation instructions
- Usage instructions
- A description of your project's structure
- How to cite your project

For more information, see [Landing Page - README File (The Turing Way)](https://the-turing-way.netlify.app/project-design/project-repo/project-repo-readme).

## Add a `requirements.txt` file

Keeping track of, and listing your project's dependencies in a `requirements.txt` file makes it easier others (or for your future self) to create a suitable Python environment in order to use your code or reproduce your results. The content of `requirements.txt` consists of **one dependency per line**. To be even more specific, you can fix the version of the packages. For example, the content of a simple `requirements.txt` file could be:

```{admonition} requirements.txt
scipy
numpy
scikit-image==0.22.0
```

When a `requirements.txt` file is present in a project, it should be possible to install a working Python environment by running the single command

```
pip install -r requirements.txt
```

to install all the project depenendencies **recursively** (`-r`) using `pip`.

## Add a `LICENSE` file

A `LICENSE` file specifies your project's license. To keep your code open source, you can use an open license such as [`MIT`](https://en.wikipedia.org/wiki/MIT_License) or [`BSD-3`](https://joinup.ec.europa.eu/licence/bsd-3-clause-new-or-revised-license).

To learn more about licenses, check out:

- [TLDRLegal](https://www.tldrlegal.com/)
- [Slides from the course Image data science with Python and Napari (EPFL, 2022)](https://github.com/BiAPoL/Image-data-science-with-Python-and-Napari-EPFL2022/raw/main/docs/day5a_Best_practices_scientific_programming/Sharing_Licensing.pdf)


## Summary

Your project folder should now look like the following:

```
my_project/
    ├── data/
        ├── image.tif
    ├── notebooks/
        ├── analysis.ipynb
    ├── scripts/
        ├── batch_analysis.py
    README.md
    requirements.txt
    LICENSE.txt
```

Using a consistent project structure like this one makes it easier for you to share your project with others or on an online repository. It helps you keep things organized by separating your data from your code, while letting you easily refer to image or data files via relative paths.

## Next steps

<!-- You might consider tracking your project using [`git`](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) and hosting it on a platform such as [GitHub](https://github.com/) or [GitLab](https://gitlab.com/). You can keep your project *private* or make it *public* to share it with others. -->

From here, you should be ready to start developing image analysis pipelines for your project. To help you refine your objectives, consider filling in one of our [Image Analysis Project Sheets](https://docs.google.com/document/d/1NUFKOpXunjs9hOxmn5RvLNrfcF0DhXfgoVGIL3-eXiA/).

<div class="video-container google-sheet">
    <iframe src="https://docs.google.com/document/d/e/2PACX-1vRqDYDopKloJNX2_5tZaTwLABLniCXEVkgBqBTSha___x2j8xKvRGWNofyGxoSQzZmyccVRgYHL8n92/pub?embedded=true"></iframe>
</div>

---
Finally, if you want to dive deeper here are a few more resources from [The Turing Way](https://the-turing-way.netlify.app/index.html):

- [Naming files, folders and other things](https://the-turing-way.netlify.app/project-design/filenaming)
- [Getting Started Checklist](https://the-turing-way.netlify.app/project-design/pd-checklist)
- [Getting Started With GitHub](https://the-turing-way.netlify.app/collaboration/github-novice)
- [Guide for Project Design](https://the-turing-way.netlify.app/project-design/project-design)