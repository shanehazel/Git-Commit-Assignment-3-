# pseudocode

# ask user for plaintext and keyword (all caps, no spaces)
plaintext_str = input("Enter the message to encrypt: ")
keyword_str = input("Enter the keyword to encrypt: ")

# define cipher string
def cipher_str(plaintext_str, keyword_str):

    # make the plaintext and keyword all caps and no spaces
    plaintext_str = plaintext_str.upper().replace("","")
    keyword_str = keyword_str.upper().replace("","")

# store the value in cipher code
    ciphercode = ""

# check every character in the plaintext
# translate letter to its corresponding nuumber
# encrypt the plaintext with the given keyword
# translate number to its corresponding letter
# convert cipher text int to str
# print output