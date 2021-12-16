def sortSentence(s: str) -> str:
    dictionary = {}
    
    sentence = s.split()
    print(sentence)
    
    for word in sentence:
        dictionary[word[-1]] = word[:-1]
        
    word = ""
    for i in dict(sorted(dictionary.items())):
        print(i)
        word += dictionary.get(i) + " "
    
    word = word.strip()
    return word