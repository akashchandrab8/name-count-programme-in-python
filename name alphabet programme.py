
name = input("type your name : ") # enter a name 
name_alphabet_count = "" # this is empty for count used in 'for' loop 
for t in range(len(name)):
    if name[t] not in name_alphabet_count:
        name_alphabet_count += name[t]
        print(f"{name[t]} :- {name.count(name[t])}")
