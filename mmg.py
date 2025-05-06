"""
Name: Julio Maldonado
Class: Programming Fundamentals
Date: 05/5/2025
Program Name: PCCC Palace Hotel Billing (Functions Version)
Description: This program computes and prints billing statements for PCCC Palace Hotel customers using modular functions.
"""

from random import randint

def setdata():
    """
    Reads customer's name, number of days stayed, and room number.
    Returns:
    name (str), days (int), room (int)
    """
    name = input("The customer name please: ")
    days = int(input("Number of Days in the Hotel: "))
    room = int(input("Room Number: "))
    return name, days, room

def setroom(room_number, days):
    """
    Determines room type and calculates room charges.
    Args: room_number (int), days (int)
    Returns: room_type (str), room_charges (float)
    """
    SINGLE_ROOM_RATE = 225.00
    FAMILY_ROOM_RATE = 325.00
    SUITE_ROOM_RATE = 550.00

    last_digits = room_number % 100

    if last_digits <= 9:
        room_type = "Single Room"
        rate = SINGLE_ROOM_RATE
    elif last_digits <= 19:
        room_type = "Family Room"
        rate = FAMILY_ROOM_RATE
    else:
        room_type = "Suite"
        rate = SUITE_ROOM_RATE

    room_charges = rate * days
    return room_type, room_charges

def setnet(days):
    """
    Handles internet usage menu and calculates internet charges.
    Args: days (int)
    Returns: net_type (str), net_charges (float)
    """
    WIFI_RATE = 9.95
    CABLE_RATE = 5.95

    usage = input("Internet Usage (Y/N): ").strip().lower()
    net_type = "None"
    net_charges = 0.0

    if usage == 'y':
        print("\n\tInternet Access Usage")
        print("1 – Wi-Fi connection")
        print("2 - Cable")
        choice = input("Enter Choice 1 or 2: ").strip().lower()
        if choice in ['1', 'w']:
            net_type = "WiFi"
            net_charges = WIFI_RATE * days
        elif choice in ['2', 'c']:
            net_type = "Cable"
            net_charges = CABLE_RATE * days

    return net_type, net_charges

def settv(days):
    """
    Handles TV usage menu and calculates TV charges.
    Args: days (int)
    Returns: tv_type (str), tv_charges (float)
    """
    CABLE_TV_RATE = 9.95
    BASIC_TV_RATE = 2.95

    usage = input("\nTV Usage (Y/N): ").strip().lower()
    tv_type = "None"
    tv_charges = 0.0

    if usage == 'y':
        print("\n\tTV Usage")
        print("1 - Cable")
        print("2 - Basic Channels")
        choice = input("Enter Choice 1 or 2: ").strip().lower()
        if choice in ['1', 'c']:
            tv_type = "Cable"
            tv_charges = CABLE_TV_RATE * days
        elif choice in ['2', 'b']:
            tv_type = "Basic"
            tv_charges = BASIC_TV_RATE * days

    return tv_type, tv_charges

def findtotal(room_charges, net_charges, tv_charges):
    """
    Calculates the total charges before tax.
    Args: room_charges (float), net_charges (float), tv_charges (float)
    Returns: total_charges (float)
    """
    total_charges = room_charges + net_charges + tv_charges
    return total_charges

def heading(name, room, days, roomtype):
    """
    Prints the hotel heading and customer information.
    Args: name (str), room (int), days (int), roomtype (str)
    Returns: None
    """
    invoice_number = randint(100, 999)
    print("\nPCCC Palace Hotel")
    print(f"\n{name}'s Billing Statement\tRoom : {room}\tInvoice#: {invoice_number}")
    print(f"\nNumber of days in hotel:  {days}\t\ta {roomtype}")

def output(roomcharges, netcharges, nettype, tvcharges, tvtype):
    """
    Prints room, internet, and TV charges.
    Args: roomcharges (float), netcharges (float), nettype (str), tvcharges (float), tvtype (str)
    Returns: None
    """
    print(f"\nRoom Charges\t\t${roomcharges:,.2f}")
    print(f"\nInternet Charges\t({nettype})\t${netcharges:,.2f}")
    print(f"\nTelevision Charges\t({tvtype})\t${tvcharges:,.2f}")

def footing(totalcharges):
    """
    Prints total charges, taxes, and total due.
    Args: totalcharges (float)
    Returns: None
    """
    TAX_RATE = 0.035
    tax = totalcharges * TAX_RATE
    total_due = totalcharges + tax
    print(f"\nTotal Charges\t\t${totalcharges:,.2f}")
    print(f"\nLocal Taxes\t\t${tax:,.2f}")
    print(f"\n\tTotal Due\t${total_due:,.2f}")
    print("\nThank you for using PCCC Palace Hotel. Hope to see you again.")

from random import randint

def main():
    name, days, room = setdata()
    roomtype, roomcharges = setroom(room,days)
    nettype, netcharges = setnet(days)
    tvtype, tvcharges = settv(days)
    totalcharges = findtotal(roomcharges, netcharges, tvcharges)
    heading(name, room, days, roomtype)
    output( roomcharges, netcharges, nettype, tvcharges,tvtype)
    footing(totalcharges)

main()
main()
main()
input("\n\nPress Enter to Continue")

