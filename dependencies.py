import os
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, Request, status
import secrets

load_dotenv()

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


def check_credentials(username: str, password: str) -> bool:
    if not ADMIN_USERNAME or not ADMIN_PASSWORD:
        return False
    correct_user = secrets.compare_digest(username, ADMIN_USERNAME)
    correct_pass = secrets.compare_digest(password, ADMIN_PASSWORD)
    return correct_user and correct_pass

def require_login(request: Request) -> str:
    user = request.session.get("user")
    if not user:
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            headers={"Location": "/login"},
        )
    return user
