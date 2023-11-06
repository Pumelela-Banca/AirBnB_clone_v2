#!/usr/bin/python3

"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of AirBnB Clone repo, using the function do_pack
"""

from fabric.api import isdir
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    create tgz archive from static
    """
    try:
        if isdir("versions") is False:
            local("mkdir versions")
        name = "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S"))
        local(f"tar -cvzf {name} web_static")
        return name
    except:
        return None
