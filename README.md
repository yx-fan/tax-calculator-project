# tax-calculator-project

## Description
This project is a tax calculator API that calculates the total income tax for a given salary and tax year based on marginal tax rates. It interacts with a provided API that returns tax brackets for supported tax years (2019-2022).

## Pre-requisites for running the application on local machine
Make sure you have the following installed on your local machine:
- Python 3.12
- Docker
- Docker Compose
- Redis (if you want to run the application server manually)

## Setup Instructions

### Clone the repository
```bash
git clone https://github.com/yx-fan/tax-calculator-project.git
cd tax-calculator-project
```

### Create a virtual environment
```bash
python3.12 -m venv project-venv
source project-venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Setup `5001` server for the tax brackets API
```bash
docker pull ptsdocker16/interview-test-server
docker run --init -p 5001:5001 -it ptsdocker16/interview-test-server
```

### Setup environment variables
```bash
mv .env.example .env
```

### Install Redis on MacOS, for other OS please refer to the official documentation
```bash
brew install redis
redis-server
```

### Run the application server manually
```bash
python run.py
```

## Setup Instructions using Docker

### Clone the repository
```bash
git clone https://github.com/yx-fan/tax-calculator-project.git
cd tax-calculator-project
```

### Setup `5001` server for the tax brackets API
```bash
docker pull ptsdocker16/interview-test-server
docker run --init -p 5001:5001 -it ptsdocker16/interview-test-server
```

### Setup environment variables
```bash
mv .docker.env.example .docker.env
```

### Build, Test, Build and Run the Docker image
```bash
chmod +x start.sh
./start.sh
```

### Stop the Docker container
```bash
chmod +x stop.sh
./stop.sh
```

## API Endpoints

### Calculate total income tax for a given salary and tax year
```bash
POST /calculate-tax
```

#### Request
```json
{
    "salary": 100000,
    "tax_year": 2022
}
```

#### Response
```json
{
    "annual_income": 160000,
    "effective_tax_rate": 20.91,
    "tax_breakdown": [
        {
            "bracket": "0 - 50197",
            "tax_amount": 7529.55
        },
        {
            "bracket": "50197 - 100392",
            "tax_amount": 10289.97
        },
        {
            "bracket": "100392 - 155625",
            "tax_amount": 14360.58
        },
        {
            "bracket": "155625 - 221708",
            "tax_amount": 1268.75
        },
        {
            "bracket": "221708 - ∞",
            "tax_amount": 0
        }
    ],
    "total_taxes": 33448.85
}
```

## Running Tests
```bash
pytest tests/
```

## Author
Yuxin Fan
```
