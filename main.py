
"""
Robot Delivery game

"""

# Assign areas using a dictionary
delivery_area = {"Downtown": 1, "Suburbs": 2, "Industrial": 3}

robot = {}

# Get 3 robot names
def get_robot_info(num):
    """
    Gets name and area of robot 1.
    
    """

    while True:
        name = input(f"Enter name for robot {num}: ").strip().title()
        area = input("Choose a delivery zone (Downtown, Suburbs, Industrial): ").strip().title()

        if area in delivery_area:
            robot[name] = area
            return name, area
        else:
            print("Invalid area. Try again.")


# Get total delivery distance (5-500km)
def get_distance():
    """
    Get and check distance
    
    """

    while True:
        try:
            d = int(input("Enter total delivery distance (5–500 km): "))
            if 5 <= d <= 500:
                return d
            print("Distance must be between 5 and 500.")
        except ValueError:
            print("Enter a valid number.")


# Get individual cargo weight (1-50kg)
def get_weight(num):
    """
    Get weight of cargo
    
    """

    while True:
        try:
            w = int(input(f"Enter cargo weight for robot {num} (1–50 kg): "))
            if 1 <= w <= 50:
                return w
            print("Weight must be between 1 and 50.")
        except ValueError:
            print("Enter a valid number.")


# Get weather condition
def get_weather():
    """
    Get weather condition
    
    """

    while True:
        w = input("Enter weather condition (Clear, Rain, Storm): ").strip().title()
        if w in ["Clear", "Rain", "Storm"]:
            return w
        print("Invalid weather condition.")


def deploy(condition):
    """
    Gives deploy message
    
    """

    if condition == "Storm":
        print("Deployment status: Unsafe!")
    elif condition == "Rain":
        print("Deployment status: Caution!")
    else:
        print("Deployment status: Safe!")


def main():
    """
    Main function that calls the other functions.

    """

    print("\nRobot Delivery Game\n")

    get_robot_info(1)
    get_robot_info(2)
    get_robot_info(3)

    distance = get_distance()
    print("Total delivery distance:", distance)

    w1 = get_weight(1)
    w2 = get_weight(2)
    w3 = get_weight(3)

    print("Cargo weights:", w1, w2, w3)

    weather = get_weather()
    print("Weather condition:", weather)

    deploy(weather)


if __name__ == "__main__":
    main()
