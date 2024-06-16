# Copyright (c) 2024, the cclib development team
#
# This file is part of cclib (http://cclib.github.io) and is distributed under
# the terms of the BSD 3-Clause License.
from dataclasses import dataclass

import cclib.attribute_parsers as cprops


@dataclass
class combinator:
    name: str
    job_list: list


DEFAULT_PARSERS = [
    cprops.scfenergies,
    cprops.atomcoords,
    cprops.atomcharges,
    cprops.atomnos,
    cprops.charge,
    cprops.ccenergies,
    cprops.dispersionenergies,
    cprops.mult,
    cprops.moenergies,
    cprops.natom,
    cprops.coreelectrons,  # dependncy on natom
    cprops.nbasis,
    cprops.gbasis,
    cprops.aooverlaps,
    cprops.atommasses,
    cprops.mosyms,
    cprops.nmo,
    cprops.atombasis,
    cprops.scftargets,
    cprops.scfvalues,
]


class auto_combinator(combinator):
    def __init__(self, tree):
        self.name = f"Autogenerated combinator for {tree.num_nodes:} jobs"
        self.job_list = [DEFAULT_PARSERS for i in range(tree.num_nodes)]
