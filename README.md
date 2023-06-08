# Car-Website
Car website for course - DIS
This is the repository for the car website project for the course DIS conducted by group group-number 

Dependencies:
- Python
- Flask
- psycopg2

Setup:
Schemas:
Run the schemas sql file in the website/website folder
Data:
To copy the dataset use the following command.
--command " "\\copy public.cars (cars_id, name, available_since, german_price, netherlands_price, unitedkingdom_price, battery, acceleration, top_speed, range, efficiency, fast_charge, towing, seats) FROM 'C:/Users/lukas/OneDrive/DOKUME~1/GitHub/CAR-WE~1/Website/Data.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8' QUOTE '\"' ESCAPE '''';""

How to run:
run the following command in your terminal in the website folder.
python .\run.py

