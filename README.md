# MlakarT-Analiza-podatkov-osu

_Projektna naloga iz analize podatkov pri predmetu Programiranje 1, 2. letnik matematike_

## Public description

Analysis of the beatmap data from the videogame Osu! with respect to the map, difficulty, number of played games, popularity depending on both difficulty and appended tags. Data found on the website [Osu! - beatmaps listing](https://osu.ppy.sh/beatmapsets?sort=difficulty_desc&s=ranked)

Working hypothesis:

- We assume, that maps with common tags; such as 'japanese', 'jpop', 'kpop', etc., have a higher playcount
- Difficult maps with higher ar (approach rate), bpm and accuracy have a lower passcount
- We will try to predict the difficulty rating of each map based on the ar, bpm and accuracy with respect to playcount and expected passcount. To compare with exact difficulty rating. Formulae will be added later.

Conclusions:

- Tag hypothesis confirmed, maps with popular tags do indeed have higher play counts, which is unsurprising, given the general population that plays the game
- Second hypothesis overted, because that is how beatmap difficulty is calculated, however we did try a different approach and get to a different finding, that is:
- Tried to predict passcount for each given beatmap based on both popularity and difficulty,
- Basing it only on difficulty did not work, because undoubtedly there are players that download the map and give it one shot, then promptly forget about it
- The popularity was based on the amount of tags in the given most common tags the beatmap had, taken that as a cofactor in the result
- The end result however is still not completely accurate, with most passcount predictions being quite accurate (within 100% deviation of the accounted value, that is on average more than 50% of all maps)

Additional note: I could only scan at most 50 maps from the website with my current tools, and was told that given the structure of the website that that is okay.

## For my professors and assistants

Analiza statistike v igri Osu! glede na mapo, zahtevnost mape, število iger in regijo, pogledamo še specifične igralce na drugi tabeli. Podatki so na strani [Osu! igre - beatmaps listing](https://osu.ppy.sh/beatmapsets?sort=difficulty_desc&s=ranked)

Delovne hipoteze:

- Predvidevamo, da imajo mape s pogostimi tagi (npr: japanese, jpop, kpop, ipd.) višji playcount
- Težje mape z višjim ar, bpm in accuracy imajo manjši passcount
- Poskušali bomo predvideti difficulty mape glede na ar, bpm in accuracy glede na playcount in pričakovani passcount. Primerjali ga bomo s dejansko težavnostjo. Formule dodamo kasneje.

Zaključki:

- Hipoteza o tagih potrjena, mape z bolj popularnimi tagi imajo kot predvideno višje število igranj, glede na populacijo ljudi, ki to igro igrajo
- Druga hipoteza ovržena, saj je to že predpostavljeni način računanja težavnosti mape, vendar smo ubrali drugi pristop do analiziranja in prišli do naslednje ugotovitve:
- Poskusili smo predvideti število uspešnih igranj gledde na težavnost in popularnost mape,
- Tega števila nemoremo bazirati le na težavnost, saj veliko ljudi downloada mapo, jo morda enkrat poiskusi in nato zavrže
- Popularnost map smo izračinali glede na število tagov, ki jih mapa vsebuje in se pojavijo med 100 najbolj pogostimi tagi, in to vzeli kot kofaktor v rezultatu
- Končni rezultat sicer ni popolnoma točen, s tem da je večina napovedi dokaj točna (znotraj 100% deviacije od dejanskega podatka, ter v povprečju več kot 50% vseh map)

Dodatna točka: Iz spletne strani sem lahko potegnil kvečjemu 50 map s trenutnimi orodji zaradi strukture dejanske spletne strani, ki se dinamično generira. Asistenti so to odobrili.
