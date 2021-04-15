#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo
"""
import fabric.api
import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents in web_static
    """
    create_time = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(create_time)
    try:
        fabric.api.local("mkdir -p /versions")
        fabric.api.local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
