#!/usr/bin/python3
'''
Fabric script creates and distributes archives to web servers
'''

from fabric.api import put, sudo, env

env.hosts = ['54.84.44.145', '54.234.38.218']
env.user = 'ubuntu'

pack_web_static = __import__('1-pack_web_static')
do_deploy_web_static = __import__('2-do_deploy_web_static')

archive_path = pack_web_static.do_pack()


def deploy():
    """creates and distributes an archive to web servers

    steps:
    1. Call the do_pack() function and store the path of the created archive
    2. Return False if no archive has been created
    3. Call the do_deploy(archive_path) function
    4. Return the return value of do_deploy

    """
    if not archive_path:
        return False
    try:
        return do_deploy_web_static.do_deploy(archive_path)
    except Exception as e:
        return False
