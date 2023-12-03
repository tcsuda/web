from fastapi import FastAPI

app = FastAPI()

@app.get('/{name}')
async def test(name):
    return {'hello': name}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='127.0.0.1',port=80,reload=True)