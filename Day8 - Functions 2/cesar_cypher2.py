alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    size = len(alphabet)
    coded = ""

    for letter in plain_text:
        position = alphabet.index(letter)
        position += shift_amount
        if(position > size):
            position -= size
        letter = alphabet[position]
        coded += letter
    print(f"The encoded text is {coded}")

def decrypt(plain_text, shift_amount):
    size = len(alphabet)
    coded = ""

    for letter in plain_text:
        position = alphabet.index(letter)
        position -= shift_amount
        if(position < 0):
            position += size
        letter = alphabet[position]
        coded += letter
    print(f"The decoded text is {coded}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if(direction == "encode"):
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Command not found")