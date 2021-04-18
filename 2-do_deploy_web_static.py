#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to a web servers
"""
import datetime
from os.path import exists
from fabric.api import put, run, env

env.hosts = ["3.89.119.219", "35.185.52.50"]


def do_deploy(archive_path):
    """
    Distribute an archive to a web server
    """
    if exists(archive_path) is False:
        return False
    else:
        try:
            file_path = "/data/web_static/releases/"
            file_name = archive_path.split("/")[-1]
            file_rm_dot = file_name.split(".")[0]
            put(archive_path, '/tmp/')
            run("mkdir -p {}{}".format(file_path, file_rm_dot))
            run("tar -xzf /tmp/{} -C {}{}/".format(file_name, file_path,
                                                   file_rm_dot))
            run("mv {}{}/web_static/* {}{}/".format(file_path, file_rm_dot))
            run("rm -fr /tmp/{}".format(file_name))
            run("rm -fr /data/web_static/current")
            run("ln -s {}{}/ /data/web_static/current".format(file_path,
                                                              file_rm_dot))
            return True
        except:
            return False
