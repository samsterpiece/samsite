# Python program to read
# json file of 500 users

import json
import statistics
import math
from collections import *


def getJSONfromFile(file):
    # Opening JSON file
    # has 500 users in file I use
    # Note: when using https://randomuser.me/api/?results=5000 from site and saving the json file,
    # had error where I had to include encoding in order for it to work.
    # This takes in the file as an argument, opens it.
    # json_file = file.read()

    # returns JSON object as
    # a dictionary
    # data is a dictionary
    # json.load takes in JSON string and parses to give dict
    data = json.loads(file)
    # Closing file
    # json_file.close()


    # Return
    return data


def processData(data):
    users = data["results"]
    numUsers = len(data["results"])

    results = {}

    # What this program should do
    # Count the instances of a value(i.e: gender, age, first/last name, state, age

    # Counters for genders
    # femaleCount = 0
    # maleCount = 0
    # nonbinaryCount = 0

    # function for calculating the percentage
    # rounded to 2 decimal places
    def percentageCalculator(targetGroup, total):

        # Formatted string had to be use due to round function not showing two decimal places.
        return "{:.2f}".format((targetGroup / total) * 100)

    # Instantiate a counter to analyse gender data
    # For chart processing data
    genderCounter = Counter(tok["gender"] for tok in users)

    results["genders"] = {
        "female": genderCounter["female"],
        "male": genderCounter["male"],
        "nonbinary": numUsers - (genderCounter["female"] + genderCounter["male"])
    }

 
    # # -------------------------------------END EXAMPLE  #1 ------------------------------------------------

    # Function that counts the number of instances
    # Of first and last names started in the specified ranges A-M and N-Z
    # Invalid names will print out error message.
    # Assuming data is valid
    def nameCalculator(names):
        aThroughM = ['A', 'B', 'C', "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]

        firstNameAmCounter = 0
        firstNameNzCounter = 0
        lastNameAmCounter = 0
        lastNameNzCounter = 0

        for name in names:
            if name["first"][0] in aThroughM:
                firstNameAmCounter += 1
            else:
                firstNameNzCounter += 1

            if name["last"][0] in aThroughM:
                lastNameAmCounter += 1
            else:
                lastNameNzCounter += 1

        return {
            "first": {
                "AM": firstNameAmCounter,
                "NZ": firstNameNzCounter
            },
            "last": {
                "AM": lastNameAmCounter,
                "NZ": lastNameNzCounter
            }
        }

    # amCounter = 0
    # nzCounter = 0

    names = list(map(lambda x: x["name"], users))
    results["names"] = nameCalculator(names)

    # # #EXAMPLE 2-  FIRST NAMES COMPARISON A-M vs N-Z
    # for j in data['results']:
    #      if(j['name']['first'][0]) in ['A','B','C', "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]: #Better way in declaring this?
    #
    #         amCounter+= 1
    #
    #      elif(j['name']['first'][0]) in ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
    #
    #          nzCounter += 1

    # print("Counter of A-M: " , amCounter)
    # print("Couxnter of N-Z: " , nzCounter)

    # results["firstNames"] = {
    #     "AM": percentageCalculator(amCounter, amCounter + nzCounter) + "%",
    #     "NZ": percentageCalculator(nzCounter, amCounter + nzCounter) + "%"
    # }
    # # #Percentage of A-M
    # print("AM percentage First Name: ", percentageCalculator(amCounter, amCounter + nzCounter),"%")

    # #Percentage of N-Z:
    # print("NZ percentage First Name: " , percentageCalculator(nzCounter, nzCounter + amCounter), "%")

    # ---------------------------- END OF EXAMPLE 2------------------------------------------------------------

    # amCounter2 and nzCounter2 to represent last names
    # amCounter2 = 0
    # nzCounter2 = 0

    # EXAMPLE 2-  LAST NAMES COMPARISON A-M vs N-Z
    # for j in data['results']:
    #     if(j['name']['last'][0]) in ['A','B','C', "D", "E", "F", "G", "H","I","J","K","L","M"]: #Better way in declaring this?
    #          amCounter2+= 1
    #     elif(j['name']['last'][0]) in ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
    #         nzCounter2 += 1

    # print("Counter of Last Name A-M: " , amCounter2)
    # print("Counter of Last Name N-Z: " , nzCounter2)

    # Percentage of A-M
    # print("AM percentage Last Name: ", percentageCalculator(amCounter2, amCounter2 + nzCounter2),"%")

    # #Percentage of N-Z:
    # print("NZ percentage Last Name:" , percentageCalculator(nzCounter2, nzCounter2 + amCounter2), "%")

    # ---------------------------------EXAMPLE 3 ------------------------------------------------------------------------------

    # Method for populous states : using mode, based on list of peoples' state, highest mode is listed first, then the second
    # highest , sort through the frequency of a mentioned state.

    results["locations"] = {}

    # Mapping function that extracts the location and state of all
    # users.
    locations = list(map(lambda x: x['location'], users))
    stateList = list(map(lambda x: x['state'], locations))

    # stateList = []

    # #prints out all the states in list
    # for j in users:
    #    stateList.append(j['location']['state'])

    # using collections.counter
    # should sort the states by frequency
    sortState = [item for items, c in Counter(stateList).most_common()
                 for item in [items] * c]

    print("States sorted by Frequency:", str(sortState))

    # top 10 list states are listed here
    # These will become the keys in our results["locations"] dictionary
    top10States = []

    # Shape of desired data structure
    # results["locations"] = {
    #     "Alabama": {
    #         "percentageAllUsers": "10%",
    #         "percentageFemaleUsers": "12%",
    #         "percentageMaleUsers": "8%",
    #         "percentageNonbinaryUsers": "10%"
    #     },
    # }

    top10States.append(sortState[0])  # appending first element in state list that is most frequent

    # If state is already in top 10 states, keep on moving
    # otherwise, we add it to the list
    # we stop after 10
    for i in sortState:
        if len(top10States) < 10:
            if i in top10States:
                pass
            else:
                top10States.append(i)
        else:
            break

    print("Top 10 states after for-loop: ", top10States)

    # Assuming state is a string in all cases
    for state in top10States:
        results["locations"][state] = {}

    # Counting people in the top 10 states we found before
    # go through top 10 states,
    # count people with state associated to them
    # should get 10 results
    peopleStateCount = []
    for state in top10States:
        #    results["locations"][state]["percentageAllUsers"] = percentageCalculator(sortState.count(state), numUsers) + "%"
        peopleStateCount.append(sortState.count(i))
    # print("People in each state count in the top 10: " , peopleStateCount)
    stateDict = dict(zip(top10States, peopleStateCount))
    # print('state dictionary: ' , stateDict)

    # total of people living in
    # all of the top 10 states
    totalPeople = sum(peopleStateCount)

    # print('total amount of people living in top 10 states: ', totalPeople)

    # for loop that accesses the dict, grabs the key value and
    # divides each state population by the total amount of people in all 10 states
    # to produce a percentage
    # just the top 10, theres other states not listed
    # rounded to 2 decimal places

    for state in stateDict:
        if type(state) == str:
            results["locations"][state]["percentageAllUsers"] = percentageCalculator(stateDict[state],
                                                                                     totalPeople) + "%"
        else:
            continue
        # print("Percentage of people in: ",state,"{:.2f}".format((stateDict[state] / totalPeople) * 100),"%")

    # if gender == female AND state == isAStateInTop10, femaleStateCount +1 , else maleStateCount+1, else nonbinaryStateCount+1
    femaleStateCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    maleStateCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    nonbinaryStateCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    femaleDict = dict(zip(top10States, femaleStateCounter))
    maleDict = dict(zip(top10States, maleStateCounter))
    nonbinaryDict = dict(zip(top10States, nonbinaryStateCounter))

    # i represents index count
    # c represents the  iterable
    for c in users:
        if c['location']['state'] in top10States and c['gender'] == 'female':
            femaleDict[c['location']['state']] += 1
        elif (c['location']['state'] in top10States and c['gender'] == 'male'):
            maleDict[c['location']['state']] += 1
        elif (c['location']['state'] in top10States and c['gender'] == 'nonbinary'):
            nonbinaryDict[c['location']['state']] += 1

    print("Female Dicts: ", femaleDict)
    print("Male Dict: ", maleDict)
    print("Nonbinary Dicts: ", nonbinaryDict)

    for state in femaleDict:
        results["locations"][state]["percentageFemaleUsers"] = percentageCalculator(femaleDict[state],
                                                                                    totalPeople) + "%"
        # print("Female percentages in: ", i,"{:.2f}".format((femaleDict[i] / totalPeople) * 100),"%")

    for state in maleDict:
        # print("Male percentages in: ",i,"{:.2f}".format((maleDict[i] / totalPeople) * 100),"%")
        results["locations"][state]["percentageMaleUsers"] = percentageCalculator(maleDict[state], totalPeople) + "%"

    for state in nonbinaryDict:
        # print("Nonbinary percentages in: ",i,"{:.2f}".format((nonbinaryDict[i] / totalPeople) * 100),"%")
        results["locations"][state]["percentageNonbinaryUsers"] = percentageCalculator(nonbinaryDict[state],
                                                                                       totalPeople) + "%"

    ##--------------------------END OF NUMBER 5 AND 6---------------------------------------------------------####

    ageCounterList = [0, 0, 0, 0, 0, 0]

    ageList = ["age0to20", "age21to40", "age41to60", "age61to80", "age81to100", "age100plus"]
    ageDict = dict(zip(ageList, ageCounterList))

    # function for people's ages
    # if statements based on age ranges
    # adds to the string element of range into dictionary
    # this in turn becomes a counter of # of people in age range
    for i in users:
        if i['dob']['age'] <= 20:
            ageDict["age0to20"] += 1
        elif i['dob']['age'] <= 40:
            ageDict["age21to40"] += 1
        elif i['dob']['age'] <= 60:
            ageDict["age41to60"] += 1
        elif i['dob']['age'] <= 80:
            ageDict["age61to80"] += 1
        elif i['dob']['age'] <= 100:
            ageDict["age81to100"] += 1
        elif i['dob']['age'] > 100:
            ageDict["age100plus"] += 1

    print("agedict:", ageDict)

    results["ages"] = ageDict

    # for i in ageDict:
    #     print("Percentage of people in: ",i,percentageCalculator(ageDict[i],len(data['results'])), "%")

    ##---END OF EXAMPLE 7---------------------------------------
    return results
