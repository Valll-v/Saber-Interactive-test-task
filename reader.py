"""
Файл от
"""


import yaml
from yaml.parser import ParserError
from conf import FILENAME_BUILDS, FILENAME_TASKS
from loguru import logger


def read_file(filename):
    with open(filename) as file:
        try:
            data = yaml.load(file, yaml.FullLoader)
            return data
        except ParserError as ex:
            logger.error(ex)
            exit()


def read_tasks():
    return read_file(FILENAME_TASKS)


def read_builds():
    return read_file(FILENAME_BUILDS)
