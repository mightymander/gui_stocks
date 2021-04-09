import tkinter as tk
import requests 
import bs4
from datetime import datetime
import time

counter = 0
current_data = ['']*5
symbols = ['']*5

def get_price(filename, url, css_sector,):

    now = datetime.now()
    global d3
    d3 = now.strftime("%d/%m/%y %H:%M:%S")

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select(css_sector)

    data = str(elems)
    price = data
    price = price[123:10000]
    real_price= price.split('<')


    print(f'{input_filename[:-4]} : ${real_price[0]} - {d3}')

    global counter
    global current_data
    current_data[counter] = f'{input_filename[:-4]} - ${real_price[0]}'
    
    f = open(input_filename, "a")
    f.write(f'\n{d3} - {real_price[0]}')
    f.close()

    counter = counter + 1
    
def run_gui():
    HEIGHT = 400
    WIDTH = 800

    def get_symbol(symbol):
        print('enterd: ' + symbol.upper())
        global input_symbol
        input_symbol = symbol.upper()
        
        
        global input_url 
        input_url = 'https://uk.finance.yahoo.com/quote/' + (input_symbol) + '?p=' + (input_symbol)
        global input_filename
        input_filename = (input_symbol) + '.txt'
        global input_css_sector
        input_css_sector = '#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div.D\(ib\).Va\(m\).Maw\(65\%\).Ov\(h\) > div'
    
        symbols[counter] = input_symbol
        get_price(input_filename, input_url, input_css_sector)
        '''
        #testing this right now doesnt work
        while True:
            if symbols[counter] in symbols:
                print(f'Already used{symbols[counter]}')
                break
            else:
                 get_price(input_filename, input_url, input_css_sector)
                 symbols[counter] = input_symbol

        '''
        label = tk.Label(frame, text=f'{d3}')
        label.place(relx= 0.01, rely=0.91)
        res = str(current_data[counter-1])


        label = tk.Label(frame, text=f'{res}')
        
        if counter == 1:
            label.place(relx= 0.01, rely=0.01)
        elif counter  == 2:
            label.place(relx= 0.01, rely=0.1)
        elif counter == 3:
            label.place(relx= 0.01, rely=0.2)
        elif counter == 4:
            label.place(relx= 0.01, rely=0.3)
        elif counter == 5:
            label.place(relx= 0.01, rely=0.4)

    

    top = tk.Tk()
    #top.resizable(width=False, height=False) 

    canvas = tk.Canvas( top, height=HEIGHT, width=WIDTH, bg='gray' )
    canvas.pack()

    frame = tk.Frame(top, bg='#cc99ff')
    frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    symbol = tk.Entry(frame, text='enter')
    symbol.place(relx= 0.35, rely=0.9)

    button = tk.Button(frame, text='Submit', bg='gray', command=lambda: get_symbol(symbol.get()))
    button.place(relx= 0.63, rely=0.91)

    

    top.mainloop()

run_gui()

print(current_data)
print(symbols)