from xml.etree import ElementTree

class SaveGameFileUtil:
    def __init__(self, filepath):
        self.filepath = filepath

    def getMoney(self):
        return getMoneyFromFile(self.filepath)

    def setMoney(self, moneyInt):
        return setMoneyInFile(self.filepath, moneyInt)


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
