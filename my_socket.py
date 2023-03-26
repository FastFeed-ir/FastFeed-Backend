import asyncio
import json
import websockets
resturants = {}

async def resturant_server(websocket, path):
    code = path.split('/')[-1]
    if code not in resturants:
        resturants[code] = set()
        print(f"Room with code = {code} craeted successfully!")

    else: print(f"A new user added to Room{code}!")
    resturants[code].add(websocket)

    try:
        async for order in websocket:
            print(f"Received order: {order}")
            try:
                data = json.loads(order)
                for client in resturants[code]:
                    if client != websocket:
                        await client.send(json.dumps({'order': data['order']}))
                        print(f"Sended order: {order}!")
            except json.JSONDecodeError:
                print(f"Invalid order: {order}!")
    finally:
        resturants[code].remove(websocket)

async def main():
    port=3000
    async with websockets.serve(resturant_server, 'localhost', port):
        print(f"Server connected at Port {port} seccesefully!")
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
