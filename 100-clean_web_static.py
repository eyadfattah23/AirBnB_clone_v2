#!/usr/bin/python3
"""
Fabric script deletes out-of-date archives, using the function do_clean

    Delete all unnecessary archives in the versions folder
    Delete all unnecessary archives in the /data/web_static/releases on both
    web servers
"""

from fabric.api import put, sudo, env, local

env.hosts = ['52.91.152.150', '34.227.91.173']
env.user = 'ubuntu'


def do_clean(number=0):
    """
    If number is 0 or 1, keep only the most recent version of your archive.
    If number is 2, keep the most recent, and second most recent versions of
    your archive. Etc.
    """
    number = int(number)

    if number <= 1:
        number = 1

    # Local cleanup
    local_archives = local("ls -t versions").split()
    archives_to_delete = local_archives[number:]
    for archive in archives_to_delete:
        local("rm versions/{}".format(archive))

    # Remote cleanup
    sudo_archives = sudo("ls -t /data/web_static/releases"
                         ).split()
    archives_to_delete = sudo_archives[number:]
    for archive in archives_to_delete:
        if "web_static_" in archive:
            sudo("rm -rf /data/web_static/releases/{}".format(archive))
