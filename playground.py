import fs_savegame

game = fs_savegame.SaveGameFileUtil("careerSavegame.xml", vehicleFilepath="vehicles.xml")

print("Current save game money: " + str(game.getMoney()))
'''
inputStr = input("Enter a new amount: ")

success = game.setMoney(int(inputStr))

if True == success:
    print("Saved it!")
else:
    print("Didn't save :(")
'''

game.getUnusedMods()