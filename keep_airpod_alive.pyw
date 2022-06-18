# will create a beeb at 37hz, and last for 0 second. 
# 37hz is the lowest you can set. You can pick any frequency

import winsound
import time

while True:
    winsound.Beep(37, 0)
    time.sleep(20) # best time is 20 sec. 
