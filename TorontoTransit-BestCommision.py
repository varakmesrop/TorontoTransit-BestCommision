#Varak Mesropian
#501168289
#I used pycharm

'''''''''
I, Varak commute everyday to university, and one of the problems I have is, if I should get the monthly TTC pass 
or continue filling my presto card, with 'pay-as-you-go' price, that is why I made this program to help you and I decide 
which one we should invest in to save money. I am using the TTC website for all the price and age information
'''''''''

runAgain = "y" #runAgain is set to 'y'

def calc(name, age, amount, uni): #function called calc, inputing name and age inputed from the user
    #all the prices, got all information from https://www.ttc.ca/Fares-and-passes
    monthly_adult = 156.00
    monthly_teen = 128.00
    monthly_uni = 128.00
    adultp = 3.20
    youthp = 2.25
    price = 0
    #checking ages
    if uni == "Y" or uni == "y": #by using string/character comparing, and boolean checking of uni is 'y' (I asked Prof. Elodie she said this counts as comparing strings and/or characters)
        # if true stay, if false go to next if statement
        if (0 <= age <= 12): #using boolean by checking if age is in between or equal to 0 and 12 (I asked Prof. Elodie she said this counts as boolean)
            #if true stay, if false go to next if statement
            with open("output.txt", 'a') as outputFile: #making the file, and appending
                print("> Ride is free for " + str(name) + "!", file = outputFile) #printing to a file

        elif (age >= 65) or (13 <= age <= 19): #using boolean by checking if age is greater than 65 or in between or equal to 13 and 19 (I asked Prof. Elodie she said this counts as boolean)
            # if true stay, if false go to next if statement
            price = round(youthp * amount,2)  # multiplying the youth/senior 'pay-as-you-go' price by how many times the user will use, and rounding it to 2 decimal places
            if price < monthly_uni:  # using boolean, checking if the price calculated is less than the monthly plan (I asked Prof. Elodie she said this counts as boolean)
                # if true stay, if false go to next if statement
                with open("output.txt", 'a') as outputFile:  # making the file, and appending
                    # printing by concatenating the name and the price of 'pay-as-you-go' option and saying it's less than monthly plan
                    print("> " + str(name) + " will be spending $" + str(price) + " with 'pay-as-you-go' option, which is less than $" + str(monthly_uni),file=outputFile)  # printing to a file
                    # therefore 'pay-as-you-go' option is better
                    print("you will save more money with the 'pay-as-you-go' option",file=outputFile)  # printing to a file

            elif monthly_uni < price:  # using boolean, checking if the price calculated is more than the monthly plan (I asked Prof. Elodie she said this counts as boolean)
                with open("output.txt", 'a') as outputFile:  # making the file, and appending
                    # printing by concatenating the name and the price of 'pay-as-you-go' option and saying it's more than monthly plan
                    print("> " + str(name) + " will be spending $" + str(price) + " with 'pay-as-you-go' option, which is more than $" + str(monthly_uni),file=outputFile)  # printing to a file
                    # therefore monthly option is better
                    print("you will save more money with the monthly pass option",file=outputFile)  # printing to a file

        else:
            price = round(adultp * amount,2)  # multiplying the adult 'pay-as-you-go' price by how many times the user will use, and rounding it to 2 decimal places
            if price < monthly_uni:  # using boolean, checking if the price calculated is less than the monthly plan (I asked Prof. Elodie she said this counts as boolean)
                # if true stay, if false go to next if statement
                with open("output.txt", 'a') as outputFile:  # making the file, and appending
                    # printing by concatenating the name and the price of 'pay-as-you-go' option and saying it's less than monthly plan
                    print("> " + str(name) + " will be spending $" + str(price) + " with 'pay-as-you-go' option, which is less than $" + str(monthly_uni),file=outputFile)  # printing to a file
                    # therefore 'pay-as-you-go' option is better
                    print("you will save more money with the 'pay-as-you-go' option",file=outputFile)  # printing to a file

            elif monthly_uni < price:  # using boolean, checking if the price calculated is more than the monthly plan (I asked Prof. Elodie she said this counts as boolean)
                with open("output.txt", 'a') as outputFile:  # making the file, and appending
                    # printing by concatenating the name and the price of 'pay-as-you-go' option and saying it's more than monthly plan
                    print("> " + str(name) + " will be spending $" + str(price) + " with 'pay-as-you-go' option, which is more than $" + str(monthly_uni),file=outputFile)
                    # therefore monthly option is better
                    print("you will save more money with the monthly pass option", file=outputFile)

    elif uni == "N" or uni == "n": #by using string/character comparing, and boolean checking of uni is 'n'
        # if true stay, if false go to next if statement
        if (0 <= age <= 12): #using boolean by checking if age is in between or equal to 0 and 12 (I asked Prof. Elodie she said this counts as boolean)
            #if true stay, if false go to next if statement
            with open("output.txt", 'a') as outputFile: #making the file, and appending
                print("> Ride is free for " + str(name) + "!", file = outputFile) #printing to a file

        elif (age >= 65) or (13 <= age <= 19): #using boolean by checking if age is greater than 65 or in between or equal to 13 and 19 (I asked Prof. Elodie she said this counts as boolean)
            # if true stay, if false go to next if statement
            price = round(youthp * amount,2) #multiplying the youth/senior 'pay-as-you-go' price by how many times the user will use, and rounding it to 2 decimal places
            if price < monthly_teen: #using boolean, checking if the price calculated is less than the monthly plan (I asked Prof. Elodie she said this counts as boolean)
                #if true stay, if false go to next if statement
                with open("output.txt", 'a') as outputFile: #making the file, and appending
                    #printing by concatenating the name and the price of 'pay-as-you-go' option and saying it's less than monthly plan
                    print("> "+str(name)+" will be spending $" + str(price) + " with 'pay-as-you-go' option, which is less than $" + str(monthly_teen),file = outputFile)#printing to a file
                    #therefore 'pay-as-you-go' option is better
                    print("you will save more money with the 'pay-as-you-go' option",file = outputFile)#printing to a file
            elif monthly_teen < price: #using boolean, checking if the price calculated is more than the monthly plan (I asked Prof. Elodie she said this counts as boolean)
                with open("output.txt", 'a') as outputFile: #making the file, and appending
                    #printing by concatenating the name and the price of 'pay-as-you-go' option and saying it's more than monthly plan
                    print("> "+str(name) + " will be spending $" + str(price) + " with 'pay-as-you-go' option, which is more than $" + str(monthly_teen),file = outputFile)#printing to a file
                    # therefore monthly option is better
                    print("you will save more money with the monthly pass option",file = outputFile)#printing to a file

        else:
            price = round(adultp * amount,2) #multiplying the adult 'pay-as-you-go' price by how many times the user will use, and rounding it to 2 decimal places
            if price < monthly_adult: #using boolean, checking if the price calculated is less than the monthly plan (I asked Prof. Elodie she said this counts as boolean)
                # if true stay, if false go to next if statement
                with open("output.txt", 'a') as outputFile: #making the file, and appending
                    # printing by concatenating the name and the price of 'pay-as-you-go' option and saying it's less than monthly plan
                    print("> "+str(name)+" will be spending $" + str(price) + " with 'pay-as-you-go' option, which is less than $" + str(monthly_adult),file = outputFile)#printing to a file
                    # therefore 'pay-as-you-go' option is better
                    print("you will save more money with the 'pay-as-you-go' option",file = outputFile)#printing to a file
            elif monthly_adult < price: #using boolean, checking if the price calculated is more than the monthly plan (I asked Prof. Elodie she said this counts as boolean)
                with open("output.txt", 'a') as outputFile: #making the file, and appending
                    # printing by concatenating the name and the price of 'pay-as-you-go' option and saying it's more than monthly plan
                    print("> "+str(name) + " will be spending $" + str(price) + " with 'pay-as-you-go' option, which is more than $" + str(monthly_adult),file = outputFile)
                    # therefore monthly option is better
                    print("you will save more money with the monthly pass option",file = outputFile)

