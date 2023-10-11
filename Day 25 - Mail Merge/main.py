#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

fLetter = open(r"Day 25 - Mail Merge\Input\Letters\starting_letter.txt", "r")
default_letter = fLetter.readlines()
fLetter.close()

names = open(r"Day 25 - Mail Merge\Input\Names\invited_names.txt", "r")

for name in names:
    print(name)
    name = name.strip()
    letter = default_letter.copy()
    print(f"DEB: {len(letter)}\n")
    letter[0] = letter[0].replace("[name]", name)
    newLetter = open(f"Day 25 - Mail Merge\Output\ReadyToSend\{name}_letter.txt", "a")
    for line in letter:
        newLetter.write(line)
    newLetter.close()

names.close()
    



#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp