import pandas as pd
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def nalog_za_uplatu(file_path, data=None):
    pdfmetrics.registerFont(TTFont('LiberationSerif-Bold', 'LiberationSerif-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSerif', 'LiberationSerif-Regular.ttf'))
    pdf = canvas.Canvas(file_path, pagesize=(595.27, 841.89))
    broj_podataka = len(data['nalog_za_uplatu'])
    for i in range(broj_podataka):
        if i % 3 == 0 and i != 0:
            pdf.showPage()
        position = i % 3 + 1
        shift = 283.5 * (position - 1)
        podatci = data['nalog_za_uplatu'][i]['podatci']
        pdf.line(300.51, 805.14 - shift, 300.51, 652.05 - shift)
        pdf.line(28.35, 632.205 - shift, 184.275, 632.205 - shift)
        pdf.line(141.75, 609.525 - shift, 283.5, 609.525 - shift)
        pdf.line(323.19, 609.525 - shift, 425.25, 609.525 - shift)
        pdf.setDash(10, 10)
        pdf.setLineWidth(0.5)
        pdf.line(0, 552.825 - shift, 595.27, 552.825 - shift)
        pdf.setDash(1, 0)
        pdf.setLineWidth(1.0)
        rectangles = [
            (28.35, 765.45 - shift, 255.15, 39.69),
            (28.35, 708.75 - shift, 255.15, 39.69),
            (28.35, 652.05 - shift, 255.15, 39.69),
            (323.19, 771.12 - shift, 34.02, 17.01),
            (368.55, 771.12 - shift, 34.02, 17.01),
            (425.25, 771.12 - shift, 141.75, 17.01),
            (368.55, 737.1 - shift, 198.45, 17.01),
            (323.19, 700.245 - shift, 34.02, 17.01),
            (368.55, 700.245 - shift, 198.45, 17.01),
        ]
        for rect in rectangles:
            pdf.rect(*rect)
        pdf.setFont('LiberationSerif', 12)
        pdf.drawCentredString(141.75, 795 - shift, str(podatci['uplatilac']['uplatilac1']))
        pdf.drawCentredString(141.75, 782 - shift, str(podatci['uplatilac']['uplatilac2']))
        pdf.drawCentredString(141.75, 769 - shift, str(podatci['uplatilac']['uplatilac3']))
        pdf.drawCentredString(141.75, 738.3 - shift, str(podatci['uplata']['svrha1']))
        pdf.drawCentredString(141.75, 725.3 - shift, str(podatci['uplata']['svrha2']))
        pdf.drawCentredString(141.75, 712.3 - shift, str(podatci['uplata']['svrha3']))
        pdf.drawCentredString(141.75, 681.6 - shift, str(podatci['primalac']['primalac1']))
        pdf.drawCentredString(141.75, 668.6 - shift, str(podatci['primalac']['primalac2']))
        pdf.drawCentredString(141.75, 655.6 - shift, str(podatci['primalac']['primalac3']))
        pdf.drawString(141.75, 611 - shift, str(podatci['mesto_datum']['datum']))
        pdf.drawString(210, 611 - shift, str(podatci['mesto_datum']['mesto']))
        pdf.drawString(323.19, 611 - shift, str(podatci['uplata']['datum_valute']))
        pdf.setFont('LiberationSerif', 14)
        pdf.drawString(370, 741 - shift, str(podatci['primalac']['racun_primaoca']))
        pdf.drawString(326, 704 - shift, str(podatci['primalac']['model']))
        pdf.drawString(370, 704 - shift, str(podatci['primalac']['poziv_na_broj']))
        pdf.drawString(326, 775 - shift, str(podatci['uplata']['sifra_placanja']))
        pdf.drawString(370, 775 - shift, str(podatci['uplata']['valuta']))
        pdf.drawString(440, 775 - shift, str(podatci['uplata']['iznos']))

        pdf.setFont('LiberationSerif', 9)
        pdf.drawString(28.35, 808.7 - shift, "Уплатилац")
        pdf.drawString(28.35, 752 - shift, "Сврха уплате")
        pdf.drawString(28.35, 695.3 - shift, "Прималац")
        pdf.drawString(28.35, 623.7 - shift, "Печат и потпис уплатиоца")
        pdf.drawString(141.75, 601.02 - shift, "Место и датум пријема")
        pdf.drawString(323.19, 601.02 - shift, "Датум валуте")
        pdf.drawString(368.55, 719.255 - shift, "Позив на број (одобрење)")
        pdf.drawString(368.55, 756.11 - shift, "Рачун примаоца")
        pdf.drawString(425.25, 790.13 - shift, "Износ")
        pdf.drawString(368.55, 790.13 - shift, "Валута")
        pdf.drawString(323.19, 800.13 - shift, "Шифра")
        pdf.drawString(323.19, 790.13 - shift, "плаћања")
        pdf.drawString(323.19, 729.255 - shift, "Број")
        pdf.drawString(323.19, 719.255 - shift, "модела")
        pdf.setFont('LiberationSerif-Bold', 14)
        pdf.drawString(431, 775 - shift, '=')
        pdf.drawRightString(571, 805.14 - shift, "НАЛОГ ЗА УПЛАТУ")
        pdf.setFont('LiberationSerif', 7)
        pdf.drawCentredString(595.27 / 2, 584.01 - shift, "Образац бр. 2")
        pdf.setFont('LiberationSerif-Bold', 14)
    pdf.showPage()
    pdf.save()
    return pdf

