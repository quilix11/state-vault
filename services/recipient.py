import httpx

DEF_URL = "http://127.0.0.1:8000/pull"

async def get_config(config_name):
    url = f"{DEF_URL}/{config_name}"
    async with httpx.AsyncClient() as cl:
        try:
            response = await cl.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except httpx.ConnectError:
                return "error"