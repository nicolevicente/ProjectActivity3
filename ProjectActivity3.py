import urllib.parse
import requests

def intro():
    MECQ = ["Apayao", "Kalinga", "Batanes", "Bataan", "Bulacan", "Cavite", "Lucena City", 
    "Rizal", "Laguna", "Naga City", "Bicol", "Iloilo Province"]

    GCQ_heightened = ["Abra", "Baguio City", "Ilocos Sur", "Pangasinan", "Cagayan", "Isabela", "Santiago City",
    "Nueva Vizcaya", "Quirino",  "Quezon", "Batangas", "Bacolod City", "Capiz", "Iloilo City", "Lapu-Lapu City",
    "Negros Oriental", "Bohol", "Zamboanga del Norte", "Zamboanga del Sur", "Cagayan de Oro City", "Misamis Oriental", 
    "Davao del Norte", "Davao Occidental", "Davao de Oro", "Butuan City", "Surigao del Sur"]

    GCQ_regular = ["Ilocos Norte", "Dagupan City", "Benguet", "Ifugao", "Tarlac", "Mariduque", "Occidental Mindoro", "Oriental Mindoro",
    "Puerto Princesa", "Albay", "Camarines Norte", "Aklan", "Antique", "Guimaras", "Negros Occidental", "Cebu City", "Cebu Province",
    "Mandaue City", "Siquijor", "Tacloban City", "Zamboanga Sibugay", "Zamboanga City", "Misamis Occidental", "Iligan City",
    "Davao City", "Davao Oriental", "Davao del Sur", "General Santos City", "Sultan Kudarat", "Sarangani", "North Cotabato",
    "South Cotabato", "Agusan del Norte", "Agusan del Sur", "Surigao del Norte", "Dinagat Islands", "Cotabato City", "Lanao del Sur"]

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    orig = input("Enter your Starting Location: ")
    dest = input("Enter your Destination: ")

    if orig in MECQ and dest in MECQ:
        print("Hi, " , name , "! You are travelling between: MECQ areas.\n")
        proceed(orig, dest)
    
    elif orig in GCQ_heightened and dest in GCQ_heightened:
        print("Hi, " , name , "! You are travelling between: Heightened GCQ areas.\n")
        proceed(orig, dest)

    elif orig in GCQ_regular and dest in GCQ_regular:
        print("Hi, " , name , "! You are travelling between: Regular GCQ areas.\n")
        proceed(orig, dest)
    
    else:
        if age < 18:
            print("Hi, " , name , "! You are a MINOR travelling interzonally.\n")
            proceed(orig, dest)

        elif age > 18 and age < 65:
            a4 = input("Are you a frontliner? Y/N: ")
            if a4 == "Y" or a4 == "y":
                print("Thank you for your service Frontliner ", name, "!")
                proceed(orig, dest)
            elif a4 == "N" or a4 == "n":
                pregnant = input("Are you pregnant? Y/N: ")
                if pregnant == "Y" or pregnant == "y":
                    print("Woah! Congrats mama ", name, "! Safe travels and take care of your little one :)")
                    proceed(orig, dest)
                elif pregnant == "N" or pregnant == "n":
                    print(name, ", sadly, you are not allowed interzonal travel! Please follow the set restrictions.")
                else:
                    print("Wrong input!")
            else:
                print("Wrong input!")
            
        elif age > 65:
            vax = input("Are you fully vaccinated? Y/N: ")
            if vax == "Y" or vax == "y":
                print("Hi, " , name , "! You are a FULLY VACCINATED ADULT travelling interzonally.\n")
                proceed(orig, dest)
            elif vax == "N" or vax == "n":
                print(name, ", sadly, you are not allowed interzonal travel! Please follow the set restrictions.")
            else:
                print("Wrong input!")
            

def proceed(orig, dest):
    print("\n Here's what we have for you: \n")

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


intro()