import mysql.connector
import random
from datetime import datetime, timedelta
import uuid

random.seed(2024)

first_names = ["Evan", "Sophie", "Liam", "Maya", "Jordan", "Emily", "Lucas", "Olivia", "Nathan", "Grace"]
last_names = ["Palmer", "Bennett", "Torres", "Sinclair", "Hayes", "Johnson", "Smith", "Williams", "Brown", "Taylor"]

def generate_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

def generate_amount():
    return random.randint(1,10) * 1000000

def generate_date(start_year, end_year):
    year = random.randint(start_year, end_year)
    start_date = datetime(year, 1, 1)
    random_days = random.randint(0, 364)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")

def generate_num_product():
    return random.randint(1, 10)

def generate_phone_number():
    area_code = random.choice(["08","06"])
    first_part = "".join(random.choices("0123456789", k=8))
    return f'{area_code}{first_part}'

def loyalty_program():
    if random.random() < 0.2:
        return 'yes'
    else:
        return 'no'
    
# connection

connection_old = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="my-secret-pw",
    database="old_database"
)

connection_new = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="my-secret-pw",
    database="new_database"
)

cursor_old = connection_old.cursor()
cursor_new = connection_new.cursor()

# insert
insert_query = '''
    INSERT INTO customer (customer_id, name, birth_date, last_purchase_date, phone_num, num_of_product, total_amount, loyalty_program)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        birth_date = VALUES(birth_date),
        last_purchase_date = VALUES(last_purchase_date),
        phone_num = VALUES(phone_num),
        num_of_product = VALUES(num_of_product),
        total_amount = VALUES(total_amount),
        loyalty_program = VALUES(loyalty_program);
'''

for i in range(100):
    name = generate_name()
    uid = str(uuid.uuid4())
    birth_date = generate_date(start_year=1960, end_year=1992)
    
    old_date = generate_date(start_year=2010, end_year=2017)
    new_date = random.choice([old_date, generate_date(start_year=2018, end_year=2024)])
    old_phone = generate_phone_number()
    if random.random() < 0.3:
        new_phone = generate_phone_number()
    else:
        new_phone = old_phone
    
    old_num_pro = generate_num_product()
    if new_date == old_date:
        new_num_pro = old_num_pro
    else:
        new_num_pro = old_num_pro + generate_num_product()
    old_amount = generate_amount()
    if new_date == old_date:
        new_amount = old_amount
    else:
        new_amount = old_amount + generate_amount()
    
    old_loyalty = loyalty_program()
    new_loyalty = loyalty_program()
    
    data_old = (uid, name, birth_date, old_date, old_phone, old_num_pro, old_amount, old_loyalty)
    data_new = (uid, name, birth_date, new_date, new_phone, new_num_pro, new_amount, new_loyalty)

    cursor_old.execute(insert_query, data_old)
    if random.random() < 0.9:
        cursor_new.execute(insert_query, data_new)


connection_old.commit()
connection_new.commit()

for i in range(20):
    name = generate_name()
    uid = str(uuid.uuid4())
    birth_date = generate_date(start_year=1960, end_year=1992)
    date = generate_date(start_year=2018, end_year=2024)
    phone = generate_phone_number()        
    number_of_product = generate_num_product()
    amount = generate_amount()
    loyalty = loyalty_program()
    data_new = (uid, name, birth_date, new_date, new_phone, new_num_pro, new_amount, new_loyalty)
    cursor_new.execute(insert_query, data_new)
    
connection_new.commit()

cursor_old.close()
connection_old.close()
cursor_new.close()
connection_new.close()