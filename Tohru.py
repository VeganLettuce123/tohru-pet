# Tohru for desktop by VeganLettuce123 (also builadble in mac)  <--- Didn't work lol

# Importes al código

from tkinter import *
import time
import sched
import os
import sys
import webbrowser
import random
import rotatescreen
from datetime import datetime, timedelta
from threading import Timer
from playsound import playsound
import psutil

#from win10toast import ToastNotifier

#from pypresence.presence import Presence


# client_id = '859148891215495169'  # Put your client ID here
#RPC = Presence(client_id)
# RPC.connect()

# RPC.update(state="The big fall", large_image="http://pm1.narvii.com/6628/15acbe8f0e1c18f7b9cdc686e9fb42108eee2fba_00.jpg",
# large_text="Tohru", start=time.time())


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Variables y paths

lastClickX = 0
lastClickY = 0


# Images and GIFs


Tohru = resource_path('images/Tohru.gif')

FakeTohru = resource_path('images/classytohru.gif')

HappyTohru = resource_path('images/Tohru_music.gif')

SHINYT = resource_path('images/shiny_tohru.gif')

tohru_discord_1: resource_path('images/discord-rpc.png')

SleepyT = resource_path('images/sleepytohru.gif')

Elma = resource_path('images/Elma.gif')

Lucoa = resource_path('images/Lucoa.gif')

Ilulu = resource_path('images/Ilulu.gif')

Kanna = resource_path('images/Kanna.gif')

GuraSpin = resource_path('images/gura.gif')

Pusheenwalk = resource_path('images/Pusheen.gif')

maikaspin = resource_path('images/maikaspin.gif')

Padoru = resource_path('images/padorumoment.gif')

KOBAYASHI = resource_path('images/Kobayashi.png')


# Audios

sad_song = resource_path('audios/sad_song.wav')

padoru_song = resource_path('audios/padorusong.wav')

# Icons for notif

sleepy_icon = resource_path('notif/sleep.ico')


wakey_icon = resource_path('notif/wake.ico')


# os.system(JIJIJI_JAH)


# Funciones rápidas


def killtoh():
    tohru.destroy()


def rick():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


# Useless shit

def funnyscreen(self):
    screen = rotatescreen.get_primary_display()
    screen.set_landscape_flipped()


def unfunnyscreen(self):
    screen = rotatescreen.get_primary_display()
    screen.set_landscape()


def helpme():

    x, y = str(random.randint(0, 1700)), str(random.randint(0, 700))

    classy_window.geometry("+%s+%s" % (x, y))
    classy_window.attributes('-alpha', 0.5)
    tohru.after(10, helpme)


def watchingstill():

    classy_window.geometry("+0+0")
    classy_window.attributes('-alpha', 0.2)


# Real Tohru window properties
a = random.randint(-0, 1280)
b = random.randint(-0, 700)

tohru = Tk()
tohru.attributes('-topmost', 1)
tohru.geometry("+{}+{}".format(a, b))
tohru.overrideredirect(1)
tohru.resizable(TRUE, TRUE)

tohruframes = [PhotoImage(file=Tohru, format='gif -index %i' % (i))
               for i in range(38)]


# Tohru GIF

def default(tind):
    tframe = tohruframes[tind]
    tind += 2
    if tind > 37:
        tind = 0
    tlabel.configure(image=tframe, bg='grey')
    tohru.wm_attributes("-transparentcolor", 'grey')

    tohru.after(100, default, tind)


tlabel = Label(tohru)
tlabel.pack()
tohru.after(0, default, 0)


# Elma window properties


elma_window = Toplevel(tohru)
elma_window.attributes('-topmost', 1)
elma_window.geometry("-200000+0")
elma_window.overrideredirect(1)
elma_window.resizable(TRUE, TRUE)
elmaframes = [PhotoImage(file=Elma, format='gif -index %i' % (i))
              for i in range(38)]


# Elma GIF

def elmagif(eind):
    eframe = elmaframes[eind]
    eind += 2
    if eind > 37:  # With this condition it will play gif infinitely
        eind = 0
    elabel.configure(image=eframe, bg='black')
    elma_window.wm_attributes("-transparentcolor", 'black')

    elma_window.after(100, elmagif, eind)


elabel = Label(elma_window)
elabel.pack()
elma_window.after(10, elmagif, 0)


