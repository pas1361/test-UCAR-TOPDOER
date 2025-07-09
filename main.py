from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse
import sqlite3
from datetime import datetime

app = FastAPI()
positive = ['хорош', 'люблю', 'отличн', 'нравит', 'довол', 'понравил', 'радует', 'класс', 'супер']
negative = ['плохо', 'ненавиж', 'ужас', 'огорч', 'отстой', 'разочаров', 'не нрав', 'не понравил', 'не довол', 'не радует']

with sqlite3.connect("reviews.db") as conn:
    conn.execute('''CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        sentiment TEXT NOT NULL,
        created_at TEXT NOT NULL)''')
    conn.commit()

@app.post("/reviews")
async def add_review(request: Request):
    text = (await request.json()).get("text")
    if not text:
        return JSONResponse(status_code=400, content={"error": "Missing 'text'"})
    sentiment = (
        'negative' if any(w in text.lower() for w in negative)
        else 'positive' if any(w in text.lower() for w in positive)
        else 'neutral'
    )
    created_at = datetime.utcnow().isoformat()

    with sqlite3.connect("reviews.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO reviews (text, sentiment, created_at) VALUES (?, ?, ?)",
                    (text, sentiment, created_at))
        review_id = cur.lastrowid
        conn.commit()

    return {"id": review_id, "text": text, "sentiment": sentiment, "created_at": created_at}

@app.get("/reviews")
def get_reviews(sentiment: str = Query(None)):
    with sqlite3.connect("reviews.db") as conn:
        cur = conn.cursor()
        if sentiment:
            cur.execute("SELECT * FROM reviews WHERE sentiment = ?", (sentiment,))
        else:
            cur.execute("SELECT * FROM reviews")
        rows = cur.fetchall()
        return [{"id": r[0], "text": r[1], "sentiment": r[2], "created_at": r[3]} for r in rows]
