# Django Rest Scholl

## Preparing the environment

### Linux (Ubuntu/Debian)

- Create a virtual environment

```bash
python3 -m venv .venv
```

- Activate the virtual environment

```bash
source .venv/bin/activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

### Windows

- Create a virtual environment

```bash
python -m venv .venv
```

- Activate the virtual environment

```bash
.venv\Scripts\activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

## Preparing Docker

- Navigate to Docker

```bash
cd Docker
```

- Create the containers

```bash
docker-compose up -d
```

- Verification (optional)

```bash
docker ps
```

## Migration DB

```bash
flask db init

flask db migrate -m "Initial migration."

flask db upgrade
```