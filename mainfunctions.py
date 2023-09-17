# Papa's Freezeria Deluxe Bot
# mainfunctions.py

# Imports
import pyautogui
import time
import random
from PIL import ImageGrab

# Constants
IMAGE_PATH = "images/"
IMAGE_EXT = ".png"


# Functions
def welcome_log():
    console_log("Hey! Welcome to the Papa's Freezeria Deluxe Bot!")
    console_log("This bot is developed by xP9nda.")
    console_log("\nIf you have any suggestions or questions please ask on the GitHub issues page.")
    console_log("\nIt is recommended that you play in fullscreen on a 1920x1080 monitor, or issues with mouse "
                "coordinates will occur.")
    console_log("You can edit the locations for various buttons and actions in the data/settings.json file to match "
                "your own needs.")
    console_log("\n--------")


def click():
    pyautogui.click()


def mouse_down():
    pyautogui.mouseDown()


def mouse_up():
    pyautogui.mouseUp()


def move_to(x, y):
    pyautogui.moveTo(x, y)


def move_to_duration(x, y, duration):
    pyautogui.moveTo(x, y, duration=duration)


def console_log(message):
    print(message)


def wait(seconds):
    time.sleep(seconds)


def find_image(image_name, confidence, region):
    return pyautogui.locateOnScreen(IMAGE_PATH + image_name + IMAGE_EXT, confidence=confidence, region=region)


def find_image_center(image_name, confidence, region):
    return pyautogui.locateCenterOnScreen(IMAGE_PATH + image_name + IMAGE_EXT, confidence=confidence, region=region)


def check_rgb(x, y, rgb):
    image = ImageGrab.grab((x, y, x + 1, y + 1))
    image_rgb = image.getpixel((0, 0))
    if image_rgb[0] == rgb[0] and image_rgb[1] == rgb[1] and image_rgb[2] == rgb[2]:
        return True

    return False


def find_image_center_in_region_from_screenshot(region_to_screenshot, confidence, region_to_find_in):
    # "temp/img-" + str(random.randint(1, 500000)) + ".png",
    image = pyautogui.screenshot("temp/img-" + str(random.randint(1, 500000)) + ".png",region=(
        region_to_screenshot[0], region_to_screenshot[1], region_to_screenshot[2] - region_to_screenshot[0],
        region_to_screenshot[3] - region_to_screenshot[1]))

    return pyautogui.locateCenterOnScreen(image, confidence=confidence, region=region_to_find_in)
