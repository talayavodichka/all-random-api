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
| **Deterministic Integer** | `GET` | `/det/random-integer` | `seed` (string, required), `min_val` (int, optional, default=-2147483647), `max_val` (int, optional, default=2147483647) | `http://localhost:8000/det/random-integer?seed=test123` | ```{"integer": -3357220}``` |
| **Non-Deterministic Integer** | `GET` | `/nondet/random-integer` | `min_val` (int, optional, default=-2147483647), `max_val` (int, optional, default=2147483647) | `http://localhost:8000/nondet/random-integer` | ```{"integer": 123456789}``` |
| **Deterministic Float** | `GET` | `/det/random-float` | `seed` (string, required), `min_val` (float, optional, default=-2147483647), `max_val` (float, optional, default=2147483647) | `http://localhost:8000/det/random-float?seed=test123` | ```{"float": -3357220.0}``` |
| **Non-Deterministic Float** | `GET` | `/nondet/random-float` | `min_val` (float, optional, default=-2147483647), `max_val` (float, optional, default=2147483647) | `http://localhost:8000/nondet/random-float` | ```{"float": 123456789.0}``` |
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
| **Deterministic IPv4** | `GET` | `/det/random-ipv4` | `seed` (string, required) | `http://localhost:8000/det/random-ipv4?seed=test123` | ```{"ipv4": "123.45.67.89"}``` |
| **Non-Deterministic IPv4** | `GET` | `/nondet/random-ipv4` | None | `http://localhost:8000/nondet/random-ipv4` | ```{"ipv4": "84.203.12.45"}``` |
| **Deterministic IPv6** | `GET` | `/det/random-ipv6` | `seed` (string, required) | `http://localhost:8000/det/random-ipv6?seed=test123` | ```{"ipv6": "746c:1cf7:60fe:8a6b:2e9d:1a81:2e23:df9d"}``` |
| **Non-Deterministic IPv6** | `GET` | `/nondet/random-ipv6` | None | `http://localhost:8000/nondet/random-ipv6` | ```{"ipv6": "343e:2f33:cb3d:01a1:14d5:631b:e7a6:8455"}``` |
| **Deterministic Coords** | `GET` | `/det/random-coords` | `seed` (string, required) | `http://localhost:8000/det/random-coords?seed=test123` | ```{"coords": [65.98980952135085, 65.67239892364952]}``` |
| **Non-Deterministic Coords** | `GET` | `/nondet/random-coords` | None | `http://localhost:8000/nondet/random-coords` | ```{"coords":  [55.883126975850075, 109.69373725793417]}``` |

**Notes:**

1. All `seed` parameters are mandatory and affect the result
2. Responses contain deterministic values ​​(same seed = same result)
3. For `/random-hash` all algorithms from `hashlib` are supported (md5, sha1, sha256, etc.)
4. Passwords are generated from the set: `A-Za-z0-9!@#$%^&*`
5. Time in `/random-timestamp` is counted from the current moment back
