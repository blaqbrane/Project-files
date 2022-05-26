# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def is_anagram(word1,word2):
    # [assignment] Add your code here
    return sorted(word1) == sorted(word2)
print(is_anagram("team", "meat"))

 
    #return True

