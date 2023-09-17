# Papa's Freezeria Deluxe Bot
# papafunctions.py

# Imports
import mainfunctions as mf
import datafunctions as df


# Functions
def check_main_menu_open():
    mf.console_log("\nChecking if main menu is open...")

    main_menu_splash = mf.find_image("main_menu_splash", 0.9, None)
    if main_menu_splash is not None:
        mf.console_log("Main menu detected as open.")
        return True

    mf.console_log("Main menu not detected as open.")
    return False


def main_menu_start_game():
    mf.console_log("\nStarting game...")

    mf.console_log("Clicking \"Start Game\" button.")
    start_game_button = mf.find_image_center("main_menu_play_button", 0.9, None)
    if start_game_button is not None:
        mf.move_to(start_game_button[0], start_game_button[1])
        mf.click()
        mf.wait(1)
        return True

    mf.console_log("Failed to click \"Start Game\" button.")
    return False


def check_save_slot_open():
    mf.console_log("\nChecking if save slot selection is open...")

    save_slot_splash = mf.find_image("save_slot_open", 0.9, None)
    if save_slot_splash is not None:
        mf.console_log("Save slot selection detected as open.")
        return True

    mf.console_log("Save slot selection not detected as open.")
    return False


def load_save_slot():
    mf.console_log("\nLoading save slot...")

    while True:
        slot_to_open = input("Which save slot would you like to open? (1-3)\n> ")
        if slot_to_open in ["1", "2", "3"]:
            mf.console_log("Opening save slot " + slot_to_open + ".")
            # Click the save slot
            slot_location = df.get_data("save_slot_locations")[slot_to_open]
            mf.move_to(slot_location[0], slot_location[1])
            mf.click()
            mf.wait(1)
            break
        else:
            mf.console_log("Invalid save slot.")


def check_stats_start_button_open():
    mf.console_log("\nChecking for stats menu start button...")

    stats_start_button = mf.find_image("stats_page_start_button", 0.9, None)
    if stats_start_button is not None:
        mf.console_log("Stats menu start button found, clicking it.")
        mf.move_to(stats_start_button[0], stats_start_button[1])
        mf.click()
        mf.wait(1)
        return True

    mf.console_log("Stats menu start button not found.")
    return False


def check_take_order_button():
    mf.console_log("\nChecking for take order button...")

    take_order_button = mf.find_image_center("take_order_button", 0.9, None)
    if take_order_button is not None:
        mf.console_log("Take order button found, clicking it.")
        mf.move_to(take_order_button[0], take_order_button[1])
        mf.click()
        mf.wait(1)
        return True

    mf.console_log("Take order button not found.")
    return False


def check_station_1_grey():
    mf.console_log("\nChecking if station 1 is grey...")

    station_1_grey = mf.check_rgb(df.get_data("station_1_pixel_location")[0],
                                  df.get_data("station_1_pixel_location")[1], df.get_data("station_1_pixel_grey"))
    if station_1_grey:
        mf.console_log("Station 1 is grey.")
        return True

    mf.console_log("Station 1 is not grey.")
    return False


def get_ticket_cup_size():
    mf.console_log("\nGetting ticket cup size...")

    ticket_cup_size = mf.find_image("order_size_S", 0.9, df.get_data("ticket_cup_size_region"))
    if ticket_cup_size is not None:
        mf.console_log("Ticket cup size is small.")
        return "s"

    ticket_cup_size = mf.find_image("order_size_M", 0.9, df.get_data("ticket_cup_size_region"))
    if ticket_cup_size is not None:
        mf.console_log("Ticket cup size is medium.")
        return "m"

    ticket_cup_size = mf.find_image("order_size_L", 0.9, df.get_data("ticket_cup_size_region"))
    if ticket_cup_size is not None:
        mf.console_log("Ticket cup size is large.")
        return "l"

    mf.console_log("Ticket cup size not found.")
    return "n/a"


