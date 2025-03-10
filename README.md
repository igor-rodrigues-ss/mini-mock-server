# Mini Mock Server

A mini mock server for http requests.

## Features
- Start an HTTP mock server without installing any web framework.
- Delay requests to simulate slow endpoints using the *response.sleep* attribute.
- Return random responses on the same route to simulate different kind of responses.

## Important Notices

> Currently, the ```mini-mock-server``` uses the ```http.server``` to start a new server, which is not recommended for production environments. The ```http.server``` only implements basic security checks. See the [official documentation](https://docs.python.org/3/library/http.server.html) for more information.

## Installation

```shell
pip install mini-mock-server
```

### Usage

1. Create a ```mock-api.json``` file for route specifications.
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
                    "sleep": 1,
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
2. Start the mock server.

```shell
mini-mock-server mock-api.json
```

