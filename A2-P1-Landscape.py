#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #:    W0443556 
#Student Name:  Kyle Preston

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    



    # Fescue = $0.05 per sq ft,  Brentgrass = $0.02 per sqft  campus = $ 0.01 per sqft  #trees = $100.00 per 


    #inputs 

    houseNumber = input("Enter House Number: ")

    length = input("Enter property depth (feet): ")

    width = input("Enter property width (feet): ")

    grassType = input("Enter type of grass (fescue, bentgrass, campus): ")

    trees = input("Enter the number of trees: ")



    #variables

    baseLabour = float(1000)
    cost = 0
    extrafee = 0
    extraCost = 0

    #calculations

    surface = float(length) * float(width)
    totalCost = cost + extrafee


    #output


    if grassType.lower() == "fescue":   # calculation based on fescue data
        cost = baseLabour + float(surface * 0.05) + (float(trees)*100)

                                            #fescue is $0.05 per sq ft
                                            #cost = baseLabour + surfaceFescue + (float(trees) * 100)
    


    elif grassType.lower() == "bentgrass": # calculation based on bentgrass data
         #brentgrass is $0.02 per sqft
        cost = baseLabour + float(surface * 0.02) + (float(trees)*100)


    elif grassType.lower() == "campus": # calculcation based on campus data
        #campus is $0.01 per sq ft
        cost = baseLabour + float(surface * 0.01) + (float(trees)*100)


    else:                   
        print("Invalid grasstype")



    if surface > 5000:      # if surface is more than 5000 sq ft
        extrafee = float(500)
        totalCost = cost + extrafee

    else:   # if surface is below 5000 sqft
        totalCost = cost







    #print for housenumber and total cost with 2 decimal spots

    print("Total cost for house {0} is: ${1:.2f}".format(houseNumber, totalCost ))







    # YOUR CODE ENDS HERE

main()