#!/usr/bin/python3
""" Module Compress before sendig """

import fabric.api
from fabric.api import local
import datetime
from os.path import getsize


def do_pack():


""" is Fabric script """

 date = datetime.datetime.now()
  date = date.strftime("%Y%m%d%H%M%S")
   try:
        with hide('running', 'stdout'):
            local('mkdir -p versions')
        # create the file
        local('tar -cvzf versions/web_static_{}.tgz web_static'.format(date))
        total_size = getsize('./versions/web_static_{}.tgz'.format(date))
        print('web_static packed: versions/web_static_{}.tgz -> {}Bytes'.
              format(date, total_size))
        return ('./versions/web_static_{}.tgz'.format(date))
    except Exception:
        return None
