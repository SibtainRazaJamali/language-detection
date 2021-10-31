#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fasttext
from iso639 import languages
import re

class LanguageIdentification:

    def __init__(self):
        pretrained_lang_model = "lid.176.bin"
        self.model = fasttext.load_model(pretrained_lang_model)

    def predict_lang(self, text):
        text = self.pre_process_text(text)
        predictions = self.model.predict(text, k=1)
        iso_code, confidence_score = predictions
        iso_code = iso_code[0].replace('__label__','')
        predicted_language = languages.get(alpha2=iso_code).name
        return predicted_language, confidence_score[0]
    
    def pre_process_text(self,text):
        text = text.replace('\n',' ')
        text = re.sub(r'[^\w\s]', '', text)
        text = ' '.join(text.split())
        text = text.encode(encoding = 'UTF-8', errors = 'strict')
        return text.decode('utf-8')
    
if __name__ == '__main__':
    LANGUAGE = LanguageIdentification()
    lang = LANGUAGE.predict_lang("benim adım sibtain")
    print(lang)