# Lucoa window properties

e = random.randint(-0, 1280)
f = random.randint(-0, 700)

lucoa_window = Toplevel(tohru)
lucoa_window.attributes('-topmost', 1)
lucoa_window.geometry("-200000+0")
lucoa_window.overrideredirect(1)
lucoa_window.resizable(TRUE, TRUE)
lucoaframes = [PhotoImage(file=Lucoa, format='gif -index %i' % (i))
               for i in range(38)]

# Lucoa GIF


def lucoagif(luind):
    luframe = lucoaframes[luind]
    luind += 2
    if luind > 37:  # With this condition it will play gif infinitely
        luind = 0
    lulabel.configure(image=luframe, bg='black')
    lucoa_window.wm_attributes("-transparentcolor", 'black')

    lucoa_window.after(100, lucoagif, luind)


lulabel = Label(lucoa_window)
lulabel.pack()
lucoa_window.after(10, lucoagif, 0)


# Ilulu window properties

g = random.randint(-0, 1280)
h = random.randint(-0, 700)

ilulu_window = Toplevel(tohru)
ilulu_window.attributes('-topmost', 1)
ilulu_window.geometry("-200000+0")
ilulu_window.overrideredirect(1)
ilulu_window.resizable(TRUE, TRUE)
iluluframes = [PhotoImage(file=Ilulu, format='gif -index %i' % (i))
               for i in range(38)]

# Illulu GIF


def ilulugif(iluind):
    iluframe = iluluframes[iluind]
    iluind += 2
    if iluind > 37:  # With this condition it will play gif infinitely
        iluind = 0
    ilulabel.configure(image=iluframe, bg='black')
    ilulu_window.wm_attributes("-transparentcolor", 'black')

    ilulu_window.after(100, ilulugif, iluind)


ilulabel = Label(ilulu_window)
ilulabel.pack()
ilulu_window.after(10, ilulugif, 0)


# Kanna window properties

i = random.randint(-0, 1280)
j = random.randint(-0, 700)

kanna_window = Toplevel(tohru)
kanna_window.attributes('-topmost', 1)
kanna_window.geometry("-200000+0")
kanna_window.overrideredirect(1)
kanna_window.resizable(TRUE, TRUE)
kannaframes = [PhotoImage(file=Kanna, format='gif -index %i' % (i))
               for i in range(38)]

# Kanna GIF


def kannagif(kaind):
    kaframe = kannaframes[kaind]
    kaind += 2
    if kaind > 37:  # With this condition it will play gif infinitely
        kaind = 0
    kalabel.configure(image=kaframe, bg='black')
    kanna_window.wm_attributes("-transparentcolor", 'black')

    kanna_window.after(100, kannagif, kaind)


kalabel = Label(kanna_window)
kalabel.pack()
kanna_window.after(10, kannagif, 0)

# Classy tohru

classy_window = Toplevel(tohru)
classy_window.attributes('-topmost', 1)
classy_window.geometry("-200000+0")
classy_window.overrideredirect(1)
classy_window.resizable(TRUE, TRUE)
classyframes = [PhotoImage(file=FakeTohru, format='gif -index %i' % (i))
                for i in range(38)]


def classygif(clasind):
    claframe = classyframes[clasind]
    clasind += 2
    if clasind > 37:  # With this condition it will play gif infinitely
        clasind = 0
    classylabel.configure(image=claframe, bg='black')
    classy_window.wm_attributes("-transparentcolor", 'black')

    classy_window.after(100, classygif, clasind)


classylabel = Label(classy_window)
classylabel.pack()
classy_window.after(10, classygif, 0)


# Kobayashi window properties
height = int(tohru.winfo_screenheight())
floordef = height - 475

kobayashi_window = Toplevel(tohru)
kobayashi_window.attributes('-topmost', 1)
kobayashi_window.geometry("-5000+{}".format(floordef))
kobayashi_window.overrideredirect(1)
kobayashi_window.resizable(TRUE, TRUE)

kobaimg = PhotoImage(file=KOBAYASHI)
kobalabel = Label(kobayashi_window, image=kobaimg)
kobalabel.config(bg='gray')
kobayashi_window.wm_attributes("-transparentcolor", 'gray')
kobalabel.pack()


