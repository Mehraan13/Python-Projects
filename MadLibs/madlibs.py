'''Mad Libs is a word game where players fill in the blanks of a story with words like adjectives, nouns, colors, and more. 
The result is a humorous story that's read aloud '''

#open the story as file
with open("story.txt" , 'r') as f:
    story = f.read()


start_of_word = -1
start_char = '<'
end_char = '>'

words = set()

#get all the placeholders (noun,adj, etc.) and store in the set
for i, char in enumerate(story):
    if char == start_char: #mark start of word
        start_of_word = i
    
    if char == end_char and start_of_word != -1:
        word = story[start_of_word : i + 1]
        words.add(word)
        start_of_word = -1 #reset the start of word

#ask the user for the madlibs
answers = {}

for word in words:
    answers[word] = input(f"Enter a {word}: ")

#now we need to replace the words in the story

for word in words:
    story = story.replace(word,answers[word]) #.replace returns a new string

print(story)