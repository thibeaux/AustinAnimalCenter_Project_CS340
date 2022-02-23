from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId



class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self,username,password):

        # Initializing the MongoClient. This helps to 

        # access the MongoDB databases and collections. 

        self.client = MongoClient('mongodb://%s:%s@localhost:37231' % (username, password))
        self.database = self.client['AAC']


# Complete this create method to implement the C in CRUD.
    '''
    @brief:         This function allows us to add a document to a the animals collection in the AAC database
    @Parameters:    Takes a dictionary type with the relevant fields to describe an animal document 
    @Returns:       Returns True if insertion was successful and False if unsuccessful. If there is no data in our dictionary type we will throw an exception.
    @Example:   
    animal = {
        'age_upon_outcome' : "2 years",
        'animal_id' : "111111",
        'animal_type' : "Dog",
        'breed' : "German Shepherd",
        'color' : "Brown/Black",
        'date_of_birth' : "2018-07-01",
        'datetime' : "2014-08-18T17:24:00",
        'monthyear' : "2014-08-18T17:24:00",
        'name' : "Forrest",
        'outcome_subtype': "Partner",
        'outcome_type' : "Transfer",
        'sex_upon_outcome' : "Neutered Male",
        'location_lat' : 30.4515549397366,
        'location_long' : -97.474104510925,
        'age_upon_outcome_in_weeks' : 62.2464285714286
        }

    '''
    def create(self, data):

        if bool(data):
            print("Attempting to add: ",data)
            result = self.database.animals.insert(data)  # data should be dictionary            
            if result:
                return True
            else:
                return False
        else:

            raise Exception("Nothing to save, because data parameter is empty")



# Create method to implement the R in CRUD.
    '''
    @Brief:     This funtion takes a query as an argument in the form of a dict data type and returns multiple dict entries from the query. You will need a list data type to print this to the terminal.  
    @Parameteres:    {'column' : 'value'}
    @Returns:   multiple documents each in a dictionary fomat
    @example:   To print the result try this result = list(AnimalShelterObj.read({'query' : 'value'}))
            print(result)
'''
    def read(self,data):
        if bool(data):
            print("Attempting to read: ", data)
            result = self.database.animals.find(data)  # data should be dictionary
            return result
        else:

            raise Exception("Nothing to save, because data parameter is empty")
            
    def readAll(self,data):
        result = self.database.animals.find(data,{"_id":False})
        return result

# Create method to implement the U in CRUD
    '''
    @Brief:     This function will update a document 
    @Parameters: Arguments to function should be the key/value lookup pair to use with the MongoDB driver find API call. Last argument to function will be a set of key/value pairs in the data type acceptable to the MongoDB driver insert API call.
    @Returns:   Result in JSON format if successful, else MongoDB returned error message.
    @Example:  exmaple inputs:
                lookUp = {'name': "Forrest"}
                newData ={"$set": {'age_upon_outcome' : "4 years"}} # $set is used to set field values 
    '''
    def update(self,lookUp, setData):
        if bool(lookUp) and bool(setData):
            print("Attempting to update: ",lookUp)
            print("With this data: ", setData)
            result = self.database.animals.update_many(lookUp,setData)  # data should be dictionary
            return result
        else:

            raise Exception("Nothing to save, because data parameter is empty")


# Create method to imlement the D in CRUD
    '''
    @Brief:     This function deletes a document
    @Parameters:    Arguments to function should be the key/value lookup pair to use with the MongoDB driver find API call.    
    @Returns:   Result in JSON format if successful, else MongoDB returned error message.
    '''
    def delete(self,lookUp):
        if bool(lookUp):
            print("Attempting to delete: ",lookUp)
            result = self.database.animals.delete_many(lookUp)  # data should be dictionary
            return result
        else:

            raise Exception("Nothing to save, because data parameter is empty")

 
