# Inbuilt string methods  - Single program 
s = " Kodnest Technologies 123 "

print("original strings:", s) # Kodnest technologies 123

# case conversion methods
print("upper():", s.upper()) # Kodnest technologies 123
print("lower():", s.lower()) # Kodnest technologies 123
print("capitalize():", s.capitalize()) # Kodnest technologies 123
print("title():", s.title()) # Kodnest technologies 123
print("swapcase():", s.swapcase()) # Kodnest technologies 123

# searching & counting 
print("find(Tech'):", s.find("Tech")) # 10 
print("count(' o '):", s.count("o")) # 3 

# Replace
print("replace('123', '2025'):", s.replace("kodnest", "2025"))

# start & end check 
print("startswith('  kod'):", s.startswith(" kod")) # true 
print("endswith('123  '):", s.endswith("123  ")) # true

# split & join 
words = s.split() #
print("split():", words)
print("join():", "-".join(words))

# strip spaces
print("strip():", s.strip())
print("lstrip():", s.lstrip())
print("rstrip():", s.rstrip())

s = "   "
#checking methods 
print("isalpha():", s.isalpha())
print("isdigit():", s.isdigit())
print("isspace():", s.isspace())
print("isalnum():", s.isalnum())
print("Hello".isalnum()) #true 

#length
print("length of string:", len(s))


