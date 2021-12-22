"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self):
        """
        opens the word file in 'read only' mode 
        """
        self.file = open('words.txt', 'r')
    
    def get_random_word(self):
        """
        imported random lib and selected a word from word file
        scrolled back to begining of word file
        """
        rand_word = random.choice(list(self.file))
        self.file.seek(0)
        return rand_word.replace('\n','')
