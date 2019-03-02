# Comp Ling - CS325 Assignment #2
# Mimi Benkoussa
# Resources used: NLTK Book
import re
import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize, word_tokenize

# smaller, sample texts I used to test (small portion of Austen and my own)
txt = '[Emma by Jane Austen 1816]\n\nVOLUME I\n\nCHAPTER I\n\n\nEmma Woodhouse, handsome, clever, and rich, with a comfortable home\nand happy disposition, seemed to unite some of the best blessings\nof existence; and had lived nearly twenty-one years in the world\nwith very little to distress or vex her.\n\nShe was the youngest of the two daughters of a most affectionate,\nindulgent father; and had, in consequence of her sister\'s marriage,\nbeen mistress of his house from a very early period.  Her mother\nhad died too long ago for her to have more than an indistinct\nremembrance of her caresses; and her place had been supplied\nby an excellent woman as governess, who had fallen little short\nof a mother in affection.\n\nSixteen years had Miss Taylor been in Mr. Woodhouse\'s family,\nless as a governess than a friend, very fond of both daughters,\nbut particularly of Emma.  Between _them_ it was more the intimacy\nof sisters.  Even before Miss Taylor had ceased to hold the nominal\noffice of governess, the mildness of her temper had hardly allowed\nher to impose any restraint; and the shadow of authority being\nnow long passed away, they had been living together as friend and\nfriend very mutually attached, and Emma doing just what she liked;\nhighly esteeming Miss Taylor\'s judgment, but directed chiefly by\nher own.\n\nThe real evils, indeed, of Emma\'s situation were the power of having\nrather too much her own way, and a disposition to think a little\ntoo well of herself; these were the disadvantages which threatened\nalloy to her many enjoyments.  The danger, however, was at present\nso unperceived, that they did not by any means rank as misfortunes\nwith her.\n\nSorrow came--a gentle sorrow--but not at all in the shape of any\ndisagreeable consciousness.--Miss Taylor married.  It was Miss\nTaylor\'s loss which first brought grief.  It was on the wedding-day\nof this beloved friend that Emma first sat in mournful thought\nof any continuance.  The wedding over, and the bride-people gone,\nher father and herself were left to dine together, with no prospect\nof a third to cheer a long evening.  Her father composed himself\nto sleep after dinner, as usual, and she had then only to sit\nand think of what she had lost.\n\nThe event had every promise of happiness for her friend.  Mr. Weston\nwas a man of unexceptionable character, easy fortune, suitable age,\nand pleasant manners; and there was some satisfaction in considering\nwith what self-denying, generous friendship she had always wished\nand promoted the match; but it was a black morning\'s work for her.\nThe want of Miss Taylor would be felt every hour of every day.\n--"Very little white satin, very few\nlace veils; a most pitiful business!--Selina would stare when she\nheard of it."--But, in spite of these deficiencies, the wishes,\nthe hopes, the confidence, the predictions of the small band\nof true friends who witnessed the ceremony, were fully answered\nin the perfect happiness of the union.\n\n\nFINIS\n'
txt2 = '[Hello world. Hello world.]'

# gutenberg texts I used (input these into my code below)
austen_raw = nltk.corpus.gutenberg.raw('austen-emma.txt')
milton_raw = nltk.corpus.gutenberg.raw('milton-paradise.txt')

''' MY CODE BELOW '''
# separating the contents of a text into sentences
def segmentation(text):
    no_linebreaks = re.sub('(\n)+', ' ', text) # removes all linebreaks from text
    no_sentenceboundaries = re.sub('[!:?.]', '\n', no_linebreaks) # splits text using sentence boundaries
    no_dashes = re.sub('-', ' ', no_sentenceboundaries) # replaces all occurences of '-' with a space
    no_punctuation = re.sub('[,;"]', '', no_dashes) # removes various punctuations',' , ';' , '"'
    no_apostrophe = re.sub("'", '', no_punctuation) # removes ''' (single quote/apostrophe)
    segmented = (no_apostrophe.split('\n')) # splits via newline
    cleaned = [line.strip() for line in segmented] # removing extra whitespace between the strings (leading or trailing)
    finaltext = [w.lower() for w in cleaned] #finally, making all of the words lowercase
    return(finaltext)

# counting the number of sentences in the text
def segment_count(text):
    segmented_text = segmentation(text) # calling segmentation fn and counting length of its output
    return(len(segmented_text))

# separating the contents of a text into words, ie tokens
def tokenization(text):
    no_apostrophe = re.sub("'", '', text) # first, removing apostrophes since they will otherwise split word tokenization into 2
    words = re.findall(r'\w+', no_apostrophe) # finding all words
    tokens = [word.lower() for word in words] # lowercasing all words (text normalization)
    return(tokens)

# counting the number of UNIQUE words in the text, ie vocabulary
def vocabulary(text):
    tokenized_text = tokenization(text) # calling tokenization fn and using the length of the set of tokens to get vocabulary
    return(len(set(tokenized_text)))

# compute the average word length of a sentence
def avg_wl(text):
    token_count = len(tokenization(text)) # number of tokens, NOT vocabulary, this will be used
    sentence_count = segment_count(text) # calling the fn that counts # of sentences
    average_wl = token_count/sentence_count
    return(average_wl)

''' FNS THAT USE PRE-SEGMENTED NLTK OUTPUTS BELOW '''
# in any of the four functions below, input either
austen = "austen-emma.txt"
milton = "milton-paradise.txt"

# NLTK list of sentences
def nltk_sents(text):
    return gutenberg.sents(text)

# NLTK list of words
def nltk_words(text):
    return gutenberg.words(text)

''' FNS THAT USE BUILT-IN NLTK SEGMENTATION FNS BELOW '''
# NLTK list of sentences method
def tokenized_sents(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

# NLTK list of words method
def tokenized_words(text):
    wrds = nltk.word_tokenize(text)
    return wrds
