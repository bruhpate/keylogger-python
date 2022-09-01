# KeyLogger

## Istruzioni (soon in english too):

**NON SERVONONO I PERMESSI DI AMMINISTRATORE SU WINDOWS, SU LINUX INVECE SI**.

Se hai scaricato il file keylogger.exe, ti basterà eseguirlo per avviarlo, una volta avviato creerà una cartella nello stesso percorso in cui è stato avviato chiamata "logs" dove conserverà tutti gli input da tastiera, ogni volta che si preme la barra spaziatrice il programma si occuperà di creare il file.csv una prima volta, chiamato come la data e l'ora, esempio: "1970-12-31 23.59.59", ed ogni volta che il tasto spazio viene premuto, il file si aggiornerà con i nuovi input ricevuti da tastiera.

Se invece hai clonato il repository e vuoi testare il software direttamente nel repository locale, ti basterà spostarti nella cartella 'scripts', e aggiornare python all'ultima versione da [qua](https://www.python.org/downloads/ 'Python download page') 

Invece per eseguire il programma ti basterà lanciare questo comando in un terminale.

su linux:
```sh
# python3 main.py
```

### Nota bene che:
Se si lancia il programma da terminale, non è necessario che l'input sia scritto nel termianle, infatti il programma prenderà in input ogni tipo tasto premuto, se il terminale da cui è stato avviato il programma si chiude, interromperà la lettura degli input e perderà tutti i dati non salvati su file



## Scarica il file .exe per Windows 10/11

[Download](https://github.com/bruhpate/keylogger-python/raw/main/keylogger.exe 'Download the exe')

## Generare il file .exe
1. Controlla se pip è installto (gestore pacchetti di python):
```sh
$ pip --version
```
* Se non è installato, aggiorna o reinstalla python da [qua](https://www.python.org/downloads/ 'Python download page') 

2. Installa Pyinstaller (estensione per creare eseguibili da codice sorgente):
```sh
$ pip install pyinstaller
```
3. Nella cartella 'scripts' lancia:
```sh
$ pyinstaller --onefile -w main.py
```
 * '-w' significa che all' avvio non si aprirà nessun terminale, decidi tu se metterlo o no

4. Cancella la cartella 'build' e il file 'main.spec' (opzionale)

5. Troverai l'eseguibile  nella cartella 'dist' e lo potrai esportare dove preferisci (windows defender potrebbe infastidire l'operazione)


## Librerie esterne utilizzare (gia importate nel progetto):

[Keyboard](https://github.com/boppreh/keyboard 'Keyboard')


