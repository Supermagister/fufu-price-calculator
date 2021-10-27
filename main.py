import tkinter as tk
from tkinter import *

dino = None
weight = 0
root = tk.Tk()
tk.Label(text='dino level : ').grid(row=0, column=1)
e1 = tk.Entry(root)
e1.grid(row=0, column=2)
tk.Label(text=" ", width=25).grid(row=2, column=1)
tk.Label(text=" ", width=25).grid(row=4, column=1)
box = tk.Listbox(root, width=30)
box.insert(tk.END, 'achatina (+ ab)')
box.insert(tk.END, 'allosaure (normal)')
box.insert(tk.END, 'allosaure (x/r)')
box.insert(tk.END, 'angler (normal)')
box.insert(tk.END, 'angler (ab)')
box.insert(tk.END, 'ankylo (normal)')
box.insert(tk.END, 'ankylo (ab/x)')
box.insert(tk.END, 'araneo (normal)')
box.insert(tk.END, 'araneo (ab)')
box.insert(tk.END, 'archeopteryx')
box.insert(tk.END, 'argentavis (normal)')
box.insert(tk.END, 'argentavis (x)')
box.insert(tk.END, 'arthropluera (normal)')
box.insert(tk.END, 'arthropluera (ab)')
box.insert(tk.END, 'astrocetus')
box.insert(tk.END, 'astrodelphis')
box.insert(tk.END, 'baryonyx')
box.insert(tk.END, 'baryonyx (ab)')
box.insert(tk.END, 'basilisk')
box.insert(tk.END, 'basilo')
box.insert(tk.END, 'basilo (x)')
box.insert(tk.END, 'beelzebufo')
box.insert(tk.END, 'beelzebufo (ab)')
box.insert(tk.END, 'bloodstalker')
box.insert(tk.END, 'bronto')
box.insert(tk.END, 'bronto (r)')
box.insert(tk.END, 'dung beetle (bousier)')
box.insert(tk.END, 'dung beetle (ab)')
box.insert(tk.END, 'buldog')
box.insert(tk.END, 'carbonemys')
box.insert(tk.END, 'carbonemys (r)')
box.insert(tk.END, 'carno')
box.insert(tk.END, 'carno (ab/r)')
box.insert(tk.END, 'castor')
box.insert(tk.END, 'chalico')
box.insert(tk.END, 'compy')
box.insert(tk.END, 'daeodon')
box.insert(tk.END, 'daeodon (x)')
box.insert(tk.END, 'deinonychus')
box.insert(tk.END, 'dilo')
box.insert(tk.END, 'dilo (r)')
box.insert(tk.END, 'dimetrodon')
box.insert(tk.END, 'dimetrodon (ab)')
box.insert(tk.END, 'dimorph')
box.insert(tk.END, 'dimorph (ab)')
box.insert(tk.END, 'diplocaulus')
box.insert(tk.END, 'diplocaulus (ab)')
box.insert(tk.END, 'diplodocus')
box.insert(tk.END, 'diplodocus (ab)')
box.insert(tk.END, 'dire bear')
box.insert(tk.END, 'dire bear (ab)')
box.insert(tk.END, 'direwolf')
box.insert(tk.END, 'direwolf (r)')
box.insert(tk.END, 'dodo')
box.insert(tk.END, 'dodo (ab)')
box.insert(tk.END, 'doedicurus')
box.insert(tk.END, 'doedicurus (ab)')
box.insert(tk.END, 'dunkleo')
box.insert(tk.END, 'dunkleo (x)')
box.insert(tk.END, 'electrophorus')
box.insert(tk.END, 'electrophorus (ab)')
box.insert(tk.END, 'enforcer (executeur)')
box.insert(tk.END, 'equus')
box.insert(tk.END, 'equus (ab/r)')
box.insert(tk.END, 'featherlight (plumineux)')
box.insert(tk.END, 'ferox')
box.insert(tk.END, 'gacha')
box.insert(tk.END, 'galiminus')
box.insert(tk.END, 'gasbag (+r)')
box.insert(tk.END, 'giant bee')
box.insert(tk.END, 'gigano')
box.insert(tk.END, 'gigano (r)')
box.insert(tk.END, 'giganto')
box.insert(tk.END, 'giganto(ab)')
box.insert(tk.END, 'glowtail (gecko)')
box.insert(tk.END, 'golem (+chalk/ice)')
box.insert(tk.END, 'golem de lave (lava elemental)')#this thing is not tamable... Maybe they meant golem x ?
box.insert(tk.END, 'griffin')
box.insert(tk.END, 'snow owl (+r)')
box.insert(tk.END, 'hesperornis')
box.insert(tk.END, 'Hyaenodon')
box.insert(tk.END, 'Ichtyornis')
box.insert(tk.END, 'ichthyosaure')
box.insert(tk.END, 'ichthyosaure (x)')
box.insert(tk.END, 'iguanodon')
box.insert(tk.END, 'iguanodon (ab)')
box.insert(tk.END, 'jerboa')
box.insert(tk.END, 'kairuku')
box.insert(tk.END, 'kapro')
box.insert(tk.END, 'karkinos')
box.insert(tk.END, 'kentro')
box.insert(tk.END, 'lezard epineux (thorny dragon)')
box.insert(tk.END, 'licorne (unicorn)')
box.insert(tk.END, 'loutre')
box.insert(tk.END, 'loutre (ab/x)')
box.insert(tk.END, 'lumicorne (shinehorn)')
box.insert(tk.END, 'limantrya')
box.insert(tk.END, 'listrausaur')
box.insert(tk.END, 'listrausaur (ab)')
box.insert(tk.END, 'maewing')
box.insert(tk.END, 'magmasaur')
box.insert(tk.END, 'mammouth')
box.insert(tk.END, 'managarm')
box.insert(tk.END, 'manta')
box.insert(tk.END, 'manta (ab)')
box.insert(tk.END, 'mantis')
box.insert(tk.END, 'megachelon')
box.insert(tk.END, 'megalania')
box.insert(tk.END, 'megaloceros')
box.insert(tk.END, 'megalodon')
box.insert(tk.END, 'megalodon (x)')
box.insert(tk.END, 'megalosaure')
box.insert(tk.END, 'megalosaure (ab)')
box.insert(tk.END, 'megatherium')
box.insert(tk.END, 'megatherium (r)')
box.insert(tk.END, 'mek')
box.insert(tk.END, 'mesopithecus')
box.insert(tk.END, 'microraptor')
box.insert(tk.END, 'morellatops')
box.insert(tk.END, 'mosasaure')
box.insert(tk.END, 'mosasaure (x)')
box.insert(tk.END, 'moschops')
box.insert(tk.END, 'moschops (ab)')
box.insert(tk.END, 'noglin')
box.insert(tk.END, 'oiseau terreur (terror bird)')
box.insert(tk.END, 'onyc')
box.insert(tk.END, 'oviraptor')
box.insert(tk.END, 'ovis (+ab)')
box.insert(tk.END, 'pachycephalosaure')
box.insert(tk.END, 'pachyrhino')
box.insert(tk.END, 'paracetherium')
box.insert(tk.END, 'paracetherium (ab/x)')
box.insert(tk.END, 'parasaur (+tek)')
box.insert(tk.END, 'parasaur (r/x)')
box.insert(tk.END, 'pegomastax')
box.insert(tk.END, 'pelagornis')
box.insert(tk.END, 'phiomia')
box.insert(tk.END, 'phoenix')
box.insert(tk.END, 'piranha')
box.insert(tk.END, 'plesio')
box.insert(tk.END, 'procoptodon')
box.insert(tk.END, 'procoptodon (r)')
box.insert(tk.END, 'ptera')
box.insert(tk.END, 'pulmonoscorpius')
box.insert(tk.END, 'pulmonoscorpius (ab)')
box.insert(tk.END, 'purlovia')
box.insert(tk.END, 'purlovia (ab)')
box.insert(tk.END, 'quetzal (+tek)')
box.insert(tk.END, 'raptor (+tek)')
box.insert(tk.END, 'raptor (ab/x)')
box.insert(tk.END, 'rat des profondeur (roll rat)')
box.insert(tk.END, 'ravager')
box.insert(tk.END, 'reaper king (+r)')
box.insert(tk.END, 'rex (+tek/x)')
box.insert(tk.END, 'rhinoceros laineux')
box.insert(tk.END, 'rhinoceros laineux (x)')
box.insert(tk.END, 'rock drake')
box.insert(tk.END, 'sabertooth')
box.insert(tk.END, 'sabertooth (x)')
box.insert(tk.END, 'sabertooth salmon')
box.insert(tk.END, 'sac a gaz (+r)')
box.insert(tk.END, 'sarco')
box.insert(tk.END, 'sarco (ab)')
box.insert(tk.END, 'saumon')
box.insert(tk.END, 'shadowmane')
box.insert(tk.END, 'shinehorne')
box.insert(tk.END, 'smilodon')
box.insert(tk.END, 'smilodon (x)')
box.insert(tk.END, 'snow owl')
box.insert(tk.END, 'snow owl (r)')
box.insert(tk.END, 'spino')
box.insert(tk.END, 'spino (ab/x)')
box.insert(tk.END, 'stego (tek)')
box.insert(tk.END, 'stego (ab)')
box.insert(tk.END, 'stryder')
box.insert(tk.END, 'tapejara')
box.insert(tk.END, 'tapejara (x)')
box.insert(tk.END, 'terror bird')
box.insert(tk.END, 'therizino')
box.insert(tk.END, 'thorny dragon')
box.insert(tk.END, 'thylac')
box.insert(tk.END, 'thylac (r)') # THERE ARE R THYLAC ??? I WANT ONE !
box.insert(tk.END, 'titanoboa')
box.insert(tk.END, 'titanoboa (ab)')
box.insert(tk.END, 'titano')
box.insert(tk.END, 'triceratop (+tek)')
box.insert(tk.END, 'triceratop (ab/x)')
box.insert(tk.END, 'trilobite')
box.insert(tk.END, 'trilobite (ab)')
box.insert(tk.END, 'troodon')
box.insert(tk.END, 'tropeo')
box.insert(tk.END, 'tusoteuthis')
box.insert(tk.END, 'unicorn')
box.insert(tk.END, 'vautour (vultur)')
box.insert(tk.END, 'velonasaure')
box.insert(tk.END, 'velonasaure (r)')
box.insert(tk.END, 'woolly rhino')
box.insert(tk.END, 'woolly rhino (x)')
box.insert(tk.END, 'wyvern (blood)')
box.insert(tk.END, 'wyvern (ember)')
box.insert(tk.END, 'wyvern (tropical)')
box.insert(tk.END, 'wyvern (fire)')
box.insert(tk.END, 'wyvern (ice)')
box.insert(tk.END, 'wyvern (lighting)')
box.insert(tk.END, 'wyvern (poison)')
box.insert(tk.END, 'wyvern (voidwyrm)')
box.insert(tk.END, 'yutyrannus')
box.insert(tk.END, 'yutyrannus (x)')
#the rest will be here SOON (maybe)
box.grid(row=0, column=0)



