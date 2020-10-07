EMPLOYEES = [
    {
      "id": 1,
      "name": "Jeremy Bakker",
      "locationId": 1,
      "animalId": 3
    },
    {
      "id": 2,
      "name": "Frank Bakker",
      "locationId": 1,
      "animalId": 3
    },
    {
      "id": 3,
      "name": "Helen Bakker",
      "locationId": 2,
      "animalId": 4
    },
    {
      "id": 4,
      "name": "Elen Bakker",
      "locationId": 2,
      "animalId": 2
    }
]


def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee