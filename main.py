from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {
        'status': True,
        'message': 'Welcome to Ecommerce'
    }
