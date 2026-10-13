from fastapi import FastAPI, HTTPException
from Exceptions.UserNotFoundError import UserNotFoundError

app = FastAPI()

@app.get("/")
async def get_root():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {
        "application": "Employee Management",
        "framework": "FastAPI",
        "language": "Python"
    }

@app.post("/employees")
def create_employee(employee: dict):
    # Here you would typically add logic to save the employee to a database
    return HTTPException(
        status_code = 201, detail="Employee created successfully"
    )

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise UserNotFoundError(user_id)

    return {"id": 1, "name": "Ravi"}

@app.post("/users/create")
def create_user(user: dict):
    # Here you would typically add logic to save the user to a database
    return HTTPException(
        status_code=409, detail="user already exists"
    )

@app.post("/users/update")
def update_user(user: dict):
    # Here you would typically add logic to update the user in a database
    return HTTPException(
        status_code=200, detail="user updated successfully"
    )

@app.patch("/users/patch")
def patch_user(user: dict):
    # Here you would typically add logic to patch the user in a database
    return HTTPException(
        status_code=200, detail="user patched successfully"
    )