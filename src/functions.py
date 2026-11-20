"""
Function for the initial greeting of the user
"""
def greeting():

    name = input("Welcome stranger! Lets get to know you. What is your name? ")

    message = f"Hello {name}! This is the Syno-tempt game!\n\nTo summarise:\n1.You will be given a word\n\n2.You will then have to guess a synonym of the given word\n\n3.Guess a synonym and if it is correct, it will be confirmed by the game\n\n4.If it is wrong, you will be given a strike.\n\nYou only have a maximum of 10 strikes so be careful!"

    print(message)


"""
Function to generate a random word from wonderwords library
"""

def generate_word():

    from wonderwords import RandomWord

    r = RandomWord()

    word = r.word(include_categories=["verb", "adjective"])
    return word

"""
Function to generate the synonym of a given word with AyDictionary library
"""

def synonym():

    given_word = generate_word()
    from AyDictionary import AyDictionary

    dictionary = AyDictionary()

    synonym = dictionary.synonym(given_word)

    return synonym, given_word

"""Function to generate the definition of a given word with AyDictionary library"""

def definition(word):

    
    from AyDictionary import AyDictionary
    dictionary = AyDictionary()

    meaning = dictionary.meaning(word)
    return meaning
    