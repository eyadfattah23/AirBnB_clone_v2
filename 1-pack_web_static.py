#!/usr/bin/python3
'''Fabric script
generates a .tgz archive
from the contents of the web_static folder of AirBnB Clone repo,
using the function do_pack.'''

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    '''
    creates an archive from the contents of web_static/
    '''
    try:

        if not os.path.exists('versions'):
            os.makedirs('versions')

        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second
        archive_name = "versions/web_static_{}{}{}{}{}{}".format(
            year, month, day, hour, minute, second)

        print(f'Packing web_static to {archive_name}')
        local('tar -cvzf {}.tgz web_static'.format(archive_name))
        return archive_name
    except Exception as e:
        return None
