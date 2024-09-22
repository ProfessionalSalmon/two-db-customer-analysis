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

with open("data/old.csv", "w") as old, open("data/new.csv", "w") as new:
    old.write("customer_id,name,birth_date,last_purchase_date,phone_num,num_of_product,total_amount,loyalty_program\n") # header
    new.write("customer_id,name,birth_date,last_purchase_date,phone_num,num_of_product,total_amount,loyalty_program\n")
    for i in range(100):
        name = generate_name()
        uid = uuid.uuid4()
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
        
        old.write(f"{uid},{name},{birth_date},{old_date},{old_phone},{old_num_pro},{old_amount},{old_loyalty}\n")
        if random.random() < 0.9:
            new.write(f"{uid},{name},{birth_date},{new_date},{new_phone},{new_num_pro},{new_amount},{new_loyalty}\n")
        
    for i in range(20):
        name = generate_name()
        uid = uuid.uuid4()
        birth_date = generate_date(start_year=1960, end_year=1992)
        date = generate_date(start_year=2018, end_year=2024)
        phone = generate_phone_number()        
        number_of_product = generate_num_product()
        amount = generate_amount()
        loyalty = loyalty_program()
        
        new.write(f"{uid},{name},{birth_date},{date},{phone},{number_of_product},{amount},{loyalty}\n")