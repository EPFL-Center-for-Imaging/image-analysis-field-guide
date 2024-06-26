# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import os
import nativeauthenticator

c = get_config()

c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"
c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"
c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"

c.JupyterHub.authenticator_class = "nativeauthenticator.NativeAuthenticator"
c.JupyterHub.template_paths = [
    f"{os.path.dirname(nativeauthenticator.__file__)}/templates/"
]
c.NativeAuthenticator.open_signup = True  # Anyone can freely sign up (YOLO).

c.JupyterHub.allow_named_servers = False  # Only one server per user

name = os.environ.get("JUPYTERHUB_NAME")
c.DockerSpawner.image = os.environ["DOCKER_NOTEBOOK_IMAGE"]

c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = os.environ["DOCKER_NETWORK_NAME"]
notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR", "/home/jovyan")
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.remove = True
c.DockerSpawner.debug = True
c.DockerSpawner.prefix = name
c.DockerSpawner.mem_limit = "64G"
c.DockerSpawner.mem_guarantee = "32G"
c.DockerSpawner.cpu_guarantee = 12
c.DockerSpawner.cpu_limit = 32
c.DockerSpawner.extra_host_config = {
    "ipc_mode": "host",
    "security_opt": ["seccomp=unconfined"],
}

c.JupyterHub.hub_ip = name
c.JupyterHub.hub_port = 8080

admin = os.environ.get("JUPYTERHUB_ADMIN")
if admin:
    c.Authenticator.admin_users = [admin]

c.JupyterHub.default_services = ["nbgitpuller"]

# Shared data folder on the host machine
shared_data_dir = os.path.join(notebook_dir, "shared_data")

c.Spawner.environment = {
    "DISPLAY": ":1.0",
    "SHARED_DATA": shared_data_dir,
    "NOTION_KEY": os.getenv('NOTION_KEY'),
    "JUPYTER_CONFIG_DIR": "/opt/.jupyter"
}

c.DockerSpawner.notebook_dir = notebook_dir

c.DockerSpawner.volumes = {
    f"{name}-user-{{username}}": notebook_dir,
}

# host_shared_data_dir = os.path.join(os.path.expanduser('~'), '.cache', 'field-guide')

# c.DockerSpawner.read_only_volumes = {
#     host_shared_data_dir: shared_data_dir,
# }

# # Make this a post-start hook that depends on the group?
# c.Spawner.post_start_cmd = "git clone https://github.com/EPFL-Center-for-Imaging/image-analysis-field-guide.git"