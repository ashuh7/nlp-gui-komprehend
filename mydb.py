
# * My Logic
# import json

# class Database:

#     def add_data(self,name,email,password):

#         with open('db.json','r') as rf:
#             database = json.load(rf)

#         if email in database:
#             return 0
#         else:
#             database[email] = [name,password]
#             with open('db.json','w') as wf:
#                 json.dump(database,wf)
#             return 1

# * Relative path error so solved by taking absolute path!!
import json
import os

class Database:

    def __init__(self):
        # Always resolve db.json relative to this file's location
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.json')

        # Create db.json if it doesn't exist
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w') as f:
                json.dump({}, f)

    def add_data(self, name, email, password):
        try:
            with open(self.db_path, 'r') as rf:
                database = json.load(rf)

            if email in database:
                return 0
            else:
                database[email] = [name, password]
                with open(self.db_path, 'w') as wf:
                    json.dump(database, wf, indent=4)
                return 1

        except Exception as e:
            print(f"Database error: {e}")
            return 0