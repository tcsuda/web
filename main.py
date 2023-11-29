from fastapi import FastAPI

app = FastAPI()

@app.route('/')
def test():
    return {'hahahaha'}