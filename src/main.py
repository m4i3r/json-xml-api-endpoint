import re
from fastapi import FastAPI, Response

"""
A simple API using FastAPI to mock the functionality of the Personio API (employees endpoint).
"""


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is running!"}

@app.get("/json")
async def getListOfEmployees():
    with open('./data/data.json') as file:
      response = file.read()
    return Response(content=response, media_type="application/JSON")


@app.get("/xml")
async def getJobsXML():
  with open('./data/data.xml') as file:
    response = file.read()
    return Response(content = response, media_type="application/xml")