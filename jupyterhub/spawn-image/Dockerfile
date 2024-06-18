#################################################################
FROM quay.io/jupyter/pytorch-notebook:x86_64-ubuntu-22.04
ENV DEBIAN_FRONTEND=noninteractive
#################################################################

USER root
WORKDIR /opt

# Install libraries
RUN apt-get update -y \
    && apt upgrade -y \
    && apt-get install -yq --no-install-recommends \
    dbus-x11 \
    net-tools \
    less \
    xfce4 \
    xfce4-panel \
    xfce4-session \
    xfce4-settings \
    xorg \
    xubuntu-icon-theme \
    gnome-terminal \
    fonts-dejavu \
    git-gui \
    gitk \
    emacs \
    sudo \
    ncdu \
    p7zip-full \
    libdbus-1-3 \
    libxkbcommon-x11-0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-xinerama0 \
    libxcb-xinput0 \
    libxcb-xfixes0\
    nodejs \
    npm \
    websockify \
    gnupg2 \
    imagemagick \
    zsh \
    tree \
    htop \
    ripgrep \
    zip \
    && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt install -y gh \
    && apt-get autoremove --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* \
    && find /var/log -type f -exec cp /dev/null \{\} \;

# Oh-my-zsh (make it default shell)
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
RUN chsh -s /bin/zsh root

#################################################################
# Install TigerVNC 1.9.0 -> Test 1.13.1
ENV tigervnc_version=1.10.1
RUN curl -sSfL https://sourceforge.net/projects/tigervnc/files/stable/${tigervnc_version}/tigervnc-${tigervnc_version}.x86_64.tar.gz/download | tar -zxf - -C /usr/local --strip=2

#################################################################
# Install noVNC 1.1.0 -> test 1.4.0
ENV novnc_version=1.1.0
RUN curl -sSfL https://github.com/novnc/noVNC/archive/v${novnc_version}.tar.gz | tar xvz -C /opt/ && \
    chmod a+rX -R /opt/noVNC-${novnc_version}

# Custom interface
COPY --chown=root:root remote_desktop/vnc.html /opt/noVNC-${novnc_version}
COPY --chown=root:root remote_desktop/ui.js /opt/noVNC-${novnc_version}/app/ui.js
COPY --chown=root:root remote_desktop/base.css /opt/noVNC-${novnc_version}/app/styles/base.css

RUN chmod -R a+rwx /home/$NB_USER/

# Make a Desktop folder
RUN mkdir /home/$NB_USER/Desktop && chown -R $NB_GID:$NB_GID /home/$NB_USER/Desktop

# Install Fiji
RUN wget -q https://downloads.imagej.net/fiji/latest/fiji-linux64.zip \
    && unzip fiji-linux64.zip -d /opt/ \
    && rm fiji-linux64.zip \
    && chmod -R a+rwX /opt/Fiji.app

# Update sites
ENV fiji /opt/Fiji.app/ImageJ-linux64
ENV updateCommand --update update
RUN ${fiji} ${updateCommand} \
    && chmod -R a+rwX /opt/Fiji.app

# Desktop icon
RUN printf '[Desktop Entry]\nVersion=1.0\nName=ImageJ\nGenericName=ImageJ\nX-GNOME-FullName=ImageJ\nComment=Scientific Image Analysis\nType=Application\nCategories=Education;Science;ImageProcessing;\nExec=/opt/Fiji.app/ImageJ-linux64 %F\nTryExec=/opt/Fiji.app/ImageJ-linux64\nTerminal=false\nStartupNotify=true\nMimeType=image/*;\nIcon=/opt/Fiji.app/images/icon.png\nStartupWMClass=net-imagej-launcher-ClassLauncher\n' > /home/$NB_USER/Desktop/Fiji.desktop

# Install ilastik
RUN wget https://files.ilastik.org/ilastik-1.4.0-Linux.tar.bz2 -O ilastik-1.4.0-Linux.tar.bz2 

RUN tar -xf ilastik-1.4.0-Linux.tar.bz2 -C /opt/ \
    && mv /opt/ilastik-1.4.0-Linux /opt/ilastik \
    && rm ilastik-1.4.0-Linux.tar.bz2 \
    && chmod -R a+rwX /opt/ilastik/

RUN mkdir -p /home/$NB_USER/Desktop && chown -R $NB_GID:$NB_GID /home/$NB_USER/Desktop \
    && printf '[Desktop Entry]\nVersion=1.4.0\nName=ilastik\nGenericName=ilastik\nX-GNOME-FullName=ilastik\nComment=Scientific Image Analysis\nType=Application\nCategories=Education;Science;ImageProcessing;\nExec=/opt/ilastik/run_ilastik.sh %F\nTryExec=/opt/ilastik/run_ilastik.sh\nTerminal=false\nStartupNotify=true\nMimeType=image/*;\nIcon=/opt/ilastik/lib/python3.7/site-packages/ilastik/shell/gui/icons/96x96/ilastik-icon.png\nStartupWMClass=ilastik\n' > /home/$NB_USER/Desktop/ilastik.desktop \
    && chown -R $NB_GID:$NB_GID /home/$NB_USER \
    && chmod +x /home/$NB_USER/Desktop/ilastik.desktop

