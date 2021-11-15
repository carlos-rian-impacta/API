import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from fastapi import FastAPI
from view import init_app

def create_app():
    app = FastAPI(
        title="Impacta",
        version="0.1.0"
    )
    init_app(app=app)
    return app

app = create_app()