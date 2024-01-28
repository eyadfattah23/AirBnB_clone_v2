#!/usr/bin/python3
'''Fabric script (based on the file 1-pack_web_static.py)
distributes an archive to your web servers,
using the function do_deploy'''

from fabric.api import run, put, env
from datetime import datetime
import os


def do_deploy(archive_path):
    """distributes an archive to your web servers

    Args:
        archive_path (string): the compressed file path that will be sent
                to the web servers

    The function makes the following steps:

    -Upload the archive to the /tmp/ directory of the web server

    -Unzip the archive to the folder /data/web_static/releases/<archive name
        without .tgz> on the web server

    -Delete the archive from the web server

    -Delete the symbolic link /data/web_static/current from the web server

    -Create a new the symbolic link /data/web_static/current on the web server,
    linked to the new version of my code
    at (/data/web_static/releases/<archive name without .tgz>)

    """
    try:
        env.hosts = ['52.3.251.8', '100.25.162.125']
        env.user = 'ubuntu'
        # Return False if the file at the path archive_path doesn’t exist
        if not os.path.exists(archive_path):
            return False

        for host in env.hosts:
            env.host_string = host
            # Upload the archive to the /tmp/ directory of the web server
            put(archive_path, '/tmp/')

            # mkdir if non-existent
            folder_name = archive_path.split("/")[-1][:-4]
            archive_name = archive_path.split("/")[-1]
            run("sudo mkdir -p /data/web_static/releases/{}".format(folder_name))

            # Uncompress the archive
            run('sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
                .format(archive_name,
                        folder_name))

            # Delete the archive from the web server
            run('rm /tmp/{}'.format(archive_name))

            # Delete the symbolic link /data/web_static/current from the web server
            run('sudo mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/'.format(folder_name, folder_name))

            run('sudo rm -rf /data/web_static/releases/{}/web_static'.format(folder_name))

            run('sudo rm -rf /data/web_static/current')

            # Create a new the symbolic link /data/web_static/current on web server,
            # linked to the new version of your code
            run('sudo ln -s /data/web_static/releases/{}/ /data/web_static/current'
                .format(folder_name))

            print('New version deployed!')
        return True
    except Exception as e:
        return False
