from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'Visakhapatnam'
    dest1.desc = 'The City of Destiny'
    dest1.img = 'vizag.jpg'
    dest1.price = 18000
    dest1.special_offer=True

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'Dum ki Biryani'
    dest2.img = 'hyderabad.jpg'
    dest2.price = 13000
    dest2.special_offer = False

    dest3 = Destination()
    dest3.name = 'Banglore'
    dest3.desc = 'Green City'
    dest3.img = 'banglore.jpg'
    dest3.price = 20000
    dest3.special_offer=False

    dest4 = Destination()
    dest4.name = 'Kerala'
    dest4.desc = 'River Boating'
    dest4.img = 'kerala.jpg'
    dest4.price = 21000
    dest4.special_offer=True


    travs1 = Travels()
    travs1.imag = 'delhi.jpg'
    travs1.date = '26 Dec'
    travs1.head = 'Best tips to travel'
    travs1.type = 'life style & travel'
    travs1.body = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Integer vitae justo eget magna
                fermentum iaculis eu.
                Augue eget arcu dictum varius. Convallis a cras semper auctor neque vitae tempus.
                Nec feugiat in fermentum posuere urna. Nunc sed augue lacus viverra vitae congue eu consequat ac.
                Dignissim convallis aenean et tortor at. Volutpat ac tincidunt vitae semper. Platea dictumst
                quisque sagittis purus sit amet volutpat. Pulvinar neque laoreet suspendisse interdum consectetur.
                Odio facilisis mauris sit amet. Pellentesque eu tincidunt tortor aliquam nulla. Sem integer vitae justo
                eget magna fermentum. Sollicitudin ac orci phasellus egestas. Consectetur a erat nam at lectus urna duis.'''

    trans2 = Travels()
    trans2.imag = 'banglore.jpg'
    trans2.date = '27 Dec'
    trans2.head = 'Best tips to travel'
    trans2.type = 'life style & travel'
    trans2.body = '''A lacus vestibulum sed arcu non odio euismod lacinia at. Amet nisl purus in mollis nunc. Vestibulum sed arcu non odio. Mollis aliquam ut porttitor leo. Eleifend quam adipiscing vitae proin sagittis. Cras ornare arcu dui vivamus arcu felis bibendum ut tristique. Tristique nulla aliquet enim tortor at auctor urna. Facilisis leo vel fringilla est ullamcorper eget nulla. Quisque non tellus orci ac. Posuere lorem ipsum dolor sit amet consectetur adipiscing elit duis.'''

    trans3 = Travels()
    trans3.imag = 'hyderabad.jpg'
    trans3.date = '26 Dec'
    trans3.head = 'Best tips to travel'
    trans3.type = 'life style & travel'
    trans3.body = '''Convallis a cras semper auctor neque vitae tempus quam. Consequat ac felis donec et odio. Tempus imperdiet nulla malesuada pellentesque elit. Ullamcorper sit amet risus nullam. Varius sit amet mattis vulputate enim nulla aliquet porttitor lacus. Volutpat commodo sed egestas egestas fringilla. Sit amet massa vitae tortor condimentum lacinia quis vel eros. Cursus metus aliquam eleifend mi in nulla. Dignissim convallis aenean et tortor at risus viverra. Lacus laoreet non curabitur gravida arcu ac tortor. Et tortor at risus viverra adipiscing at. Quis risus sed vulputate odio ut enim blandit volutpat maecenas. Scelerisque felis imperdiet proin fermentum leo vel orci porta non. Velit egestas dui id ornare arcu odio ut. Eget nunc scelerisque viverra mauris in. Cursus eget nunc scelerisque viverra mauris in. Sed viverra tellus in hac habitasse platea dictumst. Molestie ac feugiat sed lectus vestibulum.'''

    client1=Clients()
    client1.title = 'Amazing Places'
    client1.heading = 'Testimonials'
    client1.client = 'Vamsi'
    client1.type = 'Client/User'
    client1.data = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Integer vitae justo eget magna
                fermentum iaculis eu.
                Augue eget arcu dictum varius. Convallis a cras semper auctor neque vitae tempus.
                Nec feugiat in fermentum posuere urna.'''

    client2=Clients()
    client2.client = 'Harish'
    client2.type = 'Client/User'
    client2.data = '''
                Augue eget arcu dictum varius. Convallis a cras semper auctor neque vitae tempus.
                Nec feugiat in fermentum posuere urna. Nunc sed augue lacus viverra vitae congue eu consequat ac.
                Dignissim Platea dictumst
                quisque sagittis purus sit amet volutpat. Pulvinar neque laoreet suspendisse interdum consectetur.
                Odio facilisis mauris sit amet. Pellentesque eu tincidunt tortor aliquam nulla. Sem integer vitae justo
                eget magna fermentum. Sollicitudin ac orci phasellus egestas. Consectetur a erat nam at lectus urna duis'''

    client3=Clients()
    client3.client = 'Gireesh'
    client3.type = 'Client/User'
    client3.data = '''ut labore et dolore magna aliqua. Integer vitae justo eget magna
                fermentum iaculis eu.
                Augue eget arcu dictum varius. Convallis a cras semper auctor neque vitae tempus.
                Nec feugiat in fermentum posuere urna. Nunc sed augue lacus viverra vitae congue eu consequat ac.
                Dignissim convallis aenean et tortor at. Volutpat ac tincidunt vitae semper. Platea dictumst
                quisque sagittis purus sit.
                Odio facilisis mauris sit amet. Pellentesque eu tincidunt tortor aliquam nulla. Sem integer vitae justo
                eget magna fermentum. Sollicitudin ac orci phasellus egestas. Consectetur a erat nam at lectus urna duis'''

    dests = [dest1, dest2, dest3, dest4]
    travs=[travs1,trans2,trans3]
    client_all = [client1,client2,client3]
    return render(request, "index.html", {'dests': dests,'travs':travs,'clients':client_all})

def contact(request):
    return render(request,'contact.html')