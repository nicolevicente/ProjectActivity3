import urllib.parse
import requests

def again():

    #Additional Feature
    #Lets user to try again

    again = input("\nWould you like to try again? (Y/N): ")

    if again == "Y" or again == "y":
        print("\n")
        intro()

    elif again == "N" or again == "n":
        print("Thank you and keep safe!\n")

    else:
        print("Wrong input!")

def intro():
    #Additional Feature
    #Places with lockdown restrictions within the Philippines as of October 8, 2021. (array)
    #This will check if user starts from a place with lockdown restrictions.
    #Add another feature (to consider)
    #Add/Delete regions/cities (depending on new regulations imposed by the IATF)

    MECQ = ["Apayao", "Kalinga", "Batanes", "Bataan", "Bulacan", "Cavite", "Lucena",
    "Rizal", "Laguna", "Naga", "Bicol", "Iloilo Province"]

    GCQ_heightened = ["Abra", "Baguio", "Ilocos Sur", "Pangasinan", "Cagayan", "Isabela", "Santiago",
    "Nueva Vizcaya", "Quirino",  "Quezon", "Batangas", "Bacolod", "Capiz", "Iloilo", "Lapu-Lapu",
    "Negros Oriental", "Bohol", "Zamboanga del Norte", "Zamboanga del Sur", "Cagayan de Oro", "Misamis Oriental", 
    "Davao del Norte", "Davao Occidental", "Davao de Oro", "Butuan", "Surigao del Sur"]

    GCQ_regular = ["Ilocos Norte", "Dagupan", "Benguet", "Ifugao", "Tarlac", "Mariduque", "Occidental Mindoro", "Oriental Mindoro",
    "Puerto Princesa", "Albay", "Camarines Norte", "Aklan", "Antique", "Guimaras", "Negros Occidental", "Cebu City", "Cebu Province",
    "Mandaue", "Siquijor", "Tacloban", "Zamboanga Sibugay", "Zamboanga", "Misamis Occidental", "Iligan",
    "Davao", "Davao Oriental", "Davao del Sur", "General Santos", "Sultan Kudarat", "Sarangani", "North Cotabato",
    "South Cotabato", "Agusan del Norte", "Agusan del Sur", "Surigao del Norte", "Dinagat Islands", "Cotabato", "Lanao del Sur"]

    not_MGCQ = MECQ + GCQ_heightened + GCQ_regular

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    orig = input("Enter your Starting Location: ")
    dest = input("Enter your Destination: ")

    if orig in MECQ and dest in MECQ:
        print("\nHi, " , name , "! You are travelling between: MECQ areas.")
        proceed(orig, dest)
    
    elif orig in GCQ_heightened and dest in GCQ_heightened:
        print("\nHi, " , name , "! You are travelling between: Heightened GCQ areas.")
        proceed(orig, dest)

    elif orig in GCQ_regular and dest in GCQ_regular:
        print("\nHi, " , name , "! You are travelling between: Regular GCQ areas.")
        proceed(orig, dest)

    elif orig not in not_MGCQ and dest not in not_MGCQ:
        print("\nHi, " , name , "! You are travelling between: MGCQ areas.")
        proceed(orig, dest)

    elif orig in not_MGCQ and dest not in not_MGCQ:
        interzone(name, age, orig, dest)

    elif orig not in not_MGCQ and dest in not_MGCQ:
        interzone(name, age, orig, dest)

def interzone(name, age, orig, dest):
    print("\n*****INTERZONAL TRAVEL*****")

    #Additional Feature
    #Conditional statements(Age, Vaccination status, Frontliner, Pregnancy)
    #Backlogs: Conditional statements for Age, Vaccine, Frontliner, Pregnancy, Restrictions based from IATF regulations.
    #Add another feature (to consider)

    if age < 18:
        print("\nHi, " , name , "! You are a MINOR travelling interzonally.")
        proceed(orig, dest)

    elif age > 18 and age < 65:
        a4 = input("Are you a frontliner? Y/N: ")
        if a4 == "Y" or a4 == "y":
            print("\nThank you for your service Frontliner ", name, "!")
            proceed(orig, dest)
        elif a4 == "N" or a4 == "n":
            pregnant = input("Are you pregnant? Y/N: ")
            if pregnant == "Y" or pregnant == "y":
                print("\nWoah! Congrats mama ", name, "! Safe travels and take care of your little one :)")
                proceed(orig, dest)
            elif pregnant == "N" or pregnant == "n":
                print("\n")
                print(name, ", sadly, you are not allowed interzonal travel! Please follow the set restrictions.")
                again()
            else:
                print("Wrong input!")
                again()
        else:
            print("Wrong input!")
            again()
            
    elif age > 65:
        vax = input("Are you fully vaccinated? Y/N: ")
        if vax == "Y" or vax == "y":
            print("\nHi, " , name , "! You are a FULLY VACCINATED ADULT travelling interzonally.")
            proceed(orig, dest)
        elif vax == "N" or vax == "n":
            print("\n",name, ", sadly, you are not allowed interzonal travel! Please follow the set restrictions.")
            again()
        else:
            print("Wrong input!")
            again()        
            
def proceed(orig, dest):

    #Option 1 of the rubric
    #Base code from Lab 4.9.2

    print("Here's what we have for you: \n")

    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "Rbx4dUy6MAKxomggVgx9psZAXsIRwpz6"

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

    again()

intro()