life_id = None
life1_id = None
life2_id = None


def Zzz_tohru(evalue=0):

    bedtime = ['I am tired...', 'I feel sleepy...', 'Bedtime LOL',
               'A momir', '*Fucking sleeps', '*Fucking dies', 'C ya tomorrow...', 'Zzzzzzzz']
    random_bedtime = random.randint(0, 7)
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=SleepyT, format='gif -index %i' % (i))
                   for i in range(38)]

    tohru.attributes('-alpha', 1)
    elma_window.geometry("-200000+0")
    lucoa_window.geometry("-200000+0")
    ilulu_window.geometry("-200000+0")
    kanna_window.geometry("-200000+0")

    #Zzztoast = ToastNotifier()

    # Zzztoast.show_toast(title='Tohru', msg=str(
    # bedtime[random_bedtime]), icon_path=sleepy_icon, duration=10, threaded=False)


mylocaltime = time.localtime()
hour = mylocaltime.tm_hour


if hour == 22:
    Zzz_tohru(evalue=0)
elif hour == 23:
    Zzz_tohru(evalue=0)
elif hour == 24:
    Zzz_tohru(evalue=0)
elif hour == 1:
    Zzz_tohru(evalue=0)
elif hour == 2:
    Zzz_tohru(evalue=0)
elif hour == 3:
    Zzz_tohru(evalue=0)
elif hour == 4:
    Zzz_tohru(evalue=0)
elif hour == 5:
    Zzz_tohru(evalue=0)


# Poner el Zzzzzz

x = datetime.today()
y = (x + timedelta(days=1)).replace(day=x.day, hour=22, minute=0, second=0,
                                    microsecond=0)
delta_t = y-x

secs = delta_t.total_seconds()

t = Timer(secs, Zzz_tohru)
t.start()


def nomoreZ(evalue=0):

    waking = ['Good morning!', 'gm!', 'gm', 'GM', 'GM!',
              'How did you sleep?', 'Wake up sleepy head', 'Wakey wakey!']
    random_waking = random.randint(0, 7)

    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=Tohru, format='gif -index %i' % (i))
                   for i in range(38)]

    #noZzztoast = ToastNotifier()
    # noZzztoast.show_toast(title='Tohru', msg=str(
    # waking[random_waking]), icon_path=wakey_icon, duration=10, threaded=False)


if hour == 6:
    nomoreZ(evalue=0)
elif hour == 7:
    nomoreZ(evalue=0)
elif hour == 8:
    nomoreZ(evalue=0)

# Quitar el Zzzzz


xa = datetime.today()
ya = (xa + timedelta(days=1)).replace(day=xa.day, hour=6, minute=0, second=0,
                                      microsecond=0)
adelta_t = ya-xa

asecs = adelta_t.total_seconds()

ta = Timer(asecs, nomoreZ)
ta.start()


# Easter egg


xe = datetime.today()
ye = (xe + timedelta(days=1)).replace(day=xe.day, hour=12, minute=0, second=0,
                                      microsecond=0)
edelta_t = ye-xe

esecs = edelta_t.total_seconds()

te = Timer(esecs, watchingstill)
te.start()


def away():

    classy_window.geometry("-200000+0")


xi = datetime.today()
yi = (xi + timedelta(days=1)).replace(day=xi.day, hour=12, minute=0, second=10,
                                      microsecond=0)

idelta_t = yi-xi

isecs = idelta_t.total_seconds()

it = Timer(isecs, away)
it.start()


# Función cambiar de dragona y reset


def reseTohru(evalue=0):
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=Tohru, format='gif -index %i' % (i))
                   for i in range(38)]
    tohru.attributes('-alpha', 1)
    elma_window.geometry("-200000+0")
    lucoa_window.geometry("-200000+0")
    ilulu_window.geometry("-200000+0")
    kanna_window.geometry("-200000+0")
    oldlife()


LADO = None

dvd_id = None


