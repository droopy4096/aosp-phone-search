#!/bin/env python

import sys

class colors:

    '''Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold'''
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

# print(colors.bg.green, "SKk", colors.fg.red, "Amartya")
# print(colors.bg.lightgrey, "SKk", colors.fg.red, "Amartya")



def read_words(filename):
    file_words=[]
    with open(filename,'r') as f:
        for line in f:
            # line=f.readline()
            words=line.split()
            file_words.append(words)
    return file_words

def print_lines(l1, l2, s1, s2):
    common=s1 & s2
    for w in l1:
        if w.lower() in common:
            print(colors.fg.green,w,colors.reset, sep='', end=" ")
        else:
            print(w, end=" ")
    print()
    for w in l2:
        if w.lower() in common:
            print(colors.fg.red,w,colors.reset, sep='', end=" ")
        else:
            print(w, end=" ")
    print("\n")

file1=sys.argv[1]
file2=sys.argv[2]

words1=read_words(file1)
words2=read_words(file2)
delta_limit=0.75

exact_matches=[]
matched_lines1=[]
matched_lines2=[]

# first pass
for line1 in words1:
    set1=set([l.lower() for l in line1])
    # print(set1)
    if set1 in exact_matches:
        continue
    for line2 in words2:
        set2=set([l.lower() for l in line2])
        # print(set2)
        if set2 in exact_matches:
            continue
        if set1 == set2:
            exact_matches.append(set1)
            matched_lines1.append(line1)
            matched_lines2.append(line2)
            print(colors.fg.lightgreen," ".join(line1),colors.reset, sep='')
            break
print()

# we're done with exact matches
for l in matched_lines1:
    words1.remove(l)        
for l in matched_lines2:
    words2.remove(l)        

# second pass
for line1 in words1:
    set1=set([l.lower() for l in line1])
    # print(set1)
    if set1 in exact_matches:
        continue
    for line2 in words2:
        set2=set([l.lower() for l in line2])
        # print(set2)
        if set2 in exact_matches:
            continue
        if (set1.issubset(set2)) or (set2.issubset(set1)):
            # print("1>{}\n2>{}\n\n".format(" ".join(line1), " ".join(line2)))
            print_lines(line1, line2, set1, set2)
        else:
            # print_lines(line1, line2, set1, set2)
            len1=len(set1)
            len2=len(set2)
            common=set1 & set2
            lenc=len(common)
            if (lenc/len1 >= delta_limit) or (lenc/len2 >= delta_limit):
                # print("?1>{}\n?2>{}\n\n".format(" ".join(line1), " ".join(line2)))
                print_lines(line1, line2, set1, set2)
        