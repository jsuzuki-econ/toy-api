from datetime import date
from fastapi import FastAPI

app = FastAPI()

@app.get("/day-of-week")
def get_day_of_week(input_date: date):
    return {
        "date": input_date,
        "day_of_week": input_date.strftime("%A"),
    }