import logging

from aiohttp import web


# async def listen_fondy_callbacks(request):
#     print("Create Websocket")
#
#     ws = web.WebSocketResponse()
#     await ws.prepare(request)
#
#     async for msg in ws:
#         print(msg)
#
#     print("Websocket connection closed")
#
#     return ws


async def print_call(request):
    logging.info(request)
    print(request)
    with open("log.txt", "w+") as file:
        file.write(str(request))
    return web.Response(status=200)


app = web.Application()
app.add_routes([web.get("/callback", print_call),
                web.post("/callback", print_call)
                ])
print("Start server")
web.run_app(app, port=1001)
