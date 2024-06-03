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


finish = False
while not finish:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    cesar(direction, text, shift)
    ask_for_continue = input("Do you want to continue?(Enter y for Yes and n for No)\n").lower()
    if ask_for_continue == "y":
        os.system('clear')
        finish = False


    else:
        print("GOOD BYE")
        finish = True
