#!/usr/bin/pythin3
""" a fabric that creates an archjve file"""
from fabric.api import local, env
from datetime import datetime
import os

env.hosts = ['localhost']


def do_pack():
    """
    Creates a compressed .tgz archive of the web_static folder
    Returns the archive path if successful, None if unsuccessful
    """
    try:
        if not os.path.exists("./versions"):
            local("mkdir versions")

        date_format = "%Y%m%d%H%M%S"
        current_time = datetime.now().strftime(date_format)
        file_path = "versions/web_static_" + current_time + ".tgz"

        local("tar -cvzf {} web_static".format(file_path))

        return file_path
    except:
        return None
