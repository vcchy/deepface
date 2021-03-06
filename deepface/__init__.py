# -*- coding: utf-8 -*-
"""deepface
"""
from __future__ import absolute_import

from . import confs
from . import detectors
from . import recognizers
from . import utils

from .shortcuts import \
    get_detector, \
    get_recognizer, \
    save_features
