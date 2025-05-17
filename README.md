# All-Random-API

## API for generating deterministic random data

[![Docker](https://img.shields.io/badge/Docker-✔%20Ready-blue?logo=docker)](https://hub.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-✔%20Powered-green?logo=fastapi)](https://fastapi.tiangolo.com/)

### Installation

```bash
git clone https://github.com/your-username/all-random-api.git
cd all-random-api
```

### Endpoints

| Title | Method | Endpoint | Parameters | Request | Response |
| --- | --- | --- | --- | --- | --- |
| Generate Boolean | `GET` | `/random-bool` | `seed` (string, required) | `http://localhost:8000/random-bool?seed=test123` | ```{"bool": true}``` |
| Generate Digit | `GET` | `/random-digit` | `seed` (string, required) | `http://localhost:8000/random-digit?seed=test123` | ```{"digit": 5}``` |
| Generate Character | `GET` | `/random-char` | `seed` (string, required) | `http://localhost:8000/random-char?seed=test123` | ```{"char": "A"}``` |
| Generate Number | `GET` | `/random-number` | `seed` (string, required) | `http://localhost:8000/random-number?seed=test123` | ```{"number": 335722038548047932699313735189696540443}``` |
| Generate Hash | `GET` | `/random-hash` | `seed` (string, required), `algorithm` (string, optional, default=sha256) | `http://localhost:8000/random-hash?seed=test123&algorithm=md5` | ```{"hash": "e10adc3949ba59abbe56e057f20f883e"}``` |
| Generate Bytes | `GET` | `/random-bytes` | `seed` (string, required), `length` (int, optional, default=16) | `http://localhost:8000/random-bytes?seed=test123&length=32` | ```{"bytes": "bWYyNWJiZGNjNDJlYjM0ZTBj..."}``` |
| Generate Timestamp | `GET` | `/random-timestamp` | `seed` (string, required), `days` (int, optional, default=365) | `http://localhost:8000/random-timestamp?seed=test123&days=100` | ```{"timestamp": "2023-07-15 14:30:45.123456"}``` |
| Generate Color | `GET` | `/random-color` | `seed` (string, required) | `http://localhost:8000/random-color?seed=test123` | ```{"color": "#a1b2c3"}``` |
| Generate UUID | `GET` | `/random-uuid` | `seed` (string, required) | `http://localhost:8000/random-uuid?seed=test123` | ```{"uuid": "550e8400-e29b-41d4-a716-446655440000"}``` |
| Generate Password | `GET` | `/random-password` | `seed` (string, required), `length` (int, optional, default=12) | `http://localhost:8000/random-password?seed=test123&length=16` | ```{"password": "Pa$sw0Rd!12345XyZ"}``` |
| Random Choice | `GET` | `/random-choice` | `seed` (string, required), `items` (comma-separated string, required) | `http://localhost:8000/random-choice?seed=test123&items=square,circle,triangle` | ```{"choice": "circle"}``` |

**Notes:**

1. All `seed` parameters are mandatory and affect the result
2. Responses contain deterministic values ​​(same seed = same result)
3. For `/random-hash` all algorithms from `hashlib` are supported (md5, sha1, sha256, etc.)
4. Passwords are generated from the set: `A-Za-z0-9!@#$%^&*`
5. Time in `/random-timestamp` is counted from the current moment back
