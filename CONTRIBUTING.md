# 🤝 Contributing guide

Contributions to our project are welcome. 

## Get in touch

If you'd like to contribute to our project, you can contact me by email at `mallory.wittwer@epfl.ch`. The main way to get involved in our project is by **maintaining a topical pack** on a topic of interest. Your contribution will be acknowledged directly on the website.

Let us know if you'd like to maintain an existing topical pack, or add a new one. Below are some examples of topical packs that we don't yet have and that might be of interest to us:

- Digital pathology
- Spatial transcriptomics
- Geospatial imaging
- Handling big image data

## Create a topical pack

You can use our `cookiecutter` (see [README.md](./template_topical_pack/README.md)) to help you create a new topical pack.

## Maintain a topical pack

We'll give you access to our resource databases on Notion. You'll be able to 
- add new entries for software tools and online resources
- control which entries are visible on the site

Moreover, we'll add you as a maintainer of the repository. You can clone it and 

- edit the `index.md` page of your topical pack
- add `Jupyter notebook` tutorials

Updates are handled by `Pull requests` to the `main` branch of the repository. If you've never done this before, you can follow the steps below:

**Authenticate to GitHub**

We recommend authenticating via the GitHub CLI:

```
gh auth login -s 'user:email' -w
gh auth refresh -h github.com -s admin:public_key
ssh-keygen
gh ssh-key add id_rsa.pub -t <key-name>
```

**Pull request**

First, create a new branch for your feature.

```
git checkout -b my_topical_pack
```

Then, make your changes. When you're done, you can push your branch to the remote repository:

```
git add .
git commit -m "Description of your changes."
git push origin my_topical_pack
```

After that, on [Github.com](https://github.com/EPFL-Center-for-Imaging/image-analysis-field-guide) you will be prompted to create a new pull request.


## Use the `JupyterHub`

If you're at EPFL, we'll give you access to our JupyterHub, which is already set up to facilitate contributing to the project. It provides an environment already configured with all Python dependencies installed, so you can build the Jupyter book and see exactly how your content will appear on the site.
