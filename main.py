# Questo software è rilasciato sotto la licenza Apache 2.0. Vedi il file LICENSE per dettagli.

import webbrowser
from bs4 import BeautifulSoup
import bs4

print("""Questo software è fornito "così com'è", senza alcuna garanzia di alcun tipo, espressa o implicita.
      L'autore non si assume alcuna responsabilità per eventuali danni, perdite o problemi derivanti
      dall'uso di questo software. Utilizzando questo software, accetti di farlo a tuo rischio'""")
print("Continuare? [Y/n]")
choice = input(str)
if (choice != 'y' and choice != 'Y'):
    print("Uscito")
    exit()

try:
    with open ('sbifiles.htm', 'r') as file:
        soup = bs4.BeautifulSoup(file, 'html.parser')
except FileNotFoundError:
    print("Errore, rinominare il file html esattamente come sbi")

tabella = soup.find(id='table102')
links = tabella.find_all('a', href=True)

hrefs = [ link['href'] for link in links if 'sbifiles/' in link['href']]
contatore = 0
for href in hrefs:
    webbrowser.open(hrefs[contatore])
    contatore += 1