def nalog_za_isplatu(file_path, data=None):
    pdfmetrics.registerFont(TTFont('LiberationSerif-Bold', 'LiberationSerif-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSerif', 'LiberationSerif-Regular.ttf'))
    pdf = canvas.Canvas(file_path, pagesize=(595.27, 841.89))
    broj_podataka = len((data['nalog_za_isplatu']))
    for i in range(broj_podataka):
        if i % 3 == 0 and i != 0:
            pdf.showPage()
        position = i % 3 + 1
        shift = 283.5 * (position - 1)
        podatci = data['nalog_za_isplatu'][i]['podatci']
        pdf.line(300.51, 805.14 - shift, 300.51, 652.05 - shift)  # Vertical line
        pdf.line(28.35, 632.205 - shift, 184.275, 632.205 - shift)  # Line 1
        pdf.line(141.75, 609.525 - shift, 283.5, 609.525 - shift)  # Line 2
        pdf.line(323.19, 609.525 - shift, 425.25, 609.525 - shift)  # Line 3
        pdf.line(323.19, 632.205 - shift, 479.115, 632.205 - shift)  # Line 3
        pdf.setDash(10, 10)
        pdf.setLineWidth(0.5)
        pdf.line(0, 552.825 - shift, 595.27, 552.825 - shift)
        pdf.setDash(1, 0)
        pdf.setLineWidth(1.0)
        rectangles = [
            (28.35, 765.45 - shift, 255.15, 39.69),
            (28.35, 708.75 - shift, 255.15, 39.69),
            (28.35, 652.05 - shift, 255.15, 39.69),
            (323.19, 771.12 - shift, 34.02, 17.01),
            (368.55, 771.12 - shift, 34.02, 17.01),
            (425.25, 771.12 - shift, 141.75, 17.01),
            (368.55, 737.1 - shift, 198.45, 17.01),
            (323.19, 700.245 - shift, 34.02, 17.01),
            (368.55, 700.245 - shift, 198.45, 17.01),
        ]
        for rect in rectangles:
            pdf.rect(*rect)
        pdf.setFont('LiberationSerif', 12)
        pdf.drawCentredString(141.75, 795 - shift, str(podatci['isplatilac']['isplatilac1']))
        pdf.drawCentredString(141.75, 782 - shift, str(podatci['isplatilac']['isplatilac2']))
        pdf.drawCentredString(141.75, 769 - shift, str(podatci['isplatilac']['isplatilac3']))
        pdf.drawCentredString(141.75, 738.3 - shift, str(podatci['isplata']['svrha1']))
        pdf.drawCentredString(141.75, 725.3 - shift, str(podatci['isplata']['svrha2']))
        pdf.drawCentredString(141.75, 712.3 - shift, str(podatci['isplata']['svrha3']))
        pdf.drawCentredString(141.75, 681.6 - shift, str(podatci['primalac']['primalac1']))
        pdf.drawCentredString(141.75, 668.6 - shift, str(podatci['primalac']['primalac2']))
        pdf.drawCentredString(141.75, 655.6 - shift, str(podatci['primalac']['primalac3']))
        pdf.drawString(141.75, 611 - shift, str(podatci['mesto_datum']['datum']))
        pdf.drawString(210, 611 - shift, str(podatci['mesto_datum']['mesto']))
        pdf.drawString(323.19, 611 - shift, str(podatci['isplata']['datum_valute']))
        pdf.setFont('LiberationSerif', 14)
        pdf.drawString(370, 741 - shift, str(podatci['isplatilac']['racun_isplatioca']))
        pdf.drawString(326, 704 - shift, str(podatci['isplatilac']['model']))
        pdf.drawString(370, 704 - shift, str(podatci['isplatilac']['poziv_na_broj']))
        pdf.drawString(326, 775 - shift, str(podatci['isplata']['sifra_placanja']))
        pdf.drawString(370, 775 - shift, str(podatci['isplata']['valuta']))
        pdf.drawString(440, 775 - shift, str(podatci['isplata']['iznos']))
        pdf.drawString(323.19, 635 - shift, str(podatci['broj_licne']['broj_licne']))

        pdf.setFont('LiberationSerif', 9)
        pdf.drawString(28.35, 808.7 - shift, "Исплатилац")
        pdf.drawString(28.35, 752 - shift, "Сврха исплате")
        pdf.drawString(28.35, 695.3 - shift, "Прималац")
        pdf.drawString(28.35, 623.7 - shift, "Печат и потпис исплатиоца")
        pdf.drawString(141.75, 601.02 - shift, "Место и датум пријема")
        pdf.drawString(323.19, 601.02 - shift, "Датум валуте")
        pdf.drawString(323.19, 623.7 - shift, "Потпис примаоца и број личне карте")
        pdf.drawString(368.55, 719.255 - shift, "Позив на број (одобрење)")
        pdf.drawString(368.55, 756.11 - shift, "Рачун исплатиоца")
        pdf.drawString(425.25, 790.13 - shift, "Износ")
        pdf.drawString(368.55, 790.13 - shift, "Валута")
        pdf.drawString(323.19, 800.13 - shift, "Шифра")
        pdf.drawString(323.19, 790.13 - shift, "плаћања")
        pdf.drawString(323.19, 729.255 - shift, "Број")
        pdf.drawString(323.19, 719.255 - shift, "модела")

        pdf.setFont('LiberationSerif-Bold', 14)
        pdf.drawString(431, 775 - shift, '=')
        pdf.drawRightString(595.27 - 28.35, 805.14 - shift, "НАЛОГ ЗА ИСПЛАТУ")

        pdf.setFont('LiberationSerif', 7)
        pdf.drawCentredString(595.27 / 2, 584.01 - shift, "Образац бр. 2")
    pdf.showPage()
    pdf.save()
    return pdf

