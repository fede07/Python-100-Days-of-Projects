alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):

    size = len(alphabet)
    coded = ""

    for letter in text:
        position = alphabet.index(letter)
        position += shift
        if(position > size):
            position -= size
        if(position < 0):
            position += size
        letter = alphabet[position]
        coded += letter
    print(coded)
    

if(direction == "decode"):
    shift *= -1 

encrypt(text, shift)

print(text)
