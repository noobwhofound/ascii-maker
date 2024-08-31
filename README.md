# Makes ascii arts

can save it on a txt file with adding the following code to the file:
`py
text = []
text.append(all_letters[pos])
text.append('\n')
with open('h.txt', 'w') as f:
    f.write(''.join(text))
`

has 2 type of chars:
1 - almost full ascii chars, good for bigger pictures -> all_chars
2- only contains two chars, good for smaller pictures -> less_chars




