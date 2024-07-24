import re


# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != "-":
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != "-":
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True


### I. Matching Single Groups
## Example 1
# print("Is 415-555-4242 a phone number?")
# print(isPhoneNumber("415-555-4242"))
# print("Is Moshi moshi a phone number?")
# print(isPhoneNumber("Moshi moshi"))


## Example 2
# message = "Call me at 834-915-4137 tomorrow. 955-092-9531 is my home."
# for i in range(len(message)):
#     chunk = message[i : i + 12]
#     if isPhoneNumber(chunk):
#         print("Phone number found: " + chunk)
# print("Done")

##Example 3
# phoneNumRegex = re.compile(r"(\(\d{2}\)) (\d{10})")
# mo = phoneNumRegex.search("My number is (91) 8349154137 and 834-915-4137.")
# print("Country Code: " + mo.group(1))
# print("Phone number found: " + mo.group(2))
# print("Phone number found: " + mo.group())
# print(mo.groups())

###II. Matching Multiple Groups with the Pipe

## Example 1
# heroRegex = re.compile(r"Shaktimaan|Superman")
# mo2 = heroRegex.search("Superman and Shaktimaan are the best heroes.")
# print(mo2.group())
# mo1 = heroRegex.findall("Shaktimaan and Superman are the best heroes.")
# print(mo1)

## Example 2
# batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
# mo = batRegex.search("Batmobile lost a wheel")
# print(mo.group())# Batmobile
# print(mo.group(1))# mobile


### III. Optional Matching with the Question Mark
## Example 1
# shaktiRegex = re.compile(r"Shakti(wo)?man")
# mo1 = shaktiRegex.search("Shaktiwoman is the best hero.")
# print(mo1.group())

## Example 2
# phoneRegex = re.compile(r"(\d{2}-)?(\d{10})")
# mo = phoneRegex.findall(
#     "91-8349154137,7062031227, 7062158099, 7062241209, 7062391089, 7062476210, 7062543036, 7062624759, 7062717951, 7062821770, 7062970164,"
# )
# for i in mo:
#     print(i[1])

## IV. Matching Zero or More with the Star
# Example 1
# batRegex = re.compile(r"Bat(wo)*man")
# mo = batRegex.search("Batwowowowowoman is the best")
# print(mo.group())

## V .Matching One or More with the Plus
# batRegex = re.compile(r"Bat(wo)+man")
# mo1 = batRegex.search("The Adventures of Batwoman")
# print(mo1.group())

# mo2 = batRegex.search("The Adventures of Batwowowowoman")
# print(mo2.group())

# mo3 = batRegex.search("The Adventures of Batman")
# print(mo3 == None)

## VI. Matching Specific Repetitions with Braces
# haRegex = re.compile(r"(Ha){3}")
# mo1 = haRegex.search("HaHaHa")
# print(mo1.group())

# mo2 = haRegex.search("Ha")
# print(mo2 == None)

## VII. Greedy and Non-greedy Matching
# greedyHaRegex = re.compile(r"(Ha){3,5}")
# mo1 = greedyHaRegex.search("HaHaHaHaHa")
# print(mo1.group())

# nongreedyHaRegex = re.compile(r"(Ha){3,5}?")
# mo2 = nongreedyHaRegex.search("HaHaHaHaHa")
# print(mo2.group())

## VIII. Character Classes
#  Shorthand character class | Represents
#  \d -Any numeric digit from 0 to 9.
#  \D -Any character that is not a numeric digit from 0 to 9.
#  \w - Any letter, numeric digit, or the underscore character.(Think of this as matching “word” characters.)
#  \W -Any character that is not a letter, numeric digit, or the underscore character.
#  \s - Any space, tab, or newline character. (Think of this as matching “space” characters.)
#  \S -Any character that is not a space, tab, or newline.

# xmasRegex = re.compile(r"\d+\s\w+")
# sol = xmasRegex.findall(
#     "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"
# )
# print(sol)


