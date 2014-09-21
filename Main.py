__author__ = 'newScanTron'
from BaseBall import *
from stack import *


ballCount = 0
ball_stack = stack()
user_input = input("how many pitches would you lik to throw?")
while ball_stack.size() < int(user_input):
    pitch = BaseBall()
    ball_stack.push(pitch)

while not ball_stack.isEmpty():
    print(ball_stack.pop())