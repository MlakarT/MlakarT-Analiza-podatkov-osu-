import re, orodja
file = 'osu_index.txt'
aux_file = 'data-auxf.txt'
page = 'https://osu.ppy.sh/beatmapsets?sort=difficulty_desc&s=ranked'

curr_re = r'\{"beatmapsets":\[(.*?)\]\}\]'
data_re= re.compile(
    r'',
flags=re.DOTALL)

def scrape(fin: str, out: str) -> None:
    regex = re.compile(curr_re, flags=re.DOTALL) #re.DOTALL postav piko na vse, vkljucno s novo vrstico
    with open(fin) as f:
        stuff = f.read()
        with open(out, 'w', encoding='UTF8')as out:
            print(re.findall(regex, stuff), file=out)


if __name__ == '__main__':
    orodja.shrani_spletno_stran(page, file, vsili_prenos=True)
    scrape(file, aux_file)