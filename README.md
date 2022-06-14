# KeyLogger

🇺🇸: Keylogger made for fun and for learn python

🇮🇹: Keylogger creato per divertimento e per imparare python

# Instructions:


🇮🇹: **NON SERVONONO I PERMESSI DI AMMINISTRATORE SU WINDOWS, SU LINUX INVECE SI**.

Se hai scaricato il file keylogger.exe, ti basterà eseguirlo per avviarlo, una volta avviato creerà una cartella chiamata "logs" dove conserverà tutti gli input da tastiera, ogni volta che si preme la barra spaziatrice il programma si occuperà di creare il file.csv una prima volta, chiamato come il giorno e la data, esempio: "1970-12-31 23.59.59", ed ogni volta che il tasto spazio viene premuto, il file si aggiornerà con i nuovi input ricevuti da tastiera

Se invece hai clonato il repository e vuoi testare il software direttamente nel repository locale, ti basterà spostarti nella cartella scripts: 
```sh
$ cd scripts/
```
e per esegurilo ti basterà prima di tutto aggiornare python se non è gia aggiornato con:

Debian (Ubuntu, MXLinux, etc...):
```sh
$ sudo apt update
```

RHEL (Fedora, Centos):
```sh
$ sudo dnf update
```

Invece per eseguire il programma ti basterà eseguire questo comando in un terminale:
```sh
$ sudo python3.9 main.py
```


# Download the .exe for Windows 10/11

[Donwload](https://github.com/bruhpate/KeyLogger/raw/main/scripts/main.exe)

# External libraries used:

[Keyboard](https://github.com/boppreh/keyboard)


