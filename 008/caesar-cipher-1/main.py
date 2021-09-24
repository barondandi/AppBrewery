alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
text_lenght = len(text)
# print(text_lenght)
alphabet_length = len(alphabet)

#1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text = text, encrypt_shift = shift):

    #2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    #print(f"The plain text is {plain_text}")
    cipher_list = []
    for i in range(0, text_lenght):
        order = alphabet.index(plain_text[i])
        #print(order)
        if (order + shift) <= (alphabet_length - 1):
            cipher_list.append(alphabet[order + shift])
        else:
            cipher_list.append(alphabet[(order + shift) - alphabet_length])
    #cipher_list is currently a list and not a string
    #print(cipher_list)
    #to turn it into a string
    cipher_text = ""
    for character in cipher_list:
        cipher_text += character
    print(f"The encoded text is {cipher_text}")

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text, shift)


'''SOLUTION 1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Don't change the code above 👆

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
  #TODO-2: Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text.  
  #e.g. 
  #plain_text = "hello"
  #shift = 5
  #cipher_text = "mjqqt"
  #print output: "The encoded text is mjqqt"
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(plain_text=text, shift_amount=shift)
'''

'''SOLUTION 2
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Don't change the code above 👆

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > len(alphabet):
            new_position -= len(alphabet)
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

encrypt(plain_text=text, shift_amount=shift)
'''