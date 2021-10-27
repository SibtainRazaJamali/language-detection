from fastapi import FastAPI
from pydantic import BaseModel
from language_detector import LanguageIdentification

class InputText(BaseModel):
    sentence: str


app = FastAPI()
LANGUAGE_DETECTOR = LanguageIdentification()


@app.post("/detect/")
async def detect(text: InputText):
    input_text = text.sentence
    predicted_language, confidence = LANGUAGE_DETECTOR.predict_lang(input_text)
    return predicted_language, confidence
