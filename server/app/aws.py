import os
import boto3
from pydantic import BaseModel
from fastapi import HTTPException
from typing import Optional
AWS_REGION_NAME = os.getenv("AWS_REGION_NAME")
AWS_COGNITO_APP_CLIENT_ID = os.getenv("AWS_COGNITO_APP_CLIENT_ID")
AWS_COGNITO_USER_POOL_ID = os.getenv("AWS_COGNITO_USER_POOL_ID")

class SignUpModel(BaseModel):
    username: str  
    email: str      
    password: str   
    phone_number: str  
    gender: Optional[str] = None  
    birthdate: Optional[str] = None  

class AWS_Cognito:
  def __init__(self):
    self.client = boto3.client("cognito-idp", region_name=AWS_REGION_NAME)

  def sign_up(self, user: SignUpModel):
    try:
      response = self.client.sign_up(
        ClientId=AWS_COGNITO_APP_CLIENT_ID,
        Username=user.username,
        Password=user.password,
        UserAttributes=[
          {
              'Name': 'name',
              'Value': user.username,
          },
          {
              'Name': 'email',
              'Value': user.email
          },
          {
              'Name': 'phone_number',
              'Value': user.phone_number
          },
          {
              'Name': 'gender',
              'Value': user.gender if user.gender else ""
          },
          {
              'Name': 'birthdate',
              'Value': user.birthdate if user.birthdate else ""
          }
          
        ],
      )

      return response
    except self.client.exceptions.UsernameExistsException:
          raise HTTPException(status_code=400, detail="User already exists")
    except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))
  
  
def get_aws_cognito() -> AWS_Cognito:
  return AWS_Cognito()