# Morse Code dictionary mapping characters to their Morse Code representations
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Creating a reversed dictionary for decryption
reversed_dict = {value: key for key, value in MORSE_CODE_DICT.items()}

def encrypt(message):
    """
    Encrypts the given message into Morse Code.

    :param message: The message to be encrypted.
    :return: The encrypted Morse Code representation of the message.
    """
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher

def decrypt(message):
    """
    Decrypts the given Morse Code message into plain text.

    :param message: The Morse Code message to be decrypted.
    :return: The decrypted plain text.
    """
     
    i = 0
    plaintext = ''
    ciword = ''
    message += ' '
    try:
        while i < len(message):
            if message[i] != ' ':
                ciword += message[i]
            else:
                if ciword == '':
                    plaintext += ' '
                else:
                    plaintext += reversed_dict[ciword]
                ciword = ''
            i += 1
        return plaintext
    except KeyError:
        print("Invalid input")
        return ""

def main():
    """
    Main function to interactively perform encryption or decryption based on user input.
    """
    exit = False
    while not exit:
        action = input("Do you want to encrypt or decrypt? (e/d): ")
        if action == 'e':
            message = input("Enter message: ")
            result = encrypt(message.upper())
            print(result)
        elif action == 'd':
            message = input("Enter message: ")
            result = decrypt(message)
            print(result)
        else:
            print("Invalid input")
        exit = input("Do you want to exit? (y/n): ") == 'y'


if __name__ == '__main__':
    main()


