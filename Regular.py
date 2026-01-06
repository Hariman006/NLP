import re
def detect_word_pattern(pat,txt):
    result=re.findall(pat,txt)
    if result:
        print("Word Pattern Detected")
        for i in result:
            print(i)
    else :
        print("No Word Pattern Detected")
sample_inputs=[
    (r"\bG\w+","Hey, great Gamers gather here, right? Go grab your gear, game time!"),
    (r"\b\d{4}\b","I was born in the year of 2005"),
    (r"\b[a-zA-Z]{5}\b","Hello, I am Hari,And this is Python"),
    (r"\bing\b","Gaming is a great stress buster")
]
for pat,txt in sample_inputs:
    print("Pattern :",pat)
    print("Text :",txt)
    detect_word_pattern(pat,txt)
    print("+"*40)
