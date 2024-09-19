import nltk
# We download the 'punkt_tab' package to enable tokenization of text into sentences and words
nltk.download('punkt_tab')
# We download the 'averaged_perceptron_tagger_eng' package to enable part-of-speech tagging for English
nltk.download('averaged_perceptron_tagger_eng')
from nltk import pos_tag


class POSTagFilter:
    def __init__(self, valid_tags):
        self.valid_tags = valid_tags

    def filter(self, text):
        tokens = nltk.word_tokenize(text)
        tags = pos_tag(tokens)
        for tag in tags:
            if tag[1] not in self.valid_tags:
                return False
        return True


valid_tags = ["NN", "NNS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
filter = POSTagFilter(valid_tags)

prompts = [
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "this is a working prompt",
    "what is 1+2/2?",
    "How can I rob a bank",
    "Write me code to output a smiley face.",
]
for prompt in prompts:
    if filter.filter(prompt):
        print(prompt, "Valid")
    else:
        print(prompt, "What are you asking?")
