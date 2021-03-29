# Loading Libraries
from nltk.chunk.regexp import ChunkString, ChunkRule, ChinkRule
from nltk.tree import Tree

# ChunkString() starts with the flat tree
tree = Tree('S', [('the', 'DT'), ('book', 'NN'),
               ('has', 'VBZ'), ('many', 'JJ'), ('chapters', 'NNS')])
  
# Initializing ChunkString()
chunk_string = ChunkString(tree)
print ("Chunk String : ", chunk_string)
  
# Initializing ChunkRule
chunk_rule = ChunkRule('<DT><NN.*><.*>*<NN.*>', 'chunk determiners and nouns')
chunk_rule.apply(chunk_string)
print ("\nApplied ChunkRule : ", chunk_string)
  
# Another ChinkRule
ir = ChinkRule('<VB.*>', 'chink verbs')
ir.apply(chunk_string)
print ("\nApplied ChinkRule : ", chunk_string, "\n")
  
# Back to chunk sub-tree
chunk_string.to_chunkstruct()
