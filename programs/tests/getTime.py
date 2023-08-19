import os;
from time import strftime;
from time import sleep;

def captureTime():

    # dateTime = strftime("%d %m %y  %I %M %p");
    currentHours = strftime("%H");
    hour = int(currentHours);

    startTime = 21;
    endTime = 6;

    if ( ( hour >= startTime ) or ( hour < endTime ) ):
        return True;
    else:
        print("capture time is between: " + str(startTime) + " and " + str(endTime) );
        print("current time: ")
        dateCommand = ('date');
        os.system( dateCommand );
        sleep(1);
        return False;

returned = captureTime();

if ( returned ):
    print("capturing");
else:
    print("not capturing");



