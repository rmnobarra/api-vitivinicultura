from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.auth.auth import authenticate_user, create_access_token, Token

router = APIRouter()

@router.post("/login", response_model=Token, tags=["Autenticação"])
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    token = create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)
    return {"access_token": token, "token_type": "bearer"}
