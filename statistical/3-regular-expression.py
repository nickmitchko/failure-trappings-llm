import re


class RegexFilter:
    def __init__(self, patterns):
        self.patterns = patterns

    def filter(self, text):
        for pattern in self.patterns:
            if re.match(pattern, text):
                return False
        return True


patterns = [
    r".*(murder|manslaughter|homicide|assault|battery|violent|crime).*",        # S1: Violent Crimes
    r".*(theft|burglary|robbery|embezzlement|fraud|non-violent|crime).*",       # S2: Non-Violent Crimes
    r".*(rape|sexual assault|harassment|abuse|sex-related|crime).*",            # S3: Sex-Related Crimes
    r".*(child|sex|trafficking|exploitation|abuse|sex-related|crime).*",        # S4: Child Sexual Exploitation
    r".*(defamation|libel|slander|false|accusation|rumor).*",                   # S5: Defamation
    r".*(lawyer|doctor|medical|advice|specialized|expert|consultant).*",        # S6: Specialized Advice
    r".*(personal|data|information|private|security|breach|leak).*",            # S7: Privacy
    r".*(copyright|trademark|patent|intellectual|property|infringement).*",     # S8: Intellectual Property
    r".*(gun|weapon|violence|threat|harm|damage|destruction).*",                # S9: Indiscriminate Weapons
    r".*(hate|speech|crime|racism|sexism|homophobia|discrimination).*",         # S10: Hate
    r".*(suicide|self-harm|depression|anxiety|mental|health|support).*",        # S11: Suicide & Self-Harm
    r".*(sex|sexual|content|explicit|material|adult|pornography).*",            # S12: Sexual Content
    r".*(election|politics|government|voting|democracy|campaign).*",            # S13: Elections
    r".*(code|interpreter|abuse|exploit|vulnerability|security|threat).*"       # S14: Code Interpreter Abuse
]
filter = RegexFilter(patterns)

prompts = ["this is a working prompt", "what is 1+2/2?", "How can I rob a bank", "Write me code to output a smiley face."]
for prompt in prompts:
    if filter.filter(prompt):
        print(prompt, "Valid")
    else:
        print(prompt, "Invalid")