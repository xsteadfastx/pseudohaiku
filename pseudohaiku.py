import re
import random
import wikipedia
from hyphen import Hyphenator


def syllable_counter(liste):
    h = Hyphenator('en_US')
    counter = 0
    for i in liste:
        #i = i.decode('UTF-8')
        counter = counter + len(h.syllables(i))

    return counter


def matching_sentences(number, text):
    text = text.split()

    liste = []
    while syllable_counter(liste) != number:
        liste = []
        for x in range(number):
            choice = random.choice(text)
            liste.append(choice)

    return liste


def haiku(text):
    verse_list = []
    verse_list.append(' '.join(matching_sentences(5, text)))
    verse_list.append(' '.join(matching_sentences(7, text)))
    verse_list.append(' '.join(matching_sentences(5, text)))

    return verse_list


def main():
    wikipedia.set_lang('en')
    page = wikipedia.page('The Breakfast Club')
    text = page.content
    text = re.sub('[^a-zA-Z]+', ' ', text)

    for i in haiku(text):
        print(i)


if __name__ == '__main__':
    main()
