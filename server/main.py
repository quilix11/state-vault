from fastapi import FastAPI,Depends
from pydantic import BaseModel
from database.core import engine, Base
from database.models import ConfigBackup
from sqlalchemy.orm import Session
from database.core import get_db
from database.models import ConfigBackup

Base.metadata.create_all(bind=engine)

app = FastAPI()

class ConfigPayload(BaseModel):
    app_name: str
    config: str

@app.post("/config")
async def receive_config(payload: ConfigPayload, db: Session = Depends(get_db)):
    print(f"Recived config for app '{payload.app_name}':\n{payload.config}")
    backup=ConfigBackup(app_name=payload.app_name, content=payload.config)
    db.add(backup)
    db.commit()
    db.refresh(backup)

    return {"message": f"Config for '{payload.app_name}' received and stored with id {backup.id}."}
