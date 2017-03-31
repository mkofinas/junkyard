#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import datetime
import errno
import shutil

import exifread


for item in os.listdir(os.getcwd()):
    file_ext = item.split('.')[-1]
    if file_ext in ['JPG', 'jpg', 'jpeg']:
        with open(item, 'rb') as f:
            tags = exifread.process_file(f)
            if 'EXIF DateTimeOriginal' in tags.keys():
                dt = tags['EXIF DateTimeOriginal']
                q = datetime.datetime.strptime(dt.printable, '%Y:%m:%d %H:%M:%S').date()

                if q > datetime.date(q.year, 8, 31):
                    dirname = str(q.year + 1)
                else:
                    dirname = str(q.year)
                try:
                    os.mkdir(dirname)
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise exc
                    pass
                shutil.move(os.path.join(os.getcwd(), item),
                            os.path.join(os.getcwd(), dirname))
                print('{0}: {1}/{2}/{3} -> {4}'.format(
                        item, q.day, q.month, q.year, dirname), end='')
            else:
                print('{0}: No "EXIF DateTimeOriginal"'.format(item))
    else:
        print('{0} is not an image'.format(item))
