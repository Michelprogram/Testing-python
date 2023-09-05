import re

def find_word_in_sentence(lookingfor, sentence):
    # Split the sentence into an array of words
    words = sentence.split(" ")

    # Loop through each word in the array
    for word in words:
        # Check if the lowercase version of the word matches the lowercase version of the word we're looking for
        if word.lower() == lookingfor.lower():
            # If there's a match, return True
            return True
        
    # If we've looped through all the words and haven't found a match, return False
    return False     

def find_word_in_sentence_with_regex(word, sentence):
    # Create a regular expression pattern that matches the word
    pattern = re.compile(r'\b{}\b'.format(word), flags=re.IGNORECASE)
    
    # Search for the pattern in the sentence
    match = pattern.search(sentence)
    
    # Return True if the pattern is found, False otherwise
    return bool(match)