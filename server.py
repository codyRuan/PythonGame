import socket
import json
from easydict import EasyDict

START_RESPONSE = '''{
    "map": {
        "id": 1
    },
    "control": 2,
    "fps": 30,
    "players": [
        {
            "id": 1,
            "x": 300,
            "y": 200,
            "speed": 4,
            "range": 3,
            "status": "ALIVE"
        },
        {
            "id": 2,
            "x": 350,
            "y": 250,
            "speed": 5,
            "range": 7,
            "status": "DEAD"
        },
        {
            "id": 3,
            "x": 200,
            "y": 160,
            "speed": 4,
            "range": 3,
            "status": "ALIVE"
        },
    ]
}'''


def StartHandle(c, recv):
    c.send(START_RESPONSE)


def ActionHandle(c, recv):
    pass


def StopHandle(c, recv):
    pass


def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 8787
    s.bind((host, port))
    s.listen(5)

    while True:
        c, addr = s.accept()
        s = c.recv(4096)
        print(f'Server received {s}')
        recv = Easydict(json.loads(s))
        if recv.request == 'START':
            StartHandle(c, recv)
        elif recv.request == 'Action':
            ActionHandle(c, recv)
        elif recv.request == 'STOP':
            StopHandle(c, recv)


if __name__ == "__main__":
