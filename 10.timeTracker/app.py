import time

print(time.time())

# Request the name of the job
task = input("Enter name of the task : ")

# Get start time of the app and job
task_start = time.time()
app_start = task_start

# Loop and check if the job is end

try:
    while True: 

        input("Press enter when you finish the task...")

        # diff the time and show the time taking for a job

        task_time = round(time.time() - task_start,2)
        print(f"# {task} was taking {task_time}s")   

        # check if user want to start another job and ask for the job name if needed
        task = input("Enter job name if you want to start new task : ")

    # end the job on keyboard interrupt as well for Ctrl+C Exist
except KeyboardInterrupt:
    print("\nQuitting...")
# create a shell/bat file to run from anywhere

# chmod +x in linux to execute the script