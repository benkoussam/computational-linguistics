# Comp Ling - CS325 Assignment #4
# Mimi Benkoussa

import nltk
from nltk.corpus import brown
import urllib.request

''' BROWN CORPUS '''
# splitting Brown news corpus by sentences
sents = brown.sents(categories="news")
# tagging using universal tagset
tagged_sents = brown.tagged_sents(categories="news", tagset="universal")
# splitting Brown news corpus by words
words = brown.words(categories="news")
# tagging using universal tagset
tagged_words = brown.tagged_words(categories="news", tagset="universal")

''' FUNCTIONS '''
# top most frequent tags & parts of speech
def freq():
    # 8 most frequent tags
    print("8 most frequent tags:")
    tag_freq = nltk.FreqDist()
    for(word, tag) in tagged_words:
      tag_freq[tag] += 1
    print(tag_freq.most_common()[:15],"\n")
    # 15 most frequent nouns
    print("15 most frequent nouns:")
    noun_freq = nltk.FreqDist()
    for (word, tag) in tagged_words:
        if tag == 'NOUN':
            noun_freq[word] += 1
    print(noun_freq.most_common()[:15],"\n")
    # 15 most frequent verbs
    print("15 most frequent verbs:")
    verb_freq = nltk.FreqDist()
    for (word, tag) in tagged_words:
        if tag == 'VERB':
            verb_freq[word] += 1
    print(verb_freq.most_common()[:15],"\n")
    # 15 most frequent adjectives
    print("15 most frequent adjectives:")
    adj_freq = nltk.FreqDist()
    for (word, tag) in tagged_words:
        if tag == 'ADJ':
            adj_freq[word] += 1
    print(adj_freq.most_common()[:15],"\n")
    # 15 most frequent adverbs
    print("15 most frequent adverbs:")
    adv_freq = nltk.FreqDist()
    for (word, tag) in tagged_words:
        if tag == 'ADV':
            adv_freq[word] += 1
    print(adv_freq.most_common()[:15],"\n")
    return None

# tokenized text tagger
def tagger(text):
    # using the nltk tokenizer to tokenize the text
    words = nltk.word_tokenize(text)
    # defining patterns for various pos (* = catered to test texts)
    pos_patterns = [
        (r'[\.,:;\'"?!]', '.'),             # punctuation
        (r'^-?[0-9]+(.[0-9]+)?$', 'NUM'),   # cardinal numbers
        (r'.*ing$', 'VERB'),                # gerunds
        (r'.*ed$', 'VERB'),                 # simple past
        (r'.*es$', 'VERB'),                 # 3rd singular present
        (r'.*ould$', 'VERB'),               # modals
        (r'(Is|is|Are|are|Have|have)$', 'VERB'),    # verb*
        (r'.*\'s$', 'NOUN'),                # possesive nouns
        (r'.*s$', 'NOUN'),                  # plural nouns
        (r'.*ness$', 'NOUN'),               # nouns from adjectives
        # singular pronouns
        (r'(I|Me|me|Mine|mine|Myself|myself|You|you|Yours|yours|Yourself|yourself|It|it|He|he|She|she|His|his|Hers|hers|Himself|himself|Herself|herself|Itself|itself)$', 'PRON'),
        # plural pronouns
        (r'(We|we|Us|us|Ours|ours|Ourselves|ourselves|Yourselves|yourselves|They|they|Them|them|Themselves|themselves|Theirs|theirs)$', 'PRON'),
        (r'(The|the|A|a|An|an)$', 'DET'),   # articles
        # articles
        (r'(At|at|On|on|Out|out|Over|over|Per|per|That|that|Up|up|Down|down)$', 'PRT'),
        (r'.*able$', 'ADJ'),                # adjectives
        (r'.*er$', 'ADJ'),                  # adjectives
        (r'.*st$', 'ADJ'),                  # adjectives
        (r'.*ly$', 'ADV'),                  # adverbs
        # conjunctions
        (r'(For|for|And|and|But|but|Nor|nor|Or|or|Yet|yet|So|so)$', 'CONJ'), 
        (r'.*', 'NOUN')                     # nouns (default)
    ]
    tagger = nltk.RegexpTagger(pos_patterns)
    return tagger.tag(words)
    

''' TEST TEXTS '''
# test 1 (Deepak)
url1 = "https://cs.brynmawr.edu/Courses/cs325/fall2018/Test.txt"
page_source1 = urllib.request.urlopen(url1).read().decode('utf-8')
test1 = page_source1.strip("[\n\t\r]['  +']")
# test 2 (Deepak)
url2 = "https://cs.brynmawr.edu/Courses/cs325/fall2018/test2.txt"
page_source2 = urllib.request.urlopen(url2).read().decode('utf-8')
test2 = page_source2.replace("\r\n","")
# test 3 (me) - exerpt from classic story called 'The Necklace'
test3 = "She was sad. She suffered endlessly, feeling herself born for every delicacy and luxury. She suffered from the poorness of her house, from its mean walls, worn chairs, and ugly curtains. All these things, of which other women of her class would not even have been aware, tormented and insulted her."
# test 4 (me) - exerpt from Aesop called 'Timidity'
test4 = "One day, a group of rabbits came to the conclusion that as their fearness would never leave them, they were doomed to a miserable existence and it would be better to drown themselves and end their misery once and for all. Accordingly, they began to move towards a large lake. When the frogs in the lake saw the large number of rabbits approaching, they were filled with fear and made for the deepest part of the lake. Seeing this, the rabbits realized they were not the most timid animals."

