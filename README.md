# Setup for TrashTrek API

## Requirements
- Python 3.8 or above
- venv (or any python environment
- Access to a mongodb database (local or atlas)

## Installation

- Create a new virtual enviroment. When using venv, run `python -m venv .venv`
- Activate the enviroment:
  - Linux / MacOS: `source .venv/bin/activate`
  - Windows: `.venv/Scripts/activate`
- Install the required dependencies by running `pip install -r requirements.txt`
- Set up the environment variables by creating a `.env` file in the root directory and adding the following variables:
    - `MONGO_URL`: The URL of your MongoDB instance. You may use the default value `mongodb://localhost:27017` if you are using MongoDB locally.

## Running the API

- Run the API by running `fastapi run main.py` or `fastapi dev main.py` for autoreloading of server
