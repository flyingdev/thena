<div align="center">
    <h1>Thena</h1>
</div>

<div align="center">
<strong>Goal</strong>
<p>
Create a system where high-volume data can be uploaded for analysis, store it in a database table and retrieve it for analysis. Here is the task.

Part 1: Data upload

The uploaded data is a CSV file. Has max 5 columns. (The CSV is attached)
The data uploaded for the same customers is always has the same columns.
The data uploaded should get appended to the customers table if a table already exists, else we have to create a new table for this customer.


Part 2: Analysis request

When a analysis request comes in, simple aggregations like (time difference between 1st row and the most upto date row, total number of rows) should be processed and
results should be returned back to the customer.(Consider the time-space-complexity trade-offs)

Part 3:

Dockerfile or docker-compose file for us to check the code is working.
</p>
</div>

<div align="left">
<strong>Implementation</strong>
<p>

    Stacks : Python 3.8 Django 3

    Database: Sqlite3

    Introduced celery worker for pushing data into database
</p>
</div>

<div align="left">
<strong>Assumptions</strong>
<ul>
<li>CSV File Limit : 100MB</li>
</ul>
</div>

<div align="left">
<strong>Constraints</strong>
<ul>
<li>Customer id should be unique and provided to customer in advance. Recommended naming convention: UUID or integer</li>
</ul>
</div>

<div align="left">
<strong>API</strong>
<ul>
<li>
POST:  http://127.0.0.1:8000/api/v1/event/

CONTENT-TYPE: multipart/form-data

PARAMS:

    file: csv file

    customer_id: customer identifier
</li>
<li>
POST:  http://127.0.0.1:8000/api/v1/analyze/

CONTENT-TYPE: application/json

PARAMS:

    customer_id: customer identifier

    analyze_type: report type

analyze_types:

    analyze_type 10000: Time Difference

    analyze_type 10001: Total Rows
</li>
</ul>
</div>

<div align="left">
<strong>HOW TO RUN</strong>
<ul>
<li>docker-compose -f docker-compose.dev.yml build</li>
<li>docker-compose -f docker-compose.dev.yml up</li>
</ul>
</div>

<div align="left">
<strong>HOW TO TEST USING CURL</strong>
<ul>
<li>curl --location --request POST 'http://127.0.0.1:8000/api/v1/event/' \
--form 'file=@"/home/abc/Downloads/events_data.csv"' \
--form 'customer_id="1000"'</li>
<li>curl --location --request POST 'http://127.0.0.1:8000/api/v1/analyze/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "customer_id": 1000,
    "analyzer_type": 10000
}'</li>
</ul>
</div>

<div align="left">
<strong>TO DO</strong>
<ul>
<li>Swagger API documentation</li>
<li>UI for API</li>
<li>Customer ID Validation</li>
<li>Serializer</li>
<li>Write Test</li>
</ul>
</div>
