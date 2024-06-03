# Finance Project

This Django application integrates with the Yahoo Finance API using the `yfinance` library to fetch and store company data. It supports CRUD operations on company data and provides advanced functionalities like exporting data to CSV.

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip
- Virtualenv (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd finance_project

### Install dependencies
pip install -r requirements.txt

### Run migrations

python manage.py migrate



### Create a superuser  (optional):
python manage.py createsuperuser

### Start the server
python manage.py runserver

-----  API Endpoints------


### GET Companies -->

http://127.0.0.1:8000/companies/

### POST COMPANIES  -->

POST http://127.0.0.1:8000/companies/
Content-Type: application/json

{
  "symbol": "AAPL"
}

### DELETE /companies/{id}/ -->
Deletes a company by its ID.

DELETE http://127.0.0.1:8000/companies/1/


###  Downloads CSV -->
GET http://127.0.0.1:8000/export/


### RUN TESTS -->

python manage.py test
