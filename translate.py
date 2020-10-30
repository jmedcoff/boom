import nltk
import random
from . import wordlogic


grammatical_exclusions = ['RB', 'VBP', 'VBZ', 'IN', ',', '.', '?', '!']

def translate(sentence, temperature):
    tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    words = [item for item in tagged if item[0] != 'I' and item[1] not in grammatical_exclusions]
    words = wordlogic.do_word_replacements(words)
    return wordlogic.process_sentence(words, temperature)

