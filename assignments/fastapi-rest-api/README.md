# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Learn to design and implement a simple REST API using the FastAPI framework in Python. Students will create endpoints, handle requests, and return JSON responses.

## 📝 Tasks

### 🛠️ Create basic endpoints

#### Description
Set up a FastAPI application with multiple routes that return static data or echo parameters.

#### Requirements
Completed project should:

- Initialize a FastAPI app in `main.py`.
- Implement a `GET /` endpoint that returns a welcome message.
- Implement a `GET /items/{item_id}` endpoint that returns the `item_id` and a hard‑coded description.
- Implement a `POST /items` endpoint that accepts JSON with `name` and `price` and returns the created item with an `id`.

### 🛠️ Add validation and documentation

#### Description
Enhance the API using Pydantic models for request and response validation and explore the automatic docs.

#### Requirements
Completed project should:

- Define a Pydantic model `Item` with `name: str` and `price: float`.
- Use the model for the POST body and response.
- Verify interactive docs are available at `/docs`.

```
