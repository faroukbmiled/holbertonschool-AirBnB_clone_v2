#!/usr/bin/python3
"""distributes an archive to your web servers"""

import os.path
from fabric.api import run, put, env, runs_once
env.hosts = ['54.82.98.129', '52.207.196.248']


@runs_once
def do_deploy(archive_path):
    """Prototype: def do_deploy(archive_path)"""
    if os.path.exists(archive_path):
        file = archive_path.split("/")[-1]
        rm = file.split(".")[0]
        path = "/data/web_static/releases/"
        path2 = "/data/web_static/current"

        put(archive_path, '/tmp/')

        run('mkdir -p {}{}/'.format(path, rm))

        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, rm))

        run('rm /tmp/{}'.format(file))

        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, rm))

        run('rm -rf {}{}/web_static'.format(path, rm))

        run('rm -rf {}'.format(path2))

        run('ln -s {}{}/ {}'.format(path, rm, path2))

        print("New version deployed!")

        return True

    return False
