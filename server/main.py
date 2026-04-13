import fastapi
from pydantic import BaseModel

app = fastapi.FastAPI()

class ConfigPayload(BaseModel):
    app_name: str
    config: str

@app.post("/config")
async def receive_config(payload: ConfigPayload):
    print(f"Recived config for app '{payload.app_name}':\n{payload.config}")
    return {"message": f"Config for '{payload.app_name}' received successfully."}
