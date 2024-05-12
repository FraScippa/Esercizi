from ANIMALS import Animal
from FENCE import Fence
from ZOOKEEPER import ZooKeeper

zebra: Animal = Animal("Giggino", "Zebra", 15, 90, 65, "Savana")
leone: Animal = Animal ("Paolo", "Leone", 20, 40, 25, "Savana")
gazzella: Animal = Animal("Filippo", "Gazzella", 12, 20, 48, "Savana")
pinguin: Animal = Animal("Skipper", "Pinguin", 12, 50, 35, "Artic")
#print(zebra)
#print("_"*100)
#print(leone)
#print("#"*100)

zookeeper: ZooKeeper = ZooKeeper("Ferdinando", "Paolini", '5457')
zookeeper1: ZooKeeper = ZooKeeper("Nicolò", "Di Silvestro", '07080')

#print(zookeeper,zookeeper1)

savana: Fence = Fence(60, 35, "Savana")
artic: Fence = Fence(10000, -10, "Artic")

#zookeeper.add_animal(zebra, savana)
#zookeeper.add_animal(leone, savana)
zookeeper.add_animal(gazzella, savana)
#zookeeper.clean(savana)


#zookeeper.remove_animal(zebra, savana)
 #zookeeper.remove_animal(leone, savana)
print(savana)