def fourth():

    global LADO, dvd_id

    LADO = fourth

    tx = -2
    ty = -2

    tohru_x = int(tohru.winfo_x())
    tohru_y = int(tohru.winfo_y())

    tfx = tohru_x + tx

    tfy = tohru_y + ty

    tohru_width = int(tohru.winfo_width())
    tohru_height = int(tohru.winfo_height())

    max_screen_x = int(tohru.winfo_screenwidth())

    maxx = max_screen_x - tohru_width

    max_screen_y = int(tohru.winfo_screenheight())

    maxy = max_screen_y - tohru_height

    if tohru_x <= 0:
        LADO = second
    if tohru_y <= 0:
        LADO = third

    tohru.geometry("+{}+{}".format(tfx, tfy))

    dvd_id = tohru.after(10, LADO)


def third():

    global LADO, dvd_id

    LADO = third

    tx = -2
    ty = 2

    tohru_x = int(tohru.winfo_x())
    tohru_y = int(tohru.winfo_y())

    tfx = tohru_x + tx

    tfy = tohru_y + ty

    tohru_width = int(tohru.winfo_width())
    tohru_height = int(tohru.winfo_height())

    max_screen_x = int(tohru.winfo_screenwidth())

    maxx = max_screen_x - tohru_width

    max_screen_y = int(tohru.winfo_screenheight())

    maxy = max_screen_y - tohru_height

    if tohru_y >= maxy:
        LADO = fourth
    if tohru_x >= maxx:
        LADO = fourth
    if tohru_x <= 0:
        LADO = first

    tohru.geometry("+{}+{}".format(tfx, tfy))

    dvd_id = tohru.after(10, LADO)


def second():

    global LADO, dvd_id

    LADO = second

    tx = 2
    ty = -2

    tohru_x = int(tohru.winfo_x())
    tohru_y = int(tohru.winfo_y())

    tfx = tohru_x + tx

    tfy = tohru_y + ty

    tohru_width = int(tohru.winfo_width())
    tohru_height = int(tohru.winfo_height())

    max_screen_x = int(tohru.winfo_screenwidth())

    maxx = max_screen_x - tohru_width

    max_screen_y = int(tohru.winfo_screenheight())

    maxy = max_screen_y - tohru_height

    if tohru_x >= maxx:
        LADO = fourth
    if tohru_y <= 0:
        LADO = first

    tohru.geometry("+{}+{}".format(tfx, tfy))

    dvd_id = tohru.after(10, LADO)


def first():

    global LADO, dvd_id

    LADO = first

    tx = 2
    ty = 2

    tohru_x = int(tohru.winfo_x())
    tohru_y = int(tohru.winfo_y())

    tfx = tohru_x + tx

    tfy = tohru_y + ty

    tohru_width = int(tohru.winfo_width())
    tohru_height = int(tohru.winfo_height())

    max_screen_x = int(tohru.winfo_screenwidth())

    maxx = max_screen_x - tohru_width

    max_screen_y = int(tohru.winfo_screenheight())

    maxy = max_screen_y - tohru_height

    if tohru_y >= maxy:
        LADO = second
    if tohru_x >= maxx:
        LADO = second

    tohru.geometry("+{}+{}".format(tfx, tfy))

    dvd_id = tohru.after(10, LADO)


def DVD():
    first()
    mb.entryconfig("Life", state="disabled")
    mb.entryconfig("Lifeless", state="active")


def tohruupd(evalue=0):
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=Tohru, format='gif -index %i' % (i))
                   for i in range(38)]


def vibingtohru(evalue=0):
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=HappyTohru, format='gif -index %i' % (i))
                   for i in range(38)]


def shinyupd(evalue=0):
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=SHINYT, format='gif -index %i' % (i))
                   for i in range(38)]


def sleepyupd(evalue=0):
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=SleepyT, format='gif -index %i' % (i))
                   for i in range(38)]


def elmaupd(evalue=0):
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=Elma, format='gif -index %i' % (i))
                   for i in range(38)]


def lucoaupd(evalue=0):
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=Lucoa, format='gif -index %i' % (i))
                   for i in range(38)]


def iluluupd(evalue=0):
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=Ilulu, format='gif -index %i' % (i))
                   for i in range(38)]


def kannaupd(evalue=0):
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=Kanna, format='gif -index %i' % (i))
                   for i in range(38)]


def guraupd(evalue=0):
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=GuraSpin, format='gif -index %i' % (i))
                   for i in range(38)]


def pusheenupd(evalue=0):
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=Pusheenwalk, format='gif -index %i' % (i))
                   for i in range(38)]


def maikaupd(evalue=0):
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=maikaspin, format='gif -index %i' % (i))
                   for i in range(38)]


