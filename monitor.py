import asyncio
import websockets
import json
from datetime import datetime

async def monitor_commune():
    uri = "ws://127.0.0.1:3030/stream"
    print(f"[*] Connecting to Commune Stream at {uri}...")
    
    try:
        async with websockets.connect(uri) as websocket:
            print("[+] Connection Established. Listening for pulses...\n")
            while True:
                # Wait for a new message from the Rust daemon
                message = await websocket.recv()
                data = json.loads(message)
                
                # Format the output for readability
                timestamp = datetime.now().strftime("%H:%M:%S")
                who = data.get("who", "Unknown")
                feeling = data.get("feeling", "neutral")
                what = data.get("what", "")
                
                print(f"[{timestamp}] {who.upper()} | Feeling: {feeling}")
                print(f" > {what}")
                print("-" * 50)
                
    except ConnectionRefusedError:
        print("[!] Error: memory_garden daemon is not running.")
    except Exception as e:
        print(f"[!] Lost connection: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(monitor_commune())
    except KeyboardInterrupt:
        print("\n[*] Monitoring stopped.")
