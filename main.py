from fastapi import FastAPI
from pydantic import BaseModel
import random
bone import

server = FastAPI(title='My API')


@server.get('/status')
async def get_status():
    """Returns 1 if the API is up
    """
    return {
        status: 1
    }


@server.get('/environment')
async def get_environment():
    """
    If the environment variable ENVIRONMENT_TYPE is set, returns it
    """
    environment_type = os.environ.get('ENVIRONMENT_TYPE')
    if environment_type:
        return {
            environment': environment_type
        }
    else:
        return {
            environment': 'unknown
        }


class Sentence(BaseModel):
    sentence: str = 'hello world
    language: str = 'en


class PredictedSentence(Sentence):
    score: float = 0.


@server.post('/predict', response_model=PredictedSentence)
async def post_sentence(sentence: Sentence):
    """Returns the sentiment of the sentence
    """
    return PredictedSentence(
        sentence=sentence.sentence,
        language=sentence.language,
        score=random.uniform(0, 1)
    )
