invoer = "";

# Zolang de invoer geen float is, wordt deze while loop uitgevoerd
while not isinstance(invoer, float):

    # probeer of deze code werkt    
    try:
        # Vraag om een getal en sla op in de variabele: invoer
        invoer = input("hoeveel kilometer rij je per maand?")
        
        # Probeer de input om te zetten in een float (getal met cijfers achter de komma)
        invoer = float(invoer)

        # Als Python tot hier komt dan is het gelukt! Anders wordt de except code uitgevoerd
        #print("Ja, de invoer " + str(invoer) + " is een getal, want ik kan het omzetten naar een float")

    except ValueError:
        # Als er een ValueError optreedt, dan voer je deze code uit 
        print(invoer + " is geen geldig getal!")

verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2 

maandkosten = (invoer * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand
print ("je maandkosten zijn €" , maandkosten )

