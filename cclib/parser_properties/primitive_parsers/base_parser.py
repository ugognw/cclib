# Copyright (c) 2024, the cclib development team
#
# This file is part of cclib (http://cclib.github.io) and is distributed under
# the terms of the BSD 3-Clause License.
from abc import ABC


class base_parser(ABC):
    @staticmethod
    @abstractmethod
    def parse(file_handler, program, ccdata):
        return