def padorupd(evalue=0):
    if evalue > 1:
        global tohruframes
    tohruframes = [PhotoImage(file=Padoru, format='gif -index %i' % (i))
                   for i in range(38)]


def elmainvoke():

    c = random.randint(-0, 1280)
    d = random.randint(-0, 700)

    elma_window.geometry("+{}+{}".format(c, d))


def elmakill():
    elma_window.geometry("-170000+0")
    elma_window.attributes("-alpha", 1)


def lucoainvoke():

    e = random.randint(-0, 1280)
    f = random.randint(-0, 700)

    lucoa_window.geometry("+{}+{}".format(e, f))


def lucoakill():

    lucoa_window.geometry("-170000+0")
    lucoa_window.attributes("-alpha", 1)


def iluluinvoke():

    g = random.randint(-0, 1280)
    h = random.randint(-0, 700)

    ilulu_window.geometry("+{}+{}".format(g, h))


def ilulukill():

    ilulu_window.geometry("-170000+0")
    ilulu_window.attributes("-alpha", 1)


def kannainvoke():

    i = random.randint(-0, 1280)
    j = random.randint(-0, 700)

    kanna_window.geometry("+{}+{}".format(i, j))


def kannakill():
    kanna_window.geometry("-170000+0")
    kanna_window.attributes("-alpha", 1)


def kobamove():

    global floordef

    kx = int(kobayashi_window.winfo_x())
    ky = int(kobayashi_window.winfo_y())

    kxspeed = 15

    kyspeed = 0

    kfx = kx + kxspeed
    kfy = ky + kyspeed

    screen_width = int(tohru.winfo_screenwidth())

    if kx <= (screen_width):
        kfx = kx + kxspeed
    else:

        return kobayashi_window.geometry("-150000+{}".format(floordef))

    kobayashi_window.geometry("+{}+{}".format(kfx, kfy))
    tohru.after(10, kobamove)


def padorumovement():

    px = int(tohru.winfo_x())
    py = int(tohru.winfo_y())

    pxspeed = 0

    pyspeed = 1

    screen_width = int(tohru.winfo_screenwidth())
    screen_height = int(tohru.winfo_screenheight())

    tohru_width = int(tohru.winfo_width())
    tohru_height = int(tohru.winfo_height())

    halfx = int(screen_width/2+100 - tohru_width)
    halfy = int((screen_height - tohru_height) - screen_height/2)

    pfx = halfx + pxspeed
    pfy = halfy + pyspeed

    if py <= (halfy):
        pfy = py + pyspeed
    else:
        padorupd()
        return tohru.geometry("+{}+{}".format(halfx, halfy))

    tohru.geometry("+{}+{}".format(pfx, pfy))
    tohru.after(10, padorumovement)

# Life momento


def movinglilleft():

    global life_id

    x = int(tohru.winfo_x())
    y = int(tohru.winfo_y())

    xspeed = 15
    yspeed = 0

    fx = x - xspeed
    fy = y + yspeed

    tohru.geometry("+%s+%s" % (fx, fy))
    life_id = tohru.after(5000, movinglilleft)


def movinglilright():

    global life1_id

    x = int(tohru.winfo_x())
    y = int(tohru.winfo_y())

    xspeed = -15
    yspeed = 0

    fx = x - xspeed
    fy = y + yspeed

    tohru.geometry("+%s+%s" % (fx, fy))
    life1_id = tohru.after(4000, movinglilright)


