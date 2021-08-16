import socket
import sys

def main():
	try:
		ip = socket.gethostbyname(sys.argv[1])
		return f"\033[92m[+]URL: {sys.argv[1]}\n[+]IP: {ip}\033[00m"
	except IndexError:
		return "\033[91m[-]Debes especificar una url\033[00m"
	except socket.gaierror:
		return "\033[91m[-]Has proporcionado una url invalida\033[00m"

if __name__ == '__main__':
	print(main())
