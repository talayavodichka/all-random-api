# All-Random-API

## API for generating deterministic random data

[![Docker](https://img.shields.io/badge/Docker-✔%20Ready-blue?logo=docker)](https://hub.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-✔%20Powered-green?logo=fastapi)](https://fastapi.tiangolo.com/)

### Installation

```bash
git clone https://github.com/your-username/all-random-api.git
cd all-random-api
```

## Endpoints

### Generate Number

- **Method**: `GET`
- **Endpoint**: `/random-number`
- **Parameters**:
  - `seed` (string, required)
- **Request**:

```bash
  curl "http://localhost:8000/random-number?seed=test123"
```

- **Response**:

```json
{
  "random_number": 335722038548047932699313735189696540443
}
```

### Generate Bytes

- **Method**: `GET`
- **Endpoint**: `/random-bytes`
- **Parameters**:
  - `seed` (string, required)
  - `length` (string, optional)
- **Request**:

```bash
  curl "http://localhost:8000/random-bytes?seed=test123&length=32"
```

- **Response**:

```json
{
  "random_bytes": 335722038548047932699313735189696540443
}
```
