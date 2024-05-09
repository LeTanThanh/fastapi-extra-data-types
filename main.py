from fastapi import FastAPI
from fastapi import Path
from fastapi import Body

from typing import Annotated
from uuid import UUID
from datetime import datetime
from datetime import timedelta
from datetime import time

app = FastAPI()

# Extra Data Types
@app.put("/items/{id}")
async def read_item(
  id: Annotated[UUID, Path()],
  start_datetime: Annotated[datetime, Body()],
  end_datetime: Annotated[datetime, Body()],
  process_after: Annotated[timedelta, Body()],
  repeat_at: Annotated[time, Body()]
):
  start_process = start_datetime + process_after
  duration = end_datetime - start_process

  return {
    "id": id,
    "start_datetime": start_datetime,
    "end_datetime": end_datetime,
    "process_after": process_after,
    "repeat_at": repeat_at,
    "start_process": start_process,
    "duration": duration
  }
