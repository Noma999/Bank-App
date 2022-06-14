

class Profile:
    def __init__(self, name, DOB, phone, email, address,deposit):
        self.name = name
        self.DOB = DOB
        self.phone = phone
        self.email = email
        self.address = address
        self.deposit = deposit

    def show(self):

        show= [self.name, self.DOB, self.phone, self.email, self.address, self.deposit]
        
        return show