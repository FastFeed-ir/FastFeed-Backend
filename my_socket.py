import asyncio
import json
import websockets
resturants = {}

async def chat_server(websocket, path):
    code = path.split('/')[-1]
    if code not in resturants:
        resturants[code] = set()
        print(f"Room with code = {code} craeted successful")

    else: print(f"A new user added to Room{code}.")
    resturants[code].add(websocket)

    try:
        async for message in websocket:
            print(f"Received message: {message}")
            try:
                data = json.loads(message)
                for client in resturants[code]:
                    if client != websocket:
                        await client.send(json.dumps({'message': data['message']}))
                        print(f"Sended message: {message}")
            except json.JSONDecodeError:
                print(f"Invalid message: {message}")
    finally:
        resturants[code].remove(websocket)

async def main():
    port=3000
    async with websockets.serve(chat_server, 'localhost', port):
        print(f"Server connected at Port {port} secceseful")
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
