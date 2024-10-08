import json
import uuid
import random
from datetime import datetime, timedelta

# Function to generate random datetime
def random_date(start, end):
    return start + (end - start) * random.random()
 
num_messages = 40000
messages = []

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Introducing error types with their respective chances 
error_chance = {
    'user_id_not_int': 0.05,  # 5% chance
    'duplicate': 0.02,       # 2% chance
    'missing_field': 0.02,   # 2% chance
    'wrong_date_format': 0.01 # 1% chance
}

# Track seen transaction UUIDs for duplicates
# seen_transaction_uuids = set()

# Create base data with no errors
for _ in range(num_messages):
    transaction_uuid = str(uuid.uuid4())
    user_id = str(random.randint(1, 1000))
    user_action_type = str(random.randint(1, 10))
    update_date_time = random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S')
    update_date_time = random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S')

    message = {
        "transaction_uuid": transaction_uuid,
        "user_id": user_id,
        "user_action_type": user_action_type,
        "update_date_time": update_date_time
        "transaction_uuid": transaction_uuid,
        "user_id": user_id,
        "user_action_type": user_action_type,
        "update_date_time": update_date_time
    }

    # Introduce errors based on the specified chances
    if random.random() < error_chance['user_id_not_int']:
        message["user_id"] = "abc"  # Not castable to int
    
    # if random.random() < error_chance['duplicate']:
    #     if seen_transaction_uuids:
    #         message["transaction_uuid"] = random.choice(list(seen_transaction_uuids))  # Duplicate record
    
    if random.random() < error_chance['missing_field']:
        message.pop("User_action_type")  # Remove a field

    if random.random() < error_chance['wrong_date_format']:
        message["Update_date_time"] = "2023-13-40 99:99:99"  # Incorrect date format

    # seen_transaction_uuids.add(transaction_uuid)
    messages.append(message)

# Write to JSON lines file
with open('events_PreVOS_correct.jsonl', 'w') as file:
    for message in messages:
        json.dump(message, file)
        file.write('\n')

print("JSON lines file 'events_PreVOS_correct.jsonl' generated successfully.")