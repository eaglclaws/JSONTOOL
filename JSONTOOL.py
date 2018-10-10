import json
"""
The database is structured as follows

productdb.json
{
	"product name" :
	{
		"name" : "product name",
		"info" :
		{
			"manufacturer" : "string", > name of manufacturer
			"price" : int, > price of product
			"laundry" : [list of strings], > laundry instructions, null if not clothing
			"allergens" : [list of strings] > foodstuff allergens, null if empty
		}
	}
}
"""
class ProductDatabase:
	def __init__(self, jsonfile):
		self.sourcefile = jsonfile
		with open(jsonfile, "r") as jsonsource:
			self.fulldatabase = json.load(jsonsource)
	def additem(self, item):
		self.fulldatabase[item["name"]] = item
		with open(self.sourcefile, "w") as jsondest:
			json.dump(self.fulldatabase, jsondest, indent=4)
	def removeitem(self, product):
		self.fulldatabase.pop(product)
		with open(self.sourcefile, "w") as jsondest:
			json.dump(self.fulldatabase, jsondest, indent=4)
	def getproduct(self, name):
		return self.fulldatabase[name]
	def getinfo(self, product, info="none"):
		if info == "none":
			infostring = ""
			infokeys = list(self.fulldatabase[product]["info"].keys())
			for key in infokeys:
				infostring = infostring + key + " : " + str(self.fulldatabase[product]["info"][key]) + "\n"
			return infostring
		else:
			return self.fulldatabase[product]["info"][info]
	def additems(self, items):
		for item in items:
			self.fulldatabase[item["name"]] = item
		with open(self.sourcefile, "w") as jsondest:
			json.dump(self.fulldatabase, jsondest, indent=4)

def createitem():
	item = dict()
	print("What is the name of this product?")
	name = input()
	print("Who is the manufacturer?")
	manu = input()
	print("How much is this product?")
	price = int(input())
	print("Is this product clothing? (y/N)")
	clothing = input() == ("y" or "Y")
	if clothing:
		print("What are the instructions? (ex: code1, code2, code3, etc)")
		laundry = input().split(", ")
		item = {"name":name, "info":{"manufacturer":manu, "price":price, "laundry":laundry, "allergens":None}}
		return item
	else:
		print("Does this product have allergens? (Y/n)")
		nothasaler = input() == ("n" or "N")
		if nothasaler:
			item = {"name":name, "info":{"manufacturer":manu, "price":price, "laundry":None, "allergens":None}}
			return item
		else:
			print("What allergens does it have? (ex: allergen1, allergen2, etc)")
			allergens = input().split(", ")
			item = {"name":name, "info":{"manufacturer":manu, "price":price, "laundry":None, "allergens":allergens}}
			return item

def createitems(stream):
	keystrings = ["name", "manufacturer", "price", "laundry", "allergens"]
	items = []
	cnt = 0
	with open(stream, "r") as source:
		for line in enumerate(source):
			item = dict()
			item["info"] = dict()
			print(line)
			temp = line[1].replace("\n", "").split(", ")
			for value in temp:
				print(cnt)
				buff = value.split(";")
				if len(buff)==1:
					buff = buff[0]
				if cnt>=1:
					item["info"][keystrings[cnt]]=buff
				else:
					item["name"] = buff
				cnt = cnt+1
			items.append(item)
			cnt = 0
	return items
