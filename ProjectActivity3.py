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
        print("MECQ")
    
    elif orig in GCQ_heightened and dest in GCQ_heightened:
        print("GCQ heightened")

    elif orig in GCQ_regular and dest in GCQ_regular:
        print("GCQ regular")
    
    else:
        if age < 18:
            print("interzonal < 18")

        elif age > 65:
            vax = input("Are you fully vaccinated? Y/N: ")
            if vax == "Y" or vax == "y":
                print("interzonal > 65, vaxxed")
            elif vax == "N" or vax == "n":
                print("interzonal > 65, non-vaxxed")
            else:
                print("Wrong input!")
        
        else:
            a4 = input("Are you a frontliner? Y/N: ")
            if a4 == "Y" or a4 == "y":
                print("frontliner")
            elif a4 == "N" or a4 == "n":
                pregnant = input("Are you pregnant? Y/N: ")
                if pregnant == "Y" or pregnant == "y":
                    print("pregnant")
                elif pregnant == "N" or pregnant == "n":
                    print("CANNOT PASS")
                else:
                    print("Wrong input!")
            else:
                print("Wrong input!")

intro()