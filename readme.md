# Create cron job to run python (using pandas library) script from another python script

1. create python script to run
run.py

2. install requirements.txt to install dependencies
python install -r requirements.txt

3. Create scheduler.py another python script to run cron job

4. Run scheduler.py
python scheduler.py

5. It will print time on terminal after running scheduler.py script
Time will update on terminal when run.py script is executed

6. Check if cron is working
check time (it should update every minute) creation of pop.csv file