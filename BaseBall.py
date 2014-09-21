__author__ = 'newScanTron'
import random


class BaseBall():
    pitch_types = {1: "fastball", 2: "change up", 3: "curve", 4: "slider", 5: "cutter", 6:"splitter", 7:"screwball"}

    def __init__(self):
        print("i do stuff like get thrown")
        speed = random.randint(75, 102)
        print(speed)
        #some logic for pitch type
        pitch_types = {1: "fastball", 2: "change up", 3: "curve", 4: "slider",
                       5: "cutter", 6: "splitter", 7: "screwball"}
        pitch_type = random.randint(1, 7)
        print(pitch_types[pitch_type])
        # some logic to decide if it was a strike or a ball
        strike_or_ball = random.randint(1, 10)
        is_strike = True
        if strike_or_ball < 7:
            print("strike")
        elif strike_or_ball < 10:
            print("ball")
            is_strike = False
        elif strike_or_ball >= 10:
            print("you got hit by a pitch son")
            is_strike = False
        else:
            print("WTF mate")
        pitch_info = [speed, pitch_type, is_strike]
