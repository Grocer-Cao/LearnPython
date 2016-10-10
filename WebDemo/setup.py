#!/usr/bin/env Python
# -*- coding: utf-8 -*-

import setuptools

# In Python < 2.7.4, a lazy loading of package `pbr` will break
# setuptools if some other modules registered functions in `atexit`.
# solution from: http://bugs.Python.org/issue15881#msg170215

try:
    import multiprocessing #noqa
except ImportError:
    pass

setuptools.setup(setup_requires=['pbr'],pbr=True)