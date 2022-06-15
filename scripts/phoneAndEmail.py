# phoneAndEmail.py
#
# Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# phone regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # area code
    (\s|-|\.)?              # separator
    (\d{3})                 # first 3 digits
    (\s|-|\.)               # separator
    (\d{4})                 # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)
# groupの中にarea code, separator...のgroupがあることに注意。

# just for test
mo = phoneRegex.search('test phone number: 415-222-5556')
print(f"Phone number found: {mo.group(1)}")

# email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
)''', re.VERBOSE)

