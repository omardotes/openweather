# from fastapi import FastAPI
# from uuid import uuid4
# from .models import User
# from typing import List, Optional

# app=FastAPI()

# db: List[User] = [
#     User(
#         id = uuid4(),
#         firstName = "Omar",
#         middleName = "Pena",
#         lastName = "Exala"
#     ),
#     User(
#         id = uuid4(),
#         firstName = "Tim",
#         lastName = "Beldeniza"
#     ),
# ]

# app.get("/")
# async def root():
#     return {"hello":"world"}

# app.get("/api/fetch_users")
# def fetch_users():
#     return db



