letter = ' '.join(input().strip().split())
at_index = letter.find('@')
if at_index != -1:
    hashtag_index = letter.find('#', at_index)
    if hashtag_index != -1:
        letter = letter[:hashtag_index] + letter[hashtag_index+1:]
for i in letter:
    if i == '\\' and letter[letter.index('\\') + 1] == 'n':
        print("Formatted Text: ", letter[:letter.index('\\n')])
        print(letter[letter.index('\\n') + 2:])