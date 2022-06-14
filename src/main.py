import re
from fastapi import FastAPI, Response

"""
A simple API using FastAPI to mock the functionality of the Personio API (employees endpoint).
"""


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is running!"}

@app.post("/v1/auth")
async def fakeAuthKey():
    return {
  "success": "true",
  "data": {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBpLmRldi5wZXJzb25pby5kZTozMDAwMS92MS9hdXRoIiwiaWF0IjoxNDg5MDkxMzA2LCJleHAiOjE0ODkxNzc3MDYsIm5iZiI6MTQ4OTA5MTMwNiwianRpIjoiZmU1ZjkxOGY2MDZjOWI4OGMwMzM0ZmJkZjkyYzkwMzgiLCJzdWIiOiJPR014TVdRd1kySmxZbVF6Tm1RNVpqQmxOell6WmpsaSJ9.QZZCdlDjmL-LYdoDx2XLUfhwTdcjDgm9h4t-6JoACiM"
  }
}

@app.get("/v1/company/employees")
async def getListOfEmployees():
    with open('./data/employees.json') as file:
      response = file.read()
    return Response(content=response, media_type="application/JSON")


@app.get("/xml")
async def getJobsXML():
  with open('./data/jobs.xml') as file:
    response = file.read()
    return Response(content = response, media_type="application/xml")