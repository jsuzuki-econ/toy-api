from fastapi import APIRouter, HTTPException

from app.models import Event
from app.services import events as event_service

router = APIRouter()


@router.post("/events", status_code=201)
def create_event(event: Event):
    return event_service.create_event(event)


@router.get("/events")
def get_events():
    return event_service.get_events()


@router.get("/events/{event_id}")
def get_event(event_id: int):
    event = event_service.get_event(event_id)

    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    return event