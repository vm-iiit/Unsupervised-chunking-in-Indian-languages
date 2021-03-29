# Loading Libraries
from nltk.chunk.regexp import ChunkString, ChunkRule, ChinkRule
from nltk.tree import Tree
from nltk.chunk import RegexpChunkParser


# ChunkString() starts with the flat tree
tree = Tree('S', [('the', 'DT'), ('book', 'NN'),
               ('has', 'VBZ'), ('many', 'JJ'), ('chapters', 'NNS')])
  
# Initializing ChunkRule
chunk_rule = ChunkRule('<DT><NN.*><.*>*<NN.*>', 'chunk determiners and nouns')
  
  
# Another ChinkRule
chink_rule = ChinkRule('<VB.*>', 'chink verbs')
  
# Applying RegexpChunkParser
chunker = RegexpChunkParser([chunk_rule, chink_rule], chunk_label ='CP')
chunker.parse(tree)
