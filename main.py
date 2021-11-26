from typing import List

from fastapi import FastAPI, Query
from schemas import Book

app = FastAPI()


@app.post('/book')
def create_book(item: Book):
    return item


@app.get('/book')
def get_book(q: List[str] = Query(["test", "test2"], descriptions="Search book", deprecated=True)):
    return q