def get_ticket_blend_duration():
    mf.console_log("\nGetting ticket blend duration...")

    ticket_blend_duration = mf.check_rgb(df.get_data("ticket_blend_colour_location")[0],
                                         df.get_data("ticket_blend_colour_location")[1],
                                         df.get_data("blend_colour_regular"))
    if ticket_blend_duration:
        mf.console_log("Ticket blend duration is regular.")
        return "regular"

    ticket_blend_duration = mf.check_rgb(df.get_data("ticket_blend_colour_location")[0],
                                         df.get_data("ticket_blend_colour_location")[1],
                                         df.get_data("blend_colour_chunky"))
    if ticket_blend_duration:
        mf.console_log("Ticket blend duration is chunky.")
        return "chunky"

    ticket_blend_duration = mf.check_rgb(df.get_data("ticket_blend_colour_location")[0],
                                         df.get_data("ticket_blend_colour_location")[1],
                                         df.get_data("blend_colour_smooth"))
    if ticket_blend_duration:
        mf.console_log("Ticket blend duration is smooth.")
        return "smooth"

    mf.console_log("Ticket blend duration not found.")
    return "n/a"


def station_3_blend_bar_complete(duration):
    blend_colour = df.get_data("blend_colour_" + duration)
    blend_bar_complete = mf.check_rgb(df.get_data("station_3_blender_bar_location")[0],
                                      df.get_data("station_3_blender_bar_location")[1], blend_colour)
    if blend_bar_complete:
        mf.console_log("Blend bar is " + duration + ".")
        return True

    mf.console_log("Blend bar is not yet " + duration + ".")
    return False


def select_station_2_cup_size(cup_size):
    mf.console_log("\nSelecting cup size...")

    cup_size_found = False
    if cup_size == "s":
        cup_size_button = mf.find_image_center("station_2_button_S", 0.9, None)
        if cup_size_button is not None:
            mf.move_to(cup_size_button[0], cup_size_button[1])
            cup_size_found = True
    elif cup_size == "m":
        cup_size_button = mf.find_image_center("station_2_button_M", 0.9, None)
        if cup_size_button is not None:
            mf.move_to(cup_size_button[0], cup_size_button[1])
            cup_size_found = True
    elif cup_size == "l":
        cup_size_button = mf.find_image_center("station_2_button_L", 0.9, None)
        if cup_size_button is not None:
            mf.move_to(cup_size_button[0], cup_size_button[1])
            cup_size_found = True

    if cup_size_found:
        mf.click()
        mf.wait(1)
        return True

    mf.console_log("Cup size button could not be found, assuming unlock not yet purchased.")
    return False


def swap_station_2():
    mf.console_log("\nSwapping to station 2...")

    station_2_button = mf.find_image_center("station_2_coloured", 0.9, None)
    if station_2_button is not None:
        mf.move_to(station_2_button[0], station_2_button[1])
        mf.click()
        mf.wait(1)
        return True

    mf.console_log("Failed to click station 2 button.")
    return False


def dispense_bar_perfect():
    mf.console_log("\nChecking if dispense is perfect...")

    dispense_rgb = mf.check_rgb(df.get_data("dispense_bar_pixel_location")[0],
                                df.get_data("dispense_bar_pixel_location")[1], df.get_data("dispense_bar_pixel_colour"))
    if dispense_rgb:
        mf.console_log("Dispense bar is perfect, clicking button.")
        mf.move_to(df.get_data("dispense_button_pixel_location")[0], df.get_data("dispense_button_pixel_location")[1])
        mf.click()
        mf.wait(1)
        return True

    mf.console_log("Dispense was not perfect.")
    return False


def station_2_select_ingredient_1(confidence):
    mf.console_log("\nSelecting ingredient 1 with confidence {}...".format(round(confidence, 2)))

    ingredient_1_button = mf.find_image_center_in_region_from_screenshot(df.get_data("ticket_ingredient_1_region"),
                                                                         confidence,
                                                                         df.get_data("ingredient_1_selection_region"))
    if ingredient_1_button is not None:
        mf.move_to(ingredient_1_button[0], ingredient_1_button[1])
        mf.click()
        mf.wait(1)
        return True

    mf.console_log("Ingredient 1 button could not be found.")
    return False


def station_2_select_ingredient_2(confidence):
    mf.console_log("\nSelecting ingredient 2 with confidence {}...".format(round(confidence, 2)))

    ingredient_2_button = mf.find_image_center_in_region_from_screenshot(df.get_data("ticket_ingredient_2_region"),
                                                                         confidence,
                                                                         df.get_data("ingredient_2_selection_region"))
    if ingredient_2_button is not None:
        mf.move_to(ingredient_2_button[0], ingredient_2_button[1])
        mf.click()
        mf.wait(1)
        return True

    mf.console_log("Ingredient 2 button could not be found.")
    return False


def swap_station_3():
    mf.console_log("\nSwapping to station 3...")

    station_3_button = mf.find_image_center("station_3_coloured", 0.9, None)
    if station_3_button is not None:
        mf.move_to(station_3_button[0], station_3_button[1])
        mf.click()
        mf.wait(1)
        return True

    mf.console_log("Failed to click station 3 button.")
    return False


def station_3_move_cup_to_blender():
    mf.console_log("\nMoving cup to blender...")

    mf.move_to(df.get_data("station_3_cup_start_location")[0], df.get_data("station_3_cup_start_location")[1])
    mf.mouse_down()
    mf.move_to(df.get_data("station_3_blender_1_location")[0], df.get_data("station_3_blender_1_location")[1])
    mf.mouse_up()


def station_3_move_cup_to_toppings():
    mf.console_log("\nMoving cup to toppings...")

    mf.move_to(df.get_data("station_3_blender_1_location")[0], df.get_data("station_3_blender_1_location")[1])
    mf.mouse_down()
    mf.move_to(df.get_data("station_3_cup_end_location")[0], df.get_data("station_3_cup_end_location")[1])
    mf.mouse_up()


def station_3_hold_boost_button():
    mf.console_log("\nHolding boost button...")

    mf.move_to(df.get_data("station_3_blender_1_boost_location")[0],
               df.get_data("station_3_blender_1_boost_location")[1])
    mf.mouse_down()


def station_3_release_boost_button():
    mf.console_log("\nReleasing boost button...")
    mf.mouse_up()


def station_4_select_ingredient_whipped_cream(confidence):
    mf.console_log("\nSelecting whipped cream with confidence {}...".format(round(confidence, 2)))

    whipped_cream_button = mf.find_image_center_in_region_from_screenshot(df.get_data("ticket_whipped_cream_region"),
                                                                          confidence,
                                                                          df.get_data("station_4_toppings_region"))
    if whipped_cream_button is not None:
        mf.move_to(whipped_cream_button[0], whipped_cream_button[1])
        mf.mouse_down()
        mf.move_to(df.get_data("station_4_toppings_drop_start_location")[0],
                   df.get_data("station_4_toppings_drop_start_location")[1])
        mf.mouse_up()
        return True

    mf.console_log("Whipped cream button could not be found.")
    return False


def station_4_select_ingredient_syrup_1(confidence):
    mf.console_log("\nSelecting syrup 1 with confidence {}...".format(round(confidence, 2)))

    syrup_1_button = mf.find_image_center_in_region_from_screenshot(df.get_data("ticket_syrup_1_region"),
                                                                    confidence,
                                                                    df.get_data("station_4_toppings_region"))
    if syrup_1_button is not None:
        mf.move_to(syrup_1_button[0], syrup_1_button[1])
        mf.mouse_down()
        mf.move_to(df.get_data("station_4_toppings_drop_start_location")[0],
                   df.get_data("station_4_toppings_drop_start_location")[1])
        mf.mouse_up()
        return True

    mf.console_log("Syrup 1 button could not be found.")
    return False


