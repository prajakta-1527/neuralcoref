

import spacy
nlp = spacy.load('en_core_web_sm')

import neuralcoref
neuralcoref.add_to_pipe(nlp)

doc = nlp('Once upon a time, there was a boy. The boy liked to go to the park and play with his friends. One day the boy felt ill and couldnt go to the park. His friends came to his home and brought him a cake. , modern disney style')

print(doc._.has_coref)
print(doc._.coref_clusters)
print(doc._.coref_resolved)
print(doc._.coref_scores)
