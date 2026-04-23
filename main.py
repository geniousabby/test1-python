
"""
Robot Delivery game

"""

# Assign areas using a dictionary
delivery_area = {"Downtown": 1, "Suburbs": 2, "Industrial": 3}


# Get 3 robot names
def name_area1():
    """
    Gets name and area of robot 1.
    
    """

    while True:

        n1 = input("Enter robot name: ").strip().title()
        a1 = input("Choose a delivery zone for Apex (Downtown, Suburbs, Industrial): ").strip().title()
                
        if a1 == "Downtown":
            delivery_area =["Downtown"] = n1
            return delivery_area

        elif a1 == "Suburbs":
            delivery_area =["Suburbs"] = n1
            return delivery_area
        
        elif a1 == "Industrial":
            delivery_area =["Industrial"] = n1
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
            delivery_area =["Downtown"] = n2
            return delivery_area

        elif a2 == "Suburbs":
            delivery_area =["Suburbs"] = n2
            return delivery_area
        
        elif a2 == "Industrial":
            delivery_area =["Industrial"] = n2
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
            delivery_area =["Downtown"] = n3
            return delivery_area

        elif a3 == "Suburbs":
            delivery_area =["Suburbs"] = n3
            return delivery_area
        
        elif a3 == "Industrial":
            delivery_area =["Industrial"] = n3
            return delivery_area

        else:
            print("Please enter a valid location.")



# Get total delivery distance (1-500km)
def distance():


# Get individual cargo weight (1-50kg)
def weight():


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