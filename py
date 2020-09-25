import dnslib as dnl
from tkinter import *
from tkinter import BOTH, END, HORIZONTAL, Tk, scrolledtext, ttk
from tkinter import scrolledtext
from itertools import islice
import binascii

def click():
    output = open('output.txt', 'w')
    with open('lololo.txt') as inf:
        for line in islice(inf, 2, None, 4):
            line = line.replace('|', '')
            if line[92] == '8':
                print(line[88:], file=output)
    output.close()
    l = 0
    with open('output.txt') as pk:
        for line in islice(pk, 0, None, 2):
            a = binascii.hexlify(bytes.fromhex(hex(int(line, 16))[2:]))
            packet = binascii.unhexlify(a)
            d = dnl.DNSRecord.parse(packet)
            txt.insert(END, d)
            txt.yview(END)
            txt.insert(INSERT, '\n\n')

window = Tk()
window.title("DNS-parser")
window.geometry("1000x650")
window["bg"] = "gray80"
txt = scrolledtext.ScrolledText(window, width=100, height=40)
txt.grid(column=0, row=0)
btn = Button(window, text="Parse DNS-packet", command=click)
btn.grid(column=1, row=0)
window.mainloop()  # не дает окну закрыться
