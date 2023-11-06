#!/usr/bin/python3

"""
unpacks files inside servers
"""


from os.path import isdir
from fabric.api import run, put, env


env.hosts = ["18.206.192.143", "54.83.136.225"]


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
        run(f"mkdir -p {path}{fold}")
        run(f"tar -xzf /tmp/{file} -C {path}{fold}")
        run(f"rm /tmp/{file}")
        run(f"mv {path}{fold}/web_static/* {path}{fold}/")
        run(f"rm -rf {path}{fold}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {path}{fold}/ /data/web_static/current")
        return True
    except:
        return False