def nalog_za_prenos(file_path, data=None):
    pdfmetrics.registerFont(TTFont('LiberationSerif-Bold', 'LiberationSerif-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSerif', 'LiberationSerif-Regular.ttf'))
    pdf = canvas.Canvas(file_path, pagesize=(595.27, 841.89))
    broj_podataka = len(data['nalog_za_prenos'])
    for i in range(broj_podataka):
        if i % 3 == 0 and i != 0:
            pdf.showPage()
        position = i % 3 + 1
        shift = 283.5 * (position - 1)
        podatci = data['nalog_za_prenos'][i]['podatci']
        pdf.line(300.51, 805.14 - shift, 300.51, 652.05 - shift)  # Vertical line
        pdf.line(28.35, 632.205 - shift, 184.275, 632.205 - shift)  # Line 1
        pdf.line(141.75, 609.525 - shift, 283.5, 609.525 - shift)  # Line 2
        pdf.line(323.19, 609.525 - shift, 425.25, 609.525 - shift)  # Line 3
        pdf.setDash(10, 10)
        pdf.setLineWidth(0.5)
        pdf.line(0, 552.825 - shift, 595.27, 552.825 - shift)
        pdf.setDash(1, 0)
        pdf.setLineWidth(1.0)
        rectangles = [
            (28.35, 765.45 - shift, 255.15, 39.69),
            (28.35, 708.75 - shift, 255.15, 39.69),
            (28.35, 652.05 - shift, 255.15, 39.69),
            (323.19, 771.12 - shift, 34.02, 17.01),
            (368.55, 771.12 - shift, 34.02, 17.01),
            (425.25, 771.12 - shift, 141.75, 17.01),
            (323.19, 737.1 - shift, 243.81, 17.01),
            (323.19, 700.245 - shift, 34.02, 17.01),
            (368.55, 700.245 - shift, 198.45, 17.01),
            (323.19, 666.225 - shift, 243.81, 17.01),
            (323.19, 632.205 - shift, 34.02, 17.01),
            (368.55, 632.205 - shift, 198.45, 17.01),
            (504.63, 595.36 - shift, 17.01, 17.01),
        ]
        for rect in rectangles:
            pdf.rect(*rect)
        pdf.setFont('LiberationSerif', 12)
        pdf.drawCentredString(141.75, 795 - shift, str(podatci['platilac']['platilac1']))
        pdf.drawCentredString(141.75, 782 - shift, str(podatci['platilac']['platilac2']))
        pdf.drawCentredString(141.75, 769 - shift, str(podatci['platilac']['platilac3']))
        pdf.drawCentredString(141.75, 738.3 - shift, str(podatci['placanje']['svrha1']))
        pdf.drawCentredString(141.75, 725.3 - shift, str(podatci['placanje']['svrha2']))
        pdf.drawCentredString(141.75, 712.3 - shift, str(podatci['placanje']['svrha3']))
        pdf.drawCentredString(141.75, 681.6 - shift, str(podatci['primalac']['primalac1']))
        pdf.drawCentredString(141.75, 668.6 - shift, str(podatci['primalac']['primalac2']))
        pdf.drawCentredString(141.75, 655.6 - shift, str(podatci['primalac']['primalac3']))
        pdf.drawString(141.75, 611 - shift, str(podatci['mesto_datum']['datum']))
        pdf.drawString(210, 611 - shift, str(podatci['mesto_datum']['mesto']))
        pdf.drawString(323.19, 611 - shift, str(podatci['placanje']['datum_izvrsenja']))
        pdf.setFont('LiberationSerif', 14)
        pdf.drawString(327, 775 - shift, str(podatci['placanje']['sifra_placanja']))
        pdf.drawString(371, 775 - shift, str(podatci['placanje']['valuta']))
        pdf.drawString(440, 775 - shift, str(podatci['placanje']['iznos']))
        pdf.drawString(328, 742 - shift, str(podatci['platilac']['racun_platioca']))
        pdf.drawString(327, 704 - shift, str(podatci['platilac']['model']))
        pdf.drawString(371, 704 - shift, str(podatci['platilac']['poziv_na_broj']))
        pdf.drawString(327, 671 - shift, str(podatci['primalac']['racun_primaoca']))
        pdf.drawString(327, 636 - shift, str(podatci['primalac']['model']))
        pdf.drawString(371, 636 - shift, str(podatci['primalac']['poziv_na_broj']))

        pdf.setFont('LiberationSerif', 9)
        pdf.drawString(28.35, 808.7 - shift, "Платилац")
        pdf.drawString(28.35, 752 - shift, "Сврха плаћања")
        pdf.drawString(28.35, 695.3 - shift, "Прималац")
        pdf.drawString(28.35, 623.7 - shift, "Печат и потпис платиоца/примаоца")
        pdf.drawString(141.75, 601.02 - shift, "Место и датум пријема")
        pdf.drawString(323.19, 601.02 - shift, "Датум извршења")
        pdf.drawString(425.25, 790.13 - shift, "Износ")
        pdf.drawString(368.55, 790.13 - shift, "Валута")
        pdf.drawString(323.19, 800.13 - shift, "Шифра")
        pdf.drawString(323.19, 790.13 - shift, "плаћања")
        pdf.drawString(323.19, 756.11 - shift, "Рачун платиоца")
        pdf.drawString(323.19, 720.000 - shift, "Позив на број (задужења)")
        pdf.drawString(323.19, 685.235 - shift, "Рачун примаоца")
        pdf.drawString(323.19, 651.960 - shift, "Позив на број (одобрење)")
        pdf.drawCentredString(513.135, 586 - shift, "Хитно")
        pdf.setFont('LiberationSerif-Bold', 14)
        pdf.drawString(431, 775 - shift, '=')
        pdf.drawRightString(595.27 - 28.35, 805.14 - shift, "НАЛОГ ЗА ПРЕНОС")
        pdf.setFont('LiberationSerif', 7)
        pdf.drawCentredString(595.27 / 2, 584.01 - shift, "Образац бр. 3")
        if [podatci['placanje']['hitno']] == [True]:
            pdf.line(504.63, 595.36 - shift, 521.64, 612.37 - shift)
            pdf.line(504.63, 612.37 - shift, 521.64, 595.36 - shift)

    pdf.showPage()
    pdf.save()
    return pdf

