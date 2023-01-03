Grundforløbsprøve programmeringsøvelse

Mindst 2 data typer: variablen "names" på linje 31 er en sequence (liste) type,
og i funktionen listinsert() på linje 50 bliver parameter variablen "num" brugt som en integer for range() funktionen.

Mindst en if/switch sætning: if sætning bliver brugt i funktionen strvalid() på linje 43, og i funktionen sorter()
på linje 64.

Mindst en løkke: for løkken bliver brugt i funktionen listinsert() på linje 52.



Der bliver brugt nogle usædvanlige funktioner i den her program, som forklares følgende:

"import os" bruger jeg for at køre nogle Windows batch kommandoer som gør det overskueligt at kigge
på tekst på en CLI. "lambda" er en anonymt funktion der er nødvendigt for at bruge variablet som en funktion.

"try" og "except" er Pythons fejlsikker funktioner hvis en program støder ind i værdier som ikke er forventet.

"isalpha()" er en funktion der tjekker hvis en string kun indeholder bogstaver.

"if min <= int <= max" er en måde at tjekke hvis en integer er imellem to mindre og større integers.

"join()" funktionen laver listen "names" om til en enkelt string, hvor hver indeks i listen adskilles af
en ny string.
