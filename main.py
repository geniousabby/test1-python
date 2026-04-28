
"""
Robot Delivery game

"""

# Assign areas using a dictionary
delivery_area = {"Downtown": 1, "Suburbs": 2, "Industrial": 3}

robot = {}

distance = {}

weight = {}

weather = {"Clear": 1, "Rain": 2, "Storm":3}  


# Get 3 robot names
def name_area1():
    """
    Gets name and area of robot 1.
    
    """

    while True:

        n1 = input("Enter robot name: ").strip().title()
        a1 = input("Choose a delivery zone for Apex (Downtown, Suburbs, Industrial): ").strip().title()
                
        if a1 == "Downtown":
            robot[n1] = a1
            return delivery_area

        elif a1 == "Suburbs":
            robot[n1] = a1
            return delivery_area
        
        elif a1 == "Industrial":
            robot[n1] = a1
            return delivery_area

        else:
            print("Please enter a valid location.")



def name_area2():
    """
    Gets name and area of robot 2.
    
    """

    while True:
        n2 = input("Enter robot name: ").strip().title()
        a2 = input("Choose a delivery zone for Apex (Downtown, Suburbs, Industrial): ").strip().title()

        if a2 == "Downtown":
            robot[n2] = a2
            return delivery_area

        elif a2 == "Suburbs":
            robot[n2] = a2
            return delivery_area
        
        elif a2 == "Industrial":
            robot[n2] = a2
            return delivery_area

        else:
            print("Please enter a valid location.")



def name_area3():
    """
    Gets name and area of robot 3
    
    """

    while True:
        n3 = input("Enter robot name: ").strip().title()
        a3 = input("Choose a delivery zone for Apex (Downtown, Suburbs, Industrial): ").strip().title()

        if a3 == "Downtown":
            robot[n3] = a3
            return delivery_area

        elif a3 == "Suburbs":
            robot[n3] = a3
            return delivery_area
        
        elif a3 == "Industrial":
            robot[n3] = a3
            return delivery_area

        else:
            print("Please enter a valid location.")



# Get total delivery distance (5-500km)
def distance():
    """
    Get and check distance
    
    """

    while True:
        range = input("Enter total delivery distance (5-500 km): ")

        if range > 500:
            print("Number too high!")

        elif range < 5:
            print("Number too low!")

        elif range > 5 and < 500:
            return range

        else:
            print("Please enter a valid number.")
        


# Get individual cargo weight (1-50kg)
def weight():
    """
    Get weight of cargo
    
    """
    while True:
        weight = input("Enter weight of cargo (1-50 kg): ")

        if weight > 50:
            print("Number too high!")

        elif weight < 1:
            print("Number too low!")

        elif weight > 1 and < 50:
            return weight

        else:
            print("Please enter a valid number.")


# Get weather condition
def weather():


# Deployment status (safe or unsafe)
def deploy():


# Main function
def main():
    """
    Main function that calls the other functions.

    """

    name_area1()

    name_area2()

    name_area3()

    distance()

    weight()

    weather()

    deploy()



# Run main function
if __name__ == "__main__":
    main()