#!/usr/bin/python3
"""distributes an archive to your web servers"""

import os.path
import fabric.api
fabric.api.env.hosts = ['54.82.98.129', '52.207.196.248']


def do_deploy(archive_path):
    """Prototype: def do_deploy(archive_path)"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        file = archive_path.split("/")[-1]
        rm = file.split(".")[0]
        path = "/data/web_static/releases/"
        path2 = "/data/web_static/current"

        fabric.api.put(archive_path, '/tmp/')

        fabric.api.run('mkdir -p {}{}/'.format(path, rm))

        fabric.api.run('tar -zxf /tmp/{} -C {}{}/'.format(file, path, rm))

        fabric.api.run('rm -f /tmp/{}'.format(file))

        fabric.api.run('mv -f {0}{1}/web_static/* {0}{1}/'.format(path, rm))

        fabric.api.run('rm -rf {}{}/web_static'.format(path, rm))

        fabric.api.run('rm -rf {}'.format(path2))

        fabric.api.run('ln -fs {}{}/ {}'.format(path, rm, path2))

        print ("New version deployed!")
        
        return True

    except ValueError:
        return False
