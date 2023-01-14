#!/usr/bin/python3

from fabric.api import *
from datetime import datetime

def do_pack():
    """
    create archive with filesin web_static folder
    """
    now = datetime.now()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day,
            now.hour, now.minute, now.second)
    print('Packing web_static to versions/{}'.format(filename))
    local('mkdir -p versions')
    result = local('tar -vczf {} web_static'.format(filename))
    if result.succeeded:
        return (filename)
    else:
        return None

