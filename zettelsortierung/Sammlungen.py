from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True, slots=True)
class Label:
    sammlung: Enum
    confidence: float


@dataclass(frozen=True, slots=True)
class Classifier:
    title: str
    description: str


class Classifiers(Enum):
    MANUELL = Classifier("Manuell", "Händisch gelabelt")
    OCR = Classifier("OCR", "Mittels OCR-Ergebnissen sortiert")


@dataclass(frozen=True, slots=True)
class Sammlung:
    description: str
    title: str | None = None
    search_term: str | None = None
    landschaft: str | None = None
    kreis: str | None = None
    ort: str | None = None
    alias: str | None = None


class Sammlungen(Enum):
    SKIPPED = Sammlung(
        description="Vorerst übersprungene Zettel",
        title="Skipped",
    )
    FRAGEBOGEN = Sammlung(
        description="Verzettelung eines nicht weiter bestimmten Fragebogens",
        title="Fragebogen",
    )
    VERWEIS = Sammlung(
        description="Verweis",
    )

    ABELER = Sammlung(
        description="Abeler, J., Wörterbuch der Mundart von Ahlen, Kr. Beckum",
        alias="Ahlen A.",
    )
    ABH_NAT = Sammlung(
        description="Abhandlungen aus dem Westfälischen Provinzial-Museum für Naturkunde. Jg. 7 ff.: Abhandlungen aus dem Landesmuseum der Provinz Westfalen, Museum für Naturkunde",
        alias="Abh. Prov. Mus. f. Natrukde|Iserlohn Extbr",
    )
    AFFERDE = Sammlung(
        description="Afferde, Kr. Unna (August Ebbinghaus)",
        alias="Afferde E",
        kreis="Unn",
        ort="Af",
    )
    AHLING = Sammlung(
        description="Ahling",
        alias="Ahling",
    )
    ALT_HA = Sammlung(
        description="Alt Ha",
        alias="Alt Ha",
        kreis="Alt",
        ort="Ha",
    )
    ALTENA = Sammlung(
        description="Altena (Frau Karoline Krummenerl, * 1847, Fritz Künne, Fräulein Mina Künne, Frau Mina Vedder)",
        alias="Altena",
        kreis="Alt",
        ort="Al",
    )
    ARCH_RKLH = Sammlung(
        description="Archiv Recklinghausen",
        title="Archiv Recklinghausen",
    )
    ARING = Sammlung(
        description="Aring",
        kreis="Bch",
        ort="He",
    )
    ARENS = Sammlung(
        description="Arens, J., Der Vokalismus der Mundarten im Kreise Olpe unter Zugrundelegung der Mundart von Elspe.",
        alias="Arens",
        kreis="Olp",
    )
    ARNDTS = Sammlung(
        description="Sammlung Arndts",
    )
    ASD_VR = Sammlung(
        description="Asd Vr=Hö",
        kreis="Asd",
        ort="Vr",
    )
    ASSINGHAUSEN = Sammlung(
        description="Assinghausen, Kr. Brilon (Frau Knoche)",
        alias="Bri Ah",
        kreis="Bri",
        ort="Ah",
    )
    ATLAS_FRGB = Sammlung(
        description="Atlas-Fragebogen",
    )

    BAADER = Sammlung(
        description="Baader-Fragebögen und Baader-Nachlass",
        alias="Baader|BaaderOsnabr",
        title="Baader",
    )
    BAADER_NL = Sammlung(
        description="Baader Nachlass",
    )
    BAHLMANN = Sammlung(
        description="?Bahlmann, P., Münsterische Lieder und Sprichwörter in plattdeutscher Sprache. Mit einer Einleitung über Münster's niederdeutsche Litteratur.",
        alias="Bahlmann",
        landschaft="Münsterl",
    )
    BALKENHOLL = Sammlung(
        description="Balkenholl",
        alias="Balkenholl",
    )
    BANDWIRK = Sammlung(
        description="Bandwirk.",
        alias="Bandwirk.",
        kreis="Enr",
        ort="Sw",
    )
    BARLO = Sammlung(
        description="Barlo, Kr. Borken (Bauer Brake)",
        alias="Bor Ba",
        kreis="Bor",
        ort="Ba",
    )
    BAUER_C = Sammlung(
        description="Bauer, K., Waldeckisches Wörterbuch nebst Dialektproben, hrsg. v. H. Collitz.",
        alias="Bauer-C",
        kreis="Wal",
    )
    BBR_WU = Sammlung(
        description="BbrWu",
    )
    BECKMANN = Sammlung(
        description="Beckamm",
        alias="Beckmann",
        kreis="Bch",
        ort="Ld",
    )
    BEESTERMOELLER = Sammlung(
        description="Studienassessor Dr. A. Beestermöller (Beesten, Kr. Lingen)",
        alias="Beesten Be",
        kreis="Lin",
        ort="Be",
    )
    BEISENHERZ = Sammlung(
        description="Beisenherz, H., Vokalismus der Mundart des nordöstlichen Landkreises Dortmund.",
        alias="Kurl Beis.",
        kreis="Dor",
        ort="Ku",
    )
    BEK_LB = Sammlung(
        description="Bek Lb",
        kreis="Bek",
        ort="Lb",
    )
    BERGER = Sammlung(
        description="Berger, A., Niederdeutsche technische Ausdrücke aus der Handwerkersprache des Kreises Lingen. ",
        alias="Lin Pl (Berger)",
        kreis="Lin",
        ort="Pl",
    )
    BIENENZUCHT = Sammlung(
        description="Fragebogen zu besonderen Themen: Bienenzucht",
        alias="Bienenzucht",
    )
    BIRKENHAUER = Sammlung(
        description="Birkenhauer, J., Die Mundarten im Osten des Herzogtums Westfalen (die heutigen Kreise Brilon und Meschede umfassend). Phil. Diss.",
        alias="Birkenhauer",
    )
    BLESKEN = Sammlung(
        description="Rektor A. Blesken (Ampen, Kr. Soest)",
        alias="Ampen Kr|A. H. Blesken",
        kreis="Sos",
        ort="Am",
    )
    BLESKEN_SP = Sammlung(
        description="Blesken Sprichwörter",
        alias="Blesken:Sprichwörter",
    )
    BO_LAER = Sammlung(
        description="Bochum - Laer",
        alias="Bochum - Laer",
        kreis="Bch",
        ort="Lr",
    )
    BOEHMER = Sammlung(
        description="Dr. E. Böhmer (Schwelm)",
        alias="Schwelm B",
        kreis="Enr",
        ort="Sw",
    )
    BOERDE_BL = Sammlung(
        description="Soester Börde Bl.",
    )
    BOR_KR = Sammlung(
        description="Bor Kr",
        alias="Bor Kr",
        kreis="Bor",
        ort="Kr",
    )
    BRAKEL_HOEX = Sammlung(
        description="Brakel Höx",
        alias="Brakel Höx",
        kreis="Höx",
        ort="Br",
    )
    BROCKHAUSEN = Sammlung(
        description="Brockhsn. / Sos",
        kreis="Sos",
        ort="Br",
    )
    BUEDERICH_FK = Sammlung(
        description="F. Kortmann, Büderich Kr. Soest",
        kreis="Sos",
        ort="Bü",
    )
    BUELD = Sammlung(
        description="Büld, H., Volk und Sprache im nördlichen Westfalen. Westfälische Ortschaften im Spiegel ihrer Sprache.",
        alias="Büld: Volk u. Spr.",
    )
    BUER_TUE = Sammlung(
        description="Bür Tü",
        kreis="Bür",
        ort="Tü",
    )
    BULDT = Sammlung(
        description="Buldt",
        alias="Buldt|Aschend.-Ems|Asd Ad",
        kreis="Asd",
        ort="Ad",
    )
    BULMAHN = Sammlung(
        description="H. Bulmahn",
        alias="H. Bulmahn|Ilvese/Jlvese",
        kreis="Min",
        ort="Il",
    )
    BWPV = Sammlung(
        description="Jahres-Bericht des Westfälischen Provinzial-Vereins für Wissenschaft und Kunst.",
        alias="Ber. Westf. Prov. Ver.",
    )

    C_SCHULTE = Sammlung(
        description="C Schulte",
        kreis="Lst",
        ort="Ag",
    )
    CRAMER = Sammlung(
        description="Mittelschulrektor H. Cramer (Niedersfeld, Kr. Brilon)",
        alias="Niedersfeld / Bri C.",
    )

    DAHMS = Sammlung(
        description="Dr. Dahms, W., Flora von Oelde 1914",
        alias="Dahms: Flora v. Oelde",
        kreis="Bek",
        ort="Ol",
    )
    DEILINGHOFEN = Sammlung(
        description="Deilinghofen, Kr. Iserlohn (Frau Alwine Kötter, August Kötter, Melchior Dietrich Tümena, Karl Tümena, Frau Mariechen Tümena)",
        alias="Deilingh",
        kreis="Isl",
        ort="Dh",
    )
    DITTMAR = Sammlung(
        description="Pastor Dittmar (Königsstele b. Essen)",
        alias="Königssteele Dittmar",
        kreis="Ess",
        ort="Ks",
    )
    DRENSTEINFURT = Sammlung(
        description="Drensteinfurt, Kr. Lüdinghausen (Karl Wagenfeld)",
        alias="Drenst. Wa",
        kreis="Lhs",
        ort="Dr",
    )
    DWA = Sammlung(
        description="Deutscher Wortatlas",
        title="DWA",
    )

    ECKARDT = Sammlung(
        description="Schlachthofdirektor Dr. Eckardt (Wellinghofen b. Dortmund)",
        alias="Dor Wl",
        kreis="Dor",
        ort="Wl",
    )
    EGGERS = Sammlung(
        description="Adolf Eggers Borken",
        alias="Eggers",
        kreis="Bor",
        ort="Bo",
    )
    EICKUM = Sammlung(
        description="Eickum",
        alias="Eickum",
        kreis="Hfd",
        ort="Ei",
    )
    ELSEY = Sammlung(
        description="Elsey, Kr. Iserlohn (Oberregierungsrat Ernst Braß, Frau Elfriede Braß, Frau Wilhelmine Braß, Dr. med. Karl Heidsieck, Wilhelm Heidsieck, Fräulein Elisabeth Heidsieck, Fräulein Marie Heidsieck, Frau Schöneberg, Frau Voß)",
        alias="Elsey",
        kreis="Isl",
        ort="El",
    )
    ENDORF = Sammlung(
        description="Endorf, Kr. Arnsberg (stud. phil. Maria Rörig)",
        alias="Endorf R",
        kreis="Arn",
        ort="En",
    )
    ENSTE = Sammlung(
        description="Postsekretär Enste (Warstein, Kr. Arnsberg)",
        alias="Warstein E.",
        kreis="Arn",
        ort="Wa",
    )
    ESSEN_TRINKEN = Sammlung(
        description="Fragebogen zu besonderen Themen: Essen und Trinken",
        alias="Essen u. Trinken",
    )

    FLURNAMEN = Sammlung(
        description="??? Fragebogen zu besonderen Themen: Flurnamen",
        alias="Flurn",
    )
    FREDERKING = Sammlung(
        description="Frederking, Ch., Plattdeutsches Dorfwörterbuch des Dorfes Hahlen bei Minden in Westfalen. Wortschatz, Spruchweisheit, Volkskunde.",
        alias="Frdk|Min Ha",
        kreis="Min",
        ort="Ha",
    )

    GARMANN = Sammlung(
        description="Garmann",
        kreis="Lin",
        ort="Be",
    )
    GESCHER = Sammlung(
        description="Pastor Eing (Gescher, Kr. Coesfeld, und Umgegend)",
        alias="Gescher",
        kreis="Kos",
        ort="Ge",
    )
    GESEKE = Sammlung(
        description="Geseke",
        alias="Geseke W.",
        kreis="Lst",
        ort="Ge",
    )
    GLAEN = Sammlung(
        description="Glaen, K., Das Bild des Menschen in der Sprache von Dahl.",
        alias="Glaen",
        kreis="Pad",
        ort="Da",
    )
    GLOCKE_HB = Sammlung(
        description="Heimatblätter der Glocke",
        alias="Heimatbl. d. Glocke",
    )
    GOEHNER = Sammlung(
        description="Lehrer A. Göhner (Gohfeld, Kr. Herford)",
        alias="Göhner",
        kreis="Hfd",
        ort="Go",
    )
    GRAFSCHAFTER = Sammlung(
        description="Grafschafter",
        alias="Grafschafter",
    )
    GREGORY = Sammlung(
        description="Gregory, O., Flächengrammatik des Gebietes von Plettenberg in Westfalen.",
        alias="Gregory",
        kreis="Alt",
        ort="Im",
    )
    GROENINGER = Sammlung(
        description="Gröninger",
        kreis="Mep",
        ort="Li",
    )
    GRIM = Sammlung(
        description="Grim",
        alias="Grim SB|Grim GT|Grim GW|Grim OH|...",
    )
    GRM = Sammlung(
        description="Germanisch-Romanische Monatsschrift.",
        alias="GRM",
    )
    GRUPE = Sammlung(
        description="Mittelschullehrer H. Grupe (Wellingen, Kr. Osnabrück)",
        alias="Wellingen Gr",
        kreis="Osn",
        ort="Wl",
    )

    HANSES = Sammlung(
        description="Anna Hanses",
        alias="Anna Hanses",
        kreis="Mes",
        ort="Eh",
    )
    HECKSCHER = Sammlung(
        description="Heckscher",
        alias="Heckscher",
    )
    HEIDE = Sammlung(
        description="Iserlohn Heide M.",
        alias="Jserl. Heide M.",
    )
    HEIERMEIER = Sammlung(
        description="Heiermeier, B., Die landwirtschaftlichen Fachausdrücke Westfalens auf Grund der Mundart des Kreises Wiedenbrück.",
        alias="Kr. Wiedenbr. Heierm.",
    )
    HERDEMANN = Sammlung(
        description="Herdemann, F., Versuch einer Lautlehre der westmünsterländischen Mundart.",
        alias="Borken Herdemann",
        kreis="Bor",
        ort="Bo",
    )
    HERKHOFF = Sammlung(
        description="Herkenhoff, H., Anhang von Wörtern, die sich nicht bei Woeste und Klöntrup finden.",
        alias="Osn Hg: Herk/Seg",
        kreis="Osn",
        ort="Hg",
    )
    HOLTHAUS = Sammlung(
        description="Holthaus, P. H., Materialien zu einer Schrift, betitelt: Süd-Westfälisches Wörterbuch",
        alias="Holthaus",
        kreis="Enr",
        ort="Hh",
    )
    HOLZSCHUH = Sammlung(
        description="Fragebogen zu besonderen Themen: Holzschuh",
        alias="Holzschuh",
    )
    HONCAMP = Sammlung(
        description="Honcamp, F. C., Sprichwörter und sprichwörtliche Redeformen des westfälischen Volkes",
        alias="Honc|Honc.-Anm.",
    )
    HUNOLD = Sammlung(
        description="Hunold, J. F., Mein Patterböarner Platt. Stalen van Reimels un Vertällekes in Spaß un Äerns.",
        alias="Paderborn Hunold",
    )
    HUNSCHE = Sammlung(
        description="F. E. Hunsche (Lienen, Kr. Tecklenburg)",
        alias="Hunsche",
        kreis="Tek",
        ort="Le",
    )
    HUNTEMANN = Sammlung(
        description="Huntemann, J., Die plattdeutschen Namen unserer Kulturgewächse und der wildwachsenden Pflanzenarten.",
        alias="Hunteman:Pflanzen",
    )

    ISERLOHN = Sammlung(
        description="Iserlohn (Friedrich Fust, Frau Ittermann, Frau Sophie Aldenheuer, Herr und Frau Asmus, Herr und Frau Holwe, Herr und Frau Dühr)",
        alias="Iserlohn|Isl Is",
        kreis="Isl",
        ort="Is",
    )

    JEURIK = Sammlung(
        description="Jeurik",
    )
    JOERM = Sammlung(
        description="Rhynern Joermann",
        alias="Rhy. Joer.",
        kreis="Unn",
        ort="Ry",
    )
    JOS_SCHN = Sammlung(
        description="Kirchveischede, Kr. Olpe, Jos. Schn.",
        kreis="Olp",
        ort="Kv",
    )
    JUNGEHUELSING = Sammlung(
        description="Salzbergen Jungehülsing",
        kreis="Lin",
        ort="Sb",
    )

    KAHMANN = Sammlung(
        description="Hs. Kahmann",  # Bbr We?
    )
    KARTELL = Sammlung(
        description="Kartell-Fragebogen",
        alias="Kartell",
    )
    KAUMANN_L = Sammlung(
        description="Kaumann, J., Entwurf einer Laut- und Flexionslehre der münsterischen Mundart in ihrem gegenwärtigen Zustande.",
        alias="Kaumann L",
        kreis="Mün",
        ort="Mü",
    )
    KAUMANN_N = Sammlung(
        description="Nachlass Kaumann",
        alias="Nachl. Kaumann",
        landschaft="Münsterl",
    )
    KIRCHHOFF = Sammlung(
        description="Wilhelm Kirchhoff, Lehmufer bei Hennen",
        alias="Kirchhoff",
        kreis="Isl",
        ort="Lu",
    )
    KK_WB = Sammlung(
        description="KkWb 1988",
    )
    KLEINN = Sammlung(
        description="Kleinn, Klementine, Volk und Sprache zwischen Egge und Weser.",
        alias="Kleinn",
        kreis="Höx",
    )
    KLOENTRUP = Sammlung(
        description="Rosemann, Johan Gilges, genannt Klöntrup, Niederdeutsch-Westphälisches Wörterbuch.",
        title="Klöntrup",
        kreis="Osn",
    )
    KOCH_BRACHT = Sammlung(
        description="Gastwirt Koch (Bracht, Kr. Meschede)",
        alias="Bracht K.",
        kreis="Mes",
        ort="Br",
    )
    KOCH_REISTE = Sammlung(
        description="Christine Koch (Reiste, Kr. Meschede)",
        alias="Chr. Koch",
        kreis="Mes",
        ort="Re",
    )
    KOEPPEN = Sammlung(
        description="Köppen, H., Verzeichniss der Idiotismen in plattdeutscher Mundart, volksthümlich in Dortmund und dessen Umgegend.",
        alias="Dortm./Köppen",
        kreis="Dor",
    )
    KRAUTBUND = Sammlung(
        description="Krautbund im Paderborner Gebiet",
        alias="Krautbund",
    )
    KRUMME = Sammlung(
        description="M. Krumme",
    )

    LEFERING = Sammlung(
        description="Lefering, Vreden",
        kreis="Ahs",
        ort="Vr",
    )
    LIP_OE = Sammlung(
        description="Lip Oe",
        alias="Lip Oe S|Lipp Oe",
    )
    LST_RUE = Sammlung(
        description="Lst Rü",
        kreis="Lst",
        ort="Rü",
    )
    LUEG = Sammlung(
        description="Wilhelm Lueg",
        kreis="Isl",
        ort="Lb",
    )
    LYRA = Sammlung(
        description="Lyra, F. W., Plattdeutsche Briefe, Erzählungen und Gedichte mit besonderer Rücksicht auf Sprichwörter und eigenthümliche Redensarten des Landvolks in Westphalen.",
        alias="Lyra",
        kreis="Osn",
        ort="Ly",
    )

    MASTHOLTE = Sammlung(
        description="Mastholt / Wie",
    )
    MEIER = Sammlung(
        description="Enger Meier",
        alias="Enger Meier",
        kreis="Hfd",
        ort="En",
    )
    METTINGEN = Sammlung(
        description="Mettingen, Kr. Tecklenburg (Fräulein Westrup)",
        alias="Mettingen W",
        kreis="Tek",
        ort="Me",
    )
    MEVENKAMP = Sammlung(
        description="Mevenkamp",
    )
    MEYER = Sammlung(
        description="Meyer, E. H. W., Ein Niedersächsisches Dorf am Ende des 19. Jahrhunderts. Eine volkskundliche Untersuchung.",
        alias="Meyer",
    )
    MINDEN_RA = Sammlung(
        description="Reg. Akten Minden 1905",
        alias="Reg. Akten Minden",
    )
    MISSGELD = Sammlung(
        description="Medizinalrat H. Mißgeld (Recklinghausen)",
        alias="Recklh. M",
        kreis="Rek",
        ort="Rh",
    )
    MOELLER = Sammlung(
        description="Lhs Sm Möller",
    )
    MUELLER_D = Sammlung(
        description="Müller, Westphälisches Idiotikon aus der Grafschaft Diepholz.",
        alias="Müller D",
        kreis="Die",
    )
    MUELLER_WS = Sammlung(
        description="Müller, K. A., Wörtersammlung von Niedersfeld, Kr. Brilon. 1963",
        alias="K.A.Müller",
        kreis="Bri",
        ort="Nf",
    )
    MUENSTER2 = Sammlung(
        description="Mün Mü 2",
        alias="Mün Mü 2",
    )
    MUESCHEDE = Sammlung(
        description="Müschede, Kr. Arnsberg (F. Wortmann)",
        alias="Müschede W.|ArnMü",
        kreis="Arn",
        ort="Mü",
    )

    NAMEN = Sammlung(
        description="Fragebogen zu besonderen Themen: Namen",
        alias="Namen",
    )
    NATELN = Sammlung(
        description="Nateln R",
        alias="Nateln R",
        kreis="Sos",
        ort="Na",
    )
    ND_KBL = Sammlung(
        description="Korrespondenzblatt des Vereins für niederdeutsche Sprachforschung.",
        alias="Nd. Kbl.|Korr.bl.",
    )
    NDS_WB = Sammlung(
        description="Niedersächsisches Wörterbuch. 1. Bd. hrsg. d. W. Jungandreas, Neumünster 1965; seit dem 2. Bd. hrsg. d. H. Wesche, Neumünster 1958 ff.",
        alias="NdsWb",
    )
    NOLTE = Sammlung(
        description="Nolte",
        alias="Nolte",
        kreis="Arn",
        ort="Hg",
    )
    NS = Sammlung(
        description="Ns",
        alias="Münsterl. Ns, X..., (Wagenfeld)",
    )
    NWA = Sammlung(
        description="Niederdeutscher Wortatlas",
        title="NWA",
    )

    OA = Sammlung(
        description="Ohne Angabe",
    )
    OEKE = Sammlung(
        description="Seminaroberlehrer W. Oeke (Neuenheerse, Kr. Warburg, und Paderborner Land)",
        alias="Oeke",
    )
    OEL = Sammlung(
        description="Lehrer J. Oel (Drewer, Kr. Lippstadt)",
        alias="Drewer Oel",
        kreis="Lst",
        ort="Dr",
    )
    OESEDE = Sammlung(
        description="Oesede",
        kreis="Osn",
        ort="Ös",
    )
    OESTRICH = Sammlung(
        description="Östrich L",
    )
    OLPE_HB = Sammlung(
        description="Heimatbl. d. Kr. Olpe",
    )
    OSN_HB = Sammlung(
        description="Osn Hb",
        kreis="Osn",
        ort="Hb",
    )
    OSTENDORF = Sammlung(
        description="Ostendorf, J., Den Wäwedamp. Ein Volksspiel in fünf Aufzügen.",
        alias="Ost Wä",
    )
    OSTERN = Sammlung(
        description="Fragebogen zu besonderen Themen: Ostern",
        alias="Ostern",
    )
    OTTENSMEIER = Sammlung(
        description="Lehrer H. Ottensmeyer (Bischofshagen, Kr. Herford)",
        alias="Bischofsh.",
        kreis="Hfd",
        ort="Bi",
    )

    PAGENDARM = Sammlung(
        description="Lehrer P. Pagendarm (Atteln und Grundsteinheim, Kr. Büren)",
        alias="Grundsteinheim-Pag.",
        kreis="Bür",
        ort="Gr",
    )
    PFLUG = Sammlung(
        description="Fragebogen zu besonderen Themen: Pflug",
        alias="Pflug",
    )
    PICKERT = Sammlung(
        description="Pickert, J., Vokalismus der Stammsilben in der Mundart von Dorsten i. Westf.",
        alias="Pickert",
        kreis="Rek",
        ort="Do",
    )
    PLATENAU_SP = Sammlung(
        description="Platenau, F., Alte Sprichwörter, Redensarten und Wetterregeln aus dem Lipperland.",
        alias="PlatenauSp",
    )
    PLATENAU_WB = Sammlung(
        description="Platenau Wörterbuch",
        alias="PlatenauWb",
    )
    POTT = Sammlung(
        description="G. Pott (Linden a. d. Ruhr)",
        alias="Linden",
        kreis="Enr",
        ort="Li",
    )

    RAHMEDE = Sammlung(
        description="Bankangestellter A. D. Rahmede (Amt Lüdenscheid)",
        alias="Rahmede",
        kreis="Alt",
        ort="Ls",
    )
    RAKERS = Sammlung(
        description="Dr. A. Rakers (Kr. Grafschaft Bentheim)",
        alias="Rakers| BenHi R",
        kreis="Ben",
    )
    RAKERS_GV = Sammlung(
        description="Rakers, A., Grafschafter Volksreime und Sprichwörter.",
        alias="Rakers GV",
    )
    RAKERS_MB = Sammlung(
        description="Rakers, A., Die Mundarten der alten Grafschaft Bentheim und ihrer reichsdeutschen und niederländischen Umgebung. Auf dialektgeographisch-geschichtlicher Grundlage.",
        alias="Rakers Maa",
    )
    RAKERS_KARTE = Sammlung(
        description="Rakers Karte",
        alias="Rakers Karte",
    )
    RATHERS = Sammlung(
        description="Rathert, H., Westfälische Brot- und Kuchennamen.",
        alias="Rathert",
    )
    RAUB_SP = Sammlung(
        description="Raub Sp",
        alias="Raub Sp",
    )
    RECKELS = Sammlung(
        description="Reckels, H., Volkskunde des Kreises Steinfurt.",
        alias="Reckels",
        kreis="Stf",
    )
    REGENITER = Sammlung(
        description="Regeniter",
        kreis="Enr",
    )
    REINKE = Sammlung(
        description="Reinke",
        kreis="Veh",
        ort="Ve",
    )
    REINKEN = Sammlung(
        description="Frau Lehrer Reinken 75 Jahr, Natrup-Hagen 1914-1925 ges.",
        kreis="Osn",
        ort="Nh",
    )
    REK_ER = Sammlung(
        description="Rek Er",
        kreis="Rek",
        ort="Er",
    )
    REURIK = Sammlung(
        description="Rektor H. Reurik (Hilten, Kr. Grafschaft Bentheim)",
        alias="Reurik|BenHi R",
        kreis="Ben",
        ort="Hi",
    )
    RHEINE = Sammlung(
        description="Rheine, Kr. Steinfurt (Gymnasialprofessor August Vollmer)",
        alias="Rheine V",
        kreis="Stf",
        ort="Rh",
    )
    RIXEN = Sammlung(
        description="Rixen Wr.",
        alias="Rixen Wr.",
        kreis="Bri",
        ort="Ri",
    )
    ROTE_ERDE = Sammlung(
        description="Heimatblätter der Roten Erde. Monatshefte, hrsg. f. d. Westfälischen Heimatbund v. F. Castelle u. K. Wagenfeld.",
        alias="Rote Erde",
    )
    ROTTMANN = Sammlung(
        description="Rottmann",
        alias="Rottmann",
        kreis="Rek",
        ort="Kh",
    )

    SAETZE = Sammlung(
        description="Sätze wie 'Er will mir kein Geld geben'.",
    )
    SANDEBECK = Sammlung(
        description="Sandebeck, Kr. Höxter (stud. phil. Georg Müller und seine Mutter)",
        alias="Sandebeck",
        kreis="Höx",
        ort="Sb",
    )
    SCHEPERS = Sammlung(
        description="Schepers, J., Westfalen-Lippe.",
        alias="Schepers",
    )
    SCHLEEF = Sammlung(
        description="???Schleef, W., Dortmunder Wörterbuch.",
        alias="Dor SL",
        kreis="Dor",
    )
    SCHLUETER = Sammlung(
        description="Schlüter, J., Die niederländischen Wörter in der westmünsterländischen Mundart.",
        alias="Schlüter",
    )
    SCHMIEDE = Sammlung(
        description="Fragebogen zu besonderen Themen: Schmiede",
        alias="Schmiede",
    )
    SCHMITZ = Sammlung(
        description="Studienrat B. Schmitz (Altenrheine, Kr. Steinfurt)",
        alias="Schmitz",
        kreis="Stf",
        ort="Ar",
    )
    SCHOENHOFF = Sammlung(
        description="Schönhoff, H., Emsländische Grammatik. Laut- und Formenlehre der emsländischen Mundarten.",
        alias="Schönhoff",
        kreis="Emsl",
    )
    SCHOENING = Sammlung(
        description="Bankbeamter H. Schöning (Brockhagen, Kr. Halle)",
        alias="Schöning",
        kreis="Hal",
        ort="Bh",
    )
    SCHONEWEG_L = Sammlung(
        description="Schoneweg, E., Das Leinengewerbe in der Grafschaft Ravensberg. Ein Beitrag zur niederdeutschen Volks- und Altertumskunde.",
        alias="Schoneweg Leinengewerbe",
    )
    SCHOPPE_MSKR = Sammlung(
        description="Schoppe, J., Die Mundart von Röckinghausen bei Wiedenbrück.",
        alias="Röckinghausen/Wie Schoppe Mskr.",
        kreis="Wie",
        ort="Rö",
    )
    SCHOPPE = Sammlung(
        description="Oberstudienrat i. R. Dr. J. Schoppe (Röckinghausen, Kr. Wiedenbrück)",
        alias="Schoppe",
        kreis="Wie",
        ort="Rö",
    )
    SCHROEDER = Sammlung(
        description="W. Schröder",
        alias="W. Schröder",
        kreis="Ahs",
        ort="St",
    )
    SCHWAGMEYER = Sammlung(
        description="Schwagmeyer, F., Der Lautstand der Ravensbergischen Mundart von Hiddenhausen.",
        alias="Hiddenh. Schwagm.",
        kreis="Hfd",
        ort="Hi",
    )
    SEEWALD = Sammlung(
        description="Franz Seewald sen., Legden, Kreis Ahaus",
    )
    SOESTER_BOERDE_WB = Sammlung(
        description="Schmoeckel, H., u. A. Blesken, Wörterbuch der Soester Börde, ein Beitrag zur westfälischen Mundartenforschung. Soest 1952",
        alias="Wb. Soester Börde",
        kreis="Sos",
    )
    SOS_BR = Sammlung(
        description="Sos Br",
        kreis="Sos",
        ort="Br",
    )
    STF_KA = Sammlung(
        description="Stf Ka",
        alias="Stf Ka",
        kreis="Stf",
        ort="Ka",
    )
    STOLTE_BHF = Sammlung(
        description="Stolte, H., Bauernhof und Mundart in Ravensberg. Beiträge zur niederdeutschen Volkskunde.",
        alias="Stolte Bauernhof",
        kreis="Hal",
        ort="Bh",
    )
    STRODTMANN = Sammlung(
        description="Strodtmann, J. Ch., Idioticon Osnabrugense.",
        alias="Strodtmann",
    )
    SUELHOP = Sammlung(
        description="Fritz Sülhop",
        kreis="Lst",
        ort="Me",
    )
    SUTTMEYER = Sammlung(
        description="J. Suttmeyer",
        alias="Suttmeyer",
        kreis="Osn",
        ort="Kl",
    )

    TEK_RB = Sammlung(
        description="Tek Rb",
        alias="Tek Rb",
        kreis="Tek",
        ort="Rb",
    )

    UNN_AF = Sammlung(
        description="Unna Afferde",
        alias="Unn Af",
        kreis="Unn",
        ort="Af",
    )

    VEHSLAGE = Sammlung(
        description="Vehslage, H., Die Mundart des Artlandes auf der Grundlage der Mundart des Kirchspiels Badbergen. Borna-Leipzig 1908 (Phil. Diss. Münster 1908)",
        alias="Badbergen Vehslage",
        kreis="Bbr",
        ort="Bb",
    )
    VKL_ARCH = Sammlung(
        description="Vkl. Arch.",
        alias="Vkl. Arch.",
    )
    VOLKSK_ATL = Sammlung(
        description="Volksk. Atl.",
    )
    VORHELM = Sammlung(
        description="Vorhelm, Kr. Beckum (Pastor Dr. Augustin Wibbelt et al.)",
        alias="Vorhelm",
        kreis="Bek",
        ort="Vh",
    )
    WAGENFELD = Sammlung(
        description="Wagenfeld, K., Volksmund. Plattdeutsche Sprichwörter und Redensarten des Münsterlandes in ihrer Anwendung.",
        alias="Wagenfeld Volksmund",
        landschaft="Münsterl",
    )
    WAGENTEIL = Sammlung(
        description="??? Fragebogen zu besonderen Themen: Wagenteil",
        alias="Wagenteil",
    )
    WAL_BH = Sammlung(
        description="Wal/Bh",
        alias="Wal/Bh|Wal Bh",
        kreis="Wal",
        ort="Bh",
    )
    WAL_RO = Sammlung(
        description="WalRo",
        alias="WalRo",
        kreis="Wal",
        ort="Ro",
    )
    WALTER = Sammlung(
        description="Walter",  # Kreis: Tek, Ort: Hp ?
    )
    WALTER_NL = Sammlung(
        description="Walter, F., Nachlass",
        alias="Walter Nachlaß",
    )
    WALTER_SP = Sammlung(
        description="Walter, F., Plattdeutsche Sprichwörter und sprichwörtliche Redensarten aus der Stadt Recklinghausen.",
        alias="Walter Sprichw.",
        kreis="Rek",
        ort="Rh",
    )
    WARNING = Sammlung(
        description="Studienrat Dr. W. Warning (Versmold, Kr. Halle)",
        alias="Loxten Warning",
        kreis="Hal",
        ort="Lo",
    )
    WEDDIGEN = Sammlung(
        description="Ravensberg Weddigen (Buch)",
        alias="Weddigen|Weddingen",
        kreis="Hal",
        ort="Ra",
    )
    WEIL_WB = Sammlung(
        description="WeilWB 1983",
        alias="WeilWB",
        kreis="Sth",
        ort="St",
    )
    WELLINGEN = Sammlung(
        description="Wellingen Gr",
    )
    WELLMANN = Sammlung(
        description="Wellmann, H., Die Bauerschaft Mehringen a. d. Ems und Umgegend des Kirchspiels Emsbüren im Kreise Lingen (Ems). Ein Beitrag zur Heimatkunde.",
        alias="Wellmann",
        kreis="Lin",
        ort="Mr",
    )
    WESSUM = Sammlung(
        description="Wessum, Kr. Ahaus (Geheimrat Grimmelt)",
        alias="WessumGr.",
        kreis="Ahs",
        ort="We",
    )
    WESTF_SP_ARCHIV = Sammlung(
        description="Westfälisches Sprichwörterarchiv",
        alias="Westf. Sprichwörterarchiv|Westf.Sprichwörter-Archiv|WESTF.SPRICHWORTARCHIV",
    )
    WESTF_VOLKSK = Sammlung(
        description="Archiv für westfälische Volkskunde",
        alias="Archiv für westfälische Volkskunde",
    )
    WESTPH_MAG = Sammlung(
        description="Westphälisches Magazin zur Geographie, Historie und Statistik",
        alias="Westph. Mag. H",
    )
    WIX = Sammlung(
        description="Gütersloh Wix",
        alias="Gütersloh Wix",
        kreis="Wie",
        ort="Gü",
    )
    WM_WB = Sammlung(
        description="Westmünsterländisches Wörterbuch",
        alias="WmWb; Elling/Piirainen",
    )
    WML_BB = Sammlung(
        description="W-münsterl. BüldB",
    )
    WOESTE_GM = Sammlung(
        description="Woeste, J. F. L., Volksüberlieferungen in der Grafschaft Mark nebst einem Glossar.",
        alias="WoeGM",
    )
    WOESTE_NL = Sammlung(
        description="Woeste Nachlass",
        alias="Woeste N",
    )
    WOESTE_WB = Sammlung(
        description="Woeste, F. (J. F. L.), Wörterbuch der westfälischen Mundart. Neu bearb. u. hrsg. v. E. Nörrenberg.",
        alias="Woeste Wb.",
    )
