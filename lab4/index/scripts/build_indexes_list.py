import sys
sys.path.append("../")

from collections import defaultdict
from index import Index
from util.dict_util import has_key

def search_docid_record_in_indexes(values, docid):
  index = -1
  count = 0
  
  for (i, value) in enumerate(values):
    tuple_docid, frequency = value
    if tuple_docid == docid:
      index = i
      count = frequency
      
  return (index, count)

def build_index(row):
  indexes = defaultdict(list)
  docid, tokens = row
  
  for token in tokens:
    if has_key(indexes, token):
      values = indexes[token]
      index_of_record, frequency = search_docid_record_in_indexes(values, docid)
      is_encontered = index_of_record != -1
      if is_encontered:
        indexes[token][index_of_record] = Index(token, docid, frequency + 1)
      else:
        indexes[token].append(Index(token, docid, 1))
    else:
        indexes[token].append(Index(token, docid, 1))

