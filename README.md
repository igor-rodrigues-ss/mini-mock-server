# Mini Mock Server

A mini mock server for http requests.

## Features
- Start a http mock server using the lib ```http.server```.
- Delay requests to simulate slow endpoints.
- Return random responses on the same route to simulate success or error cases.

## Installation

```shell
pip install mini-mock-server
```

### Usage

1. Create ```mock-api.json``` file to routes especifications.
```
{
    "/": [
        {
            "url": "/users",
            "method": "GET",
            "response": [
                {
                    "status_code": 200,
                    "body": [
                        {"id": 1, "name": "Mario"},
                        {"id": 2, "name": "Luigi"}
                    ]
                },
                {
                    "status_code": 400,
                    "body": {"error": "Bad request custom message"}
                }
            ]
        }
    ],
    "/api": [
        {
            "url": "/products/:id",
            "method": "GET",
            "response": {
                "status_code": 200,
                "body": {
                    "id": 1,
                    "name": "Product 001",
                    "price": 115.51
                }
            }
        }
    ]
}
```
2. Start the mock server

```shell
mini-mock-server mock-api.json
```

