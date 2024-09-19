from flask import Flask
from pydantic import BaseModel
from flask_pydantic import validate

class Query(BaseModel):
    name:str
    age:int

app = Flask(__name__)

@app.route("/intro")
@validate()
def intro(query:Query):
    return "Hello, my name is {} and I am {} years old".format(query.name,query.age)