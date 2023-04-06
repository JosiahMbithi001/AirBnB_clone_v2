#!/usr/bin/python3
"""This Script sends A File to specified Remote Servers"""

from fabric.api import run, env, put
import os.path

""" Environment Variables """

env.hosts = ['34.227.101.223', '18.204.15.60']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'


def do_deploy(archive_path):
    """A function to deploy code and decompress it"""

    if not os.path.isfile(archive_path):
        return False
    """Compressed file path"""
    tgz_file = archive_path.split("/")[-1]

    """File without Extension"""
    no_ext = tgz_file.split(".")[0]

    try:
        """ Servers Remote Path variable"""

        remote_path = "/data/web_static/releases/{}/".format(no_ext)
        """ Symbolic Link """

        sym_link = "/data/web_static/current"
        """Put archive path in servers /tmp/"""

        put(archive_path, "/tmp/")

        """Makes Remote Path Direcory in the server """

        run("sudo mkdir -p {}".format(remote_path))
        """Decompresses the tgz_file to the Remote path"""

        run("sudo tar -xvzf /tmp/{} -C {}".format(tgz_file, remote_path))
        """Remove the compressed file in /tmp/ direcory"""

        run("sudo rm /tmp/{}".format(tgz_file))
        """Move Everything in web_static to the releases"""

        run("sudo mv {}/web_static/* {}".format(remote_path, remote_path))
        """Remove Web_static"""

        run("sudo rm -rf {}/web_static".format(remote_path))
        """Remove the /data/web_static/current link"""

        run("sudo rm -rf /data/web_static/current")
        """Create A New current Link"""

        run("sudo ln -sf {} {}".format(remote_path, sym_link))
        return True
    except Exception as f:
        return False
