>>> Product(name="test").save
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Product' is not defined
from mongoengine import *

class Product(Document):
    name = StringField(max_length=200)
pip install mongoengine
from mongoengine import *

class Product(Document):
    name = StringField(max_length=200)


from mongoengine import connect

connect('db1')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# MongoDB settings
MONGODB_DATABASES = {
    'default': {'name': 'db1'}
}


from mongoengine import connect

connect('db1')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# MongoDB settings
MONGODB_DATABASES = {
    'default': {'name': 'db1'}
}   

AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy'
    }
}

ROOT_URLCONF='urls'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'django.contrib.auth',
    'mongoengine.django.mongo_auth',
    
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

SESSION_ENGINE = 'mongoengine.django.sessions'
AUTH_USER_MODEL = 'mongo_auth.MongoUser'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
runfile('C:/Users/santh/.spyder-py3/pro2.py', wdir='C:/Users/santh/.spyder-py3')
print("Hello " + User_Name + """. 
Tonic is a simple Python chatbot made in order to test things such as boolean logic
and variable definition.
(Also remember to speak to the bot in lowercase, without punctuation.)""")
while (str1 != "quit"): # You need an exit condition here
    str1 = input("Say something: ")
    #"hello" //////////////////////////////////////////
    if "hello" in str1:
        print("Hi " + User_Name + "! (I read this as the 'hello' greeting.")
    #"hi" //////////////////////////////////////////
    if "hi" in str1:
        print("Hi " + User_Name + "! (I read this as the 'hi' greeting.")
    #"how are you?" //////////////////////////////////////////
    if "how are you" in str1:
        print("good, how about you? (I read this as you asking 'how are you'.)")
        mood = input("Enter Mood: ")
        if "good" in mood:
            print("Nice to hear " + User_Name + "! (I read this as you being in a good mood.)")
        if "bad" in mood:
            print("I hope you feel better soon, " + User_Name + "! (I read this as you being in a bad mood.)")
    #"name length" //////////////////////////////////////////
    if "name length" in str1:
        print( "Your name is " + len(User_Name) + "letters long. (I read this as you asking how long your name is.")
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("bot")    # create an instance of ChatBot and name it.
chatbot.set_trainer(ListTrainer)

data = ["你好",
        "我很高兴认识你"]    # add data for training

chatbot.train(data)        # train the bot

while True:
    try:
        user_input = input("you - ")                 # ask something to bot
        bot_input = chatbot.get_response(user_input)   # get curresponding output from bot
        print("bot - ",bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
List Trainer: [####################] 100%
you - 你好
bot -  我很高兴认识你
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("bot")    # create an instance of ChatBot and name it.
chatbot.set_trainer(ListTrainer)

data = ["你好",
        "我很高兴认识你"]    # add data for training

chatbot.train(data)        # train the bot

while True:
    try:
        user_input = input("you - ")                 # ask something to bot
        bot_input = chatbot.get_response(user_input)   # get curresponding output from bot
        print("bot - ",bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
ListTrainer: [####################] 100%
you - 你好
bot -  我很高兴认识你
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("bot")    # create an instance of ChatBot and name it.
chatbot.set_trainer(ListTrainer)

data = ["你好",
        "我很高兴认识你"]    # add data for training

chatbot.train(data)        # train the bot

while True:
    try:
        user_input = input("you - ")                 # ask something to bot
        bot_input = chatbot.get_response(user_input)   # get curresponding output from bot
        print("bot - ",bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
ListTrainer: [####################] 100%
you - 你好
ChatBot -  我很高兴认识你
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("bot")    # create an instance of ChatBot and name it.
chatbot.set_trainer(ListTrainer)

data = ["你好",
        "我很高兴认识你"]    # add data for training

chatbot.train(data)        # train the bot

while True:
    try:
        user_input = input("you - ")                 # ask something to bot
        bot_input = chatbot.get_response(user_input)   # get curresponding output from bot
        print("bot - ",bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
ListTrainer: [####################] 100%
you - 你好
Chatterbot -  我很高兴认识你
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("bot")    # create an instance of ChatBot and name it.
chatbot.set_trainer(ListTrainer)

data = ["你好",
        "我很高兴认识你"]    # add data for training

chatbot.train(data)        # train the bot

while True:
    try:
        user_input = input("you - ")                 # ask something to bot
        bot_input = chatbot.get_response(user_input)   # get curresponding output from bot
        print("bot - ",bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
ListTrainer: [####################] 100%
you - 你好
Bot -  我很高兴认识你
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("bot")    # create an instance of ChatBot and name it.
chatbot.set_trainer(ListTrainer)

data = ["你好",
        "我很高兴认识你"]    # add data for training

chatbot.train(data)        # train the bot

while True:
    try:
        user_input = input("you - ")                 # ask something to bot
        bot_input = chatbot.get_response(user_input)   # get curresponding output from bot
        print("bot - ",bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
ListTrainer: [####################] 100%
you - 你好
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("bot")    # create an instance of ChatBot and name it.
chatbot.set_trainer(ListTrainer)

data = ["你好",
        "我很高兴认识你"]    # add data for training

chatbot.train(data)        # train the bot

while True:
    try:
        user_input = input("you - ")                 # ask something to bot
        bot_input = chatbot.get_response(user_input)   # get curresponding output from bot
        print("bot - ",bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
ListTrainer: [####################] 100%
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("bot")    # create an instance of ChatBot and name it.
chatbot.set_trainer(ListTrainer)

data = ["你好",
        "我很高兴认识你"]    # add data for training

chatbot.train(data)        # train the bot

while True:
    try:
        user_input = input("you - ")                 # ask something to bot
        bot_input = chatbot.get_response(user_input)   # get curresponding output from bot
        print("bot - ",bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
ListTrainer: [####################] 100%
you -"你好"
Bot -  "我很高兴认识你
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("bot")    # create an instance of ChatBot and name it.
chatbot.set_trainer(ListTrainer)

data = ["你好",
        "我很高兴认识你"]    # add data for training

chatbot.train(data)        # train the bot

while True:
    try:
        user_input = input("you - ")                 # ask something to bot
        bot_input = chatbot.get_response(user_input)   # get curresponding output from bot
        print("bot - ",bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
ListTrainer: [####################] 100%
you -"你好"
sdas -  "我很高兴认识你
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("bot")    # create an instance of ChatBot and name it.
chatbot.set_trainer(ListTrainer)

data = ["你好",
        "我很高兴认识你"]    # add data for training

chatbot.train(data)        # train the bot

while True:
    try:
        user_input = input("you - ")                 # ask something to bot
        bot_input = chatbot.get_response(user_input)   # get curresponding output from bot
        print("bot - ",bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
ListTrainer: [####################] 100%
you -"你好"
data -  "我很高兴认识你
@client.event
async def on_message(message) :
    content = message.content.upper()
    
    mood = 2 # you hard-code your mood here!
    
    if content in responses: # might enter here
        
        if mood <= 0: # mood = 2, so won't enter here
            await client.send_message(message.channel, responses[content]["RANG"])
        
        if mood == 1: # mood = 2, so won't enter here
            await client.send_message(message.channel, responses[content]["ANG"])
        
        if mood == 2: # mood = 2, so ALWAYS here!
            await client.send_message(message.channel, responses[content]["NEU"])
        
        if mood == 3: # mood = 2, so won't enter here
            await client.send_message(message.channel, responses[content]["HAP"])
        
        if mood == 4: # mood = 2, so won't enter here
            await client.send_message(message.channel, responses[content]["RHAP"])
    
    if content in insults: # might enter here
        mood = mood - 0.25 # mood was 2, not it is 1.75
        
        if mood <= 0: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["RANG"])
        
        if mood == 1: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["ANG"])
        
        if mood == 2: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["NEU"])
        
        if mood == 3: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["HAP"])
        
        if mood == 4: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["RHAP"])
,    if content in insults: # might enter here
        mood = mood - 0.25 # mood was 2, now it is 1.75
        
        if mood <= 0: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["RANG"])
        
        elif mood <= 1: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["ANG"])
        
        elif mood <= 2: # mood = 1.75, so ENTER HERE
            await client.send_message(message.channel, insults[content]["NEU"])
        
        elif mood <= 3: # elif, so skipped
            await client.send_message(message.channel, insults[content]["HAP"])
        
        elif mood <= 4: # elif, so skipped
            await client.send_message(message.channel, insults[content]["RHAP"])
,mood = 2
@client.event
async def on_message(message) :
    content = message.content.upper()
    
    global mood
    
    if content in responses:
        .
        .
        .
@client.event
async def on_message(message) :
    content = message.content.upper()
    
    mood = 2 # you hard-code your mood here!
    
    if content in responses: # might enter here
        
        if mood <= 0: # mood = 2, so won't enter here
            await client.send_message(message.channel, responses[content]["RANG"])
        
        if mood == 1: # mood = 2, so won't enter here
            await client.send_message(message.channel, responses[content]["ANG"])
        
        if mood == 2: # mood = 2, so ALWAYS here!
            await client.send_message(message.channel, responses[content]["NEU"])
        
        if mood == 3: # mood = 2, so won't enter here
            await client.send_message(message.channel, responses[content]["HAP"])
        
        if mood == 4: # mood = 2, so won't enter here
            await client.send_message(message.channel, responses[content]["RHAP"])
    
    if content in insults: # might enter here
        mood = mood  0.25 # mood was 2, not it is 1.75
        
        if mood <= 0: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["RANG"])
        
        if mood == 1: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["ANG"])
        
        if mood == 2: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["NEU"])
        
        if mood == 3: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["HAP"])
        
        if mood == 4: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["RHAP"])
,    if content in insults: # might enter here
        mood = mood - 0.25 # mood was 2, now it is 1.75
        
        if mood <= 0: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["RANG"])
        
        elif mood <= 1: # mood = 1.75, so won't enter here
            await client.send_message(message.channel, insults[content]["ANG"])
        
        elif mood <= 2: # mood = 1.75, so ENTER HERE
            await client.send_message(message.channel, insults[content]["NEU"])
        
        elif mood <= 3: # elif, so skipped
            await client.send_message(message.channel, insults[content]["HAP"])
        
        elif mood <= 4: # elif, so skipped
            await client.send_message(message.channel, insults[content]["RHAP"])
,mood = 2
@client.event
async def on_message(message) :
    content = message.content.upper()
    
    global mood
    
    if content in responses:
        .
        .
        .
async def start_job(job_id, delay):
    """Start job ID after a certain amount of delay."""
    queue_time = _current_time()
    await asyncio.sleep(delay)
    start_time = _current_time()
    return JobRecord(job_id, queue_time, start_time)
def main():
    # This is a tuple of integers
    immutable = (1, 2, 3, 4)
    
    # It can be indexed like a list
    assert immutable[0] == 1
    assert immutable[-1] == 4
    
    # It can be sliced like a list
    assert immutable[1:3] == (2, 3)
    assert immutable[3:4] == (4,)
    assert immutable[1::2] == (2, 4)
    assert immutable[::-1] == (4, 3, 2, 1)
    
    # It can be iterated over like a list
    for ix, number in enumerate(immutable):
        assert immutable[ix] == number
    
    # But its contents cannot be changed. As an alternative, we can
    # create new tuples from existing tuples
    bigger_immutable = immutable + (5, 6)
    assert bigger_immutable == (1, 2, 3, 4, 5, 6)
    smaller_immutable = immutable[0:2]
    assert smaller_immutable == (1, 2)
    
    # We use tuples when the number of items is consistent. An example
    # where this can help is a 2D game with X and Y coordinates. Using a
    # tuple with two numbers can ensure that the number of coordinates
    # doesn't change to one, three, four, etc.
    moved_count = 0
    pos_x, pos_y = (0, 0)
    for i in range(1, 5, 2):
        moved_count += 1
        pos_x, pos_y = (pos_x + 10 * i, pos_y + 15 * i)
    assert moved_count == 2
    assert pos_x == 40 and pos_y == 60
output = []
for i in mountainbikes:
    if prices[i] < price:
        if travels[i] in travel:
            output.append(i)
print(output)
,output = [i for i in mountainbikes if prices[i] < price and travels[i] in travel]
import time
import random
def dateandfeels():
  """
  docstring
  """
  toPrint="";
  today = (time.strftime("%H:%M:%S"))
  toPrint+=today;
  time1 = (time.strftime("%d/%m/%Y"))
  toPrint+=" "+time1;
  whole = int(15)
  toPrint+= " "+str(whole)
  float1 = float(0.056)
  toPrint+=" "+str(float1);
  mood = ['happy', 'sad', 'moody', 'pythonic']
  toPrint+=" "+''.join(mood);
  moody = str((random.choice(mood)))
  toPrint+=" "+moody;
  print("Here print the string: \n")
  print (toPrint+"\n")
  print("Here use printf like to print all variables: \n")
  print ("Today is %s. Time is %s. My number of choice is %d and my float of choice is %f. Also I'm feeling a bit %s today" %(today,time1,whole,float1,moody))

dateandfeels()

## ---(Sun Oct 16 12:39:36 2022)---
from turtle import *
import turtle
turtle.bgcolor('black')
turtle.pencolor('red')
turtle.hideturtle()
turtle.speed()
#curve01
def curve01(a,d):
    for i in range(d):
        turtle.right(a)
        turtle.forward(1)

#making eye
turtle.width(15)
turtle.penup()
turtle.right(90)
turtle.forward(85)
turtle.left(90)
turtle.forward(35)
turtle.pendown()
turtle.fillcolor('white')
turtle.begin_fill()
turtle.left(55)
curve01(0.09,100)
curve01(0.2,100)
turtle.forward(70)
turtle.right(90)
curve01(0.5,100)
curve01(00,30)
curve01(0.3,50)
curve01(0.6,50)
turtle.forward(50)
turtle.right(47)
curve01(0.1,95)
turtle.end_fill()

#changing
turtle.penup()
turtle.left(36)
turtle.forward(70)
turtle.pendown()

#curve02
def curve02(a,d):
    for i in range(d):
        turtle.left(a)
        turtle.forward(1)

#second eye
turtle.fillcolor('white')
turtle.begin_fill()
turtle.right(55)
curve02(0.09,100)
curve02(0.2,100)
turtle.forward(70)
turtle.left(90)
curve02(0.5,100)
curve02(00,30)
curve02(0.3,50)
curve02(0.6,50)
turtle.forward(50)
turtle.left(47)
curve02(0.1,95)
turtle.end_fill()

turtle.penup()
turtle.width(0)
turtle.right(49)
turtle.forward(30)
turtle.left(102)  #100.40
turtle.forward(145)
turtle.pencolor('red')


#making left face
turtle.fillcolor('red')
turtle.begin_fill()
turtle.speed()
turtle.pendown()
turtle.left(90)
curve01(5,20)
turtle.left(175)
turtle.forward(50)
turtle.left(25)
turtle.forward(28)
turtle.right(160)
turtle.forward(170)
curve02(0.2,65)
turtle.right(60)
curve01(0.1,140)
curve01(0.5,50)
turtle.left(180)
curve02(0.2,150)
curve02(0.1,95)
turtle.left(127)
turtle.forward(5)
curve01(2,20)
turtle.right(30)
turtle.forward(90)
turtle.right(7)
turtle.forward(75)
turtle.right(160)
turtle.forward(100)
curve02(0.1,105)
turtle.right(70)
curve01(0.2,200)
curve01(0.3,70)
turtle.left(175)
curve02(0.2,150)
curve02(0.3,150)
turtle.forward(20)
turtle.left(65)
curve01(0.1,120)
curve01(0.010,105)
turtle.right(10)
curve01(0.2,110)
turtle.right(60)
curve01(0.3,138)
turtle.right(30)
curve01(0.2,160)
turtle.left(150)
curve02(0.2,100)
curve02(0.1,150)
turtle.forward(70)
curve02(0.4,40)
turtle.left(160)
curve01(0.1,60)
turtle.left(7)
curve01(0.1,120)
curve01(0.2,30)
turtle.forward(20)
turtle.right(140)
curve02(0.2,40)
turtle.right(50)
curve02(0.2,70)
turtle.right(8)
curve02(0.1,70)
curve02(0.5,50)
turtle.left(153)
curve01(0.1,170)
turtle.right(81)
curve02(0.2,20)
turtle.right(3)
curve02(0.1,62)
turtle.right(153) #..
curve01(0.1,63) 
turtle.left(50)
curve02(0.1,175)
turtle.left(60)
turtle.forward(7)
turtle.end_fill()


#going to replicate
turtle.left(92.15)
turtle.penup()
turtle.forward(417)
turtle.pendown()

turtle.fillcolor('red')
turtle.begin_fill()
#right face 
turtle.right(90)
curve02(5,20)
turtle.right(175)
turtle.forward(50)
turtle.right(25)
turtle.forward(28)
turtle.left(160)
turtle.forward(170)
curve01(0.2,65)
turtle.left(60)
curve02(0.1,140)
curve02(0.5,50)
turtle.right(180)
curve01(0.2,150)
curve01(0.1,95)
turtle.right(127)
turtle.forward(5)
curve02(2,20)
turtle.left(30)
turtle.forward(90)
turtle.left(7)
turtle.forward(75)
turtle.left(160)
turtle.forward(100)
curve01(0.1,105)
turtle.left(70)
curve02(0.2,200)
curve02(0.3,70)
turtle.right(175)
curve01(0.2,150)
curve01(0.3,150)
turtle.forward(20)
turtle.right(65)
curve02(0.1,120)
curve02(0.010,105)
turtle.left(10)
curve02(0.2,110)
turtle.left(60)
curve02(0.3,138)
turtle.left(30)
curve02(0.2,160)
turtle.right(150)
curve01(0.2,100)
curve01(0.1,150)
turtle.forward(70)
curve01(0.4,40)
turtle.right(160)
curve02(0.1,60)
turtle.right(7)
curve02(0.1,120)
curve02(0.2,30)
turtle.forward(20)
turtle.left(140)
curve01(0.2,40)
turtle.left(50)
curve01(0.2,70)
turtle.left(8)
curve01(0.1,70)
curve01(0.5,50)
turtle.right(153)
curve02(0.1,170)
turtle.left(81)
curve01(0.2,20)
turtle.left(3)
curve01(0.1,62)
turtle.left(153) #..
curve02(0.1,63) 
turtle.right(50)
curve01(0.1,100)  #0.1
turtle.forward(75)
turtle.right(75)
turtle.forward(2)
turtle.end_fill()
turtle.done()
import turtle
a=turtle.Turtle()
a.getscreen().bgcolor("black")
a.penup()
a.goto(-200, 100)
a.pendown()
a.color("yellow")
a.speed(25)
def star(turtle, size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range (5):
            turtle.pensize(2)
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
            turtle.end_fill()
star(a, 360)
turtle.done()
from turtle import *

speed(0)
bgcolor('black')
color('orange')
hideturtle()

n = 1
p = True

while True:
    circle(n)
    if p:
        n = n - 1
    else:
        n = n + 1
    
    if n == 0 or n == 60:
        p = not p
    
    left(1)
    forward(3)

done()
import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
n = 70
h = 0
for i in range (360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range (2):
        t.left(2)
        t.circle(100)
import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
n = 70
h = 0
for i in range (360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range (2):
        t.left(2)
        t.triangle(100)
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
pip install chatterbot
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()

## ---(Mon Oct 17 14:29:06 2022)---
import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()
mic=sr.Microphone(device_index=1)

with mic as source:
    audio=r.listen(source)


def speak(message):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-10)
    engine.say('Google says {}'.format(message))
    engine.runAndWait()


print(r.recognize_google(audio))
speak(r.recognize_google(audio))
runfile('C:/Users/santh/.spyder-py3/pro1.py', wdir='C:/Users/santh/.spyder-py3')

## ---(Tue Oct 18 21:46:36 2022)---
import speech_recognition as sr
import pyttsx3
import pyaudio

r=sr.Recognizer()
mic=sr.Microphone(device_index=1)

with mic as source:
    audio=r.listen(source)


def speak(message):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-10)
    engine.say('Google says {}'.format(message))py
    engine.runAndWait()


print(r.recognize_google(audio))
speak(r.recognize_google(audio))
import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()
mic=sr.Microphone(device_index=1)

with mic as source:
    audio=r.listen(source)


def speak(message):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-10)
    engine.say('Google says {}'.format(message))
    engine.runAndWait()


print(r.recognize_google(audio))
speak(r.recognize_google(audio))
import speech_recognition as sr
import pyttsx3
import pyaudio

r=sr.Recognizer()
mic=sr.Microphone(device_index=1)

with mic as source:
    audio=r.listen(source)


def speak(message):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-10)
    engine.say('Google says {}'.format(message))
    engine.runAndWait()


print(r.recognize_google(audio))
speak(r.recognize_google(audio))


from chatterbot import ChatBot

# Inorder to train our bot, we have
# to import a trainer package
# "ChatterBotCorpusTrainer"
from chatterbot.trainers import ChatterBotCorpusTrainer


# Give a name to the chatbot “corona bot”
# and assign a trainer component.
chatbot=ChatBot('corona bot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations" )

response = chatbot.get_response('What is your Number')
print(response)

response = chatbot.get_response('Who are you?')
print(response)
pip3 uninstall PyCrypto
pip3 install -U PyCryptodome

pip uninstall PyCrypto
pip install -U PyCryptodome


from chatterbot import ChatBot

# Inorder to train our bot, we have
# to import a trainer package
# "ChatterBotCorpusTrainer"
from chatterbot.trainers import ChatterBotCorpusTrainer


# Give a name to the chatbot “corona bot”
# and assign a trainer component.
chatbot=ChatBot('corona bot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations" )

response = chatbot.get_response('What is your Number')
print(response)

response = chatbot.get_response('Who are you?')
print(response)
pip install --upgrade flask_sqlalchemy


from chatterbot import ChatBot

# Inorder to train our bot, we have
# to import a trainer package
# "ChatterBotCorpusTrainer"
from chatterbot.trainers import ChatterBotCorpusTrainer


# Give a name to the chatbot “corona bot”
# and assign a trainer component.
chatbot=ChatBot('corona bot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations" )

response = chatbot.get_response('What is your Number')
print(response)

response = chatbot.get_response('Who are you?')
print(response)
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')

trainer = ListTrainer(bot)

trainer.train([
    'Hi',
    'Hello',
    'I need roadmap for Competitive Programming',
    'Just create an account on GFG and start',
    'I have a query.',
    'Please elaborate, your concern',
    'How long it will take to become expert in Coding ?',
    'It usually depends on the amount of practice.',
    'Ok Thanks',
    'No Problem! Have a Good Day!'
])

while True:
    request=input('you :')
    if request == 'OK' or request == 'ok':
        print('Bot: bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:', response)
pip install your_module --upgrade
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')

trainer = ListTrainer(bot)

trainer.train([
    'Hi',
    'Hello',
    'I need roadmap for Competitive Programming',
    'Just create an account on GFG and start',
    'I have a query.',
    'Please elaborate, your concern',
    'How long it will take to become expert in Coding ?',
    'It usually depends on the amount of practice.',
    'Ok Thanks',
    'No Problem! Have a Good Day!'
])

while True:
    request=input('you :')
    if request == 'OK' or request == 'ok':
        print('Bot: bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:', response)