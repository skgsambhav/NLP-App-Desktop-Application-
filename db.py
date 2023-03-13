import json
class Database:
    def add_data(self,name,email,password):
        with open('db.json','r') as fo:
            database = json.load(fo)
        if email in database:
            return 0                  #0 means false

        else:
            database[email] = [name,password]
            with open('db.json','w') as wf:
                json.dump(database,wf,indent=4)
            return 1            #1 means true




    def search(self,username,password):
        with open('db.json','r') as rf:
            database = json.load(rf)

        if username in database:
            if database[username][1]== password:
                return 1
            else:
                return 0

        else:
            return 0


