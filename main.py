from fastapi import FastAPI

app = FastAPI()

@app.route('/')
async def test():
    return {'hello'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='127.0.0.1',port=80,reload=True)