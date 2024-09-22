# Analysis of Old vs New Customer dataset

## Generate data
This project generates customer data and stores it in either CSV file or MySQL database

### CSV file
Execute
```bash
python insert_to_csv.py
```

### MySQL database

Before getting started, ensure you have the following installed on your device:

- [Docker](https://www.docker.com/)
- Python 3.x

Additionally, install the required Python package for connecting to MySQL:

```bash
pip install mysql-connector-python
```

Once the services are up and running, generate the data by executing:

```bash
python insert_to_db.py
```

After you're done with generating and analyzing data, you can stop and clean up the Docker containers and volumes by executing:

```bash
docker compose down --volumes
```

## Analyze Data
Once the data is generated, you can analyze it using the provided Jupyter Notebook

Open and execute the notebook cells in: `analysis.ipynb`

(The conclusions and insights shown in current analysis file output is based on data from CSV file)