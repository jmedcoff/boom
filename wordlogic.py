import yaml
import random


word_type_to_boomhauerism_map = {
    'JJ': 'adjectives',
    'JJR': 'adjectives',
    'JJS': 'adjectives',
    'NN': 'adjectives',
    'NNS': 'adjectives',
    'NNP': 'adjectives',
    'NNPS': 'adjectives',
    'PRP': 'adjectives',
    'PRP$': 'adjectives',
    'VB': 'pre_present_verbs',
    'VBP': 'pre_present_verbs',
    'VBZ': 'pre_present_verbs',
    'VBD': 'pre_past_verbs',
    'VBG': 'pre_participles',
    'VBN': 'pre_participles'
}

with open('./boom/boomhauerisms.yaml') as my_file:
    boom = yaml.load(my_file, Loader=yaml.FullLoader)

def do_word_replacements(words):
    result = []
    for word in words:
        result.append(do_word_replacement(word))
    return result

def do_word_replacement(word):
    for dictionary in boom['direct_word_replacements']:
        if word[0] in dictionary:
            return ((random.choice(dictionary[word[0]]), word[1]))
    return word

def its_hot_enough(temperature):
    return random.random() < temperature

def process_sentence(word_list, temperature):
    sentence = []

    if its_hot_enough(temperature):
        sentence.append(get_sentence_starter())
    
    for word in word_list:
        if its_hot_enough(temperature):
            sentence.append(get_boomhauerism(word))
        sentence.append(word[0])
    
    if its_hot_enough(temperature):
        sentence.append(get_sentence_ender())
        
    return ' '.join([word for word in sentence if word != None])


def get_boomhauerism(word):
    if word[1] in word_type_to_boomhauerism_map:
        return random.choice(boom[word_type_to_boomhauerism_map[word[1]]])

def get_sentence_starter():
    return random.choice(boom['sentence_starters'])

def get_sentence_ender():
    return random.choice(boom['sentence_enders'])

