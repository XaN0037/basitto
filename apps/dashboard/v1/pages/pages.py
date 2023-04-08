from base.slavar import TXT


def header(lan='uz'):
    return{
        "magazin":TXT['MAGAZIN'][lan],
        "telefon qil":TXT['QONGIROQ'][lan],
        "raqamni ko'rish":TXT["TELEFON"][lan],
        "tahrirlash":TXT["TAHIRIRLASH"][lan],
        "tahrirparol":TXT["TAHRIRPAROL"][lan],
        "logout":TXT["CHIQISH"][lan],
        "sevimlimlar":TXT["SEVIMLILAR"][lan],
        "qidiruv":TXT["QIDIRUV"][lan],
        "sevimlilarim":TXT["SEVIMLILARIM"][lan],
        "korzina":TXT["KORZINA"][lan],

    }

def footer(lan='uz'):

    return {
    "xaridor": TXT['XARIDOR'][lan],
    "tulovyetkaz": TXT['TOLOVVAYETKAZISH'][lan],

    "savoljavob": TXT['SAVOLJAVOB'][lan],
    "rassroch": TXT['RASROCHKA'][lan],
    "obmen": TXT['ALMASHTIRISH'][lan],

    "garant": TXT['GARANTIYA2'][lan],
    "offerta": TXT['OFFERTA'][lan],
    "status": TXT['STATUS'][lan],
    "ariza": TXT['ARIZA'][lan],
    "kompaniya": TXT['KOMPANIYA'][lan],
    "bizhaqimiz": TXT['BIZHAQIMIZDA'][lan],
    "blog": TXT['BLOG'][lan],
    "vakansiya": TXT['VAKANSIA'][lan],
    "kontact": TXT['KONTAKTI'][lan],
    "rekvizit": TXT['REKVIZITLAR'][lan],
    "prinsp": TXT['PRINSPLAR'][lan],
    "ishlabch": TXT['ISHLAPCHIQARISH'][lan],
    "takliflar": TXT['TAKLIFLAR'][lan],
    "bonus": TXT['BONUSPRO'][lan],
    "aksiya": TXT['AKSIYALAR'][lan],
    "chegirma": TXT['CHEGIRMALAR'][lan],
    "rekom": TXT['REKOMENDATSIYA'][lan],
    "detal": TXT['DETALNIIY'][lan],
    "partnyor": TXT['PARTNYOR'][lan],
    "franch": TXT['FRANCHAYZING'][lan],
    "yuridik": TXT['YURIDIKAM'][lan],
    "otele": TXT['OTELE'][lan],
    "ulgurci": TXT['ULGURCHITAKLIF'][lan],
    "yangiliklar": TXT['YANGILIKLAR'][lan],


    }


def page1(lan="uz"):
    page={
        "xaridor": TXT['XARIDOR'][lan],
        "xaridor": TXT['XARIDOR'][lan],

    }


    return {

        "header": header(lan),

        "page":page,

        "footer": footer(lan)

    }

def page2(lan="uz"):
    page={
        "manziltext": TXT['MANZILTEXT'][lan],

    }

    return {
        "header": header(lan),
        "page":page,
        "footer": footer(lan)

    }



def page3(lan="uz"):
    cont1={
        "header": header(lan)

    }