## IX. Making Your Own Character Classes
# vowelRegex = re.compile(r"[aeiouAEIOU]")
# vowels = vowelRegex.findall("RoboCop eats baby food. BABY FOOD.")
# print(vowels)
# print("No. of vowels in the sentence : " + str(len(vowels)))

# consonantRegex = re.compile(r"[^aeiouAEIOU]")\
# ^ is used to negate the expression

# negateVowel = consonantRegex.findall("RoboCop eats baby food. BABY FOOD.")
# print(negateVowel)
# print("No. of consonants in the sentence : " + str(len(negateVowel)))

### X.  The Caret and Dollar Sign Characters
## i. Caret Sign- Begins with
# beginsWithHello = re.compile(r'^Hello')
# print(beginsWithHello.search('Hello, world!'))
# print(beginsWithHello.search('He said hello.'))
# print(beginsWithHello.search('He said hello.') == None)

## ii. Dollar Sign- Ends with
# endsWithNumber = re.compile(r"\d$")
# print(endsWithNumber.search("Your number is 42"))
# print(endsWithNumber.search("Your number is forty two.") == None)

# wholeStringIsNum = re.compile(r'^\d+$')
# print(wholeStringIsNum.search('1234567890'))
# print(wholeStringIsNum.search('12  34567890') == None )

### XI. The Wildcard Character
# atRegex = re.compile(r'.at')
# print(atRegex.findall('The cat in the hat sat on the flat mat.'))

## i. Matching Everything with Dot-Star
# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Aashish Last Name: Singh ')
# print(mo.group(1))
# print(mo.group(2))

# nongreedyRegex = re.compile(r'<.*?>')
# mo = nongreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())

# greedyRegex = re.compile(r'<.*>')
# mo = greedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())

## ii. Matching Newlines with the Dot Character
# noNewlineRegex = re.compile('.*')
# print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())

# newlineRegex = re.compile('.*', re.DOTALL)
# print(newlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())

############################################################################################################
# Review of Regex Symbols
#  This chapter covered a lot of notation, so here’s a quick review of what you
# learned about basic regular expression syntax:
#  •	The ? matches zero or one of the preceding group.
#  •	The * matches zero or more of the preceding group.
#  •	The + matches one or more of the preceding group.
#  •	The {n} matches exactly n of the preceding group.
#  •	The {n,} matches n or more of the preceding group.
#  •	The {,m} matches 0 to m of the preceding group.
#  •	The {n,m} matches at least n and at most m of the preceding group.
#  •	{n,m}? or *? or +? performs a non-greedy match of the preceding group.
#  •	^spam means the string must begin with spam.
#  •	spam$ means the string must end with spam.
#  •	The . matches any character, except newline characters.
#  •	\d, \w, and \s match a digit, word, or space character, respectively.
#  •	\D, \W, and \S match anything except a digit, word, or space character,
# respectively.
#  •	[abc] matches any character between the brackets (such as a, b, or c).
#  •	[^abc] matches any character that isn’t between the brackets.
############################################################################################################

## XII. Case-Insensitive Matching
# robocop = re.compile(r"robocop", re.I)
# print(robocop.search("RoboCop is part man, part machine, all cop.").group())
# print(robocop.search("ROBOCOP protects the innocent.").group())

# XIII. Substituting Strings with the sub() Method
# namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
# print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# print(agentNamesRegex.findall('Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
# print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

## XIV. Managing Complex Regexes
# phoneRegex = re.compile(
#     r"""(
#     (\d{3}|\(\d{3}\))?            # area code
#     (\s|-|\.)?                    # separator
#     \d{3}                         # first 3 digits
#     (\s|-|\.)                     # separator
#     \d{4}                         # last 4 digits
#     (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
#     )""",
#     re.VERBOSE
# )
# mo = phoneRegex.search("My number is (91) 8349154137 and 834-915-4137.")
# print(mo.group())

# # XV. Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
# someRegexValue = re.compile("foo", re.IGNORECASE | re.DOTALL | re.VERBOSE)
# print(someRegexValue.findall("Foo"))
# print(someRegexValue.findall("FOO"))
