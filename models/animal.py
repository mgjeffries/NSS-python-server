class Animal():

    def __init__(self, id, name, species, status, location_id, customer_id):
        self.id = id
        self.name = name
        self.breed = species
        self.treatment = status
        self.locationId = location_id
        self.customerId = customer_id
        self.location = None
        self.customer = None