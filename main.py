file_path = '/home/niels/workspace/github.com/TheMammoet/bookbot/books/frankenstein.txt'

#open file path
with open(file_path, 'r') as f:
    
    #count the number of words
    num_words = 0
    file_contents = f.read()
    words = file_contents.split()
    num_words = len(words)
    print(num_words)
    
#count the frequency of alphabetic characters    
char_dict = {}
for char in file_contents.lower():
    if char.isalpha(): #only look for alfabethic characters
        char_dict[char] = char_dict.get(char, 0) + 1
        
#Sort the character dictianoary by frequency in desending order        
sorted_chars = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)

#print the report
print(f'--- Begin report of {file_path} ---')
print(f'{num_words} words founf in the document\n')

for char, count in sorted_chars:
    print(f"The '{char}' character was found {count} times")

print('\n--- End report ---')
            
        
   
        
    
    
    