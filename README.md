# All-Random-API

## API for generating deterministic random data

[![Docker](https://img.shields.io/badge/Docker-✔%20Ready-blue?logo=docker)](https://hub.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-✔%20Powered-green?logo=fastapi)](https://fastapi.tiangolo.com/)

### Attention

This API is designed for non-cryptographic, general-purpose randomization and should not be used in security-sensitive contexts.

### Installation

```bash
git clone https://github.com/your-username/all-random-api.git
cd all-random-api
```

### Endpoints

| Title | Method | Endpoint | Parameters | Request | Response |
| --- | --- | --- | --- | --- | --- |
| **Deterministic Boolean** | `GET` | `/det/random-bool` | `seed` (string, required) | `http://localhost:8000/det/random-bool?seed=test123` | ```{"bool": true}``` |
| **Non-Deterministic Boolean** | `GET` | `/nondet/random-bool` | None | `http://localhost:8000/nondet/random-bool` | ```{"bool": false}``` |
| **Deterministic Digit** | `GET` | `/det/random-digit` | `seed` (string, required) | `http://localhost:8000/det/random-digit?seed=test123` | ```{"digit": 5}``` |
| **Non-Deterministic Digit** | `GET` | `/nondet/random-digit` | None | `http://localhost:8000/nondet/random-digit` | ```{"digit": 3}``` |
| **Deterministic Character** | `GET` | `/det/random-char` | `seed` (string, required) | `http://localhost:8000/det/random-char?seed=test123` | ```{"char": "A"}``` |
| **Non-Deterministic Character** | `GET` | `/nondet/random-char` | None | `http://localhost:8000/nondet/random-char` | ```{"char": "$"}``` |
| **Deterministic Number** | `GET` | `/det/random-int-number` | `seed` (string, required), `min_val` (int, optional, default=-2147483647), `max_val` (int, optional, default=2147483647) | `http://localhost:8000/det/random-int-number?seed=test123` | ```{"number": -3357220}``` |
| **Non-Deterministic Number** | `GET` | `/nondet/random-int-number` | `min_val` (int, optional, default=-2147483647), `max_val` (int, optional, default=2147483647) | `http://localhost:8000/nondet/random-int-number` | ```{"number": 123456789}``` |
| **Deterministic Hash** | `GET` | `/det/random-hash` | `seed` (string, required), `algorithm` (string, optional, default=sha256) | `http://localhost:8000/det/random-hash?seed=test123&algorithm=md5` | ```{"hash": "e10adc3949ba59abbe56e057f20f883e"}``` |
| **Non-Deterministic Hash** | `GET` | `/nondet/random-hash` | `algorithm` (string, optional, default=sha256) | `http://localhost:8000/nondet/random-hash?algorithm=md5` | ```{"hash": "a1b2c3d4e5f6..."}``` |
| **Deterministic Bytes** | `GET` | `/det/random-bytes` | `seed` (string, required), `length` (int, optional, default=16) | `http://localhost:8000/det/random-bytes?seed=test123&length=32` | ```{"bytes": "bWYyNWJiZGNjNDJlYjM0ZTBj..."}``` |
| **Non-Deterministic Bytes** | `GET` | `/nondet/random-bytes` | `length` (int, optional, default=16) | `http://localhost:8000/nondet/random-bytes?length=32` | ```{"bytes": "aGVsbG8gd29ybGQh..."}``` |
| **Deterministic Timestamp** | `GET` | `/det/random-timestamp` | `seed` (string, required), `days` (int, optional, default=365) | `http://localhost:8000/det/random-timestamp?seed=test123&days=100` | ```{"timestamp": "2023-07-15 14:30:45.123456"}``` |
| **Non-Deterministic Timestamp** | `GET` | `/nondet/random-timestamp` | `days` (int, optional, default=365) | `http://localhost:8000/nondet/random-timestamp?days=100` | ```{"timestamp": "2024-01-01 00:00:00.000000"}``` |
| **Deterministic Color** | `GET` | `/det/random-color` | `seed` (string, required) | `http://localhost:8000/det/random-color?seed=test123` | ```{"color": "#a1b2c3"}``` |
| **Non-Deterministic Color** | `GET` | `/nondet/random-color` | None | `http://localhost:8000/nondet/random-color` | ```{"color": "#ff00cc"}``` |
| **Deterministic UUID** | `GET` | `/det/random-uuid` | `seed` (string, required) | `http://localhost:8000/det/random-uuid?seed=test123` | ```{"uuid": "550e8400-e29b-41d4-a716-446655440000"}``` |
| **Non-Deterministic UUID** | `GET` | `/nondet/random-uuid` | None | `http://localhost:8000/nondet/random-uuid` | ```{"uuid": "d41d8cd9-8f00-3204-a980-0998ecf8427e"}``` |
| **Deterministic Password** | `GET` | `/det/random-password` | `seed` (string, required), `length` (int, optional, default=12) | `http://localhost:8000/det/random-password?seed=test123&length=16` | ```{"password": "Pa$sw0Rd!12345XyZ"}``` |
| **Non-Deterministic Password** | `GET` | `/nondet/random-password` | `length` (int, optional, default=12) | `http://localhost:8000/nondet/random-password?length=16` | ```{"password": "9$kLm@rQvZpTn..."}``` |
| **Deterministic Choice** | `GET` | `/det/random-choice` | `seed` (string, required), `items` (comma-separated string, required) | `http://localhost:8000/det/random-choice?seed=test123&items=square,circle,triangle` | ```{"choice": "circle"}``` |
| **Non-Deterministic Choice** | `GET` | `/nondet/random-choice` | `items` (comma-separated string, required) | `http://localhost:8000/nondet/random-choice?items=square,circle,triangle` | ```{"choice": "triangle"}``` |
| **Deterministic IP** | `GET` | `/det/random-ip` | `seed` (string, required) | `http://localhost:8000/det/random-ip?seed=test123` | ```{"ip": "123.45.67.89"}``` |
| **Non-Deterministic IP** | `GET` | `/nondet/random-ip` | None | `http://localhost:8000/nondet/random-ip` | ```{"ip": "84.203.12.45"}``` |

**Notes:**

1. All `seed` parameters are mandatory and affect the result
2. Responses contain deterministic values ​​(same seed = same result)
3. For `/random-hash` all algorithms from `hashlib` are supported (md5, sha1, sha256, etc.)
4. Passwords are generated from the set: `A-Za-z0-9!@#$%^&*`
5. Time in `/random-timestamp` is counted from the current moment back
