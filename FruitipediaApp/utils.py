from FruitipediaApp.appprofile.models import Profile
from FruitipediaApp.fruit.models import Fruit


def get_profile():
    return Profile.objects.first()

def get_all_fruits():
    return Fruit.objects.all()