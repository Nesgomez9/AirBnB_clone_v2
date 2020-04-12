#!/usr/bin/python3

from fabric.api import *
from datetime  import datetime
import os

env.hosts = ['34.74.237.63']
env.user = 'ubuntu'


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

def do_deploy(archive_path):

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(m_file[0]))
        f_file = os.path.basename(archive_path)
        m_file = os.path.splitext(f_file)
        run("tar -C  /data/web_static/releases/{} -xvf /tmp/{}".format(m_file[0], f_file))
        run("rm /tmp/{}".format(f_file))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{} /data/web_static/current".format(m_file[0]))
        return True
    except:
        return False
