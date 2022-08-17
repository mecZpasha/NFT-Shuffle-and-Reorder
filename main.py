import json
import os
from pathlib import Path
import shutil
import random


os.getcwd()
collection = "collection/"
directory = os.fsencode(collection)
jsons = "jsons/"
new_collection = "new_collection/"
new_jsons = "new_jsons/"
nc = "nc/"
nj = "nj/"

oldList = []
for file in os.listdir(directory):
    fn = os.fsdecode(file)
    num = fn.split(".")[0]
    oldList.append(int(num))

random.shuffle(oldList)

newList = []
for x in range(0,len(oldList)+1):
    x += 1
    newList.append(x)

dictionary = dict(zip(oldList,newList))
print(dictionary)

for f in os.listdir(new_collection):
    os.remove(new_collection + f)
for f in os.listdir(new_jsons):
    os.remove(new_jsons + f)




for key, value in list(dictionary.items()):
    if "{}.png".format(key) in os.listdir(new_collection):
        shutil.copy(collection + "{}.png".format(key), nc)
        os.rename(nc + "{}.png".format(key), nc + "{}.png".format(value))
        shutil.copy(nc + "{}.png".format(value), new_collection)
        os.remove(nc + "{}.png".format(value))
    else:   
        shutil.copy(collection + "{}.png".format(key), new_collection)
        os.rename(new_collection + "{}.png".format(key), new_collection + "{}.png".format(value))

for key, value in list(dictionary.items()):
    if "{}.json".format(key) in os.listdir(new_jsons):
        shutil.copy(jsons + "{}.json".format(key), nj)
        os.rename(nj + "{}.json".format(key), nj + "{}.json".format(value))
        shutil.copy(nj + "{}.json".format(value), new_jsons)
        os.remove(nj + "{}.json".format(value))
    else:
        shutil.copy(jsons + "{}.json".format(key), new_jsons)
        os.rename(new_jsons + "{}.json".format(key), new_jsons + "{}.json".format(value))
        
       
directory = os.fsencode(new_jsons)

for file in os.listdir(directory):
    fn = os.fsdecode(file)
    num = fn.split(".")[0]
    with open(new_jsons + fn) as f:
        data = json.load(f)
        data["name"] = "Collection Name #{}".format(num)
        data["description"] = "Collection Explanation"
        data["image"] = "ipfs://ImageIPFSID{}.png".format(num)
        data["edition"] = num

        with open(new_jsons + "{}.json".format(num), "w" ) as f:
            json.dump(data, f, indent= 4)