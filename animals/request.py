ANIMALS = [
    {
      "id": 1,
      "name": "Doodles",
      "breed": "Poodle",
      "locationId": 2,
      "treatment": "Shampoo",
      "customerId": 2
    },
    {
      "id": 2,
      "name": "Spots",
      "breed": "Dalmation",
      "locationId": 2,
      "treatment": "Shampoo",
      "customerId": 2
    },
    {
      "id": 3,
      "name": "Jumps",
      "breed": "Blue Heeler",
      "locationId": 1,
      "treatment": "Obedience",
      "customerId": 2
    },
    {
      "id": 4,
      "name": "Spot4",
      "breed": "Dalmation",
      "locationId": 1,
      "treatment": "Nail Trimming",
      "customerId": 2
    }
]


def get_all_animals():
    return ANIMALS

# Function with a single parameter
def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal