from base.slavar import TXT


def header(lan='uz'):
    return {
        # """qidiruv........"""
        "qidiruv": TXT["QIDIRUV"][lan],
        "dangara": TXT["Dangara"][lan],
        "chiqish": TXT["Chiqish"][lan],
        # """user"""

        "tahrirlash": TXT["TAHIRIRLASH"][lan],
        "tahrirparol": TXT["TAHRIRPAROL"][lan],
        "logout": TXT["CHIQISH"][lan],
        # """izbr"""
        "sevimlilarim": TXT["SEVIMLILARIM"][lan],
        "sevimlilar": TXT["SEVIMLILAR"][lan],
        # """korzina"""
        "korzina": TXT["KORZINA"][lan],
        "tovar": TXT["TOVAR2"][lan],
        "summ": TXT["SOM"][lan],
        "kupit": TXT["KUPIT"][lan],
        "xarid": TXT["BIRGAXARID"][lan],
        "jami": TXT["JAMI"][lan],

        # # "magazin":TXT['MAGAZIN'][lan],
        # "telefon qil":TXT['QONGIROQ'][lan],
        # "raqamni ko'rish":TXT["TELEFON"][lan],
        # # "tahrirlash":TXT["TAHIRIRLASH"][lan],
        # # "tahrirparol":TXT["TAHRIRPAROL"][lan],
        # # "logout":TXT["CHIQISH"][lan],
        #

    }


def footer(lan='uz'):
    return {
        "xaridor": TXT['XARIDOR'][lan],
        "yetkaz": TXT['TOLOVVAYETKAZISH'][lan],
        "garant": TXT['GARANTIYA2'][lan],
        "ariza": TXT['ARIZA'][lan],
        "taklif": TXT['TAKLIFLAR'][lan],
        "aksiya": TXT['AKSIYALAR'][lan],
        "chegirma": TXT['CHEGIRMALAR'][lan],
        "detalniy": TXT['DETALNIIY'][lan],
        "kompaniy": TXT['KOMPANIYA'][lan],
        "bizhaqimizda": TXT['BIZHAQIMIZDA'][lan],
        "kontact": TXT['KONTAKTI'][lan],
        "ishlabchiq": TXT['ISHLAPCHIQARISH'][lan],
        "partnyor": TXT['PARTNYOR'][lan],
        "yuridik": TXT['YURIDIKAM'][lan],
        "ulgurchi": TXT['ULGURCHITAKLIF'][lan],
        "yangilik": TXT['YANGILIKLAR'][lan],
        "fintech": TXT['ISHLABCHIQILGAN'][lan],
        "maxfiylik": TXT['MAXFIYLIK'][lan],

    }


def page1(lan="uz"):
    page = {
        "yangi": TXT['YANGI'][lan],
        "manzil": TXT['MANZILI'][lan],
        "xarita": TXT['XARITA'][lan],
        "manzil2": TXT['MANZILTEXT'][lan],
        "zakaz": TXT['ZAKAZ'][lan],
        "skid": TXT['QOSHIMCHASKIDKA'][lan],
        "inovatsiya": TXT['INNOVATSIYA'][lan],
        "ishonch": TXT['UVERENNOST'][lan],
        "bizgayoz": TXT['BIZGAYOZING'][lan],
        "javob": TXT['JAVOB'][lan],
        "savolberish": TXT['SAVOLBERISH'][lan],
        "maslaxatchi": TXT['MASLAHATCHI'][lan],
        "telqil": TXT['TELQIL'][lan],
        "tezjavob": TXT['TEZJAVOB'][lan],
        "savolgajavob": TXT['SAVOLLARGAJAVOB'][lan],
        "bulimoching": TXT['BOLIMNIOCHING'][lan],
    }

    return {

        "header": header(lan),

        "page": page,

        "footer": footer(lan)

    }


def page2(lan="uz"):
    page = {
        "kod": TXT['KOD'][lan],
        "hajm": TXT['Hajm'][lan],
        "dan": TXT['DAN'][lan],
        "rang": TXT['RANGI'][lan],
        "savatqo'sh": TXT['SAVATGAQOSHISH'][lan],
        "xarid": TXT['KUPIT'][lan],
        "yetkazish": TXT['YETKAZISHVAOLISH'][lan],
        "xususiyat": TXT['XUSUSIYATLARI2'][lan],
        "tavsif": TXT['TAVSIF'][lan],
        "sharx": TXT['SHARHLAR'][lan],

    }
    page_dostavka = {
        "yetkazish": TXT['YETKAZISHVAOLISH'][lan],
        "shahar": TXT['SHAHAR'][lan],
        "uzbyetkazish": TXT['UZBYETKAZISH'][lan],
        "mdhyetkazish": TXT['MDHYETKAZISH'][lan],
        "pullik": TXT['PULLIK'][lan],
        "ulgurji": TXT['ULGURJI'][lan],
        "olibketish": TXT['OLIBKETISH'][lan],
        "olibketishmumkin": TXT['OLSHINGIZMUMKUN'][lan],
        "kelishibolish": TXT['KELISHIBOLSIH'][lan],
        "tasdiqlashkod": TXT['TASIDLASHKODINIOLING'][lan],
        "buyurtmaraqam": TXT['BUYURTMAKODINIOLING'][lan],
        "vaqtkelish": TXT['VAQTNIKELISHING'][lan],
        "xizmatqoida": TXT['XIZMATQOIDALARI'][lan],
        "chipta": TXT['CHIPTANIOLING'][lan],
        "bayram": TXT['BAYRAMDAM'][lan],

    }

    return {
        "header": header(lan),
        "page": page,
        "page_dostavka": page_dostavka,
        "footer": footer(lan)

    }


def page3(lan="uz"):
    cont1 = {
        "header": header(lan)

    }
