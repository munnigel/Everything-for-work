import json
import random
from datetime import datetime, timedelta

# Function to generate random datetime
def random_date(start, end):
    return start + (end - start) * random.random()

num_messages = 40000
messages = []

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Create base data with no errors
for _ in range(num_messages):
    transaction_uuid = random.randint(1, 10**10)  # Generate a random integer for transaction_uuid
    user_id = str(random.randint(1, 1000))
    user_action_type = str(random.randint(1, 10))
    update_date_time = random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S')

    message = {
        "transaction_uuid": transaction_uuid,
        "user_id": user_id,
        "user_action_type": user_action_type,
        "update_date_time": update_date_time
    }

    messages.append(message)

# Write to JSON lines file
with open('events_PreVOS_correct.jsonl', 'w') as file:
    for message in messages:
        json.dump(message, file)
        file.write('\n')

print("JSON lines file 'events_PreVOS_correct.jsonl' generated successfully.")