def ucitaj_excel_nalog_za_uplatu():
    json_result = {"nalog_za_uplatu": []}
    file_path = 'nalog_za_uplatu.xlsx'
    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        uplatilac = {
            "uplatilac1": row["uplatilac.uplatilac1"],
            "uplatilac2": row["uplatilac.uplatilac2"],
            "uplatilac3": row["uplatilac.uplatilac3"]
        }
        uplata = {
            "svrha1": row["uplata.svrha1"],
            "svrha2": row["uplata.svrha2"],
            "svrha3": row["uplata.svrha3"],
            "datum_valute": row["uplata.datum_valute"],
            "sifra_placanja": row["uplata.sifra_placanja"],
            "valuta": row["uplata.valuta"],
            "iznos": row["uplata.iznos"]
        }
        primalac = {
            "primalac1": row["primalac.primalac1"],
            "primalac2": row["primalac.primalac2"],
            "primalac3": row["primalac.primalac3"],
            "racun_primaoca": row["primalac.racun_primaoca"],
            "model": row["primalac.model"],
            "poziv_na_broj": row["primalac.poziv_na_broj"]
        }
        mesto_datum = {
            "mesto": row["mesto_datum.mesto"],
            "datum": row["mesto_datum.datum"]
        }
        podatci = {
            "broj": row["broj"],
            "pozicija": row["pozicija"],
            "uplatilac": uplatilac,
            "uplata": uplata,
            "primalac": primalac,
            "mesto_datum": mesto_datum
        }
        json_result["nalog_za_uplatu"].append({"podatci": podatci})
    return json_result

