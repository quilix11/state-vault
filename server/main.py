import fastapi
from pydantic import BaseModel
from database.core import engine, Base
from database.models import ConfigBackup

Base.metadata.create_all(bind=engine)

app = fastapi.FastAPI()

class ConfigPayload(BaseModel):
    app_name: str
    config: str

@app.post("/config")
async def receive_config(payload: ConfigPayload):
    print(f"Recived config for app '{payload.app_name}':\n{payload.config}")
    return {"message": f"Config for '{payload.app_name}' received successfully."}
