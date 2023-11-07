#!/usr/bin/python3

"""
unpacks files inside servers
"""


from datetime import datetime
from os.path import isdir
from fabric.api import run, put, env
from fabric.api import local


env.hosts = ["18.206.192.143", "54.83.136.225"]
env.user = 'ubuntu'
env.key_filename = r"C:\Users\DELL 3550\.ssh\holla"


def do_pack():
    """
    creates tgz archive from static folder
    """
    try:
        if isdir("versions") is False:
            local("sudo mkdir versions")
        name = "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S"))
        local(f"sudo tar -cvzf {name} web_static")
        return name
    except:
        return None


def do_deploy(archive_path):
    """
    unpack files into servers
    """
    if isdir(archive_path) is False:
        return False
    try:
        file = archive_path.split("/")[-1]
        fold = file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run(f"sudo mkdir -p {path}{fold}")
        run(f"sudo tar -xzf /tmp/{file} -C {path}{fold}")
        run(f"sudo rm /tmp/{file}")
        run(f"sudo mv {path}{fold}/web_static/* {path}{fold}/")
        run(f"sudo rm -rf {path}{fold}/web_static")
        run(f"sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s {path}{fold}/ /data/web_static/current")
        return True
    except:
        return False


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    arch_path = do_pack()
    if arch_path is None:
        return False
    return do_deploy(arch_path)
