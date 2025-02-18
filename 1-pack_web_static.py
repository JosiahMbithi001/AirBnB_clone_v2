#!/usr/bin/python3
""" a fabric that creates an archive file"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """This Method Compresses Files in web_static"""

    # Creates Datetime Object
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(time_now)

    """Makes Directory"""
    try:
        """Makes directory locally"""
        local("sudo mkdir -p versions")

        """Compresses the folder"""
        local("tar -cvzf {} web_static".format(file_path))

        """Returns Path"""
        return "file_path"

    except Exception as f:
        return None