def kobayashilinks():

    global life2_id

    kobarray = ['https://www.google.com/search?q=kobayashi+san+fanart&tbm=isch&ved=2ahUKEwjt_aWNsfPzAhWEY60KHYECC8sQ2-cCegQIABAA&oq=kobayashi+san+fanart&gs_lcp=CgNpbWcQAzoHCCMQ7wMQJzoECAAQQzoFCAAQgAQ6BAgAEB46BggAEAgQHjoECAAQGFChBFi4CmD_CmgAcAB4AIABiwGIAdwGkgEDMC43mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=_uF9Ye2GLoTHtQWBhazYDA&bih=656&biw=1396#imgrc=2Z6QW1zSTs1a2M',
                'https://www.google.com/search?q=kobayashi+san&sxsrf=AOaemvKji8gBeMO0dGfVy1Iea_41OELSjg:1635643921339&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiU0qO3wPPzAhV2mGoFHdPwCc0Q_AUoAXoECAEQAw&biw=1396&bih=656&dpr=1.38#imgrc=8PRfjCTs8u94eM',
                'https://www.google.com/search?q=kobayashi+san+cute&tbm=isch&ved=2ahUKEwjXl-y3wPPzAhUGUawKHa0_DeQQ2-cCegQIABAA&oq=kobayashi+san+cute&gs_lcp=CgNpbWcQAzIECAAQEzoHCCMQ7wMQJzoECAAQQzoFCAAQgAQ6CAgAEAgQHhATUJIEWMAOYI4PaAFwAHgBgAH4AYgB1QiSAQUxLjYuMZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=EvJ9YdfGH4aisQWt_7SgDg&bih=656&biw=1396#imgrc=-nbOpzriQZhOqM',
                'https://www.google.com/search?q=kobayashi+san+happy&tbm=isch&ved=2ahUKEwii_9vywPPzAhUBD60KHfzFB7cQ2-cCegQIABAA&oq=kobayashi+san+happy&gs_lcp=CgNpbWcQAzoHCCMQ7wMQJzoICAAQCBAeEBM6BQgAEIAEULgBWO8LYK8MaABwAHgAgAF5iAGLB5IBAzAuOJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=jfJ9YeKEPIGetAX8i5-4Cw&bih=656&biw=1396#imgrc=TEBipMm_4oEE2M',
                'https://www.google.com/search?q=kobayashi+san+funny&tbm=isch&ved=2ahUKEwjtuMuCwfPzAhUEKa0KHQDuDXoQ2-cCegQIABAA&oq=kobayashi+san+funny&gs_lcp=CgNpbWcQAzoHCCMQ7wMQJzoFCAAQgAQ6BggAEAgQHjoECAAQGFDVBli8EGCbEWgAcAB4AIABeIgBqgWSAQMwLjaYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=r_J9Ya2lEITStAWA3LfQBw&bih=656&biw=1396#imgrc=Xt9Eps1Z9pgguM',
                'https://www.google.com/search?q=kobayashi+san+jot&tbm=isch&ved=2ahUKEwiYgOSVwfPzAhUJVK0KHT0PCrsQ2-cCegQIABAA&oq=kobayashi+san+jot&gs_lcp=CgNpbWcQAzoHCCMQ7wMQJzoFCAAQgAQ6BggAEAgQHjoECAAQGFDoCViwKmD9KmgAcAB4AIABe4gBwgSSAQMwLjWYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=1_J9Ydi4H4motQW9nqjYCw&bih=656&biw=1396#imgrc=Uzyb7ggkbVasoM',
                'https://www.youtube.com/watch?v=BcQSpKvvmUI', 'https://www.youtube.com/watch?v=zBE2xvz2OV4', 'https://www.youtube.com/watch?v=KVV5Hh2RHoA', 'https://www.youtube.com/watch?v=K2GHGLbqOKo', 'https://www.youtube.com/watch?v=g4B_I7_a5mk', 'https://www.youtube.com/watch?v=9xE5e4LA08I', 'https://www.youtube.com/watch?v=WhOesCYSnso', 'https://www.youtube.com/watch?v=y6E4Gm_WlUw',
                'https://www.youtube.com/watch?v=q-UGsWvrnuQ']

    kobanumber = random.randint(0, 14)

    webbrowser.open(kobarray[kobanumber], 1, True)
    life2_id = tohru.after(60000, kobayashilinks)


def newlife():
    mb.entryconfig("Life", state="disabled")
    mb.entryconfig("Lifeless", state="active")

    movinglilleft()
    movinglilright()
    kobayashilinks()


def oldlife():

    mb.entryconfig("Lifeless", state="disabled")
    mb.entryconfig("Life", state="active")

    global life_id, life1_id, life2_id, dvd_id

    if life_id:
        tohru.after_cancel(life_id)
    life_id = None

    if life1_id:
        tohru.after_cancel(life1_id)
    life1_id = None

    if life2_id:
        tohru.after_cancel(life2_id)
    life2_id = None

    if dvd_id:
        tohru.after_cancel(dvd_id)
        dvd_id = None


