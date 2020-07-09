In [52]:
def char_test(s):
  uppercase,lowercase,special=0,0,0
  for char in s:
    if char.isupper():
        uppercase+=1
    elif char.islower():
        lowercase+=1
    else:
        special+=1
  print("number of uppercase characters=",uppercase)
  print("number of lowercase characters=",lowercase)
  print("number of special characters=",special)