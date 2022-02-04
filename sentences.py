import random


def main(gramatical_number, tense):
    t_determiner = get_determiner(gramatical_number)
    t_noun = get_noun(gramatical_number)
    t_verb = get_verb(gramatical_number,tense)
    t_preposition = get_preposition()
    text = f'{t_determiner} {t_noun} {t_verb}'
    return text

def get_determiner(grammatical_number):
    """
    Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If grammatical_number == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        grammatical_number: an integer.
            If grammatical_number == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if grammatical_number == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(grammatical_number):
    """
    Return a randomly chosen noun.
    If grammatical_number == 1, this function will
    return one of these ten single nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        grammatical_number: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if grammatical_number == 1:
        words = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    else:
        words = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_verb(grammatical_number, tense):
    """
    Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and grammatical_number is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and grammatical_number is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        grammatical_number: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense.lower() == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    else:
        if tense.lower() == "present" and grammatical_number == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"]
        
        if tense.lower() == "present" and grammatical_number != 1:
            words = ["drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]

        if tense.lower() == "future":
            words = ["will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_preposition():
    """
        Return a randomly chosen preposition
        from this list of prepositions:
            "about", "above", "across", "after", "along",
            "around", "at", "before", "behind", "below",
            "beyond", "by", "despite", "except", "for",
            "from", "in", "into", "near", "of",
            "off", "on", "onto", "out", "over",
            "past", "to", "under", "with", "without"
    """
    preposition = ["about", "above", "across", "after", "along",
            "around", "at", "before", "behind", "below",
            "beyond", "by", "despite", "except", "for",
            "from", "in", "into", "near", "of",
            "off", "on", "onto", "out", "over",
            "past", "to", "under", "with", "without"]  
    #
    # Randomly choose and return a determiner.
    word = random.choice(preposition)        
    return word

def get_prepositional_phrase(gramatical_number):
    """
    Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    t_determiner = get_determiner(gramatical_number)
    t_noun = get_noun(gramatical_number)
    t_preposition = get_preposition()
    text = f'{t_preposition} {t_determiner} {t_noun}'
    return text

"""
Potential combination of order and tenses

Grammatical Number	Verb Tense
a.	single	past
b.	plural	past
c.	single	present
d.	plural	present
e.	single	future
f.	plural	future

"""
grammatical_number = [1,2,1,2,1,2]
tense = ["past", "past", "present", "present", "future","Future"]
index = 0
while index < len(grammatical_number):
    if index <= len(grammatical_number):
        text = main(grammatical_number[index], tense[index]) + ' '
        text += get_prepositional_phrase(grammatical_number[index])
        print(f'{text}')
        index += 1
print('\n')