def cloak():
    invisvalue = 1
    invisresult = invisvalue - 0.97
    tohru.attributes('-alpha', invisresult)


# Elma
def elmacloak():
    elma_window.attributes('-alpha', 0.03)


def elmacloakreset():
    elma_window.attributes('-alpha', 1)
# Lucoa


def lucoacloak():
    lucoa_window.attributes('-alpha', 0.03)


def lucoacloakreset():
    lucoa_window.attributes('-alpha', 1)
# Ilulu


def ilulucloak():
    ilulu_window.attributes('-alpha', 0.03)


def ilulucloakreset():
    ilulu_window.attributes('-alpha', 1)

# Kanna


def kannacloak():
    kanna_window.attributes('-alpha', 0.03)


def kannacloakreset():
    kanna_window.attributes('-alpha', 1)

# Padoru moment


localdate = datetime.today()
month = int(localdate.month)


def padosong(padoru):
    playsound(padoru_song, block=False)
    pass


if month == 12:
    padosong(padoru=True)
    padorumovement()


def code(tkinterpende):
    with open('gold.txt', 'r') as f:
        code = f.readlines()

    if code == ['Su9dTSq83YFq7qw1hPa3']:
        shinyupd()

    else:
        print('Shiny mode couldnt trigger')


def moodchanger(app="Spotify"):
    spotify = False

    for proc in psutil.process_iter():
        if app.lower() in proc.name().lower() and spotify == False:
            vibingtohru(evalue=0)
            spotify = True
            print("Vibes")


mytimer = Timer(5, moodchanger)
mytimer.start()


# Menú de Tohru
mb = Menu(tohru, tearoff=0, bg='white', fg='black',
          activeforeground='white', activebackground='#c8a57a', activeborderwidth=1)

characterm = Menu(mb, tearoff=0, bg='white', fg='black',
                  activeforeground='white', activebackground='#bf8c4e', activeborderwidth=1)
characterm.add_command(label="Tohru", command=tohruupd)
characterm.add_command(label="Elma", command=elmaupd)
characterm.add_command(label="Lucoa", command=lucoaupd)
characterm.add_command(label="Ilulu", command=iluluupd)
characterm.add_command(label="Kanna", command=kannaupd)
characterm.add_separator()
characterm.add_command(label="Custom(Gura Spin)", command=guraupd)
characterm.add_command(label="Custom(Pusheen)", command=pusheenupd)
characterm.add_command(label="Custom(Maika Spin)", command=maikaupd)


fm = Menu(mb, tearoff=0, bg='white', fg='black',
          activeforeground='white', activebackground='#bf8c4e', activeborderwidth=1)
fm.add_command(label="Kill me", command=killtoh)
fm.add_command(label="Cloak", command=cloak)
fm.add_command(label="Kobayashi", command=kobamove)
fm.add_command(label="DVD", command=DVD)
fm.add_command(label="Reset", command=reseTohru)


ivm = Menu(mb, tearoff=0, bg='white', fg='black', activeforeground='white',
           activebackground='#bf8c4e', activeborderwidth=1)
ivm.add_command(label="Elma", command=elmainvoke)
ivm.add_command(label="Lucoa", command=lucoainvoke)
ivm.add_command(label="Ilulu", command=iluluinvoke)
ivm.add_command(label="Kanna", command=kannainvoke)

mb.add_cascade(label="Character", menu=characterm)
mb.add_cascade(label="Summon", menu=ivm)
mb.add_cascade(label="Actions", menu=fm)
mb.add_command(label="Life", command=newlife)
mb.add_command(label="Lifeless", command=oldlife)
mb.add_separator()
mb.add_command(label="Reset", command=reseTohru)
mb.add_command(label="?", command=rick)


# default
mb.entryconfig("Lifeless", state="disabled")


def do_popup(event):
    try:
        mb.tk_popup(event.x_root, event.y_root)
    finally:
        mb.grab_release()

# Menú de Elma


emb = Menu(elma_window, tearoff=0, bg='white', fg='black',
           activeforeground='white', activebackground='#7d5161', activeborderwidth=1)

emb.add_command(label='Kill me', command=elmakill)
emb.add_command(label='Cloak', command=elmacloak)
emb.add_separator()
emb.add_command(label='Reset', command=elmacloakreset)


