import string

direction = input("Type 'encode', to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alphabet = string.ascii_lowercase

if direction == "encode":
    def encrypt():
        new_letter_2 = []

        for i in text:
            new_letter_1 = (alphabet.find(i) + shift) % 26
            new_letter = alphabet[new_letter_1]
            new_letter_2 += new_letter

        print("".join(new_letter_2))
    encrypt()
else:
    def decrypt():
        new_letter_3 = []

        for i in text:
            new_letter_4 = (alphabet.find(i) - shift) % 26
            new_letter_5 = alphabet[new_letter_4]
            new_letter_3 += new_letter_5

        print("".join(new_letter_3))
    decrypt()






