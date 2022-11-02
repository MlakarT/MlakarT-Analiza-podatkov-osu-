import re, orodja
file = 'osu_index.txt'
page = 'https://osu.ppy.sh/beatmapsets?sort=difficulty_desc&s=ranked'

if __name__ == '__main__':
    orodja.shrani_spletno_stran(page, file, vsili_prenos=True)