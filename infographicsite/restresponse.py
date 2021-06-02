import dicttoxml
from infographicsite import infoparse
import json

def jsonResponse(jsonData):
    buildResponse(jsonData)

def xmlResponse(jsonData):
    # analyse data and build xml response
    return dicttoxml.dicttoxml(buildResponse(jsonData))

def plainTextResponse(jsonData):
    print("Built a plain text response")
    # analyse data and build plain text response

def buildResponse(data):
    results = infoparse.processData(data)

    response = {}

    totalUsers = results["genders"]["female"] + results["genders"]["male"] + results["genders"]["nonbinary"]

    response["percentFemale"] = calculatePercentage(results["genders"]["female"], totalUsers)
    response["percentMale"] = calculatePercentage(results["genders"]["male"], totalUsers)
    response["percentNonbinary"] = calculatePercentage(results["genders"]["nonbinary"], totalUsers)

    response["names"] = { "first": {}, "last": {} }
    response["names"]["first"]["percentAM"] = calculatePercentage(results["names"]["first"]["AM"], totalUsers)
    response["names"]["first"]["percentNZ"] = calculatePercentage(results["names"]["first"]["NZ"], totalUsers)
    response["names"]["last"]["percentAM"] = calculatePercentage(results["names"]["last"]["AM"], totalUsers)
    response["names"]["last"]["percentNZ"] = calculatePercentage(results["names"]["last"]["NZ"], totalUsers)
    response["locations"] = {}
    response["age"] =  {}

    return response
    # build a generic dictionary with the data to be returned

def calculatePercentage(number, total):
    return float(number) * 100 / total