#!/usr/bin/python3
"""
deletes out-of-date archives
"""

import os
from fabric.api import *


env.hosts = ['34.227.90.97', '54.90.1.16']
env.user = "ubuntu"


def do_clean(number=0):
    """ deletes """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
