events = []


def create_event(event):
    new_event = {
        "id": len(events) + 1,
        "name": event.name,
        "event_date": event.event_date,
    }

    events.append(new_event)
    return new_event


def get_events():
    return events


def get_event(event_id):
    for event in events:
        if event["id"] == event_id:
            return event

    return None