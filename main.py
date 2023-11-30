from fastapi import FastAPI

app = FastAPI()

@app.route('/')
def test():
    return {'hahahaha'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main', host='127.0.0.1',port=80,reload=True)