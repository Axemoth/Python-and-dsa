import time

max_attempts = 5
wait_time = 1
attempts = 1

while attempts <= max_attempts:
    print(f"Attempts:{attempts},wait-time:{wait_time}")
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2

print("You have reached maximum tries")