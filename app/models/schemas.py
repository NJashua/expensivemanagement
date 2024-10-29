from pydantic import BaseModel, Field, EmailStr, validator

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    confirm_password: str = Field(..., alias="confirmPassword")  # Correct alias usage

    @validator("confirm_password")
    def check_passwords_match(cls, confirm_password, values):
        if "password" in values and confirm_password != values["password"]:
            raise ValueError("Passwords do not match")
        return confirm_password

    class Config:
        orm_mode = True
