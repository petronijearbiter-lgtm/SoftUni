from typing import get_origin

godine = int(input())

if godine <= 14:
    print("drink toddy")
elif godine <= 18:
    print("drink coke")
elif godine <= 21:
    print("drink beer")
else:
    print("drink whisky")
