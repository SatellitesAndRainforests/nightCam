from time import strftime

def captureTime():

    # dateTime = strftime("%d %m %y  %I %M %p");
    currentHours = strftime("%H");
    hour = int(currentHours);

    if ( ( hour >= 17 ) or ( hour < 6 ) ):
        return True;
    else:
        return False;

returned = captureTime();

if ( returned ):
    print("capturing");
else:
    print("not capturing");



