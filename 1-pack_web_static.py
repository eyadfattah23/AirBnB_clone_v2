#!/usr/bin/python3
'''
a Fabric script that archives the contents of the web_static folder
'''
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    '''generates a tgz archive from the contents of the web_static folder where
    1. All files in the folder web_static must are added to the final archive
    2. All archives are stored in the folder versions (create if not created)
    3. name of file is web_static_<year><month><day><hour><minute><second>.tgz
    4. return the archive path if the archive has been correctly generated.
        Otherwise, it should return None'''
    try:
        path = "versions/"
        if not os.path.exists(path):
            os.makedirs(path)
        current_time = datetime.now()

        Year = current_time.year
        Month = current_time.month
        Day = current_time.day
        Hour = current_time.hour
        Minute = current_time.minute
        Second = current_time.second

        archive_name = \
            f"web_static_\{Year}{Month}{Day}\{Hour}{Minute}{Second}.tgz"
        archive_path = f"versions/{archive_name}"
        print(f"Packing web_static to {archive_path}")

        local(f'tar -cvzf {archive_path} web_static')
        return archive_path
    except Exception as e:
        return None
