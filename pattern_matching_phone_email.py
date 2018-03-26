import pyperclip, re

text=str(pyperclip.paste())

phoneRegex = re.compile(r'''(
    ( \d{3} | \(\d{3}\) ) # the prefix (area)
    ( \s | - | \.)   #   sep
    (\d{3})
    ( \s | - | \.)   #   sep
    (\d{4})
    (\s* (ext|x|ext.) \s* (\d{2,5}))?
)''',re.VERBOSE)

emailRegex = re.compile(r'''(
    [A-Za-z-.0-9%+-]+ # username
    @
    [A-Za-z0-9.-]+
    (\.[A-Za-z]{2,4})
)''', re.VERBOSE)

matches=[]

for groups in phoneRegex.findall(text):
    phoneNumber='.'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNumber)

for groups in emailRegex.findall(text):
    matches.append(groups[0])


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print("NO matches")
