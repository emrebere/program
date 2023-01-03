# Grundforløbsprøve programmeringsøvelse

# Mindst 2 data typer: variablen "names" på linje 31 er en sequence (liste) type,
# og i funktionen listinsert() på linje 50 bliver parameter variablen "num" brugt som en integer for range() funktionen.

# Mindst en if/switch sætning: if sætning bliver brugt i funktionen strvalid() på linje 43, og i funktionen sorter()
# på linje 64.

# Mindst en løkke: for løkken bliver brugt i funktionen listinsert() på linje 52.

####################################################################################################################

# Der bliver brugt nogle usædvanlige funktioner i den her program, som forklares følgende:

# "import os" bruger jeg for at køre nogle Windows batch kommandoer som gør det overskueligt at kigge
# på tekst på en CLI. "lambda" er en anonymt funktion der er nødvendigt for at bruge variablet som en funktion.

# "try" og "except" er Pythons exception handling funktioner hvis en program støder ind i værdier som ikke er forventet.

# "isalpha()" er en funktion der tjekker hvis en string kun indeholder bogstaver.

# "if min <= int <= max" er en måde at tjekke hvis en integer er imellem to mindre og større integers.

# "join()" funktionen laver listen "names" om til en enkelt string, hvor hver indeks i listen adskilles af
# en ny string.

import os;
cls = lambda: os.system("cls");
pause = lambda: os.system("pause >nul");

names = [];

def intvalid(integer):
    try:
        int(integer);
    except ValueError:
        cls();
        print("Du skal vælge et gyldigt nummer imellem 1-10");
        pause();
        return sorter();

def strvalid(string):
    if not string.isalpha():
        cls();
        print("Du skal vælge et gyldigt navn");
        names.clear();
        pause();
        return sorter();

def listinsert(num):
    num = int(num);
    for i in range(num):
        cls();
        print("Vælg navn", i, "ud af", num);
        choice = input();
        strvalid(choice);
        names.insert(i, choice);

def sorter(): # HOVEDFUNKTION
    cls();
    print("Vælg hvor mange navne du vil sortere alfabetisk (1-10)");
    choice = input();
    intvalid(choice);
    if 1 <= int(choice) <= 10:
        listinsert(choice);
        names.sort();
        cls();
        print("Navnene sorteret alfabetisk er", ', '.join(names));
        pause();
        names.clear();
        return sorter();
    else:
        cls();
        print("Nummeret skal være imellem 1-10");
        pause();
        return sorter();

sorter();
