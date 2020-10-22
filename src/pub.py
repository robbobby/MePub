class Pub:
    def __init__(self, pub_name, floor_w, floor_h, customer, staff):
        self.name = pub_name
        self.customer = customer
        self.floor_h = floor_h
        self.floor_w = floor_w
        self.staff = staff

    def change_pub_name(self, new_name):
        self.name = new_name
