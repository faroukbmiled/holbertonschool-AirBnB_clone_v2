#!/usr/bin/python3
"script that generates a .tgz archive"

import fabric.api
import datetime
import os.path


def do_pack():
    "Prototype: def do_pack():"
    try:
        date_format = "%Y%m%d%H%M%S"
        date = datetime.datetime.now().strftime(date_format)
        if os.path.isdir("versions") is False:
            fabric.api.local("mkdir versions")
        name = "versions/web_static_{}.tgz".format(date)
        fabric.api.local("tar -cvzf {} web_static".format(name))
        return name
    except ValueError:
        return None
