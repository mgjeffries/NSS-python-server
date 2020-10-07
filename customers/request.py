CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct"
    },
    {
      "id": 2,
      "name": "Adam Adders",
      "address": "1 Main St"
    },
    {
      "id": 3,
      "name": "Bobby Boy",
      "address": "2 Side St"
    },
    {
      "email": "gib@gibland.com",
      "password": "a",
      "name": "Gib Jeffries",
      "id": 4
    }
]


def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for employee in CUSTOMERS:
        if employee["id"] == id:
            requested_customer = employee

    return requested_customer