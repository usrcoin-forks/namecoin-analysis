#!/usr/bin/env python3

from re import match
from collections import Counter
import pickle
import pdb

from nltk.util import ngrams

from common import getDictSubset
from nameHistory import getMaxHeight
from segment_string import SegmentString

DOMAIN_REGEX = "^[a-z]([a-z0-9-]{0,62}[a-z0-9])?$"
def valid_domain_name(name, has_prefix=True):
    return bool(match(DOMAIN_REGEX, name.name()[2:]))


with open("nameDict.dat", "rb") as pickle_file:
    names_dict = pickle.load(pickle_file)

max_height = getMaxHeight(names_dict)
names_dict = getDictSubset(names_dict,
                      lambda record: record.isValidAtHeight(max_height))

names_dict = getDictSubset(names_dict,
                                 lambda record: record.namespace() == "d")
names_dict = getDictSubset(names_dict, valid_domain_name)

segment_counts = sorted([SegmentString().string_segments(name[2:]) for name in names_dict.keys()])

with open("segment_counts.pickle", "wb") as output_file:
    pickle.dump(segment_counts, output_file)
