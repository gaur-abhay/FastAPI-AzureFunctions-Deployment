import csv

from fastapi import APIRouter, HTTPException
from schemas.UserSchema import UserSchema

api_router = APIRouter()

class UserData:
    all_user = {}

    @classmethod
    async def populate_all_users(cls):
        with open("Users.csv", "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls.all_user[row["user"]] = row["password"]

@api_router.post("/register")
async def register_user(
        user: UserSchema,
):
    if user.email in UserData.all_user:
        HTTPException(status_code=400, detail="Email already registered")

    with open("User.csv", "a", newline="", encoding="utf-8") as file:
        fieldnames = ["email", "password"]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header only if the file is new
        if file.tell() == 0:
            csv_writer.writeheader()

        csv_writer.writerow({"email": user.email, "password": user.password})

    UserData.all_user[user.email] = user.password

    return {"message": "User Registered Successfully"}

@api_router.post("/login")
async def login_user(
        user: UserSchema,
):
    if user.email in UserData.all_user and UserData.all_user[user.email] == user.password:
        return {"message": "Login Successful"}
    else:
        HTTPException(status_code=400, detail="Incorrect Email or Password")


