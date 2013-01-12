#!/usr/bin/env python

from distutils.core import setup

setup(
    name='tornado_websocket_client',
    version='0.0.4',
    description='Tornado Web Socket Client',
    author='Jeff Balogh',
    py_modules=["tornado_websocket_client"],
    requires=["tornado"],
)
