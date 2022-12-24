from fastapi import FastAPI, Response
from pydantic import BaseModel
from transformer import AutoModelForSeq2SeqLM



#instantiate application
app = FastAPI()

pathToModel = "./model/translateToFrench"
pipeline = AutoModelForSeq2SeqLM.from_pretrained(pathToModel)

class Body(BaseModel):
    text: str

#@: decorator that modifies this specific function
# @app.get("/")
# def index():
#     return {"message": "Hello World"}

# @app.get("/cool")
# def index1():
#     return {"message": "this is cool"}


@app.get('/')
def root():
    return Response("<h1>How to Serve AI Models with FastAPI and Docker</h1>")

@app.post('/generate')
def predict(body: Body):
    results = pipeline(body.text)
    return results[0]
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
    
    

