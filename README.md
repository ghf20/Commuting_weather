# Commandline application for Sending Weather Forecasts via SMS with the Twilio API

### Installation & Instructions (Linux Only):

1.
   Ensure you have a Twilio Account. If you are a student, Github has a $50 credit for student twilio accounts
   https://education.github.com/pack

2.
   register for the free weather API on RapidAPI hub
   https://rapidapi.com/weatherapi/api/weatherapi-com/

3. install dependiencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Fill in API key and Twilio API.

5. run main.py with:
   
   ```bash
   python3 main.py
   ```
   or
   ```bash
   chmod +x main.py && ./main.py
   ```

6. register main.py to schedule execution

   Before execute the command below, be sure to change directory to the path 'main.py' is located
    
   Modify the time and date fields described as * * * * *
    
   ```bash
   echo "* * * * * ${USER}" $(which python3) $(pwd)\/main.py | tee -a /etc/crontab
   
   systemctl restart cron.service
   ```
  
     The time and date fields:

     To run main.py at 09:00 AM everyday


     ```bash
     echo "0 9 * * * ${USER}" $(which python3) $(pwd)\/main.py | tee -a /etc/crontab
      ```


     To run main.py at 02:15 PM on the first of every month:

         
     ```bash
     echo "15 14 1 * * ${USER}" $(which python3) $(pwd)\/main.py | tee -a /etc/crontab
     ```

      To check if job is scheduled for user (replace username):
      
      ```bash
      sudo crontab -u [username] -l
      ```
      
      or if root/dont have root privileges:
         
      ```bash
      less /etc/crontab
      ```
 
      Further detail refer https://man7.org/linux/man-pages/man5/crontab.5.html
