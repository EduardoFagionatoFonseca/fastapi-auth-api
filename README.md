# Auth App API

A simple authentication API built with FastAPI and SQLite to practice CRUD operations and user authentication workflows.

## Features

* User registration
* Retrieve users
* User login (authentication)
* RESTful API structure

## Tech Stack

* Python
* FastAPI
* SQLite
* Uvicorn
* Postman (for testing)

## Installation

Clone the repository:
git clone https://github.com/EduardoFagionatoFonseca/auth-app-api.git

Navigate into the project folder:
cd auth-app-api

Create a virtual environment:
python -m venv venv

Activate the virtual environment:

* Windows: venv\Scripts\activate
* Linux/Mac: source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

## Running the Application

Start the server:
uvicorn app.main:app --reload

The API will be available at:
http://127.0.0.1:8000

Interactive API docs (Swagger UI):
http://127.0.0.1:8000/docs

## Usage

You can test the endpoints using:

* Browser (for GET requests)
* Postman or Insomnia (recommended)

Available routes include:

* Create user
* Get users
* Login

## Project Structure

app/
├── main.py
├── routes/
├── models/
├── database/

## Future Improvements

* Password hashing
* JWT authentication
* User roles and permissions
* Input validation improvements
* Unit tests

## Purpose

This project was built for learning purposes, focusing on backend development, API design, and CRUD operations using FastAPI.
