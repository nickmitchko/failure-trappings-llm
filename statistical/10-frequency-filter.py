class FrequencyFilter:
    def __init__(self, min_frequency, max_frequency):
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency
        self.frequencies = {}

    def filter(self, text):
        if text in self.frequencies:
            self.frequencies[text] += 1
        else:
            self.frequencies[text] = 1

        frequency = self.frequencies[text]
        if frequency < self.min_frequency or frequency > self.max_frequency:
            return False
        return True


min_frequency = 1
max_frequency = 5
filter = FrequencyFilter(min_frequency, max_frequency)

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
        print(prompt, "You're doing that too much...")
