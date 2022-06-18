# Create a beep at any frequency (for me it is 37hz), and last for 0 second (You will not hear the beep sound since it last for 0 second)
# For Airpod, best time is 20 sec, but you can use this strategy to prevent other bluetooth speaker sleeping. 

import winsound
import time

while True:
    winsound.Beep(37, 0)
    time.sleep(20) 
