
user_input = input("what's the answer to the great question of life, the Universe and Everything?  ").strip().lower()

if user_input in ["42", "forty-two", "forty two"]:
    print("Yes")
else:
    print("No")
 
