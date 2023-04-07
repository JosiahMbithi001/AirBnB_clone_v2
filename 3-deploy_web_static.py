#!/usr/bin/python3
""" A Fabric Script that creates an archive file(do_pack function).
(do_deploy) Deploysthe archive file to Web Servers
(do_deploy_web_static) Compresses and Deploys it in the New Path
"""
import os.path
from fabric.api import local
from datetime import datetime
from fabric.api import env, run, put


""" Environment Variables """

env.hosts = ['34.227.101.223', '18.204.15.60']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'

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

def deploy():
	"""A Function that calls the above function to compress and deploy"""
	returned_path = do_pack()
	if returned_path is None:
		return False
	
	return do_deploy(returned_path)
