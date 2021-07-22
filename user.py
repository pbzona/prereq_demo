import random
import uuid

class User:
    def __init__(self):
        self.id = uuid.uuid4()
        self.state = ""
        self.context = {}
        
        self.create_context()
    
    def create_context(self):
        # Choose a random state
        state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
        self.state = random.choice(state_names)
        
        self.context = {
            "key" : self.id,
            "country" : "USA",
            "custom" : {
                "state" : self.state
            }
        }
    
    def debug(self):
        print("==========")
        print("ID: ", self.id)
        print("State: ", self.state)
        print("==========")