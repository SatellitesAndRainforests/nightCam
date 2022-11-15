from datetime import datetime

baseline_new_moon = datetime(2022, 2, 1)    # A new moon at 00:46am
now = datetime.now()
difference = float((now - baseline_new_moon).days) - 0.0319 #Days differnce as a float
                                                            #subtract 46 mins 3.19% of a day
modulos = difference % 29.53    # Subtract all full moon cycles, (29.53 days, Wikipedia)
                                # remander is current mooncycle phase progress

moonphase = ""

if (modulos < 1.84 or modulos >= 27.68 ):   # This is the only real one that needs to be 
                                            # precise. +/- 19 hour variation.  
    moonphase = "new moon"                  # Each is 29.53 / 8 (the 8 phases)
elif (modulos >= 1.84 and modulos < 5.53):
    moonphase = "cresent (right)"

elif (modulos >= 5.53 and modulos < 9.22):
    moonphase = "half moon (right)"

elif (modulos >= 9.22 and modulos < 12.91):
    moonphase = "3/4 moon (right)"

elif (modulos >= 12.91 and modulos < 16.61):
    moonphase = "full moon"

elif (modulos >= 16.61 and modulos < 20.30):
    moonphase = "3/4 moon (left)"

elif (modulos >= 20.30 and modulos < 23.99):
    moonphase = "half moon (left)" 

elif (modulos >= 23.99 and modulos < 27.68):
    moonphase = "cresent (left)"

print(moonphase)
