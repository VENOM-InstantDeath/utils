import requests
import socket

def ip_a():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def pip_a():
    return requests.get("http://ipecho.me").content.decode("utf-8").strip()

if __name__ == "__main__":
    print(f"Private IP: {ip_a()}")
    print(f"Public IP:  {pip_a()}")
