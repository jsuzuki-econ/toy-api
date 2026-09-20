from datetime import date
from datetime import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/day-of-week")
def get_day_of_week(input_date: date):
    return {
        "date": input_date,
        "day_of_week": input_date.strftime("%A"),
    }

@app.get("/days-between")
def get_days_between(start_date: date, end_date: date,):
    delta = end_date - start_date
    return {
        "start_date": start_date,
        "end_date": end_date,
        "days_between": delta.days,
    }