# Install Firefox
RUN wget -q 'https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64' -O /tmp/firefox.tar.bz2 \
    && tar xjf /tmp/firefox.tar.bz2 -C /opt/ \
    && rm -rf /tmp/firefox.tar.bz2 \
    && ln -sf /opt/firefox/firefox /usr/bin/firefox \
    && ln -sf /usr/bin/firefox ~/Desktop/firefox \
    && apt update \
    && apt install libdbus-glib-1-2 -y \
    && apt-get autoremove --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* \
    && find /var/log -type f -exec cp /dev/null \{\} \;
ENV BROWSER=firefox

# Install VS Code
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg \
    && install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/ \
    && sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list' \
    && rm -f packages.microsoft.gpg \
    && apt update \
    && apt install -y code \
    && apt-get autoremove --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* \;

# VS Code server + extensions
RUN curl -fsSL https://code-server.dev/install.sh | sh
RUN conda install jupyter-vscode-proxy
RUN code-server --install-extension ms-python.python
RUN code-server --install-extension ms-toolsai.jupyter
RUN code-server --install-extension tonybaloney.vscode-pets

# Save conda envs in the user's home folder instead of in /opt (which is not persistent across sessions)
RUN conda config --system --prepend envs_dirs '~/work/.conda/envs'

# Make the conda envs discoverable in jupyter
RUN conda install -c conda-forge nb_conda_kernels

# Customize jupyter
RUN mkdir /opt/.jupyter
RUN chown -R $NB_GID:$NB_GID /opt/.jupyter/ \
    && chmod -R a+rwx /opt/.jupyter/
COPY jupyter_notebook_config.py /opt/.jupyter/jupyter_notebook_config.py
COPY jupyter_server_config.py /opt/.jupyter/jupyter_server_config.py

# Jupyter extensions
COPY ./requirements.jupyter.txt /opt/
RUN pip install -r /opt/requirements.jupyter.txt

# Jupyter hub
ARG JUPYTERHUB_VERSION=4.0.2
RUN pip3 install --no-cache \
    jupyterhub==$JUPYTERHUB_VERSION

# Scientific python
COPY ./requirements.txt /opt/
RUN pip install -r /opt/requirements.txt

# Install spam
RUN apt-get update -y \
    && apt upgrade -y \
    && apt-get install -yq --no-install-recommends \
    python3-dev python3-venv python3-tk gcc g++ libeigen3-dev libicu-dev libgmp-dev libmpfr-dev libcgal-dev gmsh libfreetype6-dev libxml2-dev libxslt-dev \
    && apt-get autoremove --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* \
    && find /var/log -type f -exec cp /dev/null \{\} \;
RUN pip install spam

# jupyterlab-rise
RUN pip install rise jupyterlab_rise

# # jupyterlab-drawio (it breaks everyting)
# RUN mamba install -c conda-forge jupyterlab-drawio

# Configuration files
COPY --chown=$NB_GID:$NB_GID ./config/ /home/$NB_USER/

# Customize extensions
COPY lab/user-settings/@jupyter-lsp/ /opt/.jupyter/lab/user-settings/@jupyter-lsp/
COPY lab/user-settings/@jupyterlab/completer-extension/ /opt/.jupyter/lab/user-settings/@jupyterlab/completer-extension/

# App launcher
COPY jupyter_app_launcher/ /opt/conda/share/jupyter/jupyter_app_launcher/

# Conda setup for ZSH
RUN /opt/conda/bin/conda init zsh \
    && /opt/conda/bin/conda clean --all -y \
    && source /opt/conda/bin/activate \
    && . /home/$NB_USER/.zshrc

# Final chown and chmod
RUN chown -R $NB_GID:$NB_GID /home/$NB_USER/ \
    && chmod -R a+rwx /home/$NB_USER/

# For the app launcher
RUN chown -R $NB_GID:$NB_GID /opt/conda/share/jupyter/jupyter_app_launcher/ \
    && chmod -R a+rwx /opt/conda/share/jupyter/jupyter_app_launcher/

# Jupyter config folder (point to it as JUPYTER_CONFIG_DIR in jupyterhub_config.py)
RUN chown -R $NB_GID:$NB_GID /opt/.jupyter/ \
    && chmod -R a+rwx /opt/.jupyter/

# # Same for conda (not working)
# RUN chown -R $NB_GID:$NB_GID /opt/conda/ \
#     && chmod -R a+rwx /opt/conda/

# Make a shared_data folder
RUN mkdir /home/$NB_USER/shared_data \
    && chown -R $NB_GID:$NB_GID /home/$NB_USER/shared_data \
    && chmod -R a+rwx /home/$NB_USER/shared_data/

#################################################################
USER $NB_USER
WORKDIR /home/$NB_USER

CMD [ "jupyterhub-singleuser" ]