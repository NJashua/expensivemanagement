from pydantic import BaseModel, Field, EmailStr, validator

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    confirmPassword: str = Field(..., alias="confirmPassword")

    @validator("confirmPassword")
    def check_passwords_match(cls, confirmPassword, values):
        if "password" in values and confirmPassword != values["password"]:
            raise ValueError("Passwords do not match")
        return confirmPassword

    class Config:
        orm_mode = True
