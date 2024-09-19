class HITLFilter:
    def __init__(self, call_fn):
        self.call_fn = call_fn

    def filter(self, text):
        return self.call_fn(text)
    

def user_input(text):
    result = input(f"Is this a valid prompt/response?\n{text}")
    if 'y' in result:
        return True
    return False
    
# In real life, we might call to another LLM, or even to a support agent :)
filter = HITLFilter(call_fn=user_input)

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