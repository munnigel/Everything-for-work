import csv
import uuid
import random
from datetime import datetime, timedelta

# Generate 10,000 rows for Source A
num_rows = 10000
rows = []

# Generate random datetime
def random_date(start, end):
    return start + (end - start) * random.random()

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Generate data with the conditions to test for DQC
for i in range(num_rows):
    transaction_uuid = str(uuid.uuid4())
    user_id = random.randint(1, 1000)
    update_date_time = random_date(start_date, end_date).strftime('%Y%-m%-d %H:%M:%S')
    
    # Ensure more than 50% have user_action_type 5
    if i < 0.51 * num_rows:
        user_action_type = 5
    # Ensure more than 5% have user_action_type 3
    elif i < 0.56 * num_rows:
        user_action_type = 3
    else:
        user_action_type = random.randint(1, 10)
    
    rows.append([transaction_uuid, user_id, user_action_type, update_date_time])

# Write to CSV
with open('data/source_a.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['transaction_uuid', 'user_id', 'user_action_type', 'update_date_time'])
    writer.writerows(rows)

print("CSV file 'source_a.csv' generated successfully.")