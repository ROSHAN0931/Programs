# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
#             's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
#             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet 
#by the shift amount and print the encrypted text.  
#e.g. :
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test 
#the code and encrypt a message.
#TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#TODO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#e.g. 
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"
#TODO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
# Then call the correct function based on that 'drection' variable.You should be able to test the 
# code to encrypt *AND* decrypt a message.

# def encrypt(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         pos=alphabet.index(letter)
#         newpos=pos + shift_amount
#         newletter=alphabet[newpos]
#         cipher_text+=newletter
#     print(f"The encoded text is {cipher_text}")
        


# def decrypt(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         pos=alphabet.index(letter)
#         newpos=pos - shift_amount
#         newletter=alphabet[newpos]
#         cipher_text+=newletter
#     print(f"The decoded text is {cipher_text}")
    


# if direction=="encode":
#     encrypt(plain_text=text,shift_amount=shift)
# elif direction=="decode":
#     decrypt(plain_text=text,shift_amount=shift)