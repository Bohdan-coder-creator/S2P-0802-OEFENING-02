# S2P-0802-OEFENING-02

Voor deze oefening maak je gebruik van twee bronbestanden:

* `bron.txt`  
  bevat de te verwerken string  
  
  ```python
  umrwozoriztfghcaxooiymiowzmxitjuooqzelyxdeuaiveseiffuuroipkotv...
  ```

* `posities.txt`  
  het tweede bestand bevat de posities van de karakters die je zoekt, weliswaar in omgekeerde volgorde.  De posities zijn van elkaar gescheiden door een komma.  
  
  ```texttile
  1806, 730, 130, 1246, 624, 1253, 151, 684, 1337, 817, 1398, 1511, ...
  ```

In de tekst zit een boodschap verborgen.  Om de boodschap te ontcijferen maak je gebruik van de posities.  Elk getal in de lijst posities geeft de positie aan van een letter waaruit de boodschap bestaat.  Plak de letters aan elkaar en je bekomt de verborgen 
boodschap.  Echter, één klein aanvullend probleempje, de posities staan in omgekeerde volgorde. 

Het uiteindelijke resultaat, de verborgen boodschap is een uitspreekbare zin in het Nederlands.

Maak een Python-script waarmee je het bericht ontcijfert.  Schrijf het resultaat weg naar een bestand 'bericht.txt'.
