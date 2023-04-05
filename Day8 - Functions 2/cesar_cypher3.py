alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(plain_text, direction, shift_amount):
    size = len(alphabet)
    coded = ""

    if direction == "decode":
        shift_amount = shift_amount * -1

    for letter in plain_text:
        position = alphabet.index(letter)
        position += shift_amount
        if(position > size):
            position -= size
        if(position < 0):
            position += size
        letter = alphabet[position]
        coded += letter
    print(f"The final text is {coded}")

caesar(text, direction, shift)