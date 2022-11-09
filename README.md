# MlakarT-Analiza-podatkov-osu

_Projektna naloga iz analize podatkov pri predmetu Programiranje 1, 2. letnik matematike_

## Public description

Analysis of the beatmap data from the videogame Osu! with respect to the map, difficulty, number of played games, popularity depending on both difficulty and appended tags. Data found on the website [Osu! - beatmaps listing](https://osu.ppy.sh/beatmapsets?sort=difficulty_desc&s=ranked)

Working hypothesis:

- We assume, that maps with common tags; such as 'japanese', 'jpop', 'kpop', etc., have a higher playcount
- Difficult maps with higher ar (approach rate), bpm and accuracy have a lower passcount
- We will try to predict the difficulty rating of each map based on the ar, bpm and accuracy with respect to playcount and expected passcount. To compare with exact difficulty rating. Formulae will be added later.

## For my professors and assistants

Analiza statistike v igri Osu! glede na mapo, zahtevnost mape, število iger in regijo, pogledamo še specifične igralce na drugi tabeli. Podatki so na strani [Osu! igre - beatmaps listing](https://osu.ppy.sh/beatmapsets?sort=difficulty_desc&s=ranked)

Delovne hipoteze:

- Predvidevamo, da imajo mape s pogostimi tagi (npr: japanese, jpop, kpop, ipd.) višji playcount
- Težje mape z višjim ar, bpm in accuracy imajo manjši passcount
- Poskušali bomo predvideti difficulty mape glede na ar, bpm in accuracy glede na playcount in pričakovani passcount. Primerjali ga bomo s dejansko težavnostjo. Formule dodamo kasneje.
