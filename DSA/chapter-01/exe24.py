"""Write a short Python function that counts the number of vowels in a given
character string."""



def num_of_vowels(word: str) -> str:
    vowels = set('aeiouAEIOU')

    found = 0
    # for c in vowels:
    #     if c in word:
    #         found += 1
    for c in word:
        if c in vowels:
            found += 1

    return found

if __name__ == '__main__':
    print(num_of_vowels("jimroxodezi"))