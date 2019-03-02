# Comp Ling - CS325 Assignment #5
# Mimi Benkoussa

import re
import nltk

# defined grammar that accepts declarative (fact) and WH-type (query) sentences.
grammar = nltk.CFG.fromstring(
    """
    S -> NP VP F | PP VP Q | VP VP Q | VP NP Q
    NP -> N | Det N
    VP -> V | V A | V NP | V PP | V Det NP
    PP -> P
    N -> "fish" | "animal" | "bird" | "gills" | "mammals" | "animals" | "humans" | "socrates" | "human" | "deepak" | "dogs" | "collies" | "rover" | "collie" | "beagles" | "snoopy" | "birds" | "canaries" | "tweety" | "canary" | "parrots" | "polly" | "parrot" | "canines" | "hair" | "feathers"
    V -> "is" | "has" | "swims" | "swim" | "flies" | "have" | "bite" | "fly" | "are" | "walk" | "bites" | "walks" | "does"
    A -> "biped"
    P -> "who" | "what"
    Det -> "a" | "an" | "all" | "the"
    F -> "."
    Q -> "?"
    """
    )

# parser instantiation
parser = nltk.RecursiveDescentParser(grammar)

# function to tokenize the input sentence
def tokenizer(sentence):
    sentence = sentence.lower()
    tokenized = re.findall(r"[\w']+|[.,!?;]", sentence)
    return tokenized

# sample tests
s1 = "A fish is an animal."
s2 = "A bird is an animal."
s3 = "A fish has gills."
s4 = "A fish swims."
s5 = "A bird flies."
s6 = "What is a fish?"
s7 = "Is a fish an animal?" 
s8 = "Does a fish swim?"
s9 = "Does a bird have gills?"
s10 = "Does a bird fly?"

# additional tests (passing)
p1 = "Socrates is biped."
p2 = "Polly flies."
p3 = "Does Rover bite Socrates?"
# additional tests (failing)
f1 = "A fish swims?"
f2 = "Does Tweety chirp?"
f3 = "Where does a bird fly?"










