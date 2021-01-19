from server import app
from fastapi import Depends, HTTPException, Request, Response
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from server.models.userModel import User, LoginModel, RegistrationModel
from server.db import session
from passlib.hash import bcrypt
from server.config import JWT_SECRET
from server.routes.verify import verify
import jwt

@app.post('/api/user/login')
def login(user: LoginModel):
    if not user.email:
        raise HTTPException(status_code=401, detail="Missing email or password!")

    email = session.query(User).filter(User.email == user.email).first()
    if not email:
        raise HTTPException(status_code=401, detail="User does not exist!")

    try:
        if bcrypt.verify(user.password, email.password):
            token = jwt.encode({'id': email.id}, JWT_SECRET)
            response = JSONResponse(content=token)
            response.set_cookie(key='token', value=token, httponly=True)
            return response
        else:
            raise HTTPException(status_code=401, detail="Password was incorrect!")
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Something went wrong!")

@app.post('/api/user/register')
def register(user: RegistrationModel):
    if not user.name:
        raise HTTPException(status_code=401, detail="Name was not provided!")
    if not user.email:
        raise HTTPException(status_code=401, detail="Email was not provided!")
    if not user.password:
        raise HTTPException(status_code=401, detail="Password was not provided!")   

    if len(user.email) > 100 or len(user.name) > 100:
        raise HTTPException(status_code=401, detail="Max character limit exceeded!") 

    email = session.query(User).filter(User.email == user.email).first()
    if email:
        raise HTTPException(status_code=401, detail="Email is already in use!")

    hashedPassword = bcrypt.hash(user.password)

    try:
        newUser = User(user.name, user.email, bcrypt.hash(user.password))
        session.add(newUser)
        session.commit()
        session.close()
        return newUser
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Something went wrong!")

@app.post('/api/user/logout')
def logout(response: Response):
    response.delete_cookie('token')
    return {"detail": "Logged Out"}

@app.get('/api/user/isLoggedIn')
def isLoggedIn(user: str = Depends(verify)):
    return {"detail": user}

