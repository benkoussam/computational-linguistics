# Comp Ling - CS325 Assignment #3
# Mimi Benkoussa

import re
import nltk
import sys

# nltkdict - list object
nltkdict = nltk.corpus.words.words()
# linux dictionary is in a text file/string object - get to list form as above
linuxtext = open("linuxdict.txt", "r")
linuxdict = [line.strip() for line in linuxtext.readlines()]
# do the same to google dictionary
googletext = open("googledict.txt", "r")
googledict = [line.strip() for line in googletext.readlines()]
# and the same to the text hashtags to get to list form
testhashtagstext = open("testhashtags.txt", "r")
testhashtags = [line.strip() for line in testhashtagstext.readlines()]
# hashtags and solutions
testwithanswerstext = open("testwithanswers.txt", "r")
testwithanswers = [line.strip() for line in testwithanswerstext.readlines()]
# this removes the original hashtag from testwithanswers.txt
def separate(string):
  return re.sub('^.*?,', '', string)
# list of correct segmentation strings - used below w WER
answers = [separate(hashtag) for hashtag in testwithanswers]

# maxmatch output as an list of words (strings) - based off textbook algorithm   
def maxmatch_list(hashtag, wordlist):
    if not hashtag:
        return []
    for i in range(len(hashtag)-1, -1, -1):
        first_word = (hashtag[0:i+1])
        remainder = hashtag[i+1:len(hashtag)]
        if first_word in wordlist:
            return [first_word] + maxmatch_list(remainder, wordlist)
    # if no word is found, make one-character word
    first_word = hashtag[0]
    remainder = hashtag[1:len(hashtag)]
    return [first_word] + maxmatch_list(remainder, wordlist)

# maxmatch output as a single string, for the purpose of finding WER
def maxmatch(hashtag, wordlist):
    return ' '.join(maxmatch_list(hashtag, wordlist))

# minimum edit distance algorithm - based off textbook algorithm
def min_edit_distance(src, target):
    m=len(src)+1
    n=len(target)+1
    distance_matrix = {}
    for i in range(m): distance_matrix[i,0]=i
    for j in range(n): distance_matrix[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if src[i-1] == target[j-1] else 1
            distance_matrix[i,j] = min(distance_matrix[i, j-1]+1, distance_matrix[i-1, j]+1, distance_matrix[i-1, j-1]+cost)
    return distance_matrix[i,j]

# WER algorithm - minimum edit distance / len correct segmentation string
def WER(src, target):
    min_edit_dist = min_edit_distance(src, target)
    length = len(target)
    word_error_rate = min_edit_dist/length
    return word_error_rate

# this fn prints all the hashtags, maxmatches using the three lexicons + WERs
def print_all():
    # these are used for avg WER; initialized to 0
    nltktotalWER = 0
    linuxtotalWER = 0
    googletotalWER = 0
    # concurrently going through testhashtags and the separated answers
    for hashtag, sln in zip(testhashtags, answers):
        print("Given the hashtag", hashtag)
        print("Correct segmentation string:", sln)
        print ("Maxmatch using NLTK lexicon is:", maxmatch(hashtag, nltkdict))
        print("NLTK lexicon WER:", WER(maxmatch(hashtag, nltkdict), sln))
        nltktotalWER += WER(maxmatch(hashtag, nltkdict), sln)
        print ("Maxmatch using Linux lexicon is:", maxmatch(hashtag, linuxdict))
        print("Linux lexicon WER:", WER(maxmatch(hashtag, linuxdict), sln))
        linuxtotalWER += WER(maxmatch(hashtag, linuxdict), sln)
        print ("Maxmatch using Google lexicon is:", maxmatch(hashtag, googledict))
        print("Google lexicon WER:", WER(maxmatch(hashtag, googledict), sln),"\n")
        googletotalWER += WER(maxmatch(hashtag, googledict), sln)
    # average WER for each lexicon; sum of WERs divided by length of answers
    print("NLTK avg WER:", nltktotalWER/len(answers))
    print("Linux avg WER:", linuxtotalWER/len(answers))
    print("Google avg WER:", googletotalWER/len(answers))
    return None

