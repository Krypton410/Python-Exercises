def nfruits(dictionary, string):
    i = 0
    string = sorted(string)

    for idx, char in enumerate(string):
        dictionary[char] -= 1
        if idx < len(string) - 1:
            for key in dictionary:
                if key != char:
                    dictionary[key] += 1
        print dictionary
    return dictionary[max(dictionary, key = dictionary.get)]