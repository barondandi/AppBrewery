alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alphabet_lenght = len(alphabet)

#1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(input_text, shift_amount, selection):
    output_text = ""
    for letter in input_text:
        position = alphabet.index(letter)
        if selection == "encode":
            new_position = position + shift_amount
            if new_position >= alphabet_lenght:
                new_position -= alphabet_lenght
        elif selection == "decode":
            new_position = position - shift_amount
            if new_position < 0:
                new_position += alphabet_lenght
        output_text += alphabet[new_position]
    print(f"The {selection}d text is {output_text}.")

#2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(input_text=text, shift_amount=shift, selection=direction)
