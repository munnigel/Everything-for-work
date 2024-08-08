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

# Initialize counters for user action types
count_type_5 = 0
count_type_3 = 0

# Generate data with the conditions to test for DQC
for i in range(num_rows):
    transaction_uuid = str(uuid.uuid4())
    user_id = random.randint(1, 1000)
    update_date_time = random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S')

    # Set a random user action type
    user_action_type = random.randint(1, 10)

    # Ensure no more than 50% have user_action_type 5
    if user_action_type == 5 and count_type_5 >= 0.5 * num_rows:
        user_action_type = random.choice([x for x in range(1, 11) if x != 5 and (x != 3 or count_type_3 < 0.05 * num_rows)])
    elif user_action_type == 5:
        count_type_5 += 1

    # Ensure no more than 5% have user_action_type 3
    if user_action_type == 3 and count_type_3 >= 0.05 * num_rows:
        user_action_type = random.choice([x for x in range(1, 11) if x != 3 and (x != 5 or count_type_5 < 0.5 * num_rows)])
    elif user_action_type == 3:
        count_type_3 += 1

    rows.append([transaction_uuid, user_id, user_action_type, update_date_time])

# Shuffle rows to randomize the distribution of user_action_types
random.shuffle(rows)

# Write to CSV
with open('source_a_PreVOS_correct.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['transaction_uuid', 'user_id', 'user_action_type', 'update_date_time'])
    writer.writerows(rows)

print("CSV file 'source_a_PreVOS_correct.csv' generated successfully.")