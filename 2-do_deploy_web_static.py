#!/usr/bin/python3

from fabric.api import *
from datetime  import datetime
import os

env.hosts = ['34.74.237.63', '54.234.24.109']

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

    if not(os.path.exists(archive_path)):
            return False
    try:
        put(archive_path, "/tmp/")
        f_file = os.path.basename(archive_path)
        m_file = os.path.splitext(f_file)
        run("sudo mkdir -p /data/web_static/releases/{}".format(m_file[0]))
        run("sudo tar -C  /data/web_static/releases/{} -xvf /tmp/{}".format(m_file[0], f_file))
        run("sudo rm /tmp/{}".format(f_file))
        run("sudo mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}".format(m_file[0], m_file[0]))
        run("sudo rm -rf /data/web_static/releases/{}/web_static/".format(m_file[0]))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{} /data/web_static/current".format(m_file[0]))
        return True
    except Exception as e:
        print(e)
        return False