def price_of_the_selected_one():
    level = e1.get()
    for i in box.curselection():
        dino = (box.get(i))
        if dino == 'achatina (+ ab)':
            weight = 175
        if dino == 'allosaure (normal)':
            weight = 428
        if dino == 'allosaure (x/r)':
            weight = 712
        if dino == 'angler (normal)':
            weight = 375
        if dino == 'angler (ab)':
            weight = 625
        if dino == 'ankylo (normal)':
            weight = 240
        if dino == 'ankylo (ab/x)':
            weight = 400
        if dino == 'araneo (normal)':
            weight = 135
        if dino == 'araneo (ab)':
            weight = 135
        if dino == 'archeopteryx':
            weight = 225
        if dino == 'argentavis (normal)':
            weight = 225
        if dino == 'argentavis (x)':
            weight = 375
        if dino == 'arthropluera (normal)':
            weight = 165
        if dino == 'arthropluera (ab)':
            weight == 275
        if dino == 'astrocetus':
            weight = 10000
        if dino == 'astrodelphis':
            weight = 550
        if dino == 'baryonyx':
            weight=315
        if dino == 'baryonyx (ab)':
            weight = 525
        if dino == 'basilisk':
            weight = 638
        if dino == 'basilo':
            weight = 18000 # ??? seem way to high tbh
        if dino == 'basilo (x)':
            weight = 29999 #once more, look like there are too many 9
        if dino == 'beelzebufo':
            weight=165
        if dino == 'beelzebufo (ab)':
            weight=275
        if dino=='bloodstalker':
            weight=1050 # so a basilo cost almost 18 bloodstalker...
        if dino=='bronto':
            weight=750
        if dino=='bronto (r)':
            weight = 1050
        if dino=='dung beetle (bousier)':
            weight=135
        if dino =='dung beetle (ab)':
            weight=225
        if dino =='buldog':
            weight=45
        if dino =='carbonemys':
            weight = 375
        if dino =='carbonemys (r)':
            weight = 375 #same as above Oo
        if dino == 'carno':
            weight = 375
        if dino == 'carno (ab/r)':
            weight = 625
        if dino == 'castor':
            weight = 180
        if dino == 'chalico':
            weight = 450
        if dino == 'compy':
            weight = 180
        if dino == 'daeodon':
            weight = 180
        if dino == 'daeodon (x)':
            weight = 300
        if dino == 'deinonychus' :
            weight = 128
        if dino == 'dilo':
            weight = 53
        if dino == 'dilo (r)':
            weight = 87
        if dino == 'dimetrodon':
            weight = 255
        if dino == 'dimetrodon (ab)':
            weight = 425
        if dino == 'dimorph':
            weight = 105
        if dino == 'dimorph (ab)':
            weight = 175
        if dino == 'diplocaulus':
            weight = 53
        if dino == 'diplocaulus (ab)':
            weight = 87
        if dino == 'diplodocus':
            weight = 863
        if dino == 'diplodocus (ab)':
            weight = 1437
        if dino == 'dire bear':
            weight = 443
        if dino == 'dire bear (ab)':
            weight = 737
        if dino == 'direwolf':
            weight = 180
        if dino == 'direwolf (r)':
            weight = 300
        if dino == 'dodo':
            weight = 38
        if dino == 'dodo (ab)':
            weight = 62
        if dino == 'doedicurus':
            weight = 240
        if dino == 'doedicurus (ab)':
            weight = 400
        if dino == 'dunkleo':
            weight = 375
        if dino == 'dunkleo (x)':
            weight = 625
        if dino == 'electrophorus':
            dino == 375
        if dino ==  'electrophorus (ab)':
            weight = 625
        if dino == 'enforcer (executer)':
            weight = 525
        if dino == 'equus':
            weight = 188
        if dino == 'equus (ab/r)':
            weight = 312
        if dino == 'featherlight (plumineux)':
            weight = 38
        if dino == 'ferox':
            weight = 3750
        if dino == 'gacha':
            weight = 525
        if dino == 'giant bee':
            price = 200000
        if dino == 'galiminus':
            weight = 615
        if dino == 'gasbag (+r)':
            weight = 750
        if dino == 'gigano':
            weight = 1425
        if dino == 'gigano (r)':
            weight = 2375
        if dino == 'giganto':
            weight = 225
        if dino == 'giganto(ab)':
            weight = 375
        if dino == 'glowtail (gecko)':
            weight = 38
        if dino == 'golem (+chalk/ice)':
            weight = 1500
        if dino == 'golem de lave (lava elemental)':
            weight = 2500
        if dino == 'griffin':
            weight = 300
        if dino == 'hesperornis':
            weight = 180
        if dino == 'Hyaenodon':
            weight = 60
        if dino == 'Ichtyornis':
            weight = 180
        if dino == 'ichthyosaure':
            weight = 113
        if dino == 'ichthyosaure (x)':
            weight = 187
        if dino == 'iguanodon':
            weight = 188
        if dino == 'iguanodon (ab)':
            weight = 312
        if dino == 'jerboa':
            weight = 38
        if dino == 'kairuku':
            weight = 53
        if dino == 'kapro':
            weight = 615
        if dino == 'karkinos':
            weight = 675
        if dino == 'kentro':
            weight = 675
        if dino == 'lezard epineux (thorny dragon)':
            weight = 225
        if dino == 'licorne (unicorn)':
            weight = 5625  # fat unicorn
        if dino == 'loutre':
            weight = 122
        if dino == 'loutre (ab/x)':
            weight = 175
        if dino == 'lumicorne (shinehorn)':
            weight = 38
        if dino == 'limantrya':
            weight = 224
        if dino == 'listrausaur':
            weight = 38
        if dino == 'listrausaur (ab)':
            weight = 62
        if dino == 'maewing':
            weight = 2250
        if dino == 'magmasaur':
            weight = 1375
        if dino == 'mammouth':
            weight = 600
        if dino == 'managarm':
            weight = 625
        if dino == 'manta':
            weight = 113
        if dino == 'manta (ab)':
            weight = 187
        if dino == 'mantis':
            weight = 1500
        if dino == 'megachelon':
            weight = 7500
        if dino == 'megalania':
            weight = 53
        if dino == 'megaloceros':
            weight = 180
        if dino == 'megalodon':
            weight = 375
        if dino == 'megalodon (x)':
            weight = 625
        if dino == 'megalosaure':
            weight = 615
        if dino == 'megalosaure (ab)':
            weight = 1025
        if dino == 'megatherium':
            weight = 443
        if dino == 'megatherium (r)':
            weight = 737
        if dino == 'mek':
            weight = 3000
        if dino == 'mesopithecus':
            weight = 38
        if dino == 'microraptor':
            weight = 53
        if dino == 'morellatops':
            weight = 450
        if dino == 'mosasaure':
            weight = 1349
        if dino == 'mosasaure (x)':
            weight = 2247
        if dino == 'moschops':
            weight = 143
        if dino == 'moschops (ab)':
            weight = 237
        if dino == 'noglin':
            weight = 150
        if dino == 'oiseau terreur (terror bird)':
            weight = 128
        if dino == 'onyc':
            weight = 122
        if dino == 'oviraptor':
            weight = 60
        if dino == 'ovis (+ab)':
            weight = 128
        if dino == 'pachycephalosaure':
            weight = 300
        if dino == 'pachyrhino':
            weight = 900
        if dino == 'paracetherium':
            weight = 900
        if dino == 'paracetherium (ab/x)':
            weight = 1500
        if dino == 'parasaur (+tek)':
            weight = 188
        if dino == 'parasaur (ab/r/x)':
            weight = 312
        if dino == 'pegomastax':
            weight = 30
        if dino == 'pelagornis':
            weight = 180
        if dino == 'phiomia':
            weight = 180
        if dino == 'phoenix':
            weight = 26250
        if dino == 'piranha':
            weight = 32
        if dino == 'plesio':
            weight = 750
        if dino == 'procoptodon':
            weight = 615
        if dino == 'procoptodon (r)':
            weight = 1025
        if dino == 'ptera':
            weight = 224
        if dino == 'pulmonoscorpius':
            weight = 165
        if dino == 'pulmonoscorpius (ab)':
            weight = 275
        if dino == 'purlovia':
            weight = 450
        if dino == 'purlovia (ab)':
            weight = 750
        if dino == 'quetzal (+tek)':
            weight = 750
        if dino == 'raptor (+tek)':
            weight = 128
        if dino == 'raptor (ab/x)':
            weight = 212
        if dino == 'rat des profondeur (roll rat)':
            weight = 368
        if dino == 'ravager':
            weight = 180
        if dino == 'reaper king (+r)':
            weight = 1312
        if dino == 'rex (+tek/x)':
            weight = 825
        if dino == 'rhinoceros laineux':
            weight = 563
        if dino == 'rhinoceros laineux (x)':
            weight = 937
        if dino == 'rock drake':
            weight = 1062
        if dino == 'sabertooth':
            weight = 180
        if dino == 'sabertooth (x)':
            weight = 300
        if dino == 'sabertooth salmon':
            weight = 48
        if dino == 'sac a gaz (+r)':
            weight = 750
        if dino == 'sarco':
            weight = 300
        if dino == 'sarco (ab)':
            weight = 500
        if dino == 'saumon':
            weight = 48
        if dino == 'shadowmane':
            weight = 875
        if dino == 'shinehorne':
            weight = 38
        if dino == 'smilodon':
            weight = 180
        if dino == 'smilodon (x)':
            weight = 300
        if dino == 'snow owl':
            weight = 263
        if dino == 'snow owl (r)':
            weight = 263  # yes I typed it twice
        if dino == 'spino':
            weight = 825
        if dino == 'spino (ab/x)':
            weight = 1375
        if dino == 'stego (+tek)':
            weight = 375
        if dino == 'stego (ab)':
            weight = 625
        if dino == 'stryder':
            weight = 22500
        if dino == 'tapejara':
            weight = 224
        if dino == 'tapejara (x)':
            weight = 375
        if dino == 'terror bird':
            weight = 128
        if dino == 'therizino':
            weight = 375
        if dino == 'thorny dragon':
            weight = 225
        if dino == 'thylac':
            weight = 270
        if dino == 'thylac (r)':
            weight = 450
        if dino == 'titanoboa':
            weight = 165
        if dino == 'titanoboa (ab)':
            weight = 275
        if dino == 'titano':
            weight = 4500
        if dino == 'triceratop (+tek)':
            weight = 450
        if dino == 'triceratop (ab/x)':
            weight = 750
        if dino == 'trilobite':
            weight = 45
        if dino == 'trilobite (ab)':
            weight = 75
        if dino == 'troodon':
            weight = 53
        if dino == 'tropeo':
            weight = 224
        if dino == 'tusoteuthis':
            weight = 2250
        if dino == 'unicorn':
            weight = 5625
        if dino == 'vautour (vultur)':
            weight = 105
        if dino == 'velonasaure':
            weight = 300
        if dino == 'velonasaure (r)':
            weight = 500
        if dino == 'woolly rhino':
            weight = 563
        if dino == 'woolly rhino (x)':
            weight = 937
        if dino == 'wyvern (blood)':
            weight = 624
        if dino == 'wyvern (ember)':
            weight = 624
        if dino == 'wyvern (tropical)':
            weight = 624
        if dino == 'wyvern (fire)':
            weight = 833
        if dino == 'wyvern (ice)':
            weight = 833
        if dino == 'wyvern (lighting)':
            weight = 833
        if dino == 'wyvern (poison)':
            weight = 833
        if dino == 'wyvern (voidwyrm)':
            weight = 1387
        if dino == 'yutyrannus':
            weight = 750
        if dino == 'yutyrannus (x)':
            weight = 1250


        if dino != 'giant bee':
            price = int(level) * weight

        tk.Label(text="                      ").grid(row=3, column=2)
        tk.Label(text='the minimal price is :').grid(row=3, column=1)
        tk.Label(text=format(price, ',d'), fg="red").grid(row=3, column=2) #the format() is used to add "," every 3 number, to make reading the price easier
        tk.Label(text="element dust").grid(row=3, column=3)
btn = tk.Button(root, text="calculate",
                bg="blue",
                fg="white",
                width=13,
                height=2,
                command=price_of_the_selected_one)
btn.grid(row=1, column=2)

root.mainloop()
