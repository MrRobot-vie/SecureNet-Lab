import socket
import sys

from concurrent.futures import ThreadPoolExecutor 
def tester_port(ip, port):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.settimeout(1) # on dit au socket d'attendre maximum 1 seconde
   resultat = sock.connect_ex((ip, port))
   sock.close()
   if resultat == 0:
      print(f"Port {port} : OUVERT")
   
ip = sys.argv[1]
ports = range(1, 1025)
with ThreadPoolExecutor(max_workers=50) as executor:
   for port in ports:
      executor.submit(tester_port, ip, port)
