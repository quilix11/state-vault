import httpx
import asyncio
from services.scanner import find_config, read_config


async def send_config(app_name: str, config: str):
    url = "http://127.0.0.1:8000/push"
    payload = {
        "app_name": app_name,
        "config": config
    }
    async with httpx.AsyncClient() as cl:
        response = await cl.post(url, json=payload)
        if response.status_code == 200:
            return
        else:
            print(f"Failed to send config for '{app_name}'. Status code: {response.status_code}, Response: {response.text}")
        return response.json()
    

if __name__ == "__main__":
    path = find_config('zshrc')
    if path:
        content = read_config(path)
        asyncio.run(send_config("zshrc", content))


