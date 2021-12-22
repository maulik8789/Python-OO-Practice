"""Word Finder: finds random words from a dictionary."""
import random
import itertools

class WordFinder:
    
    def __init__(self, file):
        """
        opens the word file in 'read only' mode 
        """
        file = open('words.txt', 'r')
        self.file = file
    
    def get_random_word(self):
        """
        imported random lib and selected a word from word file
        scrolled back to begining of word file
        """
        rand_word = random.choice(list(self.file))
        self.file.seek(0)
        return rand_word.replace('\n','')

class SpecialWordFinder(WordFinder):
    
    def __init__(self):
        super().__init__()

    def get_random_word():
        for _ in itertools.repeat([]):
            rand_word = random.choice(list(super().file))
            super().file.seek(0)
            if rand_word[0] != '#' or rand_word[0] != " ":
                break
        return rand_word.replace('\n','')

