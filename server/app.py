from fastapi import FastAPI,Depends, HTTPException
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

@app.post("/push")
async def push_config(payload: ConfigPayload, db: Session = Depends(get_db)):
    print(f"Recived config for app '{payload.app_name}':\n{payload.config}")
    backup=ConfigBackup(app_name=payload.app_name, content=payload.config)
    db.add(backup)
    db.commit()
    db.refresh(backup)

    return {"message": f"Config for '{payload.app_name}' received and stored with id {backup.id}."}

@app.get("/pull/{config_name}")
async def pull_config(config_name: str, db: Session = Depends(get_db)):
    config = db.query(ConfigBackup).filter(ConfigBackup.config_name == config_name).order_by(ConfigBackup.id.desc()).first()
    
    if not config:
        raise HTTPException(status_code=404, detail=f"Config '{config_name}' not found")
    
    return {"config_name": config.config_name, "content": config.content}



