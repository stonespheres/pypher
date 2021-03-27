import vig
def decryption(encrypt_text, key): 
  orig_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 

if __name__ == "__main__": 
  string = input("Enter the message: ")
  key = input("Enter the keyword: ")
  print("Decrypted message:", decryption(encrypt_text, key)) 