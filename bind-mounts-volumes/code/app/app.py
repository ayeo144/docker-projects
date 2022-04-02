import datetime
from pathlib import Path
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


LOG_DIR = Path(Path(__file__).parent.parent, "logs")
LOG_DIR.mkdir(parents=False, exist_ok=True)
LOG = Path(LOG_DIR, "log.log")


class Entry(BaseModel):
    text: Optional[str] = None


app = FastAPI()


@app.post("/entry/")
def add_text_entry(entry: Entry):
    with open(LOG, "a") as file:
        tstamp = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        file.write(f"{tstamp} - {entry.text}")
    return entry