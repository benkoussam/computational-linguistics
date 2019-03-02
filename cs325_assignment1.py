# Comp Ling - CS325 Assignment #1
# Mimi Benkoussa

import re
from nltk.book import *
import nltk
import urllib.request

# lexical diversity fn - returns the lexical diversity of a list of words
# defined as number of tokens(all words in text)/vocabulary(unique words in text)
def lexical_diversity(text):
    tokens = len(text)
    vocabulary = len(set(text))
    return(tokens/vocabulary)

# percentage use fn - returns the % use of a given word in a text
def percentage_use(word, words):
    word_count = words.count(word)
    total_words = len(words)
    return(word_count/total_words)
    
# prefix finder fn - finds all of the words that begin w/ prefix 'un'
def prefix_finder():
    wordlist = nltk.corpus.words.words("en")
    r= [word for word in wordlist if re.search("^[Uu]n", word)]
    first_25_of_r = r[:25]
    r_len = len(r)
    print("First 25 words that begin w/ prefix 'un' in the wordlist corpus:")
    print(first_25_of_r)
    print("\nTotal number of words that begin with the prefix:")
    print(r_len)

# office hour fn - extracts & prints Deepak's OH from CS325 homepage
def cs325_oh():
    url = "https://cs.brynmawr.edu/Courses/cs325/fall2018"
    page_source = urllib.request.urlopen(url).read().decode('utf-8')
    # code for removing tags
    tag = re.compile(r'<.*?>')
    cleaned_page_source = tag.sub(' ', page_source) # replaces tags w/ ' ' (space) rather than '' (none)
    # code for splitting by lines
    lines = cleaned_page_source.split('\n')
    # code for extracting office hours as a string and removing any extra \n, \t, \r, as well as extra whitespace
    office_hours = [line for line in lines if re.search("[Oo]ffice [Hh]ours:", line)]
    office_hours_string = office_hours[0]
    office_hours_string = office_hours_string.strip("[\n\t\r]['  +']")
    return office_hours_string

# weather cond fn - extracts and prints current weather conditions & temp in Philly from the NOAA's weather server
def current_weather():
    url = "https://w1.weather.gov/xml/current_obs/display.php?stid=KPHL"
    page_source = urllib.request.urlopen(url).read().decode('utf-8')
    lines = page_source.split('\n')
    # weather conditions under the "weather" tag, then extracting the string
    weather_conditions = [line for line in lines if re.search("<weather>", line)]
    wc = weather_conditions[0]
    # temperature under the "temperature_string" tag, then extracting the string
    temperature = [line for line in lines if re.search("<temperature_string>", line)]
    temp = temperature[0]
    # code for removing tags (we are doing this here rather than in the beginning b/c the tags were used to
    # search for the weather and temperature information. this is done to both weather & temp strings
    tag = re.compile(r'<.*?>')
    cleaned_wc = tag.sub(' ', wc) # replaces tags w/ ' ' (space) rather than '' (none)
    cleaned_temp = tag.sub(' ', temp)
    # code for removing any extra \n, \t, \t, as well as extra whitespace for both weather & temp strings
    cleaned_wc = cleaned_wc.strip("[\n\t\r]['  +']")
    cleaned_temp = cleaned_temp.strip("[\n\t\r]['  +']")
    print("Current weather and temperature conditions in Philadelphia are:")
    print(cleaned_wc)
    print(cleaned_temp)







    
