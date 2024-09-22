CREATE DATABASE IF NOT EXISTS old_database;
USE old_database;
CREATE TABLE IF NOT EXISTS customer (
    customer_id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(100),
    birth_date DATE,
    last_purchase_date DATE,
    phone_num VARCHAR(10),
    num_of_product INT,
    total_amount DECIMAL(15,2),
    loyalty_program VARCHAR(5)
);

CREATE DATABASE IF NOT EXISTS new_database;
USE new_database;
CREATE TABLE IF NOT EXISTS customer (
    customer_id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(100),
    birth_date DATE,
    last_purchase_date DATE,
    phone_num VARCHAR(10),
    num_of_product INT,
    total_amount DECIMAL(15,2),
    loyalty_program VARCHAR(5)
);
