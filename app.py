from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
import math

# Create FastAPI app
app = FastAPI(title="Math API", description="A large FastAPI app for math calculations", version="1.0")

# Input model for POST requests
class MathInput(BaseModel):
    a: Union[float, str] = None
    b: Union[float, str] = None

# Helper function: convert string/number to float
def to_number(x: Union[str, float, int, None]) -> float:
    if x is None:
        return None
    try:
        return float(x)
    except ValueError:
        raise ValueError(f"Invalid number: {x}")

# -----------------------
# 🔹 Basic Math Operations
# -----------------------

@app.post("/add")
def add(data: MathInput):
    a, b = to_number(data.a), to_number(data.b)
    return {"operation": "addition", "a": a, "b": b, "result": a + b}

@app.post("/subtract")
def subtract(data: MathInput):
    a, b = to_number(data.a), to_number(data.b)
    return {"operation": "subtraction", "a": a, "b": b, "result": a - b}

@app.post("/multiply")
def multiply(data: MathInput):
    a, b = to_number(data.a), to_number(data.b)
    return {"operation": "multiplication", "a": a, "b": b, "result": a * b}

@app.post("/divide")
def divide(data: MathInput):
    a, b = to_number(data.a), to_number(data.b)
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"operation": "division", "a": a, "b": b, "result": a / b}

@app.post("/power")
def power(data: MathInput):
    a, b = to_number(data.a), to_number(data.b)
    return {"operation": "power", "a": a, "b": b, "result": a ** b}

# -----------------------
# 🔹 Single-Input Functions
# -----------------------

@app.get("/sqrt/{x}")
def sqrt(x: Union[str, float, int]):
    x = to_number(x)
    if x < 0:
        return {"error": "Square root of negative number is not real"}
    return {"operation": "square_root", "x": x, "result": math.sqrt(x)}

@app.get("/factorial/{x}")
def factorial(x: Union[str, int]):
    x = int(to_number(x))
    if x < 0:
        return {"error": "Factorial of negative number is not defined"}
    return {"operation": "factorial", "x": x, "result": math.factorial(x)}

@app.get("/log/{x}")
def log(x: Union[str, float]):
    x = to_number(x)
    if x <= 0:
        return {"error": "Logarithm of non-positive numbers is not defined"}
    return {"operation": "log", "x": x, "result": math.log(x)}

# -----------------------
# 🔹 Trigonometric Functions
# -----------------------

@app.get("/sin/{x}")
def sine(x: Union[str, float]):
    x = to_number(x)
    return {"operation": "sine", "x": x, "result": math.sin(math.radians(x))}

@app.get("/cos/{x}")
def cosine(x: Union[str, float]):
    x = to_number(x)
    return {"operation": "cosine", "x": x, "result": math.cos(math.radians(x))}

@app.get("/tan/{x}")
def tangent(x: Union[str, float]):
    x = to_number(x)
    return {"operation": "tangent", "x": x, "result": math.tan(math.radians(x))}

