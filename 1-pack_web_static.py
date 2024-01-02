#!/usr/bin/python3
'''Fabric script that generates a .tgz archive
from the contents of the web_static folder'''

from fabric.api import local
import datetime
import os


def do_pack():
    '''
    archive from the contents of the web_static
    '''
    try:
        if not os.path.exists('versions'):
            os.makedirs('versions')

        current_time = datetime.datetime.now()
        file = "versions/web_static_{}{}{}{}{}{}.tgz" \
            .format(current_time.year,
                    current_time.month,
                    current_time.day,
                    current_time.hour,
                    current_time.minute,
                    current_time.second)
        print(f'Packing web_static to {file}')
        local(f"tar -cvzf {file} web_static")
        return file
    except Exception as e:
        return None
