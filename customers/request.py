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

def create_customer(customer):
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
  customer_index = -1

  for index, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
      customer_index = index
  
  if customer_index >= 0:
    CUSTOMERS.pop(customer_index)
