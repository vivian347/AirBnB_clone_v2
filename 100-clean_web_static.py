#!/usr/bin/python3
"""
deletes out-of-date archives
"""

from fabric.api import *


env.hosts = ['34.227.90.97', '54.90.1.16']
env.user = "ubuntu"


def do_clean(number=0):
    """ deletes """
    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {}; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
