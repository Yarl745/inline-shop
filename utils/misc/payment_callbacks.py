from aiohttp import web


async def listen_fondy_callbacks(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        print(msg)

    print("Websocket connection closed")

    return ws