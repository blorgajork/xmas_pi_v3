from gpiozero import Button, LED
from time import sleep


global on
on = False

global speed
speed = 30

global mod
mod= 1

def add_speed():
    global speed
    if speed < 50:
        speed += mod
        if speed > 50:
            speed -= 40
    else:
        speed = 10
    print(50 - speed)

def sub_speed():
    global speed
    if speed > 10:
        speed -= mod
        if speed < 10:
            speed += 40
    else:
        speed = 50
    print(50 - speed)

def cycle_mod():
    global mod
    if mod < 10:
        mod+= 1
    else:
        mod= 0
    print(mod)

reds = [LED(17), LED(27), LED(22)]
greens = [LED(13), LED(6), LED(5)]
whites = [LED(23), LED(24)]
lights = [reds, greens, whites]


def turn_lights_off():
    global on
    on = False
    print(on)
    lights_off(lights)

def lights_off(lgroup):
    for group in lgroup:
        for light in group:
            light.off()



onButton, optionButton, leftButton, rightButton, modButton = Button(26), Button(12),  Button(25), Button(18), Button(4)
onButton.when_pressed, leftButton.when_pressed, rightButton.when_pressed, modButton.when_pressed = turn_lights_off, add_speed, sub_speed, cycle_mod


while True:
    sleep(1)
    print("         MERRY CHRISTMAS!         ")
    onButton.wait_for_press()

    print("LIGHTS ON")

    on = True


    while on:
        for group in lights:
            if not on:
                print("OFF")
                break
            for light in group:
                if not on:
                    print("OFF")
                    break
                else:
                    light.toggle()
                    sleep(speed/100)

    turn_lights_off()

