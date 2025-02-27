from fastapi import FastAPI, Depends
from database import engine, Base
from dotenv import load_dotenv
from aws import AWS_Cognito, get_aws_cognito, SignUpModel
from fastapi.middleware.cors import CORSMiddleware
from routers.volume_router import volumeRouter
from routers.issue_router import issueRouter

load_dotenv()
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(volumeRouter, prefix="/api")
app.include_router(issueRouter, prefix="/api")


@app.post("/sign_up")
def sign_up(user: SignUpModel, cognito: AWS_Cognito = Depends(get_aws_cognito)):
    return cognito.sign_up(user)