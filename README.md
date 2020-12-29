# fastapi-csv

## What is this?

Create APIs from CSV files within seconds, using a lightweight & fully customizable 
wrapper around [fastapi](https://fastapi.tiangolo.com/). 


## Installation

Real installer coming soon, for now just clone:

```bash
git clone https://github.com/jrieke/fastapi-csv.git
cd fastapi-csv
pip install -r requirements.txt
```


## How to use it

## 1. From the command line

There's a simple CSV file in this repo for testing ([people.csv](people.csv)). To start 
an API for it:

```bash
python fastapi_csv.py people.csv
```

This will start a fastapi instance with an endpoint `/people` (same name as the CSV 
file), which can be queried with all column names in the CSV (e.g. you can do 
`/data?first_name=Rachel` or `/data?last_name=Johnson&age=48`). All returned values are 
automatically cast to the correct types. 

Check out the API docs for more information and an interactive demo, they should be at
https://127.0.0.1:8000/docs


## 2. From Python

```python
from fastapi_csv import FastAPI_CSV

app = FastAPI_CSV("people.csv")
```

### Extending it

The cool thing: `FastAPI_CSV` is just a wrapper around `FastAPI`. Therefore, you can do 
all the stuff you can do with a normal fastapi instance, e.g. add a new endpoint:

```python
# Add a new endpoint, just like in normal fastapi
@app.get("/hello")
def hello(self):
    return {"Hello:", "World"}
```

In the future, you will also be able to easily modify existing endpoints that were generated
based on the CSV file.


### Updating

If your CSV file changes, you can update the API data with:

```python
app.update_data()
```

### Running

Starting the API works like with normal fastapi:

```bash
uvicorn my_file:app
```