from Retriver import *
from Dictionary import *


dictionary = Dictionary()
dictionary.dictionary, s = dictionary.read_dict()
print(len(dictionary.dictionary.keys()))
ret = Retriever(dictionary)
ret.get_dict()
ret.get_query()
ret.retrieve()

