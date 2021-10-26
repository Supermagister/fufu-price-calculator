import tkinter as tk
from tkinter import *

dino = None
weight = 0
root = tk.Tk()
tk.Label(text='dino level : ').grid(row=0, column=1)
e1 = tk.Entry(root)
e1.grid(row=0, column=2)
box = tk.Listbox(root)
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
            weight = 29999 #once more, look like there are too many 9, or are the admin trying to manipulate basilo price :O
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

        price = int(level) * weight
        if dino == 'giant bee':
            price = 200000
        tk.Label(text='the minimal price is :', bg="white").grid(row=2, column=1)
        tk.Label(text=price, bg="white", fg="red").grid(row=2, column=2)
        tk.Label(text="element dust", bg="white").grid(row=2, column=3)
btn = tk.Button(root, text="calculate",
                bg="blue",
                fg="white",
                width=13,
                height=2,
                command=price_of_the_selected_one)
btn.grid(row=1, column=2)

root.mainloop()
