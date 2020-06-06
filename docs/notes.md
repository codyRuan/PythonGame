## Data format from server after pressing START button
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
    - `id`: Which map to use.
- `control`: Player id for this client to control.
- `players`:
    - `status`:
        - Choices are `ALIVE`, `DEAD`