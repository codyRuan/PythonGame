## Start request
- Client to server:
    ```json
    {
        "request": "START"
    }
    ```
- Server to client:
    ```json
    {
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
    }
    ```
- `map`
    - `id`: Which map to use. (0 ~ n)
- `control`: Player id for this client to control. (1 ~ n)
- `players`:
    - `status`:
        - Choices are `ALIVE`, `DEAD`
## Map
- Types of blocks:
    - Breakable
    - Unbreakable
    - Map格式，`o`表可走，`b`表breakable, `u`表unbreakable
## Control
- Type of controls:
    - `0`: Nothing
    - `1`: Up
    - `2`: Right
    - `3`: Down
    - `4`: Left
    - `5`: Space, put down bubble