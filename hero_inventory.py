inventory = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(loot, inventory):
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item]+=1

def inventoryPrint(inventory):
    sizeOfInventory = 0
    print("Inventory: ")
    for item, quantity in inventory.items():
        print(item, end=': ')
        print(quantity)
        sizeOfInventory+=quantity
    print("Total number of items: {}".format(sizeOfInventory))

inventoryPrint(inventory)
addToInventory(dragonLoot,inventory)
inventoryPrint(inventory)
