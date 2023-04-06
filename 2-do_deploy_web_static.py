#!/usr/bin/python3
"""send an archive file to a remote server
and decompress it"""
from fabric.api import run, env, put
import os.path

env.hosts = ['34.224.94.210', '54.87.252.193']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'

def do_deploy(archive_path):
    """a function to deploy code and decompress it"""
    
    if not os.path.isfile(archive_path):
        return False
    compressed_file = archive_path.split("/")[-1]
    no_extension = compressed_file.split(".")[0]
    
    try:
       remote_path = "/data/web_static/releases/{}/".format(no_extension)
       sym_link = "/data/web_static/current"
       put(archive_path, "/tmp/")
       run("sudo mkdir -p {}".format(remote_path))
       run("sudo tar -xvzf /tmp/{} -C {}".format(compressed_file, remote_path))
       run("sudo rm /tmp/{}".format(compressed_file))
       run("sudo mv {}/web_static/* {}".format(remote_path, remote_path))
       run("sudo rm -rf {}/web_static".format(remote_path))
       run("sudo rm -rf /data/web_static/current")
       run("sudo ln -sf {} {}".format(remote_path, sym_link))
       return True
    except Exception as e:
       return False
