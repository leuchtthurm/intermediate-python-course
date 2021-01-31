import random
from tkinter import *

def wurf():
  roll = random.randint(1,6)

  res_im = Canvas(fenster, width = 130, height = 130)
  res_im.grid(row = 2, column = 2)

  res_im.create_rectangle(15, 12, 115, 117, fill = '#efefef')

  if roll == 1:
    res_im.create_oval(60, 60, 70, 70, fill = '#000000')
  #  result_text = Label(text = f'You rolled a {roll}!\n Back to the start!')
  elif roll == 2:
    res_im.create_oval(30, 90, 40, 100, fill = '#000000')
    res_im.create_oval(90, 30, 100, 40, fill = '#000000')
  elif roll == 3:
    res_im.create_oval(60, 60, 70, 70, fill = '#000000')
    res_im.create_oval(30, 90, 40, 100, fill = '#000000')
    res_im.create_oval(90, 30, 100, 40, fill = '#000000')
  elif roll == 4:
    res_im.create_oval(30, 90, 40, 100, fill = '#000000')
    res_im.create_oval(90, 30, 100, 40, fill = '#000000')
    res_im.create_oval(30, 30, 40, 40, fill = '#000000')
    res_im.create_oval(90, 90, 100, 100, fill = '#000000')
  elif roll == 5:
    res_im.create_oval(60, 60, 70, 70, fill = '#000000')
    res_im.create_oval(30, 90, 40, 100, fill = '#000000')
    res_im.create_oval(90, 30, 100, 40, fill = '#000000')
    res_im.create_oval(30, 30, 40, 40, fill = '#000000')
    res_im.create_oval(90, 90, 100, 100, fill = '#000000')
  elif roll == 6:
    res_im.create_oval(30, 90, 40, 100, fill = '#000000')
    res_im.create_oval(30, 60, 40, 70, fill= '#000000')
    res_im.create_oval(90, 30, 100, 40, fill = '#000000')
    res_im.create_oval(30, 30, 40, 40, fill = '#000000')
    res_im.create_oval(90, 90, 100, 100, fill = '#000000')
    res_im.create_oval(90, 60, 100, 70, fill = '#000000')
  #  result_text = Label(text = f'You rolled a {roll}!\n  Roll again!')
  #else:
  #  result_text = Label(text = f'You rolled a {roll}.')
  #result_text.pack()
  

fenster = Tk()
fenster.title("Würfel")
fenster.geometry("150x200")
#label = Label(fenster, text = "Bitte würfeln:")
#label.pack() #Anordnung durch Pack-Manager

click_me = Button(text = "Jetzt würfeln", command = wurf)
click_me.grid(row = 1, column = 2)

click_end = Button(text = "Beenden", command = fenster.destroy)
click_end.grid(row = 3, column = 2)

fenster.mainloop()

  

if __name__== "__main__":
  wurf()