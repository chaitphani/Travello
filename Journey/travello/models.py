from django.db import models
import datetime
# Create your models here.

class Destination:
    id: int
    name: str
    img: str
    desc: str
    price: int
    special_offer: bool

class Travels:
    id : int
    imag : str
    date : str
    head : str
    type : str
    body : str


class Clients:
    id : int
    title : str
    heading : str
    data : str
    client : str
    type : str