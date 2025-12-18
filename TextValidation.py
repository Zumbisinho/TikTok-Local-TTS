import json,re

blackListedWords = []
ignorecomment = False
asciiOnly = False


with open('config.json','r',encoding='UTF-8') as File:
    content = json.load(File)
    blackListedWords = content['blacklist-words']
    asciiOnly = content['ascii-only']
    ignorecomment = content['dont-say-message-if-contains-utf-8']

def validate(text:str):
    splited = text.split()
    for word in blackListedWords:
        if word in splited:
            return False  
    if not re.fullmatch(r'^[\x00-\xFF]*$', text):
        if ignorecomment:
            return False
        else:
            return re.sub(r'[^\x00-\xFF]', '', text)
    else:
        return text

    




if __name__ == "__main__":
    print(validate('Ja bati punheta pensando no e 🕊️🕊️🕊️'))