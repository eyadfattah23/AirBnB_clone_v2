#!/usr/bin/python3
'''Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to web servers,
using the function do_deploy'''

from fabric.api import local, run, sudo, put, env
import datetime
import os


def do_deploy(archive_path):
    """distributes an archive to your web servers

    Args:
        archive_path (str): the compressed file path that will be sent
to the web servers
    """

    if not os.path.exists(archive_path):
        return False
    try:
        # define web servers in Fabric environment
        env.user = 'ubuntu'
        env.hosts = ['35.175.65.20', '35.174.213.99']

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        '''
        our goal is to
        Uncompress the archive to the folder
        /data/web_static/releases/<archive name without .tgz>
        on the web server
        '''
        # first we need to get the archive name with no '.tgz'
        pars_archiv_path = archive_path.split('/')
        dir_name = pars_archiv_path[-1].remove('.tgz')

        # then let's make a dir with that name
        sudo('mkdir -p /data/web_static/releases/{}'.format(dir_name))

        # Uncompress the archive to the folder
        sudo(
            f'tar -xzf {archive_path} -C /data/web_static/releases/{dir_name}')

        # Delete the archive from the web server
        sudo('rm /tmp/{}'.format(pars_archiv_path[-1]))

        # Delete the symbolic link /data/web_static/current from the web server
        sudo(
            f'mv /data/web_static/releases/{dir_name}/web_static/* \
                /data/web_static/releases/{dir_name}/')

        sudo(f'rm -rf /data/web_static/releases/{dir_name}/web_static')

        # Create new the symlink /data/web_static/current on the web server,
        # linked to the new version of your code
        sudo(
            f'ln -s /data/web_static/releases/{dir_name}/ \
                /data/web_static/current')

        print('New version deployed!')
        return True
    except Exception as e:
        return False
