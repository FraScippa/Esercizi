from Zoo import Zoo
from ANIMALS import Animal
from FENCE import Fence
from ZOOKEEPER import ZooKeeper

zebra: Animal = Animal("Giggino", "Zebra", 15, 90, 65, "Savana")
leone: Animal = Animal ("Paolo", "Leone", 20, 120, 60, "Savana")

print(zebra)
print("_"*100)
print(leone)
print("#"*100)

zookeeper: ZooKeeper = ZooKeeper("Ferdinando", "Paolini", '5457')
zookeeper1: ZooKeeper = ZooKeeper("Nicolò", "Di Silvestro", '07080')

print(zookeeper,zookeeper1)

savana: Fence = Fence(60000, 35, "Savana")

zookeeper.add_animal(savana, zebra)
print(savana)

