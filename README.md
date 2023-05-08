# OSS_Senior_Design
Purdue ECE 49595 OSS Senior Design

## Overview

The Start Up Investor is a web-based application designed to provide users with information on startup companies, including estimated ROI values and details on individual companies.

## API Endpoints

1. /roi/: This endpoint allows users to input a startup name and investment amount and queries the database to calculate the estimated ROI value.
2. /topPicks/: This endpoint displays the top 10 startup companies with the highest ROI values from the database.
3. /details/id/: This endpoint displays the details of a startup company based on the unique ID assigned to each company in the database. The user doesn't have direct access to all IDs, but they can view details by using the /roi/ endpoint to get details using the names.

## Installation and Usage

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up the database by running the appropriate commands (`python manage.py migrate`).
4. Run the server with `python manage.py runserver`.
5. Use a web browser or API client to access the endpoints.

## Technologies Used

The Startup Predictor API was built using the following technologies:

1. Python
2. Django
3. PostgreSQL

## Python Packages Used 

The following Python packages were used in this project:

- asgiref==3.6.0
- Django==4.1.6 
- joblib==1.2.0 
- numpy==1.24.2 
- pandas==1.5.3 
- psycopg2-binary==2.9.6
- python-dateutil==2.8.2 
- pytz==2022.7.1 
- scikit-learn==1.2.1
- scipy==1.10.1 
- six==1.16.0 
- sqlparse==0.4.3
- threadpoolctl==3.1.0 
- tzdata==2022.7 
- Gunicorn

## Contributors

- Aakash Sivasankar (https://github.com/aakashsiv) 
- Siya Sharma (https://github.com/siyaduttsharma)
- Jiaqi Tang (https://github.com/KumoK17)
