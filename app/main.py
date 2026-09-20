from datetime import date

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/day-of-week")
def get_day_of_week(input_date: date):
    return {
        "date": input_date,
        "day_of_week": input_date.strftime("%A"),
    }


@app.get("/days-between")
def get_days_between(
    start_date: date,
    end_date: date,
):

    if end_date < start_date:
        raise HTTPException(
            status_code=400,
            detail="end_date must be on or after start_date",
        )

    delta = end_date - start_date
    return {
        "start_date": start_date,
        "end_date": end_date,
        "days_between": delta.days,
    }
