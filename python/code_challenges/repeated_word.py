def repeated_word(str):
    '''
    Finds the first word to occur more than once in a string
    Arguments: string
    Return: string
    '''
    tracker = {}
    words = str.split(' ')
    for element in words:
        word = ''
        for ch in element:
            if ch.isalpha():
                word += ch.lower()
        if word in tracker:
            tracker[word] += 1
            return word
        else:
            tracker[word] = 1
    print('No repeated word in the given string.')
    return tracker