def ucitaj_excel_nalog_za_isplatu():
    json_result = {"nalog_za_isplatu": []}
    file_path = 'nalog_za_isplatu.xlsx'
    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        isplatilac = {
            "isplatilac1": row["isplatilac.isplatilac1"],
            "isplatilac2": row["isplatilac.isplatilac2"],
            "isplatilac3": row["isplatilac.isplatilac3"],
            "racun_isplatioca": row["isplatilac.racun_isplatioca"],
            "model": row["isplatilac.model"],
            "poziv_na_broj": row["isplatilac.poziv_na_broj"]
        }
        isplata = {
            "svrha1": row["isplata.svrha1"],
            "svrha2": row["isplata.svrha2"],
            "svrha3": row["isplata.svrha3"],
            "datum_valute": row["isplata.datum_valute"],
            "sifra_placanja": row["isplata.sifra_placanja"],
            "valuta": row["isplata.valuta"],
            "iznos": row["isplata.iznos"]
        }
        primalac = {
            "primalac1": row["primalac.primalac1"],
            "primalac2": row["primalac.primalac2"],
            "primalac3": row["primalac.primalac3"],
        }
        mesto_datum = {
            "mesto": row["mesto_datum.mesto"],
            "datum": row["mesto_datum.datum"]
        }
        broj_licne = {
            "broj_licne": row["broj_licne"]
        }
        podatci = {
            "broj": row["broj"],
            "pozicija": row["pozicija"],
            "isplatilac": isplatilac,
            "isplata": isplata,
            "primalac": primalac,
            "mesto_datum": mesto_datum,
            "broj_licne": broj_licne
        }
        json_result["nalog_za_isplatu"].append({"podatci": podatci})
    return json_result

