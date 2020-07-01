'''
foobar:~/ abhishek252167$ cd braille-translation
foobar:~/braille-translation abhishek252167$ ls
Solution.java
constraints.txt
readme.txt
solution.py
foobar:~/braille-translation abhishek252167$ cat readme.txt
Braille Translation
===================

Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions. But she never bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating her space station. You figure printing out Braille signs will help them, and - since you'll be promoting efficiency at the same time - increase your chances of a promotion. 

Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2x3 grid, where each dot can either be a bump or be flat (no bump). You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda's command can feel the bumps on the signs and ""read"" the text with their touch. The special printer which can print the bumps onto the signs expects the dots in the following order:
1 4
2 5
3 6

So given the plain text word ""code"", you get the Braille dots:

11 10 11 10
00 01 01 01
00 10 00 00

where 1 represents a bump and 0 represents no bump.  Put together, ""code"" becomes the output string ""100100101010100110100010"".

Write a function solution(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution("code")
Output:
    100100101010100110100010

Input:
solution.solution("Braille")
Output:
    000001110000111010100000010100111000111000100010

Input:
solution.solution("The quick brown fox jumps over the lazy dog")
Output:
    000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110

-- Java cases --
Input:
Solution.solution("code")
Output:
    100100101010100110100010

Input:
Solution.solution("Braille")
Output:
    000001110000111010100000010100111000111000100010

Input:
Solution.solution("The quick brown fox jumps over the lazy dog")
Output:
    000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.



foobar:~/braille-translation abhishek252167$ cat constraints.txt
Java
====
Your code will be compiled using standard Java 8. All tests will be run by calling the solution() method inside the Solution class

Execution time is limited.

Wildcard imports and some specific classes are restricted (e.g. java.lang.ClassLoader). You will receive an error when you verify your solution if you have used a blacklisted class.

Third-party libraries, input/output operations, spawning threads or processes and changes to the execution environment are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.

Python
======
Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Input/output operations are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.
'''

charToBraile = {}
chars = 'abcdefghijklmnopqrstuvwxyz'
chars += chars.upper()
braile = '100000110000100100100110100010110100110110110010010100010110101000111000101100101110101010111100111110111010011100011110101001111001010111101101101111101011'
braile += braile
b = 0
for c in chars:
    charToBraile[c] = braile[b:b+6]
    b += 6
charToBraile[' '] = '000000'
def solution(s):
    b = ''
    for c in s:
        if c.isupper():
            b += '000001'
        b += charToBraile[c]
    return b