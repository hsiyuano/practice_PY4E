text = "X-DSPAM-Confidence:    0.8475"
atpos = text.find(":") # search the : return its position, it is a number, 18
piece = text[atpos+1:] # takes everything after :, starts one position after :, it is a text with space
stripped = piece.strip() # removes spaces from the beginning and end of a string, it is a text
flt = float(stripped) #convert text into a number
print (flt)

