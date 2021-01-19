from fastapi import Request, HTTPException
from server.config import JWT_SECRET
from server.db import session
from server.models.userModel import User
import jwt

def verify(request: Request):
    token = request.cookies.get('token')
    if not token: 
        raise HTTPException(status_code=401, detail="User is not logged in!")
    try:
        decodedToken = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        currentUser = session.query(User).get(decodedToken['id'])
        return decodedToken
    except Exception as error:
        print(error)
        raise HTTPException(status_code=401, detail="User token is invalid!")