def ucitaj_excel_nalog_za_prenos():
    json_result = {"nalog_za_prenos": []}
    file_path = 'nalog_za_prenos.xlsx'
    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        platilac = {
            "platilac1": row["platilac.platilac1"],
            "platilac2": row["platilac.platilac2"],
            "platilac3": row["platilac.platilac3"],
            "racun_platioca": row["platilac.racun_platioca"],
            "model": row["platilac.model"],
            "poziv_na_broj": row["platilac.poziv_na_broj"]
        }
        placanje = {
            "svrha1": row["placanje.svrha1"],
            "svrha2": row["placanje.svrha2"],
            "svrha3": row["placanje.svrha3"],
            "datum_izvrsenja": row["placanje.datum_izvrsenja"],
            "sifra_placanja": row["placanje.sifra_placanja"],
            "valuta": row["placanje.valuta"],
            "iznos": row["placanje.iznos"],
            "hitno": row["placanje.hitno"],
        }
        primalac = {
            "primalac1": row["primalac.primalac1"],
            "primalac2": row["primalac.primalac2"],
            "primalac3": row["primalac.primalac3"],
            "racun_primaoca": row["primalac.racun_primaoca"],
            "model": row["primalac.model"],
            "poziv_na_broj": row["primalac.poziv_na_broj"],
        }
        mesto_datum = {
            "mesto": row["mesto_datum.mesto"],
            "datum": row["mesto_datum.datum"]
        }
        podatci = {
            "broj": row["broj"],
            "pozicija": row["pozicija"],
            "platilac": platilac,
            "placanje": placanje,
            "primalac": primalac,
            "mesto_datum": mesto_datum,
        }
        json_result["nalog_za_prenos"].append({"podatci": podatci})
    return json_result


#primeri kako treba da izgleda json za svaki nalog (nalog_za_uplatu, nalog_za_isplatu, nalog_za_prenos)

