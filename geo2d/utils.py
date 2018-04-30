# -*- coding: <utf-8> -*-

import logging

utils_logger = logging.getLogger(__name__)


def check_iterable(iterable):
    utils_logger.debug('Checking if %s is iterable.', iterable)
    if not hasattr(iterable, '__iter__'):
        utils_logger.critical('Rasing AttributeError error...')
        raise AttributeError


def chunk(iterable, size):
    check_iterable(iterable)
    return [iterable[i: i + size] for i in range(0, len(iterable), size)]
