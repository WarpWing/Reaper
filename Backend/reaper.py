from typing import Optional
from fastapi import Depends, FastAPI, Request, Form, HTTPException, status, Response

app = FastAPI(root_path="/api")

@app.get('/')
def root():
    resp = '{"Response" : "Valid"}'
    return Response(content=resp, media_type="application/json")