def station_4_select_ingredient_syrup_2(confidence):
    mf.console_log("\nSelecting syrup 2 with confidence {}...".format(round(confidence, 2)))

    syrup_2_button = mf.find_image_center_in_region_from_screenshot(df.get_data("ticket_syrup_2_region"),
                                                                    confidence,
                                                                    df.get_data("station_4_toppings_region"))
    if syrup_2_button is not None:
        mf.move_to(syrup_2_button[0], syrup_2_button[1])
        mf.mouse_down()
        mf.move_to(df.get_data("station_4_toppings_drop_start_location")[0],
                   df.get_data("station_4_toppings_drop_start_location")[1])
        mf.mouse_up()
        return True

    mf.console_log("Syrup 2 button could not be found.")
    return False


def station_4_select_shaker_1(confidence):
    mf.console_log("\nSelecting shaker 1 with confidence {}...".format(round(confidence, 2)))

    shaker_1_button = mf.find_image_center_in_region_from_screenshot(df.get_data("ticket_shaker_1_region"),
                                                                     confidence,
                                                                     df.get_data("station_4_toppings_region"))
    if shaker_1_button is not None:
        mf.move_to(shaker_1_button[0], shaker_1_button[1])
        mf.mouse_down()
        mf.move_to(df.get_data("station_4_toppings_drop_start_location")[0],
                   df.get_data("station_4_toppings_drop_start_location")[1])
        mf.mouse_up()
        return True

    mf.console_log("Shaker 1 button could not be found.")
    return False


def station_4_select_shaker_2(confidence):
    mf.console_log("\nSelecting shaker 2 with confidence {}...".format(round(confidence, 2)))

    shaker_2_button = mf.find_image_center_in_region_from_screenshot(df.get_data("ticket_shaker_2_region"),
                                                                     confidence,
                                                                     df.get_data("station_4_toppings_region"))
    if shaker_2_button is not None:
        mf.move_to(shaker_2_button[0], shaker_2_button[1])
        mf.mouse_down()
        mf.move_to(df.get_data("station_4_toppings_drop_start_location")[0],
                   df.get_data("station_4_toppings_drop_start_location")[1])
        mf.mouse_up()
        return True

    mf.console_log("Shaker 2 button could not be found.")
    return False


def station_4_select_shaker_3(confidence):
    mf.console_log("\nSelecting shaker 3 with confidence {}...".format(round(confidence, 2)))

    shaker_3_button = mf.find_image_center_in_region_from_screenshot(df.get_data("ticket_shaker_3_region"),
                                                                     confidence,
                                                                     df.get_data("station_4_toppings_region"))
    if shaker_3_button is not None:
        mf.move_to(shaker_3_button[0], shaker_3_button[1])
        mf.mouse_down()
        mf.move_to(df.get_data("station_4_toppings_drop_start_location")[0],
                   df.get_data("station_4_toppings_drop_start_location")[1])
        mf.mouse_up()
        return True

    mf.console_log("Shaker 3 button could not be found.")
    return False


def station_4_drop_topping_over_cup():
    mf.console_log("\nDropping topping over cup...")

    for i in range(2):
        mf.mouse_down()
        mf.move_to_duration(df.get_data("station_4_toppings_drop_end_location")[0],
                            df.get_data("station_4_toppings_drop_end_location")[1],
                            0.55)
        mf.move_to_duration(df.get_data("station_4_toppings_drop_start_location")[0],
                            df.get_data("station_4_toppings_drop_start_location")[1],
                            0.55)
        mf.mouse_up()
    mf.mouse_up()


def station_4_select_shaker_section():
    mf.console_log("\nSelecting shaker section...")

    mf.move_to(df.get_data("station_4_toppings_shaker_location")[0],
               df.get_data("station_4_toppings_shaker_location")[1])
    mf.click()
    mf.wait(1)
    return True


def station_4_select_loose_section():
    mf.console_log("\nSelecting loose section...")

    loose_section_button = mf.find_image_center("station_4_toppings_loose_location", 0.9, None)
    if loose_section_button is not None:
        mf.move_to(loose_section_button[0], loose_section_button[1])
        mf.click()
        mf.wait(1)
        return True

    mf.console_log("Loose section button could not be found.")
    return False