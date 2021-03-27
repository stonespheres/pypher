def makecode(message, code): 
  code = list(code) 
  if len(message)==len(code): 
    return(code) 
  else: 
    for i in range(len(message)-len(code)): 
      code.append(code[i%len(code)]) 
  return("" . join(code)) 
  
def encryp(message, code): 
  enc_text = []
  for i in range(len(message)): 
    x = (ord(message[i])+ord(code[i]))%26
    x += ord('A') 
    enc_text.append(chr(x)) 
  return("".join(enc_text)) 

def decryp(enc_text, code): 
  orig_text = [] 
  for i in range(len(enc_text)): 
    x = (ord(enc_text[i])-ord(code[i])+26)%26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("".join(orig_text)) 

def main(): 
  message = input("Enter the message: ")
  codeword = input("Enter the codeword: ")
  code = makecode(message, codeword) 
  enc_text = encryp(message,code) 
  print("Encrypted message:", enc_text) 
  print("Decrypted message:", decryp(enc_text, code)) 

main()