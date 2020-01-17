import random
import string

from .models import Collection, Card


def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def load_db():
    # If we've got card, we're not doing anything here
    if Card.objects.all().count() > 0:
        return

    # Initialize collections
    empyrean_collection, _ = Collection.objects.get_or_create(
        name="Empyrean",
        bonus="2,0,0"
    )

    vosh_collection, _ = Collection.objects.get_or_create(
        name="Vosh",
        bonus="0,2,0"
    )

    # Initialize Cards
    # 2 cards of level 2
    power = 3
    damage = 4
    for i in range(2):
        c = Card(
            name=random_string(10),
            level=2,
            collection=empyrean_collection,
            base_power=power,
            base_damage=damage
        )
        c.save()
        c = Card(
            name=random_string(10),
            level=2,
            collection=vosh_collection,
            base_power=power,
            base_damage=damage
        )
        c.save()

    # 5 cards of level 3
    power = 5
    damage = 6
    for i in range(5):
        c = Card(
            name=random_string(10),
            level=3,
            collection=empyrean_collection,
            base_power=power,
            base_damage=damage
        )
        c.save()
        c = Card(
            name=random_string(10),
            level=3,
            collection=vosh_collection,
            base_power=power,
            base_damage=damage
        )
        c.save()

    # 2 cards of level 4
    power = 7
    damage = 7
    for i in range(2):
        c = Card(
            name=random_string(10),
            level=4,
            collection=empyrean_collection,
            base_power=power,
            base_damage=damage
        )
        c.save()
        c = Card(
            name=random_string(10),
            level=4,
            collection=vosh_collection,
            base_power=power,
            base_damage=damage
        )
        c.save()

    # 1 cards of level 5
    power = 10
    damage = 8
    c = Card(
        name=random_string(10),
        level=5,
        collection=empyrean_collection,
        base_power=power,
        base_damage=damage
    )
    c.save()
    c = Card(
        name=random_string(10),
        level=5,
        collection=vosh_collection,
        base_power=power,
        base_damage=damage
    )
    c.save()
