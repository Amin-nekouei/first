import os



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cesar(this_direction, this_text, this_shift):
    if this_direction != "encode" or "decode":
        print("Your Answer is not valid")
    if this_direction == "decode":
        this_shift *= -1
    new_word = ""
    for letter in this_text:
        if letter in alphabet:
            new_word += alphabet[alphabet.index(letter) + this_shift]
        else:
            new_word += letter
    print(new_word)

