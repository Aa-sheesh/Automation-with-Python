#! python3
# pigLatin.py - Converts text on the clipboard to Pig Latin.

vowels =("a","e","i","o","u");
import sys, pyperclip;
words = pyperclip.paste().split();
pigLatin = [];
for word in words:
    if word[0].lower() in vowels:
        pigLatin.append(word+"way");
    else:
        pigLatin.append(word[1:]+word[0]+"ay");
pyperclip.copy(" ".join(pigLatin));
print(" ".join(pigLatin));
