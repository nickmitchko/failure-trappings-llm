import re


class Filter:
    def __init__(self, rules):
        self.rules = rules

    def filter(self, text):
        for rule in self.rules:
            if not rule(text):
                return False
        return True


def contains_keyword(text):
    keywords = ["this"]
    for keyword in keywords:
        if keyword not in text:
            return False
    return True

def has_valid_syntax(text):
    def is_word(char):
        return re.match('^[a-zA-Z "]$', char) is not None

    for char in text:
        if not is_word(char):
            return False
    return True

def has_only_words(text):
    return has_valid_syntax(text)
    

# Define rules
rules = [contains_keyword, has_valid_syntax]

# Create filter
filter = Filter(rules)

# Test filter
prompts = ["this is a working prompt", "what is 1+2/2?"]
for prompt in prompts:
    if filter.filter(prompt):
        print(prompt, "Valid")
    else:
        print(prompt, "Invalid")
