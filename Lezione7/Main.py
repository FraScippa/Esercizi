from ANIMALS import Animal
from FENCE import Fence
from ZOOKEEPER import ZooKeeper
from ZOO import Zoo

zebra: Animal = Animal("Giggino", "Zebra", 15, 90, 65, "Savana")
leone: Animal = Animal ("Paolo", "Leone", 20, 40, 25, "Savana")
gazzella: Animal = Animal("Filippo", "Gazzella", 12, 20, 48, "Savana")
pinguin: Animal = Animal("Skipper", "Pinguin", 12, 50, 35, "Artic")

zookeeper: ZooKeeper = ZooKeeper("Ferdinando", "Paolini", '5457')
zookeeper1: ZooKeeper = ZooKeeper("Nicolò", "Di Silvestro", '07080')

savana: Fence = Fence(600000, 35, "Savana")
artic: Fence = Fence(1000000, -10, "Artic")

zookeeper.add_animal(zebra, savana)
#zookeeper.add_animal(leone, savana)
#zookeeper.add_animal(gazzella, savana)
zookeeper.feed(gazzella)
#zookeeper.remove_animal(zebra, savana)
#zookeeper.clean(savana)
#zookeeper.remove_animal(leone, savana)
print(savana)
