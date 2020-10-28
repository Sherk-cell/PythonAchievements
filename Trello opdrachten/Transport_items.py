import os
import time
Factory = []
Distribution = []
shop = []
item = "apple"
#Factory.insert(1, item)
print("Factory:",Factory )
print("Distribution:",Distribution)
print("shop:",shop)
time.sleep(1)
os.system('cls')
Factory.insert(0, item)
print("Factory:",Factory )
print("Distribution:",Distribution)
print("shop:",shop)
time.sleep(1)
os.system('cls')
Distribution.insert(0, item)
Factory.pop(0)
print("Factory:",Factory,)
print("Distribution:",Distribution)
print("shop:",shop)
time.sleep(1)
os.system('cls')
Distribution.pop(0)
shop.insert(1, item)
print("Factory:", Factory )
print("Distribution:",Distribution)
print("shop:",shop)
