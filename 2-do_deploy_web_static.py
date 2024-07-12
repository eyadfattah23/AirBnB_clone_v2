#!/usr/bin/python3
'''
a Fabric script that distributes an archive to web servers
'''
from fabric.api import put, sudo, env
from datetime import datetime
import os

env.hosts = ['52.91.152.150', '34.227.91.173']


def do_deploy(archive_path):
    """Returns True if all operations have been done correctly,
    otherwise returns False
        Steps:
            1- Upload the archive to the /tmp/ directory of the web server
            2- extract the archive to /data/web_static/releases/<filename>
            3- Delete the archive from the web server
            4- Delete the symlink /data/web_static/current from the server

    Args:
            archive_path (str): path of the tgz to upload
    """
    try:
        if not os.path.exists(archive_path):
            return False

        put(archive_path, '/tmp/')
        archive_name = archive_path.split('/')[-1]
        archive_folder = archive_name.split('.')[0]

        sudo(f'mkdir -p /data/web_static/releases/{archive_folder}')

        sudo(
            f'tar -xzf /tmp/{archive_name} -C \
/data/web_static/releases/{archive_folder}')

        sudo(f'rm /tmp/{archive_name}')

        sudo(
            f'mv /data/web_static/releases/{archive_folder}/web_static/* \
/data/web_static/releases/{archive_folder}/')

        sudo(f'rm -rf /data/web_static/releases/{archive_folder}/web_static')

        sudo('rm -rf /data/web_static/current')

        sudo(
            f'ln -s /data/web_static/releases/{archive_folder}/ \
/data/web_static/current')

        print('New version deployed!')
        return True
    except Exception as e:
        return False