data = {
    "nalog_za_uplatu": [
        {
            "podatci": {
                "broj": 1,
                "pozicija": 1,
                "uplatilac": {
                    "uplatilac1": "uplatilac red 1",
                    "uplatilac2": "uplatilac red 2",
                    "uplatilac3": "uplatilac red 3",
                },
                "uplata": {
                    "svrha1": "Svrha uplate red 1",
                    "svrha2": "Svrha uplate red 2",
                    "svrha3": "Svrha uplate red 3",
                    "datum_valute": "datum valute",
                    "sifra_placanja": "240",
                    "valuta": "123",
                    "iznos": "iznos uplate",
                },
                "primalac": {
                    "primalac1": "Primalac red 1",
                    "primalac2": "Primalac red 2",
                    "primalac3": "Primalac red 3",
                    "racun_primaoca": "racun primaoca",
                    "model": "97",
                    "poziv_na_broj": "poziv na broj",
                },
                "mesto_datum": {
                    "mesto": "Novi Sad",
                    "datum": "12.12.2019"
                },
            },
        },
        {
            "podatci": {
                "broj": 2,
                "pozicija": 2,
                "uplatilac": {
                    "uplatilac1": "uPLATILAC 2",
                    "uplatilac2": "uplatilac red 2",
                    "uplatilac3": "uplatilac red 3",
                },
                "uplata": {
                    "svrha1": "Svrha uplate red 1",
                    "svrha2": "Svrha uplate red 2",
                    "svrha3": "Svrha uplate red 3",
                    "datum_valute": "datum valute",
                    "sifra_placanja": "240",
                    "valuta": "123",
                    "iznos": "iznos uplate",
                },
                "primalac": {
                    "primalac1": "Primalac red 1",
                    "primalac2": "Primalac red 2",
                    "primalac3": "Primalac red 3",
                    "racun_primaoca": "racun primaoca",
                    "model": "97",
                    "poziv_na_broj": "poziv na broj",
                },
                "mesto_datum": {
                    "mesto": "Novi Sad",
                    "datum": "12.12.2019"
                },
            },
        },
        {
            "podatci": {
                "broj": 3,
                "pozicija": 3,
                "uplatilac": {
                    "uplatilac1": "uPLATILAC 3",
                    "uplatilac2": "uplatilac red 2",
                    "uplatilac3": "uplatilac red 3",
                },
                "uplata": {
                    "svrha1": "Svrha uplate red 1",
                    "svrha2": "Svrha uplate red 2",
                    "svrha3": "Svrha uplate red 3",
                    "datum_valute": "datum valute",
                    "sifra_placanja": "240",
                    "valuta": "123",
                    "iznos": "iznos uplate",
                },
                "primalac": {
                    "primalac1": "Primalac red 1",
                    "primalac2": "Primalac red 2",
                    "primalac3": "Primalac red 3",
                    "racun_primaoca": "racun primaoca",
                    "model": "97",
                    "poziv_na_broj": "poziv na broj",
                },
                "mesto_datum": {
                    "mesto": "Novi Sad",
                    "datum": "12.12.2019"
                },
            },
        },

    ],
    "nalog_za_isplatu": [
        {
            "podatci": {
                "broj": 1,
                "pozicija": 1,
                "isplatilac": {
                    "isplatilac1": "Isplatilac red 1",
                    "isplatilac2": "Isplatilac red 2",
                    "isplatilac3": "Isplatilac red 3",
                    "racun_isplatioca": "Racun isplatioca",
                    "model": "97",
                    "poziv_na_broj": "Poziv na broj",
                },
                "isplata": {
                    "svrha1": "svrha isplate red 1",
                    "svrha2": "svrha isplate red 2",
                    "svrha3": "svrha isplate red 3",
                    "datum_valute": "12.12.2019",
                    "sifra_placanja": "240",
                    "valuta": "VVV",
                    "iznos": "iznos isplate",
                },
                "primalac": {
                    "primalac1": "Primalac red 1",
                    "primalac2": "Primalac red 2",
                    "primalac3": "Primalac red 3",
                },
                "mesto_datum": {
                    "mesto": "Novi Sad",
                    "datum": "12.12.2019"
                },
                "broj_licne": {
                    "broj_licne": "Broj Licne"
                },
            }
        },
        {
            "podatci": {
                "broj": 2,
                "pozicija": 2,
                "isplatilac": {
                    "isplatilac1": "red 2",
                    "isplatilac2": "Isplatilac red 2",
                    "isplatilac3": "Isplatilac red 3",
                    "racun_isplatioca": "Racun isplatioca",
                    "model": "97",
                    "poziv_na_broj": "Poziv na broj",
                },
                "isplata": {
                    "svrha1": "svrha isplate red 1",
                    "svrha2": "svrha isplate red 2",
                    "svrha3": "svrha isplate red 3",
                    "datum_valute": "12.12.2019",
                    "sifra_placanja": "240",
                    "valuta": "VVV",
                    "iznos": "iznos isplate",
                },
                "primalac": {
                    "primalac1": "Primalac red 1",
                    "primalac2": "Primalac red 2",
                    "primalac3": "Primalac red 3",
                },
                "mesto_datum": {
                    "mesto": "Novi Sad",
                    "datum": "12.12.2019"
                },
                "broj_licne": {
                    "broj_licne": "Broj Licne"
                },
            }
        },
    ],
    "nalog_za_prenos": [
        {
            "podatci": {
                "broj": 1,
                "pozicija": 1,
                "platilac": {
                    "platilac1": "broj 1",
                    "platilac2": "Platilac red 2",
                    "platilac3": "Platilac red 3",
                    "racun_platioca": "Racun platioca",
                    "model": "97",
                    "poziv_na_broj": "Poziv na broj platoca"
                },
                "placanje": {
                    "svrha1": "Svrha placanja red 1",
                    "svrha2": "Svrha placanja red 2",
                    "svrha3": "Svrha placanja red 3",
                    "datum_izvrsenja": "12.12.2019",
                    "sifra_placanja": "240",
                    "valuta": "123",
                    "iznos": "iznos placanja",
                    "hitno": False,
                },
                "primalac": {
                    "primalac1": "Primalac red 1",
                    "primalac2": "Primalac red 2",
                    "primalac3": "Primalac red 3",
                    "racun_primaoca": "Racun primaoca",
                    "model": "97",
                    "poziv_na_broj": "Poziv na broj primalaca"
                },
                "mesto_datum": {
                    "mesto": "Novi Sad",
                    "datum": "12.12.2019"
                }
            }
        },
        {
            "podatci": {
                "broj": 2,
                "pozicija": 2,
                "platilac": {
                    "platilac1": "broj 2",
                    "platilac2": "Platilac red 2",
                    "platilac3": "Platilac red 3",
                    "racun_platioca": "Racun platioca",
                    "model": "97",
                    "poziv_na_broj": "Poziv na broj platoca",
                },
                "placanje": {
                    "svrha1": "Svrha placanja red 1",
                    "svrha2": "Svrha placanja red 2",
                    "svrha3": "Svrha placanja red 3",
                    "datum_izvrsenja": "12.12.2019",
                    "sifra_placanja": "240",
                    "valuta": "123",
                    "iznos": "iznos placanja",
                    "hitno": False,
                },
                "primalac": {
                    "primalac1": "Primalac red 1",
                    "primalac2": "Primalac red 2",
                    "primalac3": "Primalac red 3",
                    "racun_primaoca": "Racun primaoca",
                    "model": "97",
                    "poziv_na_broj": "Poziv na broj primalaca"
                },
                "mesto_datum": {
                    "mesto": "Novi Sad",
                    "datum": "12.12.2019",
                },
            }
        },
        {
            "podatci": {
                "broj": 3,
                "pozicija": 3,
                "platilac": {
                    "platilac1": "Platilac red 1",
                    "platilac2": "Platilac red 2",
                    "platilac3": "Platilac red 3",
                    "racun_platioca": "Racun platioca",
                    "model": "97",
                    "poziv_na_broj": "Poziv na broj platoca"
                },
                "placanje": {
                    "svrha1": "Svrha placanja red 1",
                    "svrha2": "Svrha placanja red 2",
                    "svrha3": "Svrha placanja red 3",
                    "datum_izvrsenja": "12.12.2019",
                    "sifra_placanja": "240",
                    "valuta": "123",
                    "iznos": "iznos placanja",
                    "hitno": True,
                },
                "primalac": {
                    "primalac1": "Primalac red 1",
                    "primalac2": "Primalac red 2",
                    "primalac3": "Primalac red 3",
                    "racun_primaoca": "Racun primaoca",
                    "model": "97",
                    "poziv_na_broj": "Poziv na broj primalaca"
                },
                "mesto_datum": {
                    "mesto": "Novi Sad",
                    "datum": "12.12.2019"
                },
            },
        },
        {
            "podatci": {
                "broj": 4,
                "pozicija": 1,
                "platilac": {
                    "platilac1": "Platilac red 1",
                    "platilac2": "Platilac red 2",
                    "platilac3": "Platilac red 3",
                    "racun_platioca": "Racun platioca",
                    "model": "97",
                    "poziv_na_broj": "Poziv na broj platoca"
                },
                "placanje": {
                    "svrha1": "Svrha placanja red 1",
                    "svrha2": "Svrha placanja red 2",
                    "svrha3": "Svrha placanja red 3",
                    "datum_izvrsenja": "12.12.2019",
                    "sifra_placanja": "240",
                    "valuta": "123",
                    "iznos": "iznos placanja",
                    "hitno": True,
                },
                "primalac": {
                    "primalac1": "Primalac red 1",
                    "primalac2": "Primalac red 2",
                    "primalac3": "Primalac red 3",
                    "racun_primaoca": "Racun primaoca",
                    "model": "97",
                    "poziv_na_broj": "Poziv na broj primalaca"
                },
                "mesto_datum": {
                    "mesto": "Novi Sad",
                    "datum": "12.12.2019"
                },
            },
        },
        {
            "podatci": {
                "broj": 5,
                "pozicija": 2,
                "platilac": {
                    "platilac1": "Platilac red 1",
                    "platilac2": "Platilac red 2",
                    "platilac3": "Platilac red 3",
                    "racun_platioca": "Racun platioca",
                    "model": "97",
                    "poziv_na_broj": "Poziv na broj platoca"
                },
                "placanje": {
                    "svrha1": "Svrha placanja red 1",
                    "svrha2": "Svrha placanja red 2",
                    "svrha3": "Svrha placanja red 3",
                    "datum_izvrsenja": "12.12.2019",
                    "sifra_placanja": "240",
                    "valuta": "123",
                    "iznos": "iznos placanja",
                    "hitno": True,
                },
                "primalac": {
                    "primalac1": "Primalac red 1",
                    "primalac2": "Primalac red 2",
                    "primalac3": "Primalac red 3",
                    "racun_primaoca": "Racun primaoca",
                    "model": "97",
                    "poziv_na_broj": "Poziv na broj primalaca"
                },
                "mesto_datum": {
                    "mesto": "Novi Sad",
                    "datum": "12.12.2019"
                },
            },
        },
    ],
}

nalog_za_uplatu('nalog_za_uplatu.pdf', data)
nalog_za_isplatu('nalog_za_isplatu.pdf', data)
nalog_za_prenos('nalog_za_prenos.pdf', data)

nalog_za_uplatu('nalog_za_uplatu_1.pdf', ucitaj_excel_nalog_za_uplatu())
nalog_za_isplatu('nalog_za_isplatu_1.pdf', ucitaj_excel_nalog_za_isplatu())
nalog_za_prenos('nalog_za_prenos_1.pdf', ucitaj_excel_nalog_za_prenos())
