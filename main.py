from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from datetime import date

from src.exportCsv import exportCsv
from src.sbsScrapping import sbsScrapping

class ExchangeRate:
  
  def exportCsvTk(self, csv_columns, dict_data, fileName):
    exportCsv(csv_columns, dict_data, fileName)
    messagebox.showinfo("Info", "¡Exportación exitosa!")

  def __init__(self, window):
    self.wind = window
    self.wind.title("Exchange Rate App")
    self.wind.geometry('490x390')
    self.wind.configure(bg='#282828')
    self.wind.resizable(False, False)

    self.heading = ttk.Label(
      self.wind, 
      text='Tipo de Cambio al ' + str(date.today()),
      style='Heading.TLabel', 
      background='#282828',
      foreground='white',
      font=('Monospace',16)  
    )
    self.heading.grid(column=0, row=1, columnspan=2, pady=10, sticky=N)

    dict_data = []
    dict_data = sbsScrapping(dict_data)
  
    self.currTree = ttk.Treeview(self.wind)
    self.currTree['columns'] = ('Currency', 'Buy', 'Sell')
    self.currTree.column('#0', width = 0, stretch = NO)
    self.currTree.column('Currency', width=150, anchor=CENTER)
    self.currTree.column('Buy', width=150, anchor=CENTER)
    self.currTree.column('Sell', width=150, anchor=CENTER)

    self.currTree.heading('Currency', text = 'Currency', anchor=CENTER)
    self.currTree.heading('Buy', text = 'Buy',anchor=CENTER)
    self.currTree.heading('Sell', text = 'Sell',anchor=CENTER)
    self.currTree.grid(row = 2, column = 0, padx=20)
    self.currTree.bind('<Motion>', 'break')

    dict_columns = ['currency', 'buy', 'sell']
    
    self.button = Button(
      self.wind,
      text="Exportar .csv", 
      command= lambda: self.exportCsvTk(dict_columns, dict_data, 'currencies'))

    self.button.grid(column=0, row=3, columnspan=2, pady=10, sticky=N, ipadx=4, ipady=4)
      
    if(dict_data):
      for curr in range(len(dict_data)):
        self.currTree.insert(
          '', 
          END, 
          str(curr), 
          values = (
            dict_data[curr]['currency'],
            dict_data[curr]['buy'],
            dict_data[curr]['sell'],
          ),
          text = '0' + str(curr)
        )
    else:
      messagebox.showerror('Error', 'No se pudieron extraer las divisas')
      self.button['state'] = 'disabled'

window = Tk()
app = ExchangeRate(window)
window.mainloop()