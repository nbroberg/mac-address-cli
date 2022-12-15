# Python MAC Address CLI (MacOS/zsh Instructions)

## Prerequisite Steps

1. Setup account at https://macaddress.io

2. Find API Key at https://macaddress.io/account/general in the section labeled `Your API key`

## Running from Docker Container

1. Install Docker
```
brew install docker
```

2. Open Docker Desktop
```
open /Applications/Docker.app
```

3. Build `mac-address-cli` container
```
docker build -t nbroberg/mac-address-cli:latest .
```

4. Run `mac-address-cli` container
```
docker run \
    -e API_KEY=<MACADDRESS.IO API KEY> \
    nbroberg/mac-address-cli:latest \
    44:38:39:ff:ef:57 # ANY MAC ADDRESS
```

## Debugging the Python Code

1. Clone Github repository
```
git clone https://github.com/nbroberg/mac-address-cli
cd mac-address-cli
```

2. Setup virtual environment to isolate Python dependency installation
```
python3 -m venv venv
source venv/bin/activate
```

3. Install Python dependencies
```
# note: pip3 not required in venv
pip install -r requirements.txt
```

4. Start CLI
```
# note: python3 differentiation not required in venv
python cli.py  \
    --log-level <DEBUG|INFO|WARN|ERROR>
    --api-key <MACADDRESS.IO API KEY>
    --mac-address 44:38:39:ff:ef:57 # ANY MAC ADDRESS
```
