import machine
from switch import Switch

def main():

    switch_pin = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
    my_switch = Switch(switch_pin)

    while True:

        my_switch_new_value = False

        # Disable interrupts for a short time to read shared variable
        irq_state = machine.disable_irq()
        if my_switch.new_value_available:
            my_switch_value = my_switch.value
            my_switch_new_value = True
            my_switch.new_value_available = False
        machine.enable_irq(irq_state)

        # If my switch had a new value, print the new state
        if my_switch_new_value:
            if my_switch_value:
                print("Switch Opened")
            else:
                print("Switch Closed")

main()