def edo_popup(event):
    try:
        emb.tk_popup(event.x_root, event.y_root)
    finally:
        emb.grab_release()

# Menú de Lucoa


lmb = Menu(lucoa_window, tearoff=0, bg='white', fg='black',
           activeforeground='white', activebackground='#73bbd3', activeborderwidth=1)

lmb.add_command(label='Kill me', command=lucoakill)
lmb.add_command(label='Cloak', command=lucoacloak)
lmb.add_separator()
lmb.add_command(label='Reset', command=lucoacloakreset)


def ldo_popup(event):
    try:
        lmb.tk_popup(event.x_root, event.y_root)
    finally:
        lmb.grab_release()


ilmb = Menu(ilulu_window, tearoff=0, bg='white', fg='black',
            activeforeground='white', activebackground='#cd8189', activeborderwidth=1)

ilmb.add_command(label='Kill me', command=ilulukill)
ilmb.add_command(label='Cloak', command=ilulucloak)
ilmb.add_separator()
ilmb.add_command(label='Reset', command=ilulucloakreset)


def ildo_popup(event):
    try:
        ilmb.tk_popup(event.x_root, event.y_root)
    finally:
        ilmb.grab_release()


kamb = Menu(kanna_window, tearoff=0, bg='white', fg='black',
            activeforeground='white', activebackground='#bf93b7', activeborderwidth=1)

kamb.add_command(label='Kill me', command=kannakill)
kamb.add_command(label='Cloak', command=kannacloak)
kamb.add_separator()
kamb.add_command(label='Reset', command=kannacloakreset)


def kado_popup(event):
    try:
        kamb.tk_popup(event.x_root, event.y_root)
    finally:
        kamb.grab_release()

# FUNCIÓN DE MOVER

# Tohru


def tSaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def tDragging(event):
    x, y = event.x - lastClickX + tohru.winfo_x(), event.y - \
        lastClickY + tohru.winfo_y()
    tohru.geometry("+%s+%s" % (x, y))


tohru.bind('<Button-1>', tSaveLastClickPos)
tohru.bind('<Button-2>', unfunnyscreen)
tohru.bind('<B1-Motion>', tDragging)
tohru.bind("<Button-3>", do_popup)

# Elma


def eSaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def eDragging(event):
    x, y = event.x - lastClickX + elma_window.winfo_x(), event.y - \
        lastClickY + elma_window.winfo_y()
    elma_window.geometry("+%s+%s" % (x, y))


elma_window.bind('<Button-1>', eSaveLastClickPos)
elma_window.bind('<B1-Motion>', eDragging)
elma_window.bind("<Button-3>", edo_popup)

# Lucoa


def luSaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def luDragging(event):

    x, y = event.x - lastClickX + lucoa_window.winfo_x(), event.y - \
        lastClickY + lucoa_window.winfo_y()
    lucoa_window.geometry("+%s+%s" % (x, y))


lucoa_window.bind('<Button-1>', luSaveLastClickPos)
lucoa_window.bind('<Button-2>', code)
lucoa_window.bind('<B1-Motion>', luDragging)
lucoa_window.bind('<Button-3>', ldo_popup)


# Ilulu

def iluSaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def iluDragging(event):

    x, y = event.x - lastClickX + ilulu_window.winfo_x(), event.y - \
        lastClickY + ilulu_window.winfo_y()
    ilulu_window.geometry("+%s+%s" % (x, y))


ilulu_window.bind('<Button-1>', iluSaveLastClickPos)
ilulu_window.bind('<B1-Motion>', iluDragging)
ilulu_window.bind("<Button-3>", ildo_popup)

# Kanna


def kaSaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def kaDragging(event):

    x, y = event.x - lastClickX + kanna_window.winfo_x(), event.y - \
        lastClickY + kanna_window.winfo_y()
    kanna_window.geometry("+%s+%s" % (x, y))


kanna_window.bind('<Button-1>', kaSaveLastClickPos)
kanna_window.bind('<Button-2>', funnyscreen)
kanna_window.bind('<B1-Motion>', kaDragging)
kanna_window.bind('<Button-3>', kado_popup)


def really_away(cagada):
    classy_window.geometry("-200000+0")


classy_window.bind('<Button-1>', really_away)


# Fin del código de la ventana


tohru.mainloop()
