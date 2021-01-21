# College Football Twitter Bio Update Script

### Run this from the command line. 
This script will run every 5 minutes for as many cycles as specified in Command Line arg
On first cycle, it will gather each users (from the 'twthandle' variable) bio,
First and all subsequent cycles will then check to see if the users bio has changed. If it has,
it will direct message any user specified ('myself' variable) with the updated bio

### Used to track potential coaching changes in CFB offseason

### Example:
    'python3 main.py 2'
        - this will run 2 cycles. It will run once, wait 5 minutes, run again, then quit.

### Arguments:
    api_secret = Twitter Api Secret
    api_token = Twitter Api Token
    consumer_key = Twitter Api Consumer Key
    consumer_secret = Twitter Api Consumer Secret

    twthandle = list of Twitter handles to watch
    myself = your own twitter handle to DM if there are any updates

### Returns:
    none