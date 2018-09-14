from typing import List, Any
from xml.etree import ElementTree

class SaveGameFileUtil:
    def __init__(self, savegameFilepath, vehicleFilepath):
        self.filepath = savegameFilepath
        self.vehicleFilepath = vehicleFilepath

    def getMoney(self):
        return getMoneyFromFile(self.filepath)

    def setMoney(self, moneyInt):
        return setMoneyInFile(self.filepath, moneyInt)

    def getModList(self):
        return getModList(self.filepath)

    def getUsedMods(self):
        return getUsedMods(self.filepath, self.vehicleFilepath)

    def getUnusedMods(self):
        return getUnusedMods(self.filepath, self.vehicleFilepath)


def getMoneyFromFile(filename):
    assert isinstance(filename, str)
    moneyElement = ElementTree.parse(filename).getroot().find("statistics/money")
    if moneyElement is None:
        return None
    return int(moneyElement.text)


def setMoneyInFile(filename, newMoneyIntValue):
    assert isinstance(newMoneyIntValue, int)
    assert isinstance(filename, str)
    tree = ElementTree.parse(filename)
    moneyElement = tree.getroot().find("statistics/money")
    if moneyElement is None:
        return False

    moneyElement.text = str(newMoneyIntValue)
    tree.write(filename)
    return True

def getModList(filename):
    assert isinstance(filename, str)
    modList = ElementTree.parse(filename).findall("mod")
    modNames: List[str] = []
    for mod in modList:
        modNames.append(mod.attrib["modName"])

    modNames.sort()
    print("Available mods: ", modNames)
    return modNames

def getUsedMods(savegameFilename, vehiclesXmlFilename):
    assert isinstance(savegameFilename, str)
    assert isinstance(vehiclesXmlFilename, str)

    allMods = getModList(savegameFilename)
    usedModElements = ElementTree.parse(vehiclesXmlFilename).findall("vehicle")
    usedModNames: List[str] = []

    for mod in usedModElements:
        if "modName" in mod.attrib:
            usedModNames.append(mod.attrib["modName"])

    usedModNames.sort()
    print("Mods purchased in game: ", usedModNames)
    return usedModNames

def getUnusedMods(savegameFilename, vehiclesXmlFilename):
    assert isinstance(savegameFilename, str)
    assert isinstance(vehiclesXmlFilename, str)

    allMods: List[str] = getModList(savegameFilename)
    usedMods = getUsedMods(savegameFilename, vehiclesXmlFilename)

    for mod in usedMods:
        if allMods.__contains__(mod):
            allMods.remove(mod)

    print("Unused mods: ", allMods)
    return allMods
