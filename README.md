# fastapi-csv

## What it is

Create APIs from CSV files within seconds, using a lightweight & fully customizable 
wrapper around [fastapi](https://fastapi.tiangolo.com/). 


# How to use it

### 1. From the command line

There's a simple CSV file in this repo for testing ([people.csv](people.csv)). To start 
an API for it:

```bash
python fastapi_csv.py people.csv
```

This will automatically create an endpoint `/people` (same name as the CSV file), 
which can be queried with all column names in the CSV (e.g. you can do 
`/data?first_name=Rachel` or `/data?last_name=Johnson&age=48`). All returned values are 
automatically cast to the correct types. 


### 2. From Python

```python
from fastapi_csv import FastAPI_CSV

app = FastAPI_CSV("path/to/data.csv")
```

The cool thing: `FastAPI_CSV` is just a wrapper around `FastAPI`. Therefore, you can do 
all the stuff you can do with a normal fastapi instance. E.g. to add a new endpoint, 
just do:

```python
# Add a new endpoint, just like in normal fastapi
@app.get("/hello")
def info(self):
    return {"Hello:", "World"}
```

In the future, you will also be able to easily modify existing endpoints that were generated
based on the CSV file.