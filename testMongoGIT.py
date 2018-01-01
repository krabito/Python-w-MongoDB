from pymongo import MongoClient
 
# Connect to the MongoDB.
# Atlas Cluster: cluster0-shard-00-00-scnto.mongodb.net
conn = MongoClient('mongodb+srv://krabito:xxxyyyyzzz@cluster0-scnto.mongodb.net/')
 
# Access the testdb database and the emp collection.
db = conn.VacationSpots
dbPeople = conn.VacationSpots.People
dbPlaces = conn.VacationSpots.Places
 
# create a dictionary to hold details.
 
VSdb = {}
VSPeople = {}
VSPlaces = {}
 
# set a flag variable.
flag = True
 
# Data input loop
while (flag):
   # ask for input.
   P_firstname, P_lastname, P_vspot = input("Please use , to separate enteries. Enter Firstname, Lastname  and Vacation Spot: ").split(',')
   #place values in dictionary.
   VSPeople = {'Firstname':P_firstname,'Lastname':P_lastname,'Location':P_vspot}
   # insert the record.
   dbPeople.insert(VSPeople)
   # Check if their Location is in the Places Collection
   x =  dbPlaces.find( { "Location" : P_vspot } ) 
   if ( x != P_vspot ):
   	P_city, P_state = input("Your Vacation Spot is not in our database. Please add the City and State information: City , State ").split(',')
   	VSPlaces = {'Location': P_vspot,'City':P_city,'State':P_state}
   	dbPlaces.insert(VSPlaces)

   # Ask from user if he wants to continue to insert more documents?
   flag = input('Enter another record? ')
   if (flag[0].upper() == 'N'):
      flag = False
 
# Print out documents.
ret = db.People.find()
# 
# Display documents from People collection.
print('+-+-+-+ People and their Vacation Spots -+-+-+-+-+-+-+-+-+-+-')
# 
for record in ret:
	print(record['Firstname'] + ',',record['Lastname'] + ',',record['Location'])
	print()
 
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
print()
print()
# Display documents from Places collection.
ret = db.Places.find()
print('+-+-+-+ Vacation Spots in Our Database -+-+-+-+-+-+-+-+-+-+-')
for record in ret:
	print(record['Location'] + ',',record['City'] + ',',record['State'])
	print()

print('+-+-+-+-+ END -+-+-+-+-+-+-+-+-+-')
#close the conn to MongoDB
conn.close()
