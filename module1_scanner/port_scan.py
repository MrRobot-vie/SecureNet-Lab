import socket 
def tester_port(ip, port):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.settimeout(1) # on dit au socket d'attendre maximum 1 seconde
   resultat = sock.connect_ex((ip, port))
   sock.close()
   if resultat == 0:
      print(f"Port {port} : OUVERT")
   else:
      print(f"Port {port} : FERME")
tester_port("192.168.56.101", 22)
