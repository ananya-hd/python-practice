#String indexing
name = "Ananya"
print("Name :",name)
print("First character:",name[0])
print("Second character:",name[2])
print("Last character:",name[-1])
print("Length of string:",len(name))


#Print each character in a word
word = input("Enter a word: ")
for ch in word:
    print(ch)

#Count vowels in a word
word = input("Enter a word: ")
vowel_count = 0
for ch in word:
    if ch == 'a' or ch == 'e' or ch=='i' or ch=='o' or ch =='u':
        vowel_count += 1
print("Number of vowels:",vowel_count )