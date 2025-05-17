# All-Random-API

## API for generating deterministic random data

[![Docker](https://img.shields.io/badge/Docker-✔%20Ready-blue?logo=docker)](https://hub.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-✔%20Powered-green?logo=fastapi)](https://fastapi.tiangolo.com/)

### Installation

```bash
git clone https://github.com/your-username/all-random-api.git
cd all-random-api
```

### Generate Deterministic Random Number

- **Method**: `GET`
- **Endpoint**: `/random-number`
- **Description**: Generates a unique 128-bit integer based on SHA-256 hash of the seed.  
  *Guaranteed no collisions for different seeds*.
- **Parameters**:
  - `seed` (string, required): Input seed value
- **Example**:

```bash
  curl "http://localhost:8000/random-number?seed=nice_try_251"
```
