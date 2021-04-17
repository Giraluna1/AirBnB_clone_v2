#!/usr/bin/python3
""" Module Compress before sendig """

from fabric.api import local, run, put, env
import datetime
from os.path import getsize

env.hosts = ['34.75.65.42', '34.227.197.137']


def do_pack():
    """ This script comprime .tgz """

    try:
        date = datetime.datetime.now()
        date = date.strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        # create the file
        local('tar -cvzf versions/web_static_{}.tgz web_static'.format(date))
        total_size = getsize('./versions/web_static_{}.tgz'.format(date))
        print('web_static packed: versions/web_static_{}.tgz -> {}Bytes'.
              format(date, total_size))
        return ('./versions/web_static_{}.tgz'.format(date))
    except:
        return None


def do_deploy(archive_path):
    """ Distributes an archive to  your web serves """

    try:
        # Upload
        put(archive_path, '/tmp/')
        # Uncompress
        dir_name = archive_path[9:-4]
        run('mkdir -p /data/web_static/releases/{}/'.format(dir_name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'.
            format(dir_name, dir_name))
        # Delete the archive
        run('rm /tmp/{}.tgz'.format(dir_name))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.
            format(dir_name, dir_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.
            format(dir_name))
        # Delete the symbolic link
        run('rm -rf /data/web_static/current')
        # Create a new the symbolic link
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
            format(dir_name))
    except:
        return False
