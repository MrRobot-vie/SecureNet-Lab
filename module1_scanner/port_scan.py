import socket
import sys
import json
services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}
from concurrent.futures import ThreadPoolExecutor 
def tester_port(ip, port):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.settimeout(1) # on dit au socket d'attendre maximum 1 seconde
   resultat = sock.connect_ex((ip, port))
   sock.close()
   if resultat == 0:
      nom = services.get(port, "inconnu")
      print(f"Port {port} : OUVERT ({nom})")
      resultats.append({"port": port, "service": nom, "etat": "ouvert"})
   
ip = sys.argv[1]
ports = range(1, 1025)
resultats = []
with ThreadPoolExecutor(max_workers=50) as executor:
   for port in ports:
      executor.submit(tester_port, ip, port)

donnees = {"ip" : ip, "ports": resultats}
with open("resultats.json", "w") as fichier: 
   json.dump(donnees, fichier, indent = 4)

print("\nResultats sauvegardés dans reslutats.json")
