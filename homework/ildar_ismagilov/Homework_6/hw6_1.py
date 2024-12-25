text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
text_to_list = text.split()
new_list = []

for word in text_to_list:
    if ',' in word:
        new_list.append(word[:len(word) - 1] + 'ing,')
    elif '.' in word:
        new_list.append(word[:len(word) - 1] + 'ing.')
    else:
        new_list.append(word + 'ing')

final_text = ' '.join(new_list)
print(final_text)
