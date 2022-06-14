# KeyLogger

🇺🇸: Keylogger made for fun and for learn python

🇮🇹: Keylogger creato per divertimento e per imparare python

# Instructions (soon in english too):

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

Invece per eseguire il programma ti basterà lanciare questo comando in un terminale:
```sh
$ sudo python3.9 main.py
```

## Deleting logs file

🇮🇹: Se stai cercando di rimuovere un file di log dalla cartella logs/ noterai che ti sara impossibile se non sei amministratore in quel momento, questo perchè su linux il programma va avviato come amministratore, e quindi anche i file creati saranno creati come amministratore.

Quindi innanzi tutto, se ci trovimamo nella cartella di base del repositorty, spostiamoci nella cartella logs con:

```sh
$ cd scripts/logs/
```

### Removing only one file

🇮🇹: Per rimuovere un solo file dalla cartella logs ti basterà lanciare:

```sh
$ sudo rm 'nome file.csv'
```

### Removing all file

🇮🇹: Per rimuovere tutti i file dalla cartella logs ti basterà lanciare:

```sh
$ sudo rm *
```

### Removing the logs folder

🇮🇹: Per rimuovere la cartella logs ti basterà lanciare:

-1 (solo se ti trovi nella cartella logs, altrimenti salta questo passaggio):
```sh
$ cd ..
```

-2 (una volta che ti trovi nella cartella scripts):
```sh
$ sudo rm -rf logs/
```

# Download the .exe for Windows 10/11

[Download](https://github.com/bruhpate/KeyLogger/raw/main/scripts/keylogger.exe)

# External libraries used (already imported in the repo):

[Keyboard](https://github.com/boppreh/keyboard)


