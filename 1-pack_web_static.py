#!/usr/bin/python3

from fabric.api import *
from datetime import datetime


def do_pack():

    try:
        local("mkdir -p versions")
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        path = "versions/web_static_{}".format(date)
        local("tar -cvzf {}.tgz web_static/".
              format(path))
        return (path)
    except:
        return None
