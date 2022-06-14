# KeyLogger

🇺🇸: Keylogger made for fun and for learn python.

🇮🇹: Keylogger creato per divertimento e per imparare python.

## Instructions (soon in english too):

🇮🇹: **NON SERVONONO I PERMESSI DI AMMINISTRATORE SU WINDOWS, SU LINUX INVECE SI**.

Se hai scaricato il file keylogger.exe, ti basterà eseguirlo per avviarlo, una volta avviato creerà una cartella nello stesso percorso in cui è stato avviato chiamata "logs" dove conserverà tutti gli input da tastiera, ogni volta che si preme la barra spaziatrice il programma si occuperà di creare il file.csv una prima volta, chiamato come la data e l'ora, esempio: "1970-12-31 23.59.59", ed ogni volta che il tasto spazio viene premuto, il file si aggiornerà con i nuovi input ricevuti da tastiera.

Se invece hai clonato il repository e vuoi testare il software direttamente nel repository locale, ti basterà spostarti nella cartella scripts.

e aggiornare python all'ultima versione da [qua](https://www.python.org/downloads/) 

Invece per eseguire il programma ti basterà lanciare questo comando in un terminale, su linux:
```sh
$ sudo python3 main.py
```

su windows:
```sh
$ python3 main.py
```


## Download the .exe for Windows 10/11

[Download](https://github.com/bruhpate/KeyLogger/raw/main/scripts/keylogger.exe)

## Generate the .exe
🇮🇹:
1. Controlla se pip è installto (gestore pacchetti di python):
```sh
$ pip --version
```
Se non è installato reinstall python o aggiornalo. 

## External libraries used (already imported in the repo):

[Keyboard](https://github.com/boppreh/keyboard)


