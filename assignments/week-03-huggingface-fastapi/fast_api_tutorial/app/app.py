from fastapi import FastAPI, Response, Query
from pydantic import BaseModel
from transformers import pipeline
from typing import List



#instantiate application
app = FastAPI()

pathToModelFR = "./model/translateToFrench"
pathToModelDE = "./model/translateToGerman"
pipelineFR = pipeline(task = "translation_en_to_fr", model=pathToModelFR)
pipelineDE = pipeline(task = "translation_en_to_de", model=pathToModelDE)

class TextToTranslate(BaseModel):
    input_text: str
    
class TextsToTranslate(BaseModel):
    input_texts: List[str]

#@: decorator that modifies this specific function
@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/cool")
def index1():
    return {"message": "this is cool"}

@app.post("/echo") 
def echo(message: str):
    return {"message": message}



@app.post('/simpletranslate/{text_to_translate}')
def predict(text_to_translate: str):
    results = pipelineFR(text_to_translate)
    return results

@app.post('/translate/')
def predict(text_to_translate: TextToTranslate):
    results = pipelineFR(text_to_translate.input_text)
    return results

@app.post('/translatemultiple/')
def predict(texts_to_translate: TextsToTranslate):
    results = []
    texts =  texts_to_translate.input_texts
    for text in texts:
        results.append(pipelineDE(text))
    return results

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
    
    

