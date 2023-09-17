# Papa's Freezeria Deluxe Bot
# main.py

# By: xP9nda, Sat 16 September 2023
# Description: A bot that plays Papa's Freezeria Deluxe for you.

# Recommendations:
# - play the game in fullscreen mode

# Imports
import mainfunctions as mf
import papafunctions as pf
import datafunctions as df


# Functions
def run():
    mf.welcome_log()
    df.load_data()

    # Check if main menu is open
    main_menu_open = pf.check_main_menu_open()

    # If the main menu is open, start the game
    if main_menu_open:
        pf.main_menu_start_game()

    # Check if save slot selection is open
    save_slot_open = pf.check_save_slot_open()

    # If the save slot selection is open, load the save slot
    if save_slot_open:
        pf.load_save_slot()

    # Look for the stats page start button
    pf.check_stats_start_button_open()

    # Check for the take order button
    waiting_for_new_order = True
    while waiting_for_new_order:
        mf.wait(1)
        take_order_button = pf.check_take_order_button()

        # If the take order button is found and clicked, wait for the order to be taken
        if take_order_button:
            take_order_active = True
            mf.console_log("\nTake order is now active...")

            # Wait until the station 1 button is no longer grey
            while take_order_active:
                station_1_grey = pf.check_station_1_grey()
                if station_1_grey:
                    mf.wait(1.25)
                else:
                    take_order_active = False

            # Ticket has been given out, switch to station 2
            pf.swap_station_2()

            # Get the cup size of the ticket
            cup_size = pf.get_ticket_cup_size()

            # If the cup size is valid, switch to station 2
            if cup_size in ["s", "m", "l"]:
                # Select the appropriate cup size
                pf.select_station_2_cup_size(cup_size)

            # Check if the ice cream is ready to be dispensed
            while True:
                dispense_state = pf.dispense_bar_perfect()
                if dispense_state:
                    break

            # Wait for a slight duration
            mf.wait(1)

            # Select the first ingredient
            ingredient_confidence = 0.85
            while True:
                ingredient_1 = pf.station_2_select_ingredient_1(ingredient_confidence)
                ingredient_confidence -= 0.025
                # Dispense the first ingredient
                if ingredient_1:
                    while True:
                        dispense_state = pf.dispense_bar_perfect()
                        if dispense_state:
                            break
                    break

            # Wait for a slight duration
            mf.wait(2)

            # Select the second ingredient
            ingredient_confidence = 1
            while True:
                ingredient_2 = pf.station_2_select_ingredient_2(ingredient_confidence)
                ingredient_confidence -= 0.025
                # Dispense the second ingredient
                if ingredient_2:
                    while True:
                        dispense_state = pf.dispense_bar_perfect()
                        if dispense_state:
                            break
                    break

            # Ingredients have been added, switch to station 3
            pf.swap_station_3()

            # Move the cup to the blender
            pf.station_3_move_cup_to_blender()

            # Begin holding the boost button
            pf.station_3_hold_boost_button()

            # Check for the appropriate blend duration to be reached
            blend_duration = pf.get_ticket_blend_duration()

            # Wait for the blender to meet the blend duration
            while True:
                blender_state = pf.station_3_blend_bar_complete(blend_duration)
                mf.wait(0.5)
                # Stop holding the boost button when the blender is done
                if blender_state:
                    pf.station_3_release_boost_button()
                    break

            # Move the cup to the toppings station
            pf.station_3_move_cup_to_toppings()

            # Wait for a slight duration
            mf.wait(0.75)

            # Select the whipped cream
            ingredient_confidence = 1
            while True:
                ingredient_whipped_cream = pf.station_4_select_ingredient_whipped_cream(ingredient_confidence)
                ingredient_confidence -= 0.025
                # Drop the whipped cream over the cup
                if ingredient_whipped_cream:
                    pf.station_4_drop_topping_over_cup()
                    break

            # Select syrup 1
            ingredient_confidence = 1
            while True:
                ingredient_syrup = pf.station_4_select_ingredient_syrup_1(ingredient_confidence)
                ingredient_confidence -= 0.025
                # Check that a syrup actually exists
                if ingredient_confidence < 0.6:
                    mf.console_log("Syrup 1 not found, skipping...")
                    break
                # Drop the whipped cream over the cup
                if ingredient_syrup:
                    pf.station_4_drop_topping_over_cup()
                    break

            # Select syrup 2
            ingredient_confidence = 1
            while True:
                ingredient_syrup = pf.station_4_select_ingredient_syrup_2(ingredient_confidence)
                ingredient_confidence -= 0.025
                # Check that a syrup actually exists
                if ingredient_confidence < 0.6:
                    mf.console_log("Syrup 2 not found, skipping...")
                    break
                # Drop the whipped cream over the cup
                if ingredient_syrup:
                    pf.station_4_drop_topping_over_cup()
                    break

            # Select the shaker toppings section
            pf.station_4_select_shaker_section()

            # Select shaker 1
            ingredient_confidence = 1
            while True:
                ingredient_shaker = pf.station_4_select_shaker_1(ingredient_confidence)
                ingredient_confidence -= 0.025
                # Check that a shaker actually exists
                if ingredient_confidence < 0.75:
                    mf.console_log("Shaker 1 not found, skipping...")
                    break
                # Drop the whipped cream over the cup
                if ingredient_shaker:
                    pf.station_4_drop_topping_over_cup()
                    break

            # Select shaker 2
            ingredient_confidence = 1
            while True:
                ingredient_shaker = pf.station_4_select_shaker_2(ingredient_confidence)
                ingredient_confidence -= 0.025
                # Check that a shaker actually exists
                if ingredient_confidence < 0.75:
                    mf.console_log("Shaker 2 not found, skipping...")
                    break
                # Drop the whipped cream over the cup
                if ingredient_shaker:
                    pf.station_4_drop_topping_over_cup()
                    break

            # Select shaker 3
            ingredient_confidence = 1
            while True:
                ingredient_shaker = pf.station_4_select_shaker_3(ingredient_confidence)
                ingredient_confidence -= 0.025
                # Check that a shaker actually exists
                if ingredient_confidence < 0.75:
                    mf.console_log("Shaker 3 not found, skipping...")
                    break
                # Drop the whipped cream over the cup
                if ingredient_shaker:
                    pf.station_4_drop_topping_over_cup()
                    break


# Main
if __name__ == '__main__':
    run()
