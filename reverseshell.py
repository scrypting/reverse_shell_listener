import socket
import sys
import time


def listen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    print("Listening on port " + str(port))
    conn, addr = s.accept()
    print('Connection received from ', addr)

    try:
        while True:
            ans = conn.recv(1024).decode()
            sys.stdout.write(ans)
            command = input()

            command += "\n"
            conn.send(command.encode())
            time.sleep(1)

            sys.stdout.write("\033[A" + ans.split("\n")[-1])

    except KeyboardInterrupt:
        print("\nClosing the connection.")
        conn.close()
        s.close()


if __name__ == "__main__":
    listen("0.0.0.0", 12345)  # You can replace with your desired IP and port, enjoy my code!