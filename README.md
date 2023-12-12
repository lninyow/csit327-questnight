# QuestNight API

Members:

- Baclayon, Leonel - [carefreebee](https://github.com/carefreebee)
- Sagmon, Liden - [lninyow](https://github.com/lninyow)
- Tampus, Nathaniel - [dotnize](https://github.com/dotnize)

## Setup

1. Create a virtual environment:

```sh
python -m venv .venv
```

2. Activate the virtual environment

for bash/zsh:

```sh
source .venv/bin/activate
```

for windows powershell:

```sh
.venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Create a `.env` file and with the following template:

```sh
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DB=questnight
MYSQL_CURSORCLASS=DictCursor
MYSQL_AUTOCOMMIT=true

PORT = 5000
```

### Running the Flask app

```sh
python main.py
```