# START
# introduction and description
print("I, Varak commute everyday to university, and one of the problems I have is, if I should get the monthly TTC pass")
print("or continue filling my presto card, with 'pay-as-you-go' price")
print("that is why I made this program to help you and I decide which one we should invest in to save money.")
print("I am using the TTC website for all the price and age information")
print("Let's start!")
while runAgain == "Y" or runAgain == 'y': #stay in loop while runAgain is 'y' (I asked Prof. Elodie she said this counts as comparing strings and/or characters)
    name = input("input Name: ") #asking user to input name
    amount = int(input("How many times do you think you will be using the TTC in 1 month? ")) #asking user to input how many times they think they will use the TTC, and the input is an integer
    uni = input("are you a university student? Y/N:  ")
    age = int(input("input age: "))  # asking user to input age, and the input is an integer
    # checking if age is valid
    if age < 0: #using boolean by checking if age is less than 0 (negative) (I asked Prof. Elodie she said this counts as boolean)
        # if true stay, if false go to next if statement
        print("Invalid age.") #since age can not be negative it is invalid
    elif age >= 0: #using boolean by checking if age is more than 0 (I asked Prof. Elodie she said this counts as boolean)
        calc(name, age, amount, uni) #importing the user inputs to the function

    print("to see results you need to end code") #in order to see the results on the file, the code must end
    runAgain = input("Do you want to do another calculation?: Y/N \n")
    # ask user if they want to do another calculation, if yes loop runs again since runAgain is 'y', if no leave loop

print("Goodbye") #done
#END