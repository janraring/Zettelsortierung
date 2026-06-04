from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True, slots=True)
class Sammlung:
    trace: str | None = None
    groups: str | None = None

    sigle: str | None = None  # Nur für Auszüge aus Werken
    description: str | None = None

    landschaft: str | None = None
    kreis: str | None = None
    ort: str | None = None


class Sammlungen(Enum):
    ##############################################################
    # Meta
    ##############################################################
    SKIPPED = Sammlung(
        description="Vorerst übersprungene Zettel",
    )
    VERWEIS = Sammlung(
        description="Verweis",
    )
    OA = Sammlung(
        description="Ohne Angabe",
    )
    BLANK = Sammlung(
        description="Vorderseite blank",
    )
    PHONEM = Sammlung(
        description="Phonematische Notizen",
    )
    VERKEHRT = Sammlung(
        description="Recto/Verso vertauscht",
    )

    ##############################################################
    # Fragebogen
    ##############################################################
    ANREDE = Sammlung(
        trace="Anredeformen",
        groups="Fragebogen|Anredeformen",
        description="Anredeformen (1967) 58",
    )
    ATLAS_FRGB = Sammlung(
        trace="Atlas-Frgb.",
        groups="Fragebogen|Atlas",
    )
    BAADER_FB = Sammlung(
        trace="Baader",
        groups="Fragebogen|Baader",
        description="6 Fragebogen von Prof. Dr. Baader (insgesamt 670 Fragen); verschickt 1922 bis 1926; 263 Antworten, davon 250 zu Fragebogen I (erstes Material für ein „Westfälisches Wörterbuch“; vgl. S. 10); aus dem Nachlaß Prof. Dr. Baaders: 1 Fragebogen aus dem Reg.-Bezirk Osnabrück (1948/49)",
    )
    BIENENZUCHT = Sammlung(
        trace="Bienenzucht",
        groups="Fragebogen|Bienenzucht",
        description="Fragebogen zu besonderen Themen: Bienenzucht (1942) 27",
    )
    ESSEN_TRINKEN = Sammlung(
        trace="Essen u. Trinken",
        groups="Fragebogen|EssenTrinken",
    )
    FRAGEBOGEN = Sammlung(
        trace="Fragebogen",
        groups="Fragebogen|Allgemein",
    )
    HIAT = Sammlung(
        trace="Hiatfrbg",
        groups="Fragebogen|Hiatfragebogen",
    )
    HOLZSCHUH = Sammlung(
        trace="Holzschuh",
        groups="Fragebogen|Holzschuh",
        description="Fragebogen zu besonderen Themen: Holzschuhmacherei (1942) 14",
    )
    KARTELL = Sammlung(
        trace="Kartell",
        groups="Fragebogen|Kartell",
        description="2 Fragebogen des Wörterbuchkartells in Marburg",
    )
    KARTENSPIEL = Sammlung(
        trace="Kartenspiel",
        groups="Fragebogen|Kartenspiel",
        description="Anredeformen (1967) 58",
    )
    NAMEN = Sammlung(
        trace="Frageb.: Namen",
        groups="Fragebogen|Namen",
    )
    NWA = Sammlung(
        trace="NWA",
        groups="Fragebogen|NWA",
        description="2 Fragebogen zu dem von Prof. Dr. Foerste begonnenen Niederdeutschen Wortatlas, soweit die Antworten aus dem Raum des Westfälischen Wörterbuches stammen (2662 Antworten)",
    )
    OSTERN = Sammlung(
        trace="Ostern",
        groups="Fragebogen|Ostern",
        description="Fragebogen zu besonderen Themen: Bezeichnungen für Ostern und dazugehörige Wörter (ca. 1938) 318",
    )
    PFLUG = Sammlung(
        trace="Frageb. „Pflug“",
        groups="Fragebogen|Pflug",
    )
    RHEIN_FRGB = Sammlung(
        trace="Rhein.-Frgb.",
        groups="Fragebogen|RheinFrgb",
    )
    ROGGENBROT = Sammlung(
        trace="Roggenbrot",
        groups="Fragebogen|Roggenbrot",
    )
    SCHMIEDE = Sammlung(
        trace="Schmiede",
        groups="Fragebogen|Schmiede",
        description="Fragebogen zu besonderen Themen: Schmiede (1942) 14",
    )
    SPINNEN = Sammlung(
        trace="Frageb. Spinnen",
        groups="Fragebogen|Spinnen",
        description="spinnen (1942) 24",
    )
    TONBAND = Sammlung(
        trace="Tonband",
    )
    # VERBEN = Sammlung(
    #     trace="",
    #     groups="Fragebogen|Verben",
    #     description="starke Verben (ca. 1936) 20",
    # )

    ##############################################################
    # Sammlungen
    ##############################################################
    ARCH_RKLH = Sammlung(
        trace="Kr.-Arch. Rklh.",
        groups="Sammlungen|Kreisarchiv Rrecklinghausen",
    )
    BO_LAER = Sammlung(
        trace="Bochum - Laer",
        groups="Sammlungen|Bochum Laer",
        kreis="Bch",
        ort="Lr",
    )
    GRAFSCHAFTER = Sammlung(
        trace="Grafschafter",
        groups="Sammlungen|Grafschafter",
        kreis="Ben",
    )
    HECKSCHER = Sammlung(
        trace="Heckscher",
        groups="Sammlungen|Heckscher",
    )
    RAKERS_KARTE = Sammlung(
        trace="Rakers Karte",
        groups="Sammlung|RakersKarte",
    )
    REG_AKT_MIND = Sammlung(
        trace="Reg. Akten Minden",
        groups="Sammlungen|RegAktMind",
    )
    SAETZE = Sammlung(
        trace="Er will mir kein Geld geben|...",
        description="Sätze wie 'Er will mir kein Geld geben'.",
    )
    WAGENTEIL = Sammlung(
        trace="Wagenteil",
        groups="Sammlungen|Wagenteil",
    )
    WESTF_SP_ARCHIV = Sammlung(
        trace="Westf. Sprichwörterarchiv|Westf.Sprichwörter-Archiv|WESTF.SPRICHWORTARCHIV",
        groups="Sammlungen|WestfSprichwArchiv",
    )
    WESTF_VOLKSK = Sammlung(  # möglicherweise identisch mit VKL_ARCH
        trace="Archiv für westfälische Volkskunde",
        groups="Sammlungen|WestfVolkskArchiv",
    )

    BAADER_NL = Sammlung(
        trace="Baader Nachlass",
        groups="Nachlässe|Baader",
    )
    KAUMANN_NL = Sammlung(
        trace="Nachl. Kaumann",
        groups="Nachlässe|Kaumann",
        description="Kaumann Nachlass",
        landschaft="Münsterl",
    )
    WALTER_NL = Sammlung(
        trace="Walter Nachlaß",
        groups="Nachlässe|Walter",
    )
    WOESTE_NL = Sammlung(
        trace="WoeNl",
        groups="Nachlässe|Woeste",
    )

    ##############################################################
    # Lautschrift
    ##############################################################
    AFFERDE = Sammlung(
        trace="Afferde E|Unn Af",
        groups="Lautschrift|Afferde|Kopie",
        description="Afferde, Kr. Unna (August Ebbinghaus)",
        kreis="Unn",
        ort="Af",
    )
    ALTENA = Sammlung(
        trace="Altena|Alt Al",
        groups="Lautschrift|Altena",
        description="Altena (Frau Karoline Krummenerl, * 1847, Fritz Künne, Fräulein Mina Künne, Frau Mina Vedder)",
        kreis="Alt",
        ort="Al",
    )
    ASSINGHAUSEN = Sammlung(
        trace="Bri Ah",
        groups="Lautschrift|Assinghausen",
        description="Assinghausen, Kr. Brilon (Frau Knoche)",
        kreis="Bri",
        ort="Ah",
    )
    BAECKEREI = Sammlung(
        trace="Bäckerei|Schwelm",
        groups="Lautschrift|Bäckerei",
        kreis="Enr",
        ort="Sw",
    )
    BANDWIRK = Sammlung(
        trace="Bandwirk.|Gegend Schwelm",
        groups="Lautschrift|Bandwirk",
        kreis="Enr",
        ort="Sw",
    )
    BARLO = Sammlung(
        trace="Bor Ba",
        groups="Lautschrift|Barlo",
        description="Barlo, Kr. Borken (Bauer Brake)",
        kreis="Bor",
        ort="Ba",
    )
    BROCKHAUSEN = Sammlung(
        trace="Brockhsn./Sos.|Sos Br",
        groups="Lautschrift|Brockhausen",
        kreis="Sos",
        ort="Br",
    )
    DEILINGHOFEN = Sammlung(
        trace="Deilingh.|Isl Dh|Jsl Dh",
        groups="Lautschrift|Deilinghofen",
        description="Deilinghofen, Kr. Iserlohn (Frau Alwine Kötter, August Kötter, Melchior Dietrich Tümena, Karl Tümena, Frau Mariechen Tümena)",
        kreis="Isl",
        ort="Dh",
    )
    DIEPENAU = Sammlung(
        trace="Diepenau-Nie",
        groups="Lautschrift|Diepenau",
        kreis="Nie",
        ort="Di",
    )
    DRENSTEINFURT = Sammlung(
        trace="Drenst. Wa",
        groups="Lautschrift|Drensteinfurt",
        description="Drensteinfurt, Kr. Lüdinghausen (Karl Wagenfeld)",
        kreis="Lhs",
        ort="Dr",
    )
    ELSEY = Sammlung(
        trace="Elsey|Isl El",
        groups="Lautschrift|Elsey",
        description="Elsey, Kr. Iserlohn (Oberregierungsrat Ernst Braß, Frau Elfriede Braß, Frau Wilhelmine Braß, Dr. med. Karl Heidsieck, Wilhelm Heidsieck, Fräulein Elisabeth Heidsieck, Fräulein Marie Heidsieck, Frau Schöneberg, Frau Voß)",
        kreis="Isl",
        ort="El",
    )
    ENDORF = Sammlung(
        trace="Endorf R",
        groups="Lautschrift|Endorf",
        description="Endorf, Kr. Arnsberg (stud. phil. Maria Rörig)",
        kreis="Arn",
        ort="En",
    )
    ERLE = Sammlung(
        trace="Rek Er",
        groups="Lautschrift|Erle",
        kreis="Rek",
        ort="Er",
    )
    FLURNAMEN = Sammlung(
        trace="Flurn",
    )
    GEMENKRUECKLING = Sammlung(
        trace="Bor Kr",
        groups="Lautschrift|Gemenkrückling",
        kreis="Bor",
        ort="Kr",
    )
    GESCHER = Sammlung(
        trace="Gescher|Kos Ge",
        groups="Lautschrift|Gescher",
        description="Pastor Eing (Gescher, Kr. Coesfeld, und Umgegend)",
        kreis="Kos",
        ort="Ge",
    )
    GRONAU = Sammlung(
        trace="Ahs Gr|Bremmers",
        groups="Lautschrift|Gronau",
        description="Bremmers",
        kreis="Ahs",
        ort="Gr",
    )
    ISERLOHN = Sammlung(
        trace="Iserlohn|Isl Is|Jsl Js",
        groups="Lautschrift|Iserlohn",
        description="Iserlohn (Friedrich Fust, Frau Ittermann, Frau Sophie Aldenheuer, Herr und Frau Asmus, Herr und Frau Holwe, Herr und Frau Dühr)",
        kreis="Isl",
        ort="Is",
    )
    LIENEN = Sammlung(
        trace="Tek Li",
        groups="Lautschrift|Lienen",
        kreis="Tek",
        ort="Li",
    )
    LAUTSCHRIFT_SONST = Sammlung(
        trace="e1/ü1/etc",
        groups="Lautschrift|Sonstige",
    )
    LIESBORN = Sammlung(
        trace="Bek Lb",
        groups="Lautschrift|Liesborn",
        kreis="Bek",
        ort="Lb",
    )
    LUECHTRINGEN = Sammlung(
        trace="Lüchtr.",
        groups="Lautschrift|Lüchtringen",
        kreis="Höx",
        ort="Lü",
    )
    METTINGEN = Sammlung(
        trace="Mettingen W",
        groups="Lautschrift|Mettingen",
        description="Mettingen, Kr. Tecklenburg (Fräulein Westrup)",
        kreis="Tek",
        ort="Me",
    )
    MUENSTER2 = Sammlung(
        trace="Mün Mü 2",
        groups="Lautschrift|Münster",
        description="Mün Mü 2",
        kreis="Mün",
        ort="Mü",
    )
    MUESCHEDE = Sammlung(
        trace="Müschede W.|ArnMü",
        groups="Lautschrift|Müschede",
        description="Müschede, Kr. Arnsberg (F. Wortmann)",
        kreis="Arn",
        ort="Mü",
    )
    NATELN = Sammlung(
        trace="Nateln R",
        groups="Lautschrift|Nateln",
        kreis="Sos",
        ort="Na",
    )
    RHEINE = Sammlung(
        trace="Theine V",
        groups="Lautschrift|Rheine",
        description="Rheine, Kr. Steinfurt (Gymnasialprofessor August Vollmer)",
        kreis="Stf",
        ort="Rh",
    )
    RIESENBECK = Sammlung(
        trace="Tek Rb",
        groups="Lautschrift|Riesenbeck",
        kreis="Tek",
        ort="Rb",
    )
    RIXEN = Sammlung(
        trace="Rixen Wr.",
        groups="Lautschrift|Rixen",
        kreis="Bri",
        ort="Ri",
    )
    SANDEBECK = Sammlung(
        trace="Sandebeck M.",
        groups="Lautschrift|Sandebeck",
        description="Sandebeck, Kr. Höxter (stud. phil. Georg Müller und seine Mutter)",
        kreis="Höx",
        ort="Sb",
    )
    VORHELM = Sammlung(
        trace="Vorhelm|Bek Vh",
        groups="Lautschrift|Vorhelm",
        description="Vorhelm, Kr. Beckum (Pastor Dr. Augustin Wibbelt et al.)",
        kreis="Bek",
        ort="Vh",
    )
    WARSTEIN = Sammlung(
        trace="Warstein E.",
        groups="Lautschrift|Warstein",
        description="Postsekretär Enste (Warstein, Kr. Arnsberg)",
        kreis="Arn",
        ort="Wa",
    )
    WESSUM = Sammlung(
        trace="Wessum Gr",
        groups="Lautschrift|Wessum",
        description="Wessum, Kr. Ahaus (Geheimrat Grimmelt)",
        kreis="Ahs",
        ort="We",
    )
    WULFTEN = Sammlung(
        trace="BbrWu",
        groups="Lautschrift|Wulften",
        kreis="Bbr",
        ort="Wu",
    )
    X = Sammlung(
        trace="///",
        groups="Lautschrift|X",
    )

    ##############################################################
    # Wortschatz
    ##############################################################
    AHLING_BBR = Sammlung(
        trace="Artland|Ahling|H. A.",
        groups="Wortschatz|Ahling",
        kreis="Bbr",
    )
    AHLING_BBR_NO = Sammlung(
        trace="Nortrup u. Umg.|Ahling|H. A.",
        groups="Wortschatz|Ahling|Bbr No",
        kreis="Bbr",
        ort="No",
    )
    AHLING_BBR_SU = Sammlung(
        trace="Suttrup Kr. Bersbr.|Ahling|H. A.",
        groups="Wortschatz|Ahling|Bbr Su",
        kreis="Bbr",
        ort="Su",
    )
    ARING = Sammlung(
        trace="Bch He|Aring",
        groups="Wortschatz|Aring",
        kreis="Bch",
        ort="He",
    )
    ARNDTS = Sammlung(
        trace="Plettenberg Oesterau|Sammlung Arndts",
        groups="Wortschatz|Arndts",
        kreis="Alt",
        ort="Pl",
    )
    BALKENHOLL_HM = Sammlung(
        trace="Sammlung Balkenholl",
        groups="Wortschatz|Balkenholl|Unn Hm",
        kreis="Unn",
        ort="Hm",
    )
    BALKENHOLL_UN = Sammlung(
        trace="Sammlung Balkenholl",
        groups="Wortschatz|Balkenholl|Unn Un",
        kreis="Unn",
        ort="Un",
    )
    BECKMANN = Sammlung(
        trace="Beckmann",
        groups="Wortschatz|Beckmann",
        kreis="Bch",
        ort="Ld",
    )
    BEESTERMOELLER = Sammlung(
        trace="Beesten|Dr. Bm",
        groups="Wortschatz|Beestermöller",
        description="Studienassessor Dr. A. Beestermöller (Beesten, Kr. Lingen)",
        kreis="Lin",
        ort="Be",
    )
    BLESKEN = Sammlung(
        trace="A. H. Blesen|Rektor|Hagen-Vorhalle",
        groups="Wortschatz|Blesken",
        description="Rektor A. Blesken (Ampen, Kr. Soest)",
        kreis="Sos",
        ort="Am",
    )
    BLESKEN_SP = Sammlung(
        trace="Blesken:Sprichwörter",
        groups="Wortschatz|Blesken|Sprichwörter",
        description="Rektor A. Blesken (Ampen, Kr. Soest)",
        kreis="Sos",
    )
    BOEHMER = Sammlung(
        trace="Schwelm B.",
        groups="Wortschatz|Böhmer",
        description="Dr. E. Böhmer (Schwelm)",
        kreis="Enr",
        ort="Sw",
    )
    BOLTE = Sammlung(
        trace="Bolte|Osnabrück-Schinkel",
        groups="Wortschatz|Bolte",
        kreis="Osn",
        ort="Sh",
    )
    BRENNINGMEIER = Sammlung(
        trace="Hof Brenningmeier|Mettingen",
        groups="Wortschatz|Brenningmeier",
        kreis="Tek",
        ort="Me",
    )
    BRINKERS = Sammlung(
        trace="Chr. Brinkers",
        groups="Wortschatz|Brinkers",
        kreis="Ben",
        ort="Wt",
    )
    BULDT = Sammlung(
        trace="Asd Ad|Buldt|Aschend.-Ems",
        groups="Wortschatz|Buldt",
        kreis="Asd",
        ort="Ad",
    )
    BULMAHN = Sammlung(
        trace="H. Bulmahn|Ilvese|Jlvese|Kr. Minden i.W.",
        groups="Wortschatz|Bulmahn",
        kreis="Min",
        ort="Il",
    )
    CRAMER = Sammlung(
        trace="Cramer|Niedersfeld",
        groups="Wortschatz|Cramer",
        description="Mittelschulrektor H. Cramer (Niedersfeld, Kr. Brilon)",
        kreis="Bri",
        ort="Nf",
    )
    DITTMAR = Sammlung(
        trace="Dittmar|Königsteele",
        groups="Wortschatz|Dittmar",
        description="Pastor Dittmar (Königssteele b. Essen)",
        kreis="Ess",
        ort="Ks",
    )
    ECKARDT = Sammlung(
        trace="Dor Wl",
        groups="Wortschatz|Eckardt",
        description="Schlachthofdirektor Dr. Eckardt (Wellinghofen b. Dortmund)",
        kreis="Dor",
        ort="Wl",
    )
    EGGERS = Sammlung(
        trace="Eggers|Borken i.W.",
        groups="Wortschatz|Eggers",
        description="Adolf Eggers Borken",
        kreis="Bor",
        ort="Bo",
    )
    EICKUM_B = Sammlung(
        trace="Eickum B.",
        groups="Wortschatz|Eickum",
        description="B.",
        kreis="Hfd",
        ort="Ei",
    )
    FREDERKING = Sammlung(
        trace="Frdk|Min Ha",
        groups="Wortschatz|Frederking",
        description="Frederking, Ch., Plattdeutsches Dorfwörterbuch des Dorfes Hahlen bei Minden in Westfalen. Wortschatz, Spruchweisheit, Volkskunde.",
        kreis="Min",
        ort="Ha",
    )
    GARMANN = Sammlung(
        trace="Garmann",
        groups="Wortschatz|Garmann",
        description="Garmann",
        kreis="Lin",
        ort="Be",
    )
    GESEKE_W = Sammlung(
        trace="Geseke",
        groups="Wortschatz|Geseke",
        description="W.",
        kreis="Lst",
        ort="Ge",
    )
    GOEHNER = Sammlung(
        trace="Göhner",
        groups="Wortschatz|Göhner",
        description="Lehrer A. Göhner (Gohfeld, Kr. Herford)",
        kreis="Hfd",
        ort="Go",
    )
    HALINGEN_C = Sammlung(
        trace="Halingen C.",
        groups="Wortschatz|HalingenC",
        kreis="Isl",
        ort="Ha",
    )
    HANFLAND = Sammlung(
        trace="Assinghausen Kreis Brilon|Agatha Hanfland",
        groups="Wortschatz|Hanfland",
        description="Agatha Hanfland",
        kreis="Bri",
        ort="Ah",
    )
    HANSES = Sammlung(
        trace="Anna Hanses",
        groups="Wortschatz|Hanses",
        description="Anna Hanses",
        kreis="Mes",
        ort="Eh",
    )
    HEIDE_M = Sammlung(
        trace="Jserl. Heide M.",
        groups="Wortschatz|Iserlohnerheide",
        description="Iserlohner Heide M.",
        kreis="Isl",
        ort="Hd",
    )
    HEIDENOLDENDORF = Sammlung(
        trace="Heidenoldendorf",
        groups="Wortschatz|Heidenoldendorf",
        kreis="Det",
        ort="Hd",
    )
    HESEMANN = Sammlung(
        trace="Hesemann",
        groups="Wortschatz|Hesemann",
        landschaft="Ravensbg",
    )
    HILTRUP_W = Sammlung(
        trace="Hiltrup W",
        groups="Wortschatz|HiltrupW",
        kreis="Mün",
        ort="Hi",
    )
    HOEMKEN = Sammlung(
        trace="Asd Vr=Hö",
        groups="Wortschatz|Hömken|Asd Vr",
        kreis="Asd",
        ort="Vr",
    )
    JOERMANN = Sammlung(
        trace="Rhy. Joer.",
        groups="Wortschatz|Joermann",
        kreis="Unn",
        ort="Ry",
    )
    JUNGEHUELSING = Sammlung(
        trace="Salzbergen|Jungehülsing",
        groups="Wortschatz|Jungehülsing",
        description="Studienrat Dr. G. Jungehülsing (Salzbergen, Kr. Lingen); Studienassessor Dr. A. Beestermöller (Beesten, Kr. Lingen)",
        kreis="Lin",
        ort="Sb",
    )
    KAULINGFRECKS = Sammlung(
        trace="Kaulingfrecks|Wettringen",
        groups="Wortschatz|Kaulingfrecks",
        kreis="Stf",
        ort="Wt",
    )
    KIRCHHOFF = Sammlung(
        trace="Wilhelm Kirchhoff|Lehmufer b. Hennen",
        groups="Wortschatz|Kirchhoff",
        kreis="Isl",
        ort="Lu",
    )
    KORTMANN = Sammlung(
        trace="Büderich F. K.|F. Kortmann",
        groups="Wortschatz|Kortmann",
        kreis="Sos",
        ort="Bü",
    )
    SCHN = Sammlung(
        trace="Kirchv. Kr. Olpe|Jos. Schn.",
        groups="Wortschatz|Schn",
        kreis="Olp",
        ort="Kv",
    )
    SCHULTE = Sammlung(
        trace="C Schulte|Lst Ag",
        groups="Wortschatz|Schulte",
        kreis="Lst",
        ort="Ag",
    )
    KOCH_BRACHT = Sammlung(
        trace="Bracht K.",
        groups="Wortschatz|KochBracht",
        description="Gastwirt Koch (Bracht, Kr. Meschede)",
        kreis="Mes",
        ort="Br",
    )
    KOCH_REISTE = Sammlung(
        trace="Chr. Koch",
        groups="Wortschatz|KochReiste",
        description="Christine Koch (Reiste, Kr. Meschede)",
        kreis="Mes",
        ort="Re",
    )
    LUEG = Sammlung(
        trace="Wilhelm Lueg",
        groups="Wortschatz|Lueg",
        kreis="Isl",
        ort="Lb",
    )
    MEVENKAMP = Sammlung(
        trace="Catenhorn|Mevenkamp",
        groups="Wortschatz|Mevenkamp",
        description="Heinrich Mevenkamp",
        kreis="Stf",
        ort="Ka",
    )
    MISSGELD = Sammlung(
        trace="Recklh. M",
        groups="Wortschatz|Misgeld",
        description="Medizinalrat H. Mißgeld (Recklinghausen)",
        kreis="Rek",
        ort="Rh",
    )
    MOENIG = Sammlung(
        trace="Moenig",
        groups="Wortschatz|Moenig",
    )
    NOLDE = Sammlung(
        trace="Dorsten Kr. Recklinghausen|Joh. Nolde",
        groups="Wortschatz|Nolde",
        kreis="Rek",
        ort="Do",
    )
    NOLTE = Sammlung(
        trace="Arn Nolte",
        groups="Wortschatz|Nolte",
        kreis="Arn",
        ort="Hg",
    )
    OEKE = Sammlung(
        trace="W. Oeke",
        groups="Wortschatz|Oeke",
        description="Seminaroberlehrer W. Oeke (Neuenheerse, Kr. Warburg, und Paderborner Land)",
    )
    OEL = Sammlung(
        trace="Drewer Oel|Lst Dr",
        groups="Wortschatz|Oeke",
        description="Lehrer J. Oel (Drewer, Kr. Lippstadt)",
        kreis="Lst",
        ort="Dr",
    )
    OESTRICH_L = Sammlung(
        trace="Östrich L",
        groups="Wortschatz|ÖstrichL",
        kreis="Isl",
        ort="Ös",
    )
    OTTENJANN = Sammlung(
        trace="Ottenjann",
        groups="Wortschatz|Ottenjann",
        description="Dr. H. Ottenjann, der Gründer und Leiter des Museumsdorfes in Cloppenburg",
    )
    OTTENSMEIER = Sammlung(
        trace="Heinrich Ottensmeyer|Bischofsh. Ott.",
        groups="Wortschatz|Ottensmeyer",
        description="Lehrer H. Ottensmeyer (Bischofshagen, Kr. Herford)",
        kreis="Hfd",
        ort="Bi",
    )
    PAGENDARM = Sammlung(
        trace="Grundsteinheim-Pag.",
        groups="Wortschatz|Pagendarm",
        description="Lehrer P. Pagendarm (Atteln und Grundsteinheim, Kr. Büren)",
        kreis="Bür",
        ort="Gr",
    )
    POEHLER = Sammlung(
        trace="Th. Pöhler",
        groups="Wortschatz|Pöhler",
        description="Therese Pöhler",
    )
    POTT = Sammlung(
        trace="Linden / Bch P.",
        groups="Wortschatz|Pott",
        description="G. Pott (Linden a. d. Ruhr)",
        kreis="Enr",
        ort="Li",
    )
    RAHMEDE = Sammlung(
        trace="Alt Gegend Lü|Rahmede",
        groups="Wortschatz|Rahmede",
        description="Bankangestellter A. D. Rahmede (Amt Lüdenscheid)",
        kreis="Alt",
        ort="Ls",
    )
    RAKERS = Sammlung(
        trace="Rakers|BinHi R|BenNo R",
        groups="Wortschatz|Rakers",
        description="Dr. A. Rakers (Kr. Grafschaft Bentheim)",
        kreis="Ben",
    )
    RECKE_GR = Sammlung(
        trace="Recke Gr.",
        groups="Wortschatz|ReckeGr",
        kreis="Tek",
        ort="Re",
    )
    REGENITER = Sammlung(
        trace="Regeniter",
        groups="Wortschatz|Regeniter",
        kreis="Enr",
    )
    REINKEN = Sammlung(
        trace="Frau Lehrer Reinken 75 Jahr, Natrup-Hagen 1914-1925 ges.",
        groups="Wortschatz|Reinken",
        kreis="Osn",
        ort="Nh",
    )
    REURIK = Sammlung(
        trace="Reurik",
        groups="Wortschatz|Reurik",
        description="Rektor H. Reurik (Hilten, Kr. Grafschaft Bentheim)",
        kreis="Ben",
    )
    SCHMITZ = Sammlung(
        trace="Stf Ar|Schmitz",
        groups="Wortschatz|Schmitz",
        description="Studienrat B. Schmitz (Altenrheine, Kr. Steinfurt)",
        kreis="Stf",
        ort="Ar",
    )
    SCHNELL = Sammlung(
        trace="Arn Hg|Schnell",
        groups="Wortschatz|Schnell",
        description="Clemens Schnell",
        kreis="Arn",
        ort="Hg",
    )
    SCHOENING = Sammlung(
        trace="Hal Bh (Schöning)|Brockhagen Schö.",
        groups="Wortschatz|Schöning",
        description="Bankbeamter H. Schöning (Brockhagen, Kr. Halle)",
        kreis="Hal",
        ort="Bh",
    )
    SCHOPPE = Sammlung(
        trace="Schoppe",
        groups="Wortschatz|Schoppe",
        description="Oberstudienrat i. R. Dr. J. Schoppe (Röckinghausen, Kr. Wiedenbrück)",
        kreis="Wie",
        ort="Rö",
    )
    SCHROEDER = Sammlung(
        trace="W. Schröder",
        groups="Wortschatz|Schröder",
        kreis="Ahs",
        ort="St",
    )
    STOVER = Sammlung(
        trace="Stover",
        groups="Wortschatz|Stover",
        kreis="Kos",
        ort="Ge",
    )
    WANNE_F = Sammlung(
        trace="Wanne F",
        groups="Wortschatz|WanneF",
        kreis="Gel",
        ort="Wa",
    )
    WARENDORF_KL = Sammlung(
        trace="Warendorf Kl.",
        groups="Wortschatz|WarendorfKl",
        kreis="Wdf",
        ort="Wd",
    )
    WARENDORF_NB = Sammlung(
        trace="Wardf. Nb.",
        groups="Wortschatz|WarendorfNb",
        kreis="Wdf",
        ort="Wd",
    )
    WARNING = Sammlung(
        trace="Versmold Loxten|Warning",
        groups="Wortschatz|Warning",
        description="Studienrat Dr. W. Warning (Versmold, Kr. Halle)",
        kreis="Hal",
        # ort="Lo",  # and "Vm"
    )
    WIX = Sammlung(
        trace="Gütersloh Wix",
        groups="Wortschatz|Wix",
        kreis="Wie",
        ort="Gü",
    )

    ##############################################################
    # Auszüge
    ##############################################################
    AHLEN_A = Sammlung(
        trace="Ahlen A.",
        groups="Auszüge|Abeler",
        sigle="Abeler",
        description="Abeler, J., Wörterbuch der Mundart von Ahlen, Kr. Beckum [Hs., um 1930. Oberschullehrer. Viele Wörter wohl aus der Heimatmundart Abelers, Elte, Kr. Steinfurt]",
        kreis="Bek",
        ort="Al",
    )
    ABH_NAT = Sammlung(
        trace="Abh. Prov. Mus. f. Natrukde|Iserlohn Extbr",
        groups="Auszüge|AbhNat",
        sigle="AbhNat",
        description="Abhandlungen aus dem Westfälischen Provinzial-Museum für Naturkunde. Jg. 7 ff.: Abhandlungen aus dem Landesmuseum der Provinz Westfalen, Museum für Naturkunde; Jg. 11: Abhandlungen aus dem Landesmuseum für Naturkunde der Provinz Westfalen. Jg. 1—11 Münster 1930—1940. Jg. 12 ff.: Abhandlungen aus dem Landesmuseum für Naturkunde zu Münster in Westfalen. Münster 1949 ff.",
    )
    AFD_AL = Sammlung(
        trace="AfdAl",
        groups="Auszüge|Anzeiger Altertum",
        sigle="AfdA",
        description="Anzeiger für deutsches Altertum und deutsche Literatur. Bd. 1 ff. Berlin 1876 ff.",
    )
    ALFERS = Sammlung(
        trace="J. Alfers",
        groups="Auszüge|Alfers",
        kreis="Klo",
        ort="Xy",
    )
    ALT_REK = Sammlung(
        trace="Alt-Recklinghausen",
        groups="Auszüge|AltRecklinghausen",
        sigle="Misgeld",
        description="Misgeld, H., Aolt-Riackelkusen. Stadt un Land. Skizzen aus dem Leben einer alten Stadt in Recklinghäuser Platt. Berlin o. J.",
        kreis="Rek",
        ort="Rh",
    )
    ARENS = Sammlung(
        trace="Kr. Olpe Arens",
        groups="Auszüge|Arens",
        sigle="Arens",
        description="Arens, J., Der Vokalismus der Mundarten im Kreise Olpe unter Zugrundelegung der Mundart von Elspe. Borna-Leipzig 1908 (Phil. Diss. Münster 1908)",
    )
    AUSTRUP = Sammlung(
        trace="Austrup",
        groups="Auszüge|Austrup",
        sigle="Aust",
        description="Austrup, B. H., Mester Biärtlink. 'n Vertellsel in mönsterländsk Platt. Warendorf o. J.",
    )
    BAHLMANN = Sammlung(
        trace="Münsterl.|Bahlmann",
        groups="Auszüge|Bahlmann",
        sigle="Bahlm",
        description="Bahlmann, P., Münsterische Lieder und Sprichwörter in plattdeutscher Sprache. Mit einer Einleitung über Münster's niederdeutsche Litteratur. Münster 1896",
        landschaft="Münsterl",
    )
    BAUER_C = Sammlung(
        trace="Bauer-C.|Wal",
        groups="Auszüge|Bauer",
        sigle="BauerC",
        description="Bauer, K., Waldeckisches Wörterbuch nebst Dialektproben, hrsg. v. H. Collitz. NordenLeipzig 1902 (Wörterbücher, hrsg. v. Verein f. niederdeutsche Sprachforschung, IV)",
        kreis="Wal",
    )
    BEISENHERZ = Sammlung(
        trace="Kurl Beis",
        groups="Auszüge|Beisenherz",
        sigle="Beis",
        description="Beisenherz, H., Vokalismus der Mundart des nordöstlichen Landkreises Dortmund. BornaLeipzig 1907 (Phil. Diss. Münster 1907)",
        kreis="Dor",
        ort="Ku",
    )
    BER_BIE = Sammlung(
        trace="Dahms: Flora v. Oelde|3. Ber. d. Naturwiss. Ver. Bielef.",
        groups="Auszüge|BerBie",
        sigle="BerBie",
        description="Bericht des Naturwissenschaftlichen Vereins für Bielefeld und Umgebung. Bd. 1 ff. Bielefeld 1908 ff.",
        kreis="Bek",
        ort="Öl",
    )
    BERGER = Sammlung(
        trace="Lin Pl (Berger)",
        groups="Auszüge|Berger",
        sigle="Berger",
        description="Berger, A., Niederdeutsche technische Ausdrücke aus der Handwerkersprache des Kreises Lingen. Borna-Leipzig 1907 (Phil. Diss. Münster 1907) [Mundart von Plantlünne]",
        kreis="Lin",
        ort="Pl",
    )
    BEULE = Sammlung(
        trace="Beule",
        groups="Auszüge|Beule",
        sigle="Beule",
        description="Beule, A., Biärgwind. Gedichte un Geschichten iut dem Suerlanne. Bigge 1922 (Suerlänske Baikelkes) [Mundart von Ramsbeck, Kr. Meschede]",
        kreis="Mes",
        ort="Ra",
    )
    BIRKENHAUER = Sammlung(
        trace="Birkenhauer",
        groups="Auszüge|Birkenhauer",
        sigle="Birk",
        description="Birkenhauer, J., Die Mundarten im Osten des Herzogtums Westfalen (die heutigen Kreise Brilon und Meschede umfassend). Phil. Diss. Münster 1921 [Hs.]",
    )
    BOENING = Sammlung(
        trace="Bön",
        groups="Auszüge|Böning",
        sigle="Böning",
        description="Böning, H., Plattdeutsches Wörterbuch für das Oldenburger Land. Oldenburg 1941 (Oldenburger Forschungen, 7) [Anhang, S. 136—153: II. Süd-Oldenburg. „Wörter, die in Nordoldenburg fehlen oder anders lauten.“]",
    )
    BOERSCH = Sammlung(
        trace="Börsch",
        groups="Auszüge|Börsch",
        sigle="Börsch",
        description="Börsch, J., Min Draulzen. Mundartliches aus Südsauerland. Drolshagen 1917 [Mundart von Drolshagen]",
        kreis="Olp",
        ort="Dh",
    )
    BRAEGELMANN = Sammlung(
        trace="Bräg.",
        groups="Auszüge|Brägelmann",
        sigle="Brägelm",
        description="Brägelmann, F., Vandevörn. Plattdeutsche Erzählungen aus dem Oldenburger Münsterlande und der nächsten Umgegend. Südlohne 1929",
    )
    BREPOHL = Sammlung(
        trace="Min Wt|Brepohl",
        groups="Auszüge|Brepohl",
        sigle="Brep",
        description="Brepohl, W., Bäuerliche Heilkunde in einem Dorfe des Mindener Landes um die Jahrhundertwende. Ein Beitrag zur Volkskunde von Minden-Ravensberg. Mindener Jahrbuch N. F. H. 2, 1950",
        kreis="Min",
        ort="Wt",
    )
    BROCKSIEPEN = Sammlung(
        trace="Brocks. Volkssp",
        groups="Auszüge|Brocksiepen",
        description="Brocksiepen (Hofschaft bei Halver)",
        kreis="Alt",
        ort="Ha",
    )
    BROECHER = Sammlung(
        trace="Rhonard Bröcher",
        groups="Auszüge|Bröcher",
        sigle="Bröcher",
        description="Bröcher, J., Die Sprache des Schmiedehandwerkes im Kreise Olpe auf Grund der Mundart von Rhonard. Berlin 1907 (Phil. Diss. Münster 1907)",
        kreis="Olp",
        ort="Ro",
    )
    BRUNK = Sammlung(
        trace="Brunk",
        groups="Auszüge|Brunk",
        sigle="Brunk",
        description="Brunk, A., Osnabrücker Rätselbüchlein. Osnabrück 1910",
    )
    BUELD = Sammlung(
        trace="Büld: Volk u. Spr.|Ortsneckerei",
        groups="Auszüge|Büld",
        sigle="Büld",
        description="Büld, H., Volk und Sprache im nördlichen Westfalen. Westfälische Ortschaften im Spiegel ihrer Sprache. Münster 1939",
    )
    BWPV = Sammlung(
        trace="Ber. Westf. Prov. Ver.",
        groups="Auszüge|JberWWK",
        sigle="JberWWK",
        description="Jahres-Bericht des Westfälischen Provinzial-Vereins für Wissenschaft und Kunst. 1—51/52 (1872—1922/24) Münster [1873—1925]",
    )
    DEITER = Sammlung(
        trace="Hann. Gesch.",
        groups="Auszüge|Deiter",
        sigle="Deiter",
        description="Deiter, H., Kurzes Wörterverzeichnis der plattdeutschen Mundart von Hastenbeck nebst plattdeutschen Redensarten. Hannoversche Geschichtsblätter 22 (1919) 113—164; Nachtrag zum Wörterverzeichnisse der Mundarten von Hastenbeck. Ebd. 24 (1921) 29—70",
    )
    DWA = Sammlung(
        trace="DWA",
        groups="Auszüge|DWA",
        sigle="DWA",
        description="Deutscher Wortatlas, hrsg. v. W. Mitzka u. L. E. Schmitt. Bd. 1 ff. Gießen 1951 ff.",
    )
    EGGERT = Sammlung(
        trace="EGGERT",
        groups="Auszüge|Eggert",
        sigle="Eggert",
        description="Eggert, B., Vergleichende Dialektgeographie des Gebietes der Beckumer Berge und der Soester Börde. Phil. Diss. Münster [1921; Hs.]",
        kreis="Bek",
        ort="Hf",
    )
    FBIL = Sammlung(
        trace="Bilstein",
        groups="Auszüge|FestbuchBilstein",
        sigle="FBil",
        description="Festbuch zur Siebenjahrhundertfeier der Schloßfreiheit u. Herrschaft Bilstein — Westfalen 1925, hrsg. v. A. Kleffmann. Dortmund [1925]",
    )
    FESTBUCH = Sammlung(
        trace="Festbuch",
        groups="Auszüge|FestbuchVreden",
        sigle="Vreden",
        description="Vredener Festbuch zur Feier des dreifachen Jubiläums von Kirche, Stadt und Feste im Jahre 1952. Vreden [1952]",
    )
    FIRMENICH = Sammlung(
        trace="Firmenich",
        groups="Auszüge|Firmenich",
        sigle="Firmenich",
        description="Firmenich, J. M. [Hrsg.], Germaniens Völkerstimmen. Sammlung der deutschen Mundarten in Dichtungen, Sagen, Märchen, Volksliedern u. s. w. 3 Bde. Berlin o. J. [Vorrede d. 3. Bd.s 1854]",
    )
    FREBEL = Sammlung(
        trace="Frebel",
        groups="Auszüge|Frebel",
        sigle="Frebel",
        description="Frebel, P., Die Mundarten des westlichen Sauerlandes, Marburg 1956. Auch unter dem Titel Die Mundarten des westlichen Sauerlandes zwischen Ebbegebirge und Arnsberger Wald. Marburg 1957 (Deutsche Dialektgeographie, 45)",
    )
    FROMMANN = Sammlung(
        trace="Frommann Maa",
        groups="Auszüge|Frommann",
        sigle="Frommann",
        description="Die deutschen Mundarten, begr. v. J. A. Pangkofer, fortges. v. G. K. Frommann. Bd. I—IV Nürnberg 1854—1857, V—VI Nördlingen 1858—59, VII (N. F. I) Halle 1877",
    )
    GLAD_BL = Sammlung(
        trace="Gladb. Bll.",
        groups="Auszüge|GladbeckerBlätter",
        sigle="GlaBl",
        description="Gladbecker Blätter für Orts- und Heimatkunde. Monatsbeilage der Gladbecker Zeitung. Jg. 1 ff. Gladbeck 1912 ff.; Jg. 22 ff.: Gladbecker Blätter für Orts- und Heimatkunde, hrsg. im Auftr. d. Ver. f. Orts- u. Heimatkunde. Gladbeck 1936 ff.",
    )
    GLAEN = Sammlung(
        trace="Glaen",
        groups="Auszüge|Glaen",
        sigle="Glaen",
        description="Glaen, K., Das Bild des Menschen in der Sprache von Dahl. Phil. Diss. Münster 1938 [Masch.-Schrift]",
        kreis="Pad",
        ort="Da",
    )
    GREGORY = Sammlung(
        trace="Gregory",
        groups="Auszüge|Gregory",
        sigle="Greg",
        description="Gregory, O., Flächengrammatik des Gebietes von Plettenberg in Westfalen. Gießen 1934 (Gießener Beiträge zur deutschen Philologie, hrsg. v. O. Behaghel u. A. Götze, 35)",
        kreis="Alt",
        ort="Im",
    )
    GRIMME_GES = Sammlung(
        trace="GrimXY",
        groups="Auszüge|Grimme",
        description="Grimme, F.W., Verschiedene Werke",
    )
    GROENINGER = Sammlung(
        trace="Mep Li-Gröninger 1981",
        groups="Auszüge|Gröninger",
        description="Gröninger-Lindloh, H., Gröningers Heimatgeschichten und Sprichwörter - Heiteres und Besinnliches aus dem Emsland",
        kreis="Mep",
        ort="Ll",
    )
    GRM = Sammlung(
        trace="GRM",
        groups="Auszüge|GRM",
        sigle="GRM",
        description="Germanisch-Romanische Monatsschrift. Bd. 1 ff. Heidelberg 1909 ff.",
    )
    GRUPE = Sammlung(
        trace="Grupe|Wellingen Gr.",
        groups="Auszüge|Grupe",
        sigle="Grupe",
        description="Grupe, H., Dat Blüsenbook. Osnabrück 1926 [G. stammt aus Wellingen, Kr. Osnabrück]",
        kreis="Osn",
        ort="We",
    )
    HANSEN = Sammlung(
        trace="Lip Hansen",
        groups="Auszüge|Hansen",
        sigle="Hansen",
        description="Eine Wörtersammlung zur lippischen Mundart von W. Hansen [Zettelsammlung]",
    )
    HARTWIG_VOGELN = Sammlung(
        trace="Hartwig Vogeln.",
        groups="Auszüge|HartwigVogeln",
        sigle="HarT",
        description="Hartwig, H., Plattdeutsche Tier- und Pflanzennamen aus Minden-Ravensberg. Teil I, Die Insektennamen. Teil II, 1. u. 2. Hälfte, Die Vogelnamen (Jahresberichte d. Hist. Ver. f. d. Grafschaft Ravensberg 1926, 1928, 1932)",
    )
    HASSEL = Sammlung(
        trace="M. Hassel",
        groups="Auszüge|Hassel",
        description="Maria Hassel",
        kreis="Lst",
        ort="Xy",
    )
    HBL_GL = Sammlung(
        trace="Heimatbll. d. Glocke",
        groups="Auszüge|HeimatblätterGlocke",
        description="Heimatblätter der 'Glocke' für die Kreise Beckum, Warendorf u. Wiedenbrück",
    )
    HBL_CASTR = Sammlung(
        trace="Heimatbll. f. Castrop",
        groups="Auszüge|HeimatblätterCastrop",
        sigle="HblC",
        description="Heimatblätter für Castrop und Umgegend. Monatsschrift des Vereins Heimatpflege. Jg. 1 ff. Castrop 1922 ff.",
    )
    HBL_IND = Sammlung(
        trace="Heimatbll. f. d. Ind.",
        groups="AuszügHeimatblle|HeimatblätterIndustrie",
        sigle="HblI",
        description="Heimatblätter. Monatsschrift für das niederrheinisch-westfälische Land, besonders für das Industriegebiet. Jg. 1 Essen 1919/20; Jg. 2 Dortmund 1920/21; Jg. 3: Heimatblätter. Monatsschrift für Land, Volk und Kunst in Westfalen und am Niederrhein. Dortmund 1921/22; Jg. 4 ff.: Die Heimat, Dortmund 1922 ff. [s. u. Heimat]",
    )
    HBL_O = Sammlung(
        trace="Heimatbll. f. d. Kr. Olpe",
        groups="Auszüge|HeimatblätterOlpe",
        sigle="HblO",
        description="Heimatblätter. Zeitschrift der Heimatvereine des Kreises Olpe. Jg. 1 ff. Olpe 1922 ff.; Jg. 7 ff.: Heimatblätter für das obere Sauerland. Zeitschrift für die Heimatvereine in den Kreisen Olpe und Meschede. Olpe 1930 ff.; Jg. 13 ff.: Heimatblätter für den Kreis Olpe. Olpe 1936 ff.",
    )
    HBL_MUE = Sammlung(
        trace="Münst. H. bll.",
        groups="Auszüge|MünsterischeHeimatblätter",
        sigle="MünHbl",
        description="Münsterische Heimatblätter. Beiträge zur Kulturgeschichte und Heimatkunde der westfälischen Lande und Nachbargebiete. Münster 1914–1919",
    )
    HBL_RE = Sammlung(
        trace="Rote Erde",
        groups="Auszüge|HeimatblätterRoteErde",
        sigle="HblRE",
        description="Heimatblätter der Roten Erde. Monatshefte, hrsg. f. d. Westfälischen Heimatbund v. F. Castelle u. K. Wagenfeld. Jg. 1—5 Münster 1919—1926",
    )
    HBL_SL = Sammlung(
        trace="Heimatbll. ob Sauerl",
    )
    HEIERMEIER = Sammlung(
        trace="Kr. Wiedenbr. Heierm.",
        groups="Auszüge|Heiermeier",
        sigle="Heierm",
        description="Heiermeier, B., Die landwirtschaftlichen Fachausdrücke Westfalens auf Grund der Mundart des Kreises Wiedenbrück. Bielefeld 1914 (Phil. Diss. Münster 1914). Auch im 28. Jahresbericht d. Hist. Ver. f. d. Grafschaft Ravensberg, Bielefeld 1914, S. 39—96 [H. *1888 in Mastholte, Kr. Wiedenbrück]",
        kreis="Wie",
    )
    HEIMAT_EMSDT = Sammlung(
        trace="Heimat_Emsdetten",
        groups="Auszüge|HeimatEmsdetten",
        sigle="HEms",
        description="Die Heimat. Zwanglose Blätter des Heimatbundes Emsdetten. Jg. 1 ff. Emsdetten 1919 ff.; Jg. 7 ff. als Beilage zur Emsdettener Volkszeitung. Emsdetten 1929 ff.; Jg. 18 ff.: Emsdettener Heimatblätter, hrsg. v. Heimatbund Emsdetten. Emsdetten 1950 ff.",
        kreis="Stf",
        ort="Em",
    )
    HENSSEN = Sammlung(
        trace="Henssen|Uhlenflucht",
        groups="Auszüge|Henssen",
    )
    HELLBERG = Sammlung(
        trace="Hellberg",
        groups="Auszüge|Hellberg",
    )
    HERDEMANN = Sammlung(
        trace="Borken Herdemann",
        groups="Auszüge|HerdeMann",
        sigle="Herdem",
        description="Herdemann, F., Versuch einer Lautlehre der westmünsterländischen Mundart. Phil. Diss. Münster 1921 [Hs.]. Auszug unter demselben Titel Leipzig 1925",
        kreis="Bor",
        ort="Bo",
    )
    HERKHOFF = Sammlung(
        trace="Osn Hg: Herk/Seg",
        groups="Auszüge|Herkhoff",
        sigle="Herk",
        description="Herkenhoff, H., Anhang von Wörtern, die sich nicht bei Woeste und Klöntrup finden. [Einem von H. 1920 gemachten Auszug aus Klön beigefügt; Hs., im Archiv des Westfälischen Wörterbuches]",
        kreis="Osn",
        ort="Hg",
    )
    HOLTHAUS = Sammlung(
        trace="Holthaus Mskr.",
        groups="Auszüge|Holthaus",
        sigle="Holthaus",
        description="Holthaus, P. H., Materialien zu einer Schrift, betitelt: Süd-Westfälisches Wörterbuch ... [Hs. aus dem Anfang des 19. Jh.s im Archiv des Westfälischen Wörterbuches. H. *1759 bei Breckerfeld, Ennepe-Ruhr-Kreis; seit 1789 Conrektor in Schwelm; ^+ 1831]",
        kreis="Enr",
        ort="Hh",
    )
    HOLTMANN = Sammlung(
        trace="Holtmann",
        groups="Auszüge|Holtmann",
        sigle="Holtm",
        description="Holtmann, K., Plattdütske Fierdaoge. Lingen 1924",
    )
    HONCAMP = Sammlung(
        trace="Honc|Honc.-Anm.",
        groups="Auszüge|Honcamp",
        sigle="Honc",
        description="Honcamp, F. C., Sprichwörter und sprichwörtliche Redeformen des westfälischen Volkes [Hs. i. d. Univ.-Bibl. Greifswald. H. *1805 in Welwer b. Soest; 1822—1824 Lehrerseminar Soest; seit 1825 in Büren; ^+ 1866. In der Einleitung dankt H. dem Seminarlehrer Dahlhof in Soest und dem Lehrer Lösebrink in Bönen, „die zu der Sammlung einen bedeutenden Beitrag geliefert haben“.]",
    )
    HUEFFER = Sammlung(
        trace="Hüffer",
        groups="Auszüge|Hüffer",
        sigle="Hüffer",
        description="Hüffer, Adelheid, Volksmedizin in Westfalen. Med. Diss. Münster 1945 [Masch.-Schrift]",
    )
    HUNOLD = Sammlung(
        trace="Paderborn Hunold",
        groups="Auszüge|Hunold",
        sigle="Hunold",
        description="Hunold, J. F., Mein Patterböarner Platt. Stalen van Reimels un Vertällekes in Spaß un Äerns. Paderborn 1928",
        kreis="Pad",
    )
    HUNSCHE_LE = Sammlung(
        trace="Hunsche|Erg. zu Woeste",
        groups="Auszüge|Hunsche|Lengerich",
        description="Hunsche, F. E., Ergänzungen zu Woeste",
        kreis="Tek",
        ort="Le",
    )
    HUNSCHE_LI = Sammlung(
        trace="Tek Li = Hunsche 1978",
        groups="Auszüge|Hunsche|Lienen",
        description="Hunsche, F. E., Lienen, Kr. Tecklenburg",
        kreis="Tek",
        ort="Li",
    )
    HUNTEMANN = Sammlung(
        trace="Hunteman:Pflanzen",
        groups="Auszüge|Huntemann",
        description="Huntemann, J., Die plattdeutschen Namen unserer Kulturgewächse und der wildwachsenden Pflanzenarten. Oldenburg 21931",
    )
    JB_EMSL = Sammlung(
        trace="Jb. Emsl.",
        groups="Auszüge|JahrbuchEmsland",
        sigle="JbEmsl",
        description="Jahrbuch des Emsländischen Heimatvereins. Bd. 1 ff. Meppen 1953 ff.; Bd. 11 ff. Lingen 1964 ff.",
    )
    JEURINK = Sammlung(
        trace="Jeurink",
        groups="Auszüge|Jeurink",
    )
    JOSTES = Sammlung(
        trace="Jostes",
        groups="Auszüge|Jostes",
        sigle="Jostes",
        description="Jostes, F., Westfälisches Trachtenbuch. Die jetzigen und ehemaligen westfälischen und schaumburgischen Gebiete umfassend. Bielefeld-Berlin-Leipzig 1904. Zweite Auflage bearb. u. erw. v. Martha Bringemeier, Westfälisches Trachtenbuch. Volksleben und Volkskultur in Westfalen. Die jetzigen und ehemaligen westfälischen und schaumburgischen Gebiete umfassend. Münster 1961",
    )
    KAHMANN = Sammlung(
        trace="Hs. Kahmann",
        groups="Auszüge|Kahmann",
        kreis="Bbr",
        ort="We",
    )
    KAUMANN_L = Sammlung(
        trace="Kaumann L",
        groups="Auszüge|Kaumann",
        sigle="KaumL",
        description="Kaumann, J., Entwurf einer Laut- und Flexionslehre der münsterischen Mundart in ihrem gegenwärtigen Zustande. Phil. Diss. 1. Teil, Lautlehre. Münster 1884",
        kreis="Mün",
        ort="Mü",
    )
    KK_WB = Sammlung(
        trace="KkWb",
        groups="Auszüge|KKWB",
    )
    KLEINN = Sammlung(
        trace="Kleinn",
        groups="Auszüge|Kleinn",
        sigle="Kleinn",
        description="Kleinn, Klementine, Volk und Sprache zwischen Egge und Weser. Phil. Diss. Münster 1942 [Hs.]",
        kreis="Höx",
    )
    KLOENTRUP = Sammlung(
        trace="Klöntrup",
        groups="Auszüge|Klöntrup",
        sigle="Klön",
        description="Rosemann, Johan Gilges, genannt Klöntrup, Niederdeutsch-Westphälisches Wörterbuch. [Vorwort v. 1824] [Hs. im Besitz des Ratsgymnasiums zu Osnabrück] Buchstabe A zum Abdruck gebracht von F. Runge, Osnabrück 1890 (Festschrift zur Begrüßung d. Ver. f. niederdeutsche Sprachforschung bei seiner Pfingsten 1890 in Osnabrück stattfindenden Jahresversammlung)",
        kreis="Osn",
    )
    KNOCHE = Sammlung(
        trace="HPaderb|KN",
        groups="Auszüge|Knoche",
        sigle="Knoche",
        description="Knoche, R., Niu lustert mol! Plattdeutsche Schwänke und Geschichten. Auswahl, hrsg. v. F. Wippermann. Paderborn 21959",
        landschaft="HPaderb",
    )
    KOCH = Sammlung(
        trace="Koch:Flora",
        groups="Auszüge|Koche",
        sigle="Koch",
        description="Koch, K., Flora des Regierungsbezirkes Osnabrück und der benachbarten Gebiete. Osnabrück 1934",
    )
    KOEPPEN = Sammlung(
        trace="Dortm./Köppen",
        groups="Auszüge|Köppen",
        sigle="Köppen",
        description="Köppen, H., Verzeichniss der Idiotismen in plattdeutscher Mundart, volksthümlich in Dortmund und dessen Umgegend. Veröff. v. seinen Freunden u. Verehrern. Als Manuscript gedruckt. Dortmund 1877",
        kreis="Dor",
    )
    KOESTER_BHF = Sammlung(
        trace="Kös HF",
        groups="Auszüge|KösterBurHollFast",
        sigle="KösterB",
        description="Köster, B., Bur, holl faste, wat du häst! Lingen a. d. Ems 1926 [Mundart d. Kr. Lingen. K. war Pfarrer in Glandorf, Kr. Osnabrück; *1869 in Lahn, Kr. Aschendorf; ^+ 1944 in Iburg, Kr. Osnabrück]",
    )
    KOESTER_JK = Sammlung(
        trace="Kös JK",
        groups="Auszüge|KösterJanKardel",
        sigle="KösterJK",
        description="Köster, B., Jan Kardel un siene Bande. Lingen a. d. Ems 1926 [Mundart des Hümmlings. Vgl. Bemerkungen zu KösterB]",
    )
    KRAUTBUND = Sammlung(
        trace="Krautbund im Paderborner Gebiet",
        groups="Auszüge|Krautbund",
        description="Krautbund im Paderborner Gebiet",
        kreis="Pad",
    )
    KRUEGER_HS = Sammlung(
        trace="Krüg HS",
        groups="Auszüge|Krüger|HempelmannsSmiede",
        sigle="KrüHS",
        description="Krüger, F., Hempelmann's Smiede. Ein westfälischer Roman aus der guten alten Zeit in münsterländisch-niederdeutscher Sprache. Bd. 1 Leipzig 1893, Bd. 2 u. 3 Leipzig 1894 [K. *1843 in Beckum, Kr. Beckum]",
    )
    KRUEGER_IS = Sammlung(
        trace="Krüg IS",
        groups="Auszüge|Krüger|Iärwschaden",
        sigle="KrüI",
        description="Krüger, F., Iärwschaden. Dortmund [1925] [K. *1843 in Beckum, Kr. Beckum]",
    )
    KRUEGER_RW = Sammlung(
        trace="Krüg RW",
        groups="Auszüge|Krüger|RuggeWiäge",
        sigle="KrüRW",
        description="Krüger, F., Rugge Wiäge. Aus dem westfälischen Bauernleben in niederdeutscher Sprache erzählt. Leipzig ³1891 (Bibliothek niederdeutscher Werke, 7) [K. *1843 in Beckum, Kr. Beckum]",
    )
    KRUMME = Sammlung(
        trace="M. Krumme 1977",
        groups="Auszüge|Krumme",
    )
    KUHN = Sammlung(
        trace="Kuhn Sagen",
        groups="Auszüge|Kuhn",
        sigle="Kuhn",
        description="Kuhn, A., Sagen, Gebräuche und Märchen aus Westfalen und einigen andern, besonders den angrenzenden Gegenden Norddeutschlands. 1. Teil, Sagen; 2. Teil, Gebräuche und Märchen. Leipzig 1859",
    )
    LANDOIS_FE = Sammlung(
        trace="Landois, Essink",
        groups="Auszüge|LandoisEssink",
        sigle="LandoisFE",
        description="Landois, H., Frans Essink sien Liäwen un Driewen äs aolt Mönstersk Kind. Komischer Roman in 6 Abt. 1, Bi Liäwtieden. Leipzig 101905. 2, Nao sienen Daud. 101921. 3, Up de Tuckesburg. 21901. 4, Up de Seelenwanderung. 21909. 5, Prof. Dr. H. Landois. 1900 (Illustr. Bibliothek niederdeutscher Klassiker, 1—5)",
    )
    LEHNHOFF = Sammlung(
        trace="Lehnhoff Spielbuch",
        groups="Auszüge|Lehnhoff",
        description="Westfälisches Spielbuch : 365 Jugend- und Volksspiele ; aus Wirklichkeit und Überlieferung gesammelt Wilhelm Lehnhoff",
    )
    LIN_BE_LW = Sammlung(
        trace="Lin Be|Lw",
        groups="Auszüge|BeestermöllerLandwirtschaft",
        sigle="Beesterm",
        description="Beestermöller, A., Technische landwirtschaftliche Ausdrücke aus dem Kreise Lingen. Phil. Diss. Münster 1916 [Hs., Mundart von Beesten]",
        kreis="Lin",
        ort="Be",
    )
    LINGEN_KR = Sammlung(
        trace="Kreis Lingen",
        groups="Auszüge|KreisLingen",
        sigle="Lingen",
        description="Der Kreis Lingen, hrsg. v. Lehrerverein d. Diözese Osnabrück. Lingen 1905 (Beitr. z. Heimatkunde d. Regierungsbezirks Osnabrück, 1)",
    )
    LOEFFLER = Sammlung(
        trace="Loeffler",
        groups="Auszüge|Loeffler",
        sigle="Loeffler",
        description="Loeffler, N., Flora von Rheine. Programm des Gymnasiums Rheine. Rheine 1904",
    )
    LYRA = Sammlung(
        trace="Lyra",
        groups="Auszüge|Lyra",
        sigle="Lyra",
        description="Lyra, F. W., Plattdeutsche Briefe, Erzählungen und Gedichte mit besonderer Rücksicht auf Sprichwörter und eigenthümliche Redensarten des Landvolks in Westphalen. Osnabrück 21856",
        kreis="Osn",
        ort="Xy",
    )
    MEIER = Sammlung(
        trace="Enger Meier",
        groups="Auszüge|Meier",
        sigle="Meier",
        description="Meier, E., Beiträge zur Kenntnis des Niederdeutschen. Gewerksausdrücke des Schlachters in Westfalen mit besonderer Berücksichtigung Ravensbergs. Münster 1914 (Phil. Diss. Münster 1914). Auch im 29. Jahresbericht d. Hist. Ver. f. d. Grafschaft Ravensberg, Bielefeld 1915, S. 1—69",
        kreis="Hfd",
        ort="En",
    )
    MEYER = Sammlung(
        trace="Meyer",
        groups="Auszüge|Meyer",
        sigle="Meyer",
        description="Meyer, E. H. W., Ein Niedersächsisches Dorf am Ende des 19. Jahrhunderts. Eine volkskundliche Untersuchung. Bielefeld [1927] (Sonderveröffentlichungen d. Hist. Ver. f. d. Grafschaft Ravensberg, 1)",
        kreis="Min",
        ort="Wh",
    )
    MISGELD_AR = Sammlung(
        trace="Misg. AR",
        groups="Auszüge|MisgeldAR",
        sigle="Misgeld",
        description="Misgeld, H., Aolt-Riackelkusen. Stadt un Land. Skizzen aus dem Leben einer alten Stadt in Recklinghäuser Platt. Berlin o. J.",
        kreis="Rek",
    )
    MISGELD_WO = Sammlung(
        trace="Misg.Wö.",
        groups="Auszüge|MisgeldWö",
    )
    MITT_HG = Sammlung(
        trace="Mitt Hasegau",
        groups="Auszüge|MitteilungenHasegau",
        sigle="MittHg",
        description="Mittheilungen des Vereins für Geschichte und Alterthumskunde des Hasegaues. H. 1 ff. Ankum, (später) Lingen 1887 ff.",
    )
    MITT_LIP = Sammlung(
        trace="Lip. Mitt.",
        groups="Auszüge|MitteilungenLippe",
        sigle="MittLipp",
        description="Mitteilungen aus der lippischen Geschichte und Landeskunde. Hrsg. v. Naturwiss. Ver. in Detmold. Bd. 1 ff. Detmold 1903 ff.; Bd. 22 ff.: Lippische Mitteilungen aus Geschichte und Landeskunde. Detmold 1957 ff.",
    )
    MOELLER = Sammlung(
        trace="Lhs Sm Möller",
        groups="Auszüge|Möller",
        description="Lhs Sm Möller 1976",
        kreis="Lhs",
        ort="Sm",
    )
    MOENNIGHOFF = Sammlung(
        trace="Moennighoff",
        groups="Auszüge|Moennighoff",
        kreis="Unn",
        ort="Hi",
    )
    MOHR = Sammlung(
        trace="Mohr",
        groups="Auszüge|Mohr",
        sigle="Mohr",
        description="Mohr, A., Die  intellektuelle Einschätzung des Menschen in der Mundart des Amtes  Drolshagen im Sauerland (Ein mundartliches sprachliches Feld). Münster 1939 (Schriften d. Volkskundlichen Kommission im Provinzialinstitut f. westf. Landes- u. Volkskunde, hrsg. v. J. Trier u. K. Schulte Kemminghausen, H. 3)",
    )
    MUELLER_D = Sammlung(
        trace="Müller D",
        groups="Auszüge|Müller|Diepholz",
        sigle="MüllerD",
        description="Müller, Westphälisches Idiotikon aus der Grafschaft Diepholz. Annalen der Braunschweigisch-Lüneburgischen Churlande 8 (1794) 590—603",
        kreis="Die",
    )
    MUELLER_WS = Sammlung(
        trace="K.A.Müller",
        groups="Auszüge|Müller|Wörtersammlung",
        sigle="MüllerN",
        description="Müller, K. A., Wörtersammlung von Niedersfeld, Kr. Brilon. 1963 [Hs.; im Archiv d. Westfälischen Wörterbuches]",
        kreis="Bri",
        ort="Nf",
    )
    MUEN_G = Sammlung(
        trace="Münst. Gesch. Sagen u. Legenen",
        groups="Auszüge|MünsterischeGeschichten",
        sigle="MünG",
        description="Münsterische Geschichten, Sagen und Legenden nebst einem Anhange von Volksliedern und Sprüchwörtern. Münster 1825",
    )
    N_WESTF_MAG = Sammlung(
        trace="N.Westf.Mag",
        groups="Auszüge|NeuestWestphMag",
        sigle="MagNW",
        description="Neues Westphälisches Magazin zur Geographie, Historie und Statistik, hrsg. v. P. F. Weddigen. 3 Bde. Bd. 1 Bückeburg 1789; Bd. 2 Leipzig-Lemgo-Berlin-Bielefeld 1790; Bd. 3 Lemgo-Leipzig-Berlin-Bielefeld 1792",
    )
    NAT_HEIM = Sammlung(
        trace="Natur und Heimat",
        groups="Auszüge|NaturHeimat",
        sigle="NatH",
        description="Natur und Heimat. Blätter für den Naturschutz und alle Gebiete der Naturkunde, hrsg. v. d. Arbeitsgemeinschaft naturkundlicher u. Naturschutz-Vereine der Gaue Westfalen-Nord u. -Süd. Jg. [1—]8 Münster 1934—1941; Jg. 9 ff.: hrsg. v. Landesmuseum f. Naturkunde zu Münster, Münster 1949 ff.",
    )
    ND_JB = Sammlung(
        trace="Nd. Jb.",
        groups="Auszüge|NiederdeutschesJahrbuch",
        sigle="NdJb",
        description="Jahrbuch des Vereins für niederdeutsche Sprachforschung (Niederdeutsches Jahrbuch). Jg. 1875 Bremen 1876 ff.; Bd. 7 ff., Jg. 1881, Norden-Leipzig 1882 ff.; Bd. 54 ff., Jg. 1928, Hamburg 1929 ff.; Bd. 57/58 ff., Jg. 1941/42, Neumünster 1943 ff.",
    )
    ND_KBL = Sammlung(
        trace="Nd. Kbl.|Korr.bl.",
        groups="Auszüge|NdKbl",
        sigle="NdKbl",
        description="Korrespondenzblatt des Vereins für niederdeutsche Sprachforschung. Jg. 1 (1876/77) Norden-Leipzig 1877; Jg. 2 ff. Hamburg 1878 ff.; H. 56 ff., Jg. 1943/49, Neumünster 1950 ff.",
    )
    NDS_WB = Sammlung(
        trace="NdsWb",
        groups="Auszüge|NdsWb",
        sigle="NdsWb",
        description="Niedersächsisches Wörterbuch. 1. Bd. hrsg. d. W. Jungandreas, Neumünster 1965; seit dem 2. Bd. hrsg. d. H. Wesche, Neumünster 1958 ff.",
    )
    NIBLETT = Sammlung(
        trace="Niblett",
        groups="Auszüge|Niblett",
        sigle="Niblett",
        description="Niblett, A. E., Grammatik der osnabrückischen Mundart. I. Teil. Osnabrück 1913 (Phil. Diss. München 1913) [Mundart der nächsten Umgebung Osnabrücks]",
    )
    NOTHOLZ = Sammlung(
        trace="Notholz",
        groups="Auszüge|Notholz",
        sigle="Notholz",
        description="Notholz, O., Wegenlieder un Kinnerreime. Bückeburg 1901",
    )
    NS = Sammlung(
        trace="Ns, X...",
        groups="Auszüge|Ns",
    )
    OESTERHAUS = Sammlung(
        trace="Lip Oe|Lipp Oe",
        groups="Auszüge|Oesterhaus",
        sigle="Oesterh",
        description="Oesterhaus, W., Wörterbuch der Lippisch-plattdeutschen Mundart [Hs.; im Archiv des Westfälischen Wörterbuches; Oe. * 1840 in Detmold]",
    )
    OSTENDORF = Sammlung(
        trace="Ost Wä",
        groups="Auszüge|Ostendorf",
        sigle="Ostend",
        description="Ostendorf, J., Den Wäwedamp. Ein Volksspiel in fünf Aufzügen. Bocholt 1922",
        kreis="Bor",
        ort="Bh",
    )
    PICKERT = Sammlung(
        trace="Pickert: Vok.",
        groups="Auszüge|Pickert",
        description="Pickert, J., Vokalismus der Stammsilben in der Mundart von Dorsten i. Westf. Zs. f. Deutsche Mundarten, Jg. 1917, 132—149",
        kreis="Rek",
        ort="Do",
    )
    PLATENAU = Sammlung(
        trace="Platenau",
        groups="Auszüge|Platenau",
    )
    PLATENAU_SP = Sammlung(
        trace="PlatenauSP",
        groups="Auszüge|PlatenauSp",
        sigle="PlatenauSp",
        description="Platenau, F., Alte Sprichwörter, Redensarten und Wetterregeln aus dem Lipperland. Istrup 1967 [vervielf. Ms.]",
    )
    PLATENAU_WB = Sammlung(
        trace="PlatenauWb",
        groups="Auszüge|PlatenauWb",
        description="Platenau Wörterbuch",
    )
    RAKERS_GV = Sammlung(
        trace="Rakers GV",
        groups="Auszüge|RakersGV",
        sigle="RakersGV",
        description="Rakers, A., Grafschafter Volksreime und Sprichwörter. 1. Teil, Die Sammlung. Bentheim 1930 (Das Bentheimer Land, hrsg. v. H. Specht, V)",
    )
    RAKERS_MB = Sammlung(
        trace="Rakers MB",
        sigle="RakersMB",
        groups="Auszüge|RakersMB",
        description="Rakers, A., Die Mundarten der alten Grafschaft Bentheim und ihrer reichsdeutschen und niederländischen Umgebung. Auf dialektgeographisch-geschichtlicher Grundlage. Oldenburg 1944 (Veröff. d. Provinzial-Instituts f. Landesplanung u. niedersächsische Landesforschung Hannover-Göttingen, Reihe A II, Bd. 16)",
    )
    RATHERT = Sammlung(
        trace="Rathert: Brot u. Kuchen",
        groups="Auszüge|Rathert",
        sigle="Rathert",
        description="Rathert, H., Westfälische Brot- und Kuchennamen. Phil. Diss. Münster 1916. Auch im 30. Jahresbericht d. Hist. Ver. f. d. Grafschaft Ravensberg, Bielefeld 1916, S. 1—56",
    )
    RAUB_SP = Sammlung(
        trace="Raub Sp",
        groups="Auszüge|RaubSp",
    )
    RAV_BL = Sammlung(
        trace="Ravensb. Bl.",
        groups="Auszüge|RavensbergerBlätter",
        sigle="RavBl",
        description="Ravensberger Blätter für Geschichts-, Volks- und Heimatkunde, hrsg. i. Auftr. d. Hist. Ver. f. d. Grafschaft Ravensberg. Jg. 1 ff. Bielefeld 1901 ff.; Jg. 50 ff.: Ravensberger Blätter. Organ d. Hist. Ver. f. d. Grafschaft Ravensberg. Bielefeld 1950 ff.",
        landschaft="Ravensbg",
    )
    RAV_HK = Sammlung(
        trace="Ravensb. Heimatkal",
        groups="Auszüge|RavensbergerHeimatkalender",
    )
    RECKELS = Sammlung(
        trace="Reckels",
        groups="Auszüge|Reckels",
        sigle="Reck",
        description="Reckels, H., Volkskunde des Kreises Steinfurt. 2. Teil. Burgsteinfurt 1933 (Heimatjahrbuch d. Kr. Steinfurt 1932)",
        kreis="Stf",
    )
    RICKELMANN = Sammlung(
        trace="Rick.",
        groups="Auszüge|Rickelmann",
        sigle="Rickelm",
        description="Rickelmann, H., Mettingen im Wandel der Zeiten. Lengerich 1953",
        kreis="Tek",
        ort="Me",
    )
    RIEPE = Sammlung(
        trace="Riepe PS",
        groups="Auszüge|Riepe",
        sigle="Riepe",
        description="Riepe, H., Pottkooken un Swattbraut. Osnabrück 1953",
    )
    ROTTMANN = Sammlung(
        trace="Rottmann",
        groups="Auszüge|Rottmann",
        kreis="Rek",
        ort="Kh",
    )
    SB_BL = Sammlung(
        trace="Soester Börde Bl.",
        groups="Auszüge|SoesterBördeBl",
    )
    SCHEELE = Sammlung(
        trace="Scheele",
        groups="Auszüge|Scheele",
        sigle="Scheele",
        description="Scheele, N., Geschichte der Gemeinde Olpe-Land. Olpe 1952",
    )
    SCHEPERS = Sammlung(
        trace="Schepers",
        groups="Auszüge|Schepers",
        sigle="Schepers",
        description="Schepers, J., Westfalen-Lippe. Mit Vorwort u. Beitrag v. G. Wolf. Münster 1960 (Haus und Hof deutscher Bauern. Eine Darstellung in Einzel-Bänden, hrsg. v. G. Wolf, Bd. 2)",
    )
    SCHLEEF = Sammlung(
        trace="Schleef",
        groups="Auszüge|Schleef",
        description="Schleef, W., Dortmunder Wörterbuch. Köln-Graz 1967 (Niederdeutsche Studien, hrsg. v. W. Foerste, 15)",
        kreis="Dor",
    )
    SCHLUETER = Sammlung(
        trace="Schlüter",
        groups="Auszüge|Schlüter",
        sigle="Schlüter",
        description="Schlüter, J., Die niederländischen Wörter in der westmünsterländischen Mundart. Phil. Diss. Münster 1952 [Masch.-Schrift]",
    )
    SCHMEDING = Sammlung(
        trace="Schmed",
        groups="Auszüge|Schmeding",
        sigle="Schmed",
        description="Schmeding, H., Die Mundart des Kirchspiels Lavelsloh und der angrenzenden Ortschaften. Münster 1938 (Schriften d. Volkskundlichen Kommission im Provinzialinstitut f. westf. Landes- u. Volkskunde, hrsg. v. J. Trier u. K. Schulte Kemminghausen, H. 1)",
    )
    SCHMELZER = Sammlung(
        trace="Schmelzer",
        groups="Auszüge|Schmelzer",
        sigle="Schmelzer",
        description="Schmelzer, J., Unterschiede zwischen dem süderländischen und siegerländischen Wortschatz. Phil. Diss. Münster 1906",
    )
    SCHOENHOFF = Sammlung(
        trace="Schönhoff Ems",
        groups="Auszüge|Schönhoff",
        sigle="Schönhoff",
        description="Schönhoff, H., Emsländische Grammatik. Laut- und Formenlehre der emsländischen Mundarten. Heidelberg 1908 (Germanische Bibliothek, hrsg. v. W. Streitberg, Reihe I, Bd. 8)",
        landschaft="Emsl",
    )
    SCHONEWEG = Sammlung(
        trace="Schoneweg Leinengewerbe",
        groups="Auszüge|Schoneweg",
        sigle="SchonL",
        description="Schoneweg, E., Das Leinengewerbe in der Grafschaft Ravensberg. Ein Beitrag zur niederdeutschen Volks- und Altertumskunde. Bielefeld 1923",
    )
    SCHOPPE_MSKR = Sammlung(
        trace="Röckinghausen/Wie Schoppe Mskr.",
        groups="Auszüge|Schoppe",
        sigle="Schoppe",
        description="Schoppe, J., Die Mundart von Röckinghausen bei Wiedenbrück. 1930 [Unter Zugrundelegung der Arbeit von Wix. Hs. im Archiv des Westfälischen Wörterbuches]",
        kreis="Wie",
        ort="Rö",
    )
    SCHULHOF = Sammlung(
        trace="Schulhof: Kr.Melle",
        groups="Auszüge|Schulhof",
        sigle="Schulhof",
        description="Schulhof, F., Der Kreis Melle (Grönegau). Lingen a. d. Ems 1908 (Beiträge z. Heimatkunde d. Regierungsbezirks Osnabrück, 2)",
        kreis="Mel",
    )
    SCHWAGMEYER = Sammlung(
        trace="Hiddenh. Schwagm.",
        groups="Auszüge|Schwagmeyer",
        sigle="Schwagm",
        description="Schwagmeyer, F., Der Lautstand der Ravensbergischen Mundart von Hiddenhausen. Berlin 1908 (Phil. Diss. Münster 1907)",
        kreis="Hfd",
        ort="Hi",
    )
    SCHWEER = Sammlung(
        trace="Schweer",
        groups="Auszüge|Schweer",
        description="Grafschafter Vornamen",
    )
    SOEST_HOLTH = Sammlung(
        trace="Soest Holth. D",
        groups="Auszüge|SoestHolthausen",
        sigle="HolthSos",
        description="Holthausen, F., Die Soester Mundart. Laut- und Formenlehre nebst Texten. Norden-Leipzig 1886 (Forschungen, hrsg. v. Ver. f. Niederdeutsche Sprachforschung, 1)",
        kreis="Sos",
        ort="So",
    )
    SOESTER_BOERDE_WB = Sammlung(
        trace="Wb. Soester Börde",
        groups="Auszüge|SoesterBördeWb",
        sigle="SchmB",
        description="Schmoeckel, H., u. A. Blesken, Wörterbuch der Soester Börde, ein Beitrag zur westfälischen Mundartenforschung. Soest 1952 (Soester wissenschaftliche Beiträge, 5)",
        kreis="Sos",
    )
    SOOST = Sammlung(
        trace="Soost",
        groups="Auszüge|Soost",
        sigle="Soost",
        description="Soost, H. H., Studien zur Dialektgeographie Nordhessens. Phil. Diss. Marburg 1920 [Hs.]",
    )
    STOLTE = Sammlung(
        trace="Stolte Bauernhof",
        groups="Auszüge|Stolte",
        sigle="Stolte",
        description="Stolte, H., Bauernhof und Mundart in Ravensberg. Beiträge zur niederdeutschen Volkskunde. Bielefeld 1931",
        kreis="Hal",
        ort="Bh",
    )
    STRODTMANN = Sammlung(
        trace="Strodtmann",
        groups="Auszüge|Strodtmann",
        sigle="Strodtm",
        description="Strodtmann, J. Ch., Idioticon Osnabrugense. Leipzig-Altona 1756",
    )
    SUTTMEYER = Sammlung(
        trace="Suttmeyer 1980",
        groups="Auszüge|Suttmeyer",
        kreis="Osn",
        ort="Kl",
    )
    TRAUTMANN = Sammlung(
        trace="Trautmann: Hümml",
        groups="Auszüge|Trautmann",
        sigle="Trautm",
        description="Trautmann, A., Hümmlinger Skizzen. 2. Aufl. Papenburg o. J. [1. Aufl. Lingen 1910]",
    )
    TRUTZNACHTIGALL = Sammlung(
        trace="Trutznachtigall",
        groups="Auszüge|Trutznachtigall",
        sigle="Trutz",
        description="Trutznachtigall. Heimatblätter für das kölnische Sauerland. Jg. 1 ff. Bigge 1919 ff.; Jg. 10 ff.: Heimwacht. Zeitschrift des Sauerländer-Heimatbundes. Bigge 1928 ff.; Jg. 15 ff.: Sauerlandruf. Zeitschrift ... Arnsberg 1953 ff.",
    )
    VEHSLAGE = Sammlung(
        trace="Badbergen Vehslage",
        groups="Auszüge|Vehslage",
        description="Vehslage, H., Die Mundart des Artlandes auf der Grundlage der Mundart des Kirchspiels Badbergen. Borna-Leipzig 1908 (Phil. Diss. Münster 1908) [V. * in Grothe b. Badbergen]",
        kreis="Bbr",
        ort="Ba",
    )
    VEST_HEIM = Sammlung(
        trace="Vestische Heimat",
        groups="Auszüge|VestischeHeimat",
        sigle="VestH",
        description="Vestische Heimat. Hrsg. v. Heimatgebiet Vest. Recklinghausen [1965]",
    )
    VEST_Z = Sammlung(
        trace="Vest.Z.Jg.",
        groups="Auszüge|VestischeZeitschrift",
        sigle="VestZ",
        description="Vestische Zeitschrift. Zeitschrift der Vereine für Orts- und Heimatkunde im Veste und Kreise Recklinghausen, begr. als Zeitschrift der Vereine ... Münster (u. a. Verlagsorte) 1904—1941",
    )
    VKL_ARCH = Sammlung(
        trace="Vkl. Arch.",
        groups="Auszüge|ArchivVolkskunde",
        description="Sammlungen des Archivs für westfälische Volkskunde (Volkskundliche Kommission) Münster",
    )
    VOLKSK_ATL = Sammlung(
        trace="Volksk. Atl.",
        groups="Auszübe|VolkskundeAtlas",
        sigle="ADV",
        description="Atlas der Deutschen Volkskunde. Hrsg. von H. Harmjanz u. E. Röhr. 6. Lief. Leipzig 1937—1940. N. F. hrsg. v. M. Zender. Marburg 1958 ff.",
    )
    WA_KARTE = Sammlung(
        trace="WA Karte",
        groups="Auszüge|WAKArte",
    )
    WAGENFELD = Sammlung(
        trace="Wagenfeld Volksmund",
        groups="Auszüge|Wagenfeld",
        sigle="Wagenf",
        description="Wagenfeld, K., Volksmund. Plattdeutsche Sprichwörter und Redensarten des Münsterlandes in ihrer Anwendung. Essen-Ruhr 1911",
        landschaft="Münsterl",
    )
    WAGENFELD_KK = Sammlung(
        trace="Wagenfeld Kiepenkerl",
        groups="Auszüge|WagenfeldKiepenkerl",
    )
    WAL_BH = Sammlung(
        trace="Wal/Bh S.|WalBh",
        groups="Auszüge|WalBh",
        kreis="Wal",
        ort="Bh",
    )
    WAL_RO = Sammlung(
        trace="Wal/Ro S.|WalRo",
        groups="Auszüge|WalRo",
        kreis="Wal",
        ort="Ro",
    )
    WALLMEYER = Sammlung(
        trace="Sos WM",
        groups="Auszüge|Wallmeyer",
        sigle="Wallm",
        description="Wallmeyer, F., Das Bauernhaus am mittleren Hellweg. Münster 1939 (Schriften d. Volkskundlichen Kommission im Provinzialinstitut f. westf. Landes- u. Volkskunde, hrsg. v. J. Trier u. K. Schulte Kemminghausen, H. 2)",
    )
    WALTER_SP = Sammlung(
        trace="Walter Sprichw.",
        groups="Auszüge|WalterSp",
        sigle="Walter",
        description="Walter, F., Plattdeutsche Sprichwörter und sprichwörtliche Redensarten aus der Stadt Recklinghausen. Recklinghausen 1896",
        kreis="Rek",
        ort="Rh",
    )
    WEDDIGEN = Sammlung(
        trace="Ravensberg|Weddigen|Weddingen",
        groups="Auszüge|Weddigen",
        kreis="Hal",
        ort="Ra",
    )
    WEIL_WB = Sammlung(
        trace="WeilWB",
        groups="Auszüge|WeilWb",
        kreis="Sth",
        ort="St",
    )
    WELLMANN = Sammlung(
        trace="Wellmann",
        groups="Auszüge|Wellmann",
        sigle="Wellm",
        description="Wellmann, H., Die Bauerschaft Mehringen a. d. Ems und Umgegend des Kirchspiels Emsbüren im Kreise Lingen (Ems). Ein Beitrag zur Heimatkunde. Lingen (Ems) 1934",
        kreis="Lin",
        ort="Mr",
    )
    WESTD_HEIMATK = Sammlung(
        trace="Westdeutsche Heimatkorrespondenz",
        groups="Auszüge|WestdeutscheHeimatkorrespondenz",
    )
    WESTPH_MAG = Sammlung(
        trace="Westph. Mag. H",
        groups="Auszüge|WestphMag",
        sigle="MagW",
        description="Westphälisches Magazin zur Geographie, Historie und Statistik, hrsg. v. P. F. Weddigen. 4 Bde. Bd. 1 Dessau-Leipzig 1784; Bd. 2 Bielefeld 1786; Bd. 3 u. 4 Bückeburg 1787, 1788",
    )
    WIEMERS = Sammlung(
        trace="Wiemers",
        groups="Auszüge|Wiemers",
        sigle="Wiemers",
        description="Wiemers, F., Heimatbuch des Amtes Wenden. Wenden o. J.",
    )
    WILMS = Sammlung(
        trace="Bocholt|Wilms",
        groups="Auszüge|Wilms",
        sigle="Wilms",
        description="Wilms, J., Bokeltse Dönkes. Sprichwörter, sprichwörtliche Redensarten und Dönkes in Bocholter Platt. Bocholt 21940",
        kreis="Bor",
        ort="Bh",
    )
    WITTKAMP = Sammlung(
        trace="Wittkamp",
        groups="Auszüge|Wittkamp",
        sigle="Wittk",
        description="Wittkamp, F., Heimatliche Sagen, Gebräuche und Geschichten aus dem Kreise Lüdinghausen. Lüdinghausen ²1922",
    )
    WM_WB = Sammlung(
        trace="WmWb; Elling/Piirainen",
        groups="Auszüge|WmWb",
        description="Westmünsterländisches Wörterbuch",
    )
    WML_BB = Sammlung(trace="W-münsterl. BüldB", groups="Auszüge|WmlBB")
    WOE = Sammlung(
        trace="Woe",
        groups="Auszüge|Woe",
    )
    WOESTE_GM = Sammlung(
        trace="WoeGM|WoeMG",
        groups="Auszüge|WoesteGM",
        sigle="WoeGM",
        description="Woeste, J. F. L., Volksüberlieferungen in der Grafschaft Mark nebst einem Glossar. Iserlohn 1848",
    )
    WOESTE_WB = Sammlung(
        trace="WoeN",
        groups="Auszüge|WoesteWb",
        sigle="WoeN",
        description="Woeste, F. (J. F. L.), Wörterbuch der westfälischen Mundart. Neu bearb. u. hrsg. v. E. Nörrenberg. Norden-Leipzig 1930. Nachdruck Wiesbaden 1966",
    )
    ZRHWV = Sammlung(
        trace="Z.rh.w.V.",
        groups="Auszüge|ZrhwV",
        sigle="ZrhwV",
        description="Zeitschrift des Vereins für rheinische und westfälische Volkskunde. Jg. 1—30 Elberfeld 1904 bis 1933; Jg. 31—33: Westdeutsche Zeitschrift für Volkskunde. Zeitschrift des Vereins ... Wuppertal-Elberfeld 1934—1936",
    )

    ##############################################################
    # Anonym
    ##############################################################
    ANON_AHS_AB = Sammlung(
        trace="Ahs Ab",
        groups="Wortschatz|Anonym|Ahs Ab",
        kreis="Ahs",
        ort="Ab",
    )
    ANON_AHS_AE = Sammlung(
        trace="Ahs Ae",
        groups="Wortschatz|Anonym|Ahs Ae",
        kreis="Ahs",
        ort="Ae",
    )
    ANON_AHS_AH = Sammlung(
        trace="Ahs Ah",
        groups="Wortschatz|Anonym|Ahs Ah",
        kreis="Ahs",
        ort="Ah",
    )
    ANON_AHS_AL = Sammlung(
        trace="Ahs Al",
        groups="Wortschatz|Anonym|Ahs Al",
        kreis="Ahs",
        ort="Al",
    )
    ANON_AHS_AM = Sammlung(
        trace="Ahs Am",
        groups="Wortschatz|Anonym|Ahs Am",
        kreis="Ahs",
        ort="Am",
    )
    ANON_AHS_AO = Sammlung(
        trace="Ahs Ao",
        groups="Wortschatz|Anonym|Ahs Ao",
        kreis="Ahs",
        ort="Ao",
    )
    ANON_AHS_AS = Sammlung(
        trace="Ahs As",
        groups="Wortschatz|Anonym|Ahs As",
        kreis="Ahs",
        ort="As",
    )
    ANON_AHS_DÖ = Sammlung(
        trace="Ahs Dö",
        groups="Wortschatz|Anonym|Ahs Dö",
        kreis="Ahs",
        ort="Dö",
    )
    ANON_AHS_EG = Sammlung(
        trace="Ahs Eg",
        groups="Wortschatz|Anonym|Ahs Eg",
        kreis="Ahs",
        ort="Eg",
    )
    ANON_AHS_EP = Sammlung(
        trace="Ahs Ep",
        groups="Wortschatz|Anonym|Ahs Ep",
        kreis="Ahs",
        ort="Ep",
    )
    ANON_AHS_ES = Sammlung(
        trace="Ahs Es",
        groups="Wortschatz|Anonym|Ahs Es",
        kreis="Ahs",
        ort="Es",
    )
    ANON_AHS_GE = Sammlung(
        trace="Ahs Ge",
        groups="Wortschatz|Anonym|Ahs Ge",
        kreis="Ahs",
        ort="Ge",
    )
    ANON_AHS_GM = Sammlung(
        trace="Ahs Gm",
        groups="Wortschatz|Anonym|Ahs Gm",
        kreis="Ahs",
        ort="Gm",
    )
    ANON_AHS_GR = Sammlung(
        trace="Ahs Gr",
        groups="Wortschatz|Anonym|Ahs Gr",
        kreis="Ahs",
        ort="Gr",
    )
    ANON_AHS_GS = Sammlung(
        trace="Ahs Gs",
        groups="Wortschatz|Anonym|Ahs Gs",
        kreis="Ahs",
        ort="Gs",
    )
    ANON_AHS_GX = Sammlung(
        trace="Ahs Gx",
        groups="Wortschatz|Anonym|Ahs Gx",
        kreis="Ahs",
        ort="Gx",
    )
    ANON_AHS_HE = Sammlung(
        trace="Ahs He",
        groups="Wortschatz|Anonym|Ahs He",
        kreis="Ahs",
        ort="He",
    )
    ANON_AHS_HG = Sammlung(
        trace="Ahs Hg",
        groups="Wortschatz|Anonym|Ahs Hg",
        kreis="Ahs",
        ort="Hg",
    )
    ANON_AHS_HO = Sammlung(
        trace="Ahs Ho",
        groups="Wortschatz|Anonym|Ahs Ho",
        kreis="Ahs",
        ort="Ho",
    )
    ANON_AHS_HW = Sammlung(
        trace="Ahs Hw",
        groups="Wortschatz|Anonym|Ahs Hw",
        kreis="Ahs",
        ort="Hw",
    )
    ANON_AHS_KM = Sammlung(
        trace="Ahs Km",
        groups="Wortschatz|Anonym|Ahs Km",
        kreis="Ahs",
        ort="Km",
    )
    ANON_AHS_KW = Sammlung(
        trace="Ahs Kw",
        groups="Wortschatz|Anonym|Ahs Kw",
        kreis="Ahs",
        ort="Kw",
    )
    ANON_AHS_LE = Sammlung(
        trace="Ahs Le",
        groups="Wortschatz|Anonym|Ahs Le",
        kreis="Ahs",
        ort="Le",
    )
    ANON_AHS_LÜ = Sammlung(
        trace="Ahs Lü",
        groups="Wortschatz|Anonym|Ahs Lü",
        kreis="Ahs",
        ort="Lü",
    )
    ANON_AHS_NB = Sammlung(
        trace="Ahs Nb",
        groups="Wortschatz|Anonym|Ahs Nb",
        kreis="Ahs",
        ort="Nb",
    )
    ANON_AHS_ÖD = Sammlung(
        trace="Ahs Öd",
        groups="Wortschatz|Anonym|Ahs Öd",
        kreis="Ahs",
        ort="Öd",
    )
    ANON_AHS_OT = Sammlung(
        trace="Ahs Ot",
        groups="Wortschatz|Anonym|Ahs Ot",
        kreis="Ahs",
        ort="Ot",
    )
    ANON_AHS_QU = Sammlung(
        trace="Ahs Qu",
        groups="Wortschatz|Anonym|Ahs Qu",
        kreis="Ahs",
        ort="Qu",
    )
    ANON_AHS_RB = Sammlung(
        trace="Ahs Rb",
        groups="Wortschatz|Anonym|Ahs Rb",
        kreis="Ahs",
        ort="Rb",
    )
    ANON_AHS_SC = Sammlung(
        trace="Ahs Sc",
        groups="Wortschatz|Anonym|Ahs Sc",
        kreis="Ahs",
        ort="Sc",
    )
    ANON_AHS_SL = Sammlung(
        trace="Ahs Sl",
        groups="Wortschatz|Anonym|Ahs Sl",
        kreis="Ahs",
        ort="Sl",
    )
    ANON_AHS_ST = Sammlung(
        trace="Ahs St",
        groups="Wortschatz|Anonym|Ahs St",
        kreis="Ahs",
        ort="St",
    )
    ANON_AHS_VR = Sammlung(
        trace="Ahs Vr",
        groups="Wortschatz|Anonym|Ahs Vr",
        kreis="Ahs",
        ort="Vr",
    )
    ANON_AHS_WD = Sammlung(
        trace="Ahs Wd",
        groups="Wortschatz|Anonym|Ahs Wd",
        kreis="Ahs",
        ort="Wd",
    )
    ANON_AHS_WE = Sammlung(
        trace="Ahs We",
        groups="Wortschatz|Anonym|Ahs We",
        kreis="Ahs",
        ort="We",
    )
    ANON_AHS_WF = Sammlung(
        trace="Ahs Wf",
        groups="Wortschatz|Anonym|Ahs Wf",
        kreis="Ahs",
        ort="Wf",
    )
    ANON_AHS_WG = Sammlung(
        trace="Ahs Wg",
        groups="Wortschatz|Anonym|Ahs Wg",
        kreis="Ahs",
        ort="Wg",
    )
    ANON_AHS_WR = Sammlung(
        trace="Ahs Wr",
        groups="Wortschatz|Anonym|Ahs Wr",
        kreis="Ahs",
        ort="Wr",
    )
    ANON_AHS_WÜ = Sammlung(
        trace="Ahs Wü",
        groups="Wortschatz|Anonym|Ahs Wü",
        kreis="Ahs",
        ort="Wü",
    )
    ANON_AHS_WW = Sammlung(
        trace="Ahs Ww",
        groups="Wortschatz|Anonym|Ahs Ww",
        kreis="Ahs",
        ort="Ww",
    )
    ANON_AHS_ZW = Sammlung(
        trace="Ahs Zw",
        groups="Wortschatz|Anonym|Ahs Zw",
        kreis="Ahs",
        ort="Zw",
    )
    ANON_ALT_AH = Sammlung(
        trace="Alt Ah",
        groups="Wortschatz|Anonym|Alt Ah",
        kreis="Alt",
        ort="Ah",
    )
    ANON_ALT_AL = Sammlung(
        trace="Alt Al",
        groups="Wortschatz|Anonym|Alt Al",
        kreis="Alt",
        ort="Al",
    )
    ANON_ALT_AM = Sammlung(
        trace="Alt Am",
        groups="Wortschatz|Anonym|Alt Am",
        kreis="Alt",
        ort="Am",
    )
    ANON_ALT_AN = Sammlung(
        trace="Alt An",
        groups="Wortschatz|Anonym|Alt An",
        kreis="Alt",
        ort="An",
    )
    ANON_ALT_AU = Sammlung(
        trace="Alt Au",
        groups="Wortschatz|Anonym|Alt Au",
        kreis="Alt",
        ort="Au",
    )
    ANON_ALT_BÄ = Sammlung(
        trace="Alt Bä",
        groups="Wortschatz|Anonym|Alt Bä",
        kreis="Alt",
        ort="Bä",
    )
    ANON_ALT_BB = Sammlung(
        trace="Alt Bb",
        groups="Wortschatz|Anonym|Alt Bb",
        kreis="Alt",
        ort="Bb",
    )
    ANON_ALT_BF = Sammlung(
        trace="Alt Bf",
        groups="Wortschatz|Anonym|Alt Bf",
        kreis="Alt",
        ort="Bf",
    )
    ANON_ALT_BG = Sammlung(
        trace="Alt Bg",
        groups="Wortschatz|Anonym|Alt Bg",
        kreis="Alt",
        ort="Bg",
    )
    ANON_ALT_BH = Sammlung(
        trace="Alt Bh",
        groups="Wortschatz|Anonym|Alt Bh",
        kreis="Alt",
        ort="Bh",
    )
    ANON_ALT_BL = Sammlung(
        trace="Alt Bl",
        groups="Wortschatz|Anonym|Alt Bl",
        kreis="Alt",
        ort="Bl",
    )
    ANON_ALT_BR = Sammlung(
        trace="Alt Br",
        groups="Wortschatz|Anonym|Alt Br",
        kreis="Alt",
        ort="Br",
    )
    ANON_ALT_BW = Sammlung(
        trace="Alt Bw",
        groups="Wortschatz|Anonym|Alt Bw",
        kreis="Alt",
        ort="Bw",
    )
    ANON_ALT_DA = Sammlung(
        trace="Alt Da",
        groups="Wortschatz|Anonym|Alt Da",
        kreis="Alt",
        ort="Da",
    )
    ANON_ALT_DB = Sammlung(
        trace="Alt Db",
        groups="Wortschatz|Anonym|Alt Db",
        kreis="Alt",
        ort="Db",
    )
    ANON_ALT_EB = Sammlung(
        trace="Alt Eb",
        groups="Wortschatz|Anonym|Alt Eb",
        kreis="Alt",
        ort="Eb",
    )
    ANON_ALT_EG = Sammlung(
        trace="Alt Eg",
        groups="Wortschatz|Anonym|Alt Eg",
        kreis="Alt",
        ort="Eg",
    )
    ANON_ALT_EI = Sammlung(
        trace="Alt Ei",
        groups="Wortschatz|Anonym|Alt Ei",
        kreis="Alt",
        ort="Ei",
    )
    ANON_ALT_ES = Sammlung(
        trace="Alt Es",
        groups="Wortschatz|Anonym|Alt Es",
        kreis="Alt",
        ort="Es",
    )
    ANON_ALT_EV = Sammlung(
        trace="Alt Ev",
        groups="Wortschatz|Anonym|Alt Ev",
        kreis="Alt",
        ort="Ev",
    )
    ANON_ALT_FR = Sammlung(
        trace="Alt Fr",
        groups="Wortschatz|Anonym|Alt Fr",
        kreis="Alt",
        ort="Fr",
    )
    ANON_ALT_GL = Sammlung(
        trace="Alt Gl",
        groups="Wortschatz|Anonym|Alt Gl",
        kreis="Alt",
        ort="Gl",
    )
    ANON_ALT_GR = Sammlung(
        trace="Alt Gr",
        groups="Wortschatz|Anonym|Alt Gr",
        kreis="Alt",
        ort="Gr",
    )
    ANON_ALT_HA = Sammlung(
        trace="Alt Ha",
        groups="Wortschatz|Anonym|Alt Ha",
        kreis="Alt",
        ort="Ha",
    )
    ANON_ALT_HB = Sammlung(
        trace="Alt Hb",
        groups="Wortschatz|Anonym|Alt Hb",
        kreis="Alt",
        ort="Hb",
    )
    ANON_ALT_HC = Sammlung(
        trace="Alt Hc",
        groups="Wortschatz|Anonym|Alt Hc",
        kreis="Alt",
        ort="Hc",
    )
    ANON_ALT_HD = Sammlung(
        trace="Alt Hd",
        groups="Wortschatz|Anonym|Alt Hd",
        kreis="Alt",
        ort="Hd",
    )
    ANON_ALT_HE = Sammlung(
        trace="Alt He",
        groups="Wortschatz|Anonym|Alt He",
        kreis="Alt",
        ort="He",
    )
    ANON_ALT_HF = Sammlung(
        trace="Alt Hf",
        groups="Wortschatz|Anonym|Alt Hf",
        kreis="Alt",
        ort="Hf",
    )
    ANON_ALT_HH = Sammlung(
        trace="Alt Hh",
        groups="Wortschatz|Anonym|Alt Hh",
        kreis="Alt",
        ort="Hh",
    )
    ANON_ALT_HI = Sammlung(
        trace="Alt Hi",
        groups="Wortschatz|Anonym|Alt Hi",
        kreis="Alt",
        ort="Hi",
    )
    ANON_ALT_HL = Sammlung(
        trace="Alt Hl",
        groups="Wortschatz|Anonym|Alt Hl",
        kreis="Alt",
        ort="Hl",
    )
    ANON_ALT_HR = Sammlung(
        trace="Alt Hr",
        groups="Wortschatz|Anonym|Alt Hr",
        kreis="Alt",
        ort="Hr",
    )
    ANON_ALT_HS = Sammlung(
        trace="Alt Hs",
        groups="Wortschatz|Anonym|Alt Hs",
        kreis="Alt",
        ort="Hs",
    )
    ANON_ALT_HÜ = Sammlung(
        trace="Alt Hü",
        groups="Wortschatz|Anonym|Alt Hü",
        kreis="Alt",
        ort="Hü",
    )
    ANON_ALT_HW = Sammlung(
        trace="Alt Hw",
        groups="Wortschatz|Anonym|Alt Hw",
        kreis="Alt",
        ort="Hw",
    )
    ANON_ALT_HX = Sammlung(
        trace="Alt Hx",
        groups="Wortschatz|Anonym|Alt Hx",
        kreis="Alt",
        ort="Hx",
    )
    ANON_ALT_IM = Sammlung(
        trace="Alt Im",
        groups="Wortschatz|Anonym|Alt Im",
        kreis="Alt",
        ort="Im",
    )
    ANON_ALT_IN = Sammlung(
        trace="Alt In",
        groups="Wortschatz|Anonym|Alt In",
        kreis="Alt",
        ort="In",
    )
    ANON_ALT_KI = Sammlung(
        trace="Alt Ki",
        groups="Wortschatz|Anonym|Alt Ki",
        kreis="Alt",
        ort="Ki",
    )
    ANON_ALT_KL = Sammlung(
        trace="Alt Kl",
        groups="Wortschatz|Anonym|Alt Kl",
        kreis="Alt",
        ort="Kl",
    )
    ANON_ALT_LE = Sammlung(
        trace="Alt Le",
        groups="Wortschatz|Anonym|Alt Le",
        kreis="Alt",
        ort="Le",
    )
    ANON_ALT_LL = Sammlung(
        trace="Alt Ll",
        groups="Wortschatz|Anonym|Alt Ll",
        kreis="Alt",
        ort="Ll",
    )
    ANON_ALT_LÖ = Sammlung(
        trace="Alt Lö",
        groups="Wortschatz|Anonym|Alt Lö",
        kreis="Alt",
        ort="Lö",
    )
    ANON_ALT_LS = Sammlung(
        trace="Alt Ls",
        groups="Wortschatz|Anonym|Alt Ls",
        kreis="Alt",
        ort="Ls",
    )
    ANON_ALT_LÜ = Sammlung(
        trace="Alt Lü",
        groups="Wortschatz|Anonym|Alt Lü",
        kreis="Alt",
        ort="Lü",
    )
    ANON_ALT_ME = Sammlung(
        trace="Alt Me",
        groups="Wortschatz|Anonym|Alt Me",
        kreis="Alt",
        ort="Me",
    )
    ANON_ALT_MH = Sammlung(
        trace="Alt Mh",
        groups="Wortschatz|Anonym|Alt Mh",
        kreis="Alt",
        ort="Mh",
    )
    ANON_ALT_MR = Sammlung(
        trace="Alt Mr",
        groups="Wortschatz|Anonym|Alt Mr",
        kreis="Alt",
        ort="Mr",
    )
    ANON_ALT_MS = Sammlung(
        trace="Alt Ms",
        groups="Wortschatz|Anonym|Alt Ms",
        kreis="Alt",
        ort="Ms",
    )
    ANON_ALT_NA = Sammlung(
        trace="Alt Na",
        groups="Wortschatz|Anonym|Alt Na",
        kreis="Alt",
        ort="Na",
    )
    ANON_ALT_NE = Sammlung(
        trace="Alt Ne",
        groups="Wortschatz|Anonym|Alt Ne",
        kreis="Alt",
        ort="Ne",
    )
    ANON_ALT_NH = Sammlung(
        trace="Alt Nh",
        groups="Wortschatz|Anonym|Alt Nh",
        kreis="Alt",
        ort="Nh",
    )
    ANON_ALT_NM = Sammlung(
        trace="Alt Nm",
        groups="Wortschatz|Anonym|Alt Nm",
        kreis="Alt",
        ort="Nm",
    )
    ANON_ALT_NR = Sammlung(
        trace="Alt Nr",
        groups="Wortschatz|Anonym|Alt Nr",
        kreis="Alt",
        ort="Nr",
    )
    ANON_ALT_NS = Sammlung(
        trace="Alt Ns",
        groups="Wortschatz|Anonym|Alt Ns",
        kreis="Alt",
        ort="Ns",
    )
    ANON_ALT_OB = Sammlung(
        trace="Alt Ob",
        groups="Wortschatz|Anonym|Alt Ob",
        kreis="Alt",
        ort="Ob",
    )
    ANON_ALT_OE = Sammlung(
        trace="Alt Oe",
        groups="Wortschatz|Anonym|Alt Oe",
        kreis="Alt",
        ort="Oe",
    )
    ANON_ALT_ÖH = Sammlung(
        trace="Alt Öh",
        groups="Wortschatz|Anonym|Alt Öh",
        kreis="Alt",
        ort="Öh",
    )
    ANON_ALT_OL = Sammlung(
        trace="Alt Ol",
        groups="Wortschatz|Anonym|Alt Ol",
        kreis="Alt",
        ort="Ol",
    )
    ANON_ALT_OR = Sammlung(
        trace="Alt Or",
        groups="Wortschatz|Anonym|Alt Or",
        kreis="Alt",
        ort="Or",
    )
    ANON_ALT_PB = Sammlung(
        trace="Alt Pb",
        groups="Wortschatz|Anonym|Alt Pb",
        kreis="Alt",
        ort="Pb",
    )
    ANON_ALT_PL = Sammlung(
        trace="Alt Pl",
        groups="Wortschatz|Anonym|Alt Pl",
        kreis="Alt",
        ort="Pl",
    )
    ANON_ALT_RÄ = Sammlung(
        trace="Alt Rä",
        groups="Wortschatz|Anonym|Alt Rä",
        kreis="Alt",
        ort="Rä",
    )
    ANON_ALT_RM = Sammlung(
        trace="Alt Rm",
        groups="Wortschatz|Anonym|Alt Rm",
        kreis="Alt",
        ort="Rm",
    )
    ANON_ALT_RÖ = Sammlung(
        trace="Alt Rö",
        groups="Wortschatz|Anonym|Alt Rö",
        kreis="Alt",
        ort="Rö",
    )
    ANON_ALT_RS = Sammlung(
        trace="Alt Rs",
        groups="Wortschatz|Anonym|Alt Rs",
        kreis="Alt",
        ort="Rs",
    )
    ANON_ALT_RW = Sammlung(
        trace="Alt Rw",
        groups="Wortschatz|Anonym|Alt Rw",
        kreis="Alt",
        ort="Rw",
    )
    ANON_ALT_SB = Sammlung(
        trace="Alt Sb",
        groups="Wortschatz|Anonym|Alt Sb",
        kreis="Alt",
        ort="Sb",
    )
    ANON_ALT_SC = Sammlung(
        trace="Alt Sc",
        groups="Wortschatz|Anonym|Alt Sc",
        kreis="Alt",
        ort="Sc",
    )
    ANON_ALT_SE = Sammlung(
        trace="Alt Se",
        groups="Wortschatz|Anonym|Alt Se",
        kreis="Alt",
        ort="Se",
    )
    ANON_ALT_SM = Sammlung(
        trace="Alt Sm",
        groups="Wortschatz|Anonym|Alt Sm",
        kreis="Alt",
        ort="Sm",
    )
    ANON_ALT_SR = Sammlung(
        trace="Alt Sr",
        groups="Wortschatz|Anonym|Alt Sr",
        kreis="Alt",
        ort="Sr",
    )
    ANON_ALT_SU = Sammlung(
        trace="Alt Su",
        groups="Wortschatz|Anonym|Alt Su",
        kreis="Alt",
        ort="Su",
    )
    ANON_ALT_SW = Sammlung(
        trace="Alt Sw",
        groups="Wortschatz|Anonym|Alt Sw",
        kreis="Alt",
        ort="Sw",
    )
    ANON_ALT_VA = Sammlung(
        trace="Alt Va",
        groups="Wortschatz|Anonym|Alt Va",
        kreis="Alt",
        ort="Va",
    )
    ANON_ALT_VE = Sammlung(
        trace="Alt Ve",
        groups="Wortschatz|Anonym|Alt Ve",
        kreis="Alt",
        ort="Ve",
    )
    ANON_ALT_VS = Sammlung(
        trace="Alt Vs",
        groups="Wortschatz|Anonym|Alt Vs",
        kreis="Alt",
        ort="Vs",
    )
    ANON_ALT_WD = Sammlung(
        trace="Alt Wd",
        groups="Wortschatz|Anonym|Alt Wd",
        kreis="Alt",
        ort="Wd",
    )
    ANON_ALT_WI = Sammlung(
        trace="Alt Wi",
        groups="Wortschatz|Anonym|Alt Wi",
        kreis="Alt",
        ort="Wi",
    )
    ANON_ALT_WW = Sammlung(
        trace="Alt Ww",
        groups="Wortschatz|Anonym|Alt Ww",
        kreis="Alt",
        ort="Ww",
    )
    ANON_ARN_AD = Sammlung(
        trace="Arn Ad",
        groups="Wortschatz|Anonym|Arn Ad",
        kreis="Arn",
        ort="Ad",
    )
    ANON_ARN_AF = Sammlung(
        trace="Arn Af",
        groups="Wortschatz|Anonym|Arn Af",
        kreis="Arn",
        ort="Af",
    )
    ANON_ARN_AH = Sammlung(
        trace="Arn Ah",
        groups="Wortschatz|Anonym|Arn Ah",
        kreis="Arn",
        ort="Ah",
    )
    ANON_ARN_AL = Sammlung(
        trace="Arn Al",
        groups="Wortschatz|Anonym|Arn Al",
        kreis="Arn",
        ort="Al",
    )
    ANON_ARN_AM = Sammlung(
        trace="Arn Am",
        groups="Wortschatz|Anonym|Arn Am",
        kreis="Arn",
        ort="Am",
    )
    ANON_ARN_AR = Sammlung(
        trace="Arn Ar",
        groups="Wortschatz|Anonym|Arn Ar",
        kreis="Arn",
        ort="Ar",
    )
    ANON_ARN_BA = Sammlung(
        trace="Arn Ba",
        groups="Wortschatz|Anonym|Arn Ba",
        kreis="Arn",
        ort="Ba",
    )
    ANON_ARN_BB = Sammlung(
        trace="Arn Bb",
        groups="Wortschatz|Anonym|Arn Bb",
        kreis="Arn",
        ort="Bb",
    )
    ANON_ARN_BE = Sammlung(
        trace="Arn Be",
        groups="Wortschatz|Anonym|Arn Be",
        kreis="Arn",
        ort="Be",
    )
    ANON_ARN_BH = Sammlung(
        trace="Arn Bh",
        groups="Wortschatz|Anonym|Arn Bh",
        kreis="Arn",
        ort="Bh",
    )
    ANON_ARN_BK = Sammlung(
        trace="Arn Bk",
        groups="Wortschatz|Anonym|Arn Bk",
        kreis="Arn",
        ort="Bk",
    )
    ANON_ARN_BL = Sammlung(
        trace="Arn Bl",
        groups="Wortschatz|Anonym|Arn Bl",
        kreis="Arn",
        ort="Bl",
    )
    ANON_ARN_BM = Sammlung(
        trace="Arn Bm",
        groups="Wortschatz|Anonym|Arn Bm",
        kreis="Arn",
        ort="Bm",
    )
    ANON_ARN_BR = Sammlung(
        trace="Arn Br",
        groups="Wortschatz|Anonym|Arn Br",
        kreis="Arn",
        ort="Br",
    )
    ANON_ARN_EB = Sammlung(
        trace="Arn Eb",
        groups="Wortschatz|Anonym|Arn Eb",
        kreis="Arn",
        ort="Eb",
    )
    ANON_ARN_EC = Sammlung(
        trace="Arn Ec",
        groups="Wortschatz|Anonym|Arn Ec",
        kreis="Arn",
        ort="Ec",
    )
    ANON_ARN_EH = Sammlung(
        trace="Arn Eh",
        groups="Wortschatz|Anonym|Arn Eh",
        kreis="Arn",
        ort="Eh",
    )
    ANON_ARN_EN = Sammlung(
        trace="Arn En",
        groups="Wortschatz|Anonym|Arn En",
        kreis="Arn",
        ort="En",
    )
    ANON_ARN_ES = Sammlung(
        trace="Arn Es",
        groups="Wortschatz|Anonym|Arn Es",
        kreis="Arn",
        ort="Es",
    )
    ANON_ARN_FR = Sammlung(
        trace="Arn Fr",
        groups="Wortschatz|Anonym|Arn Fr",
        kreis="Arn",
        ort="Fr",
    )
    ANON_ARN_GB = Sammlung(
        trace="Arn Gb",
        groups="Wortschatz|Anonym|Arn Gb",
        kreis="Arn",
        ort="Gb",
    )
    ANON_ARN_GR = Sammlung(
        trace="Arn Gr",
        groups="Wortschatz|Anonym|Arn Gr",
        kreis="Arn",
        ort="Gr",
    )
    ANON_ARN_HA = Sammlung(
        trace="Arn Ha",
        groups="Wortschatz|Anonym|Arn Ha",
        kreis="Arn",
        ort="Ha",
    )
    ANON_ARN_HB = Sammlung(
        trace="Arn Hb",
        groups="Wortschatz|Anonym|Arn Hb",
        kreis="Arn",
        ort="Hb",
    )
    ANON_ARN_HE = Sammlung(
        trace="Arn He",
        groups="Wortschatz|Anonym|Arn He",
        kreis="Arn",
        ort="He",
    )
    ANON_ARN_HF = Sammlung(
        trace="Arn Hf",
        groups="Wortschatz|Anonym|Arn Hf",
        kreis="Arn",
        ort="Hf",
    )
    ANON_ARN_HG = Sammlung(
        trace="Arn Hg",
        groups="Wortschatz|Anonym|Arn Hg",
        kreis="Arn",
        ort="Hg",
    )
    ANON_ARN_HÖ = Sammlung(
        trace="Arn Hö",
        groups="Wortschatz|Anonym|Arn Hö",
        kreis="Arn",
        ort="Hö",
    )
    ANON_ARN_HÜ = Sammlung(
        trace="Arn Hü",
        groups="Wortschatz|Anonym|Arn Hü",
        kreis="Arn",
        ort="Hü",
    )
    ANON_ARN_HZ = Sammlung(
        trace="Arn Hz",
        groups="Wortschatz|Anonym|Arn Hz",
        kreis="Arn",
        ort="Hz",
    )
    ANON_ARN_KÜ = Sammlung(
        trace="Arn Kü",
        groups="Wortschatz|Anonym|Arn Kü",
        kreis="Arn",
        ort="Kü",
    )
    ANON_ARN_LI = Sammlung(
        trace="Arn Li",
        groups="Wortschatz|Anonym|Arn Li",
        kreis="Arn",
        ort="Li",
    )
    ANON_ARN_LS = Sammlung(
        trace="Arn Ls",
        groups="Wortschatz|Anonym|Arn Ls",
        kreis="Arn",
        ort="Ls",
    )
    ANON_ARN_MB = Sammlung(
        trace="Arn Mb",
        groups="Wortschatz|Anonym|Arn Mb",
        kreis="Arn",
        ort="Mb",
    )
    ANON_ARN_ME = Sammlung(
        trace="Arn Me",
        groups="Wortschatz|Anonym|Arn Me",
        kreis="Arn",
        ort="Me",
    )
    ANON_ARN_MH = Sammlung(
        trace="Arn Mh",
        groups="Wortschatz|Anonym|Arn Mh",
        kreis="Arn",
        ort="Mh",
    )
    ANON_ARN_MÜ = Sammlung(
        trace="Arn Mü",
        groups="Wortschatz|Anonym|Arn Mü",
        kreis="Arn",
        ort="Mü",
    )
    ANON_ARN_NH = Sammlung(
        trace="Arn Nh",
        groups="Wortschatz|Anonym|Arn Nh",
        kreis="Arn",
        ort="Nh",
    )
    ANON_ARN_NI = Sammlung(
        trace="Arn Ni",
        groups="Wortschatz|Anonym|Arn Ni",
        kreis="Arn",
        ort="Ni",
    )
    ANON_ARN_NN = Sammlung(
        trace="Arn Nn",
        groups="Wortschatz|Anonym|Arn Nn",
        kreis="Arn",
        ort="Nn",
    )
    ANON_ARN_OB = Sammlung(
        trace="Arn Ob",
        groups="Wortschatz|Anonym|Arn Ob",
        kreis="Arn",
        ort="Ob",
    )
    ANON_ARN_ÖH = Sammlung(
        trace="Arn Öh",
        groups="Wortschatz|Anonym|Arn Öh",
        kreis="Arn",
        ort="Öh",
    )
    ANON_ARN_ÖL = Sammlung(
        trace="Arn Öl",
        groups="Wortschatz|Anonym|Arn Öl",
        kreis="Arn",
        ort="Öl",
    )
    ANON_ARN_ÖV = Sammlung(
        trace="Arn Öv",
        groups="Wortschatz|Anonym|Arn Öv",
        kreis="Arn",
        ort="Öv",
    )
    ANON_ARN_RB = Sammlung(
        trace="Arn Rb",
        groups="Wortschatz|Anonym|Arn Rb",
        kreis="Arn",
        ort="Rb",
    )
    ANON_ARN_SF = Sammlung(
        trace="Arn Sf",
        groups="Wortschatz|Anonym|Arn Sf",
        kreis="Arn",
        ort="Sf",
    )
    ANON_ARN_SI = Sammlung(
        trace="Arn Si",
        groups="Wortschatz|Anonym|Arn Si",
        kreis="Arn",
        ort="Si",
    )
    ANON_ARN_SM = Sammlung(
        trace="Arn Sm",
        groups="Wortschatz|Anonym|Arn Sm",
        kreis="Arn",
        ort="Sm",
    )
    ANON_ARN_ST = Sammlung(
        trace="Arn St",
        groups="Wortschatz|Anonym|Arn St",
        kreis="Arn",
        ort="St",
    )
    ANON_ARN_SU = Sammlung(
        trace="Arn Su",
        groups="Wortschatz|Anonym|Arn Su",
        kreis="Arn",
        ort="Su",
    )
    ANON_ARN_ÜT = Sammlung(
        trace="Arn Üt",
        groups="Wortschatz|Anonym|Arn Üt",
        kreis="Arn",
        ort="Üt",
    )
    ANON_ARN_VI = Sammlung(
        trace="Arn Vi",
        groups="Wortschatz|Anonym|Arn Vi",
        kreis="Arn",
        ort="Vi",
    )
    ANON_ARN_VO = Sammlung(
        trace="Arn Vo",
        groups="Wortschatz|Anonym|Arn Vo",
        kreis="Arn",
        ort="Vo",
    )
    ANON_ARN_VW = Sammlung(
        trace="Arn Vw",
        groups="Wortschatz|Anonym|Arn Vw",
        kreis="Arn",
        ort="Vw",
    )
    ANON_ARN_WA = Sammlung(
        trace="Arn Wa",
        groups="Wortschatz|Anonym|Arn Wa",
        kreis="Arn",
        ort="Wa",
    )
    ANON_ARN_WD = Sammlung(
        trace="Arn Wd",
        groups="Wortschatz|Anonym|Arn Wd",
        kreis="Arn",
        ort="Wd",
    )
    ANON_ARN_WE = Sammlung(
        trace="Arn We",
        groups="Wortschatz|Anonym|Arn We",
        kreis="Arn",
        ort="We",
    )
    ANON_ARN_WF = Sammlung(
        trace="Arn Wf",
        groups="Wortschatz|Anonym|Arn Wf",
        kreis="Arn",
        ort="Wf",
    )
    ANON_ARN_WH = Sammlung(
        trace="Arn Wh",
        groups="Wortschatz|Anonym|Arn Wh",
        kreis="Arn",
        ort="Wh",
    )
    ANON_ARN_WW = Sammlung(
        trace="Arn Ww",
        groups="Wortschatz|Anonym|Arn Ww",
        kreis="Arn",
        ort="Ww",
    )
    ANON_ASD_AD = Sammlung(
        trace="Asd Ad",
        groups="Wortschatz|Anonym|Asd Ad",
        kreis="Asd",
        ort="Ad",
    )
    ANON_ASD_AL = Sammlung(
        trace="Asd Al",
        groups="Wortschatz|Anonym|Asd Al",
        kreis="Asd",
        ort="Al",
    )
    ANON_ASD_BB = Sammlung(
        trace="Asd Bb",
        groups="Wortschatz|Anonym|Asd Bb",
        kreis="Asd",
        ort="Bb",
    )
    ANON_ASD_BC = Sammlung(
        trace="Asd Bc",
        groups="Wortschatz|Anonym|Asd Bc",
        kreis="Asd",
        ort="Bc",
    )
    ANON_ASD_BE = Sammlung(
        trace="Asd Be",
        groups="Wortschatz|Anonym|Asd Be",
        kreis="Asd",
        ort="Be",
    )
    ANON_ASD_BH = Sammlung(
        trace="Asd Bh",
        groups="Wortschatz|Anonym|Asd Bh",
        kreis="Asd",
        ort="Bh",
    )
    ANON_ASD_BK = Sammlung(
        trace="Asd Bk",
        groups="Wortschatz|Anonym|Asd Bk",
        kreis="Asd",
        ort="Bk",
    )
    ANON_ASD_BM = Sammlung(
        trace="Asd Bm",
        groups="Wortschatz|Anonym|Asd Bm",
        kreis="Asd",
        ort="Bm",
    )
    ANON_ASD_BO = Sammlung(
        trace="Asd Bo",
        groups="Wortschatz|Anonym|Asd Bo",
        kreis="Asd",
        ort="Bo",
    )
    ANON_ASD_BÖ = Sammlung(
        trace="Asd Bö",
        groups="Wortschatz|Anonym|Asd Bö",
        kreis="Asd",
        ort="Bö",
    )
    ANON_ASD_BR = Sammlung(
        trace="Asd Br",
        groups="Wortschatz|Anonym|Asd Br",
        kreis="Asd",
        ort="Br",
    )
    ANON_ASD_BW = Sammlung(
        trace="Asd Bw",
        groups="Wortschatz|Anonym|Asd Bw",
        kreis="Asd",
        ort="Bw",
    )
    ANON_ASD_DE = Sammlung(
        trace="Asd De",
        groups="Wortschatz|Anonym|Asd De",
        kreis="Asd",
        ort="De",
    )
    ANON_ASD_DÖ = Sammlung(
        trace="Asd Dö",
        groups="Wortschatz|Anonym|Asd Dö",
        kreis="Asd",
        ort="Dö",
    )
    ANON_ASD_DÜ = Sammlung(
        trace="Asd Dü",
        groups="Wortschatz|Anonym|Asd Dü",
        kreis="Asd",
        ort="Dü",
    )
    ANON_ASD_EI = Sammlung(
        trace="Asd Ei",
        groups="Wortschatz|Anonym|Asd Ei",
        kreis="Asd",
        ort="Ei",
    )
    ANON_ASD_ES = Sammlung(
        trace="Asd Es",
        groups="Wortschatz|Anonym|Asd Es",
        kreis="Asd",
        ort="Es",
    )
    ANON_ASD_FB = Sammlung(
        trace="Asd Fb",
        groups="Wortschatz|Anonym|Asd Fb",
        kreis="Asd",
        ort="Fb",
    )
    ANON_ASD_GB = Sammlung(
        trace="Asd Gb",
        groups="Wortschatz|Anonym|Asd Gb",
        kreis="Asd",
        ort="Gb",
    )
    ANON_ASD_HA = Sammlung(
        trace="Asd Ha",
        groups="Wortschatz|Anonym|Asd Ha",
        kreis="Asd",
        ort="Ha",
    )
    ANON_ASD_HB = Sammlung(
        trace="Asd Hb",
        groups="Wortschatz|Anonym|Asd Hb",
        kreis="Asd",
        ort="Hb",
    )
    ANON_ASD_HE = Sammlung(
        trace="Asd He",
        groups="Wortschatz|Anonym|Asd He",
        kreis="Asd",
        ort="He",
    )
    ANON_ASD_HI = Sammlung(
        trace="Asd Hi",
        groups="Wortschatz|Anonym|Asd Hi",
        kreis="Asd",
        ort="Hi",
    )
    ANON_ASD_HÜ = Sammlung(
        trace="Asd Hü",
        groups="Wortschatz|Anonym|Asd Hü",
        kreis="Asd",
        ort="Hü",
    )
    ANON_ASD_LA = Sammlung(
        trace="Asd La",
        groups="Wortschatz|Anonym|Asd La",
        kreis="Asd",
        ort="La",
    )
    ANON_ASD_LE = Sammlung(
        trace="Asd Le",
        groups="Wortschatz|Anonym|Asd Le",
        kreis="Asd",
        ort="Le",
    )
    ANON_ASD_LN = Sammlung(
        trace="Asd Ln",
        groups="Wortschatz|Anonym|Asd Ln",
        kreis="Asd",
        ort="Ln",
    )
    ANON_ASD_LO = Sammlung(
        trace="Asd Lo",
        groups="Wortschatz|Anonym|Asd Lo",
        kreis="Asd",
        ort="Lo",
    )
    ANON_ASD_ME = Sammlung(
        trace="Asd Me",
        groups="Wortschatz|Anonym|Asd Me",
        kreis="Asd",
        ort="Me",
    )
    ANON_ASD_NB = Sammlung(
        trace="Asd Nb",
        groups="Wortschatz|Anonym|Asd Nb",
        kreis="Asd",
        ort="Nb",
    )
    ANON_ASD_ND = Sammlung(
        trace="Asd Nd",
        groups="Wortschatz|Anonym|Asd Nd",
        kreis="Asd",
        ort="Nd",
    )
    ANON_ASD_NE = Sammlung(
        trace="Asd Ne",
        groups="Wortschatz|Anonym|Asd Ne",
        kreis="Asd",
        ort="Ne",
    )
    ANON_ASD_NH = Sammlung(
        trace="Asd Nh",
        groups="Wortschatz|Anonym|Asd Nh",
        kreis="Asd",
        ort="Nh",
    )
    ANON_ASD_NI = Sammlung(
        trace="Asd Ni",
        groups="Wortschatz|Anonym|Asd Ni",
        kreis="Asd",
        ort="Ni",
    )
    ANON_ASD_NL = Sammlung(
        trace="Asd Nl",
        groups="Wortschatz|Anonym|Asd Nl",
        kreis="Asd",
        ort="Nl",
    )
    ANON_ASD_NR = Sammlung(
        trace="Asd Nr",
        groups="Wortschatz|Anonym|Asd Nr",
        kreis="Asd",
        ort="Nr",
    )
    ANON_ASD_NS = Sammlung(
        trace="Asd Ns",
        groups="Wortschatz|Anonym|Asd Ns",
        kreis="Asd",
        ort="Ns",
    )
    ANON_ASD_NV = Sammlung(
        trace="Asd Nv",
        groups="Wortschatz|Anonym|Asd Nv",
        kreis="Asd",
        ort="Nv",
    )
    ANON_ASD_NW = Sammlung(
        trace="Asd Nw",
        groups="Wortschatz|Anonym|Asd Nw",
        kreis="Asd",
        ort="Nw",
    )
    ANON_ASD_OL = Sammlung(
        trace="Asd Ol",
        groups="Wortschatz|Anonym|Asd Ol",
        kreis="Asd",
        ort="Ol",
    )
    ANON_ASD_PB = Sammlung(
        trace="Asd Pb",
        groups="Wortschatz|Anonym|Asd Pb",
        kreis="Asd",
        ort="Pb",
    )
    ANON_ASD_RD = Sammlung(
        trace="Asd Rd",
        groups="Wortschatz|Anonym|Asd Rd",
        kreis="Asd",
        ort="Rd",
    )
    ANON_ASD_RH = Sammlung(
        trace="Asd Rh",
        groups="Wortschatz|Anonym|Asd Rh",
        kreis="Asd",
        ort="Rh",
    )
    ANON_ASD_SÖ = Sammlung(
        trace="Asd Sö",
        groups="Wortschatz|Anonym|Asd Sö",
        kreis="Asd",
        ort="Sö",
    )
    ANON_ASD_SP = Sammlung(
        trace="Asd Sp",
        groups="Wortschatz|Anonym|Asd Sp",
        kreis="Asd",
        ort="Sp",
    )
    ANON_ASD_ST = Sammlung(
        trace="Asd St",
        groups="Wortschatz|Anonym|Asd St",
        kreis="Asd",
        ort="St",
    )
    ANON_ASD_SU = Sammlung(
        trace="Asd Su",
        groups="Wortschatz|Anonym|Asd Su",
        kreis="Asd",
        ort="Su",
    )
    ANON_ASD_SW = Sammlung(
        trace="Asd Sw",
        groups="Wortschatz|Anonym|Asd Sw",
        kreis="Asd",
        ort="Sw",
    )
    ANON_ASD_TD = Sammlung(
        trace="Asd Td",
        groups="Wortschatz|Anonym|Asd Td",
        kreis="Asd",
        ort="Td",
    )
    ANON_ASD_VR = Sammlung(
        trace="Asd Vr",
        groups="Wortschatz|Anonym|Asd Vr",
        kreis="Asd",
        ort="Vr",
    )
    ANON_ASD_WA = Sammlung(
        trace="Asd Wa",
        groups="Wortschatz|Anonym|Asd Wa",
        kreis="Asd",
        ort="Wa",
    )
    ANON_ASD_WC = Sammlung(
        trace="Asd Wc",
        groups="Wortschatz|Anonym|Asd Wc",
        kreis="Asd",
        ort="Wc",
    )
    ANON_ASD_WE = Sammlung(
        trace="Asd We",
        groups="Wortschatz|Anonym|Asd We",
        kreis="Asd",
        ort="We",
    )
    ANON_ASD_WI = Sammlung(
        trace="Asd Wi",
        groups="Wortschatz|Anonym|Asd Wi",
        kreis="Asd",
        ort="Wi",
    )
    ANON_ASD_WL = Sammlung(
        trace="Asd Wl",
        groups="Wortschatz|Anonym|Asd Wl",
        kreis="Asd",
        ort="Wl",
    )
    ANON_ASD_WM = Sammlung(
        trace="Asd Wm",
        groups="Wortschatz|Anonym|Asd Wm",
        kreis="Asd",
        ort="Wm",
    )
    ANON_ASD_WS = Sammlung(
        trace="Asd Ws",
        groups="Wortschatz|Anonym|Asd Ws",
        kreis="Asd",
        ort="Ws",
    )
    ANON_BBR_AC = Sammlung(
        trace="Bbr Ac",
        groups="Wortschatz|Anonym|Bbr Ac",
        kreis="Bbr",
        ort="Ac",
    )
    ANON_BBR_AD = Sammlung(
        trace="Bbr Ad",
        groups="Wortschatz|Anonym|Bbr Ad",
        kreis="Bbr",
        ort="Ad",
    )
    ANON_BBR_AH = Sammlung(
        trace="Bbr Ah",
        groups="Wortschatz|Anonym|Bbr Ah",
        kreis="Bbr",
        ort="Ah",
    )
    ANON_BBR_AL = Sammlung(
        trace="Bbr Al",
        groups="Wortschatz|Anonym|Bbr Al",
        kreis="Bbr",
        ort="Al",
    )
    ANON_BBR_AN = Sammlung(
        trace="Bbr An",
        groups="Wortschatz|Anonym|Bbr An",
        kreis="Bbr",
        ort="An",
    )
    ANON_BBR_AS = Sammlung(
        trace="Bbr As",
        groups="Wortschatz|Anonym|Bbr As",
        kreis="Bbr",
        ort="As",
    )
    ANON_BBR_BA = Sammlung(
        trace="Bbr Ba",
        groups="Wortschatz|Anonym|Bbr Ba",
        kreis="Bbr",
        ort="Ba",
    )
    ANON_BBR_BE = Sammlung(
        trace="Bbr Be",
        groups="Wortschatz|Anonym|Bbr Be",
        kreis="Bbr",
        ort="Be",
    )
    ANON_BBR_BG = Sammlung(
        trace="Bbr Bg",
        groups="Wortschatz|Anonym|Bbr Bg",
        kreis="Bbr",
        ort="Bg",
    )
    ANON_BBR_BH = Sammlung(
        trace="Bbr Bh",
        groups="Wortschatz|Anonym|Bbr Bh",
        kreis="Bbr",
        ort="Bh",
    )
    ANON_BBR_BI = Sammlung(
        trace="Bbr Bi",
        groups="Wortschatz|Anonym|Bbr Bi",
        kreis="Bbr",
        ort="Bi",
    )
    ANON_BBR_BK = Sammlung(
        trace="Bbr Bk",
        groups="Wortschatz|Anonym|Bbr Bk",
        kreis="Bbr",
        ort="Bk",
    )
    ANON_BBR_BO = Sammlung(
        trace="Bbr Bo",
        groups="Wortschatz|Anonym|Bbr Bo",
        kreis="Bbr",
        ort="Bo",
    )
    ANON_BBR_BR = Sammlung(
        trace="Bbr Br",
        groups="Wortschatz|Anonym|Bbr Br",
        kreis="Bbr",
        ort="Br",
    )
    ANON_BBR_BS = Sammlung(
        trace="Bbr Bs",
        groups="Wortschatz|Anonym|Bbr Bs",
        kreis="Bbr",
        ort="Bs",
    )
    ANON_BBR_DA = Sammlung(
        trace="Bbr Da",
        groups="Wortschatz|Anonym|Bbr Da",
        kreis="Bbr",
        ort="Da",
    )
    ANON_BBR_DH = Sammlung(
        trace="Bbr Dh",
        groups="Wortschatz|Anonym|Bbr Dh",
        kreis="Bbr",
        ort="Dh",
    )
    ANON_BBR_EN = Sammlung(
        trace="Bbr En",
        groups="Wortschatz|Anonym|Bbr En",
        kreis="Bbr",
        ort="En",
    )
    ANON_BBR_EP = Sammlung(
        trace="Bbr Ep",
        groups="Wortschatz|Anonym|Bbr Ep",
        kreis="Bbr",
        ort="Ep",
    )
    ANON_BBR_ET = Sammlung(
        trace="Bbr Et",
        groups="Wortschatz|Anonym|Bbr Et",
        kreis="Bbr",
        ort="Et",
    )
    ANON_BBR_EV = Sammlung(
        trace="Bbr Ev",
        groups="Wortschatz|Anonym|Bbr Ev",
        kreis="Bbr",
        ort="Ev",
    )
    ANON_BBR_FA = Sammlung(
        trace="Bbr Fa",
        groups="Wortschatz|Anonym|Bbr Fa",
        kreis="Bbr",
        ort="Fa",
    )
    ANON_BBR_FÜ = Sammlung(
        trace="Bbr Fü",
        groups="Wortschatz|Anonym|Bbr Fü",
        kreis="Bbr",
        ort="Fü",
    )
    ANON_BBR_GD = Sammlung(
        trace="Bbr Gd",
        groups="Wortschatz|Anonym|Bbr Gd",
        kreis="Bbr",
        ort="Gd",
    )
    ANON_BBR_GE = Sammlung(
        trace="Bbr Ge",
        groups="Wortschatz|Anonym|Bbr Ge",
        kreis="Bbr",
        ort="Ge",
    )
    ANON_BBR_GF = Sammlung(
        trace="Bbr Gf",
        groups="Wortschatz|Anonym|Bbr Gf",
        kreis="Bbr",
        ort="Gf",
    )
    ANON_BBR_GL = Sammlung(
        trace="Bbr Gl",
        groups="Wortschatz|Anonym|Bbr Gl",
        kreis="Bbr",
        ort="Gl",
    )
    ANON_BBR_GM = Sammlung(
        trace="Bbr Gm",
        groups="Wortschatz|Anonym|Bbr Gm",
        kreis="Bbr",
        ort="Gm",
    )
    ANON_BBR_GR = Sammlung(
        trace="Bbr Gr",
        groups="Wortschatz|Anonym|Bbr Gr",
        kreis="Bbr",
        ort="Gr",
    )
    ANON_BBR_HA = Sammlung(
        trace="Bbr Ha",
        groups="Wortschatz|Anonym|Bbr Ha",
        kreis="Bbr",
        ort="Ha",
    )
    ANON_BBR_HE = Sammlung(
        trace="Bbr He",
        groups="Wortschatz|Anonym|Bbr He",
        kreis="Bbr",
        ort="He",
    )
    ANON_BBR_HK = Sammlung(
        trace="Bbr Hk",
        groups="Wortschatz|Anonym|Bbr Hk",
        kreis="Bbr",
        ort="Hk",
    )
    ANON_BBR_HL = Sammlung(
        trace="Bbr Hl",
        groups="Wortschatz|Anonym|Bbr Hl",
        kreis="Bbr",
        ort="Hl",
    )
    ANON_BBR_HM = Sammlung(
        trace="Bbr Hm",
        groups="Wortschatz|Anonym|Bbr Hm",
        kreis="Bbr",
        ort="Hm",
    )
    ANON_BBR_HÖ = Sammlung(
        trace="Bbr Hö",
        groups="Wortschatz|Anonym|Bbr Hö",
        kreis="Bbr",
        ort="Hö",
    )
    ANON_BBR_HP = Sammlung(
        trace="Bbr Hp",
        groups="Wortschatz|Anonym|Bbr Hp",
        kreis="Bbr",
        ort="Hp",
    )
    ANON_BBR_HR = Sammlung(
        trace="Bbr Hr",
        groups="Wortschatz|Anonym|Bbr Hr",
        kreis="Bbr",
        ort="Hr",
    )
    ANON_BBR_HS = Sammlung(
        trace="Bbr Hs",
        groups="Wortschatz|Anonym|Bbr Hs",
        kreis="Bbr",
        ort="Hs",
    )
    ANON_BBR_HX = Sammlung(
        trace="Bbr Hx",
        groups="Wortschatz|Anonym|Bbr Hx",
        kreis="Bbr",
        ort="Hx",
    )
    ANON_BBR_KA = Sammlung(
        trace="Bbr Ka",
        groups="Wortschatz|Anonym|Bbr Ka",
        kreis="Bbr",
        ort="Ka",
    )
    ANON_BBR_KB = Sammlung(
        trace="Bbr Kb",
        groups="Wortschatz|Anonym|Bbr Kb",
        kreis="Bbr",
        ort="Kb",
    )
    ANON_BBR_KK = Sammlung(
        trace="Bbr Kk",
        groups="Wortschatz|Anonym|Bbr Kk",
        kreis="Bbr",
        ort="Kk",
    )
    ANON_BBR_KM = Sammlung(
        trace="Bbr Km",
        groups="Wortschatz|Anonym|Bbr Km",
        kreis="Bbr",
        ort="Km",
    )
    ANON_BBR_LA = Sammlung(
        trace="Bbr La",
        groups="Wortschatz|Anonym|Bbr La",
        kreis="Bbr",
        ort="La",
    )
    ANON_BBR_LB = Sammlung(
        trace="Bbr Lb",
        groups="Wortschatz|Anonym|Bbr Lb",
        kreis="Bbr",
        ort="Lb",
    )
    ANON_BBR_LE = Sammlung(
        trace="Bbr Le",
        groups="Wortschatz|Anonym|Bbr Le",
        kreis="Bbr",
        ort="Le",
    )
    ANON_BBR_LI = Sammlung(
        trace="Bbr Li",
        groups="Wortschatz|Anonym|Bbr Li",
        kreis="Bbr",
        ort="Li",
    )
    ANON_BBR_LO = Sammlung(
        trace="Bbr Lo",
        groups="Wortschatz|Anonym|Bbr Lo",
        kreis="Bbr",
        ort="Lo",
    )
    ANON_BBR_LT = Sammlung(
        trace="Bbr Lt",
        groups="Wortschatz|Anonym|Bbr Lt",
        kreis="Bbr",
        ort="Lt",
    )
    ANON_BBR_ME = Sammlung(
        trace="Bbr Me",
        groups="Wortschatz|Anonym|Bbr Me",
        kreis="Bbr",
        ort="Me",
    )
    ANON_BBR_MZ = Sammlung(
        trace="Bbr Mz",
        groups="Wortschatz|Anonym|Bbr Mz",
        kreis="Bbr",
        ort="Mz",
    )
    ANON_BBR_NK = Sammlung(
        trace="Bbr Nk",
        groups="Wortschatz|Anonym|Bbr Nk",
        kreis="Bbr",
        ort="Nk",
    )
    ANON_BBR_NO = Sammlung(
        trace="Bbr No",
        groups="Wortschatz|Anonym|Bbr No",
        kreis="Bbr",
        ort="No",
    )
    ANON_BBR_OM = Sammlung(
        trace="Bbr Om",
        groups="Wortschatz|Anonym|Bbr Om",
        kreis="Bbr",
        ort="Om",
    )
    ANON_BBR_OR = Sammlung(
        trace="Bbr Or",
        groups="Wortschatz|Anonym|Bbr Or",
        kreis="Bbr",
        ort="Or",
    )
    ANON_BBR_PL = Sammlung(
        trace="Bbr Pl",
        groups="Wortschatz|Anonym|Bbr Pl",
        kreis="Bbr",
        ort="Pl",
    )
    ANON_BBR_PR = Sammlung(
        trace="Bbr Pr",
        groups="Wortschatz|Anonym|Bbr Pr",
        kreis="Bbr",
        ort="Pr",
    )
    ANON_BBR_QU = Sammlung(
        trace="Bbr Qu",
        groups="Wortschatz|Anonym|Bbr Qu",
        kreis="Bbr",
        ort="Qu",
    )
    ANON_BBR_RE = Sammlung(
        trace="Bbr Re",
        groups="Wortschatz|Anonym|Bbr Re",
        kreis="Bbr",
        ort="Re",
    )
    ANON_BBR_RF = Sammlung(
        trace="Bbr Rf",
        groups="Wortschatz|Anonym|Bbr Rf",
        kreis="Bbr",
        ort="Rf",
    )
    ANON_BBR_RH = Sammlung(
        trace="Bbr Rh",
        groups="Wortschatz|Anonym|Bbr Rh",
        kreis="Bbr",
        ort="Rh",
    )
    ANON_BBR_RI = Sammlung(
        trace="Bbr Ri",
        groups="Wortschatz|Anonym|Bbr Ri",
        kreis="Bbr",
        ort="Ri",
    )
    ANON_BBR_RL = Sammlung(
        trace="Bbr Rl",
        groups="Wortschatz|Anonym|Bbr Rl",
        kreis="Bbr",
        ort="Rl",
    )
    ANON_BBR_RÜ = Sammlung(
        trace="Bbr Rü",
        groups="Wortschatz|Anonym|Bbr Rü",
        kreis="Bbr",
        ort="Rü",
    )
    ANON_BBR_SE = Sammlung(
        trace="Bbr Se",
        groups="Wortschatz|Anonym|Bbr Se",
        kreis="Bbr",
        ort="Se",
    )
    ANON_BBR_SL = Sammlung(
        trace="Bbr Sl",
        groups="Wortschatz|Anonym|Bbr Sl",
        kreis="Bbr",
        ort="Sl",
    )
    ANON_BBR_SM = Sammlung(
        trace="Bbr Sm",
        groups="Wortschatz|Anonym|Bbr Sm",
        kreis="Bbr",
        ort="Sm",
    )
    ANON_BBR_SÖ = Sammlung(
        trace="Bbr Sö",
        groups="Wortschatz|Anonym|Bbr Sö",
        kreis="Bbr",
        ort="Sö",
    )
    ANON_BBR_SU = Sammlung(
        trace="Bbr Su",
        groups="Wortschatz|Anonym|Bbr Su",
        kreis="Bbr",
        ort="Su",
    )
    ANON_BBR_SW = Sammlung(
        trace="Bbr Sw",
        groups="Wortschatz|Anonym|Bbr Sw",
        kreis="Bbr",
        ort="Sw",
    )
    ANON_BBR_TA = Sammlung(
        trace="Bbr Ta",
        groups="Wortschatz|Anonym|Bbr Ta",
        kreis="Bbr",
        ort="Ta",
    )
    ANON_BBR_ÜF = Sammlung(
        trace="Bbr Üf",
        groups="Wortschatz|Anonym|Bbr Üf",
        kreis="Bbr",
        ort="Üf",
    )
    ANON_BBR_VC = Sammlung(
        trace="Bbr Vc",
        groups="Wortschatz|Anonym|Bbr Vc",
        kreis="Bbr",
        ort="Vc",
    )
    ANON_BBR_VE = Sammlung(
        trace="Bbr Ve",
        groups="Wortschatz|Anonym|Bbr Ve",
        kreis="Bbr",
        ort="Ve",
    )
    ANON_BBR_VI = Sammlung(
        trace="Bbr Vi",
        groups="Wortschatz|Anonym|Bbr Vi",
        kreis="Bbr",
        ort="Vi",
    )
    ANON_BBR_VO = Sammlung(
        trace="Bbr Vo",
        groups="Wortschatz|Anonym|Bbr Vo",
        kreis="Bbr",
        ort="Vo",
    )
    ANON_BBR_VÖ = Sammlung(
        trace="Bbr Vö",
        groups="Wortschatz|Anonym|Bbr Vö",
        kreis="Bbr",
        ort="Vö",
    )
    ANON_BBR_WB = Sammlung(
        trace="Bbr Wb",
        groups="Wortschatz|Anonym|Bbr Wb",
        kreis="Bbr",
        ort="Wb",
    )
    ANON_BBR_WE = Sammlung(
        trace="Bbr We",
        groups="Wortschatz|Anonym|Bbr We",
        kreis="Bbr",
        ort="We",
    )
    ANON_BBR_WH = Sammlung(
        trace="Bbr Wh",
        groups="Wortschatz|Anonym|Bbr Wh",
        kreis="Bbr",
        ort="Wh",
    )
    ANON_BBR_WS = Sammlung(
        trace="Bbr Ws",
        groups="Wortschatz|Anonym|Bbr Ws",
        kreis="Bbr",
        ort="Ws",
    )
    ANON_BBR_WU = Sammlung(
        trace="Bbr Wu",
        groups="Wortschatz|Anonym|Bbr Wu",
        kreis="Bbr",
        ort="Wu",
    )
    ANON_BBR_WW = Sammlung(
        trace="Bbr Ww",
        groups="Wortschatz|Anonym|Bbr Ww",
        kreis="Bbr",
        ort="Ww",
    )
    ANON_BCH_AB = Sammlung(
        trace="Bch Ab",
        groups="Wortschatz|Anonym|Bch Ab",
        kreis="Bch",
        ort="Ab",
    )
    ANON_BCH_BO = Sammlung(
        trace="Bch Bo",
        groups="Wortschatz|Anonym|Bch Bo",
        kreis="Bch",
        ort="Bo",
    )
    ANON_BCH_BÖ = Sammlung(
        trace="Bch Bö",
        groups="Wortschatz|Anonym|Bch Bö",
        kreis="Bch",
        ort="Bö",
    )
    ANON_BCH_BR = Sammlung(
        trace="Bch Br",
        groups="Wortschatz|Anonym|Bch Br",
        kreis="Bch",
        ort="Br",
    )
    ANON_BCH_GE = Sammlung(
        trace="Bch Ge",
        groups="Wortschatz|Anonym|Bch Ge",
        kreis="Bch",
        ort="Ge",
    )
    ANON_BCH_HA = Sammlung(
        trace="Bch Ha",
        groups="Wortschatz|Anonym|Bch Ha",
        kreis="Bch",
        ort="Ha",
    )
    ANON_BCH_HE = Sammlung(
        trace="Bch He",
        groups="Wortschatz|Anonym|Bch He",
        kreis="Bch",
        ort="He",
    )
    ANON_BCH_HI = Sammlung(
        trace="Bch Hi",
        groups="Wortschatz|Anonym|Bch Hi",
        kreis="Bch",
        ort="Hi",
    )
    ANON_BCH_HO = Sammlung(
        trace="Bch Ho",
        groups="Wortschatz|Anonym|Bch Ho",
        kreis="Bch",
        ort="Ho",
    )
    ANON_BCH_HP = Sammlung(
        trace="Bch Hp",
        groups="Wortschatz|Anonym|Bch Hp",
        kreis="Bch",
        ort="Hp",
    )
    ANON_BCH_LD = Sammlung(
        trace="Bch Ld",
        groups="Wortschatz|Anonym|Bch Ld",
        kreis="Bch",
        ort="Ld",
    )
    ANON_BCH_LD1 = Sammlung(
        trace="Bch Ld1",
        groups="Wortschatz|Anonym|Bch Ld1",
        kreis="Bch",
        ort="Ld1",
    )
    ANON_BCH_LI = Sammlung(
        trace="Bch Li",
        groups="Wortschatz|Anonym|Bch Li",
        kreis="Bch",
        ort="Li",
    )
    ANON_BCH_LR = Sammlung(
        trace="Bch Lr",
        groups="Wortschatz|Anonym|Bch Lr",
        kreis="Bch",
        ort="Lr",
    )
    ANON_BCH_LT = Sammlung(
        trace="Bch Lt",
        groups="Wortschatz|Anonym|Bch Lt",
        kreis="Bch",
        ort="Lt",
    )
    ANON_BCH_SE = Sammlung(
        trace="Bch Se",
        groups="Wortschatz|Anonym|Bch Se",
        kreis="Bch",
        ort="Se",
    )
    ANON_BCH_SO = Sammlung(
        trace="Bch So",
        groups="Wortschatz|Anonym|Bch So",
        kreis="Bch",
        ort="So",
    )
    ANON_BCH_SP = Sammlung(
        trace="Bch Sp",
        groups="Wortschatz|Anonym|Bch Sp",
        kreis="Bch",
        ort="Sp",
    )
    ANON_BCH_ST = Sammlung(
        trace="Bch St",
        groups="Wortschatz|Anonym|Bch St",
        kreis="Bch",
        ort="St",
    )
    ANON_BCH_ST1 = Sammlung(
        trace="Bch St1",
        groups="Wortschatz|Anonym|Bch St1",
        kreis="Bch",
        ort="St1",
    )
    ANON_BCH_WA = Sammlung(
        trace="Bch Wa",
        groups="Wortschatz|Anonym|Bch Wa",
        kreis="Bch",
        ort="Wa",
    )
    ANON_BCH_WE = Sammlung(
        trace="Bch We",
        groups="Wortschatz|Anonym|Bch We",
        kreis="Bch",
        ort="We",
    )
    ANON_BCH_WT = Sammlung(
        trace="Bch Wt",
        groups="Wortschatz|Anonym|Bch Wt",
        kreis="Bch",
        ort="Wt",
    )
    ANON_BEK_AA = Sammlung(
        trace="Bek Aa",
        groups="Wortschatz|Anonym|Bek Aa",
        kreis="Bek",
        ort="Aa",
    )
    ANON_BEK_AC = Sammlung(
        trace="Bek Ac",
        groups="Wortschatz|Anonym|Bek Ac",
        kreis="Bek",
        ort="Ac",
    )
    ANON_BEK_AL = Sammlung(
        trace="Bek Al",
        groups="Wortschatz|Anonym|Bek Al",
        kreis="Bek",
        ort="Al",
    )
    ANON_BEK_BB = Sammlung(
        trace="Bek Bb",
        groups="Wortschatz|Anonym|Bek Bb",
        kreis="Bek",
        ort="Bb",
    )
    ANON_BEK_BE = Sammlung(
        trace="Bek Be",
        groups="Wortschatz|Anonym|Bek Be",
        kreis="Bek",
        ort="Be",
    )
    ANON_BEK_BF = Sammlung(
        trace="Bek Bf",
        groups="Wortschatz|Anonym|Bek Bf",
        kreis="Bek",
        ort="Bf",
    )
    ANON_BEK_BK = Sammlung(
        trace="Bek Bk",
        groups="Wortschatz|Anonym|Bek Bk",
        kreis="Bek",
        ort="Bk",
    )
    ANON_BEK_DB = Sammlung(
        trace="Bek Db",
        groups="Wortschatz|Anonym|Bek Db",
        kreis="Bek",
        ort="Db",
    )
    ANON_BEK_DI = Sammlung(
        trace="Bek Di",
        groups="Wortschatz|Anonym|Bek Di",
        kreis="Bek",
        ort="Di",
    )
    ANON_BEK_EK = Sammlung(
        trace="Bek Ek",
        groups="Wortschatz|Anonym|Bek Ek",
        kreis="Bek",
        ort="Ek",
    )
    ANON_BEK_EL = Sammlung(
        trace="Bek El",
        groups="Wortschatz|Anonym|Bek El",
        kreis="Bek",
        ort="El",
    )
    ANON_BEK_EN = Sammlung(
        trace="Bek En",
        groups="Wortschatz|Anonym|Bek En",
        kreis="Bek",
        ort="En",
    )
    ANON_BEK_GÖ = Sammlung(
        trace="Bek Gö",
        groups="Wortschatz|Anonym|Bek Gö",
        kreis="Bek",
        ort="Gö",
    )
    ANON_BEK_HE = Sammlung(
        trace="Bek He",
        groups="Wortschatz|Anonym|Bek He",
        kreis="Bek",
        ort="He",
    )
    ANON_BEK_HF = Sammlung(
        trace="Bek Hf",
        groups="Wortschatz|Anonym|Bek Hf",
        kreis="Bek",
        ort="Hf",
    )
    ANON_BEK_HI = Sammlung(
        trace="Bek Hi",
        groups="Wortschatz|Anonym|Bek Hi",
        kreis="Bek",
        ort="Hi",
    )
    ANON_BEK_HO = Sammlung(
        trace="Bek Ho",
        groups="Wortschatz|Anonym|Bek Ho",
        kreis="Bek",
        ort="Ho",
    )
    ANON_BEK_KE = Sammlung(
        trace="Bek Ke",
        groups="Wortschatz|Anonym|Bek Ke",
        kreis="Bek",
        ort="Ke",
    )
    ANON_BEK_LB = Sammlung(
        trace="Bek Lb",
        groups="Wortschatz|Anonym|Bek Lb",
        kreis="Bek",
        ort="Lb",
    )
    ANON_BEK_LI = Sammlung(
        trace="Bek Li",
        groups="Wortschatz|Anonym|Bek Li",
        kreis="Bek",
        ort="Li",
    )
    ANON_BEK_NB = Sammlung(
        trace="Bek Nb",
        groups="Wortschatz|Anonym|Bek Nb",
        kreis="Bek",
        ort="Nb",
    )
    ANON_BEK_ÖL = Sammlung(
        trace="Bek Öl",
        groups="Wortschatz|Anonym|Bek Öl",
        kreis="Bek",
        ort="Öl",
    )
    ANON_BEK_ÖS = Sammlung(
        trace="Bek Ös",
        groups="Wortschatz|Anonym|Bek Ös",
        kreis="Bek",
        ort="Ös",
    )
    ANON_BEK_SH = Sammlung(
        trace="Bek Sh",
        groups="Wortschatz|Anonym|Bek Sh",
        kreis="Bek",
        ort="Sh",
    )
    ANON_BEK_ST = Sammlung(
        trace="Bek St",
        groups="Wortschatz|Anonym|Bek St",
        kreis="Bek",
        ort="St",
    )
    ANON_BEK_SÜ = Sammlung(
        trace="Bek Sü",
        groups="Wortschatz|Anonym|Bek Sü",
        kreis="Bek",
        ort="Sü",
    )
    ANON_BEK_VE = Sammlung(
        trace="Bek Ve",
        groups="Wortschatz|Anonym|Bek Ve",
        kreis="Bek",
        ort="Ve",
    )
    ANON_BEK_VH = Sammlung(
        trace="Bek Vh",
        groups="Wortschatz|Anonym|Bek Vh",
        kreis="Bek",
        ort="Vh",
    )
    ANON_BEK_WL = Sammlung(
        trace="Bek Wl",
        groups="Wortschatz|Anonym|Bek Wl",
        kreis="Bek",
        ort="Wl",
    )
    ANON_BEN_AD = Sammlung(
        trace="Ben Ad",
        groups="Wortschatz|Anonym|Ben Ad",
        kreis="Ben",
        ort="Ad",
    )
    ANON_BEN_AL = Sammlung(
        trace="Ben Al",
        groups="Wortschatz|Anonym|Ben Al",
        kreis="Ben",
        ort="Al",
    )
    ANON_BEN_AP = Sammlung(
        trace="Ben Ap",
        groups="Wortschatz|Anonym|Ben Ap",
        kreis="Ben",
        ort="Ap",
    )
    ANON_BEN_AW = Sammlung(
        trace="Ben Aw",
        groups="Wortschatz|Anonym|Ben Aw",
        kreis="Ben",
        ort="Aw",
    )
    ANON_BEN_BA = Sammlung(
        trace="Ben Ba",
        groups="Wortschatz|Anonym|Ben Ba",
        kreis="Ben",
        ort="Ba",
    )
    ANON_BEN_BG = Sammlung(
        trace="Ben Bg",
        groups="Wortschatz|Anonym|Ben Bg",
        kreis="Ben",
        ort="Bg",
    )
    ANON_BEN_BH = Sammlung(
        trace="Ben Bh",
        groups="Wortschatz|Anonym|Ben Bh",
        kreis="Ben",
        ort="Bh",
    )
    ANON_BEN_BI = Sammlung(
        trace="Ben Bi",
        groups="Wortschatz|Anonym|Ben Bi",
        kreis="Ben",
        ort="Bi",
    )
    ANON_BEN_BM = Sammlung(
        trace="Ben Bm",
        groups="Wortschatz|Anonym|Ben Bm",
        kreis="Ben",
        ort="Bm",
    )
    ANON_BEN_BN = Sammlung(
        trace="Ben Bn",
        groups="Wortschatz|Anonym|Ben Bn",
        kreis="Ben",
        ort="Bn",
    )
    ANON_BEN_BR = Sammlung(
        trace="Ben Br",
        groups="Wortschatz|Anonym|Ben Br",
        kreis="Ben",
        ort="Br",
    )
    ANON_BEN_DR = Sammlung(
        trace="Ben Dr",
        groups="Wortschatz|Anonym|Ben Dr",
        kreis="Ben",
        ort="Dr",
    )
    ANON_BEN_EC = Sammlung(
        trace="Ben Ec",
        groups="Wortschatz|Anonym|Ben Ec",
        kreis="Ben",
        ort="Ec",
    )
    ANON_BEN_EG = Sammlung(
        trace="Ben Eg",
        groups="Wortschatz|Anonym|Ben Eg",
        kreis="Ben",
        ort="Eg",
    )
    ANON_BEN_EH = Sammlung(
        trace="Ben Eh",
        groups="Wortschatz|Anonym|Ben Eh",
        kreis="Ben",
        ort="Eh",
    )
    ANON_BEN_EM = Sammlung(
        trace="Ben Em",
        groups="Wortschatz|Anonym|Ben Em",
        kreis="Ben",
        ort="Em",
    )
    ANON_BEN_EN = Sammlung(
        trace="Ben En",
        groups="Wortschatz|Anonym|Ben En",
        kreis="Ben",
        ort="En",
    )
    ANON_BEN_ES = Sammlung(
        trace="Ben Es",
        groups="Wortschatz|Anonym|Ben Es",
        kreis="Ben",
        ort="Es",
    )
    ANON_BEN_EW = Sammlung(
        trace="Ben Ew",
        groups="Wortschatz|Anonym|Ben Ew",
        kreis="Ben",
        ort="Ew",
    )
    ANON_BEN_FH = Sammlung(
        trace="Ben Fh",
        groups="Wortschatz|Anonym|Ben Fh",
        kreis="Ben",
        ort="Fh",
    )
    ANON_BEN_GD = Sammlung(
        trace="Ben Gd",
        groups="Wortschatz|Anonym|Ben Gd",
        kreis="Ben",
        ort="Gd",
    )
    ANON_BEN_GE = Sammlung(
        trace="Ben Ge",
        groups="Wortschatz|Anonym|Ben Ge",
        kreis="Ben",
        ort="Ge",
    )
    ANON_BEN_GH = Sammlung(
        trace="Ben Gh",
        groups="Wortschatz|Anonym|Ben Gh",
        kreis="Ben",
        ort="Gh",
    )
    ANON_BEN_GK = Sammlung(
        trace="Ben Gk",
        groups="Wortschatz|Anonym|Ben Gk",
        kreis="Ben",
        ort="Gk",
    )
    ANON_BEN_GM = Sammlung(
        trace="Ben Gm",
        groups="Wortschatz|Anonym|Ben Gm",
        kreis="Ben",
        ort="Gm",
    )
    ANON_BEN_GR = Sammlung(
        trace="Ben Gr",
        groups="Wortschatz|Anonym|Ben Gr",
        kreis="Ben",
        ort="Gr",
    )
    ANON_BEN_GS = Sammlung(
        trace="Ben Gs",
        groups="Wortschatz|Anonym|Ben Gs",
        kreis="Ben",
        ort="Gs",
    )
    ANON_BEN_HA = Sammlung(
        trace="Ben Ha",
        groups="Wortschatz|Anonym|Ben Ha",
        kreis="Ben",
        ort="Ha",
    )
    ANON_BEN_HE = Sammlung(
        trace="Ben He",
        groups="Wortschatz|Anonym|Ben He",
        kreis="Ben",
        ort="He",
    )
    ANON_BEN_HF = Sammlung(
        trace="Ben Hf",
        groups="Wortschatz|Anonym|Ben Hf",
        kreis="Ben",
        ort="Hf",
    )
    ANON_BEN_HH = Sammlung(
        trace="Ben Hh",
        groups="Wortschatz|Anonym|Ben Hh",
        kreis="Ben",
        ort="Hh",
    )
    ANON_BEN_HI = Sammlung(
        trace="Ben Hi",
        groups="Wortschatz|Anonym|Ben Hi",
        kreis="Ben",
        ort="Hi",
    )
    ANON_BEN_HK = Sammlung(
        trace="Ben Hk",
        groups="Wortschatz|Anonym|Ben Hk",
        kreis="Ben",
        ort="Hk",
    )
    ANON_BEN_HL = Sammlung(
        trace="Ben Hl",
        groups="Wortschatz|Anonym|Ben Hl",
        kreis="Ben",
        ort="Hl",
    )
    ANON_BEN_HO = Sammlung(
        trace="Ben Ho",
        groups="Wortschatz|Anonym|Ben Ho",
        kreis="Ben",
        ort="Ho",
    )
    ANON_BEN_HÖ = Sammlung(
        trace="Ben Hö",
        groups="Wortschatz|Anonym|Ben Hö",
        kreis="Ben",
        ort="Hö",
    )
    ANON_BEN_HP = Sammlung(
        trace="Ben Hp",
        groups="Wortschatz|Anonym|Ben Hp",
        kreis="Ben",
        ort="Hp",
    )
    ANON_BEN_IT = Sammlung(
        trace="Ben It",
        groups="Wortschatz|Anonym|Ben It",
        kreis="Ben",
        ort="It",
    )
    ANON_BEN_KA = Sammlung(
        trace="Ben Ka",
        groups="Wortschatz|Anonym|Ben Ka",
        kreis="Ben",
        ort="Ka",
    )
    ANON_BEN_LA = Sammlung(
        trace="Ben La",
        groups="Wortschatz|Anonym|Ben La",
        kreis="Ben",
        ort="La",
    )
    ANON_BEN_LR = Sammlung(
        trace="Ben Lr",
        groups="Wortschatz|Anonym|Ben Lr",
        kreis="Ben",
        ort="Lr",
    )
    ANON_BEN_NG = Sammlung(
        trace="Ben Ng",
        groups="Wortschatz|Anonym|Ben Ng",
        kreis="Ben",
        ort="Ng",
    )
    ANON_BEN_NH = Sammlung(
        trace="Ben Nh",
        groups="Wortschatz|Anonym|Ben Nh",
        kreis="Ben",
        ort="Nh",
    )
    ANON_BEN_NL = Sammlung(
        trace="Ben Nl",
        groups="Wortschatz|Anonym|Ben Nl",
        kreis="Ben",
        ort="Nl",
    )
    ANON_BEN_NO = Sammlung(
        trace="Ben No",
        groups="Wortschatz|Anonym|Ben No",
        kreis="Ben",
        ort="No",
    )
    ANON_BEN_NR = Sammlung(
        trace="Ben Nr",
        groups="Wortschatz|Anonym|Ben Nr",
        kreis="Ben",
        ort="Nr",
    )
    ANON_BEN_OG = Sammlung(
        trace="Ben Og",
        groups="Wortschatz|Anonym|Ben Og",
        kreis="Ben",
        ort="Og",
    )
    ANON_BEN_ON = Sammlung(
        trace="Ben On",
        groups="Wortschatz|Anonym|Ben On",
        kreis="Ben",
        ort="On",
    )
    ANON_BEN_OW = Sammlung(
        trace="Ben Ow",
        groups="Wortschatz|Anonym|Ben Ow",
        kreis="Ben",
        ort="Ow",
    )
    ANON_BEN_QD = Sammlung(
        trace="Ben Qd",
        groups="Wortschatz|Anonym|Ben Qd",
        kreis="Ben",
        ort="Qd",
    )
    ANON_BEN_RA = Sammlung(
        trace="Ben Ra",
        groups="Wortschatz|Anonym|Ben Ra",
        kreis="Ben",
        ort="Ra",
    )
    ANON_BEN_SA = Sammlung(
        trace="Ben Sa",
        groups="Wortschatz|Anonym|Ben Sa",
        kreis="Ben",
        ort="Sa",
    )
    ANON_BEN_SC = Sammlung(
        trace="Ben Sc",
        groups="Wortschatz|Anonym|Ben Sc",
        kreis="Ben",
        ort="Sc",
    )
    ANON_BEN_SH = Sammlung(
        trace="Ben Sh",
        groups="Wortschatz|Anonym|Ben Sh",
        kreis="Ben",
        ort="Sh",
    )
    ANON_BEN_SI = Sammlung(
        trace="Ben Si",
        groups="Wortschatz|Anonym|Ben Si",
        kreis="Ben",
        ort="Si",
    )
    ANON_BEN_SU = Sammlung(
        trace="Ben Su",
        groups="Wortschatz|Anonym|Ben Su",
        kreis="Ben",
        ort="Su",
    )
    ANON_BEN_TH = Sammlung(
        trace="Ben Th",
        groups="Wortschatz|Anonym|Ben Th",
        kreis="Ben",
        ort="Th",
    )
    ANON_BEN_ÜL = Sammlung(
        trace="Ben Ül",
        groups="Wortschatz|Anonym|Ben Ül",
        kreis="Ben",
        ort="Ül",
    )
    ANON_BEN_VH = Sammlung(
        trace="Ben Vh",
        groups="Wortschatz|Anonym|Ben Vh",
        kreis="Ben",
        ort="Vh",
    )
    ANON_BEN_VW = Sammlung(
        trace="Ben Vw",
        groups="Wortschatz|Anonym|Ben Vw",
        kreis="Ben",
        ort="Vw",
    )
    ANON_BEN_WA = Sammlung(
        trace="Ben Wa",
        groups="Wortschatz|Anonym|Ben Wa",
        kreis="Ben",
        ort="Wa",
    )
    ANON_BEN_WI = Sammlung(
        trace="Ben Wi",
        groups="Wortschatz|Anonym|Ben Wi",
        kreis="Ben",
        ort="Wi",
    )
    ANON_BEN_WM = Sammlung(
        trace="Ben Wm",
        groups="Wortschatz|Anonym|Ben Wm",
        kreis="Ben",
        ort="Wm",
    )
    ANON_BEN_WS = Sammlung(
        trace="Ben Ws",
        groups="Wortschatz|Anonym|Ben Ws",
        kreis="Ben",
        ort="Ws",
    )
    ANON_BEN_WT = Sammlung(
        trace="Ben Wt",
        groups="Wortschatz|Anonym|Ben Wt",
        kreis="Ben",
        ort="Wt",
    )
    ANON_BIE_AH = Sammlung(
        trace="Bie Ah",
        groups="Wortschatz|Anonym|Bie Ah",
        kreis="Bie",
        ort="Ah",
    )
    ANON_BIE_BA = Sammlung(
        trace="Bie Ba",
        groups="Wortschatz|Anonym|Bie Ba",
        kreis="Bie",
        ort="Ba",
    )
    ANON_BIE_BE = Sammlung(
        trace="Bie Be",
        groups="Wortschatz|Anonym|Bie Be",
        kreis="Bie",
        ort="Be",
    )
    ANON_BIE_BF = Sammlung(
        trace="Bie Bf",
        groups="Wortschatz|Anonym|Bie Bf",
        kreis="Bie",
        ort="Bf",
    )
    ANON_BIE_BH = Sammlung(
        trace="Bie Bh",
        groups="Wortschatz|Anonym|Bie Bh",
        kreis="Bie",
        ort="Bh",
    )
    ANON_BIE_BR = Sammlung(
        trace="Bie Br",
        groups="Wortschatz|Anonym|Bie Br",
        kreis="Bie",
        ort="Br",
    )
    ANON_BIE_BW = Sammlung(
        trace="Bie Bw",
        groups="Wortschatz|Anonym|Bie Bw",
        kreis="Bie",
        ort="Bw",
    )
    ANON_BIE_DB = Sammlung(
        trace="Bie Db",
        groups="Wortschatz|Anonym|Bie Db",
        kreis="Bie",
        ort="Db",
    )
    ANON_BIE_DD = Sammlung(
        trace="Bie Dd",
        groups="Wortschatz|Anonym|Bie Dd",
        kreis="Bie",
        ort="Dd",
    )
    ANON_BIE_EB = Sammlung(
        trace="Bie Eb",
        groups="Wortschatz|Anonym|Bie Eb",
        kreis="Bie",
        ort="Eb",
    )
    ANON_BIE_GB = Sammlung(
        trace="Bie Gb",
        groups="Wortschatz|Anonym|Bie Gb",
        kreis="Bie",
        ort="Gb",
    )
    ANON_BIE_GH = Sammlung(
        trace="Bie Gh",
        groups="Wortschatz|Anonym|Bie Gh",
        kreis="Bie",
        ort="Gh",
    )
    ANON_BIE_GR = Sammlung(
        trace="Bie Gr",
        groups="Wortschatz|Anonym|Bie Gr",
        kreis="Bie",
        ort="Gr",
    )
    ANON_BIE_HB = Sammlung(
        trace="Bie Hb",
        groups="Wortschatz|Anonym|Bie Hb",
        kreis="Bie",
        ort="Hb",
    )
    ANON_BIE_HE = Sammlung(
        trace="Bie He",
        groups="Wortschatz|Anonym|Bie He",
        kreis="Bie",
        ort="He",
    )
    ANON_BIE_HI = Sammlung(
        trace="Bie Hi",
        groups="Wortschatz|Anonym|Bie Hi",
        kreis="Bie",
        ort="Hi",
    )
    ANON_BIE_HK = Sammlung(
        trace="Bie Hk",
        groups="Wortschatz|Anonym|Bie Hk",
        kreis="Bie",
        ort="Hk",
    )
    ANON_BIE_HO = Sammlung(
        trace="Bie Ho",
        groups="Wortschatz|Anonym|Bie Ho",
        kreis="Bie",
        ort="Ho",
    )
    ANON_BIE_JÖ = Sammlung(
        trace="Bie Jö",
        groups="Wortschatz|Anonym|Bie Jö",
        kreis="Bie",
        ort="Jö",
    )
    ANON_BIE_IS = Sammlung(
        trace="Bie Is",
        groups="Wortschatz|Anonym|Bie Is",
        kreis="Bie",
        ort="Is",
    )
    ANON_BIE_KD = Sammlung(
        trace="Bie Kd",
        groups="Wortschatz|Anonym|Bie Kd",
        kreis="Bie",
        ort="Kd",
    )
    ANON_BIE_LH = Sammlung(
        trace="Bie Lh",
        groups="Wortschatz|Anonym|Bie Lh",
        kreis="Bie",
        ort="Lh",
    )
    ANON_BIE_MI = Sammlung(
        trace="Bie Mi",
        groups="Wortschatz|Anonym|Bie Mi",
        kreis="Bie",
        ort="Mi",
    )
    ANON_BIE_ND = Sammlung(
        trace="Bie Nd",
        groups="Wortschatz|Anonym|Bie Nd",
        kreis="Bie",
        ort="Nd",
    )
    ANON_BIE_NH = Sammlung(
        trace="Bie Nh",
        groups="Wortschatz|Anonym|Bie Nh",
        kreis="Bie",
        ort="Nh",
    )
    ANON_BIE_NI = Sammlung(
        trace="Bie Ni",
        groups="Wortschatz|Anonym|Bie Ni",
        kreis="Bie",
        ort="Ni",
    )
    ANON_BIE_NJ = Sammlung(
        trace="Bie Nj",
        groups="Wortschatz|Anonym|Bie Nj",
        kreis="Bie",
        ort="Nj",
    )
    ANON_BIE_OJ = Sammlung(
        trace="Bie Oj",
        groups="Wortschatz|Anonym|Bie Oj",
        kreis="Bie",
        ort="Oj",
    )
    ANON_BIE_OT = Sammlung(
        trace="Bie Ot",
        groups="Wortschatz|Anonym|Bie Ot",
        kreis="Bie",
        ort="Ot",
    )
    ANON_BIE_QU = Sammlung(
        trace="Bie Qu",
        groups="Wortschatz|Anonym|Bie Qu",
        kreis="Bie",
        ort="Qu",
    )
    ANON_BIE_SC = Sammlung(
        trace="Bie Sc",
        groups="Wortschatz|Anonym|Bie Sc",
        kreis="Bie",
        ort="Sc",
    )
    ANON_BIE_SE = Sammlung(
        trace="Bie Se",
        groups="Wortschatz|Anonym|Bie Se",
        kreis="Bie",
        ort="Se",
    )
    ANON_BIE_SI = Sammlung(
        trace="Bie Si",
        groups="Wortschatz|Anonym|Bie Si",
        kreis="Bie",
        ort="Si",
    )
    ANON_BIE_ST = Sammlung(
        trace="Bie St",
        groups="Wortschatz|Anonym|Bie St",
        kreis="Bie",
        ort="St",
    )
    ANON_BIE_SZ = Sammlung(
        trace="Bie Sz",
        groups="Wortschatz|Anonym|Bie Sz",
        kreis="Bie",
        ort="Sz",
    )
    ANON_BIE_TH = Sammlung(
        trace="Bie Th",
        groups="Wortschatz|Anonym|Bie Th",
        kreis="Bie",
        ort="Th",
    )
    ANON_BIE_UD = Sammlung(
        trace="Bie Ud",
        groups="Wortschatz|Anonym|Bie Ud",
        kreis="Bie",
        ort="Ud",
    )
    ANON_BIE_UT = Sammlung(
        trace="Bie Ut",
        groups="Wortschatz|Anonym|Bie Ut",
        kreis="Bie",
        ort="Ut",
    )
    ANON_BIE_VD = Sammlung(
        trace="Bie Vd",
        groups="Wortschatz|Anonym|Bie Vd",
        kreis="Bie",
        ort="Vd",
    )
    ANON_BIE_VS = Sammlung(
        trace="Bie Vs",
        groups="Wortschatz|Anonym|Bie Vs",
        kreis="Bie",
        ort="Vs",
    )
    ANON_BOR_AN = Sammlung(
        trace="Bor An",
        groups="Wortschatz|Anonym|Bor An",
        kreis="Bor",
        ort="An",
    )
    ANON_BOR_BA = Sammlung(
        trace="Bor Ba",
        groups="Wortschatz|Anonym|Bor Ba",
        kreis="Bor",
        ort="Ba",
    )
    ANON_BOR_BE = Sammlung(
        trace="Bor Be",
        groups="Wortschatz|Anonym|Bor Be",
        kreis="Bor",
        ort="Be",
    )
    ANON_BOR_BH = Sammlung(
        trace="Bor Bh",
        groups="Wortschatz|Anonym|Bor Bh",
        kreis="Bor",
        ort="Bh",
    )
    ANON_BOR_BI = Sammlung(
        trace="Bor Bi",
        groups="Wortschatz|Anonym|Bor Bi",
        kreis="Bor",
        ort="Bi",
    )
    ANON_BOR_BO = Sammlung(
        trace="Bor Bo",
        groups="Wortschatz|Anonym|Bor Bo",
        kreis="Bor",
        ort="Bo",
    )
    ANON_BOR_BÜ = Sammlung(
        trace="Bor Bü",
        groups="Wortschatz|Anonym|Bor Bü",
        kreis="Bor",
        ort="Bü",
    )
    ANON_BOR_BW = Sammlung(
        trace="Bor Bw",
        groups="Wortschatz|Anonym|Bor Bw",
        kreis="Bor",
        ort="Bw",
    )
    ANON_BOR_DI = Sammlung(
        trace="Bor Di",
        groups="Wortschatz|Anonym|Bor Di",
        kreis="Bor",
        ort="Di",
    )
    ANON_BOR_GE = Sammlung(
        trace="Bor Ge",
        groups="Wortschatz|Anonym|Bor Ge",
        kreis="Bor",
        ort="Ge",
    )
    ANON_BOR_GL = Sammlung(
        trace="Bor Gl",
        groups="Wortschatz|Anonym|Bor Gl",
        kreis="Bor",
        ort="Gl",
    )
    ANON_BOR_GR = Sammlung(
        trace="Bor Gr",
        groups="Wortschatz|Anonym|Bor Gr",
        kreis="Bor",
        ort="Gr",
    )
    ANON_BOR_GW = Sammlung(
        trace="Bor Gw",
        groups="Wortschatz|Anonym|Bor Gw",
        kreis="Bor",
        ort="Gw",
    )
    ANON_BOR_HD = Sammlung(
        trace="Bor Hd",
        groups="Wortschatz|Anonym|Bor Hd",
        kreis="Bor",
        ort="Hd",
    )
    ANON_BOR_HE = Sammlung(
        trace="Bor He",
        groups="Wortschatz|Anonym|Bor He",
        kreis="Bor",
        ort="He",
    )
    ANON_BOR_HF = Sammlung(
        trace="Bor Hf",
        groups="Wortschatz|Anonym|Bor Hf",
        kreis="Bor",
        ort="Hf",
    )
    ANON_BOR_HL = Sammlung(
        trace="Bor Hl",
        groups="Wortschatz|Anonym|Bor Hl",
        kreis="Bor",
        ort="Hl",
    )
    ANON_BOR_HO = Sammlung(
        trace="Bor Ho",
        groups="Wortschatz|Anonym|Bor Ho",
        kreis="Bor",
        ort="Ho",
    )
    ANON_BOR_HÜ = Sammlung(
        trace="Bor Hü",
        groups="Wortschatz|Anonym|Bor Hü",
        kreis="Bor",
        ort="Hü",
    )
    ANON_BOR_HW = Sammlung(
        trace="Bor Hw",
        groups="Wortschatz|Anonym|Bor Hw",
        kreis="Bor",
        ort="Hw",
    )
    ANON_BOR_KG = Sammlung(
        trace="Bor Kg",
        groups="Wortschatz|Anonym|Bor Kg",
        kreis="Bor",
        ort="Kg",
    )
    ANON_BOR_KL = Sammlung(
        trace="Bor Kl",
        groups="Wortschatz|Anonym|Bor Kl",
        kreis="Bor",
        ort="Kl",
    )
    ANON_BOR_KR = Sammlung(
        trace="Bor Kr",
        groups="Wortschatz|Anonym|Bor Kr",
        kreis="Bor",
        ort="Kr",
    )
    ANON_BOR_KT = Sammlung(
        trace="Bor Kt",
        groups="Wortschatz|Anonym|Bor Kt",
        kreis="Bor",
        ort="Kt",
    )
    ANON_BOR_LI = Sammlung(
        trace="Bor Li",
        groups="Wortschatz|Anonym|Bor Li",
        kreis="Bor",
        ort="Li",
    )
    ANON_BOR_LO = Sammlung(
        trace="Bor Lo",
        groups="Wortschatz|Anonym|Bor Lo",
        kreis="Bor",
        ort="Lo",
    )
    ANON_BOR_MB = Sammlung(
        trace="Bor Mb",
        groups="Wortschatz|Anonym|Bor Mb",
        kreis="Bor",
        ort="Mb",
    )
    ANON_BOR_MU = Sammlung(
        trace="Bor Mu",
        groups="Wortschatz|Anonym|Bor Mu",
        kreis="Bor",
        ort="Mu",
    )
    ANON_BOR_MV = Sammlung(
        trace="Bor Mv",
        groups="Wortschatz|Anonym|Bor Mv",
        kreis="Bor",
        ort="Mv",
    )
    ANON_BOR_NB = Sammlung(
        trace="Bor Nb",
        groups="Wortschatz|Anonym|Bor Nb",
        kreis="Bor",
        ort="Nb",
    )
    ANON_BOR_ND = Sammlung(
        trace="Bor Nd",
        groups="Wortschatz|Anonym|Bor Nd",
        kreis="Bor",
        ort="Nd",
    )
    ANON_BOR_NV = Sammlung(
        trace="Bor Nv",
        groups="Wortschatz|Anonym|Bor Nv",
        kreis="Bor",
        ort="Nv",
    )
    ANON_BOR_PH = Sammlung(
        trace="Bor Ph",
        groups="Wortschatz|Anonym|Bor Ph",
        kreis="Bor",
        ort="Ph",
    )
    ANON_BOR_RB = Sammlung(
        trace="Bor Rb",
        groups="Wortschatz|Anonym|Bor Rb",
        kreis="Bor",
        ort="Rb",
    )
    ANON_BOR_RD = Sammlung(
        trace="Bor Rd",
        groups="Wortschatz|Anonym|Bor Rd",
        kreis="Bor",
        ort="Rd",
    )
    ANON_BOR_RF = Sammlung(
        trace="Bor Rf",
        groups="Wortschatz|Anonym|Bor Rf",
        kreis="Bor",
        ort="Rf",
    )
    ANON_BOR_RH = Sammlung(
        trace="Bor Rh",
        groups="Wortschatz|Anonym|Bor Rh",
        kreis="Bor",
        ort="Rh",
    )
    ANON_BOR_RK = Sammlung(
        trace="Bor Rk",
        groups="Wortschatz|Anonym|Bor Rk",
        kreis="Bor",
        ort="Rk",
    )
    ANON_BOR_SP = Sammlung(
        trace="Bor Sp",
        groups="Wortschatz|Anonym|Bor Sp",
        kreis="Bor",
        ort="Sp",
    )
    ANON_BOR_SS = Sammlung(
        trace="Bor Ss",
        groups="Wortschatz|Anonym|Bor Ss",
        kreis="Bor",
        ort="Ss",
    )
    ANON_BOR_SU = Sammlung(
        trace="Bor Su",
        groups="Wortschatz|Anonym|Bor Su",
        kreis="Bor",
        ort="Su",
    )
    ANON_BOR_VE = Sammlung(
        trace="Bor Ve",
        groups="Wortschatz|Anonym|Bor Ve",
        kreis="Bor",
        ort="Ve",
    )
    ANON_BOR_VH = Sammlung(
        trace="Bor Vh",
        groups="Wortschatz|Anonym|Bor Vh",
        kreis="Bor",
        ort="Vh",
    )
    ANON_BOR_WE = Sammlung(
        trace="Bor We",
        groups="Wortschatz|Anonym|Bor We",
        kreis="Bor",
        ort="We",
    )
    ANON_BOR_WS = Sammlung(
        trace="Bor Ws",
        groups="Wortschatz|Anonym|Bor Ws",
        kreis="Bor",
        ort="Ws",
    )
    ANON_BRG_HE = Sammlung(
        trace="Brg He",
        groups="Wortschatz|Anonym|Brg He",
        kreis="Brg",
        ort="He",
    )
    ANON_BRG_HW = Sammlung(
        trace="Brg Hw",
        groups="Wortschatz|Anonym|Brg Hw",
        kreis="Brg",
        ort="Hw",
    )
    ANON_BRG_LF = Sammlung(
        trace="Brg Lf",
        groups="Wortschatz|Anonym|Brg Lf",
        kreis="Brg",
        ort="Lf",
    )
    ANON_BRG_NB = Sammlung(
        trace="Brg Nb",
        groups="Wortschatz|Anonym|Brg Nb",
        kreis="Brg",
        ort="Nb",
    )
    ANON_BRG_RW = Sammlung(
        trace="Brg Rw",
        groups="Wortschatz|Anonym|Brg Rw",
        kreis="Brg",
        ort="Rw",
    )
    ANON_BRG_WS = Sammlung(
        trace="Brg Ws",
        groups="Wortschatz|Anonym|Brg Ws",
        kreis="Brg",
        ort="Ws",
    )
    ANON_BRI_AA = Sammlung(
        trace="Bri Aa",
        groups="Wortschatz|Anonym|Bri Aa",
        kreis="Bri",
        ort="Aa",
    )
    ANON_BRI_AB = Sammlung(
        trace="Bri Ab",
        groups="Wortschatz|Anonym|Bri Ab",
        kreis="Bri",
        ort="Ab",
    )
    ANON_BRI_AF = Sammlung(
        trace="Bri Af",
        groups="Wortschatz|Anonym|Bri Af",
        kreis="Bri",
        ort="Af",
    )
    ANON_BRI_AH = Sammlung(
        trace="Bri Ah",
        groups="Wortschatz|Anonym|Bri Ah",
        kreis="Bri",
        ort="Ah",
    )
    ANON_BRI_AL = Sammlung(
        trace="Bri Al",
        groups="Wortschatz|Anonym|Bri Al",
        kreis="Bri",
        ort="Al",
    )
    ANON_BRI_BE = Sammlung(
        trace="Bri Be",
        groups="Wortschatz|Anonym|Bri Be",
        kreis="Bri",
        ort="Be",
    )
    ANON_BRI_BH = Sammlung(
        trace="Bri Bh",
        groups="Wortschatz|Anonym|Bri Bh",
        kreis="Bri",
        ort="Bh",
    )
    ANON_BRI_BI = Sammlung(
        trace="Bri Bi",
        groups="Wortschatz|Anonym|Bri Bi",
        kreis="Bri",
        ort="Bi",
    )
    ANON_BRI_BK = Sammlung(
        trace="Bri Bk",
        groups="Wortschatz|Anonym|Bri Bk",
        kreis="Bri",
        ort="Bk",
    )
    ANON_BRI_BO = Sammlung(
        trace="Bri Bo",
        groups="Wortschatz|Anonym|Bri Bo",
        kreis="Bri",
        ort="Bo",
    )
    ANON_BRI_BR = Sammlung(
        trace="Bri Br",
        groups="Wortschatz|Anonym|Bri Br",
        kreis="Bri",
        ort="Br",
    )
    ANON_BRI_DF = Sammlung(
        trace="Bri Df",
        groups="Wortschatz|Anonym|Bri Df",
        kreis="Bri",
        ort="Df",
    )
    ANON_BRI_DR = Sammlung(
        trace="Bri Dr",
        groups="Wortschatz|Anonym|Bri Dr",
        kreis="Bri",
        ort="Dr",
    )
    ANON_BRI_DÜ = Sammlung(
        trace="Bri Dü",
        groups="Wortschatz|Anonym|Bri Dü",
        kreis="Bri",
        ort="Dü",
    )
    ANON_BRI_EH = Sammlung(
        trace="Bri Eh",
        groups="Wortschatz|Anonym|Bri Eh",
        kreis="Bri",
        ort="Eh",
    )
    ANON_BRI_EL = Sammlung(
        trace="Bri El",
        groups="Wortschatz|Anonym|Bri El",
        kreis="Bri",
        ort="El",
    )
    ANON_BRI_EP = Sammlung(
        trace="Bri Ep",
        groups="Wortschatz|Anonym|Bri Ep",
        kreis="Bri",
        ort="Ep",
    )
    ANON_BRI_ER = Sammlung(
        trace="Bri Er",
        groups="Wortschatz|Anonym|Bri Er",
        kreis="Bri",
        ort="Er",
    )
    ANON_BRI_ES = Sammlung(
        trace="Bri Es",
        groups="Wortschatz|Anonym|Bri Es",
        kreis="Bri",
        ort="Es",
    )
    ANON_BRI_GB = Sammlung(
        trace="Bri Gb",
        groups="Wortschatz|Anonym|Bri Gb",
        kreis="Bri",
        ort="Gb",
    )
    ANON_BRI_GH = Sammlung(
        trace="Bri Gh",
        groups="Wortschatz|Anonym|Bri Gh",
        kreis="Bri",
        ort="Gh",
    )
    ANON_BRI_HA = Sammlung(
        trace="Bri Ha",
        groups="Wortschatz|Anonym|Bri Ha",
        kreis="Bri",
        ort="Ha",
    )
    ANON_BRI_HE = Sammlung(
        trace="Bri He",
        groups="Wortschatz|Anonym|Bri He",
        kreis="Bri",
        ort="He",
    )
    ANON_BRI_HF = Sammlung(
        trace="Bri Hf",
        groups="Wortschatz|Anonym|Bri Hf",
        kreis="Bri",
        ort="Hf",
    )
    ANON_BRI_HH = Sammlung(
        trace="Bri Hh",
        groups="Wortschatz|Anonym|Bri Hh",
        kreis="Bri",
        ort="Hh",
    )
    ANON_BRI_HL = Sammlung(
        trace="Bri Hl",
        groups="Wortschatz|Anonym|Bri Hl",
        kreis="Bri",
        ort="Hl",
    )
    ANON_BRI_HO = Sammlung(
        trace="Bri Ho",
        groups="Wortschatz|Anonym|Bri Ho",
        kreis="Bri",
        ort="Ho",
    )
    ANON_BRI_KA = Sammlung(
        trace="Bri Ka",
        groups="Wortschatz|Anonym|Bri Ka",
        kreis="Bri",
        ort="Ka",
    )
    ANON_BRI_KB = Sammlung(
        trace="Bri Kb",
        groups="Wortschatz|Anonym|Bri Kb",
        kreis="Bri",
        ort="Kb",
    )
    ANON_BRI_KS = Sammlung(
        trace="Bri Ks",
        groups="Wortschatz|Anonym|Bri Ks",
        kreis="Bri",
        ort="Ks",
    )
    ANON_BRI_LI = Sammlung(
        trace="Bri Li",
        groups="Wortschatz|Anonym|Bri Li",
        kreis="Bri",
        ort="Li",
    )
    ANON_BRI_LM = Sammlung(
        trace="Bri Lm",
        groups="Wortschatz|Anonym|Bri Lm",
        kreis="Bri",
        ort="Lm",
    )
    ANON_BRI_MA = Sammlung(
        trace="Bri Ma",
        groups="Wortschatz|Anonym|Bri Ma",
        kreis="Bri",
        ort="Ma",
    )
    ANON_BRI_MB = Sammlung(
        trace="Bri Mb",
        groups="Wortschatz|Anonym|Bri Mb",
        kreis="Bri",
        ort="Mb",
    )
    ANON_BRI_MF = Sammlung(
        trace="Bri Mf",
        groups="Wortschatz|Anonym|Bri Mf",
        kreis="Bri",
        ort="Mf",
    )
    ANON_BRI_MH = Sammlung(
        trace="Bri Mh",
        groups="Wortschatz|Anonym|Bri Mh",
        kreis="Bri",
        ort="Mh",
    )
    ANON_BRI_ML = Sammlung(
        trace="Bri Ml",
        groups="Wortschatz|Anonym|Bri Ml",
        kreis="Bri",
        ort="Ml",
    )
    ANON_BRI_NA = Sammlung(
        trace="Bri Na",
        groups="Wortschatz|Anonym|Bri Na",
        kreis="Bri",
        ort="Na",
    )
    ANON_BRI_NE = Sammlung(
        trace="Bri Ne",
        groups="Wortschatz|Anonym|Bri Ne",
        kreis="Bri",
        ort="Ne",
    )
    ANON_BRI_NF = Sammlung(
        trace="Bri Nf",
        groups="Wortschatz|Anonym|Bri Nf",
        kreis="Bri",
        ort="Nf",
    )
    ANON_BRI_NM = Sammlung(
        trace="Bri Nm",
        groups="Wortschatz|Anonym|Bri Nm",
        kreis="Bri",
        ort="Nm",
    )
    ANON_BRI_OB = Sammlung(
        trace="Bri Ob",
        groups="Wortschatz|Anonym|Bri Ob",
        kreis="Bri",
        ort="Ob",
    )
    ANON_BRI_OM = Sammlung(
        trace="Bri Om",
        groups="Wortschatz|Anonym|Bri Om",
        kreis="Bri",
        ort="Om",
    )
    ANON_BRI_OS = Sammlung(
        trace="Bri Os",
        groups="Wortschatz|Anonym|Bri Os",
        kreis="Bri",
        ort="Os",
    )
    ANON_BRI_PA = Sammlung(
        trace="Bri Pa",
        groups="Wortschatz|Anonym|Bri Pa",
        kreis="Bri",
        ort="Pa",
    )
    ANON_BRI_PB = Sammlung(
        trace="Bri Pb",
        groups="Wortschatz|Anonym|Bri Pb",
        kreis="Bri",
        ort="Pb",
    )
    ANON_BRI_RA = Sammlung(
        trace="Bri Ra",
        groups="Wortschatz|Anonym|Bri Ra",
        kreis="Bri",
        ort="Ra",
    )
    ANON_BRI_RB = Sammlung(
        trace="Bri Rb",
        groups="Wortschatz|Anonym|Bri Rb",
        kreis="Bri",
        ort="Rb",
    )
    ANON_BRI_RF = Sammlung(
        trace="Bri Rf",
        groups="Wortschatz|Anonym|Bri Rf",
        kreis="Bri",
        ort="Rf",
    )
    ANON_BRI_RI = Sammlung(
        trace="Bri Ri",
        groups="Wortschatz|Anonym|Bri Ri",
        kreis="Bri",
        ort="Ri",
    )
    ANON_BRI_SB = Sammlung(
        trace="Bri Sb",
        groups="Wortschatz|Anonym|Bri Sb",
        kreis="Bri",
        ort="Sb",
    )
    ANON_BRI_SH = Sammlung(
        trace="Bri Sh",
        groups="Wortschatz|Anonym|Bri Sh",
        kreis="Bri",
        ort="Sh",
    )
    ANON_BRI_SI = Sammlung(
        trace="Bri Si",
        groups="Wortschatz|Anonym|Bri Si",
        kreis="Bri",
        ort="Si",
    )
    ANON_BRI_TI = Sammlung(
        trace="Bri Ti",
        groups="Wortschatz|Anonym|Bri Ti",
        kreis="Bri",
        ort="Ti",
    )
    ANON_BRI_TÜ = Sammlung(
        trace="Bri Tü",
        groups="Wortschatz|Anonym|Bri Tü",
        kreis="Bri",
        ort="Tü",
    )
    ANON_BRI_UD = Sammlung(
        trace="Bri Ud",
        groups="Wortschatz|Anonym|Bri Ud",
        kreis="Bri",
        ort="Ud",
    )
    ANON_BRI_WB = Sammlung(
        trace="Bri Wb",
        groups="Wortschatz|Anonym|Bri Wb",
        kreis="Bri",
        ort="Wb",
    )
    ANON_BRI_WH = Sammlung(
        trace="Bri Wh",
        groups="Wortschatz|Anonym|Bri Wh",
        kreis="Bri",
        ort="Wh",
    )
    ANON_BRI_WU = Sammlung(
        trace="Bri Wu",
        groups="Wortschatz|Anonym|Bri Wu",
        kreis="Bri",
        ort="Wu",
    )
    ANON_BRI_ZÜ = Sammlung(
        trace="Bri Zü",
        groups="Wortschatz|Anonym|Bri Zü",
        kreis="Bri",
        ort="Zü",
    )
    ANON_BÜK_AH = Sammlung(
        trace="Bük Ah",
        groups="Wortschatz|Anonym|Bük Ah",
        kreis="Bük",
        ort="Ah",
    )
    ANON_BÜK_BÜ = Sammlung(
        trace="Bük Bü",
        groups="Wortschatz|Anonym|Bük Bü",
        kreis="Bük",
        ort="Bü",
    )
    ANON_BÜK_EV = Sammlung(
        trace="Bük Ev",
        groups="Wortschatz|Anonym|Bük Ev",
        kreis="Bük",
        ort="Ev",
    )
    ANON_BÜK_GD = Sammlung(
        trace="Bük Gd",
        groups="Wortschatz|Anonym|Bük Gd",
        kreis="Bük",
        ort="Gd",
    )
    ANON_BÜK_HE = Sammlung(
        trace="Bük He",
        groups="Wortschatz|Anonym|Bük He",
        kreis="Bük",
        ort="He",
    )
    ANON_BÜK_KH = Sammlung(
        trace="Bük Kh",
        groups="Wortschatz|Anonym|Bük Kh",
        kreis="Bük",
        ort="Kh",
    )
    ANON_BÜK_LU = Sammlung(
        trace="Bük Lu",
        groups="Wortschatz|Anonym|Bük Lu",
        kreis="Bük",
        ort="Lu",
    )
    ANON_BÜK_ME = Sammlung(
        trace="Bük Me",
        groups="Wortschatz|Anonym|Bük Me",
        kreis="Bük",
        ort="Me",
    )
    ANON_BÜK_PE = Sammlung(
        trace="Bük Pe",
        groups="Wortschatz|Anonym|Bük Pe",
        kreis="Bük",
        ort="Pe",
    )
    ANON_BÜK_RÖ = Sammlung(
        trace="Bük Rö",
        groups="Wortschatz|Anonym|Bük Rö",
        kreis="Bük",
        ort="Rö",
    )
    ANON_BÜK_RU = Sammlung(
        trace="Bük Ru",
        groups="Wortschatz|Anonym|Bük Ru",
        kreis="Bük",
        ort="Ru",
    )
    ANON_BÜK_SB = Sammlung(
        trace="Bük Sb",
        groups="Wortschatz|Anonym|Bük Sb",
        kreis="Bük",
        ort="Sb",
    )
    ANON_BÜK_SC = Sammlung(
        trace="Bük Sc",
        groups="Wortschatz|Anonym|Bük Sc",
        kreis="Bük",
        ort="Sc",
    )
    ANON_BÜK_SH = Sammlung(
        trace="Bük Sh",
        groups="Wortschatz|Anonym|Bük Sh",
        kreis="Bük",
        ort="Sh",
    )
    ANON_BÜK_ST = Sammlung(
        trace="Bük St",
        groups="Wortschatz|Anonym|Bük St",
        kreis="Bük",
        ort="St",
    )
    ANON_BÜK_VE = Sammlung(
        trace="Bük Ve",
        groups="Wortschatz|Anonym|Bük Ve",
        kreis="Bük",
        ort="Ve",
    )
    ANON_BÜK_WI = Sammlung(
        trace="Bük Wi",
        groups="Wortschatz|Anonym|Bük Wi",
        kreis="Bük",
        ort="Wi",
    )
    ANON_BÜR_AD = Sammlung(
        trace="Bür Ad",
        groups="Wortschatz|Anonym|Bür Ad",
        kreis="Bür",
        ort="Ad",
    )
    ANON_BÜR_AN = Sammlung(
        trace="Bür An",
        groups="Wortschatz|Anonym|Bür An",
        kreis="Bür",
        ort="An",
    )
    ANON_BÜR_AS = Sammlung(
        trace="Bür As",
        groups="Wortschatz|Anonym|Bür As",
        kreis="Bür",
        ort="As",
    )
    ANON_BÜR_AT = Sammlung(
        trace="Bür At",
        groups="Wortschatz|Anonym|Bür At",
        kreis="Bür",
        ort="At",
    )
    ANON_BÜR_BE = Sammlung(
        trace="Bür Be",
        groups="Wortschatz|Anonym|Bür Be",
        kreis="Bür",
        ort="Be",
    )
    ANON_BÜR_BH = Sammlung(
        trace="Bür Bh",
        groups="Wortschatz|Anonym|Bür Bh",
        kreis="Bür",
        ort="Bh",
    )
    ANON_BÜR_BL = Sammlung(
        trace="Bür Bl",
        groups="Wortschatz|Anonym|Bür Bl",
        kreis="Bür",
        ort="Bl",
    )
    ANON_BÜR_BN = Sammlung(
        trace="Bür Bn",
        groups="Wortschatz|Anonym|Bür Bn",
        kreis="Bür",
        ort="Bn",
    )
    ANON_BÜR_BO = Sammlung(
        trace="Bür Bo",
        groups="Wortschatz|Anonym|Bür Bo",
        kreis="Bür",
        ort="Bo",
    )
    ANON_BÜR_BR = Sammlung(
        trace="Bür Br",
        groups="Wortschatz|Anonym|Bür Br",
        kreis="Bür",
        ort="Br",
    )
    ANON_BÜR_BÜ = Sammlung(
        trace="Bür Bü",
        groups="Wortschatz|Anonym|Bür Bü",
        kreis="Bür",
        ort="Bü",
    )
    ANON_BÜR_DH = Sammlung(
        trace="Bür Dh",
        groups="Wortschatz|Anonym|Bür Dh",
        kreis="Bür",
        ort="Dh",
    )
    ANON_BÜR_EB = Sammlung(
        trace="Bür Eb",
        groups="Wortschatz|Anonym|Bür Eb",
        kreis="Bür",
        ort="Eb",
    )
    ANON_BÜR_EI = Sammlung(
        trace="Bür Ei",
        groups="Wortschatz|Anonym|Bür Ei",
        kreis="Bür",
        ort="Ei",
    )
    ANON_BÜR_EL = Sammlung(
        trace="Bür El",
        groups="Wortschatz|Anonym|Bür El",
        kreis="Bür",
        ort="El",
    )
    ANON_BÜR_ES = Sammlung(
        trace="Bür Es",
        groups="Wortschatz|Anonym|Bür Es",
        kreis="Bür",
        ort="Es",
    )
    ANON_BÜR_ET = Sammlung(
        trace="Bür Et",
        groups="Wortschatz|Anonym|Bür Et",
        kreis="Bür",
        ort="Et",
    )
    ANON_BÜR_FÜ = Sammlung(
        trace="Bür Fü",
        groups="Wortschatz|Anonym|Bür Fü",
        kreis="Bür",
        ort="Fü",
    )
    ANON_BÜR_GA = Sammlung(
        trace="Bür Ga",
        groups="Wortschatz|Anonym|Bür Ga",
        kreis="Bür",
        ort="Ga",
    )
    ANON_BÜR_GR = Sammlung(
        trace="Bür Gr",
        groups="Wortschatz|Anonym|Bür Gr",
        kreis="Bür",
        ort="Gr",
    )
    ANON_BÜR_HA = Sammlung(
        trace="Bür Ha",
        groups="Wortschatz|Anonym|Bür Ha",
        kreis="Bür",
        ort="Ha",
    )
    ANON_BÜR_HB = Sammlung(
        trace="Bür Hb",
        groups="Wortschatz|Anonym|Bür Hb",
        kreis="Bür",
        ort="Hb",
    )
    ANON_BÜR_HD = Sammlung(
        trace="Bür Hd",
        groups="Wortschatz|Anonym|Bür Hd",
        kreis="Bür",
        ort="Hd",
    )
    ANON_BÜR_HE = Sammlung(
        trace="Bür He",
        groups="Wortschatz|Anonym|Bür He",
        kreis="Bür",
        ort="He",
    )
    ANON_BÜR_HG = Sammlung(
        trace="Bür Hg",
        groups="Wortschatz|Anonym|Bür Hg",
        kreis="Bür",
        ort="Hg",
    )
    ANON_BÜR_HH = Sammlung(
        trace="Bür Hh",
        groups="Wortschatz|Anonym|Bür Hh",
        kreis="Bür",
        ort="Hh",
    )
    ANON_BÜR_HL = Sammlung(
        trace="Bür Hl",
        groups="Wortschatz|Anonym|Bür Hl",
        kreis="Bür",
        ort="Hl",
    )
    ANON_BÜR_HO = Sammlung(
        trace="Bür Ho",
        groups="Wortschatz|Anonym|Bür Ho",
        kreis="Bür",
        ort="Ho",
    )
    ANON_BÜR_HÖ = Sammlung(
        trace="Bür Hö",
        groups="Wortschatz|Anonym|Bür Hö",
        kreis="Bür",
        ort="Hö",
    )
    ANON_BÜR_HR = Sammlung(
        trace="Bür Hr",
        groups="Wortschatz|Anonym|Bür Hr",
        kreis="Bür",
        ort="Hr",
    )
    ANON_BÜR_IH = Sammlung(
        trace="Bür Ih",
        groups="Wortschatz|Anonym|Bür Ih",
        kreis="Bür",
        ort="Ih",
    )
    ANON_BÜR_KL = Sammlung(
        trace="Bür Kl",
        groups="Wortschatz|Anonym|Bür Kl",
        kreis="Bür",
        ort="Kl",
    )
    ANON_BÜR_LB = Sammlung(
        trace="Bür Lb",
        groups="Wortschatz|Anonym|Bür Lb",
        kreis="Bür",
        ort="Lb",
    )
    ANON_BÜR_LI = Sammlung(
        trace="Bür Li",
        groups="Wortschatz|Anonym|Bür Li",
        kreis="Bür",
        ort="Li",
    )
    ANON_BÜR_MA = Sammlung(
        trace="Bür Ma",
        groups="Wortschatz|Anonym|Bür Ma",
        kreis="Bür",
        ort="Ma",
    )
    ANON_BÜR_ME = Sammlung(
        trace="Bür Me",
        groups="Wortschatz|Anonym|Bür Me",
        kreis="Bür",
        ort="Me",
    )
    ANON_BÜR_MH = Sammlung(
        trace="Bür Mh",
        groups="Wortschatz|Anonym|Bür Mh",
        kreis="Bür",
        ort="Mh",
    )
    ANON_BÜR_NT = Sammlung(
        trace="Bür Nt",
        groups="Wortschatz|Anonym|Bür Nt",
        kreis="Bür",
        ort="Nt",
    )
    ANON_BÜR_ÖD = Sammlung(
        trace="Bür Öd",
        groups="Wortschatz|Anonym|Bür Öd",
        kreis="Bür",
        ort="Öd",
    )
    ANON_BÜR_OT = Sammlung(
        trace="Bür Ot",
        groups="Wortschatz|Anonym|Bür Ot",
        kreis="Bür",
        ort="Ot",
    )
    ANON_BÜR_RE = Sammlung(
        trace="Bür Re",
        groups="Wortschatz|Anonym|Bür Re",
        kreis="Bür",
        ort="Re",
    )
    ANON_BÜR_RI = Sammlung(
        trace="Bür Ri",
        groups="Wortschatz|Anonym|Bür Ri",
        kreis="Bür",
        ort="Ri",
    )
    ANON_BÜR_SC = Sammlung(
        trace="Bür Sc",
        groups="Wortschatz|Anonym|Bür Sc",
        kreis="Bür",
        ort="Sc",
    )
    ANON_BÜR_SH = Sammlung(
        trace="Bür Sh",
        groups="Wortschatz|Anonym|Bür Sh",
        kreis="Bür",
        ort="Sh",
    )
    ANON_BÜR_SI = Sammlung(
        trace="Bür Si",
        groups="Wortschatz|Anonym|Bür Si",
        kreis="Bür",
        ort="Si",
    )
    ANON_BÜR_SK = Sammlung(
        trace="Bür Sk",
        groups="Wortschatz|Anonym|Bür Sk",
        kreis="Bür",
        ort="Sk",
    )
    ANON_BÜR_TH = Sammlung(
        trace="Bür Th",
        groups="Wortschatz|Anonym|Bür Th",
        kreis="Bür",
        ort="Th",
    )
    ANON_BÜR_UP = Sammlung(
        trace="Bür Up",
        groups="Wortschatz|Anonym|Bür Up",
        kreis="Bür",
        ort="Up",
    )
    ANON_BÜR_VE = Sammlung(
        trace="Bür Ve",
        groups="Wortschatz|Anonym|Bür Ve",
        kreis="Bür",
        ort="Ve",
    )
    ANON_BÜR_VN = Sammlung(
        trace="Bür Vn",
        groups="Wortschatz|Anonym|Bür Vn",
        kreis="Bür",
        ort="Vn",
    )
    ANON_BÜR_WB = Sammlung(
        trace="Bür Wb",
        groups="Wortschatz|Anonym|Bür Wb",
        kreis="Bür",
        ort="Wb",
    )
    ANON_BÜR_WE = Sammlung(
        trace="Bür We",
        groups="Wortschatz|Anonym|Bür We",
        kreis="Bür",
        ort="We",
    )
    ANON_BÜR_WH = Sammlung(
        trace="Bür Wh",
        groups="Wortschatz|Anonym|Bür Wh",
        kreis="Bür",
        ort="Wh",
    )
    ANON_BÜR_WI = Sammlung(
        trace="Bür Wi",
        groups="Wortschatz|Anonym|Bür Wi",
        kreis="Bür",
        ort="Wi",
    )
    ANON_BÜR_WÜ = Sammlung(
        trace="Bür Wü",
        groups="Wortschatz|Anonym|Bür Wü",
        kreis="Bür",
        ort="Wü",
    )
    ANON_BÜR_WW = Sammlung(
        trace="Bür Ww",
        groups="Wortschatz|Anonym|Bür Ww",
        kreis="Bür",
        ort="Ww",
    )
    ANON_DET_AU = Sammlung(
        trace="Det Au",
        groups="Wortschatz|Anonym|Det Au",
        kreis="Det",
        ort="Au",
    )
    ANON_DET_BB = Sammlung(
        trace="Det Bb",
        groups="Wortschatz|Anonym|Det Bb",
        kreis="Det",
        ort="Bb",
    )
    ANON_DET_BE = Sammlung(
        trace="Det Be",
        groups="Wortschatz|Anonym|Det Be",
        kreis="Det",
        ort="Be",
    )
    ANON_DET_BH = Sammlung(
        trace="Det Bh",
        groups="Wortschatz|Anonym|Det Bh",
        kreis="Det",
        ort="Bh",
    )
    ANON_DET_BI = Sammlung(
        trace="Det Bi",
        groups="Wortschatz|Anonym|Det Bi",
        kreis="Det",
        ort="Bi",
    )
    ANON_DET_BK = Sammlung(
        trace="Det Bk",
        groups="Wortschatz|Anonym|Det Bk",
        kreis="Det",
        ort="Bk",
    )
    ANON_DET_BL = Sammlung(
        trace="Det Bl",
        groups="Wortschatz|Anonym|Det Bl",
        kreis="Det",
        ort="Bl",
    )
    ANON_DET_BM = Sammlung(
        trace="Det Bm",
        groups="Wortschatz|Anonym|Det Bm",
        kreis="Det",
        ort="Bm",
    )
    ANON_DET_BR = Sammlung(
        trace="Det Br",
        groups="Wortschatz|Anonym|Det Br",
        kreis="Det",
        ort="Br",
    )
    ANON_DET_BS = Sammlung(
        trace="Det Bs",
        groups="Wortschatz|Anonym|Det Bs",
        kreis="Det",
        ort="Bs",
    )
    ANON_DET_BY = Sammlung(
        trace="Det By",
        groups="Wortschatz|Anonym|Det By",
        kreis="Det",
        ort="By",
    )
    ANON_DET_DA = Sammlung(
        trace="Det Da",
        groups="Wortschatz|Anonym|Det Da",
        kreis="Det",
        ort="Da",
    )
    ANON_DET_DB = Sammlung(
        trace="Det Db",
        groups="Wortschatz|Anonym|Det Db",
        kreis="Det",
        ort="Db",
    )
    ANON_DET_DE = Sammlung(
        trace="Det De",
        groups="Wortschatz|Anonym|Det De",
        kreis="Det",
        ort="De",
    )
    ANON_DET_DO = Sammlung(
        trace="Det Do",
        groups="Wortschatz|Anonym|Det Do",
        kreis="Det",
        ort="Do",
    )
    ANON_DET_EB = Sammlung(
        trace="Det Eb",
        groups="Wortschatz|Anonym|Det Eb",
        kreis="Det",
        ort="Eb",
    )
    ANON_DET_EH = Sammlung(
        trace="Det Eh",
        groups="Wortschatz|Anonym|Det Eh",
        kreis="Det",
        ort="Eh",
    )
    ANON_DET_EL = Sammlung(
        trace="Det El",
        groups="Wortschatz|Anonym|Det El",
        kreis="Det",
        ort="El",
    )
    ANON_DET_ER = Sammlung(
        trace="Det Er",
        groups="Wortschatz|Anonym|Det Er",
        kreis="Det",
        ort="Er",
    )
    ANON_DET_FA = Sammlung(
        trace="Det Fa",
        groups="Wortschatz|Anonym|Det Fa",
        kreis="Det",
        ort="Fa",
    )
    ANON_DET_FH = Sammlung(
        trace="Det Fh",
        groups="Wortschatz|Anonym|Det Fh",
        kreis="Det",
        ort="Fh",
    )
    ANON_DET_GB = Sammlung(
        trace="Det Gb",
        groups="Wortschatz|Anonym|Det Gb",
        kreis="Det",
        ort="Gb",
    )
    ANON_DET_GR = Sammlung(
        trace="Det Gr",
        groups="Wortschatz|Anonym|Det Gr",
        kreis="Det",
        ort="Gr",
    )
    ANON_DET_HB = Sammlung(
        trace="Det Hb",
        groups="Wortschatz|Anonym|Det Hb",
        kreis="Det",
        ort="Hb",
    )
    ANON_DET_HD = Sammlung(
        trace="Det Hd",
        groups="Wortschatz|Anonym|Det Hd",
        kreis="Det",
        ort="Hd",
    )
    ANON_DET_HE = Sammlung(
        trace="Det He",
        groups="Wortschatz|Anonym|Det He",
        kreis="Det",
        ort="He",
    )
    ANON_DET_HH = Sammlung(
        trace="Det Hh",
        groups="Wortschatz|Anonym|Det Hh",
        kreis="Det",
        ort="Hh",
    )
    ANON_DET_HI = Sammlung(
        trace="Det Hi",
        groups="Wortschatz|Anonym|Det Hi",
        kreis="Det",
        ort="Hi",
    )
    ANON_DET_HK = Sammlung(
        trace="Det Hk",
        groups="Wortschatz|Anonym|Det Hk",
        kreis="Det",
        ort="Hk",
    )
    ANON_DET_HM = Sammlung(
        trace="Det Hm",
        groups="Wortschatz|Anonym|Det Hm",
        kreis="Det",
        ort="Hm",
    )
    ANON_DET_HN = Sammlung(
        trace="Det Hn",
        groups="Wortschatz|Anonym|Det Hn",
        kreis="Det",
        ort="Hn",
    )
    ANON_DET_HO = Sammlung(
        trace="Det Ho",
        groups="Wortschatz|Anonym|Det Ho",
        kreis="Det",
        ort="Ho",
    )
    ANON_DET_HÖ = Sammlung(
        trace="Det Hö",
        groups="Wortschatz|Anonym|Det Hö",
        kreis="Det",
        ort="Hö",
    )
    ANON_DET_HR = Sammlung(
        trace="Det Hr",
        groups="Wortschatz|Anonym|Det Hr",
        kreis="Det",
        ort="Hr",
    )
    ANON_DET_HU = Sammlung(
        trace="Det Hu",
        groups="Wortschatz|Anonym|Det Hu",
        kreis="Det",
        ort="Hu",
    )
    ANON_DET_JE = Sammlung(
        trace="Det Je",
        groups="Wortschatz|Anonym|Det Je",
        kreis="Det",
        ort="Je",
    )
    ANON_DET_IH = Sammlung(
        trace="Det Ih",
        groups="Wortschatz|Anonym|Det Ih",
        kreis="Det",
        ort="Ih",
    )
    ANON_DET_IS = Sammlung(
        trace="Det Is",
        groups="Wortschatz|Anonym|Det Is",
        kreis="Det",
        ort="Is",
    )
    ANON_DET_KA = Sammlung(
        trace="Det Ka",
        groups="Wortschatz|Anonym|Det Ka",
        kreis="Det",
        ort="Ka",
    )
    ANON_DET_KL = Sammlung(
        trace="Det Kl",
        groups="Wortschatz|Anonym|Det Kl",
        kreis="Det",
        ort="Kl",
    )
    ANON_DET_KO = Sammlung(
        trace="Det Ko",
        groups="Wortschatz|Anonym|Det Ko",
        kreis="Det",
        ort="Ko",
    )
    ANON_DET_KT = Sammlung(
        trace="Det Kt",
        groups="Wortschatz|Anonym|Det Kt",
        kreis="Det",
        ort="Kt",
    )
    ANON_DET_LA = Sammlung(
        trace="Det La",
        groups="Wortschatz|Anonym|Det La",
        kreis="Det",
        ort="La",
    )
    ANON_DET_LO = Sammlung(
        trace="Det Lo",
        groups="Wortschatz|Anonym|Det Lo",
        kreis="Det",
        ort="Lo",
    )
    ANON_DET_LT = Sammlung(
        trace="Det Lt",
        groups="Wortschatz|Anonym|Det Lt",
        kreis="Det",
        ort="Lt",
    )
    ANON_DET_MA = Sammlung(
        trace="Det Ma",
        groups="Wortschatz|Anonym|Det Ma",
        kreis="Det",
        ort="Ma",
    )
    ANON_DET_MB = Sammlung(
        trace="Det Mb",
        groups="Wortschatz|Anonym|Det Mb",
        kreis="Det",
        ort="Mb",
    )
    ANON_DET_MF = Sammlung(
        trace="Det Mf",
        groups="Wortschatz|Anonym|Det Mf",
        kreis="Det",
        ort="Mf",
    )
    ANON_DET_MO = Sammlung(
        trace="Det Mo",
        groups="Wortschatz|Anonym|Det Mo",
        kreis="Det",
        ort="Mo",
    )
    ANON_DET_NH = Sammlung(
        trace="Det Nh",
        groups="Wortschatz|Anonym|Det Nh",
        kreis="Det",
        ort="Nh",
    )
    ANON_DET_NI = Sammlung(
        trace="Det Ni",
        groups="Wortschatz|Anonym|Det Ni",
        kreis="Det",
        ort="Ni",
    )
    ANON_DET_OB = Sammlung(
        trace="Det Ob",
        groups="Wortschatz|Anonym|Det Ob",
        kreis="Det",
        ort="Ob",
    )
    ANON_DET_OS = Sammlung(
        trace="Det Os",
        groups="Wortschatz|Anonym|Det Os",
        kreis="Det",
        ort="Os",
    )
    ANON_DET_PI = Sammlung(
        trace="Det Pi",
        groups="Wortschatz|Anonym|Det Pi",
        kreis="Det",
        ort="Pi",
    )
    ANON_DET_PO = Sammlung(
        trace="Det Po",
        groups="Wortschatz|Anonym|Det Po",
        kreis="Det",
        ort="Po",
    )
    ANON_DET_RH = Sammlung(
        trace="Det Rh",
        groups="Wortschatz|Anonym|Det Rh",
        kreis="Det",
        ort="Rh",
    )
    ANON_DET_RI = Sammlung(
        trace="Det Ri",
        groups="Wortschatz|Anonym|Det Ri",
        kreis="Det",
        ort="Ri",
    )
    ANON_DET_RK = Sammlung(
        trace="Det Rk",
        groups="Wortschatz|Anonym|Det Rk",
        kreis="Det",
        ort="Rk",
    )
    ANON_DET_RÖ = Sammlung(
        trace="Det Rö",
        groups="Wortschatz|Anonym|Det Rö",
        kreis="Det",
        ort="Rö",
    )
    ANON_DET_SC = Sammlung(
        trace="Det Sc",
        groups="Wortschatz|Anonym|Det Sc",
        kreis="Det",
        ort="Sc",
    )
    ANON_DET_SH = Sammlung(
        trace="Det Sh",
        groups="Wortschatz|Anonym|Det Sh",
        kreis="Det",
        ort="Sh",
    )
    ANON_DET_SL = Sammlung(
        trace="Det Sl",
        groups="Wortschatz|Anonym|Det Sl",
        kreis="Det",
        ort="Sl",
    )
    ANON_DET_SM = Sammlung(
        trace="Det Sm",
        groups="Wortschatz|Anonym|Det Sm",
        kreis="Det",
        ort="Sm",
    )
    ANON_DET_ST = Sammlung(
        trace="Det St",
        groups="Wortschatz|Anonym|Det St",
        kreis="Det",
        ort="St",
    )
    ANON_DET_SW = Sammlung(
        trace="Det Sw",
        groups="Wortschatz|Anonym|Det Sw",
        kreis="Det",
        ort="Sw",
    )
    ANON_DET_VA = Sammlung(
        trace="Det Va",
        groups="Wortschatz|Anonym|Det Va",
        kreis="Det",
        ort="Va",
    )
    ANON_DET_VR = Sammlung(
        trace="Det Vr",
        groups="Wortschatz|Anonym|Det Vr",
        kreis="Det",
        ort="Vr",
    )
    ANON_DET_WF = Sammlung(
        trace="Det Wf",
        groups="Wortschatz|Anonym|Det Wf",
        kreis="Det",
        ort="Wf",
    )
    ANON_DET_WH = Sammlung(
        trace="Det Wh",
        groups="Wortschatz|Anonym|Det Wh",
        kreis="Det",
        ort="Wh",
    )
    ANON_DET_WÖ = Sammlung(
        trace="Det Wö",
        groups="Wortschatz|Anonym|Det Wö",
        kreis="Det",
        ort="Wö",
    )
    ANON_DIE_AS = Sammlung(
        trace="Die As",
        groups="Wortschatz|Anonym|Die As",
        kreis="Die",
        ort="As",
    )
    ANON_DIE_BA = Sammlung(
        trace="Die Ba",
        groups="Wortschatz|Anonym|Die Ba",
        kreis="Die",
        ort="Ba",
    )
    ANON_DIE_BB = Sammlung(
        trace="Die Bb",
        groups="Wortschatz|Anonym|Die Bb",
        kreis="Die",
        ort="Bb",
    )
    ANON_DIE_BV = Sammlung(
        trace="Die Bv",
        groups="Wortschatz|Anonym|Die Bv",
        kreis="Die",
        ort="Bv",
    )
    ANON_DIE_DI = Sammlung(
        trace="Die Di",
        groups="Wortschatz|Anonym|Die Di",
        kreis="Die",
        ort="Di",
    )
    ANON_DIE_DÖ = Sammlung(
        trace="Die Dö",
        groups="Wortschatz|Anonym|Die Dö",
        kreis="Die",
        ort="Dö",
    )
    ANON_DIE_HE = Sammlung(
        trace="Die He",
        groups="Wortschatz|Anonym|Die He",
        kreis="Die",
        ort="He",
    )
    ANON_DIE_HF = Sammlung(
        trace="Die Hf",
        groups="Wortschatz|Anonym|Die Hf",
        kreis="Die",
        ort="Hf",
    )
    ANON_DIE_HH = Sammlung(
        trace="Die Hh",
        groups="Wortschatz|Anonym|Die Hh",
        kreis="Die",
        ort="Hh",
    )
    ANON_DIE_HÜ = Sammlung(
        trace="Die Hü",
        groups="Wortschatz|Anonym|Die Hü",
        kreis="Die",
        ort="Hü",
    )
    ANON_DIE_KI = Sammlung(
        trace="Die Ki",
        groups="Wortschatz|Anonym|Die Ki",
        kreis="Die",
        ort="Ki",
    )
    ANON_DIE_LB = Sammlung(
        trace="Die Lb",
        groups="Wortschatz|Anonym|Die Lb",
        kreis="Die",
        ort="Lb",
    )
    ANON_DIE_LE = Sammlung(
        trace="Die Le",
        groups="Wortschatz|Anonym|Die Le",
        kreis="Die",
        ort="Le",
    )
    ANON_DIE_MA = Sammlung(
        trace="Die Ma",
        groups="Wortschatz|Anonym|Die Ma",
        kreis="Die",
        ort="Ma",
    )
    ANON_DIE_ST = Sammlung(
        trace="Die St",
        groups="Wortschatz|Anonym|Die St",
        kreis="Die",
        ort="St",
    )
    ANON_DIE_VA = Sammlung(
        trace="Die Va",
        groups="Wortschatz|Anonym|Die Va",
        kreis="Die",
        ort="Va",
    )
    ANON_DIE_WH = Sammlung(
        trace="Die Wh",
        groups="Wortschatz|Anonym|Die Wh",
        kreis="Die",
        ort="Wh",
    )
    ANON_DIE_WF = Sammlung(
        trace="Die Wf",
        groups="Wortschatz|Anonym|Die Wf",
        kreis="Die",
        ort="Wf",
    )
    ANON_DOR_AP = Sammlung(
        trace="Dor Ap",
        groups="Wortschatz|Anonym|Dor Ap",
        kreis="Dor",
        ort="Ap",
    )
    ANON_DOR_AS = Sammlung(
        trace="Dor As",
        groups="Wortschatz|Anonym|Dor As",
        kreis="Dor",
        ort="As",
    )
    ANON_DOR_BA = Sammlung(
        trace="Dor Ba",
        groups="Wortschatz|Anonym|Dor Ba",
        kreis="Dor",
        ort="Ba",
    )
    ANON_DOR_BB = Sammlung(
        trace="Dor Bb",
        groups="Wortschatz|Anonym|Dor Bb",
        kreis="Dor",
        ort="Bb",
    )
    ANON_DOR_BH = Sammlung(
        trace="Dor Bh",
        groups="Wortschatz|Anonym|Dor Bh",
        kreis="Dor",
        ort="Bh",
    )
    ANON_DOR_BK = Sammlung(
        trace="Dor Bk",
        groups="Wortschatz|Anonym|Dor Bk",
        kreis="Dor",
        ort="Bk",
    )
    ANON_DOR_BO = Sammlung(
        trace="Dor Bo",
        groups="Wortschatz|Anonym|Dor Bo",
        kreis="Dor",
        ort="Bo",
    )
    ANON_DOR_BÖ = Sammlung(
        trace="Dor Bö",
        groups="Wortschatz|Anonym|Dor Bö",
        kreis="Dor",
        ort="Bö",
    )
    ANON_DOR_BR = Sammlung(
        trace="Dor Br",
        groups="Wortschatz|Anonym|Dor Br",
        kreis="Dor",
        ort="Br",
    )
    ANON_DOR_DD = Sammlung(
        trace="Dor Dd",
        groups="Wortschatz|Anonym|Dor Dd",
        kreis="Dor",
        ort="Dd",
    )
    ANON_DOR_DE = Sammlung(
        trace="Dor De",
        groups="Wortschatz|Anonym|Dor De",
        kreis="Dor",
        ort="De",
    )
    ANON_DOR_DO = Sammlung(
        trace="Dor Do",
        groups="Wortschatz|Anonym|Dor Do",
        kreis="Dor",
        ort="Do",
    )
    ANON_DOR_EI = Sammlung(
        trace="Dor Ei",
        groups="Wortschatz|Anonym|Dor Ei",
        kreis="Dor",
        ort="Ei",
    )
    ANON_DOR_EV = Sammlung(
        trace="Dor Ev",
        groups="Wortschatz|Anonym|Dor Ev",
        kreis="Dor",
        ort="Ev",
    )
    ANON_DOR_GB = Sammlung(
        trace="Dor Gb",
        groups="Wortschatz|Anonym|Dor Gb",
        kreis="Dor",
        ort="Gb",
    )
    ANON_DOR_GV = Sammlung(
        trace="Dor Gv",
        groups="Wortschatz|Anonym|Dor Gv",
        kreis="Dor",
        ort="Gv",
    )
    ANON_DOR_HA = Sammlung(
        trace="Dor Ha",
        groups="Wortschatz|Anonym|Dor Ha",
        kreis="Dor",
        ort="Ha",
    )
    ANON_DOR_HH = Sammlung(
        trace="Dor Hh",
        groups="Wortschatz|Anonym|Dor Hh",
        kreis="Dor",
        ort="Hh",
    )
    ANON_DOR_HN = Sammlung(
        trace="Dor Hn",
        groups="Wortschatz|Anonym|Dor Hn",
        kreis="Dor",
        ort="Hn",
    )
    ANON_DOR_HÖ = Sammlung(
        trace="Dor Hö",
        groups="Wortschatz|Anonym|Dor Hö",
        kreis="Dor",
        ort="Hö",
    )
    ANON_DOR_HS = Sammlung(
        trace="Dor Hs",
        groups="Wortschatz|Anonym|Dor Hs",
        kreis="Dor",
        ort="Hs",
    )
    ANON_DOR_HU = Sammlung(
        trace="Dor Hu",
        groups="Wortschatz|Anonym|Dor Hu",
        kreis="Dor",
        ort="Hu",
    )
    ANON_DOR_KA = Sammlung(
        trace="Dor Ka",
        groups="Wortschatz|Anonym|Dor Ka",
        kreis="Dor",
        ort="Ka",
    )
    ANON_DOR_KI = Sammlung(
        trace="Dor Ki",
        groups="Wortschatz|Anonym|Dor Ki",
        kreis="Dor",
        ort="Ki",
    )
    ANON_DOR_KL = Sammlung(
        trace="Dor Kl",
        groups="Wortschatz|Anonym|Dor Kl",
        kreis="Dor",
        ort="Kl",
    )
    ANON_DOR_KN = Sammlung(
        trace="Dor Kn",
        groups="Wortschatz|Anonym|Dor Kn",
        kreis="Dor",
        ort="Kn",
    )
    ANON_DOR_KR = Sammlung(
        trace="Dor Kr",
        groups="Wortschatz|Anonym|Dor Kr",
        kreis="Dor",
        ort="Kr",
    )
    ANON_DOR_KU = Sammlung(
        trace="Dor Ku",
        groups="Wortschatz|Anonym|Dor Ku",
        kreis="Dor",
        ort="Ku",
    )
    ANON_DOR_LÖ = Sammlung(
        trace="Dor Lö",
        groups="Wortschatz|Anonym|Dor Lö",
        kreis="Dor",
        ort="Lö",
    )
    ANON_DOR_LÜ = Sammlung(
        trace="Dor Lü",
        groups="Wortschatz|Anonym|Dor Lü",
        kreis="Dor",
        ort="Lü",
    )
    ANON_DOR_MA = Sammlung(
        trace="Dor Ma",
        groups="Wortschatz|Anonym|Dor Ma",
        kreis="Dor",
        ort="Ma",
    )
    ANON_DOR_ME = Sammlung(
        trace="Dor Me",
        groups="Wortschatz|Anonym|Dor Me",
        kreis="Dor",
        ort="Me",
    )
    ANON_DOR_ÖS = Sammlung(
        trace="Dor Ös",
        groups="Wortschatz|Anonym|Dor Ös",
        kreis="Dor",
        ort="Ös",
    )
    ANON_DOR_PÖ = Sammlung(
        trace="Dor Pö",
        groups="Wortschatz|Anonym|Dor Pö",
        kreis="Dor",
        ort="Pö",
    )
    ANON_DOR_RA = Sammlung(
        trace="Dor Ra",
        groups="Wortschatz|Anonym|Dor Ra",
        kreis="Dor",
        ort="Ra",
    )
    ANON_DOR_SB = Sammlung(
        trace="Dor Sb",
        groups="Wortschatz|Anonym|Dor Sb",
        kreis="Dor",
        ort="Sb",
    )
    ANON_DOR_SC = Sammlung(
        trace="Dor Sc",
        groups="Wortschatz|Anonym|Dor Sc",
        kreis="Dor",
        ort="Sc",
    )
    ANON_DOR_SO = Sammlung(
        trace="Dor So",
        groups="Wortschatz|Anonym|Dor So",
        kreis="Dor",
        ort="So",
    )
    ANON_DOR_SO1 = Sammlung(
        trace="Dor So1",
        groups="Wortschatz|Anonym|Dor So1",
        kreis="Dor",
        ort="So1",
    )
    ANON_DOR_SÖ = Sammlung(
        trace="Dor Sö",
        groups="Wortschatz|Anonym|Dor Sö",
        kreis="Dor",
        ort="Sö",
    )
    ANON_DOR_SÜ = Sammlung(
        trace="Dor Sü",
        groups="Wortschatz|Anonym|Dor Sü",
        kreis="Dor",
        ort="Sü",
    )
    ANON_DOR_WH = Sammlung(
        trace="Dor Wh",
        groups="Wortschatz|Anonym|Dor Wh",
        kreis="Dor",
        ort="Wh",
    )
    ANON_DOR_WI = Sammlung(
        trace="Dor Wi",
        groups="Wortschatz|Anonym|Dor Wi",
        kreis="Dor",
        ort="Wi",
    )
    ANON_DOR_WL = Sammlung(
        trace="Dor Wl",
        groups="Wortschatz|Anonym|Dor Wl",
        kreis="Dor",
        ort="Wl",
    )
    ANON_ENR_AD = Sammlung(
        trace="Enr Ad",
        groups="Wortschatz|Anonym|Enr Ad",
        kreis="Enr",
        ort="Ad",
    )
    ANON_ENR_AH = Sammlung(
        trace="Enr Ah",
        groups="Wortschatz|Anonym|Enr Ah",
        kreis="Enr",
        ort="Ah",
    )
    ANON_ENR_BA = Sammlung(
        trace="Enr Ba",
        groups="Wortschatz|Anonym|Enr Ba",
        kreis="Enr",
        ort="Ba",
    )
    ANON_ENR_BE = Sammlung(
        trace="Enr Be",
        groups="Wortschatz|Anonym|Enr Be",
        kreis="Enr",
        ort="Be",
    )
    ANON_ENR_BF = Sammlung(
        trace="Enr Bf",
        groups="Wortschatz|Anonym|Enr Bf",
        kreis="Enr",
        ort="Bf",
    )
    ANON_ENR_BH = Sammlung(
        trace="Enr Bh",
        groups="Wortschatz|Anonym|Enr Bh",
        kreis="Enr",
        ort="Bh",
    )
    ANON_ENR_BL = Sammlung(
        trace="Enr Bl",
        groups="Wortschatz|Anonym|Enr Bl",
        kreis="Enr",
        ort="Bl",
    )
    ANON_ENR_BO = Sammlung(
        trace="Enr Bo",
        groups="Wortschatz|Anonym|Enr Bo",
        kreis="Enr",
        ort="Bo",
    )
    ANON_ENR_BÖ = Sammlung(
        trace="Enr Bö",
        groups="Wortschatz|Anonym|Enr Bö",
        kreis="Enr",
        ort="Bö",
    )
    ANON_ENR_BR = Sammlung(
        trace="Enr Br",
        groups="Wortschatz|Anonym|Enr Br",
        kreis="Enr",
        ort="Br",
    )
    ANON_ENR_BW = Sammlung(
        trace="Enr Bw",
        groups="Wortschatz|Anonym|Enr Bw",
        kreis="Enr",
        ort="Bw",
    )
    ANON_ENR_DA = Sammlung(
        trace="Enr Da",
        groups="Wortschatz|Anonym|Enr Da",
        kreis="Enr",
        ort="Da",
    )
    ANON_ENR_DH = Sammlung(
        trace="Enr Dh",
        groups="Wortschatz|Anonym|Enr Dh",
        kreis="Enr",
        ort="Dh",
    )
    ANON_ENR_DU = Sammlung(
        trace="Enr Du",
        groups="Wortschatz|Anonym|Enr Du",
        kreis="Enr",
        ort="Du",
    )
    ANON_ENR_EB = Sammlung(
        trace="Enr Eb",
        groups="Wortschatz|Anonym|Enr Eb",
        kreis="Enr",
        ort="Eb",
    )
    ANON_ENR_EH = Sammlung(
        trace="Enr Eh",
        groups="Wortschatz|Anonym|Enr Eh",
        kreis="Enr",
        ort="Eh",
    )
    ANON_ENR_EN = Sammlung(
        trace="Enr En",
        groups="Wortschatz|Anonym|Enr En",
        kreis="Enr",
        ort="En",
    )
    ANON_ENR_ES = Sammlung(
        trace="Enr Es",
        groups="Wortschatz|Anonym|Enr Es",
        kreis="Enr",
        ort="Es",
    )
    ANON_ENR_ET = Sammlung(
        trace="Enr Et",
        groups="Wortschatz|Anonym|Enr Et",
        kreis="Enr",
        ort="Et",
    )
    ANON_ENR_GB = Sammlung(
        trace="Enr Gb",
        groups="Wortschatz|Anonym|Enr Gb",
        kreis="Enr",
        ort="Gb",
    )
    ANON_ENR_GR = Sammlung(
        trace="Enr Gr",
        groups="Wortschatz|Anonym|Enr Gr",
        kreis="Enr",
        ort="Gr",
    )
    ANON_ENR_HA = Sammlung(
        trace="Enr Ha",
        groups="Wortschatz|Anonym|Enr Ha",
        kreis="Enr",
        ort="Ha",
    )
    ANON_ENR_HB = Sammlung(
        trace="Enr Hb",
        groups="Wortschatz|Anonym|Enr Hb",
        kreis="Enr",
        ort="Hb",
    )
    ANON_ENR_HD = Sammlung(
        trace="Enr Hd",
        groups="Wortschatz|Anonym|Enr Hd",
        kreis="Enr",
        ort="Hd",
    )
    ANON_ENR_HE = Sammlung(
        trace="Enr He",
        groups="Wortschatz|Anonym|Enr He",
        kreis="Enr",
        ort="He",
    )
    ANON_ENR_HH = Sammlung(
        trace="Enr Hh",
        groups="Wortschatz|Anonym|Enr Hh",
        kreis="Enr",
        ort="Hh",
    )
    ANON_ENR_HK = Sammlung(
        trace="Enr Hk",
        groups="Wortschatz|Anonym|Enr Hk",
        kreis="Enr",
        ort="Hk",
    )
    ANON_ENR_HO = Sammlung(
        trace="Enr Ho",
        groups="Wortschatz|Anonym|Enr Ho",
        kreis="Enr",
        ort="Ho",
    )
    ANON_ENR_HR = Sammlung(
        trace="Enr Hr",
        groups="Wortschatz|Anonym|Enr Hr",
        kreis="Enr",
        ort="Hr",
    )
    ANON_ENR_HT = Sammlung(
        trace="Enr Ht",
        groups="Wortschatz|Anonym|Enr Ht",
        kreis="Enr",
        ort="Ht",
    )
    ANON_ENR_HU = Sammlung(
        trace="Enr Hu",
        groups="Wortschatz|Anonym|Enr Hu",
        kreis="Enr",
        ort="Hu",
    )
    ANON_ENR_KH = Sammlung(
        trace="Enr Kh",
        groups="Wortschatz|Anonym|Enr Kh",
        kreis="Enr",
        ort="Kh",
    )
    ANON_ENR_LD = Sammlung(
        trace="Enr Ld",
        groups="Wortschatz|Anonym|Enr Ld",
        kreis="Enr",
        ort="Ld",
    )
    ANON_ENR_LI = Sammlung(
        trace="Enr Li",
        groups="Wortschatz|Anonym|Enr Li",
        kreis="Enr",
        ort="Li",
    )
    ANON_ENR_MI = Sammlung(
        trace="Enr Mi",
        groups="Wortschatz|Anonym|Enr Mi",
        kreis="Enr",
        ort="Mi",
    )
    ANON_ENR_MK = Sammlung(
        trace="Enr Mk",
        groups="Wortschatz|Anonym|Enr Mk",
        kreis="Enr",
        ort="Mk",
    )
    ANON_ENR_NB = Sammlung(
        trace="Enr Nb",
        groups="Wortschatz|Anonym|Enr Nb",
        kreis="Enr",
        ort="Nb",
    )
    ANON_ENR_NH = Sammlung(
        trace="Enr Nh",
        groups="Wortschatz|Anonym|Enr Nh",
        kreis="Enr",
        ort="Nh",
    )
    ANON_ENR_NS = Sammlung(
        trace="Enr Ns",
        groups="Wortschatz|Anonym|Enr Ns",
        kreis="Enr",
        ort="Ns",
    )
    ANON_ENR_NW = Sammlung(
        trace="Enr Nw",
        groups="Wortschatz|Anonym|Enr Nw",
        kreis="Enr",
        ort="Nw",
    )
    ANON_ENR_OB = Sammlung(
        trace="Enr Ob",
        groups="Wortschatz|Anonym|Enr Ob",
        kreis="Enr",
        ort="Ob",
    )
    ANON_ENR_OE = Sammlung(
        trace="Enr Oe",
        groups="Wortschatz|Anonym|Enr Oe",
        kreis="Enr",
        ort="Oe",
    )
    ANON_ENR_OS = Sammlung(
        trace="Enr Os",
        groups="Wortschatz|Anonym|Enr Os",
        kreis="Enr",
        ort="Os",
    )
    ANON_ENR_PR = Sammlung(
        trace="Enr Pr",
        groups="Wortschatz|Anonym|Enr Pr",
        kreis="Enr",
        ort="Pr",
    )
    ANON_ENR_RB = Sammlung(
        trace="Enr Rb",
        groups="Wortschatz|Anonym|Enr Rb",
        kreis="Enr",
        ort="Rb",
    )
    ANON_ENR_RU = Sammlung(
        trace="Enr Ru",
        groups="Wortschatz|Anonym|Enr Ru",
        kreis="Enr",
        ort="Ru",
    )
    ANON_ENR_SC = Sammlung(
        trace="Enr Sc",
        groups="Wortschatz|Anonym|Enr Sc",
        kreis="Enr",
        ort="Sc",
    )
    ANON_ENR_SI = Sammlung(
        trace="Enr Si",
        groups="Wortschatz|Anonym|Enr Si",
        kreis="Enr",
        ort="Si",
    )
    ANON_ENR_SP = Sammlung(
        trace="Enr Sp",
        groups="Wortschatz|Anonym|Enr Sp",
        kreis="Enr",
        ort="Sp",
    )
    ANON_ENR_ST = Sammlung(
        trace="Enr St",
        groups="Wortschatz|Anonym|Enr St",
        kreis="Enr",
        ort="St",
    )
    ANON_ENR_SW = Sammlung(
        trace="Enr Sw",
        groups="Wortschatz|Anonym|Enr Sw",
        kreis="Enr",
        ort="Sw",
    )
    ANON_ENR_VE = Sammlung(
        trace="Enr Ve",
        groups="Wortschatz|Anonym|Enr Ve",
        kreis="Enr",
        ort="Ve",
    )
    ANON_ENR_VH = Sammlung(
        trace="Enr Vh",
        groups="Wortschatz|Anonym|Enr Vh",
        kreis="Enr",
        ort="Vh",
    )
    ANON_ENR_VO = Sammlung(
        trace="Enr Vo",
        groups="Wortschatz|Anonym|Enr Vo",
        kreis="Enr",
        ort="Vo",
    )
    ANON_ENR_VÖ = Sammlung(
        trace="Enr Vö",
        groups="Wortschatz|Anonym|Enr Vö",
        kreis="Enr",
        ort="Vö",
    )
    ANON_ENR_VS = Sammlung(
        trace="Enr Vs",
        groups="Wortschatz|Anonym|Enr Vs",
        kreis="Enr",
        ort="Vs",
    )
    ANON_ENR_WA = Sammlung(
        trace="Enr Wa",
        groups="Wortschatz|Anonym|Enr Wa",
        kreis="Enr",
        ort="Wa",
    )
    ANON_ENR_WE = Sammlung(
        trace="Enr We",
        groups="Wortschatz|Anonym|Enr We",
        kreis="Enr",
        ort="We",
    )
    ANON_ENR_WP = Sammlung(
        trace="Enr Wp",
        groups="Wortschatz|Anonym|Enr Wp",
        kreis="Enr",
        ort="Wp",
    )
    ANON_ENR_WT = Sammlung(
        trace="Enr Wt",
        groups="Wortschatz|Anonym|Enr Wt",
        kreis="Enr",
        ort="Wt",
    )
    ANON_ENR_ZS = Sammlung(
        trace="Enr Zs",
        groups="Wortschatz|Anonym|Enr Zs",
        kreis="Enr",
        ort="Zs",
    )
    ANON_ESS_AE = Sammlung(
        trace="Ess Ae",
        groups="Wortschatz|Anonym|Ess Ae",
        kreis="Ess",
        ort="Ae",
    )
    ANON_ESS_BB = Sammlung(
        trace="Ess Bb",
        groups="Wortschatz|Anonym|Ess Bb",
        kreis="Ess",
        ort="Bb",
    )
    ANON_ESS_BE = Sammlung(
        trace="Ess Be",
        groups="Wortschatz|Anonym|Ess Be",
        kreis="Ess",
        ort="Be",
    )
    ANON_ESS_BF = Sammlung(
        trace="Ess Bf",
        groups="Wortschatz|Anonym|Ess Bf",
        kreis="Ess",
        ort="Bf",
    )
    ANON_ESS_BH = Sammlung(
        trace="Ess Bh",
        groups="Wortschatz|Anonym|Ess Bh",
        kreis="Ess",
        ort="Bh",
    )
    ANON_ESS_ES = Sammlung(
        trace="Ess Es",
        groups="Wortschatz|Anonym|Ess Es",
        kreis="Ess",
        ort="Es",
    )
    ANON_ESS_FB = Sammlung(
        trace="Ess Fb",
        groups="Wortschatz|Anonym|Ess Fb",
        kreis="Ess",
        ort="Fb",
    )
    ANON_ESS_FR = Sammlung(
        trace="Ess Fr",
        groups="Wortschatz|Anonym|Ess Fr",
        kreis="Ess",
        ort="Fr",
    )
    ANON_ESS_HE = Sammlung(
        trace="Ess He",
        groups="Wortschatz|Anonym|Ess He",
        kreis="Ess",
        ort="He",
    )
    ANON_ESS_HH = Sammlung(
        trace="Ess Hh",
        groups="Wortschatz|Anonym|Ess Hh",
        kreis="Ess",
        ort="Hh",
    )
    ANON_ESS_KS = Sammlung(
        trace="Ess Ks",
        groups="Wortschatz|Anonym|Ess Ks",
        kreis="Ess",
        ort="Ks",
    )
    ANON_ESS_KP = Sammlung(
        trace="Ess Kp",
        groups="Wortschatz|Anonym|Ess Kp",
        kreis="Ess",
        ort="Kp",
    )
    ANON_ESS_OF = Sammlung(
        trace="Ess Of",
        groups="Wortschatz|Anonym|Ess Of",
        kreis="Ess",
        ort="Of",
    )
    ANON_ESS_OH = Sammlung(
        trace="Ess Oh",
        groups="Wortschatz|Anonym|Ess Oh",
        kreis="Ess",
        ort="Oh",
    )
    ANON_ESS_RE = Sammlung(
        trace="Ess Re",
        groups="Wortschatz|Anonym|Ess Re",
        kreis="Ess",
        ort="Re",
    )
    ANON_ESS_SB = Sammlung(
        trace="Ess Sb",
        groups="Wortschatz|Anonym|Ess Sb",
        kreis="Ess",
        ort="Sb",
    )
    ANON_ESS_SR = Sammlung(
        trace="Ess Sr",
        groups="Wortschatz|Anonym|Ess Sr",
        kreis="Ess",
        ort="Sr",
    )
    ANON_ESS_ST = Sammlung(
        trace="Ess St",
        groups="Wortschatz|Anonym|Ess St",
        kreis="Ess",
        ort="St",
    )
    ANON_ESS_ÜR = Sammlung(
        trace="Ess Ür",
        groups="Wortschatz|Anonym|Ess Ür",
        kreis="Ess",
        ort="Ür",
    )
    ANON_GEL_BK = Sammlung(
        trace="Gel Bk",
        groups="Wortschatz|Anonym|Gel Bk",
        kreis="Gel",
        ort="Bk",
    )
    ANON_GEL_BS = Sammlung(
        trace="Gel Bs",
        groups="Wortschatz|Anonym|Gel Bs",
        kreis="Gel",
        ort="Bs",
    )
    ANON_GEL_BU = Sammlung(
        trace="Gel Bu",
        groups="Wortschatz|Anonym|Gel Bu",
        kreis="Gel",
        ort="Bu",
    )
    ANON_GEL_BX = Sammlung(
        trace="Gel Bx",
        groups="Wortschatz|Anonym|Gel Bx",
        kreis="Gel",
        ort="Bx",
    )
    ANON_GEL_GK = Sammlung(
        trace="Gel Gk",
        groups="Wortschatz|Anonym|Gel Gk",
        kreis="Gel",
        ort="Gk",
    )
    ANON_GEL_HA = Sammlung(
        trace="Gel Ha",
        groups="Wortschatz|Anonym|Gel Ha",
        kreis="Gel",
        ort="Ha",
    )
    ANON_GEL_HE = Sammlung(
        trace="Gel He",
        groups="Wortschatz|Anonym|Gel He",
        kreis="Gel",
        ort="He",
    )
    ANON_GEL_HH = Sammlung(
        trace="Gel Hh",
        groups="Wortschatz|Anonym|Gel Hh",
        kreis="Gel",
        ort="Hh",
    )
    ANON_GEL_HM = Sammlung(
        trace="Gel Hm",
        groups="Wortschatz|Anonym|Gel Hm",
        kreis="Gel",
        ort="Hm",
    )
    ANON_GEL_LT = Sammlung(
        trace="Gel Lt",
        groups="Wortschatz|Anonym|Gel Lt",
        kreis="Gel",
        ort="Lt",
    )
    ANON_GEL_RH = Sammlung(
        trace="Gel Rh",
        groups="Wortschatz|Anonym|Gel Rh",
        kreis="Gel",
        ort="Rh",
    )
    ANON_GEL_ST = Sammlung(
        trace="Gel St",
        groups="Wortschatz|Anonym|Gel St",
        kreis="Gel",
        ort="St",
    )
    ANON_GEL_ÜD = Sammlung(
        trace="Gel Üd",
        groups="Wortschatz|Anonym|Gel Üd",
        kreis="Gel",
        ort="Üd",
    )
    ANON_GEL_WA = Sammlung(
        trace="Gel Wa",
        groups="Wortschatz|Anonym|Gel Wa",
        kreis="Gel",
        ort="Wa",
    )
    ANON_GEL_WE = Sammlung(
        trace="Gel We",
        groups="Wortschatz|Anonym|Gel We",
        kreis="Gel",
        ort="We",
    )
    ANON_HAG_BO = Sammlung(
        trace="Hag Bo",
        groups="Wortschatz|Anonym|Hag Bo",
        kreis="Hag",
        ort="Bo",
    )
    ANON_HAG_EI = Sammlung(
        trace="Hag Ei",
        groups="Wortschatz|Anonym|Hag Ei",
        kreis="Hag",
        ort="Ei",
    )
    ANON_HAG_EP = Sammlung(
        trace="Hag Ep",
        groups="Wortschatz|Anonym|Hag Ep",
        kreis="Hag",
        ort="Ep",
    )
    ANON_HAG_HA = Sammlung(
        trace="Hag Ha",
        groups="Wortschatz|Anonym|Hag Ha",
        kreis="Hag",
        ort="Ha",
    )
    ANON_HAG_HG = Sammlung(
        trace="Hag Hg",
        groups="Wortschatz|Anonym|Hag Hg",
        kreis="Hag",
        ort="Hg",
    )
    ANON_HAG_HS = Sammlung(
        trace="Hag Hs",
        groups="Wortschatz|Anonym|Hag Hs",
        kreis="Hag",
        ort="Hs",
    )
    ANON_HAG_VH = Sammlung(
        trace="Hag Vh",
        groups="Wortschatz|Anonym|Hag Vh",
        kreis="Hag",
        ort="Vh",
    )
    ANON_HAL_AH = Sammlung(
        trace="Hal Ah",
        groups="Wortschatz|Anonym|Hal Ah",
        kreis="Hal",
        ort="Ah",
    )
    ANON_HAL_BC = Sammlung(
        trace="Hal Bc",
        groups="Wortschatz|Anonym|Hal Bc",
        kreis="Hal",
        ort="Bc",
    )
    ANON_HAL_BH = Sammlung(
        trace="Hal Bh",
        groups="Wortschatz|Anonym|Hal Bh",
        kreis="Hal",
        ort="Bh",
    )
    ANON_HAL_BK = Sammlung(
        trace="Hal Bk",
        groups="Wortschatz|Anonym|Hal Bk",
        kreis="Hal",
        ort="Bk",
    )
    ANON_HAL_BO = Sammlung(
        trace="Hal Bo",
        groups="Wortschatz|Anonym|Hal Bo",
        kreis="Hal",
        ort="Bo",
    )
    ANON_HAL_BV = Sammlung(
        trace="Hal Bv",
        groups="Wortschatz|Anonym|Hal Bv",
        kreis="Hal",
        ort="Bv",
    )
    ANON_HAL_EB = Sammlung(
        trace="Hal Eb",
        groups="Wortschatz|Anonym|Hal Eb",
        kreis="Hal",
        ort="Eb",
    )
    ANON_HAL_GA = Sammlung(
        trace="Hal Ga",
        groups="Wortschatz|Anonym|Hal Ga",
        kreis="Hal",
        ort="Ga",
    )
    ANON_HAL_HA = Sammlung(
        trace="Hal Ha",
        groups="Wortschatz|Anonym|Hal Ha",
        kreis="Hal",
        ort="Ha",
    )
    ANON_HAL_HE = Sammlung(
        trace="Hal He",
        groups="Wortschatz|Anonym|Hal He",
        kreis="Hal",
        ort="He",
    )
    ANON_HAL_HG = Sammlung(
        trace="Hal Hg",
        groups="Wortschatz|Anonym|Hal Hg",
        kreis="Hal",
        ort="Hg",
    )
    ANON_HAL_HÖ = Sammlung(
        trace="Hal Hö",
        groups="Wortschatz|Anonym|Hal Hö",
        kreis="Hal",
        ort="Hö",
    )
    ANON_HAL_HT = Sammlung(
        trace="Hal Ht",
        groups="Wortschatz|Anonym|Hal Ht",
        kreis="Hal",
        ort="Ht",
    )
    ANON_HAL_IS = Sammlung(
        trace="Hal Is",
        groups="Wortschatz|Anonym|Hal Is",
        kreis="Hal",
        ort="Is",
    )
    ANON_HAL_KA = Sammlung(
        trace="Hal Ka",
        groups="Wortschatz|Anonym|Hal Ka",
        kreis="Hal",
        ort="Ka",
    )
    ANON_HAL_KK = Sammlung(
        trace="Hal Kk",
        groups="Wortschatz|Anonym|Hal Kk",
        kreis="Hal",
        ort="Kk",
    )
    ANON_HAL_KL = Sammlung(
        trace="Hal Kl",
        groups="Wortschatz|Anonym|Hal Kl",
        kreis="Hal",
        ort="Kl",
    )
    ANON_HAL_KO = Sammlung(
        trace="Hal Ko",
        groups="Wortschatz|Anonym|Hal Ko",
        kreis="Hal",
        ort="Ko",
    )
    ANON_HAL_KÜ = Sammlung(
        trace="Hal Kü",
        groups="Wortschatz|Anonym|Hal Kü",
        kreis="Hal",
        ort="Kü",
    )
    ANON_HAL_LH = Sammlung(
        trace="Hal Lh",
        groups="Wortschatz|Anonym|Hal Lh",
        kreis="Hal",
        ort="Lh",
    )
    ANON_HAL_LO = Sammlung(
        trace="Hal Lo",
        groups="Wortschatz|Anonym|Hal Lo",
        kreis="Hal",
        ort="Lo",
    )
    ANON_HAL_OD = Sammlung(
        trace="Hal Od",
        groups="Wortschatz|Anonym|Hal Od",
        kreis="Hal",
        ort="Od",
    )
    ANON_HAL_ÖW = Sammlung(
        trace="Hal Öw",
        groups="Wortschatz|Anonym|Hal Öw",
        kreis="Hal",
        ort="Öw",
    )
    ANON_HAL_PH = Sammlung(
        trace="Hal Ph",
        groups="Wortschatz|Anonym|Hal Ph",
        kreis="Hal",
        ort="Ph",
    )
    ANON_HAL_PL = Sammlung(
        trace="Hal Pl",
        groups="Wortschatz|Anonym|Hal Pl",
        kreis="Hal",
        ort="Pl",
    )
    ANON_HAL_RA = Sammlung(
        trace="Hal Ra",
        groups="Wortschatz|Anonym|Hal Ra",
        kreis="Hal",
        ort="Ra",
    )
    ANON_HAL_SF = Sammlung(
        trace="Hal Sf",
        groups="Wortschatz|Anonym|Hal Sf",
        kreis="Hal",
        ort="Sf",
    )
    ANON_HAL_SH = Sammlung(
        trace="Hal Sh",
        groups="Wortschatz|Anonym|Hal Sh",
        kreis="Hal",
        ort="Sh",
    )
    ANON_HAL_SI = Sammlung(
        trace="Hal Si",
        groups="Wortschatz|Anonym|Hal Si",
        kreis="Hal",
        ort="Si",
    )
    ANON_HAL_SR = Sammlung(
        trace="Hal Sr",
        groups="Wortschatz|Anonym|Hal Sr",
        kreis="Hal",
        ort="Sr",
    )
    ANON_HAL_ST = Sammlung(
        trace="Hal St",
        groups="Wortschatz|Anonym|Hal St",
        kreis="Hal",
        ort="St",
    )
    ANON_HAL_TH = Sammlung(
        trace="Hal Th",
        groups="Wortschatz|Anonym|Hal Th",
        kreis="Hal",
        ort="Th",
    )
    ANON_HAL_VM = Sammlung(
        trace="Hal Vm",
        groups="Wortschatz|Anonym|Hal Vm",
        kreis="Hal",
        ort="Vm",
    )
    ANON_HAL_WE = Sammlung(
        trace="Hal We",
        groups="Wortschatz|Anonym|Hal We",
        kreis="Hal",
        ort="We",
    )
    ANON_HFD_AL = Sammlung(
        trace="Hfd Al",
        groups="Wortschatz|Anonym|Hfd Al",
        kreis="Hfd",
        ort="Al",
    )
    ANON_HFD_BB = Sammlung(
        trace="Hfd Bb",
        groups="Wortschatz|Anonym|Hfd Bb",
        kreis="Hfd",
        ort="Bb",
    )
    ANON_HFD_BI = Sammlung(
        trace="Hfd Bi",
        groups="Wortschatz|Anonym|Hfd Bi",
        kreis="Hfd",
        ort="Bi",
    )
    ANON_HFD_BK = Sammlung(
        trace="Hfd Bk",
        groups="Wortschatz|Anonym|Hfd Bk",
        kreis="Hfd",
        ort="Bk",
    )
    ANON_HFD_BO = Sammlung(
        trace="Hfd Bo",
        groups="Wortschatz|Anonym|Hfd Bo",
        kreis="Hfd",
        ort="Bo",
    )
    ANON_HFD_BR = Sammlung(
        trace="Hfd Br",
        groups="Wortschatz|Anonym|Hfd Br",
        kreis="Hfd",
        ort="Br",
    )
    ANON_HFD_BU = Sammlung(
        trace="Hfd Bu",
        groups="Wortschatz|Anonym|Hfd Bu",
        kreis="Hfd",
        ort="Bu",
    )
    ANON_HFD_BÜ = Sammlung(
        trace="Hfd Bü",
        groups="Wortschatz|Anonym|Hfd Bü",
        kreis="Hfd",
        ort="Bü",
    )
    ANON_HFD_DB = Sammlung(
        trace="Hfd Db",
        groups="Wortschatz|Anonym|Hfd Db",
        kreis="Hfd",
        ort="Db",
    )
    ANON_HFD_DD = Sammlung(
        trace="Hfd Dd",
        groups="Wortschatz|Anonym|Hfd Dd",
        kreis="Hfd",
        ort="Dd",
    )
    ANON_HFD_DH = Sammlung(
        trace="Hfd Dh",
        groups="Wortschatz|Anonym|Hfd Dh",
        kreis="Hfd",
        ort="Dh",
    )
    ANON_HFD_DO = Sammlung(
        trace="Hfd Do",
        groups="Wortschatz|Anonym|Hfd Do",
        kreis="Hfd",
        ort="Do",
    )
    ANON_HFD_DR = Sammlung(
        trace="Hfd Dr",
        groups="Wortschatz|Anonym|Hfd Dr",
        kreis="Hfd",
        ort="Dr",
    )
    ANON_HFD_DÜ = Sammlung(
        trace="Hfd Dü",
        groups="Wortschatz|Anonym|Hfd Dü",
        kreis="Hfd",
        ort="Dü",
    )
    ANON_HFD_EB = Sammlung(
        trace="Hfd Eb",
        groups="Wortschatz|Anonym|Hfd Eb",
        kreis="Hfd",
        ort="Eb",
    )
    ANON_HFD_ED = Sammlung(
        trace="Hfd Ed",
        groups="Wortschatz|Anonym|Hfd Ed",
        kreis="Hfd",
        ort="Ed",
    )
    ANON_HFD_EH = Sammlung(
        trace="Hfd Eh",
        groups="Wortschatz|Anonym|Hfd Eh",
        kreis="Hfd",
        ort="Eh",
    )
    ANON_HFD_EI = Sammlung(
        trace="Hfd Ei",
        groups="Wortschatz|Anonym|Hfd Ei",
        kreis="Hfd",
        ort="Ei",
    )
    ANON_HFD_EL = Sammlung(
        trace="Hfd El",
        groups="Wortschatz|Anonym|Hfd El",
        kreis="Hfd",
        ort="El",
    )
    ANON_HFD_EN = Sammlung(
        trace="Hfd En",
        groups="Wortschatz|Anonym|Hfd En",
        kreis="Hfd",
        ort="En",
    )
    ANON_HFD_EX = Sammlung(
        trace="Hfd Ex",
        groups="Wortschatz|Anonym|Hfd Ex",
        kreis="Hfd",
        ort="Ex",
    )
    ANON_HFD_FA = Sammlung(
        trace="Hfd Fa",
        groups="Wortschatz|Anonym|Hfd Fa",
        kreis="Hfd",
        ort="Fa",
    )
    ANON_HFD_FD = Sammlung(
        trace="Hfd Fd",
        groups="Wortschatz|Anonym|Hfd Fd",
        kreis="Hfd",
        ort="Fd",
    )
    ANON_HFD_GO = Sammlung(
        trace="Hfd Go",
        groups="Wortschatz|Anonym|Hfd Go",
        kreis="Hfd",
        ort="Go",
    )
    ANON_HFD_HA = Sammlung(
        trace="Hfd Ha",
        groups="Wortschatz|Anonym|Hfd Ha",
        kreis="Hfd",
        ort="Ha",
    )
    ANON_HFD_HÄ = Sammlung(
        trace="Hfd Hä",
        groups="Wortschatz|Anonym|Hfd Hä",
        kreis="Hfd",
        ort="Hä",
    )
    ANON_HFD_HB = Sammlung(
        trace="Hfd Hb",
        groups="Wortschatz|Anonym|Hfd Hb",
        kreis="Hfd",
        ort="Hb",
    )
    ANON_HFD_HF = Sammlung(
        trace="Hfd Hf",
        groups="Wortschatz|Anonym|Hfd Hf",
        kreis="Hfd",
        ort="Hf",
    )
    ANON_HFD_HH = Sammlung(
        trace="Hfd Hh",
        groups="Wortschatz|Anonym|Hfd Hh",
        kreis="Hfd",
        ort="Hh",
    )
    ANON_HFD_HI = Sammlung(
        trace="Hfd Hi",
        groups="Wortschatz|Anonym|Hfd Hi",
        kreis="Hfd",
        ort="Hi",
    )
    ANON_HFD_HO = Sammlung(
        trace="Hfd Ho",
        groups="Wortschatz|Anonym|Hfd Ho",
        kreis="Hfd",
        ort="Ho",
    )
    ANON_HFD_HS = Sammlung(
        trace="Hfd Hs",
        groups="Wortschatz|Anonym|Hfd Hs",
        kreis="Hfd",
        ort="Hs",
    )
    ANON_HFD_HU = Sammlung(
        trace="Hfd Hu",
        groups="Wortschatz|Anonym|Hfd Hu",
        kreis="Hfd",
        ort="Hu",
    )
    ANON_HFD_HÜ = Sammlung(
        trace="Hfd Hü",
        groups="Wortschatz|Anonym|Hfd Hü",
        kreis="Hfd",
        ort="Hü",
    )
    ANON_HFD_HW = Sammlung(
        trace="Hfd Hw",
        groups="Wortschatz|Anonym|Hfd Hw",
        kreis="Hfd",
        ort="Hw",
    )
    ANON_HFD_KL = Sammlung(
        trace="Hfd Kl",
        groups="Wortschatz|Anonym|Hfd Kl",
        kreis="Hfd",
        ort="Kl",
    )
    ANON_HFD_LA = Sammlung(
        trace="Hfd La",
        groups="Wortschatz|Anonym|Hfd La",
        kreis="Hfd",
        ort="La",
    )
    ANON_HFD_LH = Sammlung(
        trace="Hfd Lh",
        groups="Wortschatz|Anonym|Hfd Lh",
        kreis="Hfd",
        ort="Lh",
    )
    ANON_HFD_LÖ = Sammlung(
        trace="Hfd Lö",
        groups="Wortschatz|Anonym|Hfd Lö",
        kreis="Hfd",
        ort="Lö",
    )
    ANON_HFD_LZ = Sammlung(
        trace="Hfd Lz",
        groups="Wortschatz|Anonym|Hfd Lz",
        kreis="Hfd",
        ort="Lz",
    )
    ANON_HFD_MA = Sammlung(
        trace="Hfd Ma",
        groups="Wortschatz|Anonym|Hfd Ma",
        kreis="Hfd",
        ort="Ma",
    )
    ANON_HFD_MB = Sammlung(
        trace="Hfd Mb",
        groups="Wortschatz|Anonym|Hfd Mb",
        kreis="Hfd",
        ort="Mb",
    )
    ANON_HFD_MC = Sammlung(
        trace="Hfd Mc",
        groups="Wortschatz|Anonym|Hfd Mc",
        kreis="Hfd",
        ort="Mc",
    )
    ANON_HFD_MH = Sammlung(
        trace="Hfd Mh",
        groups="Wortschatz|Anonym|Hfd Mh",
        kreis="Hfd",
        ort="Mh",
    )
    ANON_HFD_MT = Sammlung(
        trace="Hfd Mt",
        groups="Wortschatz|Anonym|Hfd Mt",
        kreis="Hfd",
        ort="Mt",
    )
    ANON_HFD_NS = Sammlung(
        trace="Hfd Ns",
        groups="Wortschatz|Anonym|Hfd Ns",
        kreis="Hfd",
        ort="Ns",
    )
    ANON_HFD_OB = Sammlung(
        trace="Hfd Ob",
        groups="Wortschatz|Anonym|Hfd Ob",
        kreis="Hfd",
        ort="Ob",
    )
    ANON_HFD_OH = Sammlung(
        trace="Hfd Oh",
        groups="Wortschatz|Anonym|Hfd Oh",
        kreis="Hfd",
        ort="Oh",
    )
    ANON_HFD_ÖH = Sammlung(
        trace="Hfd Öh",
        groups="Wortschatz|Anonym|Hfd Öh",
        kreis="Hfd",
        ort="Öh",
    )
    ANON_HFD_OK = Sammlung(
        trace="Hfd Ok",
        groups="Wortschatz|Anonym|Hfd Ok",
        kreis="Hfd",
        ort="Ok",
    )
    ANON_HFD_OS = Sammlung(
        trace="Hfd Os",
        groups="Wortschatz|Anonym|Hfd Os",
        kreis="Hfd",
        ort="Os",
    )
    ANON_HFD_PH = Sammlung(
        trace="Hfd Ph",
        groups="Wortschatz|Anonym|Hfd Ph",
        kreis="Hfd",
        ort="Ph",
    )
    ANON_HFD_QH = Sammlung(
        trace="Hfd Qh",
        groups="Wortschatz|Anonym|Hfd Qh",
        kreis="Hfd",
        ort="Qh",
    )
    ANON_HFD_RH = Sammlung(
        trace="Hfd Rh",
        groups="Wortschatz|Anonym|Hfd Rh",
        kreis="Hfd",
        ort="Rh",
    )
    ANON_HFD_RL = Sammlung(
        trace="Hfd Rl",
        groups="Wortschatz|Anonym|Hfd Rl",
        kreis="Hfd",
        ort="Rl",
    )
    ANON_HFD_SB = Sammlung(
        trace="Hfd Sb",
        groups="Wortschatz|Anonym|Hfd Sb",
        kreis="Hfd",
        ort="Sb",
    )
    ANON_HFD_SC = Sammlung(
        trace="Hfd Sc",
        groups="Wortschatz|Anonym|Hfd Sc",
        kreis="Hfd",
        ort="Sc",
    )
    ANON_HFD_SD = Sammlung(
        trace="Hfd Sd",
        groups="Wortschatz|Anonym|Hfd Sd",
        kreis="Hfd",
        ort="Sd",
    )
    ANON_HFD_SG = Sammlung(
        trace="Hfd Sg",
        groups="Wortschatz|Anonym|Hfd Sg",
        kreis="Hfd",
        ort="Sg",
    )
    ANON_HFD_SI = Sammlung(
        trace="Hfd Si",
        groups="Wortschatz|Anonym|Hfd Si",
        kreis="Hfd",
        ort="Si",
    )
    ANON_HFD_SL = Sammlung(
        trace="Hfd Sl",
        groups="Wortschatz|Anonym|Hfd Sl",
        kreis="Hfd",
        ort="Sl",
    )
    ANON_HFD_SP = Sammlung(
        trace="Hfd Sp",
        groups="Wortschatz|Anonym|Hfd Sp",
        kreis="Hfd",
        ort="Sp",
    )
    ANON_HFD_ST = Sammlung(
        trace="Hfd St",
        groups="Wortschatz|Anonym|Hfd St",
        kreis="Hfd",
        ort="St",
    )
    ANON_HFD_SU = Sammlung(
        trace="Hfd Su",
        groups="Wortschatz|Anonym|Hfd Su",
        kreis="Hfd",
        ort="Su",
    )
    ANON_HFD_SW = Sammlung(
        trace="Hfd Sw",
        groups="Wortschatz|Anonym|Hfd Sw",
        kreis="Hfd",
        ort="Sw",
    )
    ANON_HFD_VD = Sammlung(
        trace="Hfd Vd",
        groups="Wortschatz|Anonym|Hfd Vd",
        kreis="Hfd",
        ort="Vd",
    )
    ANON_HFD_VL = Sammlung(
        trace="Hfd Vl",
        groups="Wortschatz|Anonym|Hfd Vl",
        kreis="Hfd",
        ort="Vl",
    )
    ANON_HFD_WA = Sammlung(
        trace="Hfd Wa",
        groups="Wortschatz|Anonym|Hfd Wa",
        kreis="Hfd",
        ort="Wa",
    )
    ANON_HFD_WD = Sammlung(
        trace="Hfd Wd",
        groups="Wortschatz|Anonym|Hfd Wd",
        kreis="Hfd",
        ort="Wd",
    )
    ANON_HFD_WE = Sammlung(
        trace="Hfd We",
        groups="Wortschatz|Anonym|Hfd We",
        kreis="Hfd",
        ort="We",
    )
    ANON_HFD_WF = Sammlung(
        trace="Hfd Wf",
        groups="Wortschatz|Anonym|Hfd Wf",
        kreis="Hfd",
        ort="Wf",
    )
    ANON_HFD_WK = Sammlung(
        trace="Hfd Wk",
        groups="Wortschatz|Anonym|Hfd Wk",
        kreis="Hfd",
        ort="Wk",
    )
    ANON_HÖX_AB = Sammlung(
        trace="Höx Ab",
        groups="Wortschatz|Anonym|Höx Ab",
        kreis="Höx",
        ort="Ab",
    )
    ANON_HÖX_AH = Sammlung(
        trace="Höx Ah",
        groups="Wortschatz|Anonym|Höx Ah",
        kreis="Höx",
        ort="Ah",
    )
    ANON_HÖX_AL = Sammlung(
        trace="Höx Al",
        groups="Wortschatz|Anonym|Höx Al",
        kreis="Höx",
        ort="Al",
    )
    ANON_HÖX_AM = Sammlung(
        trace="Höx Am",
        groups="Wortschatz|Anonym|Höx Am",
        kreis="Höx",
        ort="Am",
    )
    ANON_HÖX_BB = Sammlung(
        trace="Höx Bb",
        groups="Wortschatz|Anonym|Höx Bb",
        kreis="Höx",
        ort="Bb",
    )
    ANON_HÖX_BE = Sammlung(
        trace="Höx Be",
        groups="Wortschatz|Anonym|Höx Be",
        kreis="Höx",
        ort="Be",
    )
    ANON_HÖX_BG = Sammlung(
        trace="Höx Bg",
        groups="Wortschatz|Anonym|Höx Bg",
        kreis="Höx",
        ort="Bg",
    )
    ANON_HÖX_BH = Sammlung(
        trace="Höx Bh",
        groups="Wortschatz|Anonym|Höx Bh",
        kreis="Höx",
        ort="Bh",
    )
    ANON_HÖX_BL = Sammlung(
        trace="Höx Bl",
        groups="Wortschatz|Anonym|Höx Bl",
        kreis="Höx",
        ort="Bl",
    )
    ANON_HÖX_BO = Sammlung(
        trace="Höx Bo",
        groups="Wortschatz|Anonym|Höx Bo",
        kreis="Höx",
        ort="Bo",
    )
    ANON_HÖX_BÖ = Sammlung(
        trace="Höx Bö",
        groups="Wortschatz|Anonym|Höx Bö",
        kreis="Höx",
        ort="Bö",
    )
    ANON_HÖX_BR = Sammlung(
        trace="Höx Br",
        groups="Wortschatz|Anonym|Höx Br",
        kreis="Höx",
        ort="Br",
    )
    ANON_HÖX_BS = Sammlung(
        trace="Höx Bs",
        groups="Wortschatz|Anonym|Höx Bs",
        kreis="Höx",
        ort="Bs",
    )
    ANON_HÖX_BV = Sammlung(
        trace="Höx Bv",
        groups="Wortschatz|Anonym|Höx Bv",
        kreis="Höx",
        ort="Bv",
    )
    ANON_HÖX_BX = Sammlung(
        trace="Höx Bx",
        groups="Wortschatz|Anonym|Höx Bx",
        kreis="Höx",
        ort="Bx",
    )
    ANON_HÖX_DB = Sammlung(
        trace="Höx Db",
        groups="Wortschatz|Anonym|Höx Db",
        kreis="Höx",
        ort="Db",
    )
    ANON_HÖX_DH = Sammlung(
        trace="Höx Dh",
        groups="Wortschatz|Anonym|Höx Dh",
        kreis="Höx",
        ort="Dh",
    )
    ANON_HÖX_DR = Sammlung(
        trace="Höx Dr",
        groups="Wortschatz|Anonym|Höx Dr",
        kreis="Höx",
        ort="Dr",
    )
    ANON_HÖX_EN = Sammlung(
        trace="Höx En",
        groups="Wortschatz|Anonym|Höx En",
        kreis="Höx",
        ort="En",
    )
    ANON_HÖX_ER = Sammlung(
        trace="Höx Er",
        groups="Wortschatz|Anonym|Höx Er",
        kreis="Höx",
        ort="Er",
    )
    ANON_HÖX_FR = Sammlung(
        trace="Höx Fr",
        groups="Wortschatz|Anonym|Höx Fr",
        kreis="Höx",
        ort="Fr",
    )
    ANON_HÖX_FÜ = Sammlung(
        trace="Höx Fü",
        groups="Wortschatz|Anonym|Höx Fü",
        kreis="Höx",
        ort="Fü",
    )
    ANON_HÖX_GH = Sammlung(
        trace="Höx Gh",
        groups="Wortschatz|Anonym|Höx Gh",
        kreis="Höx",
        ort="Gh",
    )
    ANON_HÖX_HA = Sammlung(
        trace="Höx Ha",
        groups="Wortschatz|Anonym|Höx Ha",
        kreis="Höx",
        ort="Ha",
    )
    ANON_HÖX_HB = Sammlung(
        trace="Höx Hb",
        groups="Wortschatz|Anonym|Höx Hb",
        kreis="Höx",
        ort="Hb",
    )
    ANON_HÖX_HD = Sammlung(
        trace="Höx Hd",
        groups="Wortschatz|Anonym|Höx Hd",
        kreis="Höx",
        ort="Hd",
    )
    ANON_HÖX_HE = Sammlung(
        trace="Höx He",
        groups="Wortschatz|Anonym|Höx He",
        kreis="Höx",
        ort="He",
    )
    ANON_HÖX_HH = Sammlung(
        trace="Höx Hh",
        groups="Wortschatz|Anonym|Höx Hh",
        kreis="Höx",
        ort="Hh",
    )
    ANON_HÖX_HI = Sammlung(
        trace="Höx Hi",
        groups="Wortschatz|Anonym|Höx Hi",
        kreis="Höx",
        ort="Hi",
    )
    ANON_HÖX_HM = Sammlung(
        trace="Höx Hm",
        groups="Wortschatz|Anonym|Höx Hm",
        kreis="Höx",
        ort="Hm",
    )
    ANON_HÖX_HO = Sammlung(
        trace="Höx Ho",
        groups="Wortschatz|Anonym|Höx Ho",
        kreis="Höx",
        ort="Ho",
    )
    ANON_HÖX_HR = Sammlung(
        trace="Höx Hr",
        groups="Wortschatz|Anonym|Höx Hr",
        kreis="Höx",
        ort="Hr",
    )
    ANON_HÖX_HS = Sammlung(
        trace="Höx Hs",
        groups="Wortschatz|Anonym|Höx Hs",
        kreis="Höx",
        ort="Hs",
    )
    ANON_HÖX_HX = Sammlung(
        trace="Höx Hx",
        groups="Wortschatz|Anonym|Höx Hx",
        kreis="Höx",
        ort="Hx",
    )
    ANON_HÖX_IS = Sammlung(
        trace="Höx Is",
        groups="Wortschatz|Anonym|Höx Is",
        kreis="Höx",
        ort="Is",
    )
    ANON_HÖX_KB = Sammlung(
        trace="Höx Kb",
        groups="Wortschatz|Anonym|Höx Kb",
        kreis="Höx",
        ort="Kb",
    )
    ANON_HÖX_KO = Sammlung(
        trace="Höx Ko",
        groups="Wortschatz|Anonym|Höx Ko",
        kreis="Höx",
        ort="Ko",
    )
    ANON_HÖX_LD = Sammlung(
        trace="Höx Ld",
        groups="Wortschatz|Anonym|Höx Ld",
        kreis="Höx",
        ort="Ld",
    )
    ANON_HÖX_LM = Sammlung(
        trace="Höx Lm",
        groups="Wortschatz|Anonym|Höx Lm",
        kreis="Höx",
        ort="Lm",
    )
    ANON_HÖX_LÖ = Sammlung(
        trace="Höx Lö",
        groups="Wortschatz|Anonym|Höx Lö",
        kreis="Höx",
        ort="Lö",
    )
    ANON_HÖX_LÜ = Sammlung(
        trace="Höx Lü",
        groups="Wortschatz|Anonym|Höx Lü",
        kreis="Höx",
        ort="Lü",
    )
    ANON_HÖX_MB = Sammlung(
        trace="Höx Mb",
        groups="Wortschatz|Anonym|Höx Mb",
        kreis="Höx",
        ort="Mb",
    )
    ANON_HÖX_MH = Sammlung(
        trace="Höx Mh",
        groups="Wortschatz|Anonym|Höx Mh",
        kreis="Höx",
        ort="Mh",
    )
    ANON_HÖX_OB = Sammlung(
        trace="Höx Ob",
        groups="Wortschatz|Anonym|Höx Ob",
        kreis="Höx",
        ort="Ob",
    )
    ANON_HÖX_OE = Sammlung(
        trace="Höx Oe",
        groups="Wortschatz|Anonym|Höx Oe",
        kreis="Höx",
        ort="Oe",
    )
    ANON_HÖX_OH = Sammlung(
        trace="Höx Oh",
        groups="Wortschatz|Anonym|Höx Oh",
        kreis="Höx",
        ort="Oh",
    )
    ANON_HÖX_OT = Sammlung(
        trace="Höx Ot",
        groups="Wortschatz|Anonym|Höx Ot",
        kreis="Höx",
        ort="Ot",
    )
    ANON_HÖX_PÖ = Sammlung(
        trace="Höx Pö",
        groups="Wortschatz|Anonym|Höx Pö",
        kreis="Höx",
        ort="Pö",
    )
    ANON_HÖX_RE = Sammlung(
        trace="Höx Re",
        groups="Wortschatz|Anonym|Höx Re",
        kreis="Höx",
        ort="Re",
    )
    ANON_HÖX_RH = Sammlung(
        trace="Höx Rh",
        groups="Wortschatz|Anonym|Höx Rh",
        kreis="Höx",
        ort="Rh",
    )
    ANON_HÖX_RI = Sammlung(
        trace="Höx Ri",
        groups="Wortschatz|Anonym|Höx Ri",
        kreis="Höx",
        ort="Ri",
    )
    ANON_HÖX_RO = Sammlung(
        trace="Höx Ro",
        groups="Wortschatz|Anonym|Höx Ro",
        kreis="Höx",
        ort="Ro",
    )
    ANON_HÖX_SB = Sammlung(
        trace="Höx Sb",
        groups="Wortschatz|Anonym|Höx Sb",
        kreis="Höx",
        ort="Sb",
    )
    ANON_HÖX_SH = Sammlung(
        trace="Höx Sh",
        groups="Wortschatz|Anonym|Höx Sh",
        kreis="Höx",
        ort="Sh",
    )
    ANON_HÖX_SM = Sammlung(
        trace="Höx Sm",
        groups="Wortschatz|Anonym|Höx Sm",
        kreis="Höx",
        ort="Sm",
    )
    ANON_HÖX_SS = Sammlung(
        trace="Höx Ss",
        groups="Wortschatz|Anonym|Höx Ss",
        kreis="Höx",
        ort="Ss",
    )
    ANON_HÖX_TI = Sammlung(
        trace="Höx Ti",
        groups="Wortschatz|Anonym|Höx Ti",
        kreis="Höx",
        ort="Ti",
    )
    ANON_HÖX_VB = Sammlung(
        trace="Höx Vb",
        groups="Wortschatz|Anonym|Höx Vb",
        kreis="Höx",
        ort="Vb",
    )
    ANON_HÖX_VÖ = Sammlung(
        trace="Höx Vö",
        groups="Wortschatz|Anonym|Höx Vö",
        kreis="Höx",
        ort="Vö",
    )
    ANON_HÖX_WE = Sammlung(
        trace="Höx We",
        groups="Wortschatz|Anonym|Höx We",
        kreis="Höx",
        ort="We",
    )
    ANON_HÖX_WÜ = Sammlung(
        trace="Höx Wü",
        groups="Wortschatz|Anonym|Höx Wü",
        kreis="Höx",
        ort="Wü",
    )
    ANON_ISL_AP = Sammlung(
        trace="Isl Ap",
        groups="Wortschatz|Anonym|Isl Ap",
        kreis="Isl",
        ort="Ap",
    )
    ANON_ISL_BB = Sammlung(
        trace="Isl Bb",
        groups="Wortschatz|Anonym|Isl Bb",
        kreis="Isl",
        ort="Bb",
    )
    ANON_ISL_BC = Sammlung(
        trace="Isl Bc",
        groups="Wortschatz|Anonym|Isl Bc",
        kreis="Isl",
        ort="Bc",
    )
    ANON_ISL_BD = Sammlung(
        trace="Isl Bd",
        groups="Wortschatz|Anonym|Isl Bd",
        kreis="Isl",
        ort="Bd",
    )
    ANON_ISL_BE = Sammlung(
        trace="Isl Be",
        groups="Wortschatz|Anonym|Isl Be",
        kreis="Isl",
        ort="Be",
    )
    ANON_ISL_BG = Sammlung(
        trace="Isl Bg",
        groups="Wortschatz|Anonym|Isl Bg",
        kreis="Isl",
        ort="Bg",
    )
    ANON_ISL_BH = Sammlung(
        trace="Isl Bh",
        groups="Wortschatz|Anonym|Isl Bh",
        kreis="Isl",
        ort="Bh",
    )
    ANON_ISL_BK = Sammlung(
        trace="Isl Bk",
        groups="Wortschatz|Anonym|Isl Bk",
        kreis="Isl",
        ort="Bk",
    )
    ANON_ISL_BÖ = Sammlung(
        trace="Isl Bö",
        groups="Wortschatz|Anonym|Isl Bö",
        kreis="Isl",
        ort="Bö",
    )
    ANON_ISL_BP = Sammlung(
        trace="Isl Bp",
        groups="Wortschatz|Anonym|Isl Bp",
        kreis="Isl",
        ort="Bp",
    )
    ANON_ISL_BR = Sammlung(
        trace="Isl Br",
        groups="Wortschatz|Anonym|Isl Br",
        kreis="Isl",
        ort="Br",
    )
    ANON_ISL_BÜ = Sammlung(
        trace="Isl Bü",
        groups="Wortschatz|Anonym|Isl Bü",
        kreis="Isl",
        ort="Bü",
    )
    ANON_ISL_BX = Sammlung(
        trace="Isl Bx",
        groups="Wortschatz|Anonym|Isl Bx",
        kreis="Isl",
        ort="Bx",
    )
    ANON_ISL_DA = Sammlung(
        trace="Isl Da",
        groups="Wortschatz|Anonym|Isl Da",
        kreis="Isl",
        ort="Da",
    )
    ANON_ISL_DG = Sammlung(
        trace="Isl Dg",
        groups="Wortschatz|Anonym|Isl Dg",
        kreis="Isl",
        ort="Dg",
    )
    ANON_ISL_DH = Sammlung(
        trace="Isl Dh",
        groups="Wortschatz|Anonym|Isl Dh",
        kreis="Isl",
        ort="Dh",
    )
    ANON_ISL_DÖ = Sammlung(
        trace="Isl Dö",
        groups="Wortschatz|Anonym|Isl Dö",
        kreis="Isl",
        ort="Dö",
    )
    ANON_ISL_DP = Sammlung(
        trace="Isl Dp",
        groups="Wortschatz|Anonym|Isl Dp",
        kreis="Isl",
        ort="Dp",
    )
    ANON_ISL_DS = Sammlung(
        trace="Isl Ds",
        groups="Wortschatz|Anonym|Isl Ds",
        kreis="Isl",
        ort="Ds",
    )
    ANON_ISL_DÜ = Sammlung(
        trace="Isl Dü",
        groups="Wortschatz|Anonym|Isl Dü",
        kreis="Isl",
        ort="Dü",
    )
    ANON_ISL_EF = Sammlung(
        trace="Isl Ef",
        groups="Wortschatz|Anonym|Isl Ef",
        kreis="Isl",
        ort="Ef",
    )
    ANON_ISL_EL = Sammlung(
        trace="Isl El",
        groups="Wortschatz|Anonym|Isl El",
        kreis="Isl",
        ort="El",
    )
    ANON_ISL_ER = Sammlung(
        trace="Isl Er",
        groups="Wortschatz|Anonym|Isl Er",
        kreis="Isl",
        ort="Er",
    )
    ANON_ISL_EV = Sammlung(
        trace="Isl Ev",
        groups="Wortschatz|Anonym|Isl Ev",
        kreis="Isl",
        ort="Ev",
    )
    ANON_ISL_FB = Sammlung(
        trace="Isl Fb",
        groups="Wortschatz|Anonym|Isl Fb",
        kreis="Isl",
        ort="Fb",
    )
    ANON_ISL_GB = Sammlung(
        trace="Isl Gb",
        groups="Wortschatz|Anonym|Isl Gb",
        kreis="Isl",
        ort="Gb",
    )
    ANON_ISL_GE = Sammlung(
        trace="Isl Ge",
        groups="Wortschatz|Anonym|Isl Ge",
        kreis="Isl",
        ort="Ge",
    )
    ANON_ISL_GF = Sammlung(
        trace="Isl Gf",
        groups="Wortschatz|Anonym|Isl Gf",
        kreis="Isl",
        ort="Gf",
    )
    ANON_ISL_GH = Sammlung(
        trace="Isl Gh",
        groups="Wortschatz|Anonym|Isl Gh",
        kreis="Isl",
        ort="Gh",
    )
    ANON_ISL_GL = Sammlung(
        trace="Isl Gl",
        groups="Wortschatz|Anonym|Isl Gl",
        kreis="Isl",
        ort="Gl",
    )
    ANON_ISL_GM = Sammlung(
        trace="Isl Gm",
        groups="Wortschatz|Anonym|Isl Gm",
        kreis="Isl",
        ort="Gm",
    )
    ANON_ISL_GR = Sammlung(
        trace="Isl Gr",
        groups="Wortschatz|Anonym|Isl Gr",
        kreis="Isl",
        ort="Gr",
    )
    ANON_ISL_GS = Sammlung(
        trace="Isl Gs",
        groups="Wortschatz|Anonym|Isl Gs",
        kreis="Isl",
        ort="Gs",
    )
    ANON_ISL_GX = Sammlung(
        trace="Isl Gx",
        groups="Wortschatz|Anonym|Isl Gx",
        kreis="Isl",
        ort="Gx",
    )
    ANON_ISL_HA = Sammlung(
        trace="Isl Ha",
        groups="Wortschatz|Anonym|Isl Ha",
        kreis="Isl",
        ort="Ha",
    )
    ANON_ISL_HD = Sammlung(
        trace="Isl Hd",
        groups="Wortschatz|Anonym|Isl Hd",
        kreis="Isl",
        ort="Hd",
    )
    ANON_ISL_HE = Sammlung(
        trace="Isl He",
        groups="Wortschatz|Anonym|Isl He",
        kreis="Isl",
        ort="He",
    )
    ANON_ISL_HG = Sammlung(
        trace="Isl Hg",
        groups="Wortschatz|Anonym|Isl Hg",
        kreis="Isl",
        ort="Hg",
    )
    ANON_ISL_HN = Sammlung(
        trace="Isl Hn",
        groups="Wortschatz|Anonym|Isl Hn",
        kreis="Isl",
        ort="Hn",
    )
    ANON_ISL_HO = Sammlung(
        trace="Isl Ho",
        groups="Wortschatz|Anonym|Isl Ho",
        kreis="Isl",
        ort="Ho",
    )
    ANON_ISL_HP = Sammlung(
        trace="Isl Hp",
        groups="Wortschatz|Anonym|Isl Hp",
        kreis="Isl",
        ort="Hp",
    )
    ANON_ISL_HÜ = Sammlung(
        trace="Isl Hü",
        groups="Wortschatz|Anonym|Isl Hü",
        kreis="Isl",
        ort="Hü",
    )
    ANON_ISL_HV = Sammlung(
        trace="Isl Hv",
        groups="Wortschatz|Anonym|Isl Hv",
        kreis="Isl",
        ort="Hv",
    )
    ANON_ISL_IM = Sammlung(
        trace="Isl Im",
        groups="Wortschatz|Anonym|Isl Im",
        kreis="Isl",
        ort="Im",
    )
    ANON_ISL_IS = Sammlung(
        trace="Isl Is",
        groups="Wortschatz|Anonym|Isl Is",
        kreis="Isl",
        ort="Is",
    )
    ANON_ISL_KA = Sammlung(
        trace="Isl Ka",
        groups="Wortschatz|Anonym|Isl Ka",
        kreis="Isl",
        ort="Ka",
    )
    ANON_ISL_KB = Sammlung(
        trace="Isl Kb",
        groups="Wortschatz|Anonym|Isl Kb",
        kreis="Isl",
        ort="Kb",
    )
    ANON_ISL_KG = Sammlung(
        trace="Isl Kg",
        groups="Wortschatz|Anonym|Isl Kg",
        kreis="Isl",
        ort="Kg",
    )
    ANON_ISL_KH = Sammlung(
        trace="Isl Kh",
        groups="Wortschatz|Anonym|Isl Kh",
        kreis="Isl",
        ort="Kh",
    )
    ANON_ISL_KO = Sammlung(
        trace="Isl Ko",
        groups="Wortschatz|Anonym|Isl Ko",
        kreis="Isl",
        ort="Ko",
    )
    ANON_ISL_KR = Sammlung(
        trace="Isl Kr",
        groups="Wortschatz|Anonym|Isl Kr",
        kreis="Isl",
        ort="Kr",
    )
    ANON_ISL_LÄ = Sammlung(
        trace="Isl Lä",
        groups="Wortschatz|Anonym|Isl Lä",
        kreis="Isl",
        ort="Lä",
    )
    ANON_ISL_LB = Sammlung(
        trace="Isl Lb",
        groups="Wortschatz|Anonym|Isl Lb",
        kreis="Isl",
        ort="Lb",
    )
    ANON_ISL_LD = Sammlung(
        trace="Isl Ld",
        groups="Wortschatz|Anonym|Isl Ld",
        kreis="Isl",
        ort="Ld",
    )
    ANON_ISL_LE = Sammlung(
        trace="Isl Le",
        groups="Wortschatz|Anonym|Isl Le",
        kreis="Isl",
        ort="Le",
    )
    ANON_ISL_LH = Sammlung(
        trace="Isl Lh",
        groups="Wortschatz|Anonym|Isl Lh",
        kreis="Isl",
        ort="Lh",
    )
    ANON_ISL_LK = Sammlung(
        trace="Isl Lk",
        groups="Wortschatz|Anonym|Isl Lk",
        kreis="Isl",
        ort="Lk",
    )
    ANON_ISL_LÖ = Sammlung(
        trace="Isl Lö",
        groups="Wortschatz|Anonym|Isl Lö",
        kreis="Isl",
        ort="Lö",
    )
    ANON_ISL_LU = Sammlung(
        trace="Isl Lu",
        groups="Wortschatz|Anonym|Isl Lu",
        kreis="Isl",
        ort="Lu",
    )
    ANON_ISL_LÜ = Sammlung(
        trace="Isl Lü",
        groups="Wortschatz|Anonym|Isl Lü",
        kreis="Isl",
        ort="Lü",
    )
    ANON_ISL_ME = Sammlung(
        trace="Isl Me",
        groups="Wortschatz|Anonym|Isl Me",
        kreis="Isl",
        ort="Me",
    )
    ANON_ISL_NI = Sammlung(
        trace="Isl Ni",
        groups="Wortschatz|Anonym|Isl Ni",
        kreis="Isl",
        ort="Ni",
    )
    ANON_ISL_OG = Sammlung(
        trace="Isl Og",
        groups="Wortschatz|Anonym|Isl Og",
        kreis="Isl",
        ort="Og",
    )
    ANON_ISL_OÖ = Sammlung(
        trace="Isl Oö",
        groups="Wortschatz|Anonym|Isl Oö",
        kreis="Isl",
        ort="Oö",
    )
    ANON_ISL_ÖS = Sammlung(
        trace="Isl Ös",
        groups="Wortschatz|Anonym|Isl Ös",
        kreis="Isl",
        ort="Ös",
    )
    ANON_ISL_ÖZ = Sammlung(
        trace="Isl Öz",
        groups="Wortschatz|Anonym|Isl Öz",
        kreis="Isl",
        ort="Öz",
    )
    ANON_ISL_PI = Sammlung(
        trace="Isl Pi",
        groups="Wortschatz|Anonym|Isl Pi",
        kreis="Isl",
        ort="Pi",
    )
    ANON_ISL_RE = Sammlung(
        trace="Isl Re",
        groups="Wortschatz|Anonym|Isl Re",
        kreis="Isl",
        ort="Re",
    )
    ANON_ISL_RG = Sammlung(
        trace="Isl Rg",
        groups="Wortschatz|Anonym|Isl Rg",
        kreis="Isl",
        ort="Rg",
    )
    ANON_ISL_RH = Sammlung(
        trace="Isl Rh",
        groups="Wortschatz|Anonym|Isl Rh",
        kreis="Isl",
        ort="Rh",
    )
    ANON_ISL_RO = Sammlung(
        trace="Isl Ro",
        groups="Wortschatz|Anonym|Isl Ro",
        kreis="Isl",
        ort="Ro",
    )
    ANON_ISL_RS = Sammlung(
        trace="Isl Rs",
        groups="Wortschatz|Anonym|Isl Rs",
        kreis="Isl",
        ort="Rs",
    )
    ANON_ISL_RÜ = Sammlung(
        trace="Isl Rü",
        groups="Wortschatz|Anonym|Isl Rü",
        kreis="Isl",
        ort="Rü",
    )
    ANON_ISL_SA = Sammlung(
        trace="Isl Sa",
        groups="Wortschatz|Anonym|Isl Sa",
        kreis="Isl",
        ort="Sa",
    )
    ANON_ISL_SB = Sammlung(
        trace="Isl Sb",
        groups="Wortschatz|Anonym|Isl Sb",
        kreis="Isl",
        ort="Sb",
    )
    ANON_ISL_SC = Sammlung(
        trace="Isl Sc",
        groups="Wortschatz|Anonym|Isl Sc",
        kreis="Isl",
        ort="Sc",
    )
    ANON_ISL_SI = Sammlung(
        trace="Isl Si",
        groups="Wortschatz|Anonym|Isl Si",
        kreis="Isl",
        ort="Si",
    )
    ANON_ISL_SK = Sammlung(
        trace="Isl Sk",
        groups="Wortschatz|Anonym|Isl Sk",
        kreis="Isl",
        ort="Sk",
    )
    ANON_ISL_SU = Sammlung(
        trace="Isl Su",
        groups="Wortschatz|Anonym|Isl Su",
        kreis="Isl",
        ort="Su",
    )
    ANON_ISL_SÜ = Sammlung(
        trace="Isl Sü",
        groups="Wortschatz|Anonym|Isl Sü",
        kreis="Isl",
        ort="Sü",
    )
    ANON_ISL_SW = Sammlung(
        trace="Isl Sw",
        groups="Wortschatz|Anonym|Isl Sw",
        kreis="Isl",
        ort="Sw",
    )
    ANON_ISL_UG = Sammlung(
        trace="Isl Ug",
        groups="Wortschatz|Anonym|Isl Ug",
        kreis="Isl",
        ort="Ug",
    )
    ANON_ISL_VH = Sammlung(
        trace="Isl Vh",
        groups="Wortschatz|Anonym|Isl Vh",
        kreis="Isl",
        ort="Vh",
    )
    ANON_ISL_VI = Sammlung(
        trace="Isl Vi",
        groups="Wortschatz|Anonym|Isl Vi",
        kreis="Isl",
        ort="Vi",
    )
    ANON_ISL_WD = Sammlung(
        trace="Isl Wd",
        groups="Wortschatz|Anonym|Isl Wd",
        kreis="Isl",
        ort="Wd",
    )
    ANON_ISL_WE = Sammlung(
        trace="Isl We",
        groups="Wortschatz|Anonym|Isl We",
        kreis="Isl",
        ort="We",
    )
    ANON_ISL_WH = Sammlung(
        trace="Isl Wh",
        groups="Wortschatz|Anonym|Isl Wh",
        kreis="Isl",
        ort="Wh",
    )
    ANON_ISL_WI = Sammlung(
        trace="Isl Wi",
        groups="Wortschatz|Anonym|Isl Wi",
        kreis="Isl",
        ort="Wi",
    )
    ANON_ISL_WR = Sammlung(
        trace="Isl Wr",
        groups="Wortschatz|Anonym|Isl Wr",
        kreis="Isl",
        ort="Wr",
    )
    ANON_ISL_WU = Sammlung(
        trace="Isl Wu",
        groups="Wortschatz|Anonym|Isl Wu",
        kreis="Isl",
        ort="Wu",
    )
    ANON_ISL_WX = Sammlung(
        trace="Isl Wx",
        groups="Wortschatz|Anonym|Isl Wx",
        kreis="Isl",
        ort="Wx",
    )
    ANON_KLO_AB = Sammlung(
        trace="Klo Ab",
        groups="Wortschatz|Anonym|Klo Ab",
        kreis="Klo",
        ort="Ab",
    )
    ANON_KLO_AD = Sammlung(
        trace="Klo Ad",
        groups="Wortschatz|Anonym|Klo Ad",
        kreis="Klo",
        ort="Ad",
    )
    ANON_KLO_AG = Sammlung(
        trace="Klo Ag",
        groups="Wortschatz|Anonym|Klo Ag",
        kreis="Klo",
        ort="Ag",
    )
    ANON_KLO_AL = Sammlung(
        trace="Klo Al",
        groups="Wortschatz|Anonym|Klo Al",
        kreis="Klo",
        ort="Al",
    )
    ANON_KLO_AM = Sammlung(
        trace="Klo Am",
        groups="Wortschatz|Anonym|Klo Am",
        kreis="Klo",
        ort="Am",
    )
    ANON_KLO_AP = Sammlung(
        trace="Klo Ap",
        groups="Wortschatz|Anonym|Klo Ap",
        kreis="Klo",
        ort="Ap",
    )
    ANON_KLO_AU = Sammlung(
        trace="Klo Au",
        groups="Wortschatz|Anonym|Klo Au",
        kreis="Klo",
        ort="Au",
    )
    ANON_KLO_BB = Sammlung(
        trace="Klo Bb",
        groups="Wortschatz|Anonym|Klo Bb",
        kreis="Klo",
        ort="Bb",
    )
    ANON_KLO_BE = Sammlung(
        trace="Klo Be",
        groups="Wortschatz|Anonym|Klo Be",
        kreis="Klo",
        ort="Be",
    )
    ANON_KLO_BH = Sammlung(
        trace="Klo Bh",
        groups="Wortschatz|Anonym|Klo Bh",
        kreis="Klo",
        ort="Bh",
    )
    ANON_KLO_BL = Sammlung(
        trace="Klo Bl",
        groups="Wortschatz|Anonym|Klo Bl",
        kreis="Klo",
        ort="Bl",
    )
    ANON_KLO_BO = Sammlung(
        trace="Klo Bo",
        groups="Wortschatz|Anonym|Klo Bo",
        kreis="Klo",
        ort="Bo",
    )
    ANON_KLO_BS = Sammlung(
        trace="Klo Bs",
        groups="Wortschatz|Anonym|Klo Bs",
        kreis="Klo",
        ort="Bs",
    )
    ANON_KLO_BU = Sammlung(
        trace="Klo Bu",
        groups="Wortschatz|Anonym|Klo Bu",
        kreis="Klo",
        ort="Bu",
    )
    ANON_KLO_BÜ = Sammlung(
        trace="Klo Bü",
        groups="Wortschatz|Anonym|Klo Bü",
        kreis="Klo",
        ort="Bü",
    )
    ANON_KLO_BV = Sammlung(
        trace="Klo Bv",
        groups="Wortschatz|Anonym|Klo Bv",
        kreis="Klo",
        ort="Bv",
    )
    ANON_KLO_DW = Sammlung(
        trace="Klo Dw",
        groups="Wortschatz|Anonym|Klo Dw",
        kreis="Klo",
        ort="Dw",
    )
    ANON_KLO_EB = Sammlung(
        trace="Klo Eb",
        groups="Wortschatz|Anonym|Klo Eb",
        kreis="Klo",
        ort="Eb",
    )
    ANON_KLO_EF = Sammlung(
        trace="Klo Ef",
        groups="Wortschatz|Anonym|Klo Ef",
        kreis="Klo",
        ort="Ef",
    )
    ANON_KLO_EH = Sammlung(
        trace="Klo Eh",
        groups="Wortschatz|Anonym|Klo Eh",
        kreis="Klo",
        ort="Eh",
    )
    ANON_KLO_EL = Sammlung(
        trace="Klo El",
        groups="Wortschatz|Anonym|Klo El",
        kreis="Klo",
        ort="El",
    )
    ANON_KLO_EM = Sammlung(
        trace="Klo Em",
        groups="Wortschatz|Anonym|Klo Em",
        kreis="Klo",
        ort="Em",
    )
    ANON_KLO_ER = Sammlung(
        trace="Klo Er",
        groups="Wortschatz|Anonym|Klo Er",
        kreis="Klo",
        ort="Er",
    )
    ANON_KLO_ES = Sammlung(
        trace="Klo Es",
        groups="Wortschatz|Anonym|Klo Es",
        kreis="Klo",
        ort="Es",
    )
    ANON_KLO_EV = Sammlung(
        trace="Klo Ev",
        groups="Wortschatz|Anonym|Klo Ev",
        kreis="Klo",
        ort="Ev",
    )
    ANON_KLO_FB = Sammlung(
        trace="Klo Fb",
        groups="Wortschatz|Anonym|Klo Fb",
        kreis="Klo",
        ort="Fb",
    )
    ANON_KLO_FR = Sammlung(
        trace="Klo Fr",
        groups="Wortschatz|Anonym|Klo Fr",
        kreis="Klo",
        ort="Fr",
    )
    ANON_KLO_GA = Sammlung(
        trace="Klo Ga",
        groups="Wortschatz|Anonym|Klo Ga",
        kreis="Klo",
        ort="Ga",
    )
    ANON_KLO_GG = Sammlung(
        trace="Klo Gg",
        groups="Wortschatz|Anonym|Klo Gg",
        kreis="Klo",
        ort="Gg",
    )
    ANON_KLO_GL = Sammlung(
        trace="Klo Gl",
        groups="Wortschatz|Anonym|Klo Gl",
        kreis="Klo",
        ort="Gl",
    )
    ANON_KLO_GT = Sammlung(
        trace="Klo Gt",
        groups="Wortschatz|Anonym|Klo Gt",
        kreis="Klo",
        ort="Gt",
    )
    ANON_KLO_HA = Sammlung(
        trace="Klo Ha",
        groups="Wortschatz|Anonym|Klo Ha",
        kreis="Klo",
        ort="Ha",
    )
    ANON_KLO_HB = Sammlung(
        trace="Klo Hb",
        groups="Wortschatz|Anonym|Klo Hb",
        kreis="Klo",
        ort="Hb",
    )
    ANON_KLO_HE = Sammlung(
        trace="Klo He",
        groups="Wortschatz|Anonym|Klo He",
        kreis="Klo",
        ort="He",
    )
    ANON_KLO_HG = Sammlung(
        trace="Klo Hg",
        groups="Wortschatz|Anonym|Klo Hg",
        kreis="Klo",
        ort="Hg",
    )
    ANON_KLO_HH = Sammlung(
        trace="Klo Hh",
        groups="Wortschatz|Anonym|Klo Hh",
        kreis="Klo",
        ort="Hh",
    )
    ANON_KLO_HL = Sammlung(
        trace="Klo Hl",
        groups="Wortschatz|Anonym|Klo Hl",
        kreis="Klo",
        ort="Hl",
    )
    ANON_KLO_HM = Sammlung(
        trace="Klo Hm",
        groups="Wortschatz|Anonym|Klo Hm",
        kreis="Klo",
        ort="Hm",
    )
    ANON_KLO_HO = Sammlung(
        trace="Klo Ho",
        groups="Wortschatz|Anonym|Klo Ho",
        kreis="Klo",
        ort="Ho",
    )
    ANON_KLO_HR = Sammlung(
        trace="Klo Hr",
        groups="Wortschatz|Anonym|Klo Hr",
        kreis="Klo",
        ort="Hr",
    )
    ANON_KLO_KA = Sammlung(
        trace="Klo Ka",
        groups="Wortschatz|Anonym|Klo Ka",
        kreis="Klo",
        ort="Ka",
    )
    ANON_KLO_KF = Sammlung(
        trace="Klo Kf",
        groups="Wortschatz|Anonym|Klo Kf",
        kreis="Klo",
        ort="Kf",
    )
    ANON_KLO_KH = Sammlung(
        trace="Klo Kh",
        groups="Wortschatz|Anonym|Klo Kh",
        kreis="Klo",
        ort="Kh",
    )
    ANON_KLO_KL = Sammlung(
        trace="Klo Kl",
        groups="Wortschatz|Anonym|Klo Kl",
        kreis="Klo",
        ort="Kl",
    )
    ANON_KLO_LA = Sammlung(
        trace="Klo La",
        groups="Wortschatz|Anonym|Klo La",
        kreis="Klo",
        ort="La",
    )
    ANON_KLO_LI = Sammlung(
        trace="Klo Li",
        groups="Wortschatz|Anonym|Klo Li",
        kreis="Klo",
        ort="Li",
    )
    ANON_KLO_LO = Sammlung(
        trace="Klo Lo",
        groups="Wortschatz|Anonym|Klo Lo",
        kreis="Klo",
        ort="Lo",
    )
    ANON_KLO_LÖ = Sammlung(
        trace="Klo Lö",
        groups="Wortschatz|Anonym|Klo Lö",
        kreis="Klo",
        ort="Lö",
    )
    ANON_KLO_MA = Sammlung(
        trace="Klo Ma",
        groups="Wortschatz|Anonym|Klo Ma",
        kreis="Klo",
        ort="Ma",
    )
    ANON_KLO_MO = Sammlung(
        trace="Klo Mo",
        groups="Wortschatz|Anonym|Klo Mo",
        kreis="Klo",
        ort="Mo",
    )
    ANON_KLO_ND = Sammlung(
        trace="Klo Nd",
        groups="Wortschatz|Anonym|Klo Nd",
        kreis="Klo",
        ort="Nd",
    )
    ANON_KLO_NM = Sammlung(
        trace="Klo Nm",
        groups="Wortschatz|Anonym|Klo Nm",
        kreis="Klo",
        ort="Nm",
    )
    ANON_KLO_NT = Sammlung(
        trace="Klo Nt",
        groups="Wortschatz|Anonym|Klo Nt",
        kreis="Klo",
        ort="Nt",
    )
    ANON_KLO_NU = Sammlung(
        trace="Klo Nu",
        groups="Wortschatz|Anonym|Klo Nu",
        kreis="Klo",
        ort="Nu",
    )
    ANON_KLO_PD = Sammlung(
        trace="Klo Pd",
        groups="Wortschatz|Anonym|Klo Pd",
        kreis="Klo",
        ort="Pd",
    )
    ANON_KLO_PH = Sammlung(
        trace="Klo Ph",
        groups="Wortschatz|Anonym|Klo Ph",
        kreis="Klo",
        ort="Ph",
    )
    ANON_KLO_RH = Sammlung(
        trace="Klo Rh",
        groups="Wortschatz|Anonym|Klo Rh",
        kreis="Klo",
        ort="Rh",
    )
    ANON_KLO_SE = Sammlung(
        trace="Klo Se",
        groups="Wortschatz|Anonym|Klo Se",
        kreis="Klo",
        ort="Se",
    )
    ANON_KLO_SH = Sammlung(
        trace="Klo Sh",
        groups="Wortschatz|Anonym|Klo Sh",
        kreis="Klo",
        ort="Sh",
    )
    ANON_KLO_ST = Sammlung(
        trace="Klo St",
        groups="Wortschatz|Anonym|Klo St",
        kreis="Klo",
        ort="St",
    )
    ANON_KLO_SW = Sammlung(
        trace="Klo Sw",
        groups="Wortschatz|Anonym|Klo Sw",
        kreis="Klo",
        ort="Sw",
    )
    ANON_KLO_TE = Sammlung(
        trace="Klo Te",
        groups="Wortschatz|Anonym|Klo Te",
        kreis="Klo",
        ort="Te",
    )
    ANON_KLO_TÜ = Sammlung(
        trace="Klo Tü",
        groups="Wortschatz|Anonym|Klo Tü",
        kreis="Klo",
        ort="Tü",
    )
    ANON_KLO_TW = Sammlung(
        trace="Klo Tw",
        groups="Wortschatz|Anonym|Klo Tw",
        kreis="Klo",
        ort="Tw",
    )
    ANON_KLO_VA = Sammlung(
        trace="Klo Va",
        groups="Wortschatz|Anonym|Klo Va",
        kreis="Klo",
        ort="Va",
    )
    ANON_KLO_VB = Sammlung(
        trace="Klo Vb",
        groups="Wortschatz|Anonym|Klo Vb",
        kreis="Klo",
        ort="Vb",
    )
    ANON_KLO_VT = Sammlung(
        trace="Klo Vt",
        groups="Wortschatz|Anonym|Klo Vt",
        kreis="Klo",
        ort="Vt",
    )
    ANON_KLO_WI = Sammlung(
        trace="Klo Wi",
        groups="Wortschatz|Anonym|Klo Wi",
        kreis="Klo",
        ort="Wi",
    )
    ANON_KLO_WS = Sammlung(
        trace="Klo Ws",
        groups="Wortschatz|Anonym|Klo Ws",
        kreis="Klo",
        ort="Ws",
    )
    ANON_KOS_AU = Sammlung(
        trace="Kos Au",
        groups="Wortschatz|Anonym|Kos Au",
        kreis="Kos",
        ort="Au",
    )
    ANON_KOS_BA = Sammlung(
        trace="Kos Ba",
        groups="Wortschatz|Anonym|Kos Ba",
        kreis="Kos",
        ort="Ba",
    )
    ANON_KOS_BB = Sammlung(
        trace="Kos Bb",
        groups="Wortschatz|Anonym|Kos Bb",
        kreis="Kos",
        ort="Bb",
    )
    ANON_KOS_BE = Sammlung(
        trace="Kos Be",
        groups="Wortschatz|Anonym|Kos Be",
        kreis="Kos",
        ort="Be",
    )
    ANON_KOS_BÖ = Sammlung(
        trace="Kos Bö",
        groups="Wortschatz|Anonym|Kos Bö",
        kreis="Kos",
        ort="Bö",
    )
    ANON_KOS_BU = Sammlung(
        trace="Kos Bu",
        groups="Wortschatz|Anonym|Kos Bu",
        kreis="Kos",
        ort="Bu",
    )
    ANON_KOS_BÜ = Sammlung(
        trace="Kos Bü",
        groups="Wortschatz|Anonym|Kos Bü",
        kreis="Kos",
        ort="Bü",
    )
    ANON_KOS_DA = Sammlung(
        trace="Kos Da",
        groups="Wortschatz|Anonym|Kos Da",
        kreis="Kos",
        ort="Da",
    )
    ANON_KOS_DD = Sammlung(
        trace="Kos Dd",
        groups="Wortschatz|Anonym|Kos Dd",
        kreis="Kos",
        ort="Dd",
    )
    ANON_KOS_DF = Sammlung(
        trace="Kos Df",
        groups="Wortschatz|Anonym|Kos Df",
        kreis="Kos",
        ort="Df",
    )
    ANON_KOS_DK = Sammlung(
        trace="Kos Dk",
        groups="Wortschatz|Anonym|Kos Dk",
        kreis="Kos",
        ort="Dk",
    )
    ANON_KOS_DÜ = Sammlung(
        trace="Kos Dü",
        groups="Wortschatz|Anonym|Kos Dü",
        kreis="Kos",
        ort="Dü",
    )
    ANON_KOS_ES = Sammlung(
        trace="Kos Es",
        groups="Wortschatz|Anonym|Kos Es",
        kreis="Kos",
        ort="Es",
    )
    ANON_KOS_FL = Sammlung(
        trace="Kos Fl",
        groups="Wortschatz|Anonym|Kos Fl",
        kreis="Kos",
        ort="Fl",
    )
    ANON_KOS_GA = Sammlung(
        trace="Kos Ga",
        groups="Wortschatz|Anonym|Kos Ga",
        kreis="Kos",
        ort="Ga",
    )
    ANON_KOS_GB = Sammlung(
        trace="Kos Gb",
        groups="Wortschatz|Anonym|Kos Gb",
        kreis="Kos",
        ort="Gb",
    )
    ANON_KOS_GE = Sammlung(
        trace="Kos Ge",
        groups="Wortschatz|Anonym|Kos Ge",
        kreis="Kos",
        ort="Ge",
    )
    ANON_KOS_GO = Sammlung(
        trace="Kos Go",
        groups="Wortschatz|Anonym|Kos Go",
        kreis="Kos",
        ort="Go",
    )
    ANON_KOS_GP = Sammlung(
        trace="Kos Gp",
        groups="Wortschatz|Anonym|Kos Gp",
        kreis="Kos",
        ort="Gp",
    )
    ANON_KOS_HA = Sammlung(
        trace="Kos Ha",
        groups="Wortschatz|Anonym|Kos Ha",
        kreis="Kos",
        ort="Ha",
    )
    ANON_KOS_HD = Sammlung(
        trace="Kos Hd",
        groups="Wortschatz|Anonym|Kos Hd",
        kreis="Kos",
        ort="Hd",
    )
    ANON_KOS_HE = Sammlung(
        trace="Kos He",
        groups="Wortschatz|Anonym|Kos He",
        kreis="Kos",
        ort="He",
    )
    ANON_KOS_HI = Sammlung(
        trace="Kos Hi",
        groups="Wortschatz|Anonym|Kos Hi",
        kreis="Kos",
        ort="Hi",
    )
    ANON_KOS_HO = Sammlung(
        trace="Kos Ho",
        groups="Wortschatz|Anonym|Kos Ho",
        kreis="Kos",
        ort="Ho",
    )
    ANON_KOS_HÖ = Sammlung(
        trace="Kos Hö",
        groups="Wortschatz|Anonym|Kos Hö",
        kreis="Kos",
        ort="Hö",
    )
    ANON_KOS_HW = Sammlung(
        trace="Kos Hw",
        groups="Wortschatz|Anonym|Kos Hw",
        kreis="Kos",
        ort="Hw",
    )
    ANON_KOS_KA = Sammlung(
        trace="Kos Ka",
        groups="Wortschatz|Anonym|Kos Ka",
        kreis="Kos",
        ort="Ka",
    )
    ANON_KOS_KF = Sammlung(
        trace="Kos Kf",
        groups="Wortschatz|Anonym|Kos Kf",
        kreis="Kos",
        ort="Kf",
    )
    ANON_KOS_KH = Sammlung(
        trace="Kos Kh",
        groups="Wortschatz|Anonym|Kos Kh",
        kreis="Kos",
        ort="Kh",
    )
    ANON_KOS_KL = Sammlung(
        trace="Kos Kl",
        groups="Wortschatz|Anonym|Kos Kl",
        kreis="Kos",
        ort="Kl",
    )
    ANON_KOS_LE = Sammlung(
        trace="Kos Le",
        groups="Wortschatz|Anonym|Kos Le",
        kreis="Kos",
        ort="Le",
    )
    ANON_KOS_LS = Sammlung(
        trace="Kos Ls",
        groups="Wortschatz|Anonym|Kos Ls",
        kreis="Kos",
        ort="Ls",
    )
    ANON_KOS_MF = Sammlung(
        trace="Kos Mf",
        groups="Wortschatz|Anonym|Kos Mf",
        kreis="Kos",
        ort="Mf",
    )
    ANON_KOS_MW = Sammlung(
        trace="Kos Mw",
        groups="Wortschatz|Anonym|Kos Mw",
        kreis="Kos",
        ort="Mw",
    )
    ANON_KOS_OH = Sammlung(
        trace="Kos Oh",
        groups="Wortschatz|Anonym|Kos Oh",
        kreis="Kos",
        ort="Oh",
    )
    ANON_KOS_OW = Sammlung(
        trace="Kos Ow",
        groups="Wortschatz|Anonym|Kos Ow",
        kreis="Kos",
        ort="Ow",
    )
    ANON_KOS_RR = Sammlung(
        trace="Kos Rr",
        groups="Wortschatz|Anonym|Kos Rr",
        kreis="Kos",
        ort="Rr",
    )
    ANON_KOS_SF = Sammlung(
        trace="Kos Sf",
        groups="Wortschatz|Anonym|Kos Sf",
        kreis="Kos",
        ort="Sf",
    )
    ANON_KOS_SK = Sammlung(
        trace="Kos Sk",
        groups="Wortschatz|Anonym|Kos Sk",
        kreis="Kos",
        ort="Sk",
    )
    ANON_KOS_ST = Sammlung(
        trace="Kos St",
        groups="Wortschatz|Anonym|Kos St",
        kreis="Kos",
        ort="St",
    )
    ANON_KOS_TU = Sammlung(
        trace="Kos Tu",
        groups="Wortschatz|Anonym|Kos Tu",
        kreis="Kos",
        ort="Tu",
    )
    ANON_KOS_VI = Sammlung(
        trace="Kos Vi",
        groups="Wortschatz|Anonym|Kos Vi",
        kreis="Kos",
        ort="Vi",
    )
    ANON_KOS_WE = Sammlung(
        trace="Kos We",
        groups="Wortschatz|Anonym|Kos We",
        kreis="Kos",
        ort="We",
    )
    ANON_LEM_AD = Sammlung(
        trace="Lem Ad",
        groups="Wortschatz|Anonym|Lem Ad",
        kreis="Lem",
        ort="Ad",
    )
    ANON_LEM_AL = Sammlung(
        trace="Lem Al",
        groups="Wortschatz|Anonym|Lem Al",
        kreis="Lem",
        ort="Al",
    )
    ANON_LEM_AM = Sammlung(
        trace="Lem Am",
        groups="Wortschatz|Anonym|Lem Am",
        kreis="Lem",
        ort="Am",
    )
    ANON_LEM_AS = Sammlung(
        trace="Lem As",
        groups="Wortschatz|Anonym|Lem As",
        kreis="Lem",
        ort="As",
    )
    ANON_LEM_BA = Sammlung(
        trace="Lem Ba",
        groups="Wortschatz|Anonym|Lem Ba",
        kreis="Lem",
        ort="Ba",
    )
    ANON_LEM_BE = Sammlung(
        trace="Lem Be",
        groups="Wortschatz|Anonym|Lem Be",
        kreis="Lem",
        ort="Be",
    )
    ANON_LEM_BF = Sammlung(
        trace="Lem Bf",
        groups="Wortschatz|Anonym|Lem Bf",
        kreis="Lem",
        ort="Bf",
    )
    ANON_LEM_BG = Sammlung(
        trace="Lem Bg",
        groups="Wortschatz|Anonym|Lem Bg",
        kreis="Lem",
        ort="Bg",
    )
    ANON_LEM_BK = Sammlung(
        trace="Lem Bk",
        groups="Wortschatz|Anonym|Lem Bk",
        kreis="Lem",
        ort="Bk",
    )
    ANON_LEM_BP = Sammlung(
        trace="Lem Bp",
        groups="Wortschatz|Anonym|Lem Bp",
        kreis="Lem",
        ort="Bp",
    )
    ANON_LEM_BR = Sammlung(
        trace="Lem Br",
        groups="Wortschatz|Anonym|Lem Br",
        kreis="Lem",
        ort="Br",
    )
    ANON_LEM_BT = Sammlung(
        trace="Lem Bt",
        groups="Wortschatz|Anonym|Lem Bt",
        kreis="Lem",
        ort="Bt",
    )
    ANON_LEM_BX = Sammlung(
        trace="Lem Bx",
        groups="Wortschatz|Anonym|Lem Bx",
        kreis="Lem",
        ort="Bx",
    )
    ANON_LEM_DÖ = Sammlung(
        trace="Lem Dö",
        groups="Wortschatz|Anonym|Lem Dö",
        kreis="Lem",
        ort="Dö",
    )
    ANON_LEM_ER = Sammlung(
        trace="Lem Er",
        groups="Wortschatz|Anonym|Lem Er",
        kreis="Lem",
        ort="Er",
    )
    ANON_LEM_GÖ = Sammlung(
        trace="Lem Gö",
        groups="Wortschatz|Anonym|Lem Gö",
        kreis="Lem",
        ort="Gö",
    )
    ANON_LEM_GR = Sammlung(
        trace="Lem Gr",
        groups="Wortschatz|Anonym|Lem Gr",
        kreis="Lem",
        ort="Gr",
    )
    ANON_LEM_HB = Sammlung(
        trace="Lem Hb",
        groups="Wortschatz|Anonym|Lem Hb",
        kreis="Lem",
        ort="Hb",
    )
    ANON_LEM_HD = Sammlung(
        trace="Lem Hd",
        groups="Wortschatz|Anonym|Lem Hd",
        kreis="Lem",
        ort="Hd",
    )
    ANON_LEM_HE = Sammlung(
        trace="Lem He",
        groups="Wortschatz|Anonym|Lem He",
        kreis="Lem",
        ort="He",
    )
    ANON_LEM_HF = Sammlung(
        trace="Lem Hf",
        groups="Wortschatz|Anonym|Lem Hf",
        kreis="Lem",
        ort="Hf",
    )
    ANON_LEM_HG = Sammlung(
        trace="Lem Hg",
        groups="Wortschatz|Anonym|Lem Hg",
        kreis="Lem",
        ort="Hg",
    )
    ANON_LEM_HH = Sammlung(
        trace="Lem Hh",
        groups="Wortschatz|Anonym|Lem Hh",
        kreis="Lem",
        ort="Hh",
    )
    ANON_LEM_HO = Sammlung(
        trace="Lem Ho",
        groups="Wortschatz|Anonym|Lem Ho",
        kreis="Lem",
        ort="Ho",
    )
    ANON_LEM_HÖ = Sammlung(
        trace="Lem Hö",
        groups="Wortschatz|Anonym|Lem Hö",
        kreis="Lem",
        ort="Hö",
    )
    ANON_LEM_HT = Sammlung(
        trace="Lem Ht",
        groups="Wortschatz|Anonym|Lem Ht",
        kreis="Lem",
        ort="Ht",
    )
    ANON_LEM_KA = Sammlung(
        trace="Lem Ka",
        groups="Wortschatz|Anonym|Lem Ka",
        kreis="Lem",
        ort="Ka",
    )
    ANON_LEM_KI = Sammlung(
        trace="Lem Ki",
        groups="Wortschatz|Anonym|Lem Ki",
        kreis="Lem",
        ort="Ki",
    )
    ANON_LEM_KN = Sammlung(
        trace="Lem Kn",
        groups="Wortschatz|Anonym|Lem Kn",
        kreis="Lem",
        ort="Kn",
    )
    ANON_LEM_LA = Sammlung(
        trace="Lem La",
        groups="Wortschatz|Anonym|Lem La",
        kreis="Lem",
        ort="La",
    )
    ANON_LEM_LB = Sammlung(
        trace="Lem Lb",
        groups="Wortschatz|Anonym|Lem Lb",
        kreis="Lem",
        ort="Lb",
    )
    ANON_LEM_LC = Sammlung(
        trace="Lem Lc",
        groups="Wortschatz|Anonym|Lem Lc",
        kreis="Lem",
        ort="Lc",
    )
    ANON_LEM_LD = Sammlung(
        trace="Lem Ld",
        groups="Wortschatz|Anonym|Lem Ld",
        kreis="Lem",
        ort="Ld",
    )
    ANON_LEM_LE = Sammlung(
        trace="Lem Le",
        groups="Wortschatz|Anonym|Lem Le",
        kreis="Lem",
        ort="Le",
    )
    ANON_LEM_LF = Sammlung(
        trace="Lem Lf",
        groups="Wortschatz|Anonym|Lem Lf",
        kreis="Lem",
        ort="Lf",
    )
    ANON_LEM_LG = Sammlung(
        trace="Lem Lg",
        groups="Wortschatz|Anonym|Lem Lg",
        kreis="Lem",
        ort="Lg",
    )
    ANON_LEM_LH = Sammlung(
        trace="Lem Lh",
        groups="Wortschatz|Anonym|Lem Lh",
        kreis="Lem",
        ort="Lh",
    )
    ANON_LEM_LI = Sammlung(
        trace="Lem Li",
        groups="Wortschatz|Anonym|Lem Li",
        kreis="Lem",
        ort="Li",
    )
    ANON_LEM_LO = Sammlung(
        trace="Lem Lo",
        groups="Wortschatz|Anonym|Lem Lo",
        kreis="Lem",
        ort="Lo",
    )
    ANON_LEM_LP = Sammlung(
        trace="Lem Lp",
        groups="Wortschatz|Anonym|Lem Lp",
        kreis="Lem",
        ort="Lp",
    )
    ANON_LEM_LR = Sammlung(
        trace="Lem Lr",
        groups="Wortschatz|Anonym|Lem Lr",
        kreis="Lem",
        ort="Lr",
    )
    ANON_LEM_LÜ = Sammlung(
        trace="Lem Lü",
        groups="Wortschatz|Anonym|Lem Lü",
        kreis="Lem",
        ort="Lü",
    )
    ANON_LEM_MA = Sammlung(
        trace="Lem Ma",
        groups="Wortschatz|Anonym|Lem Ma",
        kreis="Lem",
        ort="Ma",
    )
    ANON_LEM_MB = Sammlung(
        trace="Lem Mb",
        groups="Wortschatz|Anonym|Lem Mb",
        kreis="Lem",
        ort="Mb",
    )
    ANON_LEM_MT = Sammlung(
        trace="Lem Mt",
        groups="Wortschatz|Anonym|Lem Mt",
        kreis="Lem",
        ort="Mt",
    )
    ANON_LEM_ÖR = Sammlung(
        trace="Lem Ör",
        groups="Wortschatz|Anonym|Lem Ör",
        kreis="Lem",
        ort="Ör",
    )
    ANON_LEM_RE = Sammlung(
        trace="Lem Re",
        groups="Wortschatz|Anonym|Lem Re",
        kreis="Lem",
        ort="Re",
    )
    ANON_LEM_SB = Sammlung(
        trace="Lem Sb",
        groups="Wortschatz|Anonym|Lem Sb",
        kreis="Lem",
        ort="Sb",
    )
    ANON_LEM_SC = Sammlung(
        trace="Lem Sc",
        groups="Wortschatz|Anonym|Lem Sc",
        kreis="Lem",
        ort="Sc",
    )
    ANON_LEM_SE = Sammlung(
        trace="Lem Se",
        groups="Wortschatz|Anonym|Lem Se",
        kreis="Lem",
        ort="Se",
    )
    ANON_LEM_SH = Sammlung(
        trace="Lem Sh",
        groups="Wortschatz|Anonym|Lem Sh",
        kreis="Lem",
        ort="Sh",
    )
    ANON_LEM_SI = Sammlung(
        trace="Lem Si",
        groups="Wortschatz|Anonym|Lem Si",
        kreis="Lem",
        ort="Si",
    )
    ANON_LEM_SM = Sammlung(
        trace="Lem Sm",
        groups="Wortschatz|Anonym|Lem Sm",
        kreis="Lem",
        ort="Sm",
    )
    ANON_LEM_ST = Sammlung(
        trace="Lem St",
        groups="Wortschatz|Anonym|Lem St",
        kreis="Lem",
        ort="St",
    )
    ANON_LEM_SU = Sammlung(
        trace="Lem Su",
        groups="Wortschatz|Anonym|Lem Su",
        kreis="Lem",
        ort="Su",
    )
    ANON_LEM_SW = Sammlung(
        trace="Lem Sw",
        groups="Wortschatz|Anonym|Lem Sw",
        kreis="Lem",
        ort="Sw",
    )
    ANON_LEM_SX = Sammlung(
        trace="Lem Sx",
        groups="Wortschatz|Anonym|Lem Sx",
        kreis="Lem",
        ort="Sx",
    )
    ANON_LEM_TA = Sammlung(
        trace="Lem Ta",
        groups="Wortschatz|Anonym|Lem Ta",
        kreis="Lem",
        ort="Ta",
    )
    ANON_LEM_VA = Sammlung(
        trace="Lem Va",
        groups="Wortschatz|Anonym|Lem Va",
        kreis="Lem",
        ort="Va",
    )
    ANON_LEM_VH = Sammlung(
        trace="Lem Vh",
        groups="Wortschatz|Anonym|Lem Vh",
        kreis="Lem",
        ort="Vh",
    )
    ANON_LEM_VO = Sammlung(
        trace="Lem Vo",
        groups="Wortschatz|Anonym|Lem Vo",
        kreis="Lem",
        ort="Vo",
    )
    ANON_LEM_WA = Sammlung(
        trace="Lem Wa",
        groups="Wortschatz|Anonym|Lem Wa",
        kreis="Lem",
        ort="Wa",
    )
    ANON_LEM_WB = Sammlung(
        trace="Lem Wb",
        groups="Wortschatz|Anonym|Lem Wb",
        kreis="Lem",
        ort="Wb",
    )
    ANON_LEM_WD = Sammlung(
        trace="Lem Wd",
        groups="Wortschatz|Anonym|Lem Wd",
        kreis="Lem",
        ort="Wd",
    )
    ANON_LEM_WH = Sammlung(
        trace="Lem Wh",
        groups="Wortschatz|Anonym|Lem Wh",
        kreis="Lem",
        ort="Wh",
    )
    ANON_LEM_WR = Sammlung(
        trace="Lem Wr",
        groups="Wortschatz|Anonym|Lem Wr",
        kreis="Lem",
        ort="Wr",
    )
    ANON_LEM_WÜ = Sammlung(
        trace="Lem Wü",
        groups="Wortschatz|Anonym|Lem Wü",
        kreis="Lem",
        ort="Wü",
    )
    ANON_LHS_AB = Sammlung(
        trace="Lhs Ab",
        groups="Wortschatz|Anonym|Lhs Ab",
        kreis="Lhs",
        ort="Ab",
    )
    ANON_LHS_AH = Sammlung(
        trace="Lhs Ah",
        groups="Wortschatz|Anonym|Lhs Ah",
        kreis="Lhs",
        ort="Ah",
    )
    ANON_LHS_AL = Sammlung(
        trace="Lhs Al",
        groups="Wortschatz|Anonym|Lhs Al",
        kreis="Lhs",
        ort="Al",
    )
    ANON_LHS_BB = Sammlung(
        trace="Lhs Bb",
        groups="Wortschatz|Anonym|Lhs Bb",
        kreis="Lhs",
        ort="Bb",
    )
    ANON_LHS_BH = Sammlung(
        trace="Lhs Bh",
        groups="Wortschatz|Anonym|Lhs Bh",
        kreis="Lhs",
        ort="Bh",
    )
    ANON_LHS_BK = Sammlung(
        trace="Lhs Bk",
        groups="Wortschatz|Anonym|Lhs Bk",
        kreis="Lhs",
        ort="Bk",
    )
    ANON_LHS_BO = Sammlung(
        trace="Lhs Bo",
        groups="Wortschatz|Anonym|Lhs Bo",
        kreis="Lhs",
        ort="Bo",
    )
    ANON_LHS_DB = Sammlung(
        trace="Lhs Db",
        groups="Wortschatz|Anonym|Lhs Db",
        kreis="Lhs",
        ort="Db",
    )
    ANON_LHS_DR = Sammlung(
        trace="Lhs Dr",
        groups="Wortschatz|Anonym|Lhs Dr",
        kreis="Lhs",
        ort="Dr",
    )
    ANON_LHS_EI = Sammlung(
        trace="Lhs Ei",
        groups="Wortschatz|Anonym|Lhs Ei",
        kreis="Lhs",
        ort="Ei",
    )
    ANON_LHS_EL = Sammlung(
        trace="Lhs El",
        groups="Wortschatz|Anonym|Lhs El",
        kreis="Lhs",
        ort="El",
    )
    ANON_LHS_EM = Sammlung(
        trace="Lhs Em",
        groups="Wortschatz|Anonym|Lhs Em",
        kreis="Lhs",
        ort="Em",
    )
    ANON_LHS_ER = Sammlung(
        trace="Lhs Er",
        groups="Wortschatz|Anonym|Lhs Er",
        kreis="Lhs",
        ort="Er",
    )
    ANON_LHS_FH = Sammlung(
        trace="Lhs Fh",
        groups="Wortschatz|Anonym|Lhs Fh",
        kreis="Lhs",
        ort="Fh",
    )
    ANON_LHS_HE = Sammlung(
        trace="Lhs He",
        groups="Wortschatz|Anonym|Lhs He",
        kreis="Lhs",
        ort="He",
    )
    ANON_LHS_HO = Sammlung(
        trace="Lhs Ho",
        groups="Wortschatz|Anonym|Lhs Ho",
        kreis="Lhs",
        ort="Ho",
    )
    ANON_LHS_HÖ = Sammlung(
        trace="Lhs Hö",
        groups="Wortschatz|Anonym|Lhs Hö",
        kreis="Lhs",
        ort="Hö",
    )
    ANON_LHS_HS = Sammlung(
        trace="Lhs Hs",
        groups="Wortschatz|Anonym|Lhs Hs",
        kreis="Lhs",
        ort="Hs",
    )
    ANON_LHS_KA = Sammlung(
        trace="Lhs Ka",
        groups="Wortschatz|Anonym|Lhs Ka",
        kreis="Lhs",
        ort="Ka",
    )
    ANON_LHS_LA = Sammlung(
        trace="Lhs La",
        groups="Wortschatz|Anonym|Lhs La",
        kreis="Lhs",
        ort="La",
    )
    ANON_LHS_LH = Sammlung(
        trace="Lhs Lh",
        groups="Wortschatz|Anonym|Lhs Lh",
        kreis="Lhs",
        ort="Lh",
    )
    ANON_LHS_ME = Sammlung(
        trace="Lhs Me",
        groups="Wortschatz|Anonym|Lhs Me",
        kreis="Lhs",
        ort="Me",
    )
    ANON_LHS_NB = Sammlung(
        trace="Lhs Nb",
        groups="Wortschatz|Anonym|Lhs Nb",
        kreis="Lhs",
        ort="Nb",
    )
    ANON_LHS_NK = Sammlung(
        trace="Lhs Nk",
        groups="Wortschatz|Anonym|Lhs Nk",
        kreis="Lhs",
        ort="Nk",
    )
    ANON_LHS_OB = Sammlung(
        trace="Lhs Ob",
        groups="Wortschatz|Anonym|Lhs Ob",
        kreis="Lhs",
        ort="Ob",
    )
    ANON_LHS_OL = Sammlung(
        trace="Lhs Ol",
        groups="Wortschatz|Anonym|Lhs Ol",
        kreis="Lhs",
        ort="Ol",
    )
    ANON_LHS_ON = Sammlung(
        trace="Lhs On",
        groups="Wortschatz|Anonym|Lhs On",
        kreis="Lhs",
        ort="On",
    )
    ANON_LHS_SE = Sammlung(
        trace="Lhs Se",
        groups="Wortschatz|Anonym|Lhs Se",
        kreis="Lhs",
        ort="Se",
    )
    ANON_LHS_SK = Sammlung(
        trace="Lhs Sk",
        groups="Wortschatz|Anonym|Lhs Sk",
        kreis="Lhs",
        ort="Sk",
    )
    ANON_LHS_SM = Sammlung(
        trace="Lhs Sm",
        groups="Wortschatz|Anonym|Lhs Sm",
        kreis="Lhs",
        ort="Sm",
    )
    ANON_LHS_SR = Sammlung(
        trace="Lhs Sr",
        groups="Wortschatz|Anonym|Lhs Sr",
        kreis="Lhs",
        ort="Sr",
    )
    ANON_LHS_ST = Sammlung(
        trace="Lhs St",
        groups="Wortschatz|Anonym|Lhs St",
        kreis="Lhs",
        ort="St",
    )
    ANON_LHS_TE = Sammlung(
        trace="Lhs Te",
        groups="Wortschatz|Anonym|Lhs Te",
        kreis="Lhs",
        ort="Te",
    )
    ANON_LHS_TH = Sammlung(
        trace="Lhs Th",
        groups="Wortschatz|Anonym|Lhs Th",
        kreis="Lhs",
        ort="Th",
    )
    ANON_LHS_VE = Sammlung(
        trace="Lhs Ve",
        groups="Wortschatz|Anonym|Lhs Ve",
        kreis="Lhs",
        ort="Ve",
    )
    ANON_LHS_VI = Sammlung(
        trace="Lhs Vi",
        groups="Wortschatz|Anonym|Lhs Vi",
        kreis="Lhs",
        ort="Vi",
    )
    ANON_LHS_WE = Sammlung(
        trace="Lhs We",
        groups="Wortschatz|Anonym|Lhs We",
        kreis="Lhs",
        ort="We",
    )
    ANON_LHS_WI = Sammlung(
        trace="Lhs Wi",
        groups="Wortschatz|Anonym|Lhs Wi",
        kreis="Lhs",
        ort="Wi",
    )
    ANON_LHS_WL = Sammlung(
        trace="Lhs Wl",
        groups="Wortschatz|Anonym|Lhs Wl",
        kreis="Lhs",
        ort="Wl",
    )
    ANON_LHS_WN = Sammlung(
        trace="Lhs Wn",
        groups="Wortschatz|Anonym|Lhs Wn",
        kreis="Lhs",
        ort="Wn",
    )
    ANON_LHS_WP = Sammlung(
        trace="Lhs Wp",
        groups="Wortschatz|Anonym|Lhs Wp",
        kreis="Lhs",
        ort="Wp",
    )
    ANON_LHS_WS = Sammlung(
        trace="Lhs Ws",
        groups="Wortschatz|Anonym|Lhs Ws",
        kreis="Lhs",
        ort="Ws",
    )
    ANON_LIN_AL = Sammlung(
        trace="Lin Al",
        groups="Wortschatz|Anonym|Lin Al",
        kreis="Lin",
        ort="Al",
    )
    ANON_LIN_AV = Sammlung(
        trace="Lin Av",
        groups="Wortschatz|Anonym|Lin Av",
        kreis="Lin",
        ort="Av",
    )
    ANON_LIN_AX = Sammlung(
        trace="Lin Ax",
        groups="Wortschatz|Anonym|Lin Ax",
        kreis="Lin",
        ort="Ax",
    )
    ANON_LIN_AY = Sammlung(
        trace="Lin Ay",
        groups="Wortschatz|Anonym|Lin Ay",
        kreis="Lin",
        ort="Ay",
    )
    ANON_LIN_BA = Sammlung(
        trace="Lin Ba",
        groups="Wortschatz|Anonym|Lin Ba",
        kreis="Lin",
        ort="Ba",
    )
    ANON_LIN_BE = Sammlung(
        trace="Lin Be",
        groups="Wortschatz|Anonym|Lin Be",
        kreis="Lin",
        ort="Be",
    )
    ANON_LIN_BH = Sammlung(
        trace="Lin Bh",
        groups="Wortschatz|Anonym|Lin Bh",
        kreis="Lin",
        ort="Bh",
    )
    ANON_LIN_BI = Sammlung(
        trace="Lin Bi",
        groups="Wortschatz|Anonym|Lin Bi",
        kreis="Lin",
        ort="Bi",
    )
    ANON_LIN_BK = Sammlung(
        trace="Lin Bk",
        groups="Wortschatz|Anonym|Lin Bk",
        kreis="Lin",
        ort="Bk",
    )
    ANON_LIN_BL = Sammlung(
        trace="Lin Bl",
        groups="Wortschatz|Anonym|Lin Bl",
        kreis="Lin",
        ort="Bl",
    )
    ANON_LIN_BR = Sammlung(
        trace="Lin Br",
        groups="Wortschatz|Anonym|Lin Br",
        kreis="Lin",
        ort="Br",
    )
    ANON_LIN_BS = Sammlung(
        trace="Lin Bs",
        groups="Wortschatz|Anonym|Lin Bs",
        kreis="Lin",
        ort="Bs",
    )
    ANON_LIN_BT = Sammlung(
        trace="Lin Bt",
        groups="Wortschatz|Anonym|Lin Bt",
        kreis="Lin",
        ort="Bt",
    )
    ANON_LIN_BW = Sammlung(
        trace="Lin Bw",
        groups="Wortschatz|Anonym|Lin Bw",
        kreis="Lin",
        ort="Bw",
    )
    ANON_LIN_BX = Sammlung(
        trace="Lin Bx",
        groups="Wortschatz|Anonym|Lin Bx",
        kreis="Lin",
        ort="Bx",
    )
    ANON_LIN_DA = Sammlung(
        trace="Lin Da",
        groups="Wortschatz|Anonym|Lin Da",
        kreis="Lin",
        ort="Da",
    )
    ANON_LIN_DP = Sammlung(
        trace="Lin Dp",
        groups="Wortschatz|Anonym|Lin Dp",
        kreis="Lin",
        ort="Dp",
    )
    ANON_LIN_EB = Sammlung(
        trace="Lin Eb",
        groups="Wortschatz|Anonym|Lin Eb",
        kreis="Lin",
        ort="Eb",
    )
    ANON_LIN_EM = Sammlung(
        trace="Lin Em",
        groups="Wortschatz|Anonym|Lin Em",
        kreis="Lin",
        ort="Em",
    )
    ANON_LIN_ES = Sammlung(
        trace="Lin Es",
        groups="Wortschatz|Anonym|Lin Es",
        kreis="Lin",
        ort="Es",
    )
    ANON_LIN_FR = Sammlung(
        trace="Lin Fr",
        groups="Wortschatz|Anonym|Lin Fr",
        kreis="Lin",
        ort="Fr",
    )
    ANON_LIN_GE = Sammlung(
        trace="Lin Ge",
        groups="Wortschatz|Anonym|Lin Ge",
        kreis="Lin",
        ort="Ge",
    )
    ANON_LIN_GL = Sammlung(
        trace="Lin Gl",
        groups="Wortschatz|Anonym|Lin Gl",
        kreis="Lin",
        ort="Gl",
    )
    ANON_LIN_HA = Sammlung(
        trace="Lin Ha",
        groups="Wortschatz|Anonym|Lin Ha",
        kreis="Lin",
        ort="Ha",
    )
    ANON_LIN_HD = Sammlung(
        trace="Lin Hd",
        groups="Wortschatz|Anonym|Lin Hd",
        kreis="Lin",
        ort="Hd",
    )
    ANON_LIN_HH = Sammlung(
        trace="Lin Hh",
        groups="Wortschatz|Anonym|Lin Hh",
        kreis="Lin",
        ort="Hh",
    )
    ANON_LIN_HO = Sammlung(
        trace="Lin Ho",
        groups="Wortschatz|Anonym|Lin Ho",
        kreis="Lin",
        ort="Ho",
    )
    ANON_LIN_LA = Sammlung(
        trace="Lin La",
        groups="Wortschatz|Anonym|Lin La",
        kreis="Lin",
        ort="La",
    )
    ANON_LIN_LE = Sammlung(
        trace="Lin Le",
        groups="Wortschatz|Anonym|Lin Le",
        kreis="Lin",
        ort="Le",
    )
    ANON_LIN_LI = Sammlung(
        trace="Lin Li",
        groups="Wortschatz|Anonym|Lin Li",
        kreis="Lin",
        ort="Li",
    )
    ANON_LIN_LO = Sammlung(
        trace="Lin Lo",
        groups="Wortschatz|Anonym|Lin Lo",
        kreis="Lin",
        ort="Lo",
    )
    ANON_LIN_LS = Sammlung(
        trace="Lin Ls",
        groups="Wortschatz|Anonym|Lin Ls",
        kreis="Lin",
        ort="Ls",
    )
    ANON_LIN_LT = Sammlung(
        trace="Lin Lt",
        groups="Wortschatz|Anonym|Lin Lt",
        kreis="Lin",
        ort="Lt",
    )
    ANON_LIN_LX = Sammlung(
        trace="Lin Lx",
        groups="Wortschatz|Anonym|Lin Lx",
        kreis="Lin",
        ort="Lx",
    )
    ANON_LIN_ME = Sammlung(
        trace="Lin Me",
        groups="Wortschatz|Anonym|Lin Me",
        kreis="Lin",
        ort="Me",
    )
    ANON_LIN_MR = Sammlung(
        trace="Lin Mr",
        groups="Wortschatz|Anonym|Lin Mr",
        kreis="Lin",
        ort="Mr",
    )
    ANON_LIN_MU = Sammlung(
        trace="Lin Mu",
        groups="Wortschatz|Anonym|Lin Mu",
        kreis="Lin",
        ort="Mu",
    )
    ANON_LIN_NL = Sammlung(
        trace="Lin Nl",
        groups="Wortschatz|Anonym|Lin Nl",
        kreis="Lin",
        ort="Nl",
    )
    ANON_LIN_PL = Sammlung(
        trace="Lin Pl",
        groups="Wortschatz|Anonym|Lin Pl",
        kreis="Lin",
        ort="Pl",
    )
    ANON_LIN_PO = Sammlung(
        trace="Lin Po",
        groups="Wortschatz|Anonym|Lin Po",
        kreis="Lin",
        ort="Po",
    )
    ANON_LIN_SB = Sammlung(
        trace="Lin Sb",
        groups="Wortschatz|Anonym|Lin Sb",
        kreis="Lin",
        ort="Sb",
    )
    ANON_LIN_SC = Sammlung(
        trace="Lin Sc",
        groups="Wortschatz|Anonym|Lin Sc",
        kreis="Lin",
        ort="Sc",
    )
    ANON_LIN_SD = Sammlung(
        trace="Lin Sd",
        groups="Wortschatz|Anonym|Lin Sd",
        kreis="Lin",
        ort="Sd",
    )
    ANON_LIN_SL = Sammlung(
        trace="Lin Sl",
        groups="Wortschatz|Anonym|Lin Sl",
        kreis="Lin",
        ort="Sl",
    )
    ANON_LIN_SN = Sammlung(
        trace="Lin Sn",
        groups="Wortschatz|Anonym|Lin Sn",
        kreis="Lin",
        ort="Sn",
    )
    ANON_LIN_SP = Sammlung(
        trace="Lin Sp",
        groups="Wortschatz|Anonym|Lin Sp",
        kreis="Lin",
        ort="Sp",
    )
    ANON_LIN_ST = Sammlung(
        trace="Lin St",
        groups="Wortschatz|Anonym|Lin St",
        kreis="Lin",
        ort="St",
    )
    ANON_LIN_SU = Sammlung(
        trace="Lin Su",
        groups="Wortschatz|Anonym|Lin Su",
        kreis="Lin",
        ort="Su",
    )
    ANON_LIN_TH = Sammlung(
        trace="Lin Th",
        groups="Wortschatz|Anonym|Lin Th",
        kreis="Lin",
        ort="Th",
    )
    ANON_LIN_VA = Sammlung(
        trace="Lin Va",
        groups="Wortschatz|Anonym|Lin Va",
        kreis="Lin",
        ort="Va",
    )
    ANON_LIN_VH = Sammlung(
        trace="Lin Vh",
        groups="Wortschatz|Anonym|Lin Vh",
        kreis="Lin",
        ort="Vh",
    )
    ANON_LIN_WD = Sammlung(
        trace="Lin Wd",
        groups="Wortschatz|Anonym|Lin Wd",
        kreis="Lin",
        ort="Wd",
    )
    ANON_LIN_WE = Sammlung(
        trace="Lin We",
        groups="Wortschatz|Anonym|Lin We",
        kreis="Lin",
        ort="We",
    )
    ANON_LST_AG = Sammlung(
        trace="Lst Ag",
        groups="Wortschatz|Anonym|Lst Ag",
        kreis="Lst",
        ort="Ag",
    )
    ANON_LST_AN = Sammlung(
        trace="Lst An",
        groups="Wortschatz|Anonym|Lst An",
        kreis="Lst",
        ort="An",
    )
    ANON_LST_AR = Sammlung(
        trace="Lst Ar",
        groups="Wortschatz|Anonym|Lst Ar",
        kreis="Lst",
        ort="Ar",
    )
    ANON_LST_BB = Sammlung(
        trace="Lst Bb",
        groups="Wortschatz|Anonym|Lst Bb",
        kreis="Lst",
        ort="Bb",
    )
    ANON_LST_BF = Sammlung(
        trace="Lst Bf",
        groups="Wortschatz|Anonym|Lst Bf",
        kreis="Lst",
        ort="Bf",
    )
    ANON_LST_BG = Sammlung(
        trace="Lst Bg",
        groups="Wortschatz|Anonym|Lst Bg",
        kreis="Lst",
        ort="Bg",
    )
    ANON_LST_BH = Sammlung(
        trace="Lst Bh",
        groups="Wortschatz|Anonym|Lst Bh",
        kreis="Lst",
        ort="Bh",
    )
    ANON_LST_BÖ = Sammlung(
        trace="Lst Bö",
        groups="Wortschatz|Anonym|Lst Bö",
        kreis="Lst",
        ort="Bö",
    )
    ANON_LST_DH = Sammlung(
        trace="Lst Dh",
        groups="Wortschatz|Anonym|Lst Dh",
        kreis="Lst",
        ort="Dh",
    )
    ANON_LST_DR = Sammlung(
        trace="Lst Dr",
        groups="Wortschatz|Anonym|Lst Dr",
        kreis="Lst",
        ort="Dr",
    )
    ANON_LST_EB = Sammlung(
        trace="Lst Eb",
        groups="Wortschatz|Anonym|Lst Eb",
        kreis="Lst",
        ort="Eb",
    )
    ANON_LST_EF = Sammlung(
        trace="Lst Ef",
        groups="Wortschatz|Anonym|Lst Ef",
        kreis="Lst",
        ort="Ef",
    )
    ANON_LST_EH = Sammlung(
        trace="Lst Eh",
        groups="Wortschatz|Anonym|Lst Eh",
        kreis="Lst",
        ort="Eh",
    )
    ANON_LST_EI = Sammlung(
        trace="Lst Ei",
        groups="Wortschatz|Anonym|Lst Ei",
        kreis="Lst",
        ort="Ei",
    )
    ANON_LST_ER = Sammlung(
        trace="Lst Er",
        groups="Wortschatz|Anonym|Lst Er",
        kreis="Lst",
        ort="Er",
    )
    ANON_LST_ES = Sammlung(
        trace="Lst Es",
        groups="Wortschatz|Anonym|Lst Es",
        kreis="Lst",
        ort="Es",
    )
    ANON_LST_GE = Sammlung(
        trace="Lst Ge",
        groups="Wortschatz|Anonym|Lst Ge",
        kreis="Lst",
        ort="Ge",
    )
    ANON_LST_HE = Sammlung(
        trace="Lst He",
        groups="Wortschatz|Anonym|Lst He",
        kreis="Lst",
        ort="He",
    )
    ANON_LST_HH = Sammlung(
        trace="Lst Hh",
        groups="Wortschatz|Anonym|Lst Hh",
        kreis="Lst",
        ort="Hh",
    )
    ANON_LST_HO = Sammlung(
        trace="Lst Ho",
        groups="Wortschatz|Anonym|Lst Ho",
        kreis="Lst",
        ort="Ho",
    )
    ANON_LST_HS = Sammlung(
        trace="Lst Hs",
        groups="Wortschatz|Anonym|Lst Hs",
        kreis="Lst",
        ort="Hs",
    )
    ANON_LST_KA = Sammlung(
        trace="Lst Ka",
        groups="Wortschatz|Anonym|Lst Ka",
        kreis="Lst",
        ort="Ka",
    )
    ANON_LST_KH = Sammlung(
        trace="Lst Kh",
        groups="Wortschatz|Anonym|Lst Kh",
        kreis="Lst",
        ort="Kh",
    )
    ANON_LST_KL = Sammlung(
        trace="Lst Kl",
        groups="Wortschatz|Anonym|Lst Kl",
        kreis="Lst",
        ort="Kl",
    )
    ANON_LST_KN = Sammlung(
        trace="Lst Kn",
        groups="Wortschatz|Anonym|Lst Kn",
        kreis="Lst",
        ort="Kn",
    )
    ANON_LST_KP = Sammlung(
        trace="Lst Kp",
        groups="Wortschatz|Anonym|Lst Kp",
        kreis="Lst",
        ort="Kp",
    )
    ANON_LST_LA = Sammlung(
        trace="Lst La",
        groups="Wortschatz|Anonym|Lst La",
        kreis="Lst",
        ort="La",
    )
    ANON_LST_LI = Sammlung(
        trace="Lst Li",
        groups="Wortschatz|Anonym|Lst Li",
        kreis="Lst",
        ort="Li",
    )
    ANON_LST_LR = Sammlung(
        trace="Lst Lr",
        groups="Wortschatz|Anonym|Lst Lr",
        kreis="Lst",
        ort="Lr",
    )
    ANON_LST_LS = Sammlung(
        trace="Lst Ls",
        groups="Wortschatz|Anonym|Lst Ls",
        kreis="Lst",
        ort="Ls",
    )
    ANON_LST_ME = Sammlung(
        trace="Lst Me",
        groups="Wortschatz|Anonym|Lst Me",
        kreis="Lst",
        ort="Me",
    )
    ANON_LST_MH = Sammlung(
        trace="Lst Mh",
        groups="Wortschatz|Anonym|Lst Mh",
        kreis="Lst",
        ort="Mh",
    )
    ANON_LST_MÖ = Sammlung(
        trace="Lst Mö",
        groups="Wortschatz|Anonym|Lst Mö",
        kreis="Lst",
        ort="Mö",
    )
    ANON_LST_MS = Sammlung(
        trace="Lst Ms",
        groups="Wortschatz|Anonym|Lst Ms",
        kreis="Lst",
        ort="Ms",
    )
    ANON_LST_MZ = Sammlung(
        trace="Lst Mz",
        groups="Wortschatz|Anonym|Lst Mz",
        kreis="Lst",
        ort="Mz",
    )
    ANON_LST_OH = Sammlung(
        trace="Lst Oh",
        groups="Wortschatz|Anonym|Lst Oh",
        kreis="Lst",
        ort="Oh",
    )
    ANON_LST_ÖS = Sammlung(
        trace="Lst Ös",
        groups="Wortschatz|Anonym|Lst Ös",
        kreis="Lst",
        ort="Ös",
    )
    ANON_LST_RI = Sammlung(
        trace="Lst Ri",
        groups="Wortschatz|Anonym|Lst Ri",
        kreis="Lst",
        ort="Ri",
    )
    ANON_LST_RO = Sammlung(
        trace="Lst Ro",
        groups="Wortschatz|Anonym|Lst Ro",
        kreis="Lst",
        ort="Ro",
    )
    ANON_LST_RÜ = Sammlung(
        trace="Lst Rü",
        groups="Wortschatz|Anonym|Lst Rü",
        kreis="Lst",
        ort="Rü",
    )
    ANON_LST_SC = Sammlung(
        trace="Lst Sc",
        groups="Wortschatz|Anonym|Lst Sc",
        kreis="Lst",
        ort="Sc",
    )
    ANON_LST_SL = Sammlung(
        trace="Lst Sl",
        groups="Wortschatz|Anonym|Lst Sl",
        kreis="Lst",
        ort="Sl",
    )
    ANON_LST_SM = Sammlung(
        trace="Lst Sm",
        groups="Wortschatz|Anonym|Lst Sm",
        kreis="Lst",
        ort="Sm",
    )
    ANON_LST_ST = Sammlung(
        trace="Lst St",
        groups="Wortschatz|Anonym|Lst St",
        kreis="Lst",
        ort="St",
    )
    ANON_LST_SU = Sammlung(
        trace="Lst Su",
        groups="Wortschatz|Anonym|Lst Su",
        kreis="Lst",
        ort="Su",
    )
    ANON_LST_VÖ = Sammlung(
        trace="Lst Vö",
        groups="Wortschatz|Anonym|Lst Vö",
        kreis="Lst",
        ort="Vö",
    )
    ANON_LST_WK = Sammlung(
        trace="Lst Wk",
        groups="Wortschatz|Anonym|Lst Wk",
        kreis="Lst",
        ort="Wk",
    )
    ANON_LÜB_AL = Sammlung(
        trace="Lüb Al",
        groups="Wortschatz|Anonym|Lüb Al",
        kreis="Lüb",
        ort="Al",
    )
    ANON_LÜB_AR = Sammlung(
        trace="Lüb Ar",
        groups="Wortschatz|Anonym|Lüb Ar",
        kreis="Lüb",
        ort="Ar",
    )
    ANON_LÜB_AS = Sammlung(
        trace="Lüb As",
        groups="Wortschatz|Anonym|Lüb As",
        kreis="Lüb",
        ort="As",
    )
    ANON_LÜB_BA = Sammlung(
        trace="Lüb Ba",
        groups="Wortschatz|Anonym|Lüb Ba",
        kreis="Lüb",
        ort="Ba",
    )
    ANON_LÜB_BH = Sammlung(
        trace="Lüb Bh",
        groups="Wortschatz|Anonym|Lüb Bh",
        kreis="Lüb",
        ort="Bh",
    )
    ANON_LÜB_BL = Sammlung(
        trace="Lüb Bl",
        groups="Wortschatz|Anonym|Lüb Bl",
        kreis="Lüb",
        ort="Bl",
    )
    ANON_LÜB_BR = Sammlung(
        trace="Lüb Br",
        groups="Wortschatz|Anonym|Lüb Br",
        kreis="Lüb",
        ort="Br",
    )
    ANON_LÜB_BÜ = Sammlung(
        trace="Lüb Bü",
        groups="Wortschatz|Anonym|Lüb Bü",
        kreis="Lüb",
        ort="Bü",
    )
    ANON_LÜB_DE = Sammlung(
        trace="Lüb De",
        groups="Wortschatz|Anonym|Lüb De",
        kreis="Lüb",
        ort="De",
    )
    ANON_LÜB_DI = Sammlung(
        trace="Lüb Di",
        groups="Wortschatz|Anonym|Lüb Di",
        kreis="Lüb",
        ort="Di",
    )
    ANON_LÜB_DR = Sammlung(
        trace="Lüb Dr",
        groups="Wortschatz|Anonym|Lüb Dr",
        kreis="Lüb",
        ort="Dr",
    )
    ANON_LÜB_EN = Sammlung(
        trace="Lüb En",
        groups="Wortschatz|Anonym|Lüb En",
        kreis="Lüb",
        ort="En",
    )
    ANON_LÜB_FA = Sammlung(
        trace="Lüb Fa",
        groups="Wortschatz|Anonym|Lüb Fa",
        kreis="Lüb",
        ort="Fa",
    )
    ANON_LÜB_FI = Sammlung(
        trace="Lüb Fi",
        groups="Wortschatz|Anonym|Lüb Fi",
        kreis="Lüb",
        ort="Fi",
    )
    ANON_LÜB_FR = Sammlung(
        trace="Lüb Fr",
        groups="Wortschatz|Anonym|Lüb Fr",
        kreis="Lüb",
        ort="Fr",
    )
    ANON_LÜB_FS = Sammlung(
        trace="Lüb Fs",
        groups="Wortschatz|Anonym|Lüb Fs",
        kreis="Lüb",
        ort="Fs",
    )
    ANON_LÜB_GB = Sammlung(
        trace="Lüb Gb",
        groups="Wortschatz|Anonym|Lüb Gb",
        kreis="Lüb",
        ort="Gb",
    )
    ANON_LÜB_GE = Sammlung(
        trace="Lüb Ge",
        groups="Wortschatz|Anonym|Lüb Ge",
        kreis="Lüb",
        ort="Ge",
    )
    ANON_LÜB_HA = Sammlung(
        trace="Lüb Ha",
        groups="Wortschatz|Anonym|Lüb Ha",
        kreis="Lüb",
        ort="Ha",
    )
    ANON_LÜB_HE = Sammlung(
        trace="Lüb He",
        groups="Wortschatz|Anonym|Lüb He",
        kreis="Lüb",
        ort="He",
    )
    ANON_LÜB_HH = Sammlung(
        trace="Lüb Hh",
        groups="Wortschatz|Anonym|Lüb Hh",
        kreis="Lüb",
        ort="Hh",
    )
    ANON_LÜB_HL = Sammlung(
        trace="Lüb Hl",
        groups="Wortschatz|Anonym|Lüb Hl",
        kreis="Lüb",
        ort="Hl",
    )
    ANON_LÜB_HO = Sammlung(
        trace="Lüb Ho",
        groups="Wortschatz|Anonym|Lüb Ho",
        kreis="Lüb",
        ort="Ho",
    )
    ANON_LÜB_HT = Sammlung(
        trace="Lüb Ht",
        groups="Wortschatz|Anonym|Lüb Ht",
        kreis="Lüb",
        ort="Ht",
    )
    ANON_LÜB_HÜ = Sammlung(
        trace="Lüb Hü",
        groups="Wortschatz|Anonym|Lüb Hü",
        kreis="Lüb",
        ort="Hü",
    )
    ANON_LÜB_IS = Sammlung(
        trace="Lüb Is",
        groups="Wortschatz|Anonym|Lüb Is",
        kreis="Lüb",
        ort="Is",
    )
    ANON_LÜB_KL = Sammlung(
        trace="Lüb Kl",
        groups="Wortschatz|Anonym|Lüb Kl",
        kreis="Lüb",
        ort="Kl",
    )
    ANON_LÜB_LB = Sammlung(
        trace="Lüb Lb",
        groups="Wortschatz|Anonym|Lüb Lb",
        kreis="Lüb",
        ort="Lb",
    )
    ANON_LÜB_LE = Sammlung(
        trace="Lüb Le",
        groups="Wortschatz|Anonym|Lüb Le",
        kreis="Lüb",
        ort="Le",
    )
    ANON_LÜB_MO = Sammlung(
        trace="Lüb Mo",
        groups="Wortschatz|Anonym|Lüb Mo",
        kreis="Lüb",
        ort="Mo",
    )
    ANON_LÜB_NE = Sammlung(
        trace="Lüb Ne",
        groups="Wortschatz|Anonym|Lüb Ne",
        kreis="Lüb",
        ort="Ne",
    )
    ANON_LÜB_NM = Sammlung(
        trace="Lüb Nm",
        groups="Wortschatz|Anonym|Lüb Nm",
        kreis="Lüb",
        ort="Nm",
    )
    ANON_LÜB_OB = Sammlung(
        trace="Lüb Ob",
        groups="Wortschatz|Anonym|Lüb Ob",
        kreis="Lüb",
        ort="Ob",
    )
    ANON_LÜB_OD = Sammlung(
        trace="Lüb Od",
        groups="Wortschatz|Anonym|Lüb Od",
        kreis="Lüb",
        ort="Od",
    )
    ANON_LÜB_OF = Sammlung(
        trace="Lüb Of",
        groups="Wortschatz|Anonym|Lüb Of",
        kreis="Lüb",
        ort="Of",
    )
    ANON_LÜB_OM = Sammlung(
        trace="Lüb Om",
        groups="Wortschatz|Anonym|Lüb Om",
        kreis="Lüb",
        ort="Om",
    )
    ANON_LÜB_OW = Sammlung(
        trace="Lüb Ow",
        groups="Wortschatz|Anonym|Lüb Ow",
        kreis="Lüb",
        ort="Ow",
    )
    ANON_LÜB_PO = Sammlung(
        trace="Lüb Po",
        groups="Wortschatz|Anonym|Lüb Po",
        kreis="Lüb",
        ort="Po",
    )
    ANON_LÜB_PS = Sammlung(
        trace="Lüb Ps",
        groups="Wortschatz|Anonym|Lüb Ps",
        kreis="Lüb",
        ort="Ps",
    )
    ANON_LÜB_RA = Sammlung(
        trace="Lüb Ra",
        groups="Wortschatz|Anonym|Lüb Ra",
        kreis="Lüb",
        ort="Ra",
    )
    ANON_LÜB_SH = Sammlung(
        trace="Lüb Sh",
        groups="Wortschatz|Anonym|Lüb Sh",
        kreis="Lüb",
        ort="Sh",
    )
    ANON_LÜB_SI = Sammlung(
        trace="Lüb Si",
        groups="Wortschatz|Anonym|Lüb Si",
        kreis="Lüb",
        ort="Si",
    )
    ANON_LÜB_SN = Sammlung(
        trace="Lüb Sn",
        groups="Wortschatz|Anonym|Lüb Sn",
        kreis="Lüb",
        ort="Sn",
    )
    ANON_LÜB_ST = Sammlung(
        trace="Lüb St",
        groups="Wortschatz|Anonym|Lüb St",
        kreis="Lüb",
        ort="St",
    )
    ANON_LÜB_SU = Sammlung(
        trace="Lüb Su",
        groups="Wortschatz|Anonym|Lüb Su",
        kreis="Lüb",
        ort="Su",
    )
    ANON_LÜB_TE = Sammlung(
        trace="Lüb Te",
        groups="Wortschatz|Anonym|Lüb Te",
        kreis="Lüb",
        ort="Te",
    )
    ANON_LÜB_TI = Sammlung(
        trace="Lüb Ti",
        groups="Wortschatz|Anonym|Lüb Ti",
        kreis="Lüb",
        ort="Ti",
    )
    ANON_LÜB_TO = Sammlung(
        trace="Lüb To",
        groups="Wortschatz|Anonym|Lüb To",
        kreis="Lüb",
        ort="To",
    )
    ANON_LÜB_TW = Sammlung(
        trace="Lüb Tw",
        groups="Wortschatz|Anonym|Lüb Tw",
        kreis="Lüb",
        ort="Tw",
    )
    ANON_LÜB_VA = Sammlung(
        trace="Lüb Va",
        groups="Wortschatz|Anonym|Lüb Va",
        kreis="Lüb",
        ort="Va",
    )
    ANON_LÜB_VE = Sammlung(
        trace="Lüb Ve",
        groups="Wortschatz|Anonym|Lüb Ve",
        kreis="Lüb",
        ort="Ve",
    )
    ANON_LÜB_VH = Sammlung(
        trace="Lüb Vh",
        groups="Wortschatz|Anonym|Lüb Vh",
        kreis="Lüb",
        ort="Vh",
    )
    ANON_LÜB_WE = Sammlung(
        trace="Lüb We",
        groups="Wortschatz|Anonym|Lüb We",
        kreis="Lüb",
        ort="We",
    )
    ANON_LÜB_WH = Sammlung(
        trace="Lüb Wh",
        groups="Wortschatz|Anonym|Lüb Wh",
        kreis="Lüb",
        ort="Wh",
    )
    ANON_LÜB_WP = Sammlung(
        trace="Lüb Wp",
        groups="Wortschatz|Anonym|Lüb Wp",
        kreis="Lüb",
        ort="Wp",
    )
    ANON_MEL_AM = Sammlung(
        trace="Mel Am",
        groups="Wortschatz|Anonym|Mel Am",
        kreis="Mel",
        ort="Am",
    )
    ANON_MEL_BM = Sammlung(
        trace="Mel Bm",
        groups="Wortschatz|Anonym|Mel Bm",
        kreis="Mel",
        ort="Bm",
    )
    ANON_MEL_BU = Sammlung(
        trace="Mel Bu",
        groups="Wortschatz|Anonym|Mel Bu",
        kreis="Mel",
        ort="Bu",
    )
    ANON_MEL_DD = Sammlung(
        trace="Mel Dd",
        groups="Wortschatz|Anonym|Mel Dd",
        kreis="Mel",
        ort="Dd",
    )
    ANON_MEL_DÖ = Sammlung(
        trace="Mel Dö",
        groups="Wortschatz|Anonym|Mel Dö",
        kreis="Mel",
        ort="Dö",
    )
    ANON_MEL_DR = Sammlung(
        trace="Mel Dr",
        groups="Wortschatz|Anonym|Mel Dr",
        kreis="Mel",
        ort="Dr",
    )
    ANON_MEL_DT = Sammlung(
        trace="Mel Dt",
        groups="Wortschatz|Anonym|Mel Dt",
        kreis="Mel",
        ort="Dt",
    )
    ANON_MEL_DÜ = Sammlung(
        trace="Mel Dü",
        groups="Wortschatz|Anonym|Mel Dü",
        kreis="Mel",
        ort="Dü",
    )
    ANON_MEL_EB = Sammlung(
        trace="Mel Eb",
        groups="Wortschatz|Anonym|Mel Eb",
        kreis="Mel",
        ort="Eb",
    )
    ANON_MEL_FÖ = Sammlung(
        trace="Mel Fö",
        groups="Wortschatz|Anonym|Mel Fö",
        kreis="Mel",
        ort="Fö",
    )
    ANON_MEL_GA = Sammlung(
        trace="Mel Ga",
        groups="Wortschatz|Anonym|Mel Ga",
        kreis="Mel",
        ort="Ga",
    )
    ANON_MEL_GD = Sammlung(
        trace="Mel Gd",
        groups="Wortschatz|Anonym|Mel Gd",
        kreis="Mel",
        ort="Gd",
    )
    ANON_MEL_GE = Sammlung(
        trace="Mel Ge",
        groups="Wortschatz|Anonym|Mel Ge",
        kreis="Mel",
        ort="Ge",
    )
    ANON_MEL_HD = Sammlung(
        trace="Mel Hd",
        groups="Wortschatz|Anonym|Mel Hd",
        kreis="Mel",
        ort="Hd",
    )
    ANON_MEL_HO = Sammlung(
        trace="Mel Ho",
        groups="Wortschatz|Anonym|Mel Ho",
        kreis="Mel",
        ort="Ho",
    )
    ANON_MEL_HU = Sammlung(
        trace="Mel Hu",
        groups="Wortschatz|Anonym|Mel Hu",
        kreis="Mel",
        ort="Hu",
    )
    ANON_MEL_KR = Sammlung(
        trace="Mel Kr",
        groups="Wortschatz|Anonym|Mel Kr",
        kreis="Mel",
        ort="Kr",
    )
    ANON_MEL_KÜ = Sammlung(
        trace="Mel Kü",
        groups="Wortschatz|Anonym|Mel Kü",
        kreis="Mel",
        ort="Kü",
    )
    ANON_MEL_MD = Sammlung(
        trace="Mel Md",
        groups="Wortschatz|Anonym|Mel Md",
        kreis="Mel",
        ort="Md",
    )
    ANON_MEL_ME = Sammlung(
        trace="Mel Me",
        groups="Wortschatz|Anonym|Mel Me",
        kreis="Mel",
        ort="Me",
    )
    ANON_MEL_NF = Sammlung(
        trace="Mel Nf",
        groups="Wortschatz|Anonym|Mel Nf",
        kreis="Mel",
        ort="Nf",
    )
    ANON_MEL_NK = Sammlung(
        trace="Mel Nk",
        groups="Wortschatz|Anonym|Mel Nk",
        kreis="Mel",
        ort="Nk",
    )
    ANON_MEL_NS = Sammlung(
        trace="Mel Ns",
        groups="Wortschatz|Anonym|Mel Ns",
        kreis="Mel",
        ort="Ns",
    )
    ANON_MEL_OD = Sammlung(
        trace="Mel Od",
        groups="Wortschatz|Anonym|Mel Od",
        kreis="Mel",
        ort="Od",
    )
    ANON_MEL_RI = Sammlung(
        trace="Mel Ri",
        groups="Wortschatz|Anonym|Mel Ri",
        kreis="Mel",
        ort="Ri",
    )
    ANON_MEL_SA = Sammlung(
        trace="Mel Sa",
        groups="Wortschatz|Anonym|Mel Sa",
        kreis="Mel",
        ort="Sa",
    )
    ANON_MEL_SU = Sammlung(
        trace="Mel Su",
        groups="Wortschatz|Anonym|Mel Su",
        kreis="Mel",
        ort="Su",
    )
    ANON_MEL_UB = Sammlung(
        trace="Mel Ub",
        groups="Wortschatz|Anonym|Mel Ub",
        kreis="Mel",
        ort="Ub",
    )
    ANON_MEL_ÜH = Sammlung(
        trace="Mel Üh",
        groups="Wortschatz|Anonym|Mel Üh",
        kreis="Mel",
        ort="Üh",
    )
    ANON_MEL_WD = Sammlung(
        trace="Mel Wd",
        groups="Wortschatz|Anonym|Mel Wd",
        kreis="Mel",
        ort="Wd",
    )
    ANON_MEL_WE = Sammlung(
        trace="Mel We",
        groups="Wortschatz|Anonym|Mel We",
        kreis="Mel",
        ort="We",
    )
    ANON_MEL_WH = Sammlung(
        trace="Mel Wh",
        groups="Wortschatz|Anonym|Mel Wh",
        kreis="Mel",
        ort="Wh",
    )
    ANON_MEL_WT = Sammlung(
        trace="Mel Wt",
        groups="Wortschatz|Anonym|Mel Wt",
        kreis="Mel",
        ort="Wt",
    )
    ANON_MEL_WY = Sammlung(
        trace="Mel Wy",
        groups="Wortschatz|Anonym|Mel Wy",
        kreis="Mel",
        ort="Wy",
    )
    ANON_MEP_AB = Sammlung(
        trace="Mep Ab",
        groups="Wortschatz|Anonym|Mep Ab",
        kreis="Mep",
        ort="Ab",
    )
    ANON_MEP_AD = Sammlung(
        trace="Mep Ad",
        groups="Wortschatz|Anonym|Mep Ad",
        kreis="Mep",
        ort="Ad",
    )
    ANON_MEP_AH = Sammlung(
        trace="Mep Ah",
        groups="Wortschatz|Anonym|Mep Ah",
        kreis="Mep",
        ort="Ah",
    )
    ANON_MEP_AM = Sammlung(
        trace="Mep Am",
        groups="Wortschatz|Anonym|Mep Am",
        kreis="Mep",
        ort="Am",
    )
    ANON_MEP_BH = Sammlung(
        trace="Mep Bh",
        groups="Wortschatz|Anonym|Mep Bh",
        kreis="Mep",
        ort="Bh",
    )
    ANON_MEP_BO = Sammlung(
        trace="Mep Bo",
        groups="Wortschatz|Anonym|Mep Bo",
        kreis="Mep",
        ort="Bo",
    )
    ANON_MEP_BÜ = Sammlung(
        trace="Mep Bü",
        groups="Wortschatz|Anonym|Mep Bü",
        kreis="Mep",
        ort="Bü",
    )
    ANON_MEP_DA = Sammlung(
        trace="Mep Da",
        groups="Wortschatz|Anonym|Mep Da",
        kreis="Mep",
        ort="Da",
    )
    ANON_MEP_DK = Sammlung(
        trace="Mep Dk",
        groups="Wortschatz|Anonym|Mep Dk",
        kreis="Mep",
        ort="Dk",
    )
    ANON_MEP_DO = Sammlung(
        trace="Mep Do",
        groups="Wortschatz|Anonym|Mep Do",
        kreis="Mep",
        ort="Do",
    )
    ANON_MEP_DÖ = Sammlung(
        trace="Mep Dö",
        groups="Wortschatz|Anonym|Mep Dö",
        kreis="Mep",
        ort="Dö",
    )
    ANON_MEP_EM = Sammlung(
        trace="Mep Em",
        groups="Wortschatz|Anonym|Mep Em",
        kreis="Mep",
        ort="Em",
    )
    ANON_MEP_FU = Sammlung(
        trace="Mep Fu",
        groups="Wortschatz|Anonym|Mep Fu",
        kreis="Mep",
        ort="Fu",
    )
    ANON_MEP_GB = Sammlung(
        trace="Mep Gb",
        groups="Wortschatz|Anonym|Mep Gb",
        kreis="Mep",
        ort="Gb",
    )
    ANON_MEP_GE = Sammlung(
        trace="Mep Ge",
        groups="Wortschatz|Anonym|Mep Ge",
        kreis="Mep",
        ort="Ge",
    )
    ANON_MEP_GF = Sammlung(
        trace="Mep Gf",
        groups="Wortschatz|Anonym|Mep Gf",
        kreis="Mep",
        ort="Gf",
    )
    ANON_MEP_GH = Sammlung(
        trace="Mep Gh",
        groups="Wortschatz|Anonym|Mep Gh",
        kreis="Mep",
        ort="Gh",
    )
    ANON_MEP_GS = Sammlung(
        trace="Mep Gs",
        groups="Wortschatz|Anonym|Mep Gs",
        kreis="Mep",
        ort="Gs",
    )
    ANON_MEP_HA = Sammlung(
        trace="Mep Ha",
        groups="Wortschatz|Anonym|Mep Ha",
        kreis="Mep",
        ort="Ha",
    )
    ANON_MEP_HE = Sammlung(
        trace="Mep He",
        groups="Wortschatz|Anonym|Mep He",
        kreis="Mep",
        ort="He",
    )
    ANON_MEP_HL = Sammlung(
        trace="Mep Hl",
        groups="Wortschatz|Anonym|Mep Hl",
        kreis="Mep",
        ort="Hl",
    )
    ANON_MEP_HM = Sammlung(
        trace="Mep Hm",
        groups="Wortschatz|Anonym|Mep Hm",
        kreis="Mep",
        ort="Hm",
    )
    ANON_MEP_HN = Sammlung(
        trace="Mep Hn",
        groups="Wortschatz|Anonym|Mep Hn",
        kreis="Mep",
        ort="Hn",
    )
    ANON_MEP_HO = Sammlung(
        trace="Mep Ho",
        groups="Wortschatz|Anonym|Mep Ho",
        kreis="Mep",
        ort="Ho",
    )
    ANON_MEP_HS = Sammlung(
        trace="Mep Hs",
        groups="Wortschatz|Anonym|Mep Hs",
        kreis="Mep",
        ort="Hs",
    )
    ANON_MEP_HT = Sammlung(
        trace="Mep Ht",
        groups="Wortschatz|Anonym|Mep Ht",
        kreis="Mep",
        ort="Ht",
    )
    ANON_MEP_HÜ = Sammlung(
        trace="Mep Hü",
        groups="Wortschatz|Anonym|Mep Hü",
        kreis="Mep",
        ort="Hü",
    )
    ANON_MEP_KH = Sammlung(
        trace="Mep Kh",
        groups="Wortschatz|Anonym|Mep Kh",
        kreis="Mep",
        ort="Kh",
    )
    ANON_MEP_KS = Sammlung(
        trace="Mep Ks",
        groups="Wortschatz|Anonym|Mep Ks",
        kreis="Mep",
        ort="Ks",
    )
    ANON_MEP_LA = Sammlung(
        trace="Mep La",
        groups="Wortschatz|Anonym|Mep La",
        kreis="Mep",
        ort="La",
    )
    ANON_MEP_LÄ = Sammlung(
        trace="Mep Lä",
        groups="Wortschatz|Anonym|Mep Lä",
        kreis="Mep",
        ort="Lä",
    )
    ANON_MEP_LE = Sammlung(
        trace="Mep Le",
        groups="Wortschatz|Anonym|Mep Le",
        kreis="Mep",
        ort="Le",
    )
    ANON_MEP_LG = Sammlung(
        trace="Mep Lg",
        groups="Wortschatz|Anonym|Mep Lg",
        kreis="Mep",
        ort="Lg",
    )
    ANON_MEP_LL = Sammlung(
        trace="Mep Ll",
        groups="Wortschatz|Anonym|Mep Ll",
        kreis="Mep",
        ort="Ll",
    )
    ANON_MEP_LO = Sammlung(
        trace="Mep Lo",
        groups="Wortschatz|Anonym|Mep Lo",
        kreis="Mep",
        ort="Lo",
    )
    ANON_MEP_LT = Sammlung(
        trace="Mep Lt",
        groups="Wortschatz|Anonym|Mep Lt",
        kreis="Mep",
        ort="Lt",
    )
    ANON_MEP_MP = Sammlung(
        trace="Mep Mp",
        groups="Wortschatz|Anonym|Mep Mp",
        kreis="Mep",
        ort="Mp",
    )
    ANON_MEP_RB = Sammlung(
        trace="Mep Rb",
        groups="Wortschatz|Anonym|Mep Rb",
        kreis="Mep",
        ort="Rb",
    )
    ANON_MEP_RM = Sammlung(
        trace="Mep Rm",
        groups="Wortschatz|Anonym|Mep Rm",
        kreis="Mep",
        ort="Rm",
    )
    ANON_MEP_RT = Sammlung(
        trace="Mep Rt",
        groups="Wortschatz|Anonym|Mep Rt",
        kreis="Mep",
        ort="Rt",
    )
    ANON_MEP_RÜ = Sammlung(
        trace="Mep Rü",
        groups="Wortschatz|Anonym|Mep Rü",
        kreis="Mep",
        ort="Rü",
    )
    ANON_MEP_SD = Sammlung(
        trace="Mep Sd",
        groups="Wortschatz|Anonym|Mep Sd",
        kreis="Mep",
        ort="Sd",
    )
    ANON_MEP_SF = Sammlung(
        trace="Mep Sf",
        groups="Wortschatz|Anonym|Mep Sf",
        kreis="Mep",
        ort="Sf",
    )
    ANON_MEP_SP = Sammlung(
        trace="Mep Sp",
        groups="Wortschatz|Anonym|Mep Sp",
        kreis="Mep",
        ort="Sp",
    )
    ANON_MEP_SW = Sammlung(
        trace="Mep Sw",
        groups="Wortschatz|Anonym|Mep Sw",
        kreis="Mep",
        ort="Sw",
    )
    ANON_MEP_TE = Sammlung(
        trace="Mep Te",
        groups="Wortschatz|Anonym|Mep Te",
        kreis="Mep",
        ort="Te",
    )
    ANON_MEP_TW = Sammlung(
        trace="Mep Tw",
        groups="Wortschatz|Anonym|Mep Tw",
        kreis="Mep",
        ort="Tw",
    )
    ANON_MEP_VA = Sammlung(
        trace="Mep Va",
        groups="Wortschatz|Anonym|Mep Va",
        kreis="Mep",
        ort="Va",
    )
    ANON_MEP_VE = Sammlung(
        trace="Mep Ve",
        groups="Wortschatz|Anonym|Mep Ve",
        kreis="Mep",
        ort="Ve",
    )
    ANON_MEP_VI = Sammlung(
        trace="Mep Vi",
        groups="Wortschatz|Anonym|Mep Vi",
        kreis="Mep",
        ort="Vi",
    )
    ANON_MEP_WA = Sammlung(
        trace="Mep Wa",
        groups="Wortschatz|Anonym|Mep Wa",
        kreis="Mep",
        ort="Wa",
    )
    ANON_MEP_WE = Sammlung(
        trace="Mep We",
        groups="Wortschatz|Anonym|Mep We",
        kreis="Mep",
        ort="We",
    )
    ANON_MEP_WL = Sammlung(
        trace="Mep Wl",
        groups="Wortschatz|Anonym|Mep Wl",
        kreis="Mep",
        ort="Wl",
    )
    ANON_MES_AF = Sammlung(
        trace="Mes Af",
        groups="Wortschatz|Anonym|Mes Af",
        kreis="Mes",
        ort="Af",
    )
    ANON_MES_AI = Sammlung(
        trace="Mes Ai",
        groups="Wortschatz|Anonym|Mes Ai",
        kreis="Mes",
        ort="Ai",
    )
    ANON_MES_BA = Sammlung(
        trace="Mes Ba",
        groups="Wortschatz|Anonym|Mes Ba",
        kreis="Mes",
        ort="Ba",
    )
    ANON_MES_BB = Sammlung(
        trace="Mes Bb",
        groups="Wortschatz|Anonym|Mes Bb",
        kreis="Mes",
        ort="Bb",
    )
    ANON_MES_BD = Sammlung(
        trace="Mes Bd",
        groups="Wortschatz|Anonym|Mes Bd",
        kreis="Mes",
        ort="Bd",
    )
    ANON_MES_BE = Sammlung(
        trace="Mes Be",
        groups="Wortschatz|Anonym|Mes Be",
        kreis="Mes",
        ort="Be",
    )
    ANON_MES_BF = Sammlung(
        trace="Mes Bf",
        groups="Wortschatz|Anonym|Mes Bf",
        kreis="Mes",
        ort="Bf",
    )
    ANON_MES_BH = Sammlung(
        trace="Mes Bh",
        groups="Wortschatz|Anonym|Mes Bh",
        kreis="Mes",
        ort="Bh",
    )
    ANON_MES_BK = Sammlung(
        trace="Mes Bk",
        groups="Wortschatz|Anonym|Mes Bk",
        kreis="Mes",
        ort="Bk",
    )
    ANON_MES_BL = Sammlung(
        trace="Mes Bl",
        groups="Wortschatz|Anonym|Mes Bl",
        kreis="Mes",
        ort="Bl",
    )
    ANON_MES_BÖ = Sammlung(
        trace="Mes Bö",
        groups="Wortschatz|Anonym|Mes Bö",
        kreis="Mes",
        ort="Bö",
    )
    ANON_MES_BR = Sammlung(
        trace="Mes Br",
        groups="Wortschatz|Anonym|Mes Br",
        kreis="Mes",
        ort="Br",
    )
    ANON_MES_BS = Sammlung(
        trace="Mes Bs",
        groups="Wortschatz|Anonym|Mes Bs",
        kreis="Mes",
        ort="Bs",
    )
    ANON_MES_BÜ = Sammlung(
        trace="Mes Bü",
        groups="Wortschatz|Anonym|Mes Bü",
        kreis="Mes",
        ort="Bü",
    )
    ANON_MES_BW = Sammlung(
        trace="Mes Bw",
        groups="Wortschatz|Anonym|Mes Bw",
        kreis="Mes",
        ort="Bw",
    )
    ANON_MES_DO = Sammlung(
        trace="Mes Do",
        groups="Wortschatz|Anonym|Mes Do",
        kreis="Mes",
        ort="Do",
    )
    ANON_MES_DT = Sammlung(
        trace="Mes Dt",
        groups="Wortschatz|Anonym|Mes Dt",
        kreis="Mes",
        ort="Dt",
    )
    ANON_MES_EH = Sammlung(
        trace="Mes Eh",
        groups="Wortschatz|Anonym|Mes Eh",
        kreis="Mes",
        ort="Eh",
    )
    ANON_MES_ES = Sammlung(
        trace="Mes Es",
        groups="Wortschatz|Anonym|Mes Es",
        kreis="Mes",
        ort="Es",
    )
    ANON_MES_EV = Sammlung(
        trace="Mes Ev",
        groups="Wortschatz|Anonym|Mes Ev",
        kreis="Mes",
        ort="Ev",
    )
    ANON_MES_FB = Sammlung(
        trace="Mes Fb",
        groups="Wortschatz|Anonym|Mes Fb",
        kreis="Mes",
        ort="Fb",
    )
    ANON_MES_FH = Sammlung(
        trace="Mes Fh",
        groups="Wortschatz|Anonym|Mes Fh",
        kreis="Mes",
        ort="Fh",
    )
    ANON_MES_FI = Sammlung(
        trace="Mes Fi",
        groups="Wortschatz|Anonym|Mes Fi",
        kreis="Mes",
        ort="Fi",
    )
    ANON_MES_FR = Sammlung(
        trace="Mes Fr",
        groups="Wortschatz|Anonym|Mes Fr",
        kreis="Mes",
        ort="Fr",
    )
    ANON_MES_FT = Sammlung(
        trace="Mes Ft",
        groups="Wortschatz|Anonym|Mes Ft",
        kreis="Mes",
        ort="Ft",
    )
    ANON_MES_GE = Sammlung(
        trace="Mes Ge",
        groups="Wortschatz|Anonym|Mes Ge",
        kreis="Mes",
        ort="Ge",
    )
    ANON_MES_GH = Sammlung(
        trace="Mes Gh",
        groups="Wortschatz|Anonym|Mes Gh",
        kreis="Mes",
        ort="Gh",
    )
    ANON_MES_GL = Sammlung(
        trace="Mes Gl",
        groups="Wortschatz|Anonym|Mes Gl",
        kreis="Mes",
        ort="Gl",
    )
    ANON_MES_GR = Sammlung(
        trace="Mes Gr",
        groups="Wortschatz|Anonym|Mes Gr",
        kreis="Mes",
        ort="Gr",
    )
    ANON_MES_HB = Sammlung(
        trace="Mes Hb",
        groups="Wortschatz|Anonym|Mes Hb",
        kreis="Mes",
        ort="Hb",
    )
    ANON_MES_HE = Sammlung(
        trace="Mes He",
        groups="Wortschatz|Anonym|Mes He",
        kreis="Mes",
        ort="He",
    )
    ANON_MES_HH = Sammlung(
        trace="Mes Hh",
        groups="Wortschatz|Anonym|Mes Hh",
        kreis="Mes",
        ort="Hh",
    )
    ANON_MES_HO = Sammlung(
        trace="Mes Ho",
        groups="Wortschatz|Anonym|Mes Ho",
        kreis="Mes",
        ort="Ho",
    )
    ANON_MES_KA = Sammlung(
        trace="Mes Ka",
        groups="Wortschatz|Anonym|Mes Ka",
        kreis="Mes",
        ort="Ka",
    )
    ANON_MES_KL = Sammlung(
        trace="Mes Kl",
        groups="Wortschatz|Anonym|Mes Kl",
        kreis="Mes",
        ort="Kl",
    )
    ANON_MES_KO = Sammlung(
        trace="Mes Ko",
        groups="Wortschatz|Anonym|Mes Ko",
        kreis="Mes",
        ort="Ko",
    )
    ANON_MES_KR = Sammlung(
        trace="Mes Kr",
        groups="Wortschatz|Anonym|Mes Kr",
        kreis="Mes",
        ort="Kr",
    )
    ANON_MES_KÜ = Sammlung(
        trace="Mes Kü",
        groups="Wortschatz|Anonym|Mes Kü",
        kreis="Mes",
        ort="Kü",
    )
    ANON_MES_LA = Sammlung(
        trace="Mes La",
        groups="Wortschatz|Anonym|Mes La",
        kreis="Mes",
        ort="La",
    )
    ANON_MES_LH = Sammlung(
        trace="Mes Lh",
        groups="Wortschatz|Anonym|Mes Lh",
        kreis="Mes",
        ort="Lh",
    )
    ANON_MES_ME = Sammlung(
        trace="Mes Me",
        groups="Wortschatz|Anonym|Mes Me",
        kreis="Mes",
        ort="Me",
    )
    ANON_MES_MS = Sammlung(
        trace="Mes Ms",
        groups="Wortschatz|Anonym|Mes Ms",
        kreis="Mes",
        ort="Ms",
    )
    ANON_MES_NA = Sammlung(
        trace="Mes Na",
        groups="Wortschatz|Anonym|Mes Na",
        kreis="Mes",
        ort="Na",
    )
    ANON_MES_NF = Sammlung(
        trace="Mes Nf",
        groups="Wortschatz|Anonym|Mes Nf",
        kreis="Mes",
        ort="Nf",
    )
    ANON_MES_NH = Sammlung(
        trace="Mes Nh",
        groups="Wortschatz|Anonym|Mes Nh",
        kreis="Mes",
        ort="Nh",
    )
    ANON_MES_NI = Sammlung(
        trace="Mes Ni",
        groups="Wortschatz|Anonym|Mes Ni",
        kreis="Mes",
        ort="Ni",
    )
    ANON_MES_NL = Sammlung(
        trace="Mes Nl",
        groups="Wortschatz|Anonym|Mes Nl",
        kreis="Mes",
        ort="Nl",
    )
    ANON_MES_NO = Sammlung(
        trace="Mes No",
        groups="Wortschatz|Anonym|Mes No",
        kreis="Mes",
        ort="No",
    )
    ANON_MES_NS = Sammlung(
        trace="Mes Ns",
        groups="Wortschatz|Anonym|Mes Ns",
        kreis="Mes",
        ort="Ns",
    )
    ANON_MES_NU = Sammlung(
        trace="Mes Nu",
        groups="Wortschatz|Anonym|Mes Nu",
        kreis="Mes",
        ort="Nu",
    )
    ANON_MES_ÖD = Sammlung(
        trace="Mes Öd",
        groups="Wortschatz|Anonym|Mes Öd",
        kreis="Mes",
        ort="Öd",
    )
    ANON_MES_OH = Sammlung(
        trace="Mes Oh",
        groups="Wortschatz|Anonym|Mes Oh",
        kreis="Mes",
        ort="Oh",
    )
    ANON_MES_OK = Sammlung(
        trace="Mes Ok",
        groups="Wortschatz|Anonym|Mes Ok",
        kreis="Mes",
        ort="Ok",
    )
    ANON_MES_OS = Sammlung(
        trace="Mes Os",
        groups="Wortschatz|Anonym|Mes Os",
        kreis="Mes",
        ort="Os",
    )
    ANON_MES_OT = Sammlung(
        trace="Mes Ot",
        groups="Wortschatz|Anonym|Mes Ot",
        kreis="Mes",
        ort="Ot",
    )
    ANON_MES_OW = Sammlung(
        trace="Mes Ow",
        groups="Wortschatz|Anonym|Mes Ow",
        kreis="Mes",
        ort="Ow",
    )
    ANON_MES_RA = Sammlung(
        trace="Mes Ra",
        groups="Wortschatz|Anonym|Mes Ra",
        kreis="Mes",
        ort="Ra",
    )
    ANON_MES_RB = Sammlung(
        trace="Mes Rb",
        groups="Wortschatz|Anonym|Mes Rb",
        kreis="Mes",
        ort="Rb",
    )
    ANON_MES_RE = Sammlung(
        trace="Mes Re",
        groups="Wortschatz|Anonym|Mes Re",
        kreis="Mes",
        ort="Re",
    )
    ANON_MES_RH = Sammlung(
        trace="Mes Rh",
        groups="Wortschatz|Anonym|Mes Rh",
        kreis="Mes",
        ort="Rh",
    )
    ANON_MES_SC = Sammlung(
        trace="Mes Sc",
        groups="Wortschatz|Anonym|Mes Sc",
        kreis="Mes",
        ort="Sc",
    )
    ANON_MES_SD = Sammlung(
        trace="Mes Sd",
        groups="Wortschatz|Anonym|Mes Sd",
        kreis="Mes",
        ort="Sd",
    )
    ANON_MES_SH = Sammlung(
        trace="Mes Sh",
        groups="Wortschatz|Anonym|Mes Sh",
        kreis="Mes",
        ort="Sh",
    )
    ANON_MES_SM = Sammlung(
        trace="Mes Sm",
        groups="Wortschatz|Anonym|Mes Sm",
        kreis="Mes",
        ort="Sm",
    )
    ANON_MES_SR = Sammlung(
        trace="Mes Sr",
        groups="Wortschatz|Anonym|Mes Sr",
        kreis="Mes",
        ort="Sr",
    )
    ANON_MES_ST = Sammlung(
        trace="Mes St",
        groups="Wortschatz|Anonym|Mes St",
        kreis="Mes",
        ort="St",
    )
    ANON_MES_VE = Sammlung(
        trace="Mes Ve",
        groups="Wortschatz|Anonym|Mes Ve",
        kreis="Mes",
        ort="Ve",
    )
    ANON_MES_WA = Sammlung(
        trace="Mes Wa",
        groups="Wortschatz|Anonym|Mes Wa",
        kreis="Mes",
        ort="Wa",
    )
    ANON_MES_WB = Sammlung(
        trace="Mes Wb",
        groups="Wortschatz|Anonym|Mes Wb",
        kreis="Mes",
        ort="Wb",
    )
    ANON_MES_WE = Sammlung(
        trace="Mes We",
        groups="Wortschatz|Anonym|Mes We",
        kreis="Mes",
        ort="We",
    )
    ANON_MES_WF = Sammlung(
        trace="Mes Wf",
        groups="Wortschatz|Anonym|Mes Wf",
        kreis="Mes",
        ort="Wf",
    )
    ANON_MES_WH = Sammlung(
        trace="Mes Wh",
        groups="Wortschatz|Anonym|Mes Wh",
        kreis="Mes",
        ort="Wh",
    )
    ANON_MES_WO = Sammlung(
        trace="Mes Wo",
        groups="Wortschatz|Anonym|Mes Wo",
        kreis="Mes",
        ort="Wo",
    )
    ANON_MES_WP = Sammlung(
        trace="Mes Wp",
        groups="Wortschatz|Anonym|Mes Wp",
        kreis="Mes",
        ort="Wp",
    )
    ANON_MES_WS = Sammlung(
        trace="Mes Ws",
        groups="Wortschatz|Anonym|Mes Ws",
        kreis="Mes",
        ort="Ws",
    )
    ANON_MIN_BA = Sammlung(
        trace="Min Ba",
        groups="Wortschatz|Anonym|Min Ba",
        kreis="Min",
        ort="Ba",
    )
    ANON_MIN_BH = Sammlung(
        trace="Min Bh",
        groups="Wortschatz|Anonym|Min Bh",
        kreis="Min",
        ort="Bh",
    )
    ANON_MIN_BI = Sammlung(
        trace="Min Bi",
        groups="Wortschatz|Anonym|Min Bi",
        kreis="Min",
        ort="Bi",
    )
    ANON_MIN_BK = Sammlung(
        trace="Min Bk",
        groups="Wortschatz|Anonym|Min Bk",
        kreis="Min",
        ort="Bk",
    )
    ANON_MIN_BN = Sammlung(
        trace="Min Bn",
        groups="Wortschatz|Anonym|Min Bn",
        kreis="Min",
        ort="Bn",
    )
    ANON_MIN_BÖ = Sammlung(
        trace="Min Bö",
        groups="Wortschatz|Anonym|Min Bö",
        kreis="Min",
        ort="Bö",
    )
    ANON_MIN_DA = Sammlung(
        trace="Min Da",
        groups="Wortschatz|Anonym|Min Da",
        kreis="Min",
        ort="Da",
    )
    ANON_MIN_DE = Sammlung(
        trace="Min De",
        groups="Wortschatz|Anonym|Min De",
        kreis="Min",
        ort="De",
    )
    ANON_MIN_DÖ = Sammlung(
        trace="Min Dö",
        groups="Wortschatz|Anonym|Min Dö",
        kreis="Min",
        ort="Dö",
    )
    ANON_MIN_DÜ = Sammlung(
        trace="Min Dü",
        groups="Wortschatz|Anonym|Min Dü",
        kreis="Min",
        ort="Dü",
    )
    ANON_MIN_EH = Sammlung(
        trace="Min Eh",
        groups="Wortschatz|Anonym|Min Eh",
        kreis="Min",
        ort="Eh",
    )
    ANON_MIN_EI = Sammlung(
        trace="Min Ei",
        groups="Wortschatz|Anonym|Min Ei",
        kreis="Min",
        ort="Ei",
    )
    ANON_MIN_EL = Sammlung(
        trace="Min El",
        groups="Wortschatz|Anonym|Min El",
        kreis="Min",
        ort="El",
    )
    ANON_MIN_EN = Sammlung(
        trace="Min En",
        groups="Wortschatz|Anonym|Min En",
        kreis="Min",
        ort="En",
    )
    ANON_MIN_FR = Sammlung(
        trace="Min Fr",
        groups="Wortschatz|Anonym|Min Fr",
        kreis="Min",
        ort="Fr",
    )
    ANON_MIN_FW = Sammlung(
        trace="Min Fw",
        groups="Wortschatz|Anonym|Min Fw",
        kreis="Min",
        ort="Fw",
    )
    ANON_MIN_GO = Sammlung(
        trace="Min Go",
        groups="Wortschatz|Anonym|Min Go",
        kreis="Min",
        ort="Go",
    )
    ANON_MIN_GR = Sammlung(
        trace="Min Gr",
        groups="Wortschatz|Anonym|Min Gr",
        kreis="Min",
        ort="Gr",
    )
    ANON_MIN_HA = Sammlung(
        trace="Min Ha",
        groups="Wortschatz|Anonym|Min Ha",
        kreis="Min",
        ort="Ha",
    )
    ANON_MIN_HÄ = Sammlung(
        trace="Min Hä",
        groups="Wortschatz|Anonym|Min Hä",
        kreis="Min",
        ort="Hä",
    )
    ANON_MIN_HB = Sammlung(
        trace="Min Hb",
        groups="Wortschatz|Anonym|Min Hb",
        kreis="Min",
        ort="Hb",
    )
    ANON_MIN_HD = Sammlung(
        trace="Min Hd",
        groups="Wortschatz|Anonym|Min Hd",
        kreis="Min",
        ort="Hd",
    )
    ANON_MIN_HE = Sammlung(
        trace="Min He",
        groups="Wortschatz|Anonym|Min He",
        kreis="Min",
        ort="He",
    )
    ANON_MIN_HH = Sammlung(
        trace="Min Hh",
        groups="Wortschatz|Anonym|Min Hh",
        kreis="Min",
        ort="Hh",
    )
    ANON_MIN_HI = Sammlung(
        trace="Min Hi",
        groups="Wortschatz|Anonym|Min Hi",
        kreis="Min",
        ort="Hi",
    )
    ANON_MIN_HM = Sammlung(
        trace="Min Hm",
        groups="Wortschatz|Anonym|Min Hm",
        kreis="Min",
        ort="Hm",
    )
    ANON_MIN_HO = Sammlung(
        trace="Min Ho",
        groups="Wortschatz|Anonym|Min Ho",
        kreis="Min",
        ort="Ho",
    )
    ANON_MIN_HS = Sammlung(
        trace="Min Hs",
        groups="Wortschatz|Anonym|Min Hs",
        kreis="Min",
        ort="Hs",
    )
    ANON_MIN_HZ = Sammlung(
        trace="Min Hz",
        groups="Wortschatz|Anonym|Min Hz",
        kreis="Min",
        ort="Hz",
    )
    ANON_MIN_IH = Sammlung(
        trace="Min Ih",
        groups="Wortschatz|Anonym|Min Ih",
        kreis="Min",
        ort="Ih",
    )
    ANON_MIN_IL = Sammlung(
        trace="Min Il",
        groups="Wortschatz|Anonym|Min Il",
        kreis="Min",
        ort="Il",
    )
    ANON_MIN_IS = Sammlung(
        trace="Min Is",
        groups="Wortschatz|Anonym|Min Is",
        kreis="Min",
        ort="Is",
    )
    ANON_MIN_JÖ = Sammlung(
        trace="Min Jö",
        groups="Wortschatz|Anonym|Min Jö",
        kreis="Min",
        ort="Jö",
    )
    ANON_MIN_KB = Sammlung(
        trace="Min Kb",
        groups="Wortschatz|Anonym|Min Kb",
        kreis="Min",
        ort="Kb",
    )
    ANON_MIN_KH = Sammlung(
        trace="Min Kh",
        groups="Wortschatz|Anonym|Min Kh",
        kreis="Min",
        ort="Kh",
    )
    ANON_MIN_KO = Sammlung(
        trace="Min Ko",
        groups="Wortschatz|Anonym|Min Ko",
        kreis="Min",
        ort="Ko",
    )
    ANON_MIN_LA = Sammlung(
        trace="Min La",
        groups="Wortschatz|Anonym|Min La",
        kreis="Min",
        ort="La",
    )
    ANON_MIN_LB = Sammlung(
        trace="Min Lb",
        groups="Wortschatz|Anonym|Min Lb",
        kreis="Min",
        ort="Lb",
    )
    ANON_MIN_LF = Sammlung(
        trace="Min Lf",
        groups="Wortschatz|Anonym|Min Lf",
        kreis="Min",
        ort="Lf",
    )
    ANON_MIN_LO = Sammlung(
        trace="Min Lo",
        groups="Wortschatz|Anonym|Min Lo",
        kreis="Min",
        ort="Lo",
    )
    ANON_MIN_MA = Sammlung(
        trace="Min Ma",
        groups="Wortschatz|Anonym|Min Ma",
        kreis="Min",
        ort="Ma",
    )
    ANON_MIN_MB = Sammlung(
        trace="Min Mb",
        groups="Wortschatz|Anonym|Min Mb",
        kreis="Min",
        ort="Mb",
    )
    ANON_MIN_ME = Sammlung(
        trace="Min Me",
        groups="Wortschatz|Anonym|Min Me",
        kreis="Min",
        ort="Me",
    )
    ANON_MIN_MI = Sammlung(
        trace="Min Mi",
        groups="Wortschatz|Anonym|Min Mi",
        kreis="Min",
        ort="Mi",
    )
    ANON_MIN_ML = Sammlung(
        trace="Min Ml",
        groups="Wortschatz|Anonym|Min Ml",
        kreis="Min",
        ort="Ml",
    )
    ANON_MIN_MO = Sammlung(
        trace="Min Mo",
        groups="Wortschatz|Anonym|Min Mo",
        kreis="Min",
        ort="Mo",
    )
    ANON_MIN_MW = Sammlung(
        trace="Min Mw",
        groups="Wortschatz|Anonym|Min Mw",
        kreis="Min",
        ort="Mw",
    )
    ANON_MIN_NA = Sammlung(
        trace="Min Na",
        groups="Wortschatz|Anonym|Min Na",
        kreis="Min",
        ort="Na",
    )
    ANON_MIN_NB = Sammlung(
        trace="Min Nb",
        groups="Wortschatz|Anonym|Min Nb",
        kreis="Min",
        ort="Nb",
    )
    ANON_MIN_NE = Sammlung(
        trace="Min Ne",
        groups="Wortschatz|Anonym|Min Ne",
        kreis="Min",
        ort="Ne",
    )
    ANON_MIN_NH = Sammlung(
        trace="Min Nh",
        groups="Wortschatz|Anonym|Min Nh",
        kreis="Min",
        ort="Nh",
    )
    ANON_MIN_NK = Sammlung(
        trace="Min Nk",
        groups="Wortschatz|Anonym|Min Nk",
        kreis="Min",
        ort="Nk",
    )
    ANON_MIN_NS = Sammlung(
        trace="Min Ns",
        groups="Wortschatz|Anonym|Min Ns",
        kreis="Min",
        ort="Ns",
    )
    ANON_MIN_OB = Sammlung(
        trace="Min Ob",
        groups="Wortschatz|Anonym|Min Ob",
        kreis="Min",
        ort="Ob",
    )
    ANON_MIN_ÖH = Sammlung(
        trace="Min Öh",
        groups="Wortschatz|Anonym|Min Öh",
        kreis="Min",
        ort="Öh",
    )
    ANON_MIN_OL = Sammlung(
        trace="Min Ol",
        groups="Wortschatz|Anonym|Min Ol",
        kreis="Min",
        ort="Ol",
    )
    ANON_MIN_OS = Sammlung(
        trace="Min Os",
        groups="Wortschatz|Anonym|Min Os",
        kreis="Min",
        ort="Os",
    )
    ANON_MIN_PÄ = Sammlung(
        trace="Min Pä",
        groups="Wortschatz|Anonym|Min Pä",
        kreis="Min",
        ort="Pä",
    )
    ANON_MIN_PH = Sammlung(
        trace="Min Ph",
        groups="Wortschatz|Anonym|Min Ph",
        kreis="Min",
        ort="Ph",
    )
    ANON_MIN_QU = Sammlung(
        trace="Min Qu",
        groups="Wortschatz|Anonym|Min Qu",
        kreis="Min",
        ort="Qu",
    )
    ANON_MIN_RD = Sammlung(
        trace="Min Rd",
        groups="Wortschatz|Anonym|Min Rd",
        kreis="Min",
        ort="Rd",
    )
    ANON_MIN_RE = Sammlung(
        trace="Min Re",
        groups="Wortschatz|Anonym|Min Re",
        kreis="Min",
        ort="Re",
    )
    ANON_MIN_RH = Sammlung(
        trace="Min Rh",
        groups="Wortschatz|Anonym|Min Rh",
        kreis="Min",
        ort="Rh",
    )
    ANON_MIN_RO = Sammlung(
        trace="Min Ro",
        groups="Wortschatz|Anonym|Min Ro",
        kreis="Min",
        ort="Ro",
    )
    ANON_MIN_SB = Sammlung(
        trace="Min Sb",
        groups="Wortschatz|Anonym|Min Sb",
        kreis="Min",
        ort="Sb",
    )
    ANON_MIN_SF = Sammlung(
        trace="Min Sf",
        groups="Wortschatz|Anonym|Min Sf",
        kreis="Min",
        ort="Sf",
    )
    ANON_MIN_SH = Sammlung(
        trace="Min Sh",
        groups="Wortschatz|Anonym|Min Sh",
        kreis="Min",
        ort="Sh",
    )
    ANON_MIN_ST = Sammlung(
        trace="Min St",
        groups="Wortschatz|Anonym|Min St",
        kreis="Min",
        ort="St",
    )
    ANON_MIN_TO = Sammlung(
        trace="Min To",
        groups="Wortschatz|Anonym|Min To",
        kreis="Min",
        ort="To",
    )
    ANON_MIN_UF = Sammlung(
        trace="Min Uf",
        groups="Wortschatz|Anonym|Min Uf",
        kreis="Min",
        ort="Uf",
    )
    ANON_MIN_UL = Sammlung(
        trace="Min Ul",
        groups="Wortschatz|Anonym|Min Ul",
        kreis="Min",
        ort="Ul",
    )
    ANON_MIN_VE = Sammlung(
        trace="Min Ve",
        groups="Wortschatz|Anonym|Min Ve",
        kreis="Min",
        ort="Ve",
    )
    ANON_MIN_VH = Sammlung(
        trace="Min Vh",
        groups="Wortschatz|Anonym|Min Vh",
        kreis="Min",
        ort="Vh",
    )
    ANON_MIN_VO = Sammlung(
        trace="Min Vo",
        groups="Wortschatz|Anonym|Min Vo",
        kreis="Min",
        ort="Vo",
    )
    ANON_MIN_WE = Sammlung(
        trace="Min We",
        groups="Wortschatz|Anonym|Min We",
        kreis="Min",
        ort="We",
    )
    ANON_MIN_WG = Sammlung(
        trace="Min Wg",
        groups="Wortschatz|Anonym|Min Wg",
        kreis="Min",
        ort="Wg",
    )
    ANON_MIN_WH = Sammlung(
        trace="Min Wh",
        groups="Wortschatz|Anonym|Min Wh",
        kreis="Min",
        ort="Wh",
    )
    ANON_MIN_WK = Sammlung(
        trace="Min Wk",
        groups="Wortschatz|Anonym|Min Wk",
        kreis="Min",
        ort="Wk",
    )
    ANON_MIN_WL = Sammlung(
        trace="Min Wl",
        groups="Wortschatz|Anonym|Min Wl",
        kreis="Min",
        ort="Wl",
    )
    ANON_MIN_WÖ = Sammlung(
        trace="Min Wö",
        groups="Wortschatz|Anonym|Min Wö",
        kreis="Min",
        ort="Wö",
    )
    ANON_MIN_WT = Sammlung(
        trace="Min Wt",
        groups="Wortschatz|Anonym|Min Wt",
        kreis="Min",
        ort="Wt",
    )
    ANON_MIN_WU = Sammlung(
        trace="Min Wu",
        groups="Wortschatz|Anonym|Min Wu",
        kreis="Min",
        ort="Wu",
    )
    ANON_MÜN_AB = Sammlung(
        trace="Mün Ab",
        groups="Wortschatz|Anonym|Mün Ab",
        kreis="Mün",
        ort="Ab",
    )
    ANON_MÜN_AD = Sammlung(
        trace="Mün Ad",
        groups="Wortschatz|Anonym|Mün Ad",
        kreis="Mün",
        ort="Ad",
    )
    ANON_MÜN_AK = Sammlung(
        trace="Mün Ak",
        groups="Wortschatz|Anonym|Mün Ak",
        kreis="Mün",
        ort="Ak",
    )
    ANON_MÜN_AL = Sammlung(
        trace="Mün Al",
        groups="Wortschatz|Anonym|Mün Al",
        kreis="Mün",
        ort="Al",
    )
    ANON_MÜN_AM = Sammlung(
        trace="Mün Am",
        groups="Wortschatz|Anonym|Mün Am",
        kreis="Mün",
        ort="Am",
    )
    ANON_MÜN_AN = Sammlung(
        trace="Mün An",
        groups="Wortschatz|Anonym|Mün An",
        kreis="Mün",
        ort="An",
    )
    ANON_MÜN_AP = Sammlung(
        trace="Mün Ap",
        groups="Wortschatz|Anonym|Mün Ap",
        kreis="Mün",
        ort="Ap",
    )
    ANON_MÜN_BB = Sammlung(
        trace="Mün Bb",
        groups="Wortschatz|Anonym|Mün Bb",
        kreis="Mün",
        ort="Bb",
    )
    ANON_MÜN_BO = Sammlung(
        trace="Mün Bo",
        groups="Wortschatz|Anonym|Mün Bo",
        kreis="Mün",
        ort="Bo",
    )
    ANON_MÜN_BR = Sammlung(
        trace="Mün Br",
        groups="Wortschatz|Anonym|Mün Br",
        kreis="Mün",
        ort="Br",
    )
    ANON_MÜN_BS = Sammlung(
        trace="Mün Bs",
        groups="Wortschatz|Anonym|Mün Bs",
        kreis="Mün",
        ort="Bs",
    )
    ANON_MÜN_DB = Sammlung(
        trace="Mün Db",
        groups="Wortschatz|Anonym|Mün Db",
        kreis="Mün",
        ort="Db",
    )
    ANON_MÜN_GB = Sammlung(
        trace="Mün Gb",
        groups="Wortschatz|Anonym|Mün Gb",
        kreis="Mün",
        ort="Gb",
    )
    ANON_MÜN_GE = Sammlung(
        trace="Mün Ge",
        groups="Wortschatz|Anonym|Mün Ge",
        kreis="Mün",
        ort="Ge",
    )
    ANON_MÜN_GI = Sammlung(
        trace="Mün Gi",
        groups="Wortschatz|Anonym|Mün Gi",
        kreis="Mün",
        ort="Gi",
    )
    ANON_MÜN_GR = Sammlung(
        trace="Mün Gr",
        groups="Wortschatz|Anonym|Mün Gr",
        kreis="Mün",
        ort="Gr",
    )
    ANON_MÜN_GS = Sammlung(
        trace="Mün Gs",
        groups="Wortschatz|Anonym|Mün Gs",
        kreis="Mün",
        ort="Gs",
    )
    ANON_MÜN_GU = Sammlung(
        trace="Mün Gu",
        groups="Wortschatz|Anonym|Mün Gu",
        kreis="Mün",
        ort="Gu",
    )
    ANON_MÜN_HA = Sammlung(
        trace="Mün Ha",
        groups="Wortschatz|Anonym|Mün Ha",
        kreis="Mün",
        ort="Ha",
    )
    ANON_MÜN_HB = Sammlung(
        trace="Mün Hb",
        groups="Wortschatz|Anonym|Mün Hb",
        kreis="Mün",
        ort="Hb",
    )
    ANON_MÜN_HD = Sammlung(
        trace="Mün Hd",
        groups="Wortschatz|Anonym|Mün Hd",
        kreis="Mün",
        ort="Hd",
    )
    ANON_MÜN_HI = Sammlung(
        trace="Mün Hi",
        groups="Wortschatz|Anonym|Mün Hi",
        kreis="Mün",
        ort="Hi",
    )
    ANON_MÜN_HO = Sammlung(
        trace="Mün Ho",
        groups="Wortschatz|Anonym|Mün Ho",
        kreis="Mün",
        ort="Ho",
    )
    ANON_MÜN_HP = Sammlung(
        trace="Mün Hp",
        groups="Wortschatz|Anonym|Mün Hp",
        kreis="Mün",
        ort="Hp",
    )
    ANON_MÜN_KH = Sammlung(
        trace="Mün Kh",
        groups="Wortschatz|Anonym|Mün Kh",
        kreis="Mün",
        ort="Kh",
    )
    ANON_MÜN_KÖ = Sammlung(
        trace="Mün Kö",
        groups="Wortschatz|Anonym|Mün Kö",
        kreis="Mün",
        ort="Kö",
    )
    ANON_MÜN_KW = Sammlung(
        trace="Mün Kw",
        groups="Wortschatz|Anonym|Mün Kw",
        kreis="Mün",
        ort="Kw",
    )
    ANON_MÜN_MB = Sammlung(
        trace="Mün Mb",
        groups="Wortschatz|Anonym|Mün Mb",
        kreis="Mün",
        ort="Mb",
    )
    ANON_MÜN_MS = Sammlung(
        trace="Mün Ms",
        groups="Wortschatz|Anonym|Mün Ms",
        kreis="Mün",
        ort="Ms",
    )
    ANON_MÜN_MÜ = Sammlung(
        trace="Mün Mü",
        groups="Wortschatz|Anonym|Mün Mü",
        kreis="Mün",
        ort="Mü",
    )
    ANON_MÜN_MZ = Sammlung(
        trace="Mün Mz",
        groups="Wortschatz|Anonym|Mün Mz",
        kreis="Mün",
        ort="Mz",
    )
    ANON_MÜN_NB = Sammlung(
        trace="Mün Nb",
        groups="Wortschatz|Anonym|Mün Nb",
        kreis="Mün",
        ort="Nb",
    )
    ANON_MÜN_NO = Sammlung(
        trace="Mün No",
        groups="Wortschatz|Anonym|Mün No",
        kreis="Mün",
        ort="No",
    )
    ANON_MÜN_RO = Sammlung(
        trace="Mün Ro",
        groups="Wortschatz|Anonym|Mün Ro",
        kreis="Mün",
        ort="Ro",
    )
    ANON_MÜN_RR = Sammlung(
        trace="Mün Rr",
        groups="Wortschatz|Anonym|Mün Rr",
        kreis="Mün",
        ort="Rr",
    )
    ANON_MÜN_SB = Sammlung(
        trace="Mün Sb",
        groups="Wortschatz|Anonym|Mün Sb",
        kreis="Mün",
        ort="Sb",
    )
    ANON_MÜN_SD = Sammlung(
        trace="Mün Sd",
        groups="Wortschatz|Anonym|Mün Sd",
        kreis="Mün",
        ort="Sd",
    )
    ANON_MÜN_SH = Sammlung(
        trace="Mün Sh",
        groups="Wortschatz|Anonym|Mün Sh",
        kreis="Mün",
        ort="Sh",
    )
    ANON_MÜN_SP = Sammlung(
        trace="Mün Sp",
        groups="Wortschatz|Anonym|Mün Sp",
        kreis="Mün",
        ort="Sp",
    )
    ANON_MÜN_TE = Sammlung(
        trace="Mün Te",
        groups="Wortschatz|Anonym|Mün Te",
        kreis="Mün",
        ort="Te",
    )
    ANON_MÜN_WB = Sammlung(
        trace="Mün Wb",
        groups="Wortschatz|Anonym|Mün Wb",
        kreis="Mün",
        ort="Wb",
    )
    ANON_MÜN_WL = Sammlung(
        trace="Mün Wl",
        groups="Wortschatz|Anonym|Mün Wl",
        kreis="Mün",
        ort="Wl",
    )
    ANON_MÜN_WO = Sammlung(
        trace="Mün Wo",
        groups="Wortschatz|Anonym|Mün Wo",
        kreis="Mün",
        ort="Wo",
    )
    ANON_NIE_AM = Sammlung(
        trace="Nie Am",
        groups="Wortschatz|Anonym|Nie Am",
        kreis="Nie",
        ort="Am",
    )
    ANON_NIE_BH = Sammlung(
        trace="Nie Bh",
        groups="Wortschatz|Anonym|Nie Bh",
        kreis="Nie",
        ort="Bh",
    )
    ANON_NIE_BO = Sammlung(
        trace="Nie Bo",
        groups="Wortschatz|Anonym|Nie Bo",
        kreis="Nie",
        ort="Bo",
    )
    ANON_NIE_BR = Sammlung(
        trace="Nie Br",
        groups="Wortschatz|Anonym|Nie Br",
        kreis="Nie",
        ort="Br",
    )
    ANON_NIE_DH = Sammlung(
        trace="Nie Dh",
        groups="Wortschatz|Anonym|Nie Dh",
        kreis="Nie",
        ort="Dh",
    )
    ANON_NIE_DI = Sammlung(
        trace="Nie Di",
        groups="Wortschatz|Anonym|Nie Di",
        kreis="Nie",
        ort="Di",
    )
    ANON_NIE_DL = Sammlung(
        trace="Nie Dl",
        groups="Wortschatz|Anonym|Nie Dl",
        kreis="Nie",
        ort="Dl",
    )
    ANON_NIE_DT = Sammlung(
        trace="Nie Dt",
        groups="Wortschatz|Anonym|Nie Dt",
        kreis="Nie",
        ort="Dt",
    )
    ANON_NIE_ES = Sammlung(
        trace="Nie Es",
        groups="Wortschatz|Anonym|Nie Es",
        kreis="Nie",
        ort="Es",
    )
    ANON_NIE_GV = Sammlung(
        trace="Nie Gv",
        groups="Wortschatz|Anonym|Nie Gv",
        kreis="Nie",
        ort="Gv",
    )
    ANON_NIE_HH = Sammlung(
        trace="Nie Hh",
        groups="Wortschatz|Anonym|Nie Hh",
        kreis="Nie",
        ort="Hh",
    )
    ANON_NIE_HI = Sammlung(
        trace="Nie Hi",
        groups="Wortschatz|Anonym|Nie Hi",
        kreis="Nie",
        ort="Hi",
    )
    ANON_NIE_HO = Sammlung(
        trace="Nie Ho",
        groups="Wortschatz|Anonym|Nie Ho",
        kreis="Nie",
        ort="Ho",
    )
    ANON_NIE_HÖ = Sammlung(
        trace="Nie Hö",
        groups="Wortschatz|Anonym|Nie Hö",
        kreis="Nie",
        ort="Hö",
    )
    ANON_NIE_HS = Sammlung(
        trace="Nie Hs",
        groups="Wortschatz|Anonym|Nie Hs",
        kreis="Nie",
        ort="Hs",
    )
    ANON_NIE_HT = Sammlung(
        trace="Nie Ht",
        groups="Wortschatz|Anonym|Nie Ht",
        kreis="Nie",
        ort="Ht",
    )
    ANON_NIE_HU = Sammlung(
        trace="Nie Hu",
        groups="Wortschatz|Anonym|Nie Hu",
        kreis="Nie",
        ort="Hu",
    )
    ANON_NIE_JH = Sammlung(
        trace="Nie Jh",
        groups="Wortschatz|Anonym|Nie Jh",
        kreis="Nie",
        ort="Jh",
    )
    ANON_NIE_LA = Sammlung(
        trace="Nie La",
        groups="Wortschatz|Anonym|Nie La",
        kreis="Nie",
        ort="La",
    )
    ANON_NIE_LH = Sammlung(
        trace="Nie Lh",
        groups="Wortschatz|Anonym|Nie Lh",
        kreis="Nie",
        ort="Lh",
    )
    ANON_NIE_LO = Sammlung(
        trace="Nie Lo",
        groups="Wortschatz|Anonym|Nie Lo",
        kreis="Nie",
        ort="Lo",
    )
    ANON_NIE_MH = Sammlung(
        trace="Nie Mh",
        groups="Wortschatz|Anonym|Nie Mh",
        kreis="Nie",
        ort="Mh",
    )
    ANON_NIE_MÜ = Sammlung(
        trace="Nie Mü",
        groups="Wortschatz|Anonym|Nie Mü",
        kreis="Nie",
        ort="Mü",
    )
    ANON_NIE_ND = Sammlung(
        trace="Nie Nd",
        groups="Wortschatz|Anonym|Nie Nd",
        kreis="Nie",
        ort="Nd",
    )
    ANON_NIE_NO = Sammlung(
        trace="Nie No",
        groups="Wortschatz|Anonym|Nie No",
        kreis="Nie",
        ort="No",
    )
    ANON_NIE_SA = Sammlung(
        trace="Nie Sa",
        groups="Wortschatz|Anonym|Nie Sa",
        kreis="Nie",
        ort="Sa",
    )
    ANON_NIE_SH = Sammlung(
        trace="Nie Sh",
        groups="Wortschatz|Anonym|Nie Sh",
        kreis="Nie",
        ort="Sh",
    )
    ANON_NIE_ST = Sammlung(
        trace="Nie St",
        groups="Wortschatz|Anonym|Nie St",
        kreis="Nie",
        ort="St",
    )
    ANON_NIE_UC = Sammlung(
        trace="Nie Uc",
        groups="Wortschatz|Anonym|Nie Uc",
        kreis="Nie",
        ort="Uc",
    )
    ANON_NIE_WA = Sammlung(
        trace="Nie Wa",
        groups="Wortschatz|Anonym|Nie Wa",
        kreis="Nie",
        ort="Wa",
    )
    ANON_NIE_WF = Sammlung(
        trace="Nie Wf",
        groups="Wortschatz|Anonym|Nie Wf",
        kreis="Nie",
        ort="Wf",
    )
    ANON_NIE_WH = Sammlung(
        trace="Nie Wh",
        groups="Wortschatz|Anonym|Nie Wh",
        kreis="Nie",
        ort="Wh",
    )
    ANON_NIE_WI = Sammlung(
        trace="Nie Wi",
        groups="Wortschatz|Anonym|Nie Wi",
        kreis="Nie",
        ort="Wi",
    )
    ANON_OLP_AB = Sammlung(
        trace="Olp Ab",
        groups="Wortschatz|Anonym|Olp Ab",
        kreis="Olp",
        ort="Ab",
    )
    ANON_OLP_AH = Sammlung(
        trace="Olp Ah",
        groups="Wortschatz|Anonym|Olp Ah",
        kreis="Olp",
        ort="Ah",
    )
    ANON_OLP_AK = Sammlung(
        trace="Olp Ak",
        groups="Wortschatz|Anonym|Olp Ak",
        kreis="Olp",
        ort="Ak",
    )
    ANON_OLP_AT = Sammlung(
        trace="Olp At",
        groups="Wortschatz|Anonym|Olp At",
        kreis="Olp",
        ort="At",
    )
    ANON_OLP_BB = Sammlung(
        trace="Olp Bb",
        groups="Wortschatz|Anonym|Olp Bb",
        kreis="Olp",
        ort="Bb",
    )
    ANON_OLP_BE = Sammlung(
        trace="Olp Be",
        groups="Wortschatz|Anonym|Olp Be",
        kreis="Olp",
        ort="Be",
    )
    ANON_OLP_BH = Sammlung(
        trace="Olp Bh",
        groups="Wortschatz|Anonym|Olp Bh",
        kreis="Olp",
        ort="Bh",
    )
    ANON_OLP_BL = Sammlung(
        trace="Olp Bl",
        groups="Wortschatz|Anonym|Olp Bl",
        kreis="Olp",
        ort="Bl",
    )
    ANON_OLP_BS = Sammlung(
        trace="Olp Bs",
        groups="Wortschatz|Anonym|Olp Bs",
        kreis="Olp",
        ort="Bs",
    )
    ANON_OLP_BÜ = Sammlung(
        trace="Olp Bü",
        groups="Wortschatz|Anonym|Olp Bü",
        kreis="Olp",
        ort="Bü",
    )
    ANON_OLP_DA = Sammlung(
        trace="Olp Da",
        groups="Wortschatz|Anonym|Olp Da",
        kreis="Olp",
        ort="Da",
    )
    ANON_OLP_DH = Sammlung(
        trace="Olp Dh",
        groups="Wortschatz|Anonym|Olp Dh",
        kreis="Olp",
        ort="Dh",
    )
    ANON_OLP_DÜ = Sammlung(
        trace="Olp Dü",
        groups="Wortschatz|Anonym|Olp Dü",
        kreis="Olp",
        ort="Dü",
    )
    ANON_OLP_EB = Sammlung(
        trace="Olp Eb",
        groups="Wortschatz|Anonym|Olp Eb",
        kreis="Olp",
        ort="Eb",
    )
    ANON_OLP_EH = Sammlung(
        trace="Olp Eh",
        groups="Wortschatz|Anonym|Olp Eh",
        kreis="Olp",
        ort="Eh",
    )
    ANON_OLP_EL = Sammlung(
        trace="Olp El",
        groups="Wortschatz|Anonym|Olp El",
        kreis="Olp",
        ort="El",
    )
    ANON_OLP_EN = Sammlung(
        trace="Olp En",
        groups="Wortschatz|Anonym|Olp En",
        kreis="Olp",
        ort="En",
    )
    ANON_OLP_FÖ = Sammlung(
        trace="Olp Fö",
        groups="Wortschatz|Anonym|Olp Fö",
        kreis="Olp",
        ort="Fö",
    )
    ANON_OLP_GB = Sammlung(
        trace="Olp Gb",
        groups="Wortschatz|Anonym|Olp Gb",
        kreis="Olp",
        ort="Gb",
    )
    ANON_OLP_GE = Sammlung(
        trace="Olp Ge",
        groups="Wortschatz|Anonym|Olp Ge",
        kreis="Olp",
        ort="Ge",
    )
    ANON_OLP_GI = Sammlung(
        trace="Olp Gi",
        groups="Wortschatz|Anonym|Olp Gi",
        kreis="Olp",
        ort="Gi",
    )
    ANON_OLP_HA = Sammlung(
        trace="Olp Ha",
        groups="Wortschatz|Anonym|Olp Ha",
        kreis="Olp",
        ort="Ha",
    )
    ANON_OLP_HB = Sammlung(
        trace="Olp Hb",
        groups="Wortschatz|Anonym|Olp Hb",
        kreis="Olp",
        ort="Hb",
    )
    ANON_OLP_HE = Sammlung(
        trace="Olp He",
        groups="Wortschatz|Anonym|Olp He",
        kreis="Olp",
        ort="He",
    )
    ANON_OLP_HG = Sammlung(
        trace="Olp Hg",
        groups="Wortschatz|Anonym|Olp Hg",
        kreis="Olp",
        ort="Hg",
    )
    ANON_OLP_HI = Sammlung(
        trace="Olp Hi",
        groups="Wortschatz|Anonym|Olp Hi",
        kreis="Olp",
        ort="Hi",
    )
    ANON_OLP_HO = Sammlung(
        trace="Olp Ho",
        groups="Wortschatz|Anonym|Olp Ho",
        kreis="Olp",
        ort="Ho",
    )
    ANON_OLP_HP = Sammlung(
        trace="Olp Hp",
        groups="Wortschatz|Anonym|Olp Hp",
        kreis="Olp",
        ort="Hp",
    )
    ANON_OLP_HS = Sammlung(
        trace="Olp Hs",
        groups="Wortschatz|Anonym|Olp Hs",
        kreis="Olp",
        ort="Hs",
    )
    ANON_OLP_HÜ = Sammlung(
        trace="Olp Hü",
        groups="Wortschatz|Anonym|Olp Hü",
        kreis="Olp",
        ort="Hü",
    )
    ANON_OLP_KH = Sammlung(
        trace="Olp Kh",
        groups="Wortschatz|Anonym|Olp Kh",
        kreis="Olp",
        ort="Kh",
    )
    ANON_OLP_KV = Sammlung(
        trace="Olp Kv",
        groups="Wortschatz|Anonym|Olp Kv",
        kreis="Olp",
        ort="Kv",
    )
    ANON_OLP_LA = Sammlung(
        trace="Olp La",
        groups="Wortschatz|Anonym|Olp La",
        kreis="Olp",
        ort="La",
    )
    ANON_OLP_LE = Sammlung(
        trace="Olp Le",
        groups="Wortschatz|Anonym|Olp Le",
        kreis="Olp",
        ort="Le",
    )
    ANON_OLP_LI = Sammlung(
        trace="Olp Li",
        groups="Wortschatz|Anonym|Olp Li",
        kreis="Olp",
        ort="Li",
    )
    ANON_OLP_LS = Sammlung(
        trace="Olp Ls",
        groups="Wortschatz|Anonym|Olp Ls",
        kreis="Olp",
        ort="Ls",
    )
    ANON_OLP_LÜ = Sammlung(
        trace="Olp Lü",
        groups="Wortschatz|Anonym|Olp Lü",
        kreis="Olp",
        ort="Lü",
    )
    ANON_OLP_MA = Sammlung(
        trace="Olp Ma",
        groups="Wortschatz|Anonym|Olp Ma",
        kreis="Olp",
        ort="Ma",
    )
    ANON_OLP_MB = Sammlung(
        trace="Olp Mb",
        groups="Wortschatz|Anonym|Olp Mb",
        kreis="Olp",
        ort="Mb",
    )
    ANON_OLP_ME = Sammlung(
        trace="Olp Me",
        groups="Wortschatz|Anonym|Olp Me",
        kreis="Olp",
        ort="Me",
    )
    ANON_OLP_MH = Sammlung(
        trace="Olp Mh",
        groups="Wortschatz|Anonym|Olp Mh",
        kreis="Olp",
        ort="Mh",
    )
    ANON_OLP_MK = Sammlung(
        trace="Olp Mk",
        groups="Wortschatz|Anonym|Olp Mk",
        kreis="Olp",
        ort="Mk",
    )
    ANON_OLP_NE = Sammlung(
        trace="Olp Ne",
        groups="Wortschatz|Anonym|Olp Ne",
        kreis="Olp",
        ort="Ne",
    )
    ANON_OLP_NH = Sammlung(
        trace="Olp Nh",
        groups="Wortschatz|Anonym|Olp Nh",
        kreis="Olp",
        ort="Nh",
    )
    ANON_OLP_NK = Sammlung(
        trace="Olp Nk",
        groups="Wortschatz|Anonym|Olp Nk",
        kreis="Olp",
        ort="Nk",
    )
    ANON_OLP_OE = Sammlung(
        trace="Olp Oe",
        groups="Wortschatz|Anonym|Olp Oe",
        kreis="Olp",
        ort="Oe",
    )
    ANON_OLP_OF = Sammlung(
        trace="Olp Of",
        groups="Wortschatz|Anonym|Olp Of",
        kreis="Olp",
        ort="Of",
    )
    ANON_OLP_OH = Sammlung(
        trace="Olp Oh",
        groups="Wortschatz|Anonym|Olp Oh",
        kreis="Olp",
        ort="Oh",
    )
    ANON_OLP_OL = Sammlung(
        trace="Olp Ol",
        groups="Wortschatz|Anonym|Olp Ol",
        kreis="Olp",
        ort="Ol",
    )
    ANON_OLP_OM = Sammlung(
        trace="Olp Om",
        groups="Wortschatz|Anonym|Olp Om",
        kreis="Olp",
        ort="Om",
    )
    ANON_OLP_OV = Sammlung(
        trace="Olp Ov",
        groups="Wortschatz|Anonym|Olp Ov",
        kreis="Olp",
        ort="Ov",
    )
    ANON_OLP_RB = Sammlung(
        trace="Olp Rb",
        groups="Wortschatz|Anonym|Olp Rb",
        kreis="Olp",
        ort="Rb",
    )
    ANON_OLP_RE = Sammlung(
        trace="Olp Re",
        groups="Wortschatz|Anonym|Olp Re",
        kreis="Olp",
        ort="Re",
    )
    ANON_OLP_RH = Sammlung(
        trace="Olp Rh",
        groups="Wortschatz|Anonym|Olp Rh",
        kreis="Olp",
        ort="Rh",
    )
    ANON_OLP_RI = Sammlung(
        trace="Olp Ri",
        groups="Wortschatz|Anonym|Olp Ri",
        kreis="Olp",
        ort="Ri",
    )
    ANON_OLP_RL = Sammlung(
        trace="Olp Rl",
        groups="Wortschatz|Anonym|Olp Rl",
        kreis="Olp",
        ort="Rl",
    )
    ANON_OLP_RO = Sammlung(
        trace="Olp Ro",
        groups="Wortschatz|Anonym|Olp Ro",
        kreis="Olp",
        ort="Ro",
    )
    ANON_OLP_RÖ = Sammlung(
        trace="Olp Rö",
        groups="Wortschatz|Anonym|Olp Rö",
        kreis="Olp",
        ort="Rö",
    )
    ANON_OLP_RP = Sammlung(
        trace="Olp Rp",
        groups="Wortschatz|Anonym|Olp Rp",
        kreis="Olp",
        ort="Rp",
    )
    ANON_OLP_RÜ = Sammlung(
        trace="Olp Rü",
        groups="Wortschatz|Anonym|Olp Rü",
        kreis="Olp",
        ort="Rü",
    )
    ANON_OLP_SB = Sammlung(
        trace="Olp Sb",
        groups="Wortschatz|Anonym|Olp Sb",
        kreis="Olp",
        ort="Sb",
    )
    ANON_OLP_SC = Sammlung(
        trace="Olp Sc",
        groups="Wortschatz|Anonym|Olp Sc",
        kreis="Olp",
        ort="Sc",
    )
    ANON_OLP_SH = Sammlung(
        trace="Olp Sh",
        groups="Wortschatz|Anonym|Olp Sh",
        kreis="Olp",
        ort="Sh",
    )
    ANON_OLP_SM = Sammlung(
        trace="Olp Sm",
        groups="Wortschatz|Anonym|Olp Sm",
        kreis="Olp",
        ort="Sm",
    )
    ANON_OLP_SP = Sammlung(
        trace="Olp Sp",
        groups="Wortschatz|Anonym|Olp Sp",
        kreis="Olp",
        ort="Sp",
    )
    ANON_OLP_SR = Sammlung(
        trace="Olp Sr",
        groups="Wortschatz|Anonym|Olp Sr",
        kreis="Olp",
        ort="Sr",
    )
    ANON_OLP_TE = Sammlung(
        trace="Olp Te",
        groups="Wortschatz|Anonym|Olp Te",
        kreis="Olp",
        ort="Te",
    )
    ANON_OLP_TH = Sammlung(
        trace="Olp Th",
        groups="Wortschatz|Anonym|Olp Th",
        kreis="Olp",
        ort="Th",
    )
    ANON_OLP_TI = Sammlung(
        trace="Olp Ti",
        groups="Wortschatz|Anonym|Olp Ti",
        kreis="Olp",
        ort="Ti",
    )
    ANON_OLP_VA = Sammlung(
        trace="Olp Va",
        groups="Wortschatz|Anonym|Olp Va",
        kreis="Olp",
        ort="Va",
    )
    ANON_OLP_WE = Sammlung(
        trace="Olp We",
        groups="Wortschatz|Anonym|Olp We",
        kreis="Olp",
        ort="We",
    )
    ANON_OLP_WI = Sammlung(
        trace="Olp Wi",
        groups="Wortschatz|Anonym|Olp Wi",
        kreis="Olp",
        ort="Wi",
    )
    ANON_OLP_WN = Sammlung(
        trace="Olp Wn",
        groups="Wortschatz|Anonym|Olp Wn",
        kreis="Olp",
        ort="Wn",
    )
    ANON_OSN_AD = Sammlung(
        trace="Osn Ad",
        groups="Wortschatz|Anonym|Osn Ad",
        kreis="Osn",
        ort="Ad",
    )
    ANON_OSN_AF = Sammlung(
        trace="Osn Af",
        groups="Wortschatz|Anonym|Osn Af",
        kreis="Osn",
        ort="Af",
    )
    ANON_OSN_AL = Sammlung(
        trace="Osn Al",
        groups="Wortschatz|Anonym|Osn Al",
        kreis="Osn",
        ort="Al",
    )
    ANON_OSN_AS = Sammlung(
        trace="Osn As",
        groups="Wortschatz|Anonym|Osn As",
        kreis="Osn",
        ort="As",
    )
    ANON_OSN_AT = Sammlung(
        trace="Osn At",
        groups="Wortschatz|Anonym|Osn At",
        kreis="Osn",
        ort="At",
    )
    ANON_OSN_BD = Sammlung(
        trace="Osn Bd",
        groups="Wortschatz|Anonym|Osn Bd",
        kreis="Osn",
        ort="Bd",
    )
    ANON_OSN_BE = Sammlung(
        trace="Osn Be",
        groups="Wortschatz|Anonym|Osn Be",
        kreis="Osn",
        ort="Be",
    )
    ANON_OSN_BO = Sammlung(
        trace="Osn Bo",
        groups="Wortschatz|Anonym|Osn Bo",
        kreis="Osn",
        ort="Bo",
    )
    ANON_OSN_ED = Sammlung(
        trace="Osn Ed",
        groups="Wortschatz|Anonym|Osn Ed",
        kreis="Osn",
        ort="Ed",
    )
    ANON_OSN_ER = Sammlung(
        trace="Osn Er",
        groups="Wortschatz|Anonym|Osn Er",
        kreis="Osn",
        ort="Er",
    )
    ANON_OSN_GA = Sammlung(
        trace="Osn Ga",
        groups="Wortschatz|Anonym|Osn Ga",
        kreis="Osn",
        ort="Ga",
    )
    ANON_OSN_GB = Sammlung(
        trace="Osn Gb",
        groups="Wortschatz|Anonym|Osn Gb",
        kreis="Osn",
        ort="Gb",
    )
    ANON_OSN_GH = Sammlung(
        trace="Osn Gh",
        groups="Wortschatz|Anonym|Osn Gh",
        kreis="Osn",
        ort="Gh",
    )
    ANON_OSN_GL = Sammlung(
        trace="Osn Gl",
        groups="Wortschatz|Anonym|Osn Gl",
        kreis="Osn",
        ort="Gl",
    )
    ANON_OSN_GN = Sammlung(
        trace="Osn Gn",
        groups="Wortschatz|Anonym|Osn Gn",
        kreis="Osn",
        ort="Gn",
    )
    ANON_OSN_GR = Sammlung(
        trace="Osn Gr",
        groups="Wortschatz|Anonym|Osn Gr",
        kreis="Osn",
        ort="Gr",
    )
    ANON_OSN_HA = Sammlung(
        trace="Osn Ha",
        groups="Wortschatz|Anonym|Osn Ha",
        kreis="Osn",
        ort="Ha",
    )
    ANON_OSN_HB = Sammlung(
        trace="Osn Hb",
        groups="Wortschatz|Anonym|Osn Hb",
        kreis="Osn",
        ort="Hb",
    )
    ANON_OSN_HD = Sammlung(
        trace="Osn Hd",
        groups="Wortschatz|Anonym|Osn Hd",
        kreis="Osn",
        ort="Hd",
    )
    ANON_OSN_HE = Sammlung(
        trace="Osn He",
        groups="Wortschatz|Anonym|Osn He",
        kreis="Osn",
        ort="He",
    )
    ANON_OSN_HG = Sammlung(
        trace="Osn Hg",
        groups="Wortschatz|Anonym|Osn Hg",
        kreis="Osn",
        ort="Hg",
    )
    ANON_OSN_HI = Sammlung(
        trace="Osn Hi",
        groups="Wortschatz|Anonym|Osn Hi",
        kreis="Osn",
        ort="Hi",
    )
    ANON_OSN_HL = Sammlung(
        trace="Osn Hl",
        groups="Wortschatz|Anonym|Osn Hl",
        kreis="Osn",
        ort="Hl",
    )
    ANON_OSN_HR = Sammlung(
        trace="Osn Hr",
        groups="Wortschatz|Anonym|Osn Hr",
        kreis="Osn",
        ort="Hr",
    )
    ANON_OSN_HS = Sammlung(
        trace="Osn Hs",
        groups="Wortschatz|Anonym|Osn Hs",
        kreis="Osn",
        ort="Hs",
    )
    ANON_OSN_HT = Sammlung(
        trace="Osn Ht",
        groups="Wortschatz|Anonym|Osn Ht",
        kreis="Osn",
        ort="Ht",
    )
    ANON_OSN_IB = Sammlung(
        trace="Osn Ib",
        groups="Wortschatz|Anonym|Osn Ib",
        kreis="Osn",
        ort="Ib",
    )
    ANON_OSN_IK = Sammlung(
        trace="Osn Ik",
        groups="Wortschatz|Anonym|Osn Ik",
        kreis="Osn",
        ort="Ik",
    )
    ANON_OSN_JE = Sammlung(
        trace="Osn Je",
        groups="Wortschatz|Anonym|Osn Je",
        kreis="Osn",
        ort="Je",
    )
    ANON_OSN_KK = Sammlung(
        trace="Osn Kk",
        groups="Wortschatz|Anonym|Osn Kk",
        kreis="Osn",
        ort="Kk",
    )
    ANON_OSN_KL = Sammlung(
        trace="Osn Kl",
        groups="Wortschatz|Anonym|Osn Kl",
        kreis="Osn",
        ort="Kl",
    )
    ANON_OSN_LA = Sammlung(
        trace="Osn La",
        groups="Wortschatz|Anonym|Osn La",
        kreis="Osn",
        ort="La",
    )
    ANON_OSN_LE = Sammlung(
        trace="Osn Le",
        groups="Wortschatz|Anonym|Osn Le",
        kreis="Osn",
        ort="Le",
    )
    ANON_OSN_LÜ = Sammlung(
        trace="Osn Lü",
        groups="Wortschatz|Anonym|Osn Lü",
        kreis="Osn",
        ort="Lü",
    )
    ANON_OSN_MB = Sammlung(
        trace="Osn Mb",
        groups="Wortschatz|Anonym|Osn Mb",
        kreis="Osn",
        ort="Mb",
    )
    ANON_OSN_ME = Sammlung(
        trace="Osn Me",
        groups="Wortschatz|Anonym|Osn Me",
        kreis="Osn",
        ort="Me",
    )
    ANON_OSN_MY = Sammlung(
        trace="Osn My",
        groups="Wortschatz|Anonym|Osn My",
        kreis="Osn",
        ort="My",
    )
    ANON_OSN_NA = Sammlung(
        trace="Osn Na",
        groups="Wortschatz|Anonym|Osn Na",
        kreis="Osn",
        ort="Na",
    )
    ANON_OSN_NE = Sammlung(
        trace="Osn Ne",
        groups="Wortschatz|Anonym|Osn Ne",
        kreis="Osn",
        ort="Ne",
    )
    ANON_OSN_NH = Sammlung(
        trace="Osn Nh",
        groups="Wortschatz|Anonym|Osn Nh",
        kreis="Osn",
        ort="Nh",
    )
    ANON_OSN_NT = Sammlung(
        trace="Osn Nt",
        groups="Wortschatz|Anonym|Osn Nt",
        kreis="Osn",
        ort="Nt",
    )
    ANON_OSN_OB = Sammlung(
        trace="Osn Ob",
        groups="Wortschatz|Anonym|Osn Ob",
        kreis="Osn",
        ort="Ob",
    )
    ANON_OSN_OF = Sammlung(
        trace="Osn Of",
        groups="Wortschatz|Anonym|Osn Of",
        kreis="Osn",
        ort="Of",
    )
    ANON_OSN_OK = Sammlung(
        trace="Osn Ok",
        groups="Wortschatz|Anonym|Osn Ok",
        kreis="Osn",
        ort="Ok",
    )
    ANON_OSN_OR = Sammlung(
        trace="Osn Or",
        groups="Wortschatz|Anonym|Osn Or",
        kreis="Osn",
        ort="Or",
    )
    ANON_OSN_ÖS = Sammlung(
        trace="Osn Ös",
        groups="Wortschatz|Anonym|Osn Ös",
        kreis="Osn",
        ort="Ös",
    )
    ANON_OSN_PI = Sammlung(
        trace="Osn Pi",
        groups="Wortschatz|Anonym|Osn Pi",
        kreis="Osn",
        ort="Pi",
    )
    ANON_OSN_RE = Sammlung(
        trace="Osn Re",
        groups="Wortschatz|Anonym|Osn Re",
        kreis="Osn",
        ort="Re",
    )
    ANON_OSN_RF = Sammlung(
        trace="Osn Rf",
        groups="Wortschatz|Anonym|Osn Rf",
        kreis="Osn",
        ort="Rf",
    )
    ANON_OSN_RU = Sammlung(
        trace="Osn Ru",
        groups="Wortschatz|Anonym|Osn Ru",
        kreis="Osn",
        ort="Ru",
    )
    ANON_OSN_SC = Sammlung(
        trace="Osn Sc",
        groups="Wortschatz|Anonym|Osn Sc",
        kreis="Osn",
        ort="Sc",
    )
    ANON_OSN_SD = Sammlung(
        trace="Osn Sd",
        groups="Wortschatz|Anonym|Osn Sd",
        kreis="Osn",
        ort="Sd",
    )
    ANON_OSN_SE = Sammlung(
        trace="Osn Se",
        groups="Wortschatz|Anonym|Osn Se",
        kreis="Osn",
        ort="Se",
    )
    ANON_OSN_SF = Sammlung(
        trace="Osn Sf",
        groups="Wortschatz|Anonym|Osn Sf",
        kreis="Osn",
        ort="Sf",
    )
    ANON_OSN_SH = Sammlung(
        trace="Osn Sh",
        groups="Wortschatz|Anonym|Osn Sh",
        kreis="Osn",
        ort="Sh",
    )
    ANON_OSN_SL = Sammlung(
        trace="Osn Sl",
        groups="Wortschatz|Anonym|Osn Sl",
        kreis="Osn",
        ort="Sl",
    )
    ANON_OSN_SP = Sammlung(
        trace="Osn Sp",
        groups="Wortschatz|Anonym|Osn Sp",
        kreis="Osn",
        ort="Sp",
    )
    ANON_OSN_SU = Sammlung(
        trace="Osn Su",
        groups="Wortschatz|Anonym|Osn Su",
        kreis="Osn",
        ort="Su",
    )
    ANON_OSN_SW = Sammlung(
        trace="Osn Sw",
        groups="Wortschatz|Anonym|Osn Sw",
        kreis="Osn",
        ort="Sw",
    )
    ANON_OSN_UH = Sammlung(
        trace="Osn Uh",
        groups="Wortschatz|Anonym|Osn Uh",
        kreis="Osn",
        ort="Uh",
    )
    ANON_OSN_VE = Sammlung(
        trace="Osn Ve",
        groups="Wortschatz|Anonym|Osn Ve",
        kreis="Osn",
        ort="Ve",
    )
    ANON_OSN_VO = Sammlung(
        trace="Osn Vo",
        groups="Wortschatz|Anonym|Osn Vo",
        kreis="Osn",
        ort="Vo",
    )
    ANON_OSN_WD = Sammlung(
        trace="Osn Wd",
        groups="Wortschatz|Anonym|Osn Wd",
        kreis="Osn",
        ort="Wd",
    )
    ANON_OSN_WE = Sammlung(
        trace="Osn We",
        groups="Wortschatz|Anonym|Osn We",
        kreis="Osn",
        ort="We",
    )
    ANON_OSN_WF = Sammlung(
        trace="Osn Wf",
        groups="Wortschatz|Anonym|Osn Wf",
        kreis="Osn",
        ort="Wf",
    )
    ANON_OSN_WH = Sammlung(
        trace="Osn Wh",
        groups="Wortschatz|Anonym|Osn Wh",
        kreis="Osn",
        ort="Wh",
    )
    ANON_OSN_WS = Sammlung(
        trace="Osn Ws",
        groups="Wortschatz|Anonym|Osn Ws",
        kreis="Osn",
        ort="Ws",
    )
    ANON_PAD_AB = Sammlung(
        trace="Pad Ab",
        groups="Wortschatz|Anonym|Pad Ab",
        kreis="Pad",
        ort="Ab",
    )
    ANON_PAD_AL = Sammlung(
        trace="Pad Al",
        groups="Wortschatz|Anonym|Pad Al",
        kreis="Pad",
        ort="Al",
    )
    ANON_PAD_BH = Sammlung(
        trace="Pad Bh",
        groups="Wortschatz|Anonym|Pad Bh",
        kreis="Pad",
        ort="Bh",
    )
    ANON_PAD_BO = Sammlung(
        trace="Pad Bo",
        groups="Wortschatz|Anonym|Pad Bo",
        kreis="Pad",
        ort="Bo",
    )
    ANON_PAD_BU = Sammlung(
        trace="Pad Bu",
        groups="Wortschatz|Anonym|Pad Bu",
        kreis="Pad",
        ort="Bu",
    )
    ANON_PAD_DA = Sammlung(
        trace="Pad Da",
        groups="Wortschatz|Anonym|Pad Da",
        kreis="Pad",
        ort="Da",
    )
    ANON_PAD_DB = Sammlung(
        trace="Pad Db",
        groups="Wortschatz|Anonym|Pad Db",
        kreis="Pad",
        ort="Db",
    )
    ANON_PAD_DH = Sammlung(
        trace="Pad Dh",
        groups="Wortschatz|Anonym|Pad Dh",
        kreis="Pad",
        ort="Dh",
    )
    ANON_PAD_EL = Sammlung(
        trace="Pad El",
        groups="Wortschatz|Anonym|Pad El",
        kreis="Pad",
        ort="El",
    )
    ANON_PAD_ES = Sammlung(
        trace="Pad Es",
        groups="Wortschatz|Anonym|Pad Es",
        kreis="Pad",
        ort="Es",
    )
    ANON_PAD_HH = Sammlung(
        trace="Pad Hh",
        groups="Wortschatz|Anonym|Pad Hh",
        kreis="Pad",
        ort="Hh",
    )
    ANON_PAD_HÖ = Sammlung(
        trace="Pad Hö",
        groups="Wortschatz|Anonym|Pad Hö",
        kreis="Pad",
        ort="Hö",
    )
    ANON_PAD_KB = Sammlung(
        trace="Pad Kb",
        groups="Wortschatz|Anonym|Pad Kb",
        kreis="Pad",
        ort="Kb",
    )
    ANON_PAD_KL = Sammlung(
        trace="Pad Kl",
        groups="Wortschatz|Anonym|Pad Kl",
        kreis="Pad",
        ort="Kl",
    )
    ANON_PAD_LI = Sammlung(
        trace="Pad Li",
        groups="Wortschatz|Anonym|Pad Li",
        kreis="Pad",
        ort="Li",
    )
    ANON_PAD_LP = Sammlung(
        trace="Pad Lp",
        groups="Wortschatz|Anonym|Pad Lp",
        kreis="Pad",
        ort="Lp",
    )
    ANON_PAD_ML = Sammlung(
        trace="Pad Ml",
        groups="Wortschatz|Anonym|Pad Ml",
        kreis="Pad",
        ort="Ml",
    )
    ANON_PAD_NB = Sammlung(
        trace="Pad Nb",
        groups="Wortschatz|Anonym|Pad Nb",
        kreis="Pad",
        ort="Nb",
    )
    ANON_PAD_NE = Sammlung(
        trace="Pad Ne",
        groups="Wortschatz|Anonym|Pad Ne",
        kreis="Pad",
        ort="Ne",
    )
    ANON_PAD_NH = Sammlung(
        trace="Pad Nh",
        groups="Wortschatz|Anonym|Pad Nh",
        kreis="Pad",
        ort="Nh",
    )
    ANON_PAD_NS = Sammlung(
        trace="Pad Ns",
        groups="Wortschatz|Anonym|Pad Ns",
        kreis="Pad",
        ort="Ns",
    )
    ANON_PAD_NT = Sammlung(
        trace="Pad Nt",
        groups="Wortschatz|Anonym|Pad Nt",
        kreis="Pad",
        ort="Nt",
    )
    ANON_PAD_OL = Sammlung(
        trace="Pad Ol",
        groups="Wortschatz|Anonym|Pad Ol",
        kreis="Pad",
        ort="Ol",
    )
    ANON_PAD_OM = Sammlung(
        trace="Pad Om",
        groups="Wortschatz|Anonym|Pad Om",
        kreis="Pad",
        ort="Om",
    )
    ANON_PAD_PB = Sammlung(
        trace="Pad Pb",
        groups="Wortschatz|Anonym|Pad Pb",
        kreis="Pad",
        ort="Pb",
    )
    ANON_PAD_RI = Sammlung(
        trace="Pad Ri",
        groups="Wortschatz|Anonym|Pad Ri",
        kreis="Pad",
        ort="Ri",
    )
    ANON_PAD_SA = Sammlung(
        trace="Pad Sa",
        groups="Wortschatz|Anonym|Pad Sa",
        kreis="Pad",
        ort="Sa",
    )
    ANON_PAD_SC = Sammlung(
        trace="Pad Sc",
        groups="Wortschatz|Anonym|Pad Sc",
        kreis="Pad",
        ort="Sc",
    )
    ANON_PAD_SH = Sammlung(
        trace="Pad Sh",
        groups="Wortschatz|Anonym|Pad Sh",
        kreis="Pad",
        ort="Sh",
    )
    ANON_PAD_SL = Sammlung(
        trace="Pad Sl",
        groups="Wortschatz|Anonym|Pad Sl",
        kreis="Pad",
        ort="Sl",
    )
    ANON_PAD_ST = Sammlung(
        trace="Pad St",
        groups="Wortschatz|Anonym|Pad St",
        kreis="Pad",
        ort="St",
    )
    ANON_PAD_SU = Sammlung(
        trace="Pad Su",
        groups="Wortschatz|Anonym|Pad Su",
        kreis="Pad",
        ort="Su",
    )
    ANON_PAD_SW = Sammlung(
        trace="Pad Sw",
        groups="Wortschatz|Anonym|Pad Sw",
        kreis="Pad",
        ort="Sw",
    )
    ANON_PAD_WH = Sammlung(
        trace="Pad Wh",
        groups="Wortschatz|Anonym|Pad Wh",
        kreis="Pad",
        ort="Wh",
    )
    ANON_PAD_WL = Sammlung(
        trace="Pad Wl",
        groups="Wortschatz|Anonym|Pad Wl",
        kreis="Pad",
        ort="Wl",
    )
    ANON_PAD_WW = Sammlung(
        trace="Pad Ww",
        groups="Wortschatz|Anonym|Pad Ww",
        kreis="Pad",
        ort="Ww",
    )
    ANON_REK_AD = Sammlung(
        trace="Rek Ad",
        groups="Wortschatz|Anonym|Rek Ad",
        kreis="Rek",
        ort="Ad",
    )
    ANON_REK_AL = Sammlung(
        trace="Rek Al",
        groups="Wortschatz|Anonym|Rek Al",
        kreis="Rek",
        ort="Al",
    )
    ANON_REK_AS = Sammlung(
        trace="Rek As",
        groups="Wortschatz|Anonym|Rek As",
        kreis="Rek",
        ort="As",
    )
    ANON_REK_BA = Sammlung(
        trace="Rek Ba",
        groups="Wortschatz|Anonym|Rek Ba",
        kreis="Rek",
        ort="Ba",
    )
    ANON_REK_BD = Sammlung(
        trace="Rek Bd",
        groups="Wortschatz|Anonym|Rek Bd",
        kreis="Rek",
        ort="Bd",
    )
    ANON_REK_BM = Sammlung(
        trace="Rek Bm",
        groups="Wortschatz|Anonym|Rek Bm",
        kreis="Rek",
        ort="Bm",
    )
    ANON_REK_BO = Sammlung(
        trace="Rek Bo",
        groups="Wortschatz|Anonym|Rek Bo",
        kreis="Rek",
        ort="Bo",
    )
    ANON_REK_BP = Sammlung(
        trace="Rek Bp",
        groups="Wortschatz|Anonym|Rek Bp",
        kreis="Rek",
        ort="Bp",
    )
    ANON_REK_BS = Sammlung(
        trace="Rek Bs",
        groups="Wortschatz|Anonym|Rek Bs",
        kreis="Rek",
        ort="Bs",
    )
    ANON_REK_BU = Sammlung(
        trace="Rek Bu",
        groups="Wortschatz|Anonym|Rek Bu",
        kreis="Rek",
        ort="Bu",
    )
    ANON_REK_BX = Sammlung(
        trace="Rek Bx",
        groups="Wortschatz|Anonym|Rek Bx",
        kreis="Rek",
        ort="Bx",
    )
    ANON_REK_DA = Sammlung(
        trace="Rek Da",
        groups="Wortschatz|Anonym|Rek Da",
        kreis="Rek",
        ort="Da",
    )
    ANON_REK_DE = Sammlung(
        trace="Rek De",
        groups="Wortschatz|Anonym|Rek De",
        kreis="Rek",
        ort="De",
    )
    ANON_REK_DI = Sammlung(
        trace="Rek Di",
        groups="Wortschatz|Anonym|Rek Di",
        kreis="Rek",
        ort="Di",
    )
    ANON_REK_DO = Sammlung(
        trace="Rek Do",
        groups="Wortschatz|Anonym|Rek Do",
        kreis="Rek",
        ort="Do",
    )
    ANON_REK_ER = Sammlung(
        trace="Rek Er",
        groups="Wortschatz|Anonym|Rek Er",
        kreis="Rek",
        ort="Er",
    )
    ANON_REK_ES = Sammlung(
        trace="Rek Es",
        groups="Wortschatz|Anonym|Rek Es",
        kreis="Rek",
        ort="Es",
    )
    ANON_REK_FH = Sammlung(
        trace="Rek Fh",
        groups="Wortschatz|Anonym|Rek Fh",
        kreis="Rek",
        ort="Fh",
    )
    ANON_REK_GB = Sammlung(
        trace="Rek Gb",
        groups="Wortschatz|Anonym|Rek Gb",
        kreis="Rek",
        ort="Gb",
    )
    ANON_REK_GL = Sammlung(
        trace="Rek Gl",
        groups="Wortschatz|Anonym|Rek Gl",
        kreis="Rek",
        ort="Gl",
    )
    ANON_REK_HA = Sammlung(
        trace="Rek Ha",
        groups="Wortschatz|Anonym|Rek Ha",
        kreis="Rek",
        ort="Ha",
    )
    ANON_REK_HB = Sammlung(
        trace="Rek Hb",
        groups="Wortschatz|Anonym|Rek Hb",
        kreis="Rek",
        ort="Hb",
    )
    ANON_REK_HE = Sammlung(
        trace="Rek He",
        groups="Wortschatz|Anonym|Rek He",
        kreis="Rek",
        ort="He",
    )
    ANON_REK_HH = Sammlung(
        trace="Rek Hh",
        groups="Wortschatz|Anonym|Rek Hh",
        kreis="Rek",
        ort="Hh",
    )
    ANON_REK_HL = Sammlung(
        trace="Rek Hl",
        groups="Wortschatz|Anonym|Rek Hl",
        kreis="Rek",
        ort="Hl",
    )
    ANON_REK_HM = Sammlung(
        trace="Rek Hm",
        groups="Wortschatz|Anonym|Rek Hm",
        kreis="Rek",
        ort="Hm",
    )
    ANON_REK_HO = Sammlung(
        trace="Rek Ho",
        groups="Wortschatz|Anonym|Rek Ho",
        kreis="Rek",
        ort="Ho",
    )
    ANON_REK_HR = Sammlung(
        trace="Rek Hr",
        groups="Wortschatz|Anonym|Rek Hr",
        kreis="Rek",
        ort="Hr",
    )
    ANON_REK_HU = Sammlung(
        trace="Rek Hu",
        groups="Wortschatz|Anonym|Rek Hu",
        kreis="Rek",
        ort="Hu",
    )
    ANON_REK_HÜ = Sammlung(
        trace="Rek Hü",
        groups="Wortschatz|Anonym|Rek Hü",
        kreis="Rek",
        ort="Hü",
    )
    ANON_REK_HV = Sammlung(
        trace="Rek Hv",
        groups="Wortschatz|Anonym|Rek Hv",
        kreis="Rek",
        ort="Hv",
    )
    ANON_REK_HX = Sammlung(
        trace="Rek Hx",
        groups="Wortschatz|Anonym|Rek Hx",
        kreis="Rek",
        ort="Hx",
    )
    ANON_REK_KH = Sammlung(
        trace="Rek Kh",
        groups="Wortschatz|Anonym|Rek Kh",
        kreis="Rek",
        ort="Kh",
    )
    ANON_REK_LA = Sammlung(
        trace="Rek La",
        groups="Wortschatz|Anonym|Rek La",
        kreis="Rek",
        ort="La",
    )
    ANON_REK_LB = Sammlung(
        trace="Rek Lb",
        groups="Wortschatz|Anonym|Rek Lb",
        kreis="Rek",
        ort="Lb",
    )
    ANON_REK_LD = Sammlung(
        trace="Rek Ld",
        groups="Wortschatz|Anonym|Rek Ld",
        kreis="Rek",
        ort="Ld",
    )
    ANON_REK_LH = Sammlung(
        trace="Rek Lh",
        groups="Wortschatz|Anonym|Rek Lh",
        kreis="Rek",
        ort="Lh",
    )
    ANON_REK_MA = Sammlung(
        trace="Rek Ma",
        groups="Wortschatz|Anonym|Rek Ma",
        kreis="Rek",
        ort="Ma",
    )
    ANON_REK_MH = Sammlung(
        trace="Rek Mh",
        groups="Wortschatz|Anonym|Rek Mh",
        kreis="Rek",
        ort="Mh",
    )
    ANON_REK_OF = Sammlung(
        trace="Rek Of",
        groups="Wortschatz|Anonym|Rek Of",
        kreis="Rek",
        ort="Of",
    )
    ANON_REK_PE = Sammlung(
        trace="Rek Pe",
        groups="Wortschatz|Anonym|Rek Pe",
        kreis="Rek",
        ort="Pe",
    )
    ANON_REK_PO = Sammlung(
        trace="Rek Po",
        groups="Wortschatz|Anonym|Rek Po",
        kreis="Rek",
        ort="Po",
    )
    ANON_REK_RA = Sammlung(
        trace="Rek Ra",
        groups="Wortschatz|Anonym|Rek Ra",
        kreis="Rek",
        ort="Ra",
    )
    ANON_REK_RH = Sammlung(
        trace="Rek Rh",
        groups="Wortschatz|Anonym|Rek Rh",
        kreis="Rek",
        ort="Rh",
    )
    ANON_REK_RS = Sammlung(
        trace="Rek Rs",
        groups="Wortschatz|Anonym|Rek Rs",
        kreis="Rek",
        ort="Rs",
    )
    ANON_REK_SI = Sammlung(
        trace="Rek Si",
        groups="Wortschatz|Anonym|Rek Si",
        kreis="Rek",
        ort="Si",
    )
    ANON_REK_SM = Sammlung(
        trace="Rek Sm",
        groups="Wortschatz|Anonym|Rek Sm",
        kreis="Rek",
        ort="Sm",
    )
    ANON_REK_ST = Sammlung(
        trace="Rek St",
        groups="Wortschatz|Anonym|Rek St",
        kreis="Rek",
        ort="St",
    )
    ANON_REK_SY = Sammlung(
        trace="Rek Sy",
        groups="Wortschatz|Anonym|Rek Sy",
        kreis="Rek",
        ort="Sy",
    )
    ANON_REK_WD = Sammlung(
        trace="Rek Wd",
        groups="Wortschatz|Anonym|Rek Wd",
        kreis="Rek",
        ort="Wd",
    )
    ANON_REK_WH = Sammlung(
        trace="Rek Wh",
        groups="Wortschatz|Anonym|Rek Wh",
        kreis="Rek",
        ort="Wh",
    )
    ANON_REK_WP = Sammlung(
        trace="Rek Wp",
        groups="Wortschatz|Anonym|Rek Wp",
        kreis="Rek",
        ort="Wp",
    )
    ANON_REK_WU = Sammlung(
        trace="Rek Wu",
        groups="Wortschatz|Anonym|Rek Wu",
        kreis="Rek",
        ort="Wu",
    )
    ANON_SCH_AL = Sammlung(
        trace="Sch Al",
        groups="Wortschatz|Anonym|Sch Al",
        kreis="Sch",
        ort="Al",
    )
    ANON_SCH_AN = Sammlung(
        trace="Sch An",
        groups="Wortschatz|Anonym|Sch An",
        kreis="Sch",
        ort="An",
    )
    ANON_SCH_AP = Sammlung(
        trace="Sch Ap",
        groups="Wortschatz|Anonym|Sch Ap",
        kreis="Sch",
        ort="Ap",
    )
    ANON_SCH_AU = Sammlung(
        trace="Sch Au",
        groups="Wortschatz|Anonym|Sch Au",
        kreis="Sch",
        ort="Au",
    )
    ANON_SCH_BA = Sammlung(
        trace="Sch Ba",
        groups="Wortschatz|Anonym|Sch Ba",
        kreis="Sch",
        ort="Ba",
    )
    ANON_SCH_BD = Sammlung(
        trace="Sch Bd",
        groups="Wortschatz|Anonym|Sch Bd",
        kreis="Sch",
        ort="Bd",
    )
    ANON_SCH_BO = Sammlung(
        trace="Sch Bo",
        groups="Wortschatz|Anonym|Sch Bo",
        kreis="Sch",
        ort="Bo",
    )
    ANON_SCH_DB = Sammlung(
        trace="Sch Db",
        groups="Wortschatz|Anonym|Sch Db",
        kreis="Sch",
        ort="Db",
    )
    ANON_SCH_EN = Sammlung(
        trace="Sch En",
        groups="Wortschatz|Anonym|Sch En",
        kreis="Sch",
        ort="En",
    )
    ANON_SCH_ES = Sammlung(
        trace="Sch Es",
        groups="Wortschatz|Anonym|Sch Es",
        kreis="Sch",
        ort="Es",
    )
    ANON_SCH_EX = Sammlung(
        trace="Sch Ex",
        groups="Wortschatz|Anonym|Sch Ex",
        kreis="Sch",
        ort="Ex",
    )
    ANON_SCH_FI = Sammlung(
        trace="Sch Fi",
        groups="Wortschatz|Anonym|Sch Fi",
        kreis="Sch",
        ort="Fi",
    )
    ANON_SCH_FU = Sammlung(
        trace="Sch Fu",
        groups="Wortschatz|Anonym|Sch Fu",
        kreis="Sch",
        ort="Fu",
    )
    ANON_SCH_GB = Sammlung(
        trace="Sch Gb",
        groups="Wortschatz|Anonym|Sch Gb",
        kreis="Sch",
        ort="Gb",
    )
    ANON_SCH_GH = Sammlung(
        trace="Sch Gh",
        groups="Wortschatz|Anonym|Sch Gh",
        kreis="Sch",
        ort="Gh",
    )
    ANON_SCH_GN = Sammlung(
        trace="Sch Gn",
        groups="Wortschatz|Anonym|Sch Gn",
        kreis="Sch",
        ort="Gn",
    )
    ANON_SCH_GW = Sammlung(
        trace="Sch Gw",
        groups="Wortschatz|Anonym|Sch Gw",
        kreis="Sch",
        ort="Gw",
    )
    ANON_SCH_HA = Sammlung(
        trace="Sch Ha",
        groups="Wortschatz|Anonym|Sch Ha",
        kreis="Sch",
        ort="Ha",
    )
    ANON_SCH_HD = Sammlung(
        trace="Sch Hd",
        groups="Wortschatz|Anonym|Sch Hd",
        kreis="Sch",
        ort="Hd",
    )
    ANON_SCH_HE = Sammlung(
        trace="Sch He",
        groups="Wortschatz|Anonym|Sch He",
        kreis="Sch",
        ort="He",
    )
    ANON_SCH_HH = Sammlung(
        trace="Sch Hh",
        groups="Wortschatz|Anonym|Sch Hh",
        kreis="Sch",
        ort="Hh",
    )
    ANON_SCH_HO = Sammlung(
        trace="Sch Ho",
        groups="Wortschatz|Anonym|Sch Ho",
        kreis="Sch",
        ort="Ho",
    )
    ANON_SCH_HÖ = Sammlung(
        trace="Sch Hö",
        groups="Wortschatz|Anonym|Sch Hö",
        kreis="Sch",
        ort="Hö",
    )
    ANON_SCH_HR = Sammlung(
        trace="Sch Hr",
        groups="Wortschatz|Anonym|Sch Hr",
        kreis="Sch",
        ort="Hr",
    )
    ANON_SCH_HT = Sammlung(
        trace="Sch Ht",
        groups="Wortschatz|Anonym|Sch Ht",
        kreis="Sch",
        ort="Ht",
    )
    ANON_SCH_KA = Sammlung(
        trace="Sch Ka",
        groups="Wortschatz|Anonym|Sch Ka",
        kreis="Sch",
        ort="Ka",
    )
    ANON_SCH_KH = Sammlung(
        trace="Sch Kh",
        groups="Wortschatz|Anonym|Sch Kh",
        kreis="Sch",
        ort="Kh",
    )
    ANON_SCH_KR = Sammlung(
        trace="Sch Kr",
        groups="Wortschatz|Anonym|Sch Kr",
        kreis="Sch",
        ort="Kr",
    )
    ANON_SCH_LF = Sammlung(
        trace="Sch Lf",
        groups="Wortschatz|Anonym|Sch Lf",
        kreis="Sch",
        ort="Lf",
    )
    ANON_SCH_LI = Sammlung(
        trace="Sch Li",
        groups="Wortschatz|Anonym|Sch Li",
        kreis="Sch",
        ort="Li",
    )
    ANON_SCH_LY = Sammlung(
        trace="Sch Ly",
        groups="Wortschatz|Anonym|Sch Ly",
        kreis="Sch",
        ort="Ly",
    )
    ANON_SCH_MB = Sammlung(
        trace="Sch Mb",
        groups="Wortschatz|Anonym|Sch Mb",
        kreis="Sch",
        ort="Mb",
    )
    ANON_SCH_ND = Sammlung(
        trace="Sch Nd",
        groups="Wortschatz|Anonym|Sch Nd",
        kreis="Sch",
        ort="Nd",
    )
    ANON_SCH_OB = Sammlung(
        trace="Sch Ob",
        groups="Wortschatz|Anonym|Sch Ob",
        kreis="Sch",
        ort="Ob",
    )
    ANON_SCH_OT = Sammlung(
        trace="Sch Ot",
        groups="Wortschatz|Anonym|Sch Ot",
        kreis="Sch",
        ort="Ot",
    )
    ANON_SCH_PÖ = Sammlung(
        trace="Sch Pö",
        groups="Wortschatz|Anonym|Sch Pö",
        kreis="Sch",
        ort="Pö",
    )
    ANON_SCH_RA = Sammlung(
        trace="Sch Ra",
        groups="Wortschatz|Anonym|Sch Ra",
        kreis="Sch",
        ort="Ra",
    )
    ANON_SCH_RD = Sammlung(
        trace="Sch Rd",
        groups="Wortschatz|Anonym|Sch Rd",
        kreis="Sch",
        ort="Rd",
    )
    ANON_SCH_RE = Sammlung(
        trace="Sch Re",
        groups="Wortschatz|Anonym|Sch Re",
        kreis="Sch",
        ort="Re",
    )
    ANON_SCH_RH = Sammlung(
        trace="Sch Rh",
        groups="Wortschatz|Anonym|Sch Rh",
        kreis="Sch",
        ort="Rh",
    )
    ANON_SCH_RI = Sammlung(
        trace="Sch Ri",
        groups="Wortschatz|Anonym|Sch Ri",
        kreis="Sch",
        ort="Ri",
    )
    ANON_SCH_RN = Sammlung(
        trace="Sch Rn",
        groups="Wortschatz|Anonym|Sch Rn",
        kreis="Sch",
        ort="Rn",
    )
    ANON_SCH_RO = Sammlung(
        trace="Sch Ro",
        groups="Wortschatz|Anonym|Sch Ro",
        kreis="Sch",
        ort="Ro",
    )
    ANON_SCH_RS = Sammlung(
        trace="Sch Rs",
        groups="Wortschatz|Anonym|Sch Rs",
        kreis="Sch",
        ort="Rs",
    )
    ANON_SCH_RU = Sammlung(
        trace="Sch Ru",
        groups="Wortschatz|Anonym|Sch Ru",
        kreis="Sch",
        ort="Ru",
    )
    ANON_SCH_SD = Sammlung(
        trace="Sch Sd",
        groups="Wortschatz|Anonym|Sch Sd",
        kreis="Sch",
        ort="Sd",
    )
    ANON_SCH_SH = Sammlung(
        trace="Sch Sh",
        groups="Wortschatz|Anonym|Sch Sh",
        kreis="Sch",
        ort="Sh",
    )
    ANON_SCH_WA = Sammlung(
        trace="Sch Wa",
        groups="Wortschatz|Anonym|Sch Wa",
        kreis="Sch",
        ort="Wa",
    )
    ANON_SCH_WB = Sammlung(
        trace="Sch Wb",
        groups="Wortschatz|Anonym|Sch Wb",
        kreis="Sch",
        ort="Wb",
    )
    ANON_SCH_WD = Sammlung(
        trace="Sch Wd",
        groups="Wortschatz|Anonym|Sch Wd",
        kreis="Sch",
        ort="Wd",
    )
    ANON_SCH_WE = Sammlung(
        trace="Sch We",
        groups="Wortschatz|Anonym|Sch We",
        kreis="Sch",
        ort="We",
    )
    ANON_SCH_WK = Sammlung(
        trace="Sch Wk",
        groups="Wortschatz|Anonym|Sch Wk",
        kreis="Sch",
        ort="Wk",
    )
    ANON_SOS_AL = Sammlung(
        trace="Sos Al",
        groups="Wortschatz|Anonym|Sos Al",
        kreis="Sos",
        ort="Al",
    )
    ANON_SOS_AM = Sammlung(
        trace="Sos Am",
        groups="Wortschatz|Anonym|Sos Am",
        kreis="Sos",
        ort="Am",
    )
    ANON_SOS_BA = Sammlung(
        trace="Sos Ba",
        groups="Wortschatz|Anonym|Sos Ba",
        kreis="Sos",
        ort="Ba",
    )
    ANON_SOS_BE = Sammlung(
        trace="Sos Be",
        groups="Wortschatz|Anonym|Sos Be",
        kreis="Sos",
        ort="Be",
    )
    ANON_SOS_BG = Sammlung(
        trace="Sos Bg",
        groups="Wortschatz|Anonym|Sos Bg",
        kreis="Sos",
        ort="Bg",
    )
    ANON_SOS_BH = Sammlung(
        trace="Sos Bh",
        groups="Wortschatz|Anonym|Sos Bh",
        kreis="Sos",
        ort="Bh",
    )
    ANON_SOS_BK = Sammlung(
        trace="Sos Bk",
        groups="Wortschatz|Anonym|Sos Bk",
        kreis="Sos",
        ort="Bk",
    )
    ANON_SOS_BL = Sammlung(
        trace="Sos Bl",
        groups="Wortschatz|Anonym|Sos Bl",
        kreis="Sos",
        ort="Bl",
    )
    ANON_SOS_BM = Sammlung(
        trace="Sos Bm",
        groups="Wortschatz|Anonym|Sos Bm",
        kreis="Sos",
        ort="Bm",
    )
    ANON_SOS_BN = Sammlung(
        trace="Sos Bn",
        groups="Wortschatz|Anonym|Sos Bn",
        kreis="Sos",
        ort="Bn",
    )
    ANON_SOS_BO = Sammlung(
        trace="Sos Bo",
        groups="Wortschatz|Anonym|Sos Bo",
        kreis="Sos",
        ort="Bo",
    )
    ANON_SOS_BR = Sammlung(
        trace="Sos Br",
        groups="Wortschatz|Anonym|Sos Br",
        kreis="Sos",
        ort="Br",
    )
    ANON_SOS_BS = Sammlung(
        trace="Sos Bs",
        groups="Wortschatz|Anonym|Sos Bs",
        kreis="Sos",
        ort="Bs",
    )
    ANON_SOS_BT = Sammlung(
        trace="Sos Bt",
        groups="Wortschatz|Anonym|Sos Bt",
        kreis="Sos",
        ort="Bt",
    )
    ANON_SOS_BÜ = Sammlung(
        trace="Sos Bü",
        groups="Wortschatz|Anonym|Sos Bü",
        kreis="Sos",
        ort="Bü",
    )
    ANON_SOS_BW = Sammlung(
        trace="Sos Bw",
        groups="Wortschatz|Anonym|Sos Bw",
        kreis="Sos",
        ort="Bw",
    )
    ANON_SOS_DE = Sammlung(
        trace="Sos De",
        groups="Wortschatz|Anonym|Sos De",
        kreis="Sos",
        ort="De",
    )
    ANON_SOS_DI = Sammlung(
        trace="Sos Di",
        groups="Wortschatz|Anonym|Sos Di",
        kreis="Sos",
        ort="Di",
    )
    ANON_SOS_DL = Sammlung(
        trace="Sos Dl",
        groups="Wortschatz|Anonym|Sos Dl",
        kreis="Sos",
        ort="Dl",
    )
    ANON_SOS_DW = Sammlung(
        trace="Sos Dw",
        groups="Wortschatz|Anonym|Sos Dw",
        kreis="Sos",
        ort="Dw",
    )
    ANON_SOS_EB = Sammlung(
        trace="Sos Eb",
        groups="Wortschatz|Anonym|Sos Eb",
        kreis="Sos",
        ort="Eb",
    )
    ANON_SOS_EH = Sammlung(
        trace="Sos Eh",
        groups="Wortschatz|Anonym|Sos Eh",
        kreis="Sos",
        ort="Eh",
    )
    ANON_SOS_EI = Sammlung(
        trace="Sos Ei",
        groups="Wortschatz|Anonym|Sos Ei",
        kreis="Sos",
        ort="Ei",
    )
    ANON_SOS_EK = Sammlung(
        trace="Sos Ek",
        groups="Wortschatz|Anonym|Sos Ek",
        kreis="Sos",
        ort="Ek",
    )
    ANON_SOS_EL = Sammlung(
        trace="Sos El",
        groups="Wortschatz|Anonym|Sos El",
        kreis="Sos",
        ort="El",
    )
    ANON_SOS_EM = Sammlung(
        trace="Sos Em",
        groups="Wortschatz|Anonym|Sos Em",
        kreis="Sos",
        ort="Em",
    )
    ANON_SOS_EN = Sammlung(
        trace="Sos En",
        groups="Wortschatz|Anonym|Sos En",
        kreis="Sos",
        ort="En",
    )
    ANON_SOS_EO = Sammlung(
        trace="Sos Eo",
        groups="Wortschatz|Anonym|Sos Eo",
        kreis="Sos",
        ort="Eo",
    )
    ANON_SOS_EP = Sammlung(
        trace="Sos Ep",
        groups="Wortschatz|Anonym|Sos Ep",
        kreis="Sos",
        ort="Ep",
    )
    ANON_SOS_FL = Sammlung(
        trace="Sos Fl",
        groups="Wortschatz|Anonym|Sos Fl",
        kreis="Sos",
        ort="Fl",
    )
    ANON_SOS_GA = Sammlung(
        trace="Sos Ga",
        groups="Wortschatz|Anonym|Sos Ga",
        kreis="Sos",
        ort="Ga",
    )
    ANON_SOS_GÜ = Sammlung(
        trace="Sos Gü",
        groups="Wortschatz|Anonym|Sos Gü",
        kreis="Sos",
        ort="Gü",
    )
    ANON_SOS_HA = Sammlung(
        trace="Sos Ha",
        groups="Wortschatz|Anonym|Sos Ha",
        kreis="Sos",
        ort="Ha",
    )
    ANON_SOS_HE = Sammlung(
        trace="Sos He",
        groups="Wortschatz|Anonym|Sos He",
        kreis="Sos",
        ort="He",
    )
    ANON_SOS_HH = Sammlung(
        trace="Sos Hh",
        groups="Wortschatz|Anonym|Sos Hh",
        kreis="Sos",
        ort="Hh",
    )
    ANON_SOS_HI = Sammlung(
        trace="Sos Hi",
        groups="Wortschatz|Anonym|Sos Hi",
        kreis="Sos",
        ort="Hi",
    )
    ANON_SOS_HN = Sammlung(
        trace="Sos Hn",
        groups="Wortschatz|Anonym|Sos Hn",
        kreis="Sos",
        ort="Hn",
    )
    ANON_SOS_HO = Sammlung(
        trace="Sos Ho",
        groups="Wortschatz|Anonym|Sos Ho",
        kreis="Sos",
        ort="Ho",
    )
    ANON_SOS_HÖ = Sammlung(
        trace="Sos Hö",
        groups="Wortschatz|Anonym|Sos Hö",
        kreis="Sos",
        ort="Hö",
    )
    ANON_SOS_HP = Sammlung(
        trace="Sos Hp",
        groups="Wortschatz|Anonym|Sos Hp",
        kreis="Sos",
        ort="Hp",
    )
    ANON_SOS_HT = Sammlung(
        trace="Sos Ht",
        groups="Wortschatz|Anonym|Sos Ht",
        kreis="Sos",
        ort="Ht",
    )
    ANON_SOS_HU = Sammlung(
        trace="Sos Hu",
        groups="Wortschatz|Anonym|Sos Hu",
        kreis="Sos",
        ort="Hu",
    )
    ANON_SOS_IL = Sammlung(
        trace="Sos Il",
        groups="Wortschatz|Anonym|Sos Il",
        kreis="Sos",
        ort="Il",
    )
    ANON_SOS_KA = Sammlung(
        trace="Sos Ka",
        groups="Wortschatz|Anonym|Sos Ka",
        kreis="Sos",
        ort="Ka",
    )
    ANON_SOS_KL = Sammlung(
        trace="Sos Kl",
        groups="Wortschatz|Anonym|Sos Kl",
        kreis="Sos",
        ort="Kl",
    )
    ANON_SOS_KÖ = Sammlung(
        trace="Sos Kö",
        groups="Wortschatz|Anonym|Sos Kö",
        kreis="Sos",
        ort="Kö",
    )
    ANON_SOS_KU = Sammlung(
        trace="Sos Ku",
        groups="Wortschatz|Anonym|Sos Ku",
        kreis="Sos",
        ort="Ku",
    )
    ANON_SOS_KW = Sammlung(
        trace="Sos Kw",
        groups="Wortschatz|Anonym|Sos Kw",
        kreis="Sos",
        ort="Kw",
    )
    ANON_SOS_LE = Sammlung(
        trace="Sos Le",
        groups="Wortschatz|Anonym|Sos Le",
        kreis="Sos",
        ort="Le",
    )
    ANON_SOS_LH = Sammlung(
        trace="Sos Lh",
        groups="Wortschatz|Anonym|Sos Lh",
        kreis="Sos",
        ort="Lh",
    )
    ANON_SOS_LO = Sammlung(
        trace="Sos Lo",
        groups="Wortschatz|Anonym|Sos Lo",
        kreis="Sos",
        ort="Lo",
    )
    ANON_SOS_LT = Sammlung(
        trace="Sos Lt",
        groups="Wortschatz|Anonym|Sos Lt",
        kreis="Sos",
        ort="Lt",
    )
    ANON_SOS_LÜ = Sammlung(
        trace="Sos Lü",
        groups="Wortschatz|Anonym|Sos Lü",
        kreis="Sos",
        ort="Lü",
    )
    ANON_SOS_MC = Sammlung(
        trace="Sos Mc",
        groups="Wortschatz|Anonym|Sos Mc",
        kreis="Sos",
        ort="Mc",
    )
    ANON_SOS_ME = Sammlung(
        trace="Sos Me",
        groups="Wortschatz|Anonym|Sos Me",
        kreis="Sos",
        ort="Me",
    )
    ANON_SOS_ML = Sammlung(
        trace="Sos Ml",
        groups="Wortschatz|Anonym|Sos Ml",
        kreis="Sos",
        ort="Ml",
    )
    ANON_SOS_MÜ = Sammlung(
        trace="Sos Mü",
        groups="Wortschatz|Anonym|Sos Mü",
        kreis="Sos",
        ort="Mü",
    )
    ANON_SOS_MY = Sammlung(
        trace="Sos My",
        groups="Wortschatz|Anonym|Sos My",
        kreis="Sos",
        ort="My",
    )
    ANON_SOS_NA = Sammlung(
        trace="Sos Na",
        groups="Wortschatz|Anonym|Sos Na",
        kreis="Sos",
        ort="Na",
    )
    ANON_SOS_NB = Sammlung(
        trace="Sos Nb",
        groups="Wortschatz|Anonym|Sos Nb",
        kreis="Sos",
        ort="Nb",
    )
    ANON_SOS_ND = Sammlung(
        trace="Sos Nd",
        groups="Wortschatz|Anonym|Sos Nd",
        kreis="Sos",
        ort="Nd",
    )
    ANON_SOS_NE = Sammlung(
        trace="Sos Ne",
        groups="Wortschatz|Anonym|Sos Ne",
        kreis="Sos",
        ort="Ne",
    )
    ANON_SOS_NG = Sammlung(
        trace="Sos Ng",
        groups="Wortschatz|Anonym|Sos Ng",
        kreis="Sos",
        ort="Ng",
    )
    ANON_SOS_NW = Sammlung(
        trace="Sos Nw",
        groups="Wortschatz|Anonym|Sos Nw",
        kreis="Sos",
        ort="Nw",
    )
    ANON_SOS_OB = Sammlung(
        trace="Sos Ob",
        groups="Wortschatz|Anonym|Sos Ob",
        kreis="Sos",
        ort="Ob",
    )
    ANON_SOS_OH = Sammlung(
        trace="Sos Oh",
        groups="Wortschatz|Anonym|Sos Oh",
        kreis="Sos",
        ort="Oh",
    )
    ANON_SOS_ÖH = Sammlung(
        trace="Sos Öh",
        groups="Wortschatz|Anonym|Sos Öh",
        kreis="Sos",
        ort="Öh",
    )
    ANON_SOS_OÖ = Sammlung(
        trace="Sos Oö",
        groups="Wortschatz|Anonym|Sos Oö",
        kreis="Sos",
        ort="Oö",
    )
    ANON_SOS_OP = Sammlung(
        trace="Sos Op",
        groups="Wortschatz|Anonym|Sos Op",
        kreis="Sos",
        ort="Op",
    )
    ANON_SOS_PA = Sammlung(
        trace="Sos Pa",
        groups="Wortschatz|Anonym|Sos Pa",
        kreis="Sos",
        ort="Pa",
    )
    ANON_SOS_RE = Sammlung(
        trace="Sos Re",
        groups="Wortschatz|Anonym|Sos Re",
        kreis="Sos",
        ort="Re",
    )
    ANON_SOS_RL = Sammlung(
        trace="Sos Rl",
        groups="Wortschatz|Anonym|Sos Rl",
        kreis="Sos",
        ort="Rl",
    )
    ANON_SOS_RÖ = Sammlung(
        trace="Sos Rö",
        groups="Wortschatz|Anonym|Sos Rö",
        kreis="Sos",
        ort="Rö",
    )
    ANON_SOS_RU = Sammlung(
        trace="Sos Ru",
        groups="Wortschatz|Anonym|Sos Ru",
        kreis="Sos",
        ort="Ru",
    )
    ANON_SOS_SB = Sammlung(
        trace="Sos Sb",
        groups="Wortschatz|Anonym|Sos Sb",
        kreis="Sos",
        ort="Sb",
    )
    ANON_SOS_SC = Sammlung(
        trace="Sos Sc",
        groups="Wortschatz|Anonym|Sos Sc",
        kreis="Sos",
        ort="Sc",
    )
    ANON_SOS_SD = Sammlung(
        trace="Sos Sd",
        groups="Wortschatz|Anonym|Sos Sd",
        kreis="Sos",
        ort="Sd",
    )
    ANON_SOS_SI = Sammlung(
        trace="Sos Si",
        groups="Wortschatz|Anonym|Sos Si",
        kreis="Sos",
        ort="Si",
    )
    ANON_SOS_SK = Sammlung(
        trace="Sos Sk",
        groups="Wortschatz|Anonym|Sos Sk",
        kreis="Sos",
        ort="Sk",
    )
    ANON_SOS_SL = Sammlung(
        trace="Sos Sl",
        groups="Wortschatz|Anonym|Sos Sl",
        kreis="Sos",
        ort="Sl",
    )
    ANON_SOS_SO = Sammlung(
        trace="Sos So",
        groups="Wortschatz|Anonym|Sos So",
        kreis="Sos",
        ort="So",
    )
    ANON_SOS_ST = Sammlung(
        trace="Sos St",
        groups="Wortschatz|Anonym|Sos St",
        kreis="Sos",
        ort="St",
    )
    ANON_SOS_SW = Sammlung(
        trace="Sos Sw",
        groups="Wortschatz|Anonym|Sos Sw",
        kreis="Sos",
        ort="Sw",
    )
    ANON_SOS_TH = Sammlung(
        trace="Sos Th",
        groups="Wortschatz|Anonym|Sos Th",
        kreis="Sos",
        ort="Th",
    )
    ANON_SOS_TÖ = Sammlung(
        trace="Sos Tö",
        groups="Wortschatz|Anonym|Sos Tö",
        kreis="Sos",
        ort="Tö",
    )
    ANON_SOS_VE = Sammlung(
        trace="Sos Ve",
        groups="Wortschatz|Anonym|Sos Ve",
        kreis="Sos",
        ort="Ve",
    )
    ANON_SOS_VÖ = Sammlung(
        trace="Sos Vö",
        groups="Wortschatz|Anonym|Sos Vö",
        kreis="Sos",
        ort="Vö",
    )
    ANON_SOS_WA = Sammlung(
        trace="Sos Wa",
        groups="Wortschatz|Anonym|Sos Wa",
        kreis="Sos",
        ort="Wa",
    )
    ANON_SOS_WB = Sammlung(
        trace="Sos Wb",
        groups="Wortschatz|Anonym|Sos Wb",
        kreis="Sos",
        ort="Wb",
    )
    ANON_SOS_WD = Sammlung(
        trace="Sos Wd",
        groups="Wortschatz|Anonym|Sos Wd",
        kreis="Sos",
        ort="Wd",
    )
    ANON_SOS_WE = Sammlung(
        trace="Sos We",
        groups="Wortschatz|Anonym|Sos We",
        kreis="Sos",
        ort="We",
    )
    ANON_SOS_WH = Sammlung(
        trace="Sos Wh",
        groups="Wortschatz|Anonym|Sos Wh",
        kreis="Sos",
        ort="Wh",
    )
    ANON_SOS_WI = Sammlung(
        trace="Sos Wi",
        groups="Wortschatz|Anonym|Sos Wi",
        kreis="Sos",
        ort="Wi",
    )
    ANON_SOS_WL = Sammlung(
        trace="Sos Wl",
        groups="Wortschatz|Anonym|Sos Wl",
        kreis="Sos",
        ort="Wl",
    )
    ANON_SOS_WÖ = Sammlung(
        trace="Sos Wö",
        groups="Wortschatz|Anonym|Sos Wö",
        kreis="Sos",
        ort="Wö",
    )
    ANON_SOS_WP = Sammlung(
        trace="Sos Wp",
        groups="Wortschatz|Anonym|Sos Wp",
        kreis="Sos",
        ort="Wp",
    )
    ANON_SOS_WV = Sammlung(
        trace="Sos Wv",
        groups="Wortschatz|Anonym|Sos Wv",
        kreis="Sos",
        ort="Wv",
    )
    ANON_STF_AB = Sammlung(
        trace="Stf Ab",
        groups="Wortschatz|Anonym|Stf Ab",
        kreis="Stf",
        ort="Ab",
    )
    ANON_STF_AR = Sammlung(
        trace="Stf Ar",
        groups="Wortschatz|Anonym|Stf Ar",
        kreis="Stf",
        ort="Ar",
    )
    ANON_STF_BO = Sammlung(
        trace="Stf Bo",
        groups="Wortschatz|Anonym|Stf Bo",
        kreis="Stf",
        ort="Bo",
    )
    ANON_STF_BU = Sammlung(
        trace="Stf Bu",
        groups="Wortschatz|Anonym|Stf Bu",
        kreis="Stf",
        ort="Bu",
    )
    ANON_STF_DU = Sammlung(
        trace="Stf Du",
        groups="Wortschatz|Anonym|Stf Du",
        kreis="Stf",
        ort="Du",
    )
    ANON_STF_EL = Sammlung(
        trace="Stf El",
        groups="Wortschatz|Anonym|Stf El",
        kreis="Stf",
        ort="El",
    )
    ANON_STF_EM = Sammlung(
        trace="Stf Em",
        groups="Wortschatz|Anonym|Stf Em",
        kreis="Stf",
        ort="Em",
    )
    ANON_STF_HA = Sammlung(
        trace="Stf Ha",
        groups="Wortschatz|Anonym|Stf Ha",
        kreis="Stf",
        ort="Ha",
    )
    ANON_STF_HB = Sammlung(
        trace="Stf Hb",
        groups="Wortschatz|Anonym|Stf Hb",
        kreis="Stf",
        ort="Hb",
    )
    ANON_STF_HH = Sammlung(
        trace="Stf Hh",
        groups="Wortschatz|Anonym|Stf Hh",
        kreis="Stf",
        ort="Hh",
    )
    ANON_STF_HL = Sammlung(
        trace="Stf Hl",
        groups="Wortschatz|Anonym|Stf Hl",
        kreis="Stf",
        ort="Hl",
    )
    ANON_STF_HO = Sammlung(
        trace="Stf Ho",
        groups="Wortschatz|Anonym|Stf Ho",
        kreis="Stf",
        ort="Ho",
    )
    ANON_STF_KA = Sammlung(
        trace="Stf Ka",
        groups="Wortschatz|Anonym|Stf Ka",
        kreis="Stf",
        ort="Ka",
    )
    ANON_STF_LA = Sammlung(
        trace="Stf La",
        groups="Wortschatz|Anonym|Stf La",
        kreis="Stf",
        ort="La",
    )
    ANON_STF_LE = Sammlung(
        trace="Stf Le",
        groups="Wortschatz|Anonym|Stf Le",
        kreis="Stf",
        ort="Le",
    )
    ANON_STF_LH = Sammlung(
        trace="Stf Lh",
        groups="Wortschatz|Anonym|Stf Lh",
        kreis="Stf",
        ort="Lh",
    )
    ANON_STF_LS = Sammlung(
        trace="Stf Ls",
        groups="Wortschatz|Anonym|Stf Ls",
        kreis="Stf",
        ort="Ls",
    )
    ANON_STF_ME = Sammlung(
        trace="Stf Me",
        groups="Wortschatz|Anonym|Stf Me",
        kreis="Stf",
        ort="Me",
    )
    ANON_STF_MS = Sammlung(
        trace="Stf Ms",
        groups="Wortschatz|Anonym|Stf Ms",
        kreis="Stf",
        ort="Ms",
    )
    ANON_STF_NK = Sammlung(
        trace="Stf Nk",
        groups="Wortschatz|Anonym|Stf Nk",
        kreis="Stf",
        ort="Nk",
    )
    ANON_STF_NW = Sammlung(
        trace="Stf Nw",
        groups="Wortschatz|Anonym|Stf Nw",
        kreis="Stf",
        ort="Nw",
    )
    ANON_STF_OC = Sammlung(
        trace="Stf Oc",
        groups="Wortschatz|Anonym|Stf Oc",
        kreis="Stf",
        ort="Oc",
    )
    ANON_STF_RH = Sammlung(
        trace="Stf Rh",
        groups="Wortschatz|Anonym|Stf Rh",
        kreis="Stf",
        ort="Rh",
    )
    ANON_STF_RO = Sammlung(
        trace="Stf Ro",
        groups="Wortschatz|Anonym|Stf Ro",
        kreis="Stf",
        ort="Ro",
    )
    ANON_STF_SE = Sammlung(
        trace="Stf Se",
        groups="Wortschatz|Anonym|Stf Se",
        kreis="Stf",
        ort="Se",
    )
    ANON_STF_VE = Sammlung(
        trace="Stf Ve",
        groups="Wortschatz|Anonym|Stf Ve",
        kreis="Stf",
        ort="Ve",
    )
    ANON_STF_WB = Sammlung(
        trace="Stf Wb",
        groups="Wortschatz|Anonym|Stf Wb",
        kreis="Stf",
        ort="Wb",
    )
    ANON_STF_WH = Sammlung(
        trace="Stf Wh",
        groups="Wortschatz|Anonym|Stf Wh",
        kreis="Stf",
        ort="Wh",
    )
    ANON_STF_WT = Sammlung(
        trace="Stf Wt",
        groups="Wortschatz|Anonym|Stf Wt",
        kreis="Stf",
        ort="Wt",
    )
    ANON_STH_EN = Sammlung(
        trace="Sth En",
        groups="Wortschatz|Anonym|Sth En",
        kreis="Sth",
        ort="En",
    )
    ANON_STH_GH = Sammlung(
        trace="Sth Gh",
        groups="Wortschatz|Anonym|Sth Gh",
        kreis="Sth",
        ort="Gh",
    )
    ANON_STH_HB = Sammlung(
        trace="Sth Hb",
        groups="Wortschatz|Anonym|Sth Hb",
        kreis="Sth",
        ort="Hb",
    )
    ANON_STH_HH = Sammlung(
        trace="Sth Hh",
        groups="Wortschatz|Anonym|Sth Hh",
        kreis="Sth",
        ort="Hh",
    )
    ANON_STH_HS = Sammlung(
        trace="Sth Hs",
        groups="Wortschatz|Anonym|Sth Hs",
        kreis="Sth",
        ort="Hs",
    )
    ANON_STH_LA = Sammlung(
        trace="Sth La",
        groups="Wortschatz|Anonym|Sth La",
        kreis="Sth",
        ort="La",
    )
    ANON_STH_LF = Sammlung(
        trace="Sth Lf",
        groups="Wortschatz|Anonym|Sth Lf",
        kreis="Sth",
        ort="Lf",
    )
    ANON_STH_LH = Sammlung(
        trace="Sth Lh",
        groups="Wortschatz|Anonym|Sth Lh",
        kreis="Sth",
        ort="Lh",
    )
    ANON_STH_MB = Sammlung(
        trace="Sth Mb",
        groups="Wortschatz|Anonym|Sth Mb",
        kreis="Sth",
        ort="Mb",
    )
    ANON_STH_NB = Sammlung(
        trace="Sth Nb",
        groups="Wortschatz|Anonym|Sth Nb",
        kreis="Sth",
        ort="Nb",
    )
    ANON_STH_NH = Sammlung(
        trace="Sth Nh",
        groups="Wortschatz|Anonym|Sth Nh",
        kreis="Sth",
        ort="Nh",
    )
    ANON_STH_NI = Sammlung(
        trace="Sth Ni",
        groups="Wortschatz|Anonym|Sth Ni",
        kreis="Sth",
        ort="Ni",
    )
    ANON_STH_NO = Sammlung(
        trace="Sth No",
        groups="Wortschatz|Anonym|Sth No",
        kreis="Sth",
        ort="No",
    )
    ANON_STH_NW = Sammlung(
        trace="Sth Nw",
        groups="Wortschatz|Anonym|Sth Nw",
        kreis="Sth",
        ort="Nw",
    )
    ANON_STH_OB = Sammlung(
        trace="Sth Ob",
        groups="Wortschatz|Anonym|Sth Ob",
        kreis="Sth",
        ort="Ob",
    )
    ANON_STH_PH = Sammlung(
        trace="Sth Ph",
        groups="Wortschatz|Anonym|Sth Ph",
        kreis="Sth",
        ort="Ph",
    )
    ANON_STH_PO = Sammlung(
        trace="Sth Po",
        groups="Wortschatz|Anonym|Sth Po",
        kreis="Sth",
        ort="Po",
    )
    ANON_STH_SH = Sammlung(
        trace="Sth Sh",
        groups="Wortschatz|Anonym|Sth Sh",
        kreis="Sth",
        ort="Sh",
    )
    ANON_STH_ST = Sammlung(
        trace="Sth St",
        groups="Wortschatz|Anonym|Sth St",
        kreis="Sth",
        ort="St",
    )
    ANON_STH_SÜ = Sammlung(
        trace="Sth Sü",
        groups="Wortschatz|Anonym|Sth Sü",
        kreis="Sth",
        ort="Sü",
    )
    ANON_STH_VO = Sammlung(
        trace="Sth Vo",
        groups="Wortschatz|Anonym|Sth Vo",
        kreis="Sth",
        ort="Vo",
    )
    ANON_STH_WH = Sammlung(
        trace="Sth Wh",
        groups="Wortschatz|Anonym|Sth Wh",
        kreis="Sth",
        ort="Wh",
    )
    ANON_STH_WI = Sammlung(
        trace="Sth Wi",
        groups="Wortschatz|Anonym|Sth Wi",
        kreis="Sth",
        ort="Wi",
    )
    ANON_STH_WÖ = Sammlung(
        trace="Sth Wö",
        groups="Wortschatz|Anonym|Sth Wö",
        kreis="Sth",
        ort="Wö",
    )
    ANON_TEK_AD = Sammlung(
        trace="Tek Ad",
        groups="Wortschatz|Anonym|Tek Ad",
        kreis="Tek",
        ort="Ad",
    )
    ANON_TEK_AL = Sammlung(
        trace="Tek Al",
        groups="Wortschatz|Anonym|Tek Al",
        kreis="Tek",
        ort="Al",
    )
    ANON_TEK_BB = Sammlung(
        trace="Tek Bb",
        groups="Wortschatz|Anonym|Tek Bb",
        kreis="Tek",
        ort="Bb",
    )
    ANON_TEK_BC = Sammlung(
        trace="Tek Bc",
        groups="Wortschatz|Anonym|Tek Bc",
        kreis="Tek",
        ort="Bc",
    )
    ANON_TEK_BE = Sammlung(
        trace="Tek Be",
        groups="Wortschatz|Anonym|Tek Be",
        kreis="Tek",
        ort="Be",
    )
    ANON_TEK_BI = Sammlung(
        trace="Tek Bi",
        groups="Wortschatz|Anonym|Tek Bi",
        kreis="Tek",
        ort="Bi",
    )
    ANON_TEK_BO = Sammlung(
        trace="Tek Bo",
        groups="Wortschatz|Anonym|Tek Bo",
        kreis="Tek",
        ort="Bo",
    )
    ANON_TEK_BR = Sammlung(
        trace="Tek Br",
        groups="Wortschatz|Anonym|Tek Br",
        kreis="Tek",
        ort="Br",
    )
    ANON_TEK_BÜ = Sammlung(
        trace="Tek Bü",
        groups="Wortschatz|Anonym|Tek Bü",
        kreis="Tek",
        ort="Bü",
    )
    ANON_TEK_DL = Sammlung(
        trace="Tek Dl",
        groups="Wortschatz|Anonym|Tek Dl",
        kreis="Tek",
        ort="Dl",
    )
    ANON_TEK_DÖ = Sammlung(
        trace="Tek Dö",
        groups="Wortschatz|Anonym|Tek Dö",
        kreis="Tek",
        ort="Dö",
    )
    ANON_TEK_DR = Sammlung(
        trace="Tek Dr",
        groups="Wortschatz|Anonym|Tek Dr",
        kreis="Tek",
        ort="Dr",
    )
    ANON_TEK_GH = Sammlung(
        trace="Tek Gh",
        groups="Wortschatz|Anonym|Tek Gh",
        kreis="Tek",
        ort="Gh",
    )
    ANON_TEK_HA = Sammlung(
        trace="Tek Ha",
        groups="Wortschatz|Anonym|Tek Ha",
        kreis="Tek",
        ort="Ha",
    )
    ANON_TEK_HB = Sammlung(
        trace="Tek Hb",
        groups="Wortschatz|Anonym|Tek Hb",
        kreis="Tek",
        ort="Hb",
    )
    ANON_TEK_HD = Sammlung(
        trace="Tek Hd",
        groups="Wortschatz|Anonym|Tek Hd",
        kreis="Tek",
        ort="Hd",
    )
    ANON_TEK_HF = Sammlung(
        trace="Tek Hf",
        groups="Wortschatz|Anonym|Tek Hf",
        kreis="Tek",
        ort="Hf",
    )
    ANON_TEK_HH = Sammlung(
        trace="Tek Hh",
        groups="Wortschatz|Anonym|Tek Hh",
        kreis="Tek",
        ort="Hh",
    )
    ANON_TEK_HO = Sammlung(
        trace="Tek Ho",
        groups="Wortschatz|Anonym|Tek Ho",
        kreis="Tek",
        ort="Ho",
    )
    ANON_TEK_HÖ = Sammlung(
        trace="Tek Hö",
        groups="Wortschatz|Anonym|Tek Hö",
        kreis="Tek",
        ort="Hö",
    )
    ANON_TEK_HP = Sammlung(
        trace="Tek Hp",
        groups="Wortschatz|Anonym|Tek Hp",
        kreis="Tek",
        ort="Hp",
    )
    ANON_TEK_HT = Sammlung(
        trace="Tek Ht",
        groups="Wortschatz|Anonym|Tek Ht",
        kreis="Tek",
        ort="Ht",
    )
    ANON_TEK_HV = Sammlung(
        trace="Tek Hv",
        groups="Wortschatz|Anonym|Tek Hv",
        kreis="Tek",
        ort="Hv",
    )
    ANON_TEK_IB = Sammlung(
        trace="Tek Ib",
        groups="Wortschatz|Anonym|Tek Ib",
        kreis="Tek",
        ort="Ib",
    )
    ANON_TEK_KV = Sammlung(
        trace="Tek Kv",
        groups="Wortschatz|Anonym|Tek Kv",
        kreis="Tek",
        ort="Kv",
    )
    ANON_TEK_LA = Sammlung(
        trace="Tek La",
        groups="Wortschatz|Anonym|Tek La",
        kreis="Tek",
        ort="La",
    )
    ANON_TEK_LB = Sammlung(
        trace="Tek Lb",
        groups="Wortschatz|Anonym|Tek Lb",
        kreis="Tek",
        ort="Lb",
    )
    ANON_TEK_LD = Sammlung(
        trace="Tek Ld",
        groups="Wortschatz|Anonym|Tek Ld",
        kreis="Tek",
        ort="Ld",
    )
    ANON_TEK_LE = Sammlung(
        trace="Tek Le",
        groups="Wortschatz|Anonym|Tek Le",
        kreis="Tek",
        ort="Le",
    )
    ANON_TEK_LH = Sammlung(
        trace="Tek Lh",
        groups="Wortschatz|Anonym|Tek Lh",
        kreis="Tek",
        ort="Lh",
    )
    ANON_TEK_LI = Sammlung(
        trace="Tek Li",
        groups="Wortschatz|Anonym|Tek Li",
        kreis="Tek",
        ort="Li",
    )
    ANON_TEK_LO = Sammlung(
        trace="Tek Lo",
        groups="Wortschatz|Anonym|Tek Lo",
        kreis="Tek",
        ort="Lo",
    )
    ANON_TEK_LT = Sammlung(
        trace="Tek Lt",
        groups="Wortschatz|Anonym|Tek Lt",
        kreis="Tek",
        ort="Lt",
    )
    ANON_TEK_LX = Sammlung(
        trace="Tek Lx",
        groups="Wortschatz|Anonym|Tek Lx",
        kreis="Tek",
        ort="Lx",
    )
    ANON_TEK_ME = Sammlung(
        trace="Tek Me",
        groups="Wortschatz|Anonym|Tek Me",
        kreis="Tek",
        ort="Me",
    )
    ANON_TEK_MT = Sammlung(
        trace="Tek Mt",
        groups="Wortschatz|Anonym|Tek Mt",
        kreis="Tek",
        ort="Mt",
    )
    ANON_TEK_MW = Sammlung(
        trace="Tek Mw",
        groups="Wortschatz|Anonym|Tek Mw",
        kreis="Tek",
        ort="Mw",
    )
    ANON_TEK_NB = Sammlung(
        trace="Tek Nb",
        groups="Wortschatz|Anonym|Tek Nb",
        kreis="Tek",
        ort="Nb",
    )
    ANON_TEK_OB = Sammlung(
        trace="Tek Ob",
        groups="Wortschatz|Anonym|Tek Ob",
        kreis="Tek",
        ort="Ob",
    )
    ANON_TEK_OL = Sammlung(
        trace="Tek Ol",
        groups="Wortschatz|Anonym|Tek Ol",
        kreis="Tek",
        ort="Ol",
    )
    ANON_TEK_OR = Sammlung(
        trace="Tek Or",
        groups="Wortschatz|Anonym|Tek Or",
        kreis="Tek",
        ort="Or",
    )
    ANON_TEK_OS = Sammlung(
        trace="Tek Os",
        groups="Wortschatz|Anonym|Tek Os",
        kreis="Tek",
        ort="Os",
    )
    ANON_TEK_OW = Sammlung(
        trace="Tek Ow",
        groups="Wortschatz|Anonym|Tek Ow",
        kreis="Tek",
        ort="Ow",
    )
    ANON_TEK_PÜ = Sammlung(
        trace="Tek Pü",
        groups="Wortschatz|Anonym|Tek Pü",
        kreis="Tek",
        ort="Pü",
    )
    ANON_TEK_RB = Sammlung(
        trace="Tek Rb",
        groups="Wortschatz|Anonym|Tek Rb",
        kreis="Tek",
        ort="Rb",
    )
    ANON_TEK_RE = Sammlung(
        trace="Tek Re",
        groups="Wortschatz|Anonym|Tek Re",
        kreis="Tek",
        ort="Re",
    )
    ANON_TEK_SB = Sammlung(
        trace="Tek Sb",
        groups="Wortschatz|Anonym|Tek Sb",
        kreis="Tek",
        ort="Sb",
    )
    ANON_TEK_SC = Sammlung(
        trace="Tek Sc",
        groups="Wortschatz|Anonym|Tek Sc",
        kreis="Tek",
        ort="Sc",
    )
    ANON_TEK_SE = Sammlung(
        trace="Tek Se",
        groups="Wortschatz|Anonym|Tek Se",
        kreis="Tek",
        ort="Se",
    )
    ANON_TEK_SL = Sammlung(
        trace="Tek Sl",
        groups="Wortschatz|Anonym|Tek Sl",
        kreis="Tek",
        ort="Sl",
    )
    ANON_TEK_ST = Sammlung(
        trace="Tek St",
        groups="Wortschatz|Anonym|Tek St",
        kreis="Tek",
        ort="St",
    )
    ANON_TEK_TB = Sammlung(
        trace="Tek Tb",
        groups="Wortschatz|Anonym|Tek Tb",
        kreis="Tek",
        ort="Tb",
    )
    ANON_TEK_UF = Sammlung(
        trace="Tek Uf",
        groups="Wortschatz|Anonym|Tek Uf",
        kreis="Tek",
        ort="Uf",
    )
    ANON_TEK_WE = Sammlung(
        trace="Tek We",
        groups="Wortschatz|Anonym|Tek We",
        kreis="Tek",
        ort="We",
    )
    ANON_TEK_WK = Sammlung(
        trace="Tek Wk",
        groups="Wortschatz|Anonym|Tek Wk",
        kreis="Tek",
        ort="Wk",
    )
    ANON_TEK_WT = Sammlung(
        trace="Tek Wt",
        groups="Wortschatz|Anonym|Tek Wt",
        kreis="Tek",
        ort="Wt",
    )
    ANON_UNN_AB = Sammlung(
        trace="Unn Ab",
        groups="Wortschatz|Anonym|Unn Ab",
        kreis="Unn",
        ort="Ab",
    )
    ANON_UNN_AD = Sammlung(
        trace="Unn Ad",
        groups="Wortschatz|Anonym|Unn Ad",
        kreis="Unn",
        ort="Ad",
    )
    ANON_UNN_AF = Sammlung(
        trace="Unn Af",
        groups="Wortschatz|Anonym|Unn Af",
        kreis="Unn",
        ort="Af",
    )
    ANON_UNN_AH = Sammlung(
        trace="Unn Ah",
        groups="Wortschatz|Anonym|Unn Ah",
        kreis="Unn",
        ort="Ah",
    )
    ANON_UNN_AR = Sammlung(
        trace="Unn Ar",
        groups="Wortschatz|Anonym|Unn Ar",
        kreis="Unn",
        ort="Ar",
    )
    ANON_UNN_BE = Sammlung(
        trace="Unn Be",
        groups="Wortschatz|Anonym|Unn Be",
        kreis="Unn",
        ort="Be",
    )
    ANON_UNN_BI = Sammlung(
        trace="Unn Bi",
        groups="Wortschatz|Anonym|Unn Bi",
        kreis="Unn",
        ort="Bi",
    )
    ANON_UNN_BK = Sammlung(
        trace="Unn Bk",
        groups="Wortschatz|Anonym|Unn Bk",
        kreis="Unn",
        ort="Bk",
    )
    ANON_UNN_BR = Sammlung(
        trace="Unn Br",
        groups="Wortschatz|Anonym|Unn Br",
        kreis="Unn",
        ort="Br",
    )
    ANON_UNN_BT = Sammlung(
        trace="Unn Bt",
        groups="Wortschatz|Anonym|Unn Bt",
        kreis="Unn",
        ort="Bt",
    )
    ANON_UNN_DH = Sammlung(
        trace="Unn Dh",
        groups="Wortschatz|Anonym|Unn Dh",
        kreis="Unn",
        ort="Dh",
    )
    ANON_UNN_DL = Sammlung(
        trace="Unn Dl",
        groups="Wortschatz|Anonym|Unn Dl",
        kreis="Unn",
        ort="Dl",
    )
    ANON_UNN_DW = Sammlung(
        trace="Unn Dw",
        groups="Wortschatz|Anonym|Unn Dw",
        kreis="Unn",
        ort="Dw",
    )
    ANON_UNN_FB = Sammlung(
        trace="Unn Fb",
        groups="Wortschatz|Anonym|Unn Fb",
        kreis="Unn",
        ort="Fb",
    )
    ANON_UNN_FH = Sammlung(
        trace="Unn Fh",
        groups="Wortschatz|Anonym|Unn Fh",
        kreis="Unn",
        ort="Fh",
    )
    ANON_UNN_FL = Sammlung(
        trace="Unn Fl",
        groups="Wortschatz|Anonym|Unn Fl",
        kreis="Unn",
        ort="Fl",
    )
    ANON_UNN_FR = Sammlung(
        trace="Unn Fr",
        groups="Wortschatz|Anonym|Unn Fr",
        kreis="Unn",
        ort="Fr",
    )
    ANON_UNN_HA = Sammlung(
        trace="Unn Ha",
        groups="Wortschatz|Anonym|Unn Ha",
        kreis="Unn",
        ort="Ha",
    )
    ANON_UNN_HD = Sammlung(
        trace="Unn Hd",
        groups="Wortschatz|Anonym|Unn Hd",
        kreis="Unn",
        ort="Hd",
    )
    ANON_UNN_HE = Sammlung(
        trace="Unn He",
        groups="Wortschatz|Anonym|Unn He",
        kreis="Unn",
        ort="He",
    )
    ANON_UNN_HH = Sammlung(
        trace="Unn Hh",
        groups="Wortschatz|Anonym|Unn Hh",
        kreis="Unn",
        ort="Hh",
    )
    ANON_UNN_HI = Sammlung(
        trace="Unn Hi",
        groups="Wortschatz|Anonym|Unn Hi",
        kreis="Unn",
        ort="Hi",
    )
    ANON_UNN_HM = Sammlung(
        trace="Unn Hm",
        groups="Wortschatz|Anonym|Unn Hm",
        kreis="Unn",
        ort="Hm",
    )
    ANON_UNN_HN = Sammlung(
        trace="Unn Hn",
        groups="Wortschatz|Anonym|Unn Hn",
        kreis="Unn",
        ort="Hn",
    )
    ANON_UNN_HO = Sammlung(
        trace="Unn Ho",
        groups="Wortschatz|Anonym|Unn Ho",
        kreis="Unn",
        ort="Ho",
    )
    ANON_UNN_HR = Sammlung(
        trace="Unn Hr",
        groups="Wortschatz|Anonym|Unn Hr",
        kreis="Unn",
        ort="Hr",
    )
    ANON_UNN_HW = Sammlung(
        trace="Unn Hw",
        groups="Wortschatz|Anonym|Unn Hw",
        kreis="Unn",
        ort="Hw",
    )
    ANON_UNN_HX = Sammlung(
        trace="Unn Hx",
        groups="Wortschatz|Anonym|Unn Hx",
        kreis="Unn",
        ort="Hx",
    )
    ANON_UNN_KA = Sammlung(
        trace="Unn Ka",
        groups="Wortschatz|Anonym|Unn Ka",
        kreis="Unn",
        ort="Ka",
    )
    ANON_UNN_KB = Sammlung(
        trace="Unn Kb",
        groups="Wortschatz|Anonym|Unn Kb",
        kreis="Unn",
        ort="Kb",
    )
    ANON_UNN_LA = Sammlung(
        trace="Unn La",
        groups="Wortschatz|Anonym|Unn La",
        kreis="Unn",
        ort="La",
    )
    ANON_UNN_LE = Sammlung(
        trace="Unn Le",
        groups="Wortschatz|Anonym|Unn Le",
        kreis="Unn",
        ort="Le",
    )
    ANON_UNN_LN = Sammlung(
        trace="Unn Ln",
        groups="Wortschatz|Anonym|Unn Ln",
        kreis="Unn",
        ort="Ln",
    )
    ANON_UNN_LÜ = Sammlung(
        trace="Unn Lü",
        groups="Wortschatz|Anonym|Unn Lü",
        kreis="Unn",
        ort="Lü",
    )
    ANON_UNN_MA = Sammlung(
        trace="Unn Ma",
        groups="Wortschatz|Anonym|Unn Ma",
        kreis="Unn",
        ort="Ma",
    )
    ANON_UNN_ME = Sammlung(
        trace="Unn Me",
        groups="Wortschatz|Anonym|Unn Me",
        kreis="Unn",
        ort="Me",
    )
    ANON_UNN_MH = Sammlung(
        trace="Unn Mh",
        groups="Wortschatz|Anonym|Unn Mh",
        kreis="Unn",
        ort="Mh",
    )
    ANON_UNN_MS = Sammlung(
        trace="Unn Ms",
        groups="Wortschatz|Anonym|Unn Ms",
        kreis="Unn",
        ort="Ms",
    )
    ANON_UNN_NB = Sammlung(
        trace="Unn Nb",
        groups="Wortschatz|Anonym|Unn Nb",
        kreis="Unn",
        ort="Nb",
    )
    ANON_UNN_ND = Sammlung(
        trace="Unn Nd",
        groups="Wortschatz|Anonym|Unn Nd",
        kreis="Unn",
        ort="Nd",
    )
    ANON_UNN_NI = Sammlung(
        trace="Unn Ni",
        groups="Wortschatz|Anonym|Unn Ni",
        kreis="Unn",
        ort="Ni",
    )
    ANON_UNN_NM = Sammlung(
        trace="Unn Nm",
        groups="Wortschatz|Anonym|Unn Nm",
        kreis="Unn",
        ort="Nm",
    )
    ANON_UNN_OA = Sammlung(
        trace="Unn Oa",
        groups="Wortschatz|Anonym|Unn Oa",
        kreis="Unn",
        ort="Oa",
    )
    ANON_UNN_OB = Sammlung(
        trace="Unn Ob",
        groups="Wortschatz|Anonym|Unn Ob",
        kreis="Unn",
        ort="Ob",
    )
    ANON_UNN_OF = Sammlung(
        trace="Unn Of",
        groups="Wortschatz|Anonym|Unn Of",
        kreis="Unn",
        ort="Of",
    )
    ANON_UNN_OH = Sammlung(
        trace="Unn Oh",
        groups="Wortschatz|Anonym|Unn Oh",
        kreis="Unn",
        ort="Oh",
    )
    ANON_UNN_OÖ = Sammlung(
        trace="Unn Oö",
        groups="Wortschatz|Anonym|Unn Oö",
        kreis="Unn",
        ort="Oö",
    )
    ANON_UNN_OT = Sammlung(
        trace="Unn Ot",
        groups="Wortschatz|Anonym|Unn Ot",
        kreis="Unn",
        ort="Ot",
    )
    ANON_UNN_OV = Sammlung(
        trace="Unn Ov",
        groups="Wortschatz|Anonym|Unn Ov",
        kreis="Unn",
        ort="Ov",
    )
    ANON_UNN_OW = Sammlung(
        trace="Unn Ow",
        groups="Wortschatz|Anonym|Unn Ow",
        kreis="Unn",
        ort="Ow",
    )
    ANON_UNN_PE = Sammlung(
        trace="Unn Pe",
        groups="Wortschatz|Anonym|Unn Pe",
        kreis="Unn",
        ort="Pe",
    )
    ANON_UNN_RO = Sammlung(
        trace="Unn Ro",
        groups="Wortschatz|Anonym|Unn Ro",
        kreis="Unn",
        ort="Ro",
    )
    ANON_UNN_RÜ = Sammlung(
        trace="Unn Rü",
        groups="Wortschatz|Anonym|Unn Rü",
        kreis="Unn",
        ort="Rü",
    )
    ANON_UNN_RY = Sammlung(
        trace="Unn Ry",
        groups="Wortschatz|Anonym|Unn Ry",
        kreis="Unn",
        ort="Ry",
    )
    ANON_UNN_SB = Sammlung(
        trace="Unn Sb",
        groups="Wortschatz|Anonym|Unn Sb",
        kreis="Unn",
        ort="Sb",
    )
    ANON_UNN_SC = Sammlung(
        trace="Unn Sc",
        groups="Wortschatz|Anonym|Unn Sc",
        kreis="Unn",
        ort="Sc",
    )
    ANON_UNN_SD = Sammlung(
        trace="Unn Sd",
        groups="Wortschatz|Anonym|Unn Sd",
        kreis="Unn",
        ort="Sd",
    )
    ANON_UNN_SI = Sammlung(
        trace="Unn Si",
        groups="Wortschatz|Anonym|Unn Si",
        kreis="Unn",
        ort="Si",
    )
    ANON_UNN_SK = Sammlung(
        trace="Unn Sk",
        groups="Wortschatz|Anonym|Unn Sk",
        kreis="Unn",
        ort="Sk",
    )
    ANON_UNN_SÖ = Sammlung(
        trace="Unn Sö",
        groups="Wortschatz|Anonym|Unn Sö",
        kreis="Unn",
        ort="Sö",
    )
    ANON_UNN_ST = Sammlung(
        trace="Unn St",
        groups="Wortschatz|Anonym|Unn St",
        kreis="Unn",
        ort="St",
    )
    ANON_UNN_SÜ = Sammlung(
        trace="Unn Sü",
        groups="Wortschatz|Anonym|Unn Sü",
        kreis="Unn",
        ort="Sü",
    )
    ANON_UNN_ÜL = Sammlung(
        trace="Unn Ül",
        groups="Wortschatz|Anonym|Unn Ül",
        kreis="Unn",
        ort="Ül",
    )
    ANON_UNN_UN = Sammlung(
        trace="Unn Un",
        groups="Wortschatz|Anonym|Unn Un",
        kreis="Unn",
        ort="Un",
    )
    ANON_UNN_ÜN = Sammlung(
        trace="Unn Ün",
        groups="Wortschatz|Anonym|Unn Ün",
        kreis="Unn",
        ort="Ün",
    )
    ANON_UNN_VÖ = Sammlung(
        trace="Unn Vö",
        groups="Wortschatz|Anonym|Unn Vö",
        kreis="Unn",
        ort="Vö",
    )
    ANON_UNN_WB = Sammlung(
        trace="Unn Wb",
        groups="Wortschatz|Anonym|Unn Wb",
        kreis="Unn",
        ort="Wb",
    )
    ANON_UNN_WD = Sammlung(
        trace="Unn Wd",
        groups="Wortschatz|Anonym|Unn Wd",
        kreis="Unn",
        ort="Wd",
    )
    ANON_UNN_WE = Sammlung(
        trace="Unn We",
        groups="Wortschatz|Anonym|Unn We",
        kreis="Unn",
        ort="We",
    )
    ANON_UNN_WH = Sammlung(
        trace="Unn Wh",
        groups="Wortschatz|Anonym|Unn Wh",
        kreis="Unn",
        ort="Wh",
    )
    ANON_UNN_WK = Sammlung(
        trace="Unn Wk",
        groups="Wortschatz|Anonym|Unn Wk",
        kreis="Unn",
        ort="Wk",
    )
    ANON_UNN_WR = Sammlung(
        trace="Unn Wr",
        groups="Wortschatz|Anonym|Unn Wr",
        kreis="Unn",
        ort="Wr",
    )
    ANON_UNN_WS = Sammlung(
        trace="Unn Ws",
        groups="Wortschatz|Anonym|Unn Ws",
        kreis="Unn",
        ort="Ws",
    )
    ANON_VCH_AB = Sammlung(
        trace="Vch Ab",
        groups="Wortschatz|Anonym|Vch Ab",
        kreis="Vch",
        ort="Ab",
    )
    ANON_VCH_AS = Sammlung(
        trace="Vch As",
        groups="Wortschatz|Anonym|Vch As",
        kreis="Vch",
        ort="As",
    )
    ANON_VCH_BA = Sammlung(
        trace="Vch Ba",
        groups="Wortschatz|Anonym|Vch Ba",
        kreis="Vch",
        ort="Ba",
    )
    ANON_VCH_BF = Sammlung(
        trace="Vch Bf",
        groups="Wortschatz|Anonym|Vch Bf",
        kreis="Vch",
        ort="Bf",
    )
    ANON_VCH_BH = Sammlung(
        trace="Vch Bh",
        groups="Wortschatz|Anonym|Vch Bh",
        kreis="Vch",
        ort="Bh",
    )
    ANON_VCH_BI = Sammlung(
        trace="Vch Bi",
        groups="Wortschatz|Anonym|Vch Bi",
        kreis="Vch",
        ort="Bi",
    )
    ANON_VCH_BK = Sammlung(
        trace="Vch Bk",
        groups="Wortschatz|Anonym|Vch Bk",
        kreis="Vch",
        ort="Bk",
    )
    ANON_VCH_BL = Sammlung(
        trace="Vch Bl",
        groups="Wortschatz|Anonym|Vch Bl",
        kreis="Vch",
        ort="Bl",
    )
    ANON_VCH_BO = Sammlung(
        trace="Vch Bo",
        groups="Wortschatz|Anonym|Vch Bo",
        kreis="Vch",
        ort="Bo",
    )
    ANON_VCH_BR = Sammlung(
        trace="Vch Br",
        groups="Wortschatz|Anonym|Vch Br",
        kreis="Vch",
        ort="Br",
    )
    ANON_VCH_DA = Sammlung(
        trace="Vch Da",
        groups="Wortschatz|Anonym|Vch Da",
        kreis="Vch",
        ort="Da",
    )
    ANON_VCH_DD = Sammlung(
        trace="Vch Dd",
        groups="Wortschatz|Anonym|Vch Dd",
        kreis="Vch",
        ort="Dd",
    )
    ANON_VCH_DL = Sammlung(
        trace="Vch Dl",
        groups="Wortschatz|Anonym|Vch Dl",
        kreis="Vch",
        ort="Dl",
    )
    ANON_VCH_DÜ = Sammlung(
        trace="Vch Dü",
        groups="Wortschatz|Anonym|Vch Dü",
        kreis="Vch",
        ort="Dü",
    )
    ANON_VCH_EI = Sammlung(
        trace="Vch Ei",
        groups="Wortschatz|Anonym|Vch Ei",
        kreis="Vch",
        ort="Ei",
    )
    ANON_VCH_EL = Sammlung(
        trace="Vch El",
        groups="Wortschatz|Anonym|Vch El",
        kreis="Vch",
        ort="El",
    )
    ANON_VCH_EN = Sammlung(
        trace="Vch En",
        groups="Wortschatz|Anonym|Vch En",
        kreis="Vch",
        ort="En",
    )
    ANON_VCH_FL = Sammlung(
        trace="Vch Fl",
        groups="Wortschatz|Anonym|Vch Fl",
        kreis="Vch",
        ort="Fl",
    )
    ANON_VCH_GH = Sammlung(
        trace="Vch Gh",
        groups="Wortschatz|Anonym|Vch Gh",
        kreis="Vch",
        ort="Gh",
    )
    ANON_VCH_GO = Sammlung(
        trace="Vch Go",
        groups="Wortschatz|Anonym|Vch Go",
        kreis="Vch",
        ort="Go",
    )
    ANON_VCH_HA = Sammlung(
        trace="Vch Ha",
        groups="Wortschatz|Anonym|Vch Ha",
        kreis="Vch",
        ort="Ha",
    )
    ANON_VCH_HB = Sammlung(
        trace="Vch Hb",
        groups="Wortschatz|Anonym|Vch Hb",
        kreis="Vch",
        ort="Hb",
    )
    ANON_VCH_HD = Sammlung(
        trace="Vch Hd",
        groups="Wortschatz|Anonym|Vch Hd",
        kreis="Vch",
        ort="Hd",
    )
    ANON_VCH_HG = Sammlung(
        trace="Vch Hg",
        groups="Wortschatz|Anonym|Vch Hg",
        kreis="Vch",
        ort="Hg",
    )
    ANON_VCH_HH = Sammlung(
        trace="Vch Hh",
        groups="Wortschatz|Anonym|Vch Hh",
        kreis="Vch",
        ort="Hh",
    )
    ANON_VCH_HI = Sammlung(
        trace="Vch Hi",
        groups="Wortschatz|Anonym|Vch Hi",
        kreis="Vch",
        ort="Hi",
    )
    ANON_VCH_HN = Sammlung(
        trace="Vch Hn",
        groups="Wortschatz|Anonym|Vch Hn",
        kreis="Vch",
        ort="Hn",
    )
    ANON_VCH_HO = Sammlung(
        trace="Vch Ho",
        groups="Wortschatz|Anonym|Vch Ho",
        kreis="Vch",
        ort="Ho",
    )
    ANON_VCH_HS = Sammlung(
        trace="Vch Hs",
        groups="Wortschatz|Anonym|Vch Hs",
        kreis="Vch",
        ort="Hs",
    )
    ANON_VCH_HT = Sammlung(
        trace="Vch Ht",
        groups="Wortschatz|Anonym|Vch Ht",
        kreis="Vch",
        ort="Ht",
    )
    ANON_VCH_HX = Sammlung(
        trace="Vch Hx",
        groups="Wortschatz|Anonym|Vch Hx",
        kreis="Vch",
        ort="Hx",
    )
    ANON_VCH_IH = Sammlung(
        trace="Vch Ih",
        groups="Wortschatz|Anonym|Vch Ih",
        kreis="Vch",
        ort="Ih",
    )
    ANON_VCH_KA = Sammlung(
        trace="Vch Ka",
        groups="Wortschatz|Anonym|Vch Ka",
        kreis="Vch",
        ort="Ka",
    )
    ANON_VCH_KF = Sammlung(
        trace="Vch Kf",
        groups="Wortschatz|Anonym|Vch Kf",
        kreis="Vch",
        ort="Kf",
    )
    ANON_VCH_KL = Sammlung(
        trace="Vch Kl",
        groups="Wortschatz|Anonym|Vch Kl",
        kreis="Vch",
        ort="Kl",
    )
    ANON_VCH_KR = Sammlung(
        trace="Vch Kr",
        groups="Wortschatz|Anonym|Vch Kr",
        kreis="Vch",
        ort="Kr",
    )
    ANON_VCH_LD = Sammlung(
        trace="Vch Ld",
        groups="Wortschatz|Anonym|Vch Ld",
        kreis="Vch",
        ort="Ld",
    )
    ANON_VCH_LF = Sammlung(
        trace="Vch Lf",
        groups="Wortschatz|Anonym|Vch Lf",
        kreis="Vch",
        ort="Lf",
    )
    ANON_VCH_LM = Sammlung(
        trace="Vch Lm",
        groups="Wortschatz|Anonym|Vch Lm",
        kreis="Vch",
        ort="Lm",
    )
    ANON_VCH_LO = Sammlung(
        trace="Vch Lo",
        groups="Wortschatz|Anonym|Vch Lo",
        kreis="Vch",
        ort="Lo",
    )
    ANON_VCH_LU = Sammlung(
        trace="Vch Lu",
        groups="Wortschatz|Anonym|Vch Lu",
        kreis="Vch",
        ort="Lu",
    )
    ANON_VCH_LW = Sammlung(
        trace="Vch Lw",
        groups="Wortschatz|Anonym|Vch Lw",
        kreis="Vch",
        ort="Lw",
    )
    ANON_VCH_MD = Sammlung(
        trace="Vch Md",
        groups="Wortschatz|Anonym|Vch Md",
        kreis="Vch",
        ort="Md",
    )
    ANON_VCH_MÜ = Sammlung(
        trace="Vch Mü",
        groups="Wortschatz|Anonym|Vch Mü",
        kreis="Vch",
        ort="Mü",
    )
    ANON_VCH_ND = Sammlung(
        trace="Vch Nd",
        groups="Wortschatz|Anonym|Vch Nd",
        kreis="Vch",
        ort="Nd",
    )
    ANON_VCH_NH = Sammlung(
        trace="Vch Nh",
        groups="Wortschatz|Anonym|Vch Nh",
        kreis="Vch",
        ort="Nh",
    )
    ANON_VCH_NK = Sammlung(
        trace="Vch Nk",
        groups="Wortschatz|Anonym|Vch Nk",
        kreis="Vch",
        ort="Nk",
    )
    ANON_VCH_NL = Sammlung(
        trace="Vch Nl",
        groups="Wortschatz|Anonym|Vch Nl",
        kreis="Vch",
        ort="Nl",
    )
    ANON_VCH_OE = Sammlung(
        trace="Vch Oe",
        groups="Wortschatz|Anonym|Vch Oe",
        kreis="Vch",
        ort="Oe",
    )
    ANON_VCH_OF = Sammlung(
        trace="Vch Of",
        groups="Wortschatz|Anonym|Vch Of",
        kreis="Vch",
        ort="Of",
    )
    ANON_VCH_OY = Sammlung(
        trace="Vch Oy",
        groups="Wortschatz|Anonym|Vch Oy",
        kreis="Vch",
        ort="Oy",
    )
    ANON_VCH_RD = Sammlung(
        trace="Vch Rd",
        groups="Wortschatz|Anonym|Vch Rd",
        kreis="Vch",
        ort="Rd",
    )
    ANON_VCH_RF = Sammlung(
        trace="Vch Rf",
        groups="Wortschatz|Anonym|Vch Rf",
        kreis="Vch",
        ort="Rf",
    )
    ANON_VCH_SC = Sammlung(
        trace="Vch Sc",
        groups="Wortschatz|Anonym|Vch Sc",
        kreis="Vch",
        ort="Sc",
    )
    ANON_VCH_SH = Sammlung(
        trace="Vch Sh",
        groups="Wortschatz|Anonym|Vch Sh",
        kreis="Vch",
        ort="Sh",
    )
    ANON_VCH_SL = Sammlung(
        trace="Vch Sl",
        groups="Wortschatz|Anonym|Vch Sl",
        kreis="Vch",
        ort="Sl",
    )
    ANON_VCH_ST = Sammlung(
        trace="Vch St",
        groups="Wortschatz|Anonym|Vch St",
        kreis="Vch",
        ort="St",
    )
    ANON_VCH_SW = Sammlung(
        trace="Vch Sw",
        groups="Wortschatz|Anonym|Vch Sw",
        kreis="Vch",
        ort="Sw",
    )
    ANON_VCH_VA = Sammlung(
        trace="Vch Va",
        groups="Wortschatz|Anonym|Vch Va",
        kreis="Vch",
        ort="Va",
    )
    ANON_VCH_VB = Sammlung(
        trace="Vch Vb",
        groups="Wortschatz|Anonym|Vch Vb",
        kreis="Vch",
        ort="Vb",
    )
    ANON_VCH_VE = Sammlung(
        trace="Vch Ve",
        groups="Wortschatz|Anonym|Vch Ve",
        kreis="Vch",
        ort="Ve",
    )
    ANON_VCH_VH = Sammlung(
        trace="Vch Vh",
        groups="Wortschatz|Anonym|Vch Vh",
        kreis="Vch",
        ort="Vh",
    )
    ANON_VCH_VP = Sammlung(
        trace="Vch Vp",
        groups="Wortschatz|Anonym|Vch Vp",
        kreis="Vch",
        ort="Vp",
    )
    ANON_VCH_WE = Sammlung(
        trace="Vch We",
        groups="Wortschatz|Anonym|Vch We",
        kreis="Vch",
        ort="We",
    )
    ANON_VCH_WÖ = Sammlung(
        trace="Vch Wö",
        groups="Wortschatz|Anonym|Vch Wö",
        kreis="Vch",
        ort="Wö",
    )
    ANON_VCH_WU = Sammlung(
        trace="Vch Wu",
        groups="Wortschatz|Anonym|Vch Wu",
        kreis="Vch",
        ort="Wu",
    )
    ANON_WAL_AD = Sammlung(
        trace="Wal Ad",
        groups="Wortschatz|Anonym|Wal Ad",
        kreis="Wal",
        ort="Ad",
    )
    ANON_WAL_AF = Sammlung(
        trace="Wal Af",
        groups="Wortschatz|Anonym|Wal Af",
        kreis="Wal",
        ort="Af",
    )
    ANON_WAL_AL = Sammlung(
        trace="Wal Al",
        groups="Wortschatz|Anonym|Wal Al",
        kreis="Wal",
        ort="Al",
    )
    ANON_WAL_AM = Sammlung(
        trace="Wal Am",
        groups="Wortschatz|Anonym|Wal Am",
        kreis="Wal",
        ort="Am",
    )
    ANON_WAL_AR = Sammlung(
        trace="Wal Ar",
        groups="Wortschatz|Anonym|Wal Ar",
        kreis="Wal",
        ort="Ar",
    )
    ANON_WAL_AS = Sammlung(
        trace="Wal As",
        groups="Wortschatz|Anonym|Wal As",
        kreis="Wal",
        ort="As",
    )
    ANON_WAL_BA = Sammlung(
        trace="Wal Ba",
        groups="Wortschatz|Anonym|Wal Ba",
        kreis="Wal",
        ort="Ba",
    )
    ANON_WAL_BB = Sammlung(
        trace="Wal Bb",
        groups="Wortschatz|Anonym|Wal Bb",
        kreis="Wal",
        ort="Bb",
    )
    ANON_WAL_BD = Sammlung(
        trace="Wal Bd",
        groups="Wortschatz|Anonym|Wal Bd",
        kreis="Wal",
        ort="Bd",
    )
    ANON_WAL_BH = Sammlung(
        trace="Wal Bh",
        groups="Wortschatz|Anonym|Wal Bh",
        kreis="Wal",
        ort="Bh",
    )
    ANON_WAL_BÖ = Sammlung(
        trace="Wal Bö",
        groups="Wortschatz|Anonym|Wal Bö",
        kreis="Wal",
        ort="Bö",
    )
    ANON_WAL_BR = Sammlung(
        trace="Wal Br",
        groups="Wortschatz|Anonym|Wal Br",
        kreis="Wal",
        ort="Br",
    )
    ANON_WAL_BÜ = Sammlung(
        trace="Wal Bü",
        groups="Wortschatz|Anonym|Wal Bü",
        kreis="Wal",
        ort="Bü",
    )
    ANON_WAL_DE = Sammlung(
        trace="Wal De",
        groups="Wortschatz|Anonym|Wal De",
        kreis="Wal",
        ort="De",
    )
    ANON_WAL_DF = Sammlung(
        trace="Wal Df",
        groups="Wortschatz|Anonym|Wal Df",
        kreis="Wal",
        ort="Df",
    )
    ANON_WAL_DH = Sammlung(
        trace="Wal Dh",
        groups="Wortschatz|Anonym|Wal Dh",
        kreis="Wal",
        ort="Dh",
    )
    ANON_WAL_DI = Sammlung(
        trace="Wal Di",
        groups="Wortschatz|Anonym|Wal Di",
        kreis="Wal",
        ort="Di",
    )
    ANON_WAL_DT = Sammlung(
        trace="Wal Dt",
        groups="Wortschatz|Anonym|Wal Dt",
        kreis="Wal",
        ort="Dt",
    )
    ANON_WAL_EI = Sammlung(
        trace="Wal Ei",
        groups="Wortschatz|Anonym|Wal Ei",
        kreis="Wal",
        ort="Ei",
    )
    ANON_WAL_EL = Sammlung(
        trace="Wal El",
        groups="Wortschatz|Anonym|Wal El",
        kreis="Wal",
        ort="El",
    )
    ANON_WAL_EN = Sammlung(
        trace="Wal En",
        groups="Wortschatz|Anonym|Wal En",
        kreis="Wal",
        ort="En",
    )
    ANON_WAL_EP = Sammlung(
        trace="Wal Ep",
        groups="Wortschatz|Anonym|Wal Ep",
        kreis="Wal",
        ort="Ep",
    )
    ANON_WAL_FB = Sammlung(
        trace="Wal Fb",
        groups="Wortschatz|Anonym|Wal Fb",
        kreis="Wal",
        ort="Fb",
    )
    ANON_WAL_FL = Sammlung(
        trace="Wal Fl",
        groups="Wortschatz|Anonym|Wal Fl",
        kreis="Wal",
        ort="Fl",
    )
    ANON_WAL_FR = Sammlung(
        trace="Wal Fr",
        groups="Wortschatz|Anonym|Wal Fr",
        kreis="Wal",
        ort="Fr",
    )
    ANON_WAL_GB = Sammlung(
        trace="Wal Gb",
        groups="Wortschatz|Anonym|Wal Gb",
        kreis="Wal",
        ort="Gb",
    )
    ANON_WAL_GD = Sammlung(
        trace="Wal Gd",
        groups="Wortschatz|Anonym|Wal Gd",
        kreis="Wal",
        ort="Gd",
    )
    ANON_WAL_GH = Sammlung(
        trace="Wal Gh",
        groups="Wortschatz|Anonym|Wal Gh",
        kreis="Wal",
        ort="Gh",
    )
    ANON_WAL_GI = Sammlung(
        trace="Wal Gi",
        groups="Wortschatz|Anonym|Wal Gi",
        kreis="Wal",
        ort="Gi",
    )
    ANON_WAL_HA = Sammlung(
        trace="Wal Ha",
        groups="Wortschatz|Anonym|Wal Ha",
        kreis="Wal",
        ort="Ha",
    )
    ANON_WAL_HB = Sammlung(
        trace="Wal Hb",
        groups="Wortschatz|Anonym|Wal Hb",
        kreis="Wal",
        ort="Hb",
    )
    ANON_WAL_HE = Sammlung(
        trace="Wal He",
        groups="Wortschatz|Anonym|Wal He",
        kreis="Wal",
        ort="He",
    )
    ANON_WAL_HH = Sammlung(
        trace="Wal Hh",
        groups="Wortschatz|Anonym|Wal Hh",
        kreis="Wal",
        ort="Hh",
    )
    ANON_WAL_HI = Sammlung(
        trace="Wal Hi",
        groups="Wortschatz|Anonym|Wal Hi",
        kreis="Wal",
        ort="Hi",
    )
    ANON_WAL_HM = Sammlung(
        trace="Wal Hm",
        groups="Wortschatz|Anonym|Wal Hm",
        kreis="Wal",
        ort="Hm",
    )
    ANON_WAL_HÖ = Sammlung(
        trace="Wal Hö",
        groups="Wortschatz|Anonym|Wal Hö",
        kreis="Wal",
        ort="Hö",
    )
    ANON_WAL_HP = Sammlung(
        trace="Wal Hp",
        groups="Wortschatz|Anonym|Wal Hp",
        kreis="Wal",
        ort="Hp",
    )
    ANON_WAL_HR = Sammlung(
        trace="Wal Hr",
        groups="Wortschatz|Anonym|Wal Hr",
        kreis="Wal",
        ort="Hr",
    )
    ANON_WAL_HS = Sammlung(
        trace="Wal Hs",
        groups="Wortschatz|Anonym|Wal Hs",
        kreis="Wal",
        ort="Hs",
    )
    ANON_WAL_HZ = Sammlung(
        trace="Wal Hz",
        groups="Wortschatz|Anonym|Wal Hz",
        kreis="Wal",
        ort="Hz",
    )
    ANON_WAL_IM = Sammlung(
        trace="Wal Im",
        groups="Wortschatz|Anonym|Wal Im",
        kreis="Wal",
        ort="Im",
    )
    ANON_WAL_IT = Sammlung(
        trace="Wal It",
        groups="Wortschatz|Anonym|Wal It",
        kreis="Wal",
        ort="It",
    )
    ANON_WAL_KB = Sammlung(
        trace="Wal Kb",
        groups="Wortschatz|Anonym|Wal Kb",
        kreis="Wal",
        ort="Kb",
    )
    ANON_WAL_KG = Sammlung(
        trace="Wal Kg",
        groups="Wortschatz|Anonym|Wal Kg",
        kreis="Wal",
        ort="Kg",
    )
    ANON_WAL_KI = Sammlung(
        trace="Wal Ki",
        groups="Wortschatz|Anonym|Wal Ki",
        kreis="Wal",
        ort="Ki",
    )
    ANON_WAL_KÜ = Sammlung(
        trace="Wal Kü",
        groups="Wortschatz|Anonym|Wal Kü",
        kreis="Wal",
        ort="Kü",
    )
    ANON_WAL_LA = Sammlung(
        trace="Wal La",
        groups="Wortschatz|Anonym|Wal La",
        kreis="Wal",
        ort="La",
    )
    ANON_WAL_LB = Sammlung(
        trace="Wal Lb",
        groups="Wortschatz|Anonym|Wal Lb",
        kreis="Wal",
        ort="Lb",
    )
    ANON_WAL_LF = Sammlung(
        trace="Wal Lf",
        groups="Wortschatz|Anonym|Wal Lf",
        kreis="Wal",
        ort="Lf",
    )
    ANON_WAL_LH = Sammlung(
        trace="Wal Lh",
        groups="Wortschatz|Anonym|Wal Lh",
        kreis="Wal",
        ort="Lh",
    )
    ANON_WAL_ME = Sammlung(
        trace="Wal Me",
        groups="Wortschatz|Anonym|Wal Me",
        kreis="Wal",
        ort="Me",
    )
    ANON_WAL_MH = Sammlung(
        trace="Wal Mh",
        groups="Wortschatz|Anonym|Wal Mh",
        kreis="Wal",
        ort="Mh",
    )
    ANON_WAL_ML = Sammlung(
        trace="Wal Ml",
        groups="Wortschatz|Anonym|Wal Ml",
        kreis="Wal",
        ort="Ml",
    )
    ANON_WAL_MN = Sammlung(
        trace="Wal Mn",
        groups="Wortschatz|Anonym|Wal Mn",
        kreis="Wal",
        ort="Mn",
    )
    ANON_WAL_MS = Sammlung(
        trace="Wal Ms",
        groups="Wortschatz|Anonym|Wal Ms",
        kreis="Wal",
        ort="Ms",
    )
    ANON_WAL_MÜ = Sammlung(
        trace="Wal Mü",
        groups="Wortschatz|Anonym|Wal Mü",
        kreis="Wal",
        ort="Mü",
    )
    ANON_WAL_NB = Sammlung(
        trace="Wal Nb",
        groups="Wortschatz|Anonym|Wal Nb",
        kreis="Wal",
        ort="Nb",
    )
    ANON_WAL_NE = Sammlung(
        trace="Wal Ne",
        groups="Wortschatz|Anonym|Wal Ne",
        kreis="Wal",
        ort="Ne",
    )
    ANON_WAL_NF = Sammlung(
        trace="Wal Nf",
        groups="Wortschatz|Anonym|Wal Nf",
        kreis="Wal",
        ort="Nf",
    )
    ANON_WAL_NR = Sammlung(
        trace="Wal Nr",
        groups="Wortschatz|Anonym|Wal Nr",
        kreis="Wal",
        ort="Nr",
    )
    ANON_WAL_NS = Sammlung(
        trace="Wal Ns",
        groups="Wortschatz|Anonym|Wal Ns",
        kreis="Wal",
        ort="Ns",
    )
    ANON_WAL_NW = Sammlung(
        trace="Wal Nw",
        groups="Wortschatz|Anonym|Wal Nw",
        kreis="Wal",
        ort="Nw",
    )
    ANON_WAL_OB = Sammlung(
        trace="Wal Ob",
        groups="Wortschatz|Anonym|Wal Ob",
        kreis="Wal",
        ort="Ob",
    )
    ANON_WAL_OE = Sammlung(
        trace="Wal Oe",
        groups="Wortschatz|Anonym|Wal Oe",
        kreis="Wal",
        ort="Oe",
    )
    ANON_WAL_OT = Sammlung(
        trace="Wal Ot",
        groups="Wortschatz|Anonym|Wal Ot",
        kreis="Wal",
        ort="Ot",
    )
    ANON_WAL_OW = Sammlung(
        trace="Wal Ow",
        groups="Wortschatz|Anonym|Wal Ow",
        kreis="Wal",
        ort="Ow",
    )
    ANON_WAL_RA = Sammlung(
        trace="Wal Ra",
        groups="Wortschatz|Anonym|Wal Ra",
        kreis="Wal",
        ort="Ra",
    )
    ANON_WAL_RE = Sammlung(
        trace="Wal Re",
        groups="Wortschatz|Anonym|Wal Re",
        kreis="Wal",
        ort="Re",
    )
    ANON_WAL_RG = Sammlung(
        trace="Wal Rg",
        groups="Wortschatz|Anonym|Wal Rg",
        kreis="Wal",
        ort="Rg",
    )
    ANON_WAL_RO = Sammlung(
        trace="Wal Ro",
        groups="Wortschatz|Anonym|Wal Ro",
        kreis="Wal",
        ort="Ro",
    )
    ANON_WAL_RT = Sammlung(
        trace="Wal Rt",
        groups="Wortschatz|Anonym|Wal Rt",
        kreis="Wal",
        ort="Rt",
    )
    ANON_WAL_SA = Sammlung(
        trace="Wal Sa",
        groups="Wortschatz|Anonym|Wal Sa",
        kreis="Wal",
        ort="Sa",
    )
    ANON_WAL_SB = Sammlung(
        trace="Wal Sb",
        groups="Wortschatz|Anonym|Wal Sb",
        kreis="Wal",
        ort="Sb",
    )
    ANON_WAL_SC = Sammlung(
        trace="Wal Sc",
        groups="Wortschatz|Anonym|Wal Sc",
        kreis="Wal",
        ort="Sc",
    )
    ANON_WAL_SE = Sammlung(
        trace="Wal Se",
        groups="Wortschatz|Anonym|Wal Se",
        kreis="Wal",
        ort="Se",
    )
    ANON_WAL_SF = Sammlung(
        trace="Wal Sf",
        groups="Wortschatz|Anonym|Wal Sf",
        kreis="Wal",
        ort="Sf",
    )
    ANON_WAL_SM = Sammlung(
        trace="Wal Sm",
        groups="Wortschatz|Anonym|Wal Sm",
        kreis="Wal",
        ort="Sm",
    )
    ANON_WAL_ST = Sammlung(
        trace="Wal St",
        groups="Wortschatz|Anonym|Wal St",
        kreis="Wal",
        ort="St",
    )
    ANON_WAL_SU = Sammlung(
        trace="Wal Su",
        groups="Wortschatz|Anonym|Wal Su",
        kreis="Wal",
        ort="Su",
    )
    ANON_WAL_TI = Sammlung(
        trace="Wal Ti",
        groups="Wortschatz|Anonym|Wal Ti",
        kreis="Wal",
        ort="Ti",
    )
    ANON_WAL_TW = Sammlung(
        trace="Wal Tw",
        groups="Wortschatz|Anonym|Wal Tw",
        kreis="Wal",
        ort="Tw",
    )
    ANON_WAL_US = Sammlung(
        trace="Wal Us",
        groups="Wortschatz|Anonym|Wal Us",
        kreis="Wal",
        ort="Us",
    )
    ANON_WAL_VA = Sammlung(
        trace="Wal Va",
        groups="Wortschatz|Anonym|Wal Va",
        kreis="Wal",
        ort="Va",
    )
    ANON_WAL_VH = Sammlung(
        trace="Wal Vh",
        groups="Wortschatz|Anonym|Wal Vh",
        kreis="Wal",
        ort="Vh",
    )
    ANON_WAL_VÖ = Sammlung(
        trace="Wal Vö",
        groups="Wortschatz|Anonym|Wal Vö",
        kreis="Wal",
        ort="Vö",
    )
    ANON_WAL_WB = Sammlung(
        trace="Wal Wb",
        groups="Wortschatz|Anonym|Wal Wb",
        kreis="Wal",
        ort="Wb",
    )
    ANON_WAL_WD = Sammlung(
        trace="Wal Wd",
        groups="Wortschatz|Anonym|Wal Wd",
        kreis="Wal",
        ort="Wd",
    )
    ANON_WAL_WE = Sammlung(
        trace="Wal We",
        groups="Wortschatz|Anonym|Wal We",
        kreis="Wal",
        ort="We",
    )
    ANON_WAL_WH = Sammlung(
        trace="Wal Wh",
        groups="Wortschatz|Anonym|Wal Wh",
        kreis="Wal",
        ort="Wh",
    )
    ANON_WAL_WI = Sammlung(
        trace="Wal Wi",
        groups="Wortschatz|Anonym|Wal Wi",
        kreis="Wal",
        ort="Wi",
    )
    ANON_WAL_WL = Sammlung(
        trace="Wal Wl",
        groups="Wortschatz|Anonym|Wal Wl",
        kreis="Wal",
        ort="Wl",
    )
    ANON_WAL_WR = Sammlung(
        trace="Wal Wr",
        groups="Wortschatz|Anonym|Wal Wr",
        kreis="Wal",
        ort="Wr",
    )
    ANON_WAL_WT = Sammlung(
        trace="Wal Wt",
        groups="Wortschatz|Anonym|Wal Wt",
        kreis="Wal",
        ort="Wt",
    )
    ANON_WBG_AH = Sammlung(
        trace="Wbg Ah",
        groups="Wortschatz|Anonym|Wbg Ah",
        kreis="Wbg",
        ort="Ah",
    )
    ANON_WBG_BB = Sammlung(
        trace="Wbg Bb",
        groups="Wortschatz|Anonym|Wbg Bb",
        kreis="Wbg",
        ort="Bb",
    )
    ANON_WBG_BG = Sammlung(
        trace="Wbg Bg",
        groups="Wortschatz|Anonym|Wbg Bg",
        kreis="Wbg",
        ort="Bg",
    )
    ANON_WBG_BH = Sammlung(
        trace="Wbg Bh",
        groups="Wortschatz|Anonym|Wbg Bh",
        kreis="Wbg",
        ort="Bh",
    )
    ANON_WBG_BO = Sammlung(
        trace="Wbg Bo",
        groups="Wortschatz|Anonym|Wbg Bo",
        kreis="Wbg",
        ort="Bo",
    )
    ANON_WBG_BÜ = Sammlung(
        trace="Wbg Bü",
        groups="Wortschatz|Anonym|Wbg Bü",
        kreis="Wbg",
        ort="Bü",
    )
    ANON_WBG_DA = Sammlung(
        trace="Wbg Da",
        groups="Wortschatz|Anonym|Wbg Da",
        kreis="Wbg",
        ort="Da",
    )
    ANON_WBG_DB = Sammlung(
        trace="Wbg Db",
        groups="Wortschatz|Anonym|Wbg Db",
        kreis="Wbg",
        ort="Db",
    )
    ANON_WBG_DÖ = Sammlung(
        trace="Wbg Dö",
        groups="Wortschatz|Anonym|Wbg Dö",
        kreis="Wbg",
        ort="Dö",
    )
    ANON_WBG_DS = Sammlung(
        trace="Wbg Ds",
        groups="Wortschatz|Anonym|Wbg Ds",
        kreis="Wbg",
        ort="Ds",
    )
    ANON_WBG_EI = Sammlung(
        trace="Wbg Ei",
        groups="Wortschatz|Anonym|Wbg Ei",
        kreis="Wbg",
        ort="Ei",
    )
    ANON_WBG_EN = Sammlung(
        trace="Wbg En",
        groups="Wortschatz|Anonym|Wbg En",
        kreis="Wbg",
        ort="En",
    )
    ANON_WBG_FÖ = Sammlung(
        trace="Wbg Fö",
        groups="Wortschatz|Anonym|Wbg Fö",
        kreis="Wbg",
        ort="Fö",
    )
    ANON_WBG_FR = Sammlung(
        trace="Wbg Fr",
        groups="Wortschatz|Anonym|Wbg Fr",
        kreis="Wbg",
        ort="Fr",
    )
    ANON_WBG_GE = Sammlung(
        trace="Wbg Ge",
        groups="Wortschatz|Anonym|Wbg Ge",
        kreis="Wbg",
        ort="Ge",
    )
    ANON_WBG_GM = Sammlung(
        trace="Wbg Gm",
        groups="Wortschatz|Anonym|Wbg Gm",
        kreis="Wbg",
        ort="Gm",
    )
    ANON_WBG_GR = Sammlung(
        trace="Wbg Gr",
        groups="Wortschatz|Anonym|Wbg Gr",
        kreis="Wbg",
        ort="Gr",
    )
    ANON_WBG_HA = Sammlung(
        trace="Wbg Ha",
        groups="Wortschatz|Anonym|Wbg Ha",
        kreis="Wbg",
        ort="Ha",
    )
    ANON_WBG_HE = Sammlung(
        trace="Wbg He",
        groups="Wortschatz|Anonym|Wbg He",
        kreis="Wbg",
        ort="He",
    )
    ANON_WBG_HH = Sammlung(
        trace="Wbg Hh",
        groups="Wortschatz|Anonym|Wbg Hh",
        kreis="Wbg",
        ort="Hh",
    )
    ANON_WBG_HO = Sammlung(
        trace="Wbg Ho",
        groups="Wortschatz|Anonym|Wbg Ho",
        kreis="Wbg",
        ort="Ho",
    )
    ANON_WBG_IK = Sammlung(
        trace="Wbg Ik",
        groups="Wortschatz|Anonym|Wbg Ik",
        kreis="Wbg",
        ort="Ik",
    )
    ANON_WBG_KA = Sammlung(
        trace="Wbg Ka",
        groups="Wortschatz|Anonym|Wbg Ka",
        kreis="Wbg",
        ort="Ka",
    )
    ANON_WBG_KÖ = Sammlung(
        trace="Wbg Kö",
        groups="Wortschatz|Anonym|Wbg Kö",
        kreis="Wbg",
        ort="Kö",
    )
    ANON_WBG_KÜ = Sammlung(
        trace="Wbg Kü",
        groups="Wortschatz|Anonym|Wbg Kü",
        kreis="Wbg",
        ort="Kü",
    )
    ANON_WBG_LÖ = Sammlung(
        trace="Wbg Lö",
        groups="Wortschatz|Anonym|Wbg Lö",
        kreis="Wbg",
        ort="Lö",
    )
    ANON_WBG_LÜ = Sammlung(
        trace="Wbg Lü",
        groups="Wortschatz|Anonym|Wbg Lü",
        kreis="Wbg",
        ort="Lü",
    )
    ANON_WBG_ME = Sammlung(
        trace="Wbg Me",
        groups="Wortschatz|Anonym|Wbg Me",
        kreis="Wbg",
        ort="Me",
    )
    ANON_WBG_MU = Sammlung(
        trace="Wbg Mu",
        groups="Wortschatz|Anonym|Wbg Mu",
        kreis="Wbg",
        ort="Mu",
    )
    ANON_WBG_NA = Sammlung(
        trace="Wbg Na",
        groups="Wortschatz|Anonym|Wbg Na",
        kreis="Wbg",
        ort="Na",
    )
    ANON_WBG_NH = Sammlung(
        trace="Wbg Nh",
        groups="Wortschatz|Anonym|Wbg Nh",
        kreis="Wbg",
        ort="Nh",
    )
    ANON_WBG_NI = Sammlung(
        trace="Wbg Ni",
        groups="Wortschatz|Anonym|Wbg Ni",
        kreis="Wbg",
        ort="Ni",
    )
    ANON_WBG_NÖ = Sammlung(
        trace="Wbg Nö",
        groups="Wortschatz|Anonym|Wbg Nö",
        kreis="Wbg",
        ort="Nö",
    )
    ANON_WBG_NZ = Sammlung(
        trace="Wbg Nz",
        groups="Wortschatz|Anonym|Wbg Nz",
        kreis="Wbg",
        ort="Nz",
    )
    ANON_WBG_OS = Sammlung(
        trace="Wbg Os",
        groups="Wortschatz|Anonym|Wbg Os",
        kreis="Wbg",
        ort="Os",
    )
    ANON_WBG_PE = Sammlung(
        trace="Wbg Pe",
        groups="Wortschatz|Anonym|Wbg Pe",
        kreis="Wbg",
        ort="Pe",
    )
    ANON_WBG_RI = Sammlung(
        trace="Wbg Ri",
        groups="Wortschatz|Anonym|Wbg Ri",
        kreis="Wbg",
        ort="Ri",
    )
    ANON_WBG_RÖ = Sammlung(
        trace="Wbg Rö",
        groups="Wortschatz|Anonym|Wbg Rö",
        kreis="Wbg",
        ort="Rö",
    )
    ANON_WBG_SF = Sammlung(
        trace="Wbg Sf",
        groups="Wortschatz|Anonym|Wbg Sf",
        kreis="Wbg",
        ort="Sf",
    )
    ANON_WBG_SH = Sammlung(
        trace="Wbg Sh",
        groups="Wortschatz|Anonym|Wbg Sh",
        kreis="Wbg",
        ort="Sh",
    )
    ANON_WBG_SI = Sammlung(
        trace="Wbg Si",
        groups="Wortschatz|Anonym|Wbg Si",
        kreis="Wbg",
        ort="Si",
    )
    ANON_WBG_SS = Sammlung(
        trace="Wbg Ss",
        groups="Wortschatz|Anonym|Wbg Ss",
        kreis="Wbg",
        ort="Ss",
    )
    ANON_WBG_WB = Sammlung(
        trace="Wbg Wb",
        groups="Wortschatz|Anonym|Wbg Wb",
        kreis="Wbg",
        ort="Wb",
    )
    ANON_WBG_WE = Sammlung(
        trace="Wbg We",
        groups="Wortschatz|Anonym|Wbg We",
        kreis="Wbg",
        ort="We",
    )
    ANON_WBG_WG = Sammlung(
        trace="Wbg Wg",
        groups="Wortschatz|Anonym|Wbg Wg",
        kreis="Wbg",
        ort="Wg",
    )
    ANON_WBG_WI = Sammlung(
        trace="Wbg Wi",
        groups="Wortschatz|Anonym|Wbg Wi",
        kreis="Wbg",
        ort="Wi",
    )
    ANON_WBG_WO = Sammlung(
        trace="Wbg Wo",
        groups="Wortschatz|Anonym|Wbg Wo",
        kreis="Wbg",
        ort="Wo",
    )
    ANON_WDF_BE = Sammlung(
        trace="Wdf Be",
        groups="Wortschatz|Anonym|Wdf Be",
        kreis="Wdf",
        ort="Be",
    )
    ANON_WDF_BL = Sammlung(
        trace="Wdf Bl",
        groups="Wortschatz|Anonym|Wdf Bl",
        kreis="Wdf",
        ort="Bl",
    )
    ANON_WDF_BR = Sammlung(
        trace="Wdf Br",
        groups="Wortschatz|Anonym|Wdf Br",
        kreis="Wdf",
        ort="Br",
    )
    ANON_WDF_BS = Sammlung(
        trace="Wdf Bs",
        groups="Wortschatz|Anonym|Wdf Bs",
        kreis="Wdf",
        ort="Bs",
    )
    ANON_WDF_DM = Sammlung(
        trace="Wdf Dm",
        groups="Wortschatz|Anonym|Wdf Dm",
        kreis="Wdf",
        ort="Dm",
    )
    ANON_WDF_EI = Sammlung(
        trace="Wdf Ei",
        groups="Wortschatz|Anonym|Wdf Ei",
        kreis="Wdf",
        ort="Ei",
    )
    ANON_WDF_EV = Sammlung(
        trace="Wdf Ev",
        groups="Wortschatz|Anonym|Wdf Ev",
        kreis="Wdf",
        ort="Ev",
    )
    ANON_WDF_FR = Sammlung(
        trace="Wdf Fr",
        groups="Wortschatz|Anonym|Wdf Fr",
        kreis="Wdf",
        ort="Fr",
    )
    ANON_WDF_FÜ = Sammlung(
        trace="Wdf Fü",
        groups="Wortschatz|Anonym|Wdf Fü",
        kreis="Wdf",
        ort="Fü",
    )
    ANON_WDF_GF = Sammlung(
        trace="Wdf Gf",
        groups="Wortschatz|Anonym|Wdf Gf",
        kreis="Wdf",
        ort="Gf",
    )
    ANON_WDF_GR = Sammlung(
        trace="Wdf Gr",
        groups="Wortschatz|Anonym|Wdf Gr",
        kreis="Wdf",
        ort="Gr",
    )
    ANON_WDF_HO = Sammlung(
        trace="Wdf Ho",
        groups="Wortschatz|Anonym|Wdf Ho",
        kreis="Wdf",
        ort="Ho",
    )
    ANON_WDF_HW = Sammlung(
        trace="Wdf Hw",
        groups="Wortschatz|Anonym|Wdf Hw",
        kreis="Wdf",
        ort="Hw",
    )
    ANON_WDF_MF = Sammlung(
        trace="Wdf Mf",
        groups="Wortschatz|Anonym|Wdf Mf",
        kreis="Wdf",
        ort="Mf",
    )
    ANON_WDF_MI = Sammlung(
        trace="Wdf Mi",
        groups="Wortschatz|Anonym|Wdf Mi",
        kreis="Wdf",
        ort="Mi",
    )
    ANON_WDF_MÜ = Sammlung(
        trace="Wdf Mü",
        groups="Wortschatz|Anonym|Wdf Mü",
        kreis="Wdf",
        ort="Mü",
    )
    ANON_WDF_OB = Sammlung(
        trace="Wdf Ob",
        groups="Wortschatz|Anonym|Wdf Ob",
        kreis="Wdf",
        ort="Ob",
    )
    ANON_WDF_OF = Sammlung(
        trace="Wdf Of",
        groups="Wortschatz|Anonym|Wdf Of",
        kreis="Wdf",
        ort="Of",
    )
    ANON_WDF_RH = Sammlung(
        trace="Wdf Rh",
        groups="Wortschatz|Anonym|Wdf Rh",
        kreis="Wdf",
        ort="Rh",
    )
    ANON_WDF_SB = Sammlung(
        trace="Wdf Sb",
        groups="Wortschatz|Anonym|Wdf Sb",
        kreis="Wdf",
        ort="Sb",
    )
    ANON_WDF_SC = Sammlung(
        trace="Wdf Sc",
        groups="Wortschatz|Anonym|Wdf Sc",
        kreis="Wdf",
        ort="Sc",
    )
    ANON_WDF_VE = Sammlung(
        trace="Wdf Ve",
        groups="Wortschatz|Anonym|Wdf Ve",
        kreis="Wdf",
        ort="Ve",
    )
    ANON_WDF_VO = Sammlung(
        trace="Wdf Vo",
        groups="Wortschatz|Anonym|Wdf Vo",
        kreis="Wdf",
        ort="Vo",
    )
    ANON_WDF_WD = Sammlung(
        trace="Wdf Wd",
        groups="Wortschatz|Anonym|Wdf Wd",
        kreis="Wdf",
        ort="Wd",
    )
    ANON_WDF_WK = Sammlung(
        trace="Wdf Wk",
        groups="Wortschatz|Anonym|Wdf Wk",
        kreis="Wdf",
        ort="Wk",
    )
    ANON_WIE_AL = Sammlung(
        trace="Wie Al",
        groups="Wortschatz|Anonym|Wie Al",
        kreis="Wie",
        ort="Al",
    )
    ANON_WIE_AV = Sammlung(
        trace="Wie Av",
        groups="Wortschatz|Anonym|Wie Av",
        kreis="Wie",
        ort="Av",
    )
    ANON_WIE_BA = Sammlung(
        trace="Wie Ba",
        groups="Wortschatz|Anonym|Wie Ba",
        kreis="Wie",
        ort="Ba",
    )
    ANON_WIE_BH = Sammlung(
        trace="Wie Bh",
        groups="Wortschatz|Anonym|Wie Bh",
        kreis="Wie",
        ort="Bh",
    )
    ANON_WIE_BL = Sammlung(
        trace="Wie Bl",
        groups="Wortschatz|Anonym|Wie Bl",
        kreis="Wie",
        ort="Bl",
    )
    ANON_WIE_BO = Sammlung(
        trace="Wie Bo",
        groups="Wortschatz|Anonym|Wie Bo",
        kreis="Wie",
        ort="Bo",
    )
    ANON_WIE_BR = Sammlung(
        trace="Wie Br",
        groups="Wortschatz|Anonym|Wie Br",
        kreis="Wie",
        ort="Br",
    )
    ANON_WIE_DR = Sammlung(
        trace="Wie Dr",
        groups="Wortschatz|Anonym|Wie Dr",
        kreis="Wie",
        ort="Dr",
    )
    ANON_WIE_EH = Sammlung(
        trace="Wie Eh",
        groups="Wortschatz|Anonym|Wie Eh",
        kreis="Wie",
        ort="Eh",
    )
    ANON_WIE_EM = Sammlung(
        trace="Wie Em",
        groups="Wortschatz|Anonym|Wie Em",
        kreis="Wie",
        ort="Em",
    )
    ANON_WIE_FR = Sammlung(
        trace="Wie Fr",
        groups="Wortschatz|Anonym|Wie Fr",
        kreis="Wie",
        ort="Fr",
    )
    ANON_WIE_GR = Sammlung(
        trace="Wie Gr",
        groups="Wortschatz|Anonym|Wie Gr",
        kreis="Wie",
        ort="Gr",
    )
    ANON_WIE_GÜ = Sammlung(
        trace="Wie Gü",
        groups="Wortschatz|Anonym|Wie Gü",
        kreis="Wie",
        ort="Gü",
    )
    ANON_WIE_HB = Sammlung(
        trace="Wie Hb",
        groups="Wortschatz|Anonym|Wie Hb",
        kreis="Wie",
        ort="Hb",
    )
    ANON_WIE_HD = Sammlung(
        trace="Wie Hd",
        groups="Wortschatz|Anonym|Wie Hd",
        kreis="Wie",
        ort="Hd",
    )
    ANON_WIE_HO = Sammlung(
        trace="Wie Ho",
        groups="Wortschatz|Anonym|Wie Ho",
        kreis="Wie",
        ort="Ho",
    )
    ANON_WIE_KL = Sammlung(
        trace="Wie Kl",
        groups="Wortschatz|Anonym|Wie Kl",
        kreis="Wie",
        ort="Kl",
    )
    ANON_WIE_KS = Sammlung(
        trace="Wie Ks",
        groups="Wortschatz|Anonym|Wie Ks",
        kreis="Wie",
        ort="Ks",
    )
    ANON_WIE_KZ = Sammlung(
        trace="Wie Kz",
        groups="Wortschatz|Anonym|Wie Kz",
        kreis="Wie",
        ort="Kz",
    )
    ANON_WIE_LB = Sammlung(
        trace="Wie Lb",
        groups="Wortschatz|Anonym|Wie Lb",
        kreis="Wie",
        ort="Lb",
    )
    ANON_WIE_LE = Sammlung(
        trace="Wie Le",
        groups="Wortschatz|Anonym|Wie Le",
        kreis="Wie",
        ort="Le",
    )
    ANON_WIE_LI = Sammlung(
        trace="Wie Li",
        groups="Wortschatz|Anonym|Wie Li",
        kreis="Wie",
        ort="Li",
    )
    ANON_WIE_LK = Sammlung(
        trace="Wie Lk",
        groups="Wortschatz|Anonym|Wie Lk",
        kreis="Wie",
        ort="Lk",
    )
    ANON_WIE_LT = Sammlung(
        trace="Wie Lt",
        groups="Wortschatz|Anonym|Wie Lt",
        kreis="Wie",
        ort="Lt",
    )
    ANON_WIE_MH = Sammlung(
        trace="Wie Mh",
        groups="Wortschatz|Anonym|Wie Mh",
        kreis="Wie",
        ort="Mh",
    )
    ANON_WIE_MÖ = Sammlung(
        trace="Wie Mö",
        groups="Wortschatz|Anonym|Wie Mö",
        kreis="Wie",
        ort="Mö",
    )
    ANON_WIE_NH = Sammlung(
        trace="Wie Nh",
        groups="Wortschatz|Anonym|Wie Nh",
        kreis="Wie",
        ort="Nh",
    )
    ANON_WIE_NK = Sammlung(
        trace="Wie Nk",
        groups="Wortschatz|Anonym|Wie Nk",
        kreis="Wie",
        ort="Nk",
    )
    ANON_WIE_NR = Sammlung(
        trace="Wie Nr",
        groups="Wortschatz|Anonym|Wie Nr",
        kreis="Wie",
        ort="Nr",
    )
    ANON_WIE_ÖW = Sammlung(
        trace="Wie Öw",
        groups="Wortschatz|Anonym|Wie Öw",
        kreis="Wie",
        ort="Öw",
    )
    ANON_WIE_PA = Sammlung(
        trace="Wie Pa",
        groups="Wortschatz|Anonym|Wie Pa",
        kreis="Wie",
        ort="Pa",
    )
    ANON_WIE_PI = Sammlung(
        trace="Wie Pi",
        groups="Wortschatz|Anonym|Wie Pi",
        kreis="Wie",
        ort="Pi",
    )
    ANON_WIE_QH = Sammlung(
        trace="Wie Qh",
        groups="Wortschatz|Anonym|Wie Qh",
        kreis="Wie",
        ort="Qh",
    )
    ANON_WIE_RB = Sammlung(
        trace="Wie Rb",
        groups="Wortschatz|Anonym|Wie Rb",
        kreis="Wie",
        ort="Rb",
    )
    ANON_WIE_RH = Sammlung(
        trace="Wie Rh",
        groups="Wortschatz|Anonym|Wie Rh",
        kreis="Wie",
        ort="Rh",
    )
    ANON_WIE_RÖ = Sammlung(
        trace="Wie Rö",
        groups="Wortschatz|Anonym|Wie Rö",
        kreis="Wie",
        ort="Rö",
    )
    ANON_WIE_SA = Sammlung(
        trace="Wie Sa",
        groups="Wortschatz|Anonym|Wie Sa",
        kreis="Wie",
        ort="Sa",
    )
    ANON_WIE_SE = Sammlung(
        trace="Wie Se",
        groups="Wortschatz|Anonym|Wie Se",
        kreis="Wie",
        ort="Se",
    )
    ANON_WIE_SH = Sammlung(
        trace="Wie Sh",
        groups="Wortschatz|Anonym|Wie Sh",
        kreis="Wie",
        ort="Sh",
    )
    ANON_WIE_SP = Sammlung(
        trace="Wie Sp",
        groups="Wortschatz|Anonym|Wie Sp",
        kreis="Wie",
        ort="Sp",
    )
    ANON_WIE_SU = Sammlung(
        trace="Wie Su",
        groups="Wortschatz|Anonym|Wie Su",
        kreis="Wie",
        ort="Su",
    )
    ANON_WIE_SV = Sammlung(
        trace="Wie Sv",
        groups="Wortschatz|Anonym|Wie Sv",
        kreis="Wie",
        ort="Sv",
    )
    ANON_WIE_VL = Sammlung(
        trace="Wie Vl",
        groups="Wortschatz|Anonym|Wie Vl",
        kreis="Wie",
        ort="Vl",
    )
    ANON_WIE_VS = Sammlung(
        trace="Wie Vs",
        groups="Wortschatz|Anonym|Wie Vs",
        kreis="Wie",
        ort="Vs",
    )
    ANON_WIE_WB = Sammlung(
        trace="Wie Wb",
        groups="Wortschatz|Anonym|Wie Wb",
        kreis="Wie",
        ort="Wb",
    )
    ANON_WIE_WH = Sammlung(
        trace="Wie Wh",
        groups="Wortschatz|Anonym|Wie Wh",
        kreis="Wie",
        ort="Wh",
    )
    ANON_WIE_WW = Sammlung(
        trace="Wie Ww",
        groups="Wortschatz|Anonym|Wie Ww",
        kreis="Wie",
        ort="Ww",
    )
    ANON_WIT_BO = Sammlung(
        trace="Wit Bo",
        groups="Wortschatz|Anonym|Wit Bo",
        kreis="Wit",
        ort="Bo",
    )
    ANON_WIT_HE = Sammlung(
        trace="Wit He",
        groups="Wortschatz|Anonym|Wit He",
        kreis="Wit",
        ort="He",
    )
    ANON_WIT_RH = Sammlung(
        trace="Wit Rh",
        groups="Wortschatz|Anonym|Wit Rh",
        kreis="Wit",
        ort="Rh",
    )
    ANON_WIT_ST = Sammlung(
        trace="Wit St",
        groups="Wortschatz|Anonym|Wit St",
        kreis="Wit",
        ort="St",
    )
    ANON_WIT_WI = Sammlung(
        trace="Wit Wi",
        groups="Wortschatz|Anonym|Wit Wi",
        kreis="Wit",
        ort="Wi",
    )
    ANON_WLG_BH = Sammlung(
        trace="Wlg Bh",
        groups="Wortschatz|Anonym|Wlg Bh",
        kreis="Wlg",
        ort="Bh",
    )
    ANON_WLG_BO = Sammlung(
        trace="Wlg Bo",
        groups="Wortschatz|Anonym|Wlg Bo",
        kreis="Wlg",
        ort="Bo",
    )
    ANON_WLG_BR = Sammlung(
        trace="Wlg Br",
        groups="Wortschatz|Anonym|Wlg Br",
        kreis="Wlg",
        ort="Br",
    )
    ANON_WLG_BX = Sammlung(
        trace="Wlg Bx",
        groups="Wortschatz|Anonym|Wlg Bx",
        kreis="Wlg",
        ort="Bx",
    )
    ANON_WLG_ES = Sammlung(
        trace="Wlg Es",
        groups="Wortschatz|Anonym|Wlg Es",
        kreis="Wlg",
        ort="Es",
    )
    ANON_WLG_HA = Sammlung(
        trace="Wlg Ha",
        groups="Wortschatz|Anonym|Wlg Ha",
        kreis="Wlg",
        ort="Ha",
    )
    ANON_WLG_HB = Sammlung(
        trace="Wlg Hb",
        groups="Wortschatz|Anonym|Wlg Hb",
        kreis="Wlg",
        ort="Hb",
    )
    ANON_WLG_HH = Sammlung(
        trace="Wlg Hh",
        groups="Wortschatz|Anonym|Wlg Hh",
        kreis="Wlg",
        ort="Hh",
    )
    ANON_WLG_HI = Sammlung(
        trace="Wlg Hi",
        groups="Wortschatz|Anonym|Wlg Hi",
        kreis="Wlg",
        ort="Hi",
    )
    ANON_WLG_LI = Sammlung(
        trace="Wlg Li",
        groups="Wortschatz|Anonym|Wlg Li",
        kreis="Wlg",
        ort="Li",
    )
    ANON_WLG_LN = Sammlung(
        trace="Wlg Ln",
        groups="Wortschatz|Anonym|Wlg Ln",
        kreis="Wlg",
        ort="Ln",
    )
    ANON_WLG_LO = Sammlung(
        trace="Wlg Lo",
        groups="Wortschatz|Anonym|Wlg Lo",
        kreis="Wlg",
        ort="Lo",
    )
    ANON_WLG_ME = Sammlung(
        trace="Wlg Me",
        groups="Wortschatz|Anonym|Wlg Me",
        kreis="Wlg",
        ort="Me",
    )
    ANON_WLG_NW = Sammlung(
        trace="Wlg Nw",
        groups="Wortschatz|Anonym|Wlg Nw",
        kreis="Wlg",
        ort="Nw",
    )
    ANON_WLG_OC = Sammlung(
        trace="Wlg Oc",
        groups="Wortschatz|Anonym|Wlg Oc",
        kreis="Wlg",
        ort="Oc",
    )
    ANON_WLG_RA = Sammlung(
        trace="Wlg Ra",
        groups="Wortschatz|Anonym|Wlg Ra",
        kreis="Wlg",
        ort="Ra",
    )
    ANON_WLG_SW = Sammlung(
        trace="Wlg Sw",
        groups="Wortschatz|Anonym|Wlg Sw",
        kreis="Wlg",
        ort="Sw",
    )
    ANON_WLG_VE = Sammlung(
        trace="Wlg Ve",
        groups="Wortschatz|Anonym|Wlg Ve",
        kreis="Wlg",
        ort="Ve",
    )
    ANON_WLG_WD = Sammlung(
        trace="Wlg Wd",
        groups="Wortschatz|Anonym|Wlg Wd",
        kreis="Wlg",
        ort="Wd",
    )
    ANON_WLG_WE = Sammlung(
        trace="Wlg We",
        groups="Wortschatz|Anonym|Wlg We",
        kreis="Wlg",
        ort="We",
    )
    ANON_WLG_WI = Sammlung(
        trace="Wlg Wi",
        groups="Wortschatz|Anonym|Wlg Wi",
        kreis="Wlg",
        ort="Wi",
    )
    ANON_WOL_AH = Sammlung(
        trace="Wol Ah",
        groups="Wortschatz|Anonym|Wol Ah",
        kreis="Wol",
        ort="Ah",
    )
    ANON_WOL_BH = Sammlung(
        trace="Wol Bh",
        groups="Wortschatz|Anonym|Wol Bh",
        kreis="Wol",
        ort="Bh",
    )
    ANON_WOL_EH = Sammlung(
        trace="Wol Eh",
        groups="Wortschatz|Anonym|Wol Eh",
        kreis="Wol",
        ort="Eh",
    )
    ANON_WOL_ER = Sammlung(
        trace="Wol Er",
        groups="Wortschatz|Anonym|Wol Er",
        kreis="Wol",
        ort="Er",
    )
    ANON_WOL_IP = Sammlung(
        trace="Wol Ip",
        groups="Wortschatz|Anonym|Wol Ip",
        kreis="Wol",
        ort="Ip",
    )
    ANON_WOL_NE = Sammlung(
        trace="Wol Ne",
        groups="Wortschatz|Anonym|Wol Ne",
        kreis="Wol",
        ort="Ne",
    )
    ANON_WOL_NF = Sammlung(
        trace="Wol Nf",
        groups="Wortschatz|Anonym|Wol Nf",
        kreis="Wol",
        ort="Nf",
    )
    ANON_WOL_NL = Sammlung(
        trace="Wol Nl",
        groups="Wortschatz|Anonym|Wol Nl",
        kreis="Wol",
        ort="Nl",
    )
    ANON_WOL_OE = Sammlung(
        trace="Wol Oe",
        groups="Wortschatz|Anonym|Wol Oe",
        kreis="Wol",
        ort="Oe",
    )
    ANON_WOL_ÖL = Sammlung(
        trace="Wol Öl",
        groups="Wortschatz|Anonym|Wol Öl",
        kreis="Wol",
        ort="Öl",
    )
    ANON_WOL_VB = Sammlung(
        trace="Wol Vb",
        groups="Wortschatz|Anonym|Wol Vb",
        kreis="Wol",
        ort="Vb",
    )
    ANON_WOL_VO = Sammlung(
        trace="Wol Vo",
        groups="Wortschatz|Anonym|Wol Vo",
        kreis="Wol",
        ort="Vo",
    )
    ANON_WOL_WE = Sammlung(
        trace="Wol We",
        groups="Wortschatz|Anonym|Wol We",
        kreis="Wol",
        ort="We",
    )
    ANON_WOL_WH = Sammlung(
        trace="Wol Wh",
        groups="Wortschatz|Anonym|Wol Wh",
        kreis="Wol",
        ort="Wh",
    )
    ANON_WOL_WO = Sammlung(
        trace="Wol Wo",
        groups="Wortschatz|Anonym|Wol Wo",
        kreis="Wol",
        ort="Wo",
    )
    ANON_WTG_LW = Sammlung(
        trace="Wtg Lw",
        groups="Wortschatz|Anonym|Wtg Lw",
        kreis="Wtg",
        ort="Lw",
    )
    ANON_WTG_NA = Sammlung(
        trace="Wtg Na",
        groups="Wortschatz|Anonym|Wtg Na",
        kreis="Wtg",
        ort="Na",
    )

    ##############################################################
    # Unbestimmte Orte
    ##############################################################
    ANON_AHS_XY = Sammlung(
        trace="Ahs Xy",
        groups="Wortschatz|Anonym|Ahs Xy",
        kreis="Ahs",
        ort="Xy",
    )
    ANON_ALT_XY = Sammlung(
        trace="Alt Xy",
        groups="Wortschatz|Anonym|Alt Xy",
        kreis="Alt",
        ort="Xy",
    )
    ANON_ARN_XY = Sammlung(
        trace="Arn Xy",
        groups="Wortschatz|Anonym|Arn Xy",
        kreis="Arn",
        ort="Xy",
    )
    ANON_ASD_XY = Sammlung(
        trace="Asd Xy",
        groups="Wortschatz|Anonym|Asd Xy",
        kreis="Asd",
        ort="Xy",
    )
    ANON_BBR_XY = Sammlung(
        trace="Bbr Xy",
        groups="Wortschatz|Anonym|Bbr Xy",
        kreis="Bbr",
        ort="Xy",
    )
    ANON_BCH_XY = Sammlung(
        trace="Bch Xy",
        groups="Wortschatz|Anonym|Bch Xy",
        kreis="Bch",
        ort="Xy",
    )
    ANON_BEK_XY = Sammlung(
        trace="Bek Xy",
        groups="Wortschatz|Anonym|Bek Xy",
        kreis="Bek",
        ort="Xy",
    )
    ANON_BEN_XY = Sammlung(
        trace="Ben Xy",
        groups="Wortschatz|Anonym|Ben Xy",
        kreis="Ben",
        ort="Xy",
    )
    ANON_BIE_XY = Sammlung(
        trace="Bie Xy",
        groups="Wortschatz|Anonym|Bie Xy",
        kreis="Bie",
        ort="Xy",
    )
    ANON_BOR_XY = Sammlung(
        trace="Bor Xy",
        groups="Wortschatz|Anonym|Bor Xy",
        kreis="Bor",
        ort="Xy",
    )
    ANON_BRG_XY = Sammlung(
        trace="Brg Xy",
        groups="Wortschatz|Anonym|Brg Xy",
        kreis="Brg",
        ort="Xy",
    )
    ANON_BRI_XY = Sammlung(
        trace="Bri Xy",
        groups="Wortschatz|Anonym|Bri Xy",
        kreis="Bri",
        ort="Xy",
    )
    ANON_BÜK_XY = Sammlung(
        trace="Bük Xy",
        groups="Wortschatz|Anonym|Bük Xy",
        kreis="Bük",
        ort="Xy",
    )
    ANON_BÜR_XY = Sammlung(
        trace="Bür Xy",
        groups="Wortschatz|Anonym|Bür Xy",
        kreis="Bür",
        ort="Xy",
    )
    ANON_DET_XY = Sammlung(
        trace="Det Xy",
        groups="Wortschatz|Anonym|Det Xy",
        kreis="Det",
        ort="Xy",
    )
    ANON_DIE_XY = Sammlung(
        trace="Die Xy",
        groups="Wortschatz|Anonym|Die Xy",
        kreis="Die",
        ort="Xy",
    )
    ANON_DOR_XY = Sammlung(
        trace="Dor Xy",
        groups="Wortschatz|Anonym|Dor Xy",
        kreis="Dor",
        ort="Xy",
    )
    ANON_ENR_XY = Sammlung(
        trace="Enr Xy",
        groups="Wortschatz|Anonym|Enr Xy",
        kreis="Enr",
        ort="Xy",
    )
    ANON_ESS_XY = Sammlung(
        trace="Ess Xy",
        groups="Wortschatz|Anonym|Ess Xy",
        kreis="Ess",
        ort="Xy",
    )
    ANON_GEL_XY = Sammlung(
        trace="Gel Xy",
        groups="Wortschatz|Anonym|Gel Xy",
        kreis="Gel",
        ort="Xy",
    )
    ANON_HAG_XY = Sammlung(
        trace="Hag Xy",
        groups="Wortschatz|Anonym|Hag Xy",
        kreis="Hag",
        ort="Xy",
    )
    ANON_HAL_XY = Sammlung(
        trace="Hal Xy",
        groups="Wortschatz|Anonym|Hal Xy",
        kreis="Hal",
        ort="Xy",
    )
    ANON_HFD_XY = Sammlung(
        trace="Hfd Xy",
        groups="Wortschatz|Anonym|Hfd Xy",
        kreis="Hfd",
        ort="Xy",
    )
    ANON_HÖX_XY = Sammlung(
        trace="Höx Xy",
        groups="Wortschatz|Anonym|Höx Xy",
        kreis="Höx",
        ort="Xy",
    )
    ANON_ISL_XY = Sammlung(
        trace="Isl Xy",
        groups="Wortschatz|Anonym|Isl Xy",
        kreis="Isl",
        ort="Xy",
    )
    ANON_KLO_XY = Sammlung(
        trace="Klo Xy",
        groups="Wortschatz|Anonym|Klo Xy",
        kreis="Klo",
        ort="Xy",
    )
    ANON_KOS_XY = Sammlung(
        trace="Kos Xy",
        groups="Wortschatz|Anonym|Kos Xy",
        kreis="Kos",
        ort="Xy",
    )
    ANON_LEM_XY = Sammlung(
        trace="Lem Xy",
        groups="Wortschatz|Anonym|Lem Xy",
        kreis="Lem",
        ort="Xy",
    )
    ANON_LHS_XY = Sammlung(
        trace="Lhs Xy",
        groups="Wortschatz|Anonym|Lhs Xy",
        kreis="Lhs",
        ort="Xy",
    )
    ANON_LIN_XY = Sammlung(
        trace="Lin Xy",
        groups="Wortschatz|Anonym|Lin Xy",
        kreis="Lin",
        ort="Xy",
    )
    ANON_LST_XY = Sammlung(
        trace="Lst Xy",
        groups="Wortschatz|Anonym|Lst Xy",
        kreis="Lst",
        ort="Xy",
    )
    ANON_LÜB_XY = Sammlung(
        trace="Lüb Xy",
        groups="Wortschatz|Anonym|Lüb Xy",
        kreis="Lüb",
        ort="Xy",
    )
    ANON_MEL_XY = Sammlung(
        trace="Mel Xy",
        groups="Wortschatz|Anonym|Mel Xy",
        kreis="Mel",
        ort="Xy",
    )
    ANON_MEP_XY = Sammlung(
        trace="Mep Xy",
        groups="Wortschatz|Anonym|Mep Xy",
        kreis="Mep",
        ort="Xy",
    )
    ANON_MES_XY = Sammlung(
        trace="Mes Xy",
        groups="Wortschatz|Anonym|Mes Xy",
        kreis="Mes",
        ort="Xy",
    )
    ANON_MIN_XY = Sammlung(
        trace="Min Xy",
        groups="Wortschatz|Anonym|Min Xy",
        kreis="Min",
        ort="Xy",
    )
    ANON_MÜN_XY = Sammlung(
        trace="Mün Xy",
        groups="Wortschatz|Anonym|Mün Xy",
        kreis="Mün",
        ort="Xy",
    )
    ANON_NIE_XY = Sammlung(
        trace="Nie Xy",
        groups="Wortschatz|Anonym|Nie Xy",
        kreis="Nie",
        ort="Xy",
    )
    ANON_OLP_XY = Sammlung(
        trace="Olp Xy",
        groups="Wortschatz|Anonym|Olp Xy",
        kreis="Olp",
        ort="Xy",
    )
    ANON_OSN_XY = Sammlung(
        trace="Osn Xy",
        groups="Wortschatz|Anonym|Osn Xy",
        kreis="Osn",
        ort="Xy",
    )
    ANON_PAD_XY = Sammlung(
        trace="Pad Xy",
        groups="Wortschatz|Anonym|Pad Xy",
        kreis="Pad",
        ort="Xy",
    )
    ANON_REK_XY = Sammlung(
        trace="Rek Xy",
        groups="Wortschatz|Anonym|Rek Xy",
        kreis="Rek",
        ort="Xy",
    )
    ANON_SCH_XY = Sammlung(
        trace="Sch Xy",
        groups="Wortschatz|Anonym|Sch Xy",
        kreis="Sch",
        ort="Xy",
    )
    ANON_SOS_XY = Sammlung(
        trace="Sos Xy",
        groups="Wortschatz|Anonym|Sos Xy",
        kreis="Sos",
        ort="Xy",
    )
    ANON_STF_XY = Sammlung(
        trace="Stf Xy",
        groups="Wortschatz|Anonym|Stf Xy",
        kreis="Stf",
        ort="Xy",
    )
    ANON_STH_XY = Sammlung(
        trace="Sth Xy",
        groups="Wortschatz|Anonym|Sth Xy",
        kreis="Sth",
        ort="Xy",
    )
    ANON_TEK_XY = Sammlung(
        trace="Tek Xy",
        groups="Wortschatz|Anonym|Tek Xy",
        kreis="Tek",
        ort="Xy",
    )
    ANON_UNN_XY = Sammlung(
        trace="Unn Xy",
        groups="Wortschatz|Anonym|Unn Xy",
        kreis="Unn",
        ort="Xy",
    )
    ANON_VCH_XY = Sammlung(
        trace="Vch Xy",
        groups="Wortschatz|Anonym|Vch Xy",
        kreis="Vch",
        ort="Xy",
    )
    ANON_WAL_XY = Sammlung(
        trace="Wal Xy",
        groups="Wortschatz|Anonym|Wal Xy",
        kreis="Wal",
        ort="Xy",
    )
    ANON_WBG_XY = Sammlung(
        trace="Wbg Xy",
        groups="Wortschatz|Anonym|Wbg Xy",
        kreis="Wbg",
        ort="Xy",
    )
    ANON_WDF_XY = Sammlung(
        trace="Wdf Xy",
        groups="Wortschatz|Anonym|Wdf Xy",
        kreis="Wdf",
        ort="Xy",
    )
    ANON_WIE_XY = Sammlung(
        trace="Wie Xy",
        groups="Wortschatz|Anonym|Wie Xy",
        kreis="Wie",
        ort="Xy",
    )
    ANON_WIT_XY = Sammlung(
        trace="Wit Xy",
        groups="Wortschatz|Anonym|Wit Xy",
        kreis="Wit",
        ort="Xy",
    )
    ANON_WLG_XY = Sammlung(
        trace="Wlg Xy",
        groups="Wortschatz|Anonym|Wlg Xy",
        kreis="Wlg",
        ort="Xy",
    )
    ANON_WOL_XY = Sammlung(
        trace="Wol Xy",
        groups="Wortschatz|Anonym|Wol Xy",
        kreis="Wol",
        ort="Xy",
    )
    ANON_WTG_XY = Sammlung(
        trace="Wtg Xy",
        groups="Wortschatz|Anonym|Wtg Xy",
        kreis="Wtg",
        ort="Xy",
    )

    ##############################################################
    # Landschaften
    ##############################################################
    ANON_EMSL = Sammlung(
        trace="Emsl|Emsland",
        groups="Wortschatz|Anonym|Emsland",
        description="Emsland d. h. die Kreise Lingen, Meppen, Aschendorf-Hümmling",
        landschaft="Emsl",
    )
    ANON_HOSNABR = Sammlung(
        trace="HOsnabr|Hochstift Ösnabrück",
        groups="Wortschatz|Anonym|HochstiftÖsnabrück",
        description="das frühere Hochstift Osnabrück, vornehmlich die Kreise Osnabrück, Melle, Wittlage",
        landschaft="HOsnabr",
    )
    ANON_HPADERB = Sammlung(
        trace="HPaderb|Hochstift Paderborn",
        groups="Wortschatz|Anonym|HochstiftPaderborn",
        description="das frühere Hochstift Paderborn, d. h. die Kreise Paderborn, Büren, Warburg, Höxter",
        landschaft="HPaderb",
    )
    ANON_KSAUERL = Sammlung(
        trace="KSauerl|Kölnisches Sauerland",
        groups="Wortschatz|Anonym|KölnischesSauerland",
        description="Kölnisches Sauerland, d. h. die Kreise Arnsberg, Olpe, Meschede, Brilon",
        landschaft="KSauerl",
    )
    ANON_LIP = Sammlung(
        trace="Lip|Lippe",
        groups="Wortschatz|Anonym|Lippe",
        description="das frühere Land Lippe, d. h. die Kreise Detmold und Lemgo",
        landschaft="Lip",
    )
    ANON_MARK = Sammlung(
        trace="Mark|Grafschaft Mark",
        groups="Wortschatz|Anonym|GrafschaftMark",
        description="die frühere Grafschaft Mark",
        landschaft="Mark",
    )
    ANON_MÜNSTERL = Sammlung(
        trace="Münsterl|Münsterland",
        groups="Wortschatz|Anonym|Münsterland",
        description="Münsterland",
        landschaft="Münsterl",
    )
    ANON_RAVENSBG = Sammlung(
        trace="Ravensbg|Grafschaft Ravensberg",
        groups="Wortschatz|Anonym|GrafschaftRavensberg",
        description="die frühere Grafschaft Ravensberg",
        landschaft="Ravensbg",
    )
    ANON_SOLDBG = Sammlung(
        trace="SOldbg|Südoldenburg",
        groups="Wortschatz|Anonym|Südoldenburg",
        description="Südoldenburg, d. h. die Kreise Vechta und Cloppenburg (ohne das Saterland)",
        landschaft="SOldbg",
    )
    ANON_WMÜNSTERL = Sammlung(
        trace="WMünsterl|Westmünsterland",
        groups="Wortschatz|Anonym|Westmünsterland",
        description="Westmünsterland",
        landschaft="WMünsterl",
    )

    ##############################################################
    # Weitere lautschriftliche Klassen
    ##############################################################
    LAUT_AHS_AB = Sammlung(
        trace="Ahs Ab",
        groups="Lautschrift|Ahs Ab",
        kreis="Ahs",
        ort="Ab",
    )
    LAUT_AHS_AE = Sammlung(
        trace="Ahs Ae",
        groups="Lautschrift|Ahs Ae",
        kreis="Ahs",
        ort="Ae",
    )
    LAUT_AHS_AH = Sammlung(
        trace="Ahs Ah",
        groups="Lautschrift|Ahs Ah",
        kreis="Ahs",
        ort="Ah",
    )
    LAUT_AHS_AL = Sammlung(
        trace="Ahs Al",
        groups="Lautschrift|Ahs Al",
        kreis="Ahs",
        ort="Al",
    )
    LAUT_AHS_AM = Sammlung(
        trace="Ahs Am",
        groups="Lautschrift|Ahs Am",
        kreis="Ahs",
        ort="Am",
    )
    LAUT_AHS_AO = Sammlung(
        trace="Ahs Ao",
        groups="Lautschrift|Ahs Ao",
        kreis="Ahs",
        ort="Ao",
    )
    LAUT_AHS_AS = Sammlung(
        trace="Ahs As",
        groups="Lautschrift|Ahs As",
        kreis="Ahs",
        ort="As",
    )
    LAUT_AHS_DÖ = Sammlung(
        trace="Ahs Dö",
        groups="Lautschrift|Ahs Dö",
        kreis="Ahs",
        ort="Dö",
    )
    LAUT_AHS_EG = Sammlung(
        trace="Ahs Eg",
        groups="Lautschrift|Ahs Eg",
        kreis="Ahs",
        ort="Eg",
    )
    LAUT_AHS_EP = Sammlung(
        trace="Ahs Ep",
        groups="Lautschrift|Ahs Ep",
        kreis="Ahs",
        ort="Ep",
    )
    LAUT_AHS_ES = Sammlung(
        trace="Ahs Es",
        groups="Lautschrift|Ahs Es",
        kreis="Ahs",
        ort="Es",
    )
    LAUT_AHS_GE = Sammlung(
        trace="Ahs Ge",
        groups="Lautschrift|Ahs Ge",
        kreis="Ahs",
        ort="Ge",
    )
    LAUT_AHS_GM = Sammlung(
        trace="Ahs Gm",
        groups="Lautschrift|Ahs Gm",
        kreis="Ahs",
        ort="Gm",
    )
    LAUT_AHS_GR = Sammlung(
        trace="Ahs Gr",
        groups="Lautschrift|Ahs Gr",
        kreis="Ahs",
        ort="Gr",
    )
    LAUT_AHS_GS = Sammlung(
        trace="Ahs Gs",
        groups="Lautschrift|Ahs Gs",
        kreis="Ahs",
        ort="Gs",
    )
    LAUT_AHS_GX = Sammlung(
        trace="Ahs Gx",
        groups="Lautschrift|Ahs Gx",
        kreis="Ahs",
        ort="Gx",
    )
    LAUT_AHS_HE = Sammlung(
        trace="Ahs He",
        groups="Lautschrift|Ahs He",
        kreis="Ahs",
        ort="He",
    )
    LAUT_AHS_HG = Sammlung(
        trace="Ahs Hg",
        groups="Lautschrift|Ahs Hg",
        kreis="Ahs",
        ort="Hg",
    )
    LAUT_AHS_HO = Sammlung(
        trace="Ahs Ho",
        groups="Lautschrift|Ahs Ho",
        kreis="Ahs",
        ort="Ho",
    )
    LAUT_AHS_HW = Sammlung(
        trace="Ahs Hw",
        groups="Lautschrift|Ahs Hw",
        kreis="Ahs",
        ort="Hw",
    )
    LAUT_AHS_KM = Sammlung(
        trace="Ahs Km",
        groups="Lautschrift|Ahs Km",
        kreis="Ahs",
        ort="Km",
    )
    LAUT_AHS_KW = Sammlung(
        trace="Ahs Kw",
        groups="Lautschrift|Ahs Kw",
        kreis="Ahs",
        ort="Kw",
    )
    LAUT_AHS_LE = Sammlung(
        trace="Ahs Le",
        groups="Lautschrift|Ahs Le",
        kreis="Ahs",
        ort="Le",
    )
    LAUT_AHS_LÜ = Sammlung(
        trace="Ahs Lü",
        groups="Lautschrift|Ahs Lü",
        kreis="Ahs",
        ort="Lü",
    )
    LAUT_AHS_NB = Sammlung(
        trace="Ahs Nb",
        groups="Lautschrift|Ahs Nb",
        kreis="Ahs",
        ort="Nb",
    )
    LAUT_AHS_ÖD = Sammlung(
        trace="Ahs Öd",
        groups="Lautschrift|Ahs Öd",
        kreis="Ahs",
        ort="Öd",
    )
    LAUT_AHS_OT = Sammlung(
        trace="Ahs Ot",
        groups="Lautschrift|Ahs Ot",
        kreis="Ahs",
        ort="Ot",
    )
    LAUT_AHS_QU = Sammlung(
        trace="Ahs Qu",
        groups="Lautschrift|Ahs Qu",
        kreis="Ahs",
        ort="Qu",
    )
    LAUT_AHS_RB = Sammlung(
        trace="Ahs Rb",
        groups="Lautschrift|Ahs Rb",
        kreis="Ahs",
        ort="Rb",
    )
    LAUT_AHS_SC = Sammlung(
        trace="Ahs Sc",
        groups="Lautschrift|Ahs Sc",
        kreis="Ahs",
        ort="Sc",
    )
    LAUT_AHS_SL = Sammlung(
        trace="Ahs Sl",
        groups="Lautschrift|Ahs Sl",
        kreis="Ahs",
        ort="Sl",
    )
    LAUT_AHS_ST = Sammlung(
        trace="Ahs St",
        groups="Lautschrift|Ahs St",
        kreis="Ahs",
        ort="St",
    )
    LAUT_AHS_VR = Sammlung(
        trace="Ahs Vr",
        groups="Lautschrift|Ahs Vr",
        kreis="Ahs",
        ort="Vr",
    )
    LAUT_AHS_WD = Sammlung(
        trace="Ahs Wd",
        groups="Lautschrift|Ahs Wd",
        kreis="Ahs",
        ort="Wd",
    )
    LAUT_AHS_WE = Sammlung(
        trace="Ahs We",
        groups="Lautschrift|Ahs We",
        kreis="Ahs",
        ort="We",
    )
    LAUT_AHS_WF = Sammlung(
        trace="Ahs Wf",
        groups="Lautschrift|Ahs Wf",
        kreis="Ahs",
        ort="Wf",
    )
    LAUT_AHS_WG = Sammlung(
        trace="Ahs Wg",
        groups="Lautschrift|Ahs Wg",
        kreis="Ahs",
        ort="Wg",
    )
    LAUT_AHS_WR = Sammlung(
        trace="Ahs Wr",
        groups="Lautschrift|Ahs Wr",
        kreis="Ahs",
        ort="Wr",
    )
    LAUT_AHS_WÜ = Sammlung(
        trace="Ahs Wü",
        groups="Lautschrift|Ahs Wü",
        kreis="Ahs",
        ort="Wü",
    )
    LAUT_AHS_WW = Sammlung(
        trace="Ahs Ww",
        groups="Lautschrift|Ahs Ww",
        kreis="Ahs",
        ort="Ww",
    )
    LAUT_AHS_ZW = Sammlung(
        trace="Ahs Zw",
        groups="Lautschrift|Ahs Zw",
        kreis="Ahs",
        ort="Zw",
    )
    LAUT_ALT_AH = Sammlung(
        trace="Alt Ah",
        groups="Lautschrift|Alt Ah",
        kreis="Alt",
        ort="Ah",
    )
    LAUT_ALT_AL = Sammlung(
        trace="Alt Al",
        groups="Lautschrift|Alt Al",
        kreis="Alt",
        ort="Al",
    )
    LAUT_ALT_AM = Sammlung(
        trace="Alt Am",
        groups="Lautschrift|Alt Am",
        kreis="Alt",
        ort="Am",
    )
    LAUT_ALT_AN = Sammlung(
        trace="Alt An",
        groups="Lautschrift|Alt An",
        kreis="Alt",
        ort="An",
    )
    LAUT_ALT_AU = Sammlung(
        trace="Alt Au",
        groups="Lautschrift|Alt Au",
        kreis="Alt",
        ort="Au",
    )
    LAUT_ALT_BÄ = Sammlung(
        trace="Alt Bä",
        groups="Lautschrift|Alt Bä",
        kreis="Alt",
        ort="Bä",
    )
    LAUT_ALT_BB = Sammlung(
        trace="Alt Bb",
        groups="Lautschrift|Alt Bb",
        kreis="Alt",
        ort="Bb",
    )
    LAUT_ALT_BF = Sammlung(
        trace="Alt Bf",
        groups="Lautschrift|Alt Bf",
        kreis="Alt",
        ort="Bf",
    )
    LAUT_ALT_BG = Sammlung(
        trace="Alt Bg",
        groups="Lautschrift|Alt Bg",
        kreis="Alt",
        ort="Bg",
    )
    LAUT_ALT_BH = Sammlung(
        trace="Alt Bh",
        groups="Lautschrift|Alt Bh",
        kreis="Alt",
        ort="Bh",
    )
    LAUT_ALT_BL = Sammlung(
        trace="Alt Bl",
        groups="Lautschrift|Alt Bl",
        kreis="Alt",
        ort="Bl",
    )
    LAUT_ALT_BR = Sammlung(
        trace="Alt Br",
        groups="Lautschrift|Alt Br",
        kreis="Alt",
        ort="Br",
    )
    LAUT_ALT_BW = Sammlung(
        trace="Alt Bw",
        groups="Lautschrift|Alt Bw",
        kreis="Alt",
        ort="Bw",
    )
    LAUT_ALT_DA = Sammlung(
        trace="Alt Da",
        groups="Lautschrift|Alt Da",
        kreis="Alt",
        ort="Da",
    )
    LAUT_ALT_DB = Sammlung(
        trace="Alt Db",
        groups="Lautschrift|Alt Db",
        kreis="Alt",
        ort="Db",
    )
    LAUT_ALT_EB = Sammlung(
        trace="Alt Eb",
        groups="Lautschrift|Alt Eb",
        kreis="Alt",
        ort="Eb",
    )
    LAUT_ALT_EG = Sammlung(
        trace="Alt Eg",
        groups="Lautschrift|Alt Eg",
        kreis="Alt",
        ort="Eg",
    )
    LAUT_ALT_EI = Sammlung(
        trace="Alt Ei",
        groups="Lautschrift|Alt Ei",
        kreis="Alt",
        ort="Ei",
    )
    LAUT_ALT_ES = Sammlung(
        trace="Alt Es",
        groups="Lautschrift|Alt Es",
        kreis="Alt",
        ort="Es",
    )
    LAUT_ALT_EV = Sammlung(
        trace="Alt Ev",
        groups="Lautschrift|Alt Ev",
        kreis="Alt",
        ort="Ev",
    )
    LAUT_ALT_FR = Sammlung(
        trace="Alt Fr",
        groups="Lautschrift|Alt Fr",
        kreis="Alt",
        ort="Fr",
    )
    LAUT_ALT_GL = Sammlung(
        trace="Alt Gl",
        groups="Lautschrift|Alt Gl",
        kreis="Alt",
        ort="Gl",
    )
    LAUT_ALT_GR = Sammlung(
        trace="Alt Gr",
        groups="Lautschrift|Alt Gr",
        kreis="Alt",
        ort="Gr",
    )
    LAUT_ALT_HA = Sammlung(
        trace="Alt Ha",
        groups="Lautschrift|Alt Ha",
        kreis="Alt",
        ort="Ha",
    )
    LAUT_ALT_HB = Sammlung(
        trace="Alt Hb",
        groups="Lautschrift|Alt Hb",
        kreis="Alt",
        ort="Hb",
    )
    LAUT_ALT_HC = Sammlung(
        trace="Alt Hc",
        groups="Lautschrift|Alt Hc",
        kreis="Alt",
        ort="Hc",
    )
    LAUT_ALT_HD = Sammlung(
        trace="Alt Hd",
        groups="Lautschrift|Alt Hd",
        kreis="Alt",
        ort="Hd",
    )
    LAUT_ALT_HE = Sammlung(
        trace="Alt He",
        groups="Lautschrift|Alt He",
        kreis="Alt",
        ort="He",
    )
    LAUT_ALT_HF = Sammlung(
        trace="Alt Hf",
        groups="Lautschrift|Alt Hf",
        kreis="Alt",
        ort="Hf",
    )
    LAUT_ALT_HH = Sammlung(
        trace="Alt Hh",
        groups="Lautschrift|Alt Hh",
        kreis="Alt",
        ort="Hh",
    )
    LAUT_ALT_HI = Sammlung(
        trace="Alt Hi",
        groups="Lautschrift|Alt Hi",
        kreis="Alt",
        ort="Hi",
    )
    LAUT_ALT_HL = Sammlung(
        trace="Alt Hl",
        groups="Lautschrift|Alt Hl",
        kreis="Alt",
        ort="Hl",
    )
    LAUT_ALT_HR = Sammlung(
        trace="Alt Hr",
        groups="Lautschrift|Alt Hr",
        kreis="Alt",
        ort="Hr",
    )
    LAUT_ALT_HS = Sammlung(
        trace="Alt Hs",
        groups="Lautschrift|Alt Hs",
        kreis="Alt",
        ort="Hs",
    )
    LAUT_ALT_HÜ = Sammlung(
        trace="Alt Hü",
        groups="Lautschrift|Alt Hü",
        kreis="Alt",
        ort="Hü",
    )
    LAUT_ALT_HW = Sammlung(
        trace="Alt Hw",
        groups="Lautschrift|Alt Hw",
        kreis="Alt",
        ort="Hw",
    )
    LAUT_ALT_HX = Sammlung(
        trace="Alt Hx",
        groups="Lautschrift|Alt Hx",
        kreis="Alt",
        ort="Hx",
    )
    LAUT_ALT_IM = Sammlung(
        trace="Alt Im",
        groups="Lautschrift|Alt Im",
        kreis="Alt",
        ort="Im",
    )
    LAUT_ALT_IN = Sammlung(
        trace="Alt In",
        groups="Lautschrift|Alt In",
        kreis="Alt",
        ort="In",
    )
    LAUT_ALT_KI = Sammlung(
        trace="Alt Ki",
        groups="Lautschrift|Alt Ki",
        kreis="Alt",
        ort="Ki",
    )
    LAUT_ALT_KL = Sammlung(
        trace="Alt Kl",
        groups="Lautschrift|Alt Kl",
        kreis="Alt",
        ort="Kl",
    )
    LAUT_ALT_LE = Sammlung(
        trace="Alt Le",
        groups="Lautschrift|Alt Le",
        kreis="Alt",
        ort="Le",
    )
    LAUT_ALT_LL = Sammlung(
        trace="Alt Ll",
        groups="Lautschrift|Alt Ll",
        kreis="Alt",
        ort="Ll",
    )
    LAUT_ALT_LÖ = Sammlung(
        trace="Alt Lö",
        groups="Lautschrift|Alt Lö",
        kreis="Alt",
        ort="Lö",
    )
    LAUT_ALT_LS = Sammlung(
        trace="Alt Ls",
        groups="Lautschrift|Alt Ls",
        kreis="Alt",
        ort="Ls",
    )
    LAUT_ALT_LÜ = Sammlung(
        trace="Alt Lü",
        groups="Lautschrift|Alt Lü",
        kreis="Alt",
        ort="Lü",
    )
    LAUT_ALT_ME = Sammlung(
        trace="Alt Me",
        groups="Lautschrift|Alt Me",
        kreis="Alt",
        ort="Me",
    )
    LAUT_ALT_MH = Sammlung(
        trace="Alt Mh",
        groups="Lautschrift|Alt Mh",
        kreis="Alt",
        ort="Mh",
    )
    LAUT_ALT_MR = Sammlung(
        trace="Alt Mr",
        groups="Lautschrift|Alt Mr",
        kreis="Alt",
        ort="Mr",
    )
    LAUT_ALT_MS = Sammlung(
        trace="Alt Ms",
        groups="Lautschrift|Alt Ms",
        kreis="Alt",
        ort="Ms",
    )
    LAUT_ALT_NA = Sammlung(
        trace="Alt Na",
        groups="Lautschrift|Alt Na",
        kreis="Alt",
        ort="Na",
    )
    LAUT_ALT_NE = Sammlung(
        trace="Alt Ne",
        groups="Lautschrift|Alt Ne",
        kreis="Alt",
        ort="Ne",
    )
    LAUT_ALT_NH = Sammlung(
        trace="Alt Nh",
        groups="Lautschrift|Alt Nh",
        kreis="Alt",
        ort="Nh",
    )
    LAUT_ALT_NM = Sammlung(
        trace="Alt Nm",
        groups="Lautschrift|Alt Nm",
        kreis="Alt",
        ort="Nm",
    )
    LAUT_ALT_NR = Sammlung(
        trace="Alt Nr",
        groups="Lautschrift|Alt Nr",
        kreis="Alt",
        ort="Nr",
    )
    LAUT_ALT_NS = Sammlung(
        trace="Alt Ns",
        groups="Lautschrift|Alt Ns",
        kreis="Alt",
        ort="Ns",
    )
    LAUT_ALT_OB = Sammlung(
        trace="Alt Ob",
        groups="Lautschrift|Alt Ob",
        kreis="Alt",
        ort="Ob",
    )
    LAUT_ALT_OE = Sammlung(
        trace="Alt Oe",
        groups="Lautschrift|Alt Oe",
        kreis="Alt",
        ort="Oe",
    )
    LAUT_ALT_ÖH = Sammlung(
        trace="Alt Öh",
        groups="Lautschrift|Alt Öh",
        kreis="Alt",
        ort="Öh",
    )
    LAUT_ALT_OL = Sammlung(
        trace="Alt Ol",
        groups="Lautschrift|Alt Ol",
        kreis="Alt",
        ort="Ol",
    )
    LAUT_ALT_OR = Sammlung(
        trace="Alt Or",
        groups="Lautschrift|Alt Or",
        kreis="Alt",
        ort="Or",
    )
    LAUT_ALT_PB = Sammlung(
        trace="Alt Pb",
        groups="Lautschrift|Alt Pb",
        kreis="Alt",
        ort="Pb",
    )
    LAUT_ALT_PL = Sammlung(
        trace="Alt Pl",
        groups="Lautschrift|Alt Pl",
        kreis="Alt",
        ort="Pl",
    )
    LAUT_ALT_RÄ = Sammlung(
        trace="Alt Rä",
        groups="Lautschrift|Alt Rä",
        kreis="Alt",
        ort="Rä",
    )
    LAUT_ALT_RM = Sammlung(
        trace="Alt Rm",
        groups="Lautschrift|Alt Rm",
        kreis="Alt",
        ort="Rm",
    )
    LAUT_ALT_RÖ = Sammlung(
        trace="Alt Rö",
        groups="Lautschrift|Alt Rö",
        kreis="Alt",
        ort="Rö",
    )
    LAUT_ALT_RS = Sammlung(
        trace="Alt Rs",
        groups="Lautschrift|Alt Rs",
        kreis="Alt",
        ort="Rs",
    )
    LAUT_ALT_RW = Sammlung(
        trace="Alt Rw",
        groups="Lautschrift|Alt Rw",
        kreis="Alt",
        ort="Rw",
    )
    LAUT_ALT_SB = Sammlung(
        trace="Alt Sb",
        groups="Lautschrift|Alt Sb",
        kreis="Alt",
        ort="Sb",
    )
    LAUT_ALT_SC = Sammlung(
        trace="Alt Sc",
        groups="Lautschrift|Alt Sc",
        kreis="Alt",
        ort="Sc",
    )
    LAUT_ALT_SE = Sammlung(
        trace="Alt Se",
        groups="Lautschrift|Alt Se",
        kreis="Alt",
        ort="Se",
    )
    LAUT_ALT_SM = Sammlung(
        trace="Alt Sm",
        groups="Lautschrift|Alt Sm",
        kreis="Alt",
        ort="Sm",
    )
    LAUT_ALT_SR = Sammlung(
        trace="Alt Sr",
        groups="Lautschrift|Alt Sr",
        kreis="Alt",
        ort="Sr",
    )
    LAUT_ALT_SU = Sammlung(
        trace="Alt Su",
        groups="Lautschrift|Alt Su",
        kreis="Alt",
        ort="Su",
    )
    LAUT_ALT_SW = Sammlung(
        trace="Alt Sw",
        groups="Lautschrift|Alt Sw",
        kreis="Alt",
        ort="Sw",
    )
    LAUT_ALT_VA = Sammlung(
        trace="Alt Va",
        groups="Lautschrift|Alt Va",
        kreis="Alt",
        ort="Va",
    )
    LAUT_ALT_VE = Sammlung(
        trace="Alt Ve",
        groups="Lautschrift|Alt Ve",
        kreis="Alt",
        ort="Ve",
    )
    LAUT_ALT_VS = Sammlung(
        trace="Alt Vs",
        groups="Lautschrift|Alt Vs",
        kreis="Alt",
        ort="Vs",
    )
    LAUT_ALT_WD = Sammlung(
        trace="Alt Wd",
        groups="Lautschrift|Alt Wd",
        kreis="Alt",
        ort="Wd",
    )
    LAUT_ALT_WI = Sammlung(
        trace="Alt Wi",
        groups="Lautschrift|Alt Wi",
        kreis="Alt",
        ort="Wi",
    )
    LAUT_ALT_WW = Sammlung(
        trace="Alt Ww",
        groups="Lautschrift|Alt Ww",
        kreis="Alt",
        ort="Ww",
    )
    LAUT_ARN_AD = Sammlung(
        trace="Arn Ad",
        groups="Lautschrift|Arn Ad",
        kreis="Arn",
        ort="Ad",
    )
    LAUT_ARN_AF = Sammlung(
        trace="Arn Af",
        groups="Lautschrift|Arn Af",
        kreis="Arn",
        ort="Af",
    )
    LAUT_ARN_AH = Sammlung(
        trace="Arn Ah",
        groups="Lautschrift|Arn Ah",
        kreis="Arn",
        ort="Ah",
    )
    LAUT_ARN_AL = Sammlung(
        trace="Arn Al",
        groups="Lautschrift|Arn Al",
        kreis="Arn",
        ort="Al",
    )
    LAUT_ARN_AM = Sammlung(
        trace="Arn Am",
        groups="Lautschrift|Arn Am",
        kreis="Arn",
        ort="Am",
    )
    LAUT_ARN_AR = Sammlung(
        trace="Arn Ar",
        groups="Lautschrift|Arn Ar",
        kreis="Arn",
        ort="Ar",
    )
    LAUT_ARN_BA = Sammlung(
        trace="Arn Ba",
        groups="Lautschrift|Arn Ba",
        kreis="Arn",
        ort="Ba",
    )
    LAUT_ARN_BB = Sammlung(
        trace="Arn Bb",
        groups="Lautschrift|Arn Bb",
        kreis="Arn",
        ort="Bb",
    )
    LAUT_ARN_BE = Sammlung(
        trace="Arn Be",
        groups="Lautschrift|Arn Be",
        kreis="Arn",
        ort="Be",
    )
    LAUT_ARN_BH = Sammlung(
        trace="Arn Bh",
        groups="Lautschrift|Arn Bh",
        kreis="Arn",
        ort="Bh",
    )
    LAUT_ARN_BK = Sammlung(
        trace="Arn Bk",
        groups="Lautschrift|Arn Bk",
        kreis="Arn",
        ort="Bk",
    )
    LAUT_ARN_BL = Sammlung(
        trace="Arn Bl",
        groups="Lautschrift|Arn Bl",
        kreis="Arn",
        ort="Bl",
    )
    LAUT_ARN_BM = Sammlung(
        trace="Arn Bm",
        groups="Lautschrift|Arn Bm",
        kreis="Arn",
        ort="Bm",
    )
    LAUT_ARN_BR = Sammlung(
        trace="Arn Br",
        groups="Lautschrift|Arn Br",
        kreis="Arn",
        ort="Br",
    )
    LAUT_ARN_EB = Sammlung(
        trace="Arn Eb",
        groups="Lautschrift|Arn Eb",
        kreis="Arn",
        ort="Eb",
    )
    LAUT_ARN_EC = Sammlung(
        trace="Arn Ec",
        groups="Lautschrift|Arn Ec",
        kreis="Arn",
        ort="Ec",
    )
    LAUT_ARN_EH = Sammlung(
        trace="Arn Eh",
        groups="Lautschrift|Arn Eh",
        kreis="Arn",
        ort="Eh",
    )
    LAUT_ARN_EN = Sammlung(
        trace="Arn En",
        groups="Lautschrift|Arn En",
        kreis="Arn",
        ort="En",
    )
    LAUT_ARN_ES = Sammlung(
        trace="Arn Es",
        groups="Lautschrift|Arn Es",
        kreis="Arn",
        ort="Es",
    )
    LAUT_ARN_FR = Sammlung(
        trace="Arn Fr",
        groups="Lautschrift|Arn Fr",
        kreis="Arn",
        ort="Fr",
    )
    LAUT_ARN_GB = Sammlung(
        trace="Arn Gb",
        groups="Lautschrift|Arn Gb",
        kreis="Arn",
        ort="Gb",
    )
    LAUT_ARN_GR = Sammlung(
        trace="Arn Gr",
        groups="Lautschrift|Arn Gr",
        kreis="Arn",
        ort="Gr",
    )
    LAUT_ARN_HA = Sammlung(
        trace="Arn Ha",
        groups="Lautschrift|Arn Ha",
        kreis="Arn",
        ort="Ha",
    )
    LAUT_ARN_HB = Sammlung(
        trace="Arn Hb",
        groups="Lautschrift|Arn Hb",
        kreis="Arn",
        ort="Hb",
    )
    LAUT_ARN_HE = Sammlung(
        trace="Arn He",
        groups="Lautschrift|Arn He",
        kreis="Arn",
        ort="He",
    )
    LAUT_ARN_HF = Sammlung(
        trace="Arn Hf",
        groups="Lautschrift|Arn Hf",
        kreis="Arn",
        ort="Hf",
    )
    LAUT_ARN_HG = Sammlung(
        trace="Arn Hg",
        groups="Lautschrift|Arn Hg",
        kreis="Arn",
        ort="Hg",
    )
    LAUT_ARN_HÖ = Sammlung(
        trace="Arn Hö",
        groups="Lautschrift|Arn Hö",
        kreis="Arn",
        ort="Hö",
    )
    LAUT_ARN_HÜ = Sammlung(
        trace="Arn Hü",
        groups="Lautschrift|Arn Hü",
        kreis="Arn",
        ort="Hü",
    )
    LAUT_ARN_HZ = Sammlung(
        trace="Arn Hz",
        groups="Lautschrift|Arn Hz",
        kreis="Arn",
        ort="Hz",
    )
    LAUT_ARN_KÜ = Sammlung(
        trace="Arn Kü",
        groups="Lautschrift|Arn Kü",
        kreis="Arn",
        ort="Kü",
    )
    LAUT_ARN_LI = Sammlung(
        trace="Arn Li",
        groups="Lautschrift|Arn Li",
        kreis="Arn",
        ort="Li",
    )
    LAUT_ARN_LS = Sammlung(
        trace="Arn Ls",
        groups="Lautschrift|Arn Ls",
        kreis="Arn",
        ort="Ls",
    )
    LAUT_ARN_MB = Sammlung(
        trace="Arn Mb",
        groups="Lautschrift|Arn Mb",
        kreis="Arn",
        ort="Mb",
    )
    LAUT_ARN_ME = Sammlung(
        trace="Arn Me",
        groups="Lautschrift|Arn Me",
        kreis="Arn",
        ort="Me",
    )
    LAUT_ARN_MH = Sammlung(
        trace="Arn Mh",
        groups="Lautschrift|Arn Mh",
        kreis="Arn",
        ort="Mh",
    )
    LAUT_ARN_MÜ = Sammlung(
        trace="Arn Mü",
        groups="Lautschrift|Arn Mü",
        kreis="Arn",
        ort="Mü",
    )
    LAUT_ARN_NH = Sammlung(
        trace="Arn Nh",
        groups="Lautschrift|Arn Nh",
        kreis="Arn",
        ort="Nh",
    )
    LAUT_ARN_NI = Sammlung(
        trace="Arn Ni",
        groups="Lautschrift|Arn Ni",
        kreis="Arn",
        ort="Ni",
    )
    LAUT_ARN_NN = Sammlung(
        trace="Arn Nn",
        groups="Lautschrift|Arn Nn",
        kreis="Arn",
        ort="Nn",
    )
    LAUT_ARN_OB = Sammlung(
        trace="Arn Ob",
        groups="Lautschrift|Arn Ob",
        kreis="Arn",
        ort="Ob",
    )
    LAUT_ARN_ÖH = Sammlung(
        trace="Arn Öh",
        groups="Lautschrift|Arn Öh",
        kreis="Arn",
        ort="Öh",
    )
    LAUT_ARN_ÖL = Sammlung(
        trace="Arn Öl",
        groups="Lautschrift|Arn Öl",
        kreis="Arn",
        ort="Öl",
    )
    LAUT_ARN_ÖV = Sammlung(
        trace="Arn Öv",
        groups="Lautschrift|Arn Öv",
        kreis="Arn",
        ort="Öv",
    )
    LAUT_ARN_RB = Sammlung(
        trace="Arn Rb",
        groups="Lautschrift|Arn Rb",
        kreis="Arn",
        ort="Rb",
    )
    LAUT_ARN_SF = Sammlung(
        trace="Arn Sf",
        groups="Lautschrift|Arn Sf",
        kreis="Arn",
        ort="Sf",
    )
    LAUT_ARN_SI = Sammlung(
        trace="Arn Si",
        groups="Lautschrift|Arn Si",
        kreis="Arn",
        ort="Si",
    )
    LAUT_ARN_SM = Sammlung(
        trace="Arn Sm",
        groups="Lautschrift|Arn Sm",
        kreis="Arn",
        ort="Sm",
    )
    LAUT_ARN_ST = Sammlung(
        trace="Arn St",
        groups="Lautschrift|Arn St",
        kreis="Arn",
        ort="St",
    )
    LAUT_ARN_SU = Sammlung(
        trace="Arn Su",
        groups="Lautschrift|Arn Su",
        kreis="Arn",
        ort="Su",
    )
    LAUT_ARN_ÜT = Sammlung(
        trace="Arn Üt",
        groups="Lautschrift|Arn Üt",
        kreis="Arn",
        ort="Üt",
    )
    LAUT_ARN_VI = Sammlung(
        trace="Arn Vi",
        groups="Lautschrift|Arn Vi",
        kreis="Arn",
        ort="Vi",
    )
    LAUT_ARN_VO = Sammlung(
        trace="Arn Vo",
        groups="Lautschrift|Arn Vo",
        kreis="Arn",
        ort="Vo",
    )
    LAUT_ARN_VW = Sammlung(
        trace="Arn Vw",
        groups="Lautschrift|Arn Vw",
        kreis="Arn",
        ort="Vw",
    )
    LAUT_ARN_WA = Sammlung(
        trace="Arn Wa",
        groups="Lautschrift|Arn Wa",
        kreis="Arn",
        ort="Wa",
    )
    LAUT_ARN_WD = Sammlung(
        trace="Arn Wd",
        groups="Lautschrift|Arn Wd",
        kreis="Arn",
        ort="Wd",
    )
    LAUT_ARN_WE = Sammlung(
        trace="Arn We",
        groups="Lautschrift|Arn We",
        kreis="Arn",
        ort="We",
    )
    LAUT_ARN_WF = Sammlung(
        trace="Arn Wf",
        groups="Lautschrift|Arn Wf",
        kreis="Arn",
        ort="Wf",
    )
    LAUT_ARN_WH = Sammlung(
        trace="Arn Wh",
        groups="Lautschrift|Arn Wh",
        kreis="Arn",
        ort="Wh",
    )
    LAUT_ARN_WW = Sammlung(
        trace="Arn Ww",
        groups="Lautschrift|Arn Ww",
        kreis="Arn",
        ort="Ww",
    )
    LAUT_ASD_AD = Sammlung(
        trace="Asd Ad",
        groups="Lautschrift|Asd Ad",
        kreis="Asd",
        ort="Ad",
    )
    LAUT_ASD_AL = Sammlung(
        trace="Asd Al",
        groups="Lautschrift|Asd Al",
        kreis="Asd",
        ort="Al",
    )
    LAUT_ASD_BB = Sammlung(
        trace="Asd Bb",
        groups="Lautschrift|Asd Bb",
        kreis="Asd",
        ort="Bb",
    )
    LAUT_ASD_BC = Sammlung(
        trace="Asd Bc",
        groups="Lautschrift|Asd Bc",
        kreis="Asd",
        ort="Bc",
    )
    LAUT_ASD_BE = Sammlung(
        trace="Asd Be",
        groups="Lautschrift|Asd Be",
        kreis="Asd",
        ort="Be",
    )
    LAUT_ASD_BH = Sammlung(
        trace="Asd Bh",
        groups="Lautschrift|Asd Bh",
        kreis="Asd",
        ort="Bh",
    )
    LAUT_ASD_BK = Sammlung(
        trace="Asd Bk",
        groups="Lautschrift|Asd Bk",
        kreis="Asd",
        ort="Bk",
    )
    LAUT_ASD_BM = Sammlung(
        trace="Asd Bm",
        groups="Lautschrift|Asd Bm",
        kreis="Asd",
        ort="Bm",
    )
    LAUT_ASD_BO = Sammlung(
        trace="Asd Bo",
        groups="Lautschrift|Asd Bo",
        kreis="Asd",
        ort="Bo",
    )
    LAUT_ASD_BÖ = Sammlung(
        trace="Asd Bö",
        groups="Lautschrift|Asd Bö",
        kreis="Asd",
        ort="Bö",
    )
    LAUT_ASD_BR = Sammlung(
        trace="Asd Br",
        groups="Lautschrift|Asd Br",
        kreis="Asd",
        ort="Br",
    )
    LAUT_ASD_BW = Sammlung(
        trace="Asd Bw",
        groups="Lautschrift|Asd Bw",
        kreis="Asd",
        ort="Bw",
    )
    LAUT_ASD_DE = Sammlung(
        trace="Asd De",
        groups="Lautschrift|Asd De",
        kreis="Asd",
        ort="De",
    )
    LAUT_ASD_DÖ = Sammlung(
        trace="Asd Dö",
        groups="Lautschrift|Asd Dö",
        kreis="Asd",
        ort="Dö",
    )
    LAUT_ASD_DÜ = Sammlung(
        trace="Asd Dü",
        groups="Lautschrift|Asd Dü",
        kreis="Asd",
        ort="Dü",
    )
    LAUT_ASD_EI = Sammlung(
        trace="Asd Ei",
        groups="Lautschrift|Asd Ei",
        kreis="Asd",
        ort="Ei",
    )
    LAUT_ASD_ES = Sammlung(
        trace="Asd Es",
        groups="Lautschrift|Asd Es",
        kreis="Asd",
        ort="Es",
    )
    LAUT_ASD_FB = Sammlung(
        trace="Asd Fb",
        groups="Lautschrift|Asd Fb",
        kreis="Asd",
        ort="Fb",
    )
    LAUT_ASD_GB = Sammlung(
        trace="Asd Gb",
        groups="Lautschrift|Asd Gb",
        kreis="Asd",
        ort="Gb",
    )
    LAUT_ASD_HA = Sammlung(
        trace="Asd Ha",
        groups="Lautschrift|Asd Ha",
        kreis="Asd",
        ort="Ha",
    )
    LAUT_ASD_HB = Sammlung(
        trace="Asd Hb",
        groups="Lautschrift|Asd Hb",
        kreis="Asd",
        ort="Hb",
    )
    LAUT_ASD_HE = Sammlung(
        trace="Asd He",
        groups="Lautschrift|Asd He",
        kreis="Asd",
        ort="He",
    )
    LAUT_ASD_HI = Sammlung(
        trace="Asd Hi",
        groups="Lautschrift|Asd Hi",
        kreis="Asd",
        ort="Hi",
    )
    LAUT_ASD_HÜ = Sammlung(
        trace="Asd Hü",
        groups="Lautschrift|Asd Hü",
        kreis="Asd",
        ort="Hü",
    )
    LAUT_ASD_LA = Sammlung(
        trace="Asd La",
        groups="Lautschrift|Asd La",
        kreis="Asd",
        ort="La",
    )
    LAUT_ASD_LE = Sammlung(
        trace="Asd Le",
        groups="Lautschrift|Asd Le",
        kreis="Asd",
        ort="Le",
    )
    LAUT_ASD_LN = Sammlung(
        trace="Asd Ln",
        groups="Lautschrift|Asd Ln",
        kreis="Asd",
        ort="Ln",
    )
    LAUT_ASD_LO = Sammlung(
        trace="Asd Lo",
        groups="Lautschrift|Asd Lo",
        kreis="Asd",
        ort="Lo",
    )
    LAUT_ASD_ME = Sammlung(
        trace="Asd Me",
        groups="Lautschrift|Asd Me",
        kreis="Asd",
        ort="Me",
    )
    LAUT_ASD_NB = Sammlung(
        trace="Asd Nb",
        groups="Lautschrift|Asd Nb",
        kreis="Asd",
        ort="Nb",
    )
    LAUT_ASD_ND = Sammlung(
        trace="Asd Nd",
        groups="Lautschrift|Asd Nd",
        kreis="Asd",
        ort="Nd",
    )
    LAUT_ASD_NE = Sammlung(
        trace="Asd Ne",
        groups="Lautschrift|Asd Ne",
        kreis="Asd",
        ort="Ne",
    )
    LAUT_ASD_NH = Sammlung(
        trace="Asd Nh",
        groups="Lautschrift|Asd Nh",
        kreis="Asd",
        ort="Nh",
    )
    LAUT_ASD_NI = Sammlung(
        trace="Asd Ni",
        groups="Lautschrift|Asd Ni",
        kreis="Asd",
        ort="Ni",
    )
    LAUT_ASD_NL = Sammlung(
        trace="Asd Nl",
        groups="Lautschrift|Asd Nl",
        kreis="Asd",
        ort="Nl",
    )
    LAUT_ASD_NR = Sammlung(
        trace="Asd Nr",
        groups="Lautschrift|Asd Nr",
        kreis="Asd",
        ort="Nr",
    )
    LAUT_ASD_NS = Sammlung(
        trace="Asd Ns",
        groups="Lautschrift|Asd Ns",
        kreis="Asd",
        ort="Ns",
    )
    LAUT_ASD_NV = Sammlung(
        trace="Asd Nv",
        groups="Lautschrift|Asd Nv",
        kreis="Asd",
        ort="Nv",
    )
    LAUT_ASD_NW = Sammlung(
        trace="Asd Nw",
        groups="Lautschrift|Asd Nw",
        kreis="Asd",
        ort="Nw",
    )
    LAUT_ASD_OL = Sammlung(
        trace="Asd Ol",
        groups="Lautschrift|Asd Ol",
        kreis="Asd",
        ort="Ol",
    )
    LAUT_ASD_PB = Sammlung(
        trace="Asd Pb",
        groups="Lautschrift|Asd Pb",
        kreis="Asd",
        ort="Pb",
    )
    LAUT_ASD_RD = Sammlung(
        trace="Asd Rd",
        groups="Lautschrift|Asd Rd",
        kreis="Asd",
        ort="Rd",
    )
    LAUT_ASD_RH = Sammlung(
        trace="Asd Rh",
        groups="Lautschrift|Asd Rh",
        kreis="Asd",
        ort="Rh",
    )
    LAUT_ASD_SÖ = Sammlung(
        trace="Asd Sö",
        groups="Lautschrift|Asd Sö",
        kreis="Asd",
        ort="Sö",
    )
    LAUT_ASD_SP = Sammlung(
        trace="Asd Sp",
        groups="Lautschrift|Asd Sp",
        kreis="Asd",
        ort="Sp",
    )
    LAUT_ASD_ST = Sammlung(
        trace="Asd St",
        groups="Lautschrift|Asd St",
        kreis="Asd",
        ort="St",
    )
    LAUT_ASD_SU = Sammlung(
        trace="Asd Su",
        groups="Lautschrift|Asd Su",
        kreis="Asd",
        ort="Su",
    )
    LAUT_ASD_SW = Sammlung(
        trace="Asd Sw",
        groups="Lautschrift|Asd Sw",
        kreis="Asd",
        ort="Sw",
    )
    LAUT_ASD_TD = Sammlung(
        trace="Asd Td",
        groups="Lautschrift|Asd Td",
        kreis="Asd",
        ort="Td",
    )
    LAUT_ASD_VR = Sammlung(
        trace="Asd Vr",
        groups="Lautschrift|Asd Vr",
        kreis="Asd",
        ort="Vr",
    )
    LAUT_ASD_WA = Sammlung(
        trace="Asd Wa",
        groups="Lautschrift|Asd Wa",
        kreis="Asd",
        ort="Wa",
    )
    LAUT_ASD_WC = Sammlung(
        trace="Asd Wc",
        groups="Lautschrift|Asd Wc",
        kreis="Asd",
        ort="Wc",
    )
    LAUT_ASD_WE = Sammlung(
        trace="Asd We",
        groups="Lautschrift|Asd We",
        kreis="Asd",
        ort="We",
    )
    LAUT_ASD_WI = Sammlung(
        trace="Asd Wi",
        groups="Lautschrift|Asd Wi",
        kreis="Asd",
        ort="Wi",
    )
    LAUT_ASD_WL = Sammlung(
        trace="Asd Wl",
        groups="Lautschrift|Asd Wl",
        kreis="Asd",
        ort="Wl",
    )
    LAUT_ASD_WM = Sammlung(
        trace="Asd Wm",
        groups="Lautschrift|Asd Wm",
        kreis="Asd",
        ort="Wm",
    )
    LAUT_ASD_WS = Sammlung(
        trace="Asd Ws",
        groups="Lautschrift|Asd Ws",
        kreis="Asd",
        ort="Ws",
    )
    LAUT_BBR_AC = Sammlung(
        trace="Bbr Ac",
        groups="Lautschrift|Bbr Ac",
        kreis="Bbr",
        ort="Ac",
    )
    LAUT_BBR_AD = Sammlung(
        trace="Bbr Ad",
        groups="Lautschrift|Bbr Ad",
        kreis="Bbr",
        ort="Ad",
    )
    LAUT_BBR_AH = Sammlung(
        trace="Bbr Ah",
        groups="Lautschrift|Bbr Ah",
        kreis="Bbr",
        ort="Ah",
    )
    LAUT_BBR_AL = Sammlung(
        trace="Bbr Al",
        groups="Lautschrift|Bbr Al",
        kreis="Bbr",
        ort="Al",
    )
    LAUT_BBR_AN = Sammlung(
        trace="Bbr An",
        groups="Lautschrift|Bbr An",
        kreis="Bbr",
        ort="An",
    )
    LAUT_BBR_AS = Sammlung(
        trace="Bbr As",
        groups="Lautschrift|Bbr As",
        kreis="Bbr",
        ort="As",
    )
    LAUT_BBR_BA = Sammlung(
        trace="Bbr Ba",
        groups="Lautschrift|Bbr Ba",
        kreis="Bbr",
        ort="Ba",
    )
    LAUT_BBR_BE = Sammlung(
        trace="Bbr Be",
        groups="Lautschrift|Bbr Be",
        kreis="Bbr",
        ort="Be",
    )
    LAUT_BBR_BG = Sammlung(
        trace="Bbr Bg",
        groups="Lautschrift|Bbr Bg",
        kreis="Bbr",
        ort="Bg",
    )
    LAUT_BBR_BH = Sammlung(
        trace="Bbr Bh",
        groups="Lautschrift|Bbr Bh",
        kreis="Bbr",
        ort="Bh",
    )
    LAUT_BBR_BI = Sammlung(
        trace="Bbr Bi",
        groups="Lautschrift|Bbr Bi",
        kreis="Bbr",
        ort="Bi",
    )
    LAUT_BBR_BK = Sammlung(
        trace="Bbr Bk",
        groups="Lautschrift|Bbr Bk",
        kreis="Bbr",
        ort="Bk",
    )
    LAUT_BBR_BO = Sammlung(
        trace="Bbr Bo",
        groups="Lautschrift|Bbr Bo",
        kreis="Bbr",
        ort="Bo",
    )
    LAUT_BBR_BR = Sammlung(
        trace="Bbr Br",
        groups="Lautschrift|Bbr Br",
        kreis="Bbr",
        ort="Br",
    )
    LAUT_BBR_BS = Sammlung(
        trace="Bbr Bs",
        groups="Lautschrift|Bbr Bs",
        kreis="Bbr",
        ort="Bs",
    )
    LAUT_BBR_DA = Sammlung(
        trace="Bbr Da",
        groups="Lautschrift|Bbr Da",
        kreis="Bbr",
        ort="Da",
    )
    LAUT_BBR_DH = Sammlung(
        trace="Bbr Dh",
        groups="Lautschrift|Bbr Dh",
        kreis="Bbr",
        ort="Dh",
    )
    LAUT_BBR_EN = Sammlung(
        trace="Bbr En",
        groups="Lautschrift|Bbr En",
        kreis="Bbr",
        ort="En",
    )
    LAUT_BBR_EP = Sammlung(
        trace="Bbr Ep",
        groups="Lautschrift|Bbr Ep",
        kreis="Bbr",
        ort="Ep",
    )
    LAUT_BBR_ET = Sammlung(
        trace="Bbr Et",
        groups="Lautschrift|Bbr Et",
        kreis="Bbr",
        ort="Et",
    )
    LAUT_BBR_EV = Sammlung(
        trace="Bbr Ev",
        groups="Lautschrift|Bbr Ev",
        kreis="Bbr",
        ort="Ev",
    )
    LAUT_BBR_FA = Sammlung(
        trace="Bbr Fa",
        groups="Lautschrift|Bbr Fa",
        kreis="Bbr",
        ort="Fa",
    )
    LAUT_BBR_FÜ = Sammlung(
        trace="Bbr Fü",
        groups="Lautschrift|Bbr Fü",
        kreis="Bbr",
        ort="Fü",
    )
    LAUT_BBR_GD = Sammlung(
        trace="Bbr Gd",
        groups="Lautschrift|Bbr Gd",
        kreis="Bbr",
        ort="Gd",
    )
    LAUT_BBR_GE = Sammlung(
        trace="Bbr Ge",
        groups="Lautschrift|Bbr Ge",
        kreis="Bbr",
        ort="Ge",
    )
    LAUT_BBR_GF = Sammlung(
        trace="Bbr Gf",
        groups="Lautschrift|Bbr Gf",
        kreis="Bbr",
        ort="Gf",
    )
    LAUT_BBR_GL = Sammlung(
        trace="Bbr Gl",
        groups="Lautschrift|Bbr Gl",
        kreis="Bbr",
        ort="Gl",
    )
    LAUT_BBR_GM = Sammlung(
        trace="Bbr Gm",
        groups="Lautschrift|Bbr Gm",
        kreis="Bbr",
        ort="Gm",
    )
    LAUT_BBR_GR = Sammlung(
        trace="Bbr Gr",
        groups="Lautschrift|Bbr Gr",
        kreis="Bbr",
        ort="Gr",
    )
    LAUT_BBR_HA = Sammlung(
        trace="Bbr Ha",
        groups="Lautschrift|Bbr Ha",
        kreis="Bbr",
        ort="Ha",
    )
    LAUT_BBR_HE = Sammlung(
        trace="Bbr He",
        groups="Lautschrift|Bbr He",
        kreis="Bbr",
        ort="He",
    )
    LAUT_BBR_HK = Sammlung(
        trace="Bbr Hk",
        groups="Lautschrift|Bbr Hk",
        kreis="Bbr",
        ort="Hk",
    )
    LAUT_BBR_HL = Sammlung(
        trace="Bbr Hl",
        groups="Lautschrift|Bbr Hl",
        kreis="Bbr",
        ort="Hl",
    )
    LAUT_BBR_HM = Sammlung(
        trace="Bbr Hm",
        groups="Lautschrift|Bbr Hm",
        kreis="Bbr",
        ort="Hm",
    )
    LAUT_BBR_HÖ = Sammlung(
        trace="Bbr Hö",
        groups="Lautschrift|Bbr Hö",
        kreis="Bbr",
        ort="Hö",
    )
    LAUT_BBR_HP = Sammlung(
        trace="Bbr Hp",
        groups="Lautschrift|Bbr Hp",
        kreis="Bbr",
        ort="Hp",
    )
    LAUT_BBR_HR = Sammlung(
        trace="Bbr Hr",
        groups="Lautschrift|Bbr Hr",
        kreis="Bbr",
        ort="Hr",
    )
    LAUT_BBR_HS = Sammlung(
        trace="Bbr Hs",
        groups="Lautschrift|Bbr Hs",
        kreis="Bbr",
        ort="Hs",
    )
    LAUT_BBR_HX = Sammlung(
        trace="Bbr Hx",
        groups="Lautschrift|Bbr Hx",
        kreis="Bbr",
        ort="Hx",
    )
    LAUT_BBR_KA = Sammlung(
        trace="Bbr Ka",
        groups="Lautschrift|Bbr Ka",
        kreis="Bbr",
        ort="Ka",
    )
    LAUT_BBR_KB = Sammlung(
        trace="Bbr Kb",
        groups="Lautschrift|Bbr Kb",
        kreis="Bbr",
        ort="Kb",
    )
    LAUT_BBR_KK = Sammlung(
        trace="Bbr Kk",
        groups="Lautschrift|Bbr Kk",
        kreis="Bbr",
        ort="Kk",
    )
    LAUT_BBR_KM = Sammlung(
        trace="Bbr Km",
        groups="Lautschrift|Bbr Km",
        kreis="Bbr",
        ort="Km",
    )
    LAUT_BBR_LA = Sammlung(
        trace="Bbr La",
        groups="Lautschrift|Bbr La",
        kreis="Bbr",
        ort="La",
    )
    LAUT_BBR_LB = Sammlung(
        trace="Bbr Lb",
        groups="Lautschrift|Bbr Lb",
        kreis="Bbr",
        ort="Lb",
    )
    LAUT_BBR_LE = Sammlung(
        trace="Bbr Le",
        groups="Lautschrift|Bbr Le",
        kreis="Bbr",
        ort="Le",
    )
    LAUT_BBR_LI = Sammlung(
        trace="Bbr Li",
        groups="Lautschrift|Bbr Li",
        kreis="Bbr",
        ort="Li",
    )
    LAUT_BBR_LO = Sammlung(
        trace="Bbr Lo",
        groups="Lautschrift|Bbr Lo",
        kreis="Bbr",
        ort="Lo",
    )
    LAUT_BBR_LT = Sammlung(
        trace="Bbr Lt",
        groups="Lautschrift|Bbr Lt",
        kreis="Bbr",
        ort="Lt",
    )
    LAUT_BBR_ME = Sammlung(
        trace="Bbr Me",
        groups="Lautschrift|Bbr Me",
        kreis="Bbr",
        ort="Me",
    )
    LAUT_BBR_MZ = Sammlung(
        trace="Bbr Mz",
        groups="Lautschrift|Bbr Mz",
        kreis="Bbr",
        ort="Mz",
    )
    LAUT_BBR_NK = Sammlung(
        trace="Bbr Nk",
        groups="Lautschrift|Bbr Nk",
        kreis="Bbr",
        ort="Nk",
    )
    LAUT_BBR_NO = Sammlung(
        trace="Bbr No",
        groups="Lautschrift|Bbr No",
        kreis="Bbr",
        ort="No",
    )
    LAUT_BBR_OM = Sammlung(
        trace="Bbr Om",
        groups="Lautschrift|Bbr Om",
        kreis="Bbr",
        ort="Om",
    )
    LAUT_BBR_OR = Sammlung(
        trace="Bbr Or",
        groups="Lautschrift|Bbr Or",
        kreis="Bbr",
        ort="Or",
    )
    LAUT_BBR_PL = Sammlung(
        trace="Bbr Pl",
        groups="Lautschrift|Bbr Pl",
        kreis="Bbr",
        ort="Pl",
    )
    LAUT_BBR_PR = Sammlung(
        trace="Bbr Pr",
        groups="Lautschrift|Bbr Pr",
        kreis="Bbr",
        ort="Pr",
    )
    LAUT_BBR_QU = Sammlung(
        trace="Bbr Qu",
        groups="Lautschrift|Bbr Qu",
        kreis="Bbr",
        ort="Qu",
    )
    LAUT_BBR_RE = Sammlung(
        trace="Bbr Re",
        groups="Lautschrift|Bbr Re",
        kreis="Bbr",
        ort="Re",
    )
    LAUT_BBR_RF = Sammlung(
        trace="Bbr Rf",
        groups="Lautschrift|Bbr Rf",
        kreis="Bbr",
        ort="Rf",
    )
    LAUT_BBR_RH = Sammlung(
        trace="Bbr Rh",
        groups="Lautschrift|Bbr Rh",
        kreis="Bbr",
        ort="Rh",
    )
    LAUT_BBR_RI = Sammlung(
        trace="Bbr Ri",
        groups="Lautschrift|Bbr Ri",
        kreis="Bbr",
        ort="Ri",
    )
    LAUT_BBR_RL = Sammlung(
        trace="Bbr Rl",
        groups="Lautschrift|Bbr Rl",
        kreis="Bbr",
        ort="Rl",
    )
    LAUT_BBR_RÜ = Sammlung(
        trace="Bbr Rü",
        groups="Lautschrift|Bbr Rü",
        kreis="Bbr",
        ort="Rü",
    )
    LAUT_BBR_SE = Sammlung(
        trace="Bbr Se",
        groups="Lautschrift|Bbr Se",
        kreis="Bbr",
        ort="Se",
    )
    LAUT_BBR_SL = Sammlung(
        trace="Bbr Sl",
        groups="Lautschrift|Bbr Sl",
        kreis="Bbr",
        ort="Sl",
    )
    LAUT_BBR_SM = Sammlung(
        trace="Bbr Sm",
        groups="Lautschrift|Bbr Sm",
        kreis="Bbr",
        ort="Sm",
    )
    LAUT_BBR_SÖ = Sammlung(
        trace="Bbr Sö",
        groups="Lautschrift|Bbr Sö",
        kreis="Bbr",
        ort="Sö",
    )
    LAUT_BBR_SU = Sammlung(
        trace="Bbr Su",
        groups="Lautschrift|Bbr Su",
        kreis="Bbr",
        ort="Su",
    )
    LAUT_BBR_SW = Sammlung(
        trace="Bbr Sw",
        groups="Lautschrift|Bbr Sw",
        kreis="Bbr",
        ort="Sw",
    )
    LAUT_BBR_TA = Sammlung(
        trace="Bbr Ta",
        groups="Lautschrift|Bbr Ta",
        kreis="Bbr",
        ort="Ta",
    )
    LAUT_BBR_ÜF = Sammlung(
        trace="Bbr Üf",
        groups="Lautschrift|Bbr Üf",
        kreis="Bbr",
        ort="Üf",
    )
    LAUT_BBR_VC = Sammlung(
        trace="Bbr Vc",
        groups="Lautschrift|Bbr Vc",
        kreis="Bbr",
        ort="Vc",
    )
    LAUT_BBR_VE = Sammlung(
        trace="Bbr Ve",
        groups="Lautschrift|Bbr Ve",
        kreis="Bbr",
        ort="Ve",
    )
    LAUT_BBR_VI = Sammlung(
        trace="Bbr Vi",
        groups="Lautschrift|Bbr Vi",
        kreis="Bbr",
        ort="Vi",
    )
    LAUT_BBR_VO = Sammlung(
        trace="Bbr Vo",
        groups="Lautschrift|Bbr Vo",
        kreis="Bbr",
        ort="Vo",
    )
    LAUT_BBR_VÖ = Sammlung(
        trace="Bbr Vö",
        groups="Lautschrift|Bbr Vö",
        kreis="Bbr",
        ort="Vö",
    )
    LAUT_BBR_WB = Sammlung(
        trace="Bbr Wb",
        groups="Lautschrift|Bbr Wb",
        kreis="Bbr",
        ort="Wb",
    )
    LAUT_BBR_WE = Sammlung(
        trace="Bbr We",
        groups="Lautschrift|Bbr We",
        kreis="Bbr",
        ort="We",
    )
    LAUT_BBR_WH = Sammlung(
        trace="Bbr Wh",
        groups="Lautschrift|Bbr Wh",
        kreis="Bbr",
        ort="Wh",
    )
    LAUT_BBR_WS = Sammlung(
        trace="Bbr Ws",
        groups="Lautschrift|Bbr Ws",
        kreis="Bbr",
        ort="Ws",
    )
    LAUT_BBR_WU = Sammlung(
        trace="Bbr Wu",
        groups="Lautschrift|Bbr Wu",
        kreis="Bbr",
        ort="Wu",
    )
    LAUT_BBR_WW = Sammlung(
        trace="Bbr Ww",
        groups="Lautschrift|Bbr Ww",
        kreis="Bbr",
        ort="Ww",
    )
    LAUT_BCH_AB = Sammlung(
        trace="Bch Ab",
        groups="Lautschrift|Bch Ab",
        kreis="Bch",
        ort="Ab",
    )
    LAUT_BCH_BO = Sammlung(
        trace="Bch Bo",
        groups="Lautschrift|Bch Bo",
        kreis="Bch",
        ort="Bo",
    )
    LAUT_BCH_BÖ = Sammlung(
        trace="Bch Bö",
        groups="Lautschrift|Bch Bö",
        kreis="Bch",
        ort="Bö",
    )
    LAUT_BCH_BR = Sammlung(
        trace="Bch Br",
        groups="Lautschrift|Bch Br",
        kreis="Bch",
        ort="Br",
    )
    LAUT_BCH_GE = Sammlung(
        trace="Bch Ge",
        groups="Lautschrift|Bch Ge",
        kreis="Bch",
        ort="Ge",
    )
    LAUT_BCH_HA = Sammlung(
        trace="Bch Ha",
        groups="Lautschrift|Bch Ha",
        kreis="Bch",
        ort="Ha",
    )
    LAUT_BCH_HE = Sammlung(
        trace="Bch He",
        groups="Lautschrift|Bch He",
        kreis="Bch",
        ort="He",
    )
    LAUT_BCH_HI = Sammlung(
        trace="Bch Hi",
        groups="Lautschrift|Bch Hi",
        kreis="Bch",
        ort="Hi",
    )
    LAUT_BCH_HO = Sammlung(
        trace="Bch Ho",
        groups="Lautschrift|Bch Ho",
        kreis="Bch",
        ort="Ho",
    )
    LAUT_BCH_HP = Sammlung(
        trace="Bch Hp",
        groups="Lautschrift|Bch Hp",
        kreis="Bch",
        ort="Hp",
    )
    LAUT_BCH_LD = Sammlung(
        trace="Bch Ld",
        groups="Lautschrift|Bch Ld",
        kreis="Bch",
        ort="Ld",
    )
    LAUT_BCH_LD1 = Sammlung(
        trace="Bch Ld1",
        groups="Lautschrift|Bch Ld1",
        kreis="Bch",
        ort="Ld1",
    )
    LAUT_BCH_LI = Sammlung(
        trace="Bch Li",
        groups="Lautschrift|Bch Li",
        kreis="Bch",
        ort="Li",
    )
    LAUT_BCH_LR = Sammlung(
        trace="Bch Lr",
        groups="Lautschrift|Bch Lr",
        kreis="Bch",
        ort="Lr",
    )
    LAUT_BCH_LT = Sammlung(
        trace="Bch Lt",
        groups="Lautschrift|Bch Lt",
        kreis="Bch",
        ort="Lt",
    )
    LAUT_BCH_SE = Sammlung(
        trace="Bch Se",
        groups="Lautschrift|Bch Se",
        kreis="Bch",
        ort="Se",
    )
    LAUT_BCH_SO = Sammlung(
        trace="Bch So",
        groups="Lautschrift|Bch So",
        kreis="Bch",
        ort="So",
    )
    LAUT_BCH_SP = Sammlung(
        trace="Bch Sp",
        groups="Lautschrift|Bch Sp",
        kreis="Bch",
        ort="Sp",
    )
    LAUT_BCH_ST = Sammlung(
        trace="Bch St",
        groups="Lautschrift|Bch St",
        kreis="Bch",
        ort="St",
    )
    LAUT_BCH_ST1 = Sammlung(
        trace="Bch St1",
        groups="Lautschrift|Bch St1",
        kreis="Bch",
        ort="St1",
    )
    LAUT_BCH_WA = Sammlung(
        trace="Bch Wa",
        groups="Lautschrift|Bch Wa",
        kreis="Bch",
        ort="Wa",
    )
    LAUT_BCH_WE = Sammlung(
        trace="Bch We",
        groups="Lautschrift|Bch We",
        kreis="Bch",
        ort="We",
    )
    LAUT_BCH_WT = Sammlung(
        trace="Bch Wt",
        groups="Lautschrift|Bch Wt",
        kreis="Bch",
        ort="Wt",
    )
    LAUT_BEK_AA = Sammlung(
        trace="Bek Aa",
        groups="Lautschrift|Bek Aa",
        kreis="Bek",
        ort="Aa",
    )
    LAUT_BEK_AC = Sammlung(
        trace="Bek Ac",
        groups="Lautschrift|Bek Ac",
        kreis="Bek",
        ort="Ac",
    )
    LAUT_BEK_AL = Sammlung(
        trace="Bek Al",
        groups="Lautschrift|Bek Al",
        kreis="Bek",
        ort="Al",
    )
    LAUT_BEK_BB = Sammlung(
        trace="Bek Bb",
        groups="Lautschrift|Bek Bb",
        kreis="Bek",
        ort="Bb",
    )
    LAUT_BEK_BE = Sammlung(
        trace="Bek Be",
        groups="Lautschrift|Bek Be",
        kreis="Bek",
        ort="Be",
    )
    LAUT_BEK_BF = Sammlung(
        trace="Bek Bf",
        groups="Lautschrift|Bek Bf",
        kreis="Bek",
        ort="Bf",
    )
    LAUT_BEK_BK = Sammlung(
        trace="Bek Bk",
        groups="Lautschrift|Bek Bk",
        kreis="Bek",
        ort="Bk",
    )
    LAUT_BEK_DB = Sammlung(
        trace="Bek Db",
        groups="Lautschrift|Bek Db",
        kreis="Bek",
        ort="Db",
    )
    LAUT_BEK_DI = Sammlung(
        trace="Bek Di",
        groups="Lautschrift|Bek Di",
        kreis="Bek",
        ort="Di",
    )
    LAUT_BEK_EK = Sammlung(
        trace="Bek Ek",
        groups="Lautschrift|Bek Ek",
        kreis="Bek",
        ort="Ek",
    )
    LAUT_BEK_EL = Sammlung(
        trace="Bek El",
        groups="Lautschrift|Bek El",
        kreis="Bek",
        ort="El",
    )
    LAUT_BEK_EN = Sammlung(
        trace="Bek En",
        groups="Lautschrift|Bek En",
        kreis="Bek",
        ort="En",
    )
    LAUT_BEK_GÖ = Sammlung(
        trace="Bek Gö",
        groups="Lautschrift|Bek Gö",
        kreis="Bek",
        ort="Gö",
    )
    LAUT_BEK_HE = Sammlung(
        trace="Bek He",
        groups="Lautschrift|Bek He",
        kreis="Bek",
        ort="He",
    )
    LAUT_BEK_HF = Sammlung(
        trace="Bek Hf",
        groups="Lautschrift|Bek Hf",
        kreis="Bek",
        ort="Hf",
    )
    LAUT_BEK_HI = Sammlung(
        trace="Bek Hi",
        groups="Lautschrift|Bek Hi",
        kreis="Bek",
        ort="Hi",
    )
    LAUT_BEK_HO = Sammlung(
        trace="Bek Ho",
        groups="Lautschrift|Bek Ho",
        kreis="Bek",
        ort="Ho",
    )
    LAUT_BEK_KE = Sammlung(
        trace="Bek Ke",
        groups="Lautschrift|Bek Ke",
        kreis="Bek",
        ort="Ke",
    )
    LAUT_BEK_LB = Sammlung(
        trace="Bek Lb",
        groups="Lautschrift|Bek Lb",
        kreis="Bek",
        ort="Lb",
    )
    LAUT_BEK_LI = Sammlung(
        trace="Bek Li",
        groups="Lautschrift|Bek Li",
        kreis="Bek",
        ort="Li",
    )
    LAUT_BEK_NB = Sammlung(
        trace="Bek Nb",
        groups="Lautschrift|Bek Nb",
        kreis="Bek",
        ort="Nb",
    )
    LAUT_BEK_ÖL = Sammlung(
        trace="Bek Öl",
        groups="Lautschrift|Bek Öl",
        kreis="Bek",
        ort="Öl",
    )
    LAUT_BEK_ÖS = Sammlung(
        trace="Bek Ös",
        groups="Lautschrift|Bek Ös",
        kreis="Bek",
        ort="Ös",
    )
    LAUT_BEK_SH = Sammlung(
        trace="Bek Sh",
        groups="Lautschrift|Bek Sh",
        kreis="Bek",
        ort="Sh",
    )
    LAUT_BEK_ST = Sammlung(
        trace="Bek St",
        groups="Lautschrift|Bek St",
        kreis="Bek",
        ort="St",
    )
    LAUT_BEK_SÜ = Sammlung(
        trace="Bek Sü",
        groups="Lautschrift|Bek Sü",
        kreis="Bek",
        ort="Sü",
    )
    LAUT_BEK_VE = Sammlung(
        trace="Bek Ve",
        groups="Lautschrift|Bek Ve",
        kreis="Bek",
        ort="Ve",
    )
    LAUT_BEK_VH = Sammlung(
        trace="Bek Vh",
        groups="Lautschrift|Bek Vh",
        kreis="Bek",
        ort="Vh",
    )
    LAUT_BEK_WL = Sammlung(
        trace="Bek Wl",
        groups="Lautschrift|Bek Wl",
        kreis="Bek",
        ort="Wl",
    )
    LAUT_BEN_AD = Sammlung(
        trace="Ben Ad",
        groups="Lautschrift|Ben Ad",
        kreis="Ben",
        ort="Ad",
    )
    LAUT_BEN_AL = Sammlung(
        trace="Ben Al",
        groups="Lautschrift|Ben Al",
        kreis="Ben",
        ort="Al",
    )
    LAUT_BEN_AP = Sammlung(
        trace="Ben Ap",
        groups="Lautschrift|Ben Ap",
        kreis="Ben",
        ort="Ap",
    )
    LAUT_BEN_AW = Sammlung(
        trace="Ben Aw",
        groups="Lautschrift|Ben Aw",
        kreis="Ben",
        ort="Aw",
    )
    LAUT_BEN_BA = Sammlung(
        trace="Ben Ba",
        groups="Lautschrift|Ben Ba",
        kreis="Ben",
        ort="Ba",
    )
    LAUT_BEN_BG = Sammlung(
        trace="Ben Bg",
        groups="Lautschrift|Ben Bg",
        kreis="Ben",
        ort="Bg",
    )
    LAUT_BEN_BH = Sammlung(
        trace="Ben Bh",
        groups="Lautschrift|Ben Bh",
        kreis="Ben",
        ort="Bh",
    )
    LAUT_BEN_BI = Sammlung(
        trace="Ben Bi",
        groups="Lautschrift|Ben Bi",
        kreis="Ben",
        ort="Bi",
    )
    LAUT_BEN_BM = Sammlung(
        trace="Ben Bm",
        groups="Lautschrift|Ben Bm",
        kreis="Ben",
        ort="Bm",
    )
    LAUT_BEN_BN = Sammlung(
        trace="Ben Bn",
        groups="Lautschrift|Ben Bn",
        kreis="Ben",
        ort="Bn",
    )
    LAUT_BEN_BR = Sammlung(
        trace="Ben Br",
        groups="Lautschrift|Ben Br",
        kreis="Ben",
        ort="Br",
    )
    LAUT_BEN_DR = Sammlung(
        trace="Ben Dr",
        groups="Lautschrift|Ben Dr",
        kreis="Ben",
        ort="Dr",
    )
    LAUT_BEN_EC = Sammlung(
        trace="Ben Ec",
        groups="Lautschrift|Ben Ec",
        kreis="Ben",
        ort="Ec",
    )
    LAUT_BEN_EG = Sammlung(
        trace="Ben Eg",
        groups="Lautschrift|Ben Eg",
        kreis="Ben",
        ort="Eg",
    )
    LAUT_BEN_EH = Sammlung(
        trace="Ben Eh",
        groups="Lautschrift|Ben Eh",
        kreis="Ben",
        ort="Eh",
    )
    LAUT_BEN_EM = Sammlung(
        trace="Ben Em",
        groups="Lautschrift|Ben Em",
        kreis="Ben",
        ort="Em",
    )
    LAUT_BEN_EN = Sammlung(
        trace="Ben En",
        groups="Lautschrift|Ben En",
        kreis="Ben",
        ort="En",
    )
    LAUT_BEN_ES = Sammlung(
        trace="Ben Es",
        groups="Lautschrift|Ben Es",
        kreis="Ben",
        ort="Es",
    )
    LAUT_BEN_EW = Sammlung(
        trace="Ben Ew",
        groups="Lautschrift|Ben Ew",
        kreis="Ben",
        ort="Ew",
    )
    LAUT_BEN_FH = Sammlung(
        trace="Ben Fh",
        groups="Lautschrift|Ben Fh",
        kreis="Ben",
        ort="Fh",
    )
    LAUT_BEN_GD = Sammlung(
        trace="Ben Gd",
        groups="Lautschrift|Ben Gd",
        kreis="Ben",
        ort="Gd",
    )
    LAUT_BEN_GE = Sammlung(
        trace="Ben Ge",
        groups="Lautschrift|Ben Ge",
        kreis="Ben",
        ort="Ge",
    )
    LAUT_BEN_GH = Sammlung(
        trace="Ben Gh",
        groups="Lautschrift|Ben Gh",
        kreis="Ben",
        ort="Gh",
    )
    LAUT_BEN_GK = Sammlung(
        trace="Ben Gk",
        groups="Lautschrift|Ben Gk",
        kreis="Ben",
        ort="Gk",
    )
    LAUT_BEN_GM = Sammlung(
        trace="Ben Gm",
        groups="Lautschrift|Ben Gm",
        kreis="Ben",
        ort="Gm",
    )
    LAUT_BEN_GR = Sammlung(
        trace="Ben Gr",
        groups="Lautschrift|Ben Gr",
        kreis="Ben",
        ort="Gr",
    )
    LAUT_BEN_GS = Sammlung(
        trace="Ben Gs",
        groups="Lautschrift|Ben Gs",
        kreis="Ben",
        ort="Gs",
    )
    LAUT_BEN_HA = Sammlung(
        trace="Ben Ha",
        groups="Lautschrift|Ben Ha",
        kreis="Ben",
        ort="Ha",
    )
    LAUT_BEN_HE = Sammlung(
        trace="Ben He",
        groups="Lautschrift|Ben He",
        kreis="Ben",
        ort="He",
    )
    LAUT_BEN_HF = Sammlung(
        trace="Ben Hf",
        groups="Lautschrift|Ben Hf",
        kreis="Ben",
        ort="Hf",
    )
    LAUT_BEN_HH = Sammlung(
        trace="Ben Hh",
        groups="Lautschrift|Ben Hh",
        kreis="Ben",
        ort="Hh",
    )
    LAUT_BEN_HI = Sammlung(
        trace="Ben Hi",
        groups="Lautschrift|Ben Hi",
        kreis="Ben",
        ort="Hi",
    )
    LAUT_BEN_HK = Sammlung(
        trace="Ben Hk",
        groups="Lautschrift|Ben Hk",
        kreis="Ben",
        ort="Hk",
    )
    LAUT_BEN_HL = Sammlung(
        trace="Ben Hl",
        groups="Lautschrift|Ben Hl",
        kreis="Ben",
        ort="Hl",
    )
    LAUT_BEN_HO = Sammlung(
        trace="Ben Ho",
        groups="Lautschrift|Ben Ho",
        kreis="Ben",
        ort="Ho",
    )
    LAUT_BEN_HÖ = Sammlung(
        trace="Ben Hö",
        groups="Lautschrift|Ben Hö",
        kreis="Ben",
        ort="Hö",
    )
    LAUT_BEN_HP = Sammlung(
        trace="Ben Hp",
        groups="Lautschrift|Ben Hp",
        kreis="Ben",
        ort="Hp",
    )
    LAUT_BEN_IT = Sammlung(
        trace="Ben It",
        groups="Lautschrift|Ben It",
        kreis="Ben",
        ort="It",
    )
    LAUT_BEN_KA = Sammlung(
        trace="Ben Ka",
        groups="Lautschrift|Ben Ka",
        kreis="Ben",
        ort="Ka",
    )
    LAUT_BEN_LA = Sammlung(
        trace="Ben La",
        groups="Lautschrift|Ben La",
        kreis="Ben",
        ort="La",
    )
    LAUT_BEN_LR = Sammlung(
        trace="Ben Lr",
        groups="Lautschrift|Ben Lr",
        kreis="Ben",
        ort="Lr",
    )
    LAUT_BEN_NG = Sammlung(
        trace="Ben Ng",
        groups="Lautschrift|Ben Ng",
        kreis="Ben",
        ort="Ng",
    )
    LAUT_BEN_NH = Sammlung(
        trace="Ben Nh",
        groups="Lautschrift|Ben Nh",
        kreis="Ben",
        ort="Nh",
    )
    LAUT_BEN_NL = Sammlung(
        trace="Ben Nl",
        groups="Lautschrift|Ben Nl",
        kreis="Ben",
        ort="Nl",
    )
    LAUT_BEN_NO = Sammlung(
        trace="Ben No",
        groups="Lautschrift|Ben No",
        kreis="Ben",
        ort="No",
    )
    LAUT_BEN_NR = Sammlung(
        trace="Ben Nr",
        groups="Lautschrift|Ben Nr",
        kreis="Ben",
        ort="Nr",
    )
    LAUT_BEN_OG = Sammlung(
        trace="Ben Og",
        groups="Lautschrift|Ben Og",
        kreis="Ben",
        ort="Og",
    )
    LAUT_BEN_ON = Sammlung(
        trace="Ben On",
        groups="Lautschrift|Ben On",
        kreis="Ben",
        ort="On",
    )
    LAUT_BEN_OW = Sammlung(
        trace="Ben Ow",
        groups="Lautschrift|Ben Ow",
        kreis="Ben",
        ort="Ow",
    )
    LAUT_BEN_QD = Sammlung(
        trace="Ben Qd",
        groups="Lautschrift|Ben Qd",
        kreis="Ben",
        ort="Qd",
    )
    LAUT_BEN_RA = Sammlung(
        trace="Ben Ra",
        groups="Lautschrift|Ben Ra",
        kreis="Ben",
        ort="Ra",
    )
    LAUT_BEN_SA = Sammlung(
        trace="Ben Sa",
        groups="Lautschrift|Ben Sa",
        kreis="Ben",
        ort="Sa",
    )
    LAUT_BEN_SC = Sammlung(
        trace="Ben Sc",
        groups="Lautschrift|Ben Sc",
        kreis="Ben",
        ort="Sc",
    )
    LAUT_BEN_SH = Sammlung(
        trace="Ben Sh",
        groups="Lautschrift|Ben Sh",
        kreis="Ben",
        ort="Sh",
    )
    LAUT_BEN_SI = Sammlung(
        trace="Ben Si",
        groups="Lautschrift|Ben Si",
        kreis="Ben",
        ort="Si",
    )
    LAUT_BEN_SU = Sammlung(
        trace="Ben Su",
        groups="Lautschrift|Ben Su",
        kreis="Ben",
        ort="Su",
    )
    LAUT_BEN_TH = Sammlung(
        trace="Ben Th",
        groups="Lautschrift|Ben Th",
        kreis="Ben",
        ort="Th",
    )
    LAUT_BEN_ÜL = Sammlung(
        trace="Ben Ül",
        groups="Lautschrift|Ben Ül",
        kreis="Ben",
        ort="Ül",
    )
    LAUT_BEN_VH = Sammlung(
        trace="Ben Vh",
        groups="Lautschrift|Ben Vh",
        kreis="Ben",
        ort="Vh",
    )
    LAUT_BEN_VW = Sammlung(
        trace="Ben Vw",
        groups="Lautschrift|Ben Vw",
        kreis="Ben",
        ort="Vw",
    )
    LAUT_BEN_WA = Sammlung(
        trace="Ben Wa",
        groups="Lautschrift|Ben Wa",
        kreis="Ben",
        ort="Wa",
    )
    LAUT_BEN_WI = Sammlung(
        trace="Ben Wi",
        groups="Lautschrift|Ben Wi",
        kreis="Ben",
        ort="Wi",
    )
    LAUT_BEN_WM = Sammlung(
        trace="Ben Wm",
        groups="Lautschrift|Ben Wm",
        kreis="Ben",
        ort="Wm",
    )
    LAUT_BEN_WS = Sammlung(
        trace="Ben Ws",
        groups="Lautschrift|Ben Ws",
        kreis="Ben",
        ort="Ws",
    )
    LAUT_BEN_WT = Sammlung(
        trace="Ben Wt",
        groups="Lautschrift|Ben Wt",
        kreis="Ben",
        ort="Wt",
    )
    LAUT_BIE_AH = Sammlung(
        trace="Bie Ah",
        groups="Lautschrift|Bie Ah",
        kreis="Bie",
        ort="Ah",
    )
    LAUT_BIE_BA = Sammlung(
        trace="Bie Ba",
        groups="Lautschrift|Bie Ba",
        kreis="Bie",
        ort="Ba",
    )
    LAUT_BIE_BE = Sammlung(
        trace="Bie Be",
        groups="Lautschrift|Bie Be",
        kreis="Bie",
        ort="Be",
    )
    LAUT_BIE_BF = Sammlung(
        trace="Bie Bf",
        groups="Lautschrift|Bie Bf",
        kreis="Bie",
        ort="Bf",
    )
    LAUT_BIE_BH = Sammlung(
        trace="Bie Bh",
        groups="Lautschrift|Bie Bh",
        kreis="Bie",
        ort="Bh",
    )
    LAUT_BIE_BR = Sammlung(
        trace="Bie Br",
        groups="Lautschrift|Bie Br",
        kreis="Bie",
        ort="Br",
    )
    LAUT_BIE_BW = Sammlung(
        trace="Bie Bw",
        groups="Lautschrift|Bie Bw",
        kreis="Bie",
        ort="Bw",
    )
    LAUT_BIE_DB = Sammlung(
        trace="Bie Db",
        groups="Lautschrift|Bie Db",
        kreis="Bie",
        ort="Db",
    )
    LAUT_BIE_DD = Sammlung(
        trace="Bie Dd",
        groups="Lautschrift|Bie Dd",
        kreis="Bie",
        ort="Dd",
    )
    LAUT_BIE_EB = Sammlung(
        trace="Bie Eb",
        groups="Lautschrift|Bie Eb",
        kreis="Bie",
        ort="Eb",
    )
    LAUT_BIE_GB = Sammlung(
        trace="Bie Gb",
        groups="Lautschrift|Bie Gb",
        kreis="Bie",
        ort="Gb",
    )
    LAUT_BIE_GH = Sammlung(
        trace="Bie Gh",
        groups="Lautschrift|Bie Gh",
        kreis="Bie",
        ort="Gh",
    )
    LAUT_BIE_GR = Sammlung(
        trace="Bie Gr",
        groups="Lautschrift|Bie Gr",
        kreis="Bie",
        ort="Gr",
    )
    LAUT_BIE_HB = Sammlung(
        trace="Bie Hb",
        groups="Lautschrift|Bie Hb",
        kreis="Bie",
        ort="Hb",
    )
    LAUT_BIE_HE = Sammlung(
        trace="Bie He",
        groups="Lautschrift|Bie He",
        kreis="Bie",
        ort="He",
    )
    LAUT_BIE_HI = Sammlung(
        trace="Bie Hi",
        groups="Lautschrift|Bie Hi",
        kreis="Bie",
        ort="Hi",
    )
    LAUT_BIE_HK = Sammlung(
        trace="Bie Hk",
        groups="Lautschrift|Bie Hk",
        kreis="Bie",
        ort="Hk",
    )
    LAUT_BIE_HO = Sammlung(
        trace="Bie Ho",
        groups="Lautschrift|Bie Ho",
        kreis="Bie",
        ort="Ho",
    )
    LAUT_BIE_JÖ = Sammlung(
        trace="Bie Jö",
        groups="Lautschrift|Bie Jö",
        kreis="Bie",
        ort="Jö",
    )
    LAUT_BIE_IS = Sammlung(
        trace="Bie Is",
        groups="Lautschrift|Bie Is",
        kreis="Bie",
        ort="Is",
    )
    LAUT_BIE_KD = Sammlung(
        trace="Bie Kd",
        groups="Lautschrift|Bie Kd",
        kreis="Bie",
        ort="Kd",
    )
    LAUT_BIE_LH = Sammlung(
        trace="Bie Lh",
        groups="Lautschrift|Bie Lh",
        kreis="Bie",
        ort="Lh",
    )
    LAUT_BIE_MI = Sammlung(
        trace="Bie Mi",
        groups="Lautschrift|Bie Mi",
        kreis="Bie",
        ort="Mi",
    )
    LAUT_BIE_ND = Sammlung(
        trace="Bie Nd",
        groups="Lautschrift|Bie Nd",
        kreis="Bie",
        ort="Nd",
    )
    LAUT_BIE_NH = Sammlung(
        trace="Bie Nh",
        groups="Lautschrift|Bie Nh",
        kreis="Bie",
        ort="Nh",
    )
    LAUT_BIE_NI = Sammlung(
        trace="Bie Ni",
        groups="Lautschrift|Bie Ni",
        kreis="Bie",
        ort="Ni",
    )
    LAUT_BIE_NJ = Sammlung(
        trace="Bie Nj",
        groups="Lautschrift|Bie Nj",
        kreis="Bie",
        ort="Nj",
    )
    LAUT_BIE_OJ = Sammlung(
        trace="Bie Oj",
        groups="Lautschrift|Bie Oj",
        kreis="Bie",
        ort="Oj",
    )
    LAUT_BIE_OT = Sammlung(
        trace="Bie Ot",
        groups="Lautschrift|Bie Ot",
        kreis="Bie",
        ort="Ot",
    )
    LAUT_BIE_QU = Sammlung(
        trace="Bie Qu",
        groups="Lautschrift|Bie Qu",
        kreis="Bie",
        ort="Qu",
    )
    LAUT_BIE_SC = Sammlung(
        trace="Bie Sc",
        groups="Lautschrift|Bie Sc",
        kreis="Bie",
        ort="Sc",
    )
    LAUT_BIE_SE = Sammlung(
        trace="Bie Se",
        groups="Lautschrift|Bie Se",
        kreis="Bie",
        ort="Se",
    )
    LAUT_BIE_SI = Sammlung(
        trace="Bie Si",
        groups="Lautschrift|Bie Si",
        kreis="Bie",
        ort="Si",
    )
    LAUT_BIE_ST = Sammlung(
        trace="Bie St",
        groups="Lautschrift|Bie St",
        kreis="Bie",
        ort="St",
    )
    LAUT_BIE_SZ = Sammlung(
        trace="Bie Sz",
        groups="Lautschrift|Bie Sz",
        kreis="Bie",
        ort="Sz",
    )
    LAUT_BIE_TH = Sammlung(
        trace="Bie Th",
        groups="Lautschrift|Bie Th",
        kreis="Bie",
        ort="Th",
    )
    LAUT_BIE_UD = Sammlung(
        trace="Bie Ud",
        groups="Lautschrift|Bie Ud",
        kreis="Bie",
        ort="Ud",
    )
    LAUT_BIE_UT = Sammlung(
        trace="Bie Ut",
        groups="Lautschrift|Bie Ut",
        kreis="Bie",
        ort="Ut",
    )
    LAUT_BIE_VD = Sammlung(
        trace="Bie Vd",
        groups="Lautschrift|Bie Vd",
        kreis="Bie",
        ort="Vd",
    )
    LAUT_BIE_VS = Sammlung(
        trace="Bie Vs",
        groups="Lautschrift|Bie Vs",
        kreis="Bie",
        ort="Vs",
    )
    LAUT_BOR_AN = Sammlung(
        trace="Bor An",
        groups="Lautschrift|Bor An",
        kreis="Bor",
        ort="An",
    )
    LAUT_BOR_BA = Sammlung(
        trace="Bor Ba",
        groups="Lautschrift|Bor Ba",
        kreis="Bor",
        ort="Ba",
    )
    LAUT_BOR_BE = Sammlung(
        trace="Bor Be",
        groups="Lautschrift|Bor Be",
        kreis="Bor",
        ort="Be",
    )
    LAUT_BOR_BH = Sammlung(
        trace="Bor Bh",
        groups="Lautschrift|Bor Bh",
        kreis="Bor",
        ort="Bh",
    )
    LAUT_BOR_BI = Sammlung(
        trace="Bor Bi",
        groups="Lautschrift|Bor Bi",
        kreis="Bor",
        ort="Bi",
    )
    LAUT_BOR_BO = Sammlung(
        trace="Bor Bo",
        groups="Lautschrift|Bor Bo",
        kreis="Bor",
        ort="Bo",
    )
    LAUT_BOR_BÜ = Sammlung(
        trace="Bor Bü",
        groups="Lautschrift|Bor Bü",
        kreis="Bor",
        ort="Bü",
    )
    LAUT_BOR_BW = Sammlung(
        trace="Bor Bw",
        groups="Lautschrift|Bor Bw",
        kreis="Bor",
        ort="Bw",
    )
    LAUT_BOR_DI = Sammlung(
        trace="Bor Di",
        groups="Lautschrift|Bor Di",
        kreis="Bor",
        ort="Di",
    )
    LAUT_BOR_GE = Sammlung(
        trace="Bor Ge",
        groups="Lautschrift|Bor Ge",
        kreis="Bor",
        ort="Ge",
    )
    LAUT_BOR_GL = Sammlung(
        trace="Bor Gl",
        groups="Lautschrift|Bor Gl",
        kreis="Bor",
        ort="Gl",
    )
    LAUT_BOR_GR = Sammlung(
        trace="Bor Gr",
        groups="Lautschrift|Bor Gr",
        kreis="Bor",
        ort="Gr",
    )
    LAUT_BOR_GW = Sammlung(
        trace="Bor Gw",
        groups="Lautschrift|Bor Gw",
        kreis="Bor",
        ort="Gw",
    )
    LAUT_BOR_HD = Sammlung(
        trace="Bor Hd",
        groups="Lautschrift|Bor Hd",
        kreis="Bor",
        ort="Hd",
    )
    LAUT_BOR_HE = Sammlung(
        trace="Bor He",
        groups="Lautschrift|Bor He",
        kreis="Bor",
        ort="He",
    )
    LAUT_BOR_HF = Sammlung(
        trace="Bor Hf",
        groups="Lautschrift|Bor Hf",
        kreis="Bor",
        ort="Hf",
    )
    LAUT_BOR_HL = Sammlung(
        trace="Bor Hl",
        groups="Lautschrift|Bor Hl",
        kreis="Bor",
        ort="Hl",
    )
    LAUT_BOR_HO = Sammlung(
        trace="Bor Ho",
        groups="Lautschrift|Bor Ho",
        kreis="Bor",
        ort="Ho",
    )
    LAUT_BOR_HÜ = Sammlung(
        trace="Bor Hü",
        groups="Lautschrift|Bor Hü",
        kreis="Bor",
        ort="Hü",
    )
    LAUT_BOR_HW = Sammlung(
        trace="Bor Hw",
        groups="Lautschrift|Bor Hw",
        kreis="Bor",
        ort="Hw",
    )
    LAUT_BOR_KG = Sammlung(
        trace="Bor Kg",
        groups="Lautschrift|Bor Kg",
        kreis="Bor",
        ort="Kg",
    )
    LAUT_BOR_KL = Sammlung(
        trace="Bor Kl",
        groups="Lautschrift|Bor Kl",
        kreis="Bor",
        ort="Kl",
    )
    LAUT_BOR_KR = Sammlung(
        trace="Bor Kr",
        groups="Lautschrift|Bor Kr",
        kreis="Bor",
        ort="Kr",
    )
    LAUT_BOR_KT = Sammlung(
        trace="Bor Kt",
        groups="Lautschrift|Bor Kt",
        kreis="Bor",
        ort="Kt",
    )
    LAUT_BOR_LI = Sammlung(
        trace="Bor Li",
        groups="Lautschrift|Bor Li",
        kreis="Bor",
        ort="Li",
    )
    LAUT_BOR_LO = Sammlung(
        trace="Bor Lo",
        groups="Lautschrift|Bor Lo",
        kreis="Bor",
        ort="Lo",
    )
    LAUT_BOR_MB = Sammlung(
        trace="Bor Mb",
        groups="Lautschrift|Bor Mb",
        kreis="Bor",
        ort="Mb",
    )
    LAUT_BOR_MU = Sammlung(
        trace="Bor Mu",
        groups="Lautschrift|Bor Mu",
        kreis="Bor",
        ort="Mu",
    )
    LAUT_BOR_MV = Sammlung(
        trace="Bor Mv",
        groups="Lautschrift|Bor Mv",
        kreis="Bor",
        ort="Mv",
    )
    LAUT_BOR_NB = Sammlung(
        trace="Bor Nb",
        groups="Lautschrift|Bor Nb",
        kreis="Bor",
        ort="Nb",
    )
    LAUT_BOR_ND = Sammlung(
        trace="Bor Nd",
        groups="Lautschrift|Bor Nd",
        kreis="Bor",
        ort="Nd",
    )
    LAUT_BOR_NV = Sammlung(
        trace="Bor Nv",
        groups="Lautschrift|Bor Nv",
        kreis="Bor",
        ort="Nv",
    )
    LAUT_BOR_PH = Sammlung(
        trace="Bor Ph",
        groups="Lautschrift|Bor Ph",
        kreis="Bor",
        ort="Ph",
    )
    LAUT_BOR_RB = Sammlung(
        trace="Bor Rb",
        groups="Lautschrift|Bor Rb",
        kreis="Bor",
        ort="Rb",
    )
    LAUT_BOR_RD = Sammlung(
        trace="Bor Rd",
        groups="Lautschrift|Bor Rd",
        kreis="Bor",
        ort="Rd",
    )
    LAUT_BOR_RF = Sammlung(
        trace="Bor Rf",
        groups="Lautschrift|Bor Rf",
        kreis="Bor",
        ort="Rf",
    )
    LAUT_BOR_RH = Sammlung(
        trace="Bor Rh",
        groups="Lautschrift|Bor Rh",
        kreis="Bor",
        ort="Rh",
    )
    LAUT_BOR_RK = Sammlung(
        trace="Bor Rk",
        groups="Lautschrift|Bor Rk",
        kreis="Bor",
        ort="Rk",
    )
    LAUT_BOR_SP = Sammlung(
        trace="Bor Sp",
        groups="Lautschrift|Bor Sp",
        kreis="Bor",
        ort="Sp",
    )
    LAUT_BOR_SS = Sammlung(
        trace="Bor Ss",
        groups="Lautschrift|Bor Ss",
        kreis="Bor",
        ort="Ss",
    )
    LAUT_BOR_SU = Sammlung(
        trace="Bor Su",
        groups="Lautschrift|Bor Su",
        kreis="Bor",
        ort="Su",
    )
    LAUT_BOR_VE = Sammlung(
        trace="Bor Ve",
        groups="Lautschrift|Bor Ve",
        kreis="Bor",
        ort="Ve",
    )
    LAUT_BOR_VH = Sammlung(
        trace="Bor Vh",
        groups="Lautschrift|Bor Vh",
        kreis="Bor",
        ort="Vh",
    )
    LAUT_BOR_WE = Sammlung(
        trace="Bor We",
        groups="Lautschrift|Bor We",
        kreis="Bor",
        ort="We",
    )
    LAUT_BOR_WS = Sammlung(
        trace="Bor Ws",
        groups="Lautschrift|Bor Ws",
        kreis="Bor",
        ort="Ws",
    )
    LAUT_BRG_HE = Sammlung(
        trace="Brg He",
        groups="Lautschrift|Brg He",
        kreis="Brg",
        ort="He",
    )
    LAUT_BRG_HW = Sammlung(
        trace="Brg Hw",
        groups="Lautschrift|Brg Hw",
        kreis="Brg",
        ort="Hw",
    )
    LAUT_BRG_LF = Sammlung(
        trace="Brg Lf",
        groups="Lautschrift|Brg Lf",
        kreis="Brg",
        ort="Lf",
    )
    LAUT_BRG_NB = Sammlung(
        trace="Brg Nb",
        groups="Lautschrift|Brg Nb",
        kreis="Brg",
        ort="Nb",
    )
    LAUT_BRG_RW = Sammlung(
        trace="Brg Rw",
        groups="Lautschrift|Brg Rw",
        kreis="Brg",
        ort="Rw",
    )
    LAUT_BRG_WS = Sammlung(
        trace="Brg Ws",
        groups="Lautschrift|Brg Ws",
        kreis="Brg",
        ort="Ws",
    )
    LAUT_BRI_AA = Sammlung(
        trace="Bri Aa",
        groups="Lautschrift|Bri Aa",
        kreis="Bri",
        ort="Aa",
    )
    LAUT_BRI_AB = Sammlung(
        trace="Bri Ab",
        groups="Lautschrift|Bri Ab",
        kreis="Bri",
        ort="Ab",
    )
    LAUT_BRI_AF = Sammlung(
        trace="Bri Af",
        groups="Lautschrift|Bri Af",
        kreis="Bri",
        ort="Af",
    )
    LAUT_BRI_AH = Sammlung(
        trace="Bri Ah",
        groups="Lautschrift|Bri Ah",
        kreis="Bri",
        ort="Ah",
    )
    LAUT_BRI_AL = Sammlung(
        trace="Bri Al",
        groups="Lautschrift|Bri Al",
        kreis="Bri",
        ort="Al",
    )
    LAUT_BRI_BE = Sammlung(
        trace="Bri Be",
        groups="Lautschrift|Bri Be",
        kreis="Bri",
        ort="Be",
    )
    LAUT_BRI_BH = Sammlung(
        trace="Bri Bh",
        groups="Lautschrift|Bri Bh",
        kreis="Bri",
        ort="Bh",
    )
    LAUT_BRI_BI = Sammlung(
        trace="Bri Bi",
        groups="Lautschrift|Bri Bi",
        kreis="Bri",
        ort="Bi",
    )
    LAUT_BRI_BK = Sammlung(
        trace="Bri Bk",
        groups="Lautschrift|Bri Bk",
        kreis="Bri",
        ort="Bk",
    )
    LAUT_BRI_BO = Sammlung(
        trace="Bri Bo",
        groups="Lautschrift|Bri Bo",
        kreis="Bri",
        ort="Bo",
    )
    LAUT_BRI_BR = Sammlung(
        trace="Bri Br",
        groups="Lautschrift|Bri Br",
        kreis="Bri",
        ort="Br",
    )
    LAUT_BRI_DF = Sammlung(
        trace="Bri Df",
        groups="Lautschrift|Bri Df",
        kreis="Bri",
        ort="Df",
    )
    LAUT_BRI_DR = Sammlung(
        trace="Bri Dr",
        groups="Lautschrift|Bri Dr",
        kreis="Bri",
        ort="Dr",
    )
    LAUT_BRI_DÜ = Sammlung(
        trace="Bri Dü",
        groups="Lautschrift|Bri Dü",
        kreis="Bri",
        ort="Dü",
    )
    LAUT_BRI_EH = Sammlung(
        trace="Bri Eh",
        groups="Lautschrift|Bri Eh",
        kreis="Bri",
        ort="Eh",
    )
    LAUT_BRI_EL = Sammlung(
        trace="Bri El",
        groups="Lautschrift|Bri El",
        kreis="Bri",
        ort="El",
    )
    LAUT_BRI_EP = Sammlung(
        trace="Bri Ep",
        groups="Lautschrift|Bri Ep",
        kreis="Bri",
        ort="Ep",
    )
    LAUT_BRI_ER = Sammlung(
        trace="Bri Er",
        groups="Lautschrift|Bri Er",
        kreis="Bri",
        ort="Er",
    )
    LAUT_BRI_ES = Sammlung(
        trace="Bri Es",
        groups="Lautschrift|Bri Es",
        kreis="Bri",
        ort="Es",
    )
    LAUT_BRI_GB = Sammlung(
        trace="Bri Gb",
        groups="Lautschrift|Bri Gb",
        kreis="Bri",
        ort="Gb",
    )
    LAUT_BRI_GH = Sammlung(
        trace="Bri Gh",
        groups="Lautschrift|Bri Gh",
        kreis="Bri",
        ort="Gh",
    )
    LAUT_BRI_HA = Sammlung(
        trace="Bri Ha",
        groups="Lautschrift|Bri Ha",
        kreis="Bri",
        ort="Ha",
    )
    LAUT_BRI_HE = Sammlung(
        trace="Bri He",
        groups="Lautschrift|Bri He",
        kreis="Bri",
        ort="He",
    )
    LAUT_BRI_HF = Sammlung(
        trace="Bri Hf",
        groups="Lautschrift|Bri Hf",
        kreis="Bri",
        ort="Hf",
    )
    LAUT_BRI_HH = Sammlung(
        trace="Bri Hh",
        groups="Lautschrift|Bri Hh",
        kreis="Bri",
        ort="Hh",
    )
    LAUT_BRI_HL = Sammlung(
        trace="Bri Hl",
        groups="Lautschrift|Bri Hl",
        kreis="Bri",
        ort="Hl",
    )
    LAUT_BRI_HO = Sammlung(
        trace="Bri Ho",
        groups="Lautschrift|Bri Ho",
        kreis="Bri",
        ort="Ho",
    )
    LAUT_BRI_KA = Sammlung(
        trace="Bri Ka",
        groups="Lautschrift|Bri Ka",
        kreis="Bri",
        ort="Ka",
    )
    LAUT_BRI_KB = Sammlung(
        trace="Bri Kb",
        groups="Lautschrift|Bri Kb",
        kreis="Bri",
        ort="Kb",
    )
    LAUT_BRI_KS = Sammlung(
        trace="Bri Ks",
        groups="Lautschrift|Bri Ks",
        kreis="Bri",
        ort="Ks",
    )
    LAUT_BRI_LI = Sammlung(
        trace="Bri Li",
        groups="Lautschrift|Bri Li",
        kreis="Bri",
        ort="Li",
    )
    LAUT_BRI_LM = Sammlung(
        trace="Bri Lm",
        groups="Lautschrift|Bri Lm",
        kreis="Bri",
        ort="Lm",
    )
    LAUT_BRI_MA = Sammlung(
        trace="Bri Ma",
        groups="Lautschrift|Bri Ma",
        kreis="Bri",
        ort="Ma",
    )
    LAUT_BRI_MB = Sammlung(
        trace="Bri Mb",
        groups="Lautschrift|Bri Mb",
        kreis="Bri",
        ort="Mb",
    )
    LAUT_BRI_MF = Sammlung(
        trace="Bri Mf",
        groups="Lautschrift|Bri Mf",
        kreis="Bri",
        ort="Mf",
    )
    LAUT_BRI_MH = Sammlung(
        trace="Bri Mh",
        groups="Lautschrift|Bri Mh",
        kreis="Bri",
        ort="Mh",
    )
    LAUT_BRI_ML = Sammlung(
        trace="Bri Ml",
        groups="Lautschrift|Bri Ml",
        kreis="Bri",
        ort="Ml",
    )
    LAUT_BRI_NA = Sammlung(
        trace="Bri Na",
        groups="Lautschrift|Bri Na",
        kreis="Bri",
        ort="Na",
    )
    LAUT_BRI_NE = Sammlung(
        trace="Bri Ne",
        groups="Lautschrift|Bri Ne",
        kreis="Bri",
        ort="Ne",
    )
    LAUT_BRI_NF = Sammlung(
        trace="Bri Nf",
        groups="Lautschrift|Bri Nf",
        kreis="Bri",
        ort="Nf",
    )
    LAUT_BRI_NM = Sammlung(
        trace="Bri Nm",
        groups="Lautschrift|Bri Nm",
        kreis="Bri",
        ort="Nm",
    )
    LAUT_BRI_OB = Sammlung(
        trace="Bri Ob",
        groups="Lautschrift|Bri Ob",
        kreis="Bri",
        ort="Ob",
    )
    LAUT_BRI_OM = Sammlung(
        trace="Bri Om",
        groups="Lautschrift|Bri Om",
        kreis="Bri",
        ort="Om",
    )
    LAUT_BRI_OS = Sammlung(
        trace="Bri Os",
        groups="Lautschrift|Bri Os",
        kreis="Bri",
        ort="Os",
    )
    LAUT_BRI_PA = Sammlung(
        trace="Bri Pa",
        groups="Lautschrift|Bri Pa",
        kreis="Bri",
        ort="Pa",
    )
    LAUT_BRI_PB = Sammlung(
        trace="Bri Pb",
        groups="Lautschrift|Bri Pb",
        kreis="Bri",
        ort="Pb",
    )
    LAUT_BRI_RA = Sammlung(
        trace="Bri Ra",
        groups="Lautschrift|Bri Ra",
        kreis="Bri",
        ort="Ra",
    )
    LAUT_BRI_RB = Sammlung(
        trace="Bri Rb",
        groups="Lautschrift|Bri Rb",
        kreis="Bri",
        ort="Rb",
    )
    LAUT_BRI_RF = Sammlung(
        trace="Bri Rf",
        groups="Lautschrift|Bri Rf",
        kreis="Bri",
        ort="Rf",
    )
    LAUT_BRI_RI = Sammlung(
        trace="Bri Ri",
        groups="Lautschrift|Bri Ri",
        kreis="Bri",
        ort="Ri",
    )
    LAUT_BRI_SB = Sammlung(
        trace="Bri Sb",
        groups="Lautschrift|Bri Sb",
        kreis="Bri",
        ort="Sb",
    )
    LAUT_BRI_SH = Sammlung(
        trace="Bri Sh",
        groups="Lautschrift|Bri Sh",
        kreis="Bri",
        ort="Sh",
    )
    LAUT_BRI_SI = Sammlung(
        trace="Bri Si",
        groups="Lautschrift|Bri Si",
        kreis="Bri",
        ort="Si",
    )
    LAUT_BRI_TI = Sammlung(
        trace="Bri Ti",
        groups="Lautschrift|Bri Ti",
        kreis="Bri",
        ort="Ti",
    )
    LAUT_BRI_TÜ = Sammlung(
        trace="Bri Tü",
        groups="Lautschrift|Bri Tü",
        kreis="Bri",
        ort="Tü",
    )
    LAUT_BRI_UD = Sammlung(
        trace="Bri Ud",
        groups="Lautschrift|Bri Ud",
        kreis="Bri",
        ort="Ud",
    )
    LAUT_BRI_WB = Sammlung(
        trace="Bri Wb",
        groups="Lautschrift|Bri Wb",
        kreis="Bri",
        ort="Wb",
    )
    LAUT_BRI_WH = Sammlung(
        trace="Bri Wh",
        groups="Lautschrift|Bri Wh",
        kreis="Bri",
        ort="Wh",
    )
    LAUT_BRI_WU = Sammlung(
        trace="Bri Wu",
        groups="Lautschrift|Bri Wu",
        kreis="Bri",
        ort="Wu",
    )
    LAUT_BRI_ZÜ = Sammlung(
        trace="Bri Zü",
        groups="Lautschrift|Bri Zü",
        kreis="Bri",
        ort="Zü",
    )
    LAUT_BÜK_AH = Sammlung(
        trace="Bük Ah",
        groups="Lautschrift|Bük Ah",
        kreis="Bük",
        ort="Ah",
    )
    LAUT_BÜK_BÜ = Sammlung(
        trace="Bük Bü",
        groups="Lautschrift|Bük Bü",
        kreis="Bük",
        ort="Bü",
    )
    LAUT_BÜK_EV = Sammlung(
        trace="Bük Ev",
        groups="Lautschrift|Bük Ev",
        kreis="Bük",
        ort="Ev",
    )
    LAUT_BÜK_GD = Sammlung(
        trace="Bük Gd",
        groups="Lautschrift|Bük Gd",
        kreis="Bük",
        ort="Gd",
    )
    LAUT_BÜK_HE = Sammlung(
        trace="Bük He",
        groups="Lautschrift|Bük He",
        kreis="Bük",
        ort="He",
    )
    LAUT_BÜK_KH = Sammlung(
        trace="Bük Kh",
        groups="Lautschrift|Bük Kh",
        kreis="Bük",
        ort="Kh",
    )
    LAUT_BÜK_LU = Sammlung(
        trace="Bük Lu",
        groups="Lautschrift|Bük Lu",
        kreis="Bük",
        ort="Lu",
    )
    LAUT_BÜK_ME = Sammlung(
        trace="Bük Me",
        groups="Lautschrift|Bük Me",
        kreis="Bük",
        ort="Me",
    )
    LAUT_BÜK_PE = Sammlung(
        trace="Bük Pe",
        groups="Lautschrift|Bük Pe",
        kreis="Bük",
        ort="Pe",
    )
    LAUT_BÜK_RÖ = Sammlung(
        trace="Bük Rö",
        groups="Lautschrift|Bük Rö",
        kreis="Bük",
        ort="Rö",
    )
    LAUT_BÜK_RU = Sammlung(
        trace="Bük Ru",
        groups="Lautschrift|Bük Ru",
        kreis="Bük",
        ort="Ru",
    )
    LAUT_BÜK_SB = Sammlung(
        trace="Bük Sb",
        groups="Lautschrift|Bük Sb",
        kreis="Bük",
        ort="Sb",
    )
    LAUT_BÜK_SC = Sammlung(
        trace="Bük Sc",
        groups="Lautschrift|Bük Sc",
        kreis="Bük",
        ort="Sc",
    )
    LAUT_BÜK_SH = Sammlung(
        trace="Bük Sh",
        groups="Lautschrift|Bük Sh",
        kreis="Bük",
        ort="Sh",
    )
    LAUT_BÜK_ST = Sammlung(
        trace="Bük St",
        groups="Lautschrift|Bük St",
        kreis="Bük",
        ort="St",
    )
    LAUT_BÜK_VE = Sammlung(
        trace="Bük Ve",
        groups="Lautschrift|Bük Ve",
        kreis="Bük",
        ort="Ve",
    )
    LAUT_BÜK_WI = Sammlung(
        trace="Bük Wi",
        groups="Lautschrift|Bük Wi",
        kreis="Bük",
        ort="Wi",
    )
    LAUT_BÜR_AD = Sammlung(
        trace="Bür Ad",
        groups="Lautschrift|Bür Ad",
        kreis="Bür",
        ort="Ad",
    )
    LAUT_BÜR_AN = Sammlung(
        trace="Bür An",
        groups="Lautschrift|Bür An",
        kreis="Bür",
        ort="An",
    )
    LAUT_BÜR_AS = Sammlung(
        trace="Bür As",
        groups="Lautschrift|Bür As",
        kreis="Bür",
        ort="As",
    )
    LAUT_BÜR_AT = Sammlung(
        trace="Bür At",
        groups="Lautschrift|Bür At",
        kreis="Bür",
        ort="At",
    )
    LAUT_BÜR_BE = Sammlung(
        trace="Bür Be",
        groups="Lautschrift|Bür Be",
        kreis="Bür",
        ort="Be",
    )
    LAUT_BÜR_BH = Sammlung(
        trace="Bür Bh",
        groups="Lautschrift|Bür Bh",
        kreis="Bür",
        ort="Bh",
    )
    LAUT_BÜR_BL = Sammlung(
        trace="Bür Bl",
        groups="Lautschrift|Bür Bl",
        kreis="Bür",
        ort="Bl",
    )
    LAUT_BÜR_BN = Sammlung(
        trace="Bür Bn",
        groups="Lautschrift|Bür Bn",
        kreis="Bür",
        ort="Bn",
    )
    LAUT_BÜR_BO = Sammlung(
        trace="Bür Bo",
        groups="Lautschrift|Bür Bo",
        kreis="Bür",
        ort="Bo",
    )
    LAUT_BÜR_BR = Sammlung(
        trace="Bür Br",
        groups="Lautschrift|Bür Br",
        kreis="Bür",
        ort="Br",
    )
    LAUT_BÜR_BÜ = Sammlung(
        trace="Bür Bü",
        groups="Lautschrift|Bür Bü",
        kreis="Bür",
        ort="Bü",
    )
    LAUT_BÜR_DH = Sammlung(
        trace="Bür Dh",
        groups="Lautschrift|Bür Dh",
        kreis="Bür",
        ort="Dh",
    )
    LAUT_BÜR_EB = Sammlung(
        trace="Bür Eb",
        groups="Lautschrift|Bür Eb",
        kreis="Bür",
        ort="Eb",
    )
    LAUT_BÜR_EI = Sammlung(
        trace="Bür Ei",
        groups="Lautschrift|Bür Ei",
        kreis="Bür",
        ort="Ei",
    )
    LAUT_BÜR_EL = Sammlung(
        trace="Bür El",
        groups="Lautschrift|Bür El",
        kreis="Bür",
        ort="El",
    )
    LAUT_BÜR_ES = Sammlung(
        trace="Bür Es",
        groups="Lautschrift|Bür Es",
        kreis="Bür",
        ort="Es",
    )
    LAUT_BÜR_ET = Sammlung(
        trace="Bür Et",
        groups="Lautschrift|Bür Et",
        kreis="Bür",
        ort="Et",
    )
    LAUT_BÜR_FÜ = Sammlung(
        trace="Bür Fü",
        groups="Lautschrift|Bür Fü",
        kreis="Bür",
        ort="Fü",
    )
    LAUT_BÜR_GA = Sammlung(
        trace="Bür Ga",
        groups="Lautschrift|Bür Ga",
        kreis="Bür",
        ort="Ga",
    )
    LAUT_BÜR_GR = Sammlung(
        trace="Bür Gr",
        groups="Lautschrift|Bür Gr",
        kreis="Bür",
        ort="Gr",
    )
    LAUT_BÜR_HA = Sammlung(
        trace="Bür Ha",
        groups="Lautschrift|Bür Ha",
        kreis="Bür",
        ort="Ha",
    )
    LAUT_BÜR_HB = Sammlung(
        trace="Bür Hb",
        groups="Lautschrift|Bür Hb",
        kreis="Bür",
        ort="Hb",
    )
    LAUT_BÜR_HD = Sammlung(
        trace="Bür Hd",
        groups="Lautschrift|Bür Hd",
        kreis="Bür",
        ort="Hd",
    )
    LAUT_BÜR_HE = Sammlung(
        trace="Bür He",
        groups="Lautschrift|Bür He",
        kreis="Bür",
        ort="He",
    )
    LAUT_BÜR_HG = Sammlung(
        trace="Bür Hg",
        groups="Lautschrift|Bür Hg",
        kreis="Bür",
        ort="Hg",
    )
    LAUT_BÜR_HH = Sammlung(
        trace="Bür Hh",
        groups="Lautschrift|Bür Hh",
        kreis="Bür",
        ort="Hh",
    )
    LAUT_BÜR_HL = Sammlung(
        trace="Bür Hl",
        groups="Lautschrift|Bür Hl",
        kreis="Bür",
        ort="Hl",
    )
    LAUT_BÜR_HO = Sammlung(
        trace="Bür Ho",
        groups="Lautschrift|Bür Ho",
        kreis="Bür",
        ort="Ho",
    )
    LAUT_BÜR_HÖ = Sammlung(
        trace="Bür Hö",
        groups="Lautschrift|Bür Hö",
        kreis="Bür",
        ort="Hö",
    )
    LAUT_BÜR_HR = Sammlung(
        trace="Bür Hr",
        groups="Lautschrift|Bür Hr",
        kreis="Bür",
        ort="Hr",
    )
    LAUT_BÜR_IH = Sammlung(
        trace="Bür Ih",
        groups="Lautschrift|Bür Ih",
        kreis="Bür",
        ort="Ih",
    )
    LAUT_BÜR_KL = Sammlung(
        trace="Bür Kl",
        groups="Lautschrift|Bür Kl",
        kreis="Bür",
        ort="Kl",
    )
    LAUT_BÜR_LB = Sammlung(
        trace="Bür Lb",
        groups="Lautschrift|Bür Lb",
        kreis="Bür",
        ort="Lb",
    )
    LAUT_BÜR_LI = Sammlung(
        trace="Bür Li",
        groups="Lautschrift|Bür Li",
        kreis="Bür",
        ort="Li",
    )
    LAUT_BÜR_MA = Sammlung(
        trace="Bür Ma",
        groups="Lautschrift|Bür Ma",
        kreis="Bür",
        ort="Ma",
    )
    LAUT_BÜR_ME = Sammlung(
        trace="Bür Me",
        groups="Lautschrift|Bür Me",
        kreis="Bür",
        ort="Me",
    )
    LAUT_BÜR_MH = Sammlung(
        trace="Bür Mh",
        groups="Lautschrift|Bür Mh",
        kreis="Bür",
        ort="Mh",
    )
    LAUT_BÜR_NT = Sammlung(
        trace="Bür Nt",
        groups="Lautschrift|Bür Nt",
        kreis="Bür",
        ort="Nt",
    )
    LAUT_BÜR_ÖD = Sammlung(
        trace="Bür Öd",
        groups="Lautschrift|Bür Öd",
        kreis="Bür",
        ort="Öd",
    )
    LAUT_BÜR_OT = Sammlung(
        trace="Bür Ot",
        groups="Lautschrift|Bür Ot",
        kreis="Bür",
        ort="Ot",
    )
    LAUT_BÜR_RE = Sammlung(
        trace="Bür Re",
        groups="Lautschrift|Bür Re",
        kreis="Bür",
        ort="Re",
    )
    LAUT_BÜR_RI = Sammlung(
        trace="Bür Ri",
        groups="Lautschrift|Bür Ri",
        kreis="Bür",
        ort="Ri",
    )
    LAUT_BÜR_SC = Sammlung(
        trace="Bür Sc",
        groups="Lautschrift|Bür Sc",
        kreis="Bür",
        ort="Sc",
    )
    LAUT_BÜR_SH = Sammlung(
        trace="Bür Sh",
        groups="Lautschrift|Bür Sh",
        kreis="Bür",
        ort="Sh",
    )
    LAUT_BÜR_SI = Sammlung(
        trace="Bür Si",
        groups="Lautschrift|Bür Si",
        kreis="Bür",
        ort="Si",
    )
    LAUT_BÜR_SK = Sammlung(
        trace="Bür Sk",
        groups="Lautschrift|Bür Sk",
        kreis="Bür",
        ort="Sk",
    )
    LAUT_BÜR_TH = Sammlung(
        trace="Bür Th",
        groups="Lautschrift|Bür Th",
        kreis="Bür",
        ort="Th",
    )
    LAUT_BÜR_UP = Sammlung(
        trace="Bür Up",
        groups="Lautschrift|Bür Up",
        kreis="Bür",
        ort="Up",
    )
    LAUT_BÜR_VE = Sammlung(
        trace="Bür Ve",
        groups="Lautschrift|Bür Ve",
        kreis="Bür",
        ort="Ve",
    )
    LAUT_BÜR_VN = Sammlung(
        trace="Bür Vn",
        groups="Lautschrift|Bür Vn",
        kreis="Bür",
        ort="Vn",
    )
    LAUT_BÜR_WB = Sammlung(
        trace="Bür Wb",
        groups="Lautschrift|Bür Wb",
        kreis="Bür",
        ort="Wb",
    )
    LAUT_BÜR_WE = Sammlung(
        trace="Bür We",
        groups="Lautschrift|Bür We",
        kreis="Bür",
        ort="We",
    )
    LAUT_BÜR_WH = Sammlung(
        trace="Bür Wh",
        groups="Lautschrift|Bür Wh",
        kreis="Bür",
        ort="Wh",
    )
    LAUT_BÜR_WI = Sammlung(
        trace="Bür Wi",
        groups="Lautschrift|Bür Wi",
        kreis="Bür",
        ort="Wi",
    )
    LAUT_BÜR_WÜ = Sammlung(
        trace="Bür Wü",
        groups="Lautschrift|Bür Wü",
        kreis="Bür",
        ort="Wü",
    )
    LAUT_BÜR_WW = Sammlung(
        trace="Bür Ww",
        groups="Lautschrift|Bür Ww",
        kreis="Bür",
        ort="Ww",
    )
    LAUT_DET_AU = Sammlung(
        trace="Det Au",
        groups="Lautschrift|Det Au",
        kreis="Det",
        ort="Au",
    )
    LAUT_DET_BB = Sammlung(
        trace="Det Bb",
        groups="Lautschrift|Det Bb",
        kreis="Det",
        ort="Bb",
    )
    LAUT_DET_BE = Sammlung(
        trace="Det Be",
        groups="Lautschrift|Det Be",
        kreis="Det",
        ort="Be",
    )
    LAUT_DET_BH = Sammlung(
        trace="Det Bh",
        groups="Lautschrift|Det Bh",
        kreis="Det",
        ort="Bh",
    )
    LAUT_DET_BI = Sammlung(
        trace="Det Bi",
        groups="Lautschrift|Det Bi",
        kreis="Det",
        ort="Bi",
    )
    LAUT_DET_BK = Sammlung(
        trace="Det Bk",
        groups="Lautschrift|Det Bk",
        kreis="Det",
        ort="Bk",
    )
    LAUT_DET_BL = Sammlung(
        trace="Det Bl",
        groups="Lautschrift|Det Bl",
        kreis="Det",
        ort="Bl",
    )
    LAUT_DET_BM = Sammlung(
        trace="Det Bm",
        groups="Lautschrift|Det Bm",
        kreis="Det",
        ort="Bm",
    )
    LAUT_DET_BR = Sammlung(
        trace="Det Br",
        groups="Lautschrift|Det Br",
        kreis="Det",
        ort="Br",
    )
    LAUT_DET_BS = Sammlung(
        trace="Det Bs",
        groups="Lautschrift|Det Bs",
        kreis="Det",
        ort="Bs",
    )
    LAUT_DET_BY = Sammlung(
        trace="Det By",
        groups="Lautschrift|Det By",
        kreis="Det",
        ort="By",
    )
    LAUT_DET_DA = Sammlung(
        trace="Det Da",
        groups="Lautschrift|Det Da",
        kreis="Det",
        ort="Da",
    )
    LAUT_DET_DB = Sammlung(
        trace="Det Db",
        groups="Lautschrift|Det Db",
        kreis="Det",
        ort="Db",
    )
    LAUT_DET_DE = Sammlung(
        trace="Det De",
        groups="Lautschrift|Det De",
        kreis="Det",
        ort="De",
    )
    LAUT_DET_DO = Sammlung(
        trace="Det Do",
        groups="Lautschrift|Det Do",
        kreis="Det",
        ort="Do",
    )
    LAUT_DET_EB = Sammlung(
        trace="Det Eb",
        groups="Lautschrift|Det Eb",
        kreis="Det",
        ort="Eb",
    )
    LAUT_DET_EH = Sammlung(
        trace="Det Eh",
        groups="Lautschrift|Det Eh",
        kreis="Det",
        ort="Eh",
    )
    LAUT_DET_EL = Sammlung(
        trace="Det El",
        groups="Lautschrift|Det El",
        kreis="Det",
        ort="El",
    )
    LAUT_DET_ER = Sammlung(
        trace="Det Er",
        groups="Lautschrift|Det Er",
        kreis="Det",
        ort="Er",
    )
    LAUT_DET_FA = Sammlung(
        trace="Det Fa",
        groups="Lautschrift|Det Fa",
        kreis="Det",
        ort="Fa",
    )
    LAUT_DET_FH = Sammlung(
        trace="Det Fh",
        groups="Lautschrift|Det Fh",
        kreis="Det",
        ort="Fh",
    )
    LAUT_DET_GB = Sammlung(
        trace="Det Gb",
        groups="Lautschrift|Det Gb",
        kreis="Det",
        ort="Gb",
    )
    LAUT_DET_GR = Sammlung(
        trace="Det Gr",
        groups="Lautschrift|Det Gr",
        kreis="Det",
        ort="Gr",
    )
    LAUT_DET_HB = Sammlung(
        trace="Det Hb",
        groups="Lautschrift|Det Hb",
        kreis="Det",
        ort="Hb",
    )
    LAUT_DET_HD = Sammlung(
        trace="Det Hd",
        groups="Lautschrift|Det Hd",
        kreis="Det",
        ort="Hd",
    )
    LAUT_DET_HE = Sammlung(
        trace="Det He",
        groups="Lautschrift|Det He",
        kreis="Det",
        ort="He",
    )
    LAUT_DET_HH = Sammlung(
        trace="Det Hh",
        groups="Lautschrift|Det Hh",
        kreis="Det",
        ort="Hh",
    )
    LAUT_DET_HI = Sammlung(
        trace="Det Hi",
        groups="Lautschrift|Det Hi",
        kreis="Det",
        ort="Hi",
    )
    LAUT_DET_HK = Sammlung(
        trace="Det Hk",
        groups="Lautschrift|Det Hk",
        kreis="Det",
        ort="Hk",
    )
    LAUT_DET_HM = Sammlung(
        trace="Det Hm",
        groups="Lautschrift|Det Hm",
        kreis="Det",
        ort="Hm",
    )
    LAUT_DET_HN = Sammlung(
        trace="Det Hn",
        groups="Lautschrift|Det Hn",
        kreis="Det",
        ort="Hn",
    )
    LAUT_DET_HO = Sammlung(
        trace="Det Ho",
        groups="Lautschrift|Det Ho",
        kreis="Det",
        ort="Ho",
    )
    LAUT_DET_HÖ = Sammlung(
        trace="Det Hö",
        groups="Lautschrift|Det Hö",
        kreis="Det",
        ort="Hö",
    )
    LAUT_DET_HR = Sammlung(
        trace="Det Hr",
        groups="Lautschrift|Det Hr",
        kreis="Det",
        ort="Hr",
    )
    LAUT_DET_HU = Sammlung(
        trace="Det Hu",
        groups="Lautschrift|Det Hu",
        kreis="Det",
        ort="Hu",
    )
    LAUT_DET_JE = Sammlung(
        trace="Det Je",
        groups="Lautschrift|Det Je",
        kreis="Det",
        ort="Je",
    )
    LAUT_DET_IH = Sammlung(
        trace="Det Ih",
        groups="Lautschrift|Det Ih",
        kreis="Det",
        ort="Ih",
    )
    LAUT_DET_IS = Sammlung(
        trace="Det Is",
        groups="Lautschrift|Det Is",
        kreis="Det",
        ort="Is",
    )
    LAUT_DET_KA = Sammlung(
        trace="Det Ka",
        groups="Lautschrift|Det Ka",
        kreis="Det",
        ort="Ka",
    )
    LAUT_DET_KL = Sammlung(
        trace="Det Kl",
        groups="Lautschrift|Det Kl",
        kreis="Det",
        ort="Kl",
    )
    LAUT_DET_KO = Sammlung(
        trace="Det Ko",
        groups="Lautschrift|Det Ko",
        kreis="Det",
        ort="Ko",
    )
    LAUT_DET_KT = Sammlung(
        trace="Det Kt",
        groups="Lautschrift|Det Kt",
        kreis="Det",
        ort="Kt",
    )
    LAUT_DET_LA = Sammlung(
        trace="Det La",
        groups="Lautschrift|Det La",
        kreis="Det",
        ort="La",
    )
    LAUT_DET_LO = Sammlung(
        trace="Det Lo",
        groups="Lautschrift|Det Lo",
        kreis="Det",
        ort="Lo",
    )
    LAUT_DET_LT = Sammlung(
        trace="Det Lt",
        groups="Lautschrift|Det Lt",
        kreis="Det",
        ort="Lt",
    )
    LAUT_DET_MA = Sammlung(
        trace="Det Ma",
        groups="Lautschrift|Det Ma",
        kreis="Det",
        ort="Ma",
    )
    LAUT_DET_MB = Sammlung(
        trace="Det Mb",
        groups="Lautschrift|Det Mb",
        kreis="Det",
        ort="Mb",
    )
    LAUT_DET_MF = Sammlung(
        trace="Det Mf",
        groups="Lautschrift|Det Mf",
        kreis="Det",
        ort="Mf",
    )
    LAUT_DET_MO = Sammlung(
        trace="Det Mo",
        groups="Lautschrift|Det Mo",
        kreis="Det",
        ort="Mo",
    )
    LAUT_DET_NH = Sammlung(
        trace="Det Nh",
        groups="Lautschrift|Det Nh",
        kreis="Det",
        ort="Nh",
    )
    LAUT_DET_NI = Sammlung(
        trace="Det Ni",
        groups="Lautschrift|Det Ni",
        kreis="Det",
        ort="Ni",
    )
    LAUT_DET_OB = Sammlung(
        trace="Det Ob",
        groups="Lautschrift|Det Ob",
        kreis="Det",
        ort="Ob",
    )
    LAUT_DET_OS = Sammlung(
        trace="Det Os",
        groups="Lautschrift|Det Os",
        kreis="Det",
        ort="Os",
    )
    LAUT_DET_PI = Sammlung(
        trace="Det Pi",
        groups="Lautschrift|Det Pi",
        kreis="Det",
        ort="Pi",
    )
    LAUT_DET_PO = Sammlung(
        trace="Det Po",
        groups="Lautschrift|Det Po",
        kreis="Det",
        ort="Po",
    )
    LAUT_DET_RH = Sammlung(
        trace="Det Rh",
        groups="Lautschrift|Det Rh",
        kreis="Det",
        ort="Rh",
    )
    LAUT_DET_RI = Sammlung(
        trace="Det Ri",
        groups="Lautschrift|Det Ri",
        kreis="Det",
        ort="Ri",
    )
    LAUT_DET_RK = Sammlung(
        trace="Det Rk",
        groups="Lautschrift|Det Rk",
        kreis="Det",
        ort="Rk",
    )
    LAUT_DET_RÖ = Sammlung(
        trace="Det Rö",
        groups="Lautschrift|Det Rö",
        kreis="Det",
        ort="Rö",
    )
    LAUT_DET_SC = Sammlung(
        trace="Det Sc",
        groups="Lautschrift|Det Sc",
        kreis="Det",
        ort="Sc",
    )
    LAUT_DET_SH = Sammlung(
        trace="Det Sh",
        groups="Lautschrift|Det Sh",
        kreis="Det",
        ort="Sh",
    )
    LAUT_DET_SL = Sammlung(
        trace="Det Sl",
        groups="Lautschrift|Det Sl",
        kreis="Det",
        ort="Sl",
    )
    LAUT_DET_SM = Sammlung(
        trace="Det Sm",
        groups="Lautschrift|Det Sm",
        kreis="Det",
        ort="Sm",
    )
    LAUT_DET_ST = Sammlung(
        trace="Det St",
        groups="Lautschrift|Det St",
        kreis="Det",
        ort="St",
    )
    LAUT_DET_SW = Sammlung(
        trace="Det Sw",
        groups="Lautschrift|Det Sw",
        kreis="Det",
        ort="Sw",
    )
    LAUT_DET_VA = Sammlung(
        trace="Det Va",
        groups="Lautschrift|Det Va",
        kreis="Det",
        ort="Va",
    )
    LAUT_DET_VR = Sammlung(
        trace="Det Vr",
        groups="Lautschrift|Det Vr",
        kreis="Det",
        ort="Vr",
    )
    LAUT_DET_WF = Sammlung(
        trace="Det Wf",
        groups="Lautschrift|Det Wf",
        kreis="Det",
        ort="Wf",
    )
    LAUT_DET_WH = Sammlung(
        trace="Det Wh",
        groups="Lautschrift|Det Wh",
        kreis="Det",
        ort="Wh",
    )
    LAUT_DET_WÖ = Sammlung(
        trace="Det Wö",
        groups="Lautschrift|Det Wö",
        kreis="Det",
        ort="Wö",
    )
    LAUT_DIE_AS = Sammlung(
        trace="Die As",
        groups="Lautschrift|Die As",
        kreis="Die",
        ort="As",
    )
    LAUT_DIE_BA = Sammlung(
        trace="Die Ba",
        groups="Lautschrift|Die Ba",
        kreis="Die",
        ort="Ba",
    )
    LAUT_DIE_BB = Sammlung(
        trace="Die Bb",
        groups="Lautschrift|Die Bb",
        kreis="Die",
        ort="Bb",
    )
    LAUT_DIE_BV = Sammlung(
        trace="Die Bv",
        groups="Lautschrift|Die Bv",
        kreis="Die",
        ort="Bv",
    )
    LAUT_DIE_DI = Sammlung(
        trace="Die Di",
        groups="Lautschrift|Die Di",
        kreis="Die",
        ort="Di",
    )
    LAUT_DIE_DÖ = Sammlung(
        trace="Die Dö",
        groups="Lautschrift|Die Dö",
        kreis="Die",
        ort="Dö",
    )
    LAUT_DIE_HE = Sammlung(
        trace="Die He",
        groups="Lautschrift|Die He",
        kreis="Die",
        ort="He",
    )
    LAUT_DIE_HF = Sammlung(
        trace="Die Hf",
        groups="Lautschrift|Die Hf",
        kreis="Die",
        ort="Hf",
    )
    LAUT_DIE_HH = Sammlung(
        trace="Die Hh",
        groups="Lautschrift|Die Hh",
        kreis="Die",
        ort="Hh",
    )
    LAUT_DIE_HÜ = Sammlung(
        trace="Die Hü",
        groups="Lautschrift|Die Hü",
        kreis="Die",
        ort="Hü",
    )
    LAUT_DIE_KI = Sammlung(
        trace="Die Ki",
        groups="Lautschrift|Die Ki",
        kreis="Die",
        ort="Ki",
    )
    LAUT_DIE_LB = Sammlung(
        trace="Die Lb",
        groups="Lautschrift|Die Lb",
        kreis="Die",
        ort="Lb",
    )
    LAUT_DIE_LE = Sammlung(
        trace="Die Le",
        groups="Lautschrift|Die Le",
        kreis="Die",
        ort="Le",
    )
    LAUT_DIE_MA = Sammlung(
        trace="Die Ma",
        groups="Lautschrift|Die Ma",
        kreis="Die",
        ort="Ma",
    )
    LAUT_DIE_ST = Sammlung(
        trace="Die St",
        groups="Lautschrift|Die St",
        kreis="Die",
        ort="St",
    )
    LAUT_DIE_VA = Sammlung(
        trace="Die Va",
        groups="Lautschrift|Die Va",
        kreis="Die",
        ort="Va",
    )
    LAUT_DIE_WH = Sammlung(
        trace="Die Wh",
        groups="Lautschrift|Die Wh",
        kreis="Die",
        ort="Wh",
    )
    LAUT_DIE_WF = Sammlung(
        trace="Die Wf",
        groups="Lautschrift|Die Wf",
        kreis="Die",
        ort="Wf",
    )
    LAUT_DOR_AP = Sammlung(
        trace="Dor Ap",
        groups="Lautschrift|Dor Ap",
        kreis="Dor",
        ort="Ap",
    )
    LAUT_DOR_AS = Sammlung(
        trace="Dor As",
        groups="Lautschrift|Dor As",
        kreis="Dor",
        ort="As",
    )
    LAUT_DOR_BA = Sammlung(
        trace="Dor Ba",
        groups="Lautschrift|Dor Ba",
        kreis="Dor",
        ort="Ba",
    )
    LAUT_DOR_BB = Sammlung(
        trace="Dor Bb",
        groups="Lautschrift|Dor Bb",
        kreis="Dor",
        ort="Bb",
    )
    LAUT_DOR_BH = Sammlung(
        trace="Dor Bh",
        groups="Lautschrift|Dor Bh",
        kreis="Dor",
        ort="Bh",
    )
    LAUT_DOR_BK = Sammlung(
        trace="Dor Bk",
        groups="Lautschrift|Dor Bk",
        kreis="Dor",
        ort="Bk",
    )
    LAUT_DOR_BO = Sammlung(
        trace="Dor Bo",
        groups="Lautschrift|Dor Bo",
        kreis="Dor",
        ort="Bo",
    )
    LAUT_DOR_BÖ = Sammlung(
        trace="Dor Bö",
        groups="Lautschrift|Dor Bö",
        kreis="Dor",
        ort="Bö",
    )
    LAUT_DOR_BR = Sammlung(
        trace="Dor Br",
        groups="Lautschrift|Dor Br",
        kreis="Dor",
        ort="Br",
    )
    LAUT_DOR_DD = Sammlung(
        trace="Dor Dd",
        groups="Lautschrift|Dor Dd",
        kreis="Dor",
        ort="Dd",
    )
    LAUT_DOR_DE = Sammlung(
        trace="Dor De",
        groups="Lautschrift|Dor De",
        kreis="Dor",
        ort="De",
    )
    LAUT_DOR_DO = Sammlung(
        trace="Dor Do",
        groups="Lautschrift|Dor Do",
        kreis="Dor",
        ort="Do",
    )
    LAUT_DOR_EI = Sammlung(
        trace="Dor Ei",
        groups="Lautschrift|Dor Ei",
        kreis="Dor",
        ort="Ei",
    )
    LAUT_DOR_EV = Sammlung(
        trace="Dor Ev",
        groups="Lautschrift|Dor Ev",
        kreis="Dor",
        ort="Ev",
    )
    LAUT_DOR_GB = Sammlung(
        trace="Dor Gb",
        groups="Lautschrift|Dor Gb",
        kreis="Dor",
        ort="Gb",
    )
    LAUT_DOR_GV = Sammlung(
        trace="Dor Gv",
        groups="Lautschrift|Dor Gv",
        kreis="Dor",
        ort="Gv",
    )
    LAUT_DOR_HA = Sammlung(
        trace="Dor Ha",
        groups="Lautschrift|Dor Ha",
        kreis="Dor",
        ort="Ha",
    )
    LAUT_DOR_HH = Sammlung(
        trace="Dor Hh",
        groups="Lautschrift|Dor Hh",
        kreis="Dor",
        ort="Hh",
    )
    LAUT_DOR_HN = Sammlung(
        trace="Dor Hn",
        groups="Lautschrift|Dor Hn",
        kreis="Dor",
        ort="Hn",
    )
    LAUT_DOR_HÖ = Sammlung(
        trace="Dor Hö",
        groups="Lautschrift|Dor Hö",
        kreis="Dor",
        ort="Hö",
    )
    LAUT_DOR_HS = Sammlung(
        trace="Dor Hs",
        groups="Lautschrift|Dor Hs",
        kreis="Dor",
        ort="Hs",
    )
    LAUT_DOR_HU = Sammlung(
        trace="Dor Hu",
        groups="Lautschrift|Dor Hu",
        kreis="Dor",
        ort="Hu",
    )
    LAUT_DOR_KA = Sammlung(
        trace="Dor Ka",
        groups="Lautschrift|Dor Ka",
        kreis="Dor",
        ort="Ka",
    )
    LAUT_DOR_KI = Sammlung(
        trace="Dor Ki",
        groups="Lautschrift|Dor Ki",
        kreis="Dor",
        ort="Ki",
    )
    LAUT_DOR_KL = Sammlung(
        trace="Dor Kl",
        groups="Lautschrift|Dor Kl",
        kreis="Dor",
        ort="Kl",
    )
    LAUT_DOR_KN = Sammlung(
        trace="Dor Kn",
        groups="Lautschrift|Dor Kn",
        kreis="Dor",
        ort="Kn",
    )
    LAUT_DOR_KR = Sammlung(
        trace="Dor Kr",
        groups="Lautschrift|Dor Kr",
        kreis="Dor",
        ort="Kr",
    )
    LAUT_DOR_KU = Sammlung(
        trace="Dor Ku",
        groups="Lautschrift|Dor Ku",
        kreis="Dor",
        ort="Ku",
    )
    LAUT_DOR_LÖ = Sammlung(
        trace="Dor Lö",
        groups="Lautschrift|Dor Lö",
        kreis="Dor",
        ort="Lö",
    )
    LAUT_DOR_LÜ = Sammlung(
        trace="Dor Lü",
        groups="Lautschrift|Dor Lü",
        kreis="Dor",
        ort="Lü",
    )
    LAUT_DOR_MA = Sammlung(
        trace="Dor Ma",
        groups="Lautschrift|Dor Ma",
        kreis="Dor",
        ort="Ma",
    )
    LAUT_DOR_ME = Sammlung(
        trace="Dor Me",
        groups="Lautschrift|Dor Me",
        kreis="Dor",
        ort="Me",
    )
    LAUT_DOR_ÖS = Sammlung(
        trace="Dor Ös",
        groups="Lautschrift|Dor Ös",
        kreis="Dor",
        ort="Ös",
    )
    LAUT_DOR_PÖ = Sammlung(
        trace="Dor Pö",
        groups="Lautschrift|Dor Pö",
        kreis="Dor",
        ort="Pö",
    )
    LAUT_DOR_RA = Sammlung(
        trace="Dor Ra",
        groups="Lautschrift|Dor Ra",
        kreis="Dor",
        ort="Ra",
    )
    LAUT_DOR_SB = Sammlung(
        trace="Dor Sb",
        groups="Lautschrift|Dor Sb",
        kreis="Dor",
        ort="Sb",
    )
    LAUT_DOR_SC = Sammlung(
        trace="Dor Sc",
        groups="Lautschrift|Dor Sc",
        kreis="Dor",
        ort="Sc",
    )
    LAUT_DOR_SO = Sammlung(
        trace="Dor So",
        groups="Lautschrift|Dor So",
        kreis="Dor",
        ort="So",
    )
    LAUT_DOR_SO1 = Sammlung(
        trace="Dor So1",
        groups="Lautschrift|Dor So1",
        kreis="Dor",
        ort="So1",
    )
    LAUT_DOR_SÖ = Sammlung(
        trace="Dor Sö",
        groups="Lautschrift|Dor Sö",
        kreis="Dor",
        ort="Sö",
    )
    LAUT_DOR_SÜ = Sammlung(
        trace="Dor Sü",
        groups="Lautschrift|Dor Sü",
        kreis="Dor",
        ort="Sü",
    )
    LAUT_DOR_WH = Sammlung(
        trace="Dor Wh",
        groups="Lautschrift|Dor Wh",
        kreis="Dor",
        ort="Wh",
    )
    LAUT_DOR_WI = Sammlung(
        trace="Dor Wi",
        groups="Lautschrift|Dor Wi",
        kreis="Dor",
        ort="Wi",
    )
    LAUT_DOR_WL = Sammlung(
        trace="Dor Wl",
        groups="Lautschrift|Dor Wl",
        kreis="Dor",
        ort="Wl",
    )
    LAUT_ENR_AD = Sammlung(
        trace="Enr Ad",
        groups="Lautschrift|Enr Ad",
        kreis="Enr",
        ort="Ad",
    )
    LAUT_ENR_AH = Sammlung(
        trace="Enr Ah",
        groups="Lautschrift|Enr Ah",
        kreis="Enr",
        ort="Ah",
    )
    LAUT_ENR_BA = Sammlung(
        trace="Enr Ba",
        groups="Lautschrift|Enr Ba",
        kreis="Enr",
        ort="Ba",
    )
    LAUT_ENR_BE = Sammlung(
        trace="Enr Be",
        groups="Lautschrift|Enr Be",
        kreis="Enr",
        ort="Be",
    )
    LAUT_ENR_BF = Sammlung(
        trace="Enr Bf",
        groups="Lautschrift|Enr Bf",
        kreis="Enr",
        ort="Bf",
    )
    LAUT_ENR_BH = Sammlung(
        trace="Enr Bh",
        groups="Lautschrift|Enr Bh",
        kreis="Enr",
        ort="Bh",
    )
    LAUT_ENR_BL = Sammlung(
        trace="Enr Bl",
        groups="Lautschrift|Enr Bl",
        kreis="Enr",
        ort="Bl",
    )
    LAUT_ENR_BO = Sammlung(
        trace="Enr Bo",
        groups="Lautschrift|Enr Bo",
        kreis="Enr",
        ort="Bo",
    )
    LAUT_ENR_BÖ = Sammlung(
        trace="Enr Bö",
        groups="Lautschrift|Enr Bö",
        kreis="Enr",
        ort="Bö",
    )
    LAUT_ENR_BR = Sammlung(
        trace="Enr Br",
        groups="Lautschrift|Enr Br",
        kreis="Enr",
        ort="Br",
    )
    LAUT_ENR_BW = Sammlung(
        trace="Enr Bw",
        groups="Lautschrift|Enr Bw",
        kreis="Enr",
        ort="Bw",
    )
    LAUT_ENR_DA = Sammlung(
        trace="Enr Da",
        groups="Lautschrift|Enr Da",
        kreis="Enr",
        ort="Da",
    )
    LAUT_ENR_DH = Sammlung(
        trace="Enr Dh",
        groups="Lautschrift|Enr Dh",
        kreis="Enr",
        ort="Dh",
    )
    LAUT_ENR_DU = Sammlung(
        trace="Enr Du",
        groups="Lautschrift|Enr Du",
        kreis="Enr",
        ort="Du",
    )
    LAUT_ENR_EB = Sammlung(
        trace="Enr Eb",
        groups="Lautschrift|Enr Eb",
        kreis="Enr",
        ort="Eb",
    )
    LAUT_ENR_EH = Sammlung(
        trace="Enr Eh",
        groups="Lautschrift|Enr Eh",
        kreis="Enr",
        ort="Eh",
    )
    LAUT_ENR_EN = Sammlung(
        trace="Enr En",
        groups="Lautschrift|Enr En",
        kreis="Enr",
        ort="En",
    )
    LAUT_ENR_ES = Sammlung(
        trace="Enr Es",
        groups="Lautschrift|Enr Es",
        kreis="Enr",
        ort="Es",
    )
    LAUT_ENR_ET = Sammlung(
        trace="Enr Et",
        groups="Lautschrift|Enr Et",
        kreis="Enr",
        ort="Et",
    )
    LAUT_ENR_GB = Sammlung(
        trace="Enr Gb",
        groups="Lautschrift|Enr Gb",
        kreis="Enr",
        ort="Gb",
    )
    LAUT_ENR_GR = Sammlung(
        trace="Enr Gr",
        groups="Lautschrift|Enr Gr",
        kreis="Enr",
        ort="Gr",
    )
    LAUT_ENR_HA = Sammlung(
        trace="Enr Ha",
        groups="Lautschrift|Enr Ha",
        kreis="Enr",
        ort="Ha",
    )
    LAUT_ENR_HB = Sammlung(
        trace="Enr Hb",
        groups="Lautschrift|Enr Hb",
        kreis="Enr",
        ort="Hb",
    )
    LAUT_ENR_HD = Sammlung(
        trace="Enr Hd",
        groups="Lautschrift|Enr Hd",
        kreis="Enr",
        ort="Hd",
    )
    LAUT_ENR_HE = Sammlung(
        trace="Enr He",
        groups="Lautschrift|Enr He",
        kreis="Enr",
        ort="He",
    )
    LAUT_ENR_HH = Sammlung(
        trace="Enr Hh",
        groups="Lautschrift|Enr Hh",
        kreis="Enr",
        ort="Hh",
    )
    LAUT_ENR_HK = Sammlung(
        trace="Enr Hk",
        groups="Lautschrift|Enr Hk",
        kreis="Enr",
        ort="Hk",
    )
    LAUT_ENR_HO = Sammlung(
        trace="Enr Ho",
        groups="Lautschrift|Enr Ho",
        kreis="Enr",
        ort="Ho",
    )
    LAUT_ENR_HR = Sammlung(
        trace="Enr Hr",
        groups="Lautschrift|Enr Hr",
        kreis="Enr",
        ort="Hr",
    )
    LAUT_ENR_HT = Sammlung(
        trace="Enr Ht",
        groups="Lautschrift|Enr Ht",
        kreis="Enr",
        ort="Ht",
    )
    LAUT_ENR_HU = Sammlung(
        trace="Enr Hu",
        groups="Lautschrift|Enr Hu",
        kreis="Enr",
        ort="Hu",
    )
    LAUT_ENR_KH = Sammlung(
        trace="Enr Kh",
        groups="Lautschrift|Enr Kh",
        kreis="Enr",
        ort="Kh",
    )
    LAUT_ENR_LD = Sammlung(
        trace="Enr Ld",
        groups="Lautschrift|Enr Ld",
        kreis="Enr",
        ort="Ld",
    )
    LAUT_ENR_LI = Sammlung(
        trace="Enr Li",
        groups="Lautschrift|Enr Li",
        kreis="Enr",
        ort="Li",
    )
    LAUT_ENR_MI = Sammlung(
        trace="Enr Mi",
        groups="Lautschrift|Enr Mi",
        kreis="Enr",
        ort="Mi",
    )
    LAUT_ENR_MK = Sammlung(
        trace="Enr Mk",
        groups="Lautschrift|Enr Mk",
        kreis="Enr",
        ort="Mk",
    )
    LAUT_ENR_NB = Sammlung(
        trace="Enr Nb",
        groups="Lautschrift|Enr Nb",
        kreis="Enr",
        ort="Nb",
    )
    LAUT_ENR_NH = Sammlung(
        trace="Enr Nh",
        groups="Lautschrift|Enr Nh",
        kreis="Enr",
        ort="Nh",
    )
    LAUT_ENR_NS = Sammlung(
        trace="Enr Ns",
        groups="Lautschrift|Enr Ns",
        kreis="Enr",
        ort="Ns",
    )
    LAUT_ENR_NW = Sammlung(
        trace="Enr Nw",
        groups="Lautschrift|Enr Nw",
        kreis="Enr",
        ort="Nw",
    )
    LAUT_ENR_OB = Sammlung(
        trace="Enr Ob",
        groups="Lautschrift|Enr Ob",
        kreis="Enr",
        ort="Ob",
    )
    LAUT_ENR_OE = Sammlung(
        trace="Enr Oe",
        groups="Lautschrift|Enr Oe",
        kreis="Enr",
        ort="Oe",
    )
    LAUT_ENR_OS = Sammlung(
        trace="Enr Os",
        groups="Lautschrift|Enr Os",
        kreis="Enr",
        ort="Os",
    )
    LAUT_ENR_PR = Sammlung(
        trace="Enr Pr",
        groups="Lautschrift|Enr Pr",
        kreis="Enr",
        ort="Pr",
    )
    LAUT_ENR_RB = Sammlung(
        trace="Enr Rb",
        groups="Lautschrift|Enr Rb",
        kreis="Enr",
        ort="Rb",
    )
    LAUT_ENR_RU = Sammlung(
        trace="Enr Ru",
        groups="Lautschrift|Enr Ru",
        kreis="Enr",
        ort="Ru",
    )
    LAUT_ENR_SC = Sammlung(
        trace="Enr Sc",
        groups="Lautschrift|Enr Sc",
        kreis="Enr",
        ort="Sc",
    )
    LAUT_ENR_SI = Sammlung(
        trace="Enr Si",
        groups="Lautschrift|Enr Si",
        kreis="Enr",
        ort="Si",
    )
    LAUT_ENR_SP = Sammlung(
        trace="Enr Sp",
        groups="Lautschrift|Enr Sp",
        kreis="Enr",
        ort="Sp",
    )
    LAUT_ENR_ST = Sammlung(
        trace="Enr St",
        groups="Lautschrift|Enr St",
        kreis="Enr",
        ort="St",
    )
    LAUT_ENR_SW = Sammlung(
        trace="Enr Sw",
        groups="Lautschrift|Enr Sw",
        kreis="Enr",
        ort="Sw",
    )
    LAUT_ENR_VE = Sammlung(
        trace="Enr Ve",
        groups="Lautschrift|Enr Ve",
        kreis="Enr",
        ort="Ve",
    )
    LAUT_ENR_VH = Sammlung(
        trace="Enr Vh",
        groups="Lautschrift|Enr Vh",
        kreis="Enr",
        ort="Vh",
    )
    LAUT_ENR_VO = Sammlung(
        trace="Enr Vo",
        groups="Lautschrift|Enr Vo",
        kreis="Enr",
        ort="Vo",
    )
    LAUT_ENR_VÖ = Sammlung(
        trace="Enr Vö",
        groups="Lautschrift|Enr Vö",
        kreis="Enr",
        ort="Vö",
    )
    LAUT_ENR_VS = Sammlung(
        trace="Enr Vs",
        groups="Lautschrift|Enr Vs",
        kreis="Enr",
        ort="Vs",
    )
    LAUT_ENR_WA = Sammlung(
        trace="Enr Wa",
        groups="Lautschrift|Enr Wa",
        kreis="Enr",
        ort="Wa",
    )
    LAUT_ENR_WE = Sammlung(
        trace="Enr We",
        groups="Lautschrift|Enr We",
        kreis="Enr",
        ort="We",
    )
    LAUT_ENR_WP = Sammlung(
        trace="Enr Wp",
        groups="Lautschrift|Enr Wp",
        kreis="Enr",
        ort="Wp",
    )
    LAUT_ENR_WT = Sammlung(
        trace="Enr Wt",
        groups="Lautschrift|Enr Wt",
        kreis="Enr",
        ort="Wt",
    )
    LAUT_ENR_ZS = Sammlung(
        trace="Enr Zs",
        groups="Lautschrift|Enr Zs",
        kreis="Enr",
        ort="Zs",
    )
    LAUT_ESS_AE = Sammlung(
        trace="Ess Ae",
        groups="Lautschrift|Ess Ae",
        kreis="Ess",
        ort="Ae",
    )
    LAUT_ESS_BB = Sammlung(
        trace="Ess Bb",
        groups="Lautschrift|Ess Bb",
        kreis="Ess",
        ort="Bb",
    )
    LAUT_ESS_BE = Sammlung(
        trace="Ess Be",
        groups="Lautschrift|Ess Be",
        kreis="Ess",
        ort="Be",
    )
    LAUT_ESS_BF = Sammlung(
        trace="Ess Bf",
        groups="Lautschrift|Ess Bf",
        kreis="Ess",
        ort="Bf",
    )
    LAUT_ESS_BH = Sammlung(
        trace="Ess Bh",
        groups="Lautschrift|Ess Bh",
        kreis="Ess",
        ort="Bh",
    )
    LAUT_ESS_ES = Sammlung(
        trace="Ess Es",
        groups="Lautschrift|Ess Es",
        kreis="Ess",
        ort="Es",
    )
    LAUT_ESS_FB = Sammlung(
        trace="Ess Fb",
        groups="Lautschrift|Ess Fb",
        kreis="Ess",
        ort="Fb",
    )
    LAUT_ESS_FR = Sammlung(
        trace="Ess Fr",
        groups="Lautschrift|Ess Fr",
        kreis="Ess",
        ort="Fr",
    )
    LAUT_ESS_HE = Sammlung(
        trace="Ess He",
        groups="Lautschrift|Ess He",
        kreis="Ess",
        ort="He",
    )
    LAUT_ESS_HH = Sammlung(
        trace="Ess Hh",
        groups="Lautschrift|Ess Hh",
        kreis="Ess",
        ort="Hh",
    )
    LAUT_ESS_KS = Sammlung(
        trace="Ess Ks",
        groups="Lautschrift|Ess Ks",
        kreis="Ess",
        ort="Ks",
    )
    LAUT_ESS_KP = Sammlung(
        trace="Ess Kp",
        groups="Lautschrift|Ess Kp",
        kreis="Ess",
        ort="Kp",
    )
    LAUT_ESS_OF = Sammlung(
        trace="Ess Of",
        groups="Lautschrift|Ess Of",
        kreis="Ess",
        ort="Of",
    )
    LAUT_ESS_OH = Sammlung(
        trace="Ess Oh",
        groups="Lautschrift|Ess Oh",
        kreis="Ess",
        ort="Oh",
    )
    LAUT_ESS_RE = Sammlung(
        trace="Ess Re",
        groups="Lautschrift|Ess Re",
        kreis="Ess",
        ort="Re",
    )
    LAUT_ESS_SB = Sammlung(
        trace="Ess Sb",
        groups="Lautschrift|Ess Sb",
        kreis="Ess",
        ort="Sb",
    )
    LAUT_ESS_SR = Sammlung(
        trace="Ess Sr",
        groups="Lautschrift|Ess Sr",
        kreis="Ess",
        ort="Sr",
    )
    LAUT_ESS_ST = Sammlung(
        trace="Ess St",
        groups="Lautschrift|Ess St",
        kreis="Ess",
        ort="St",
    )
    LAUT_ESS_ÜR = Sammlung(
        trace="Ess Ür",
        groups="Lautschrift|Ess Ür",
        kreis="Ess",
        ort="Ür",
    )
    LAUT_GEL_BK = Sammlung(
        trace="Gel Bk",
        groups="Lautschrift|Gel Bk",
        kreis="Gel",
        ort="Bk",
    )
    LAUT_GEL_BS = Sammlung(
        trace="Gel Bs",
        groups="Lautschrift|Gel Bs",
        kreis="Gel",
        ort="Bs",
    )
    LAUT_GEL_BU = Sammlung(
        trace="Gel Bu",
        groups="Lautschrift|Gel Bu",
        kreis="Gel",
        ort="Bu",
    )
    LAUT_GEL_BX = Sammlung(
        trace="Gel Bx",
        groups="Lautschrift|Gel Bx",
        kreis="Gel",
        ort="Bx",
    )
    LAUT_GEL_GK = Sammlung(
        trace="Gel Gk",
        groups="Lautschrift|Gel Gk",
        kreis="Gel",
        ort="Gk",
    )
    LAUT_GEL_HA = Sammlung(
        trace="Gel Ha",
        groups="Lautschrift|Gel Ha",
        kreis="Gel",
        ort="Ha",
    )
    LAUT_GEL_HE = Sammlung(
        trace="Gel He",
        groups="Lautschrift|Gel He",
        kreis="Gel",
        ort="He",
    )
    LAUT_GEL_HH = Sammlung(
        trace="Gel Hh",
        groups="Lautschrift|Gel Hh",
        kreis="Gel",
        ort="Hh",
    )
    LAUT_GEL_HM = Sammlung(
        trace="Gel Hm",
        groups="Lautschrift|Gel Hm",
        kreis="Gel",
        ort="Hm",
    )
    LAUT_GEL_LT = Sammlung(
        trace="Gel Lt",
        groups="Lautschrift|Gel Lt",
        kreis="Gel",
        ort="Lt",
    )
    LAUT_GEL_RH = Sammlung(
        trace="Gel Rh",
        groups="Lautschrift|Gel Rh",
        kreis="Gel",
        ort="Rh",
    )
    LAUT_GEL_ST = Sammlung(
        trace="Gel St",
        groups="Lautschrift|Gel St",
        kreis="Gel",
        ort="St",
    )
    LAUT_GEL_ÜD = Sammlung(
        trace="Gel Üd",
        groups="Lautschrift|Gel Üd",
        kreis="Gel",
        ort="Üd",
    )
    LAUT_GEL_WA = Sammlung(
        trace="Gel Wa",
        groups="Lautschrift|Gel Wa",
        kreis="Gel",
        ort="Wa",
    )
    LAUT_GEL_WE = Sammlung(
        trace="Gel We",
        groups="Lautschrift|Gel We",
        kreis="Gel",
        ort="We",
    )
    LAUT_HAG_BO = Sammlung(
        trace="Hag Bo",
        groups="Lautschrift|Hag Bo",
        kreis="Hag",
        ort="Bo",
    )
    LAUT_HAG_EI = Sammlung(
        trace="Hag Ei",
        groups="Lautschrift|Hag Ei",
        kreis="Hag",
        ort="Ei",
    )
    LAUT_HAG_EP = Sammlung(
        trace="Hag Ep",
        groups="Lautschrift|Hag Ep",
        kreis="Hag",
        ort="Ep",
    )
    LAUT_HAG_HA = Sammlung(
        trace="Hag Ha",
        groups="Lautschrift|Hag Ha",
        kreis="Hag",
        ort="Ha",
    )
    LAUT_HAG_HG = Sammlung(
        trace="Hag Hg",
        groups="Lautschrift|Hag Hg",
        kreis="Hag",
        ort="Hg",
    )
    LAUT_HAG_HS = Sammlung(
        trace="Hag Hs",
        groups="Lautschrift|Hag Hs",
        kreis="Hag",
        ort="Hs",
    )
    LAUT_HAG_VH = Sammlung(
        trace="Hag Vh",
        groups="Lautschrift|Hag Vh",
        kreis="Hag",
        ort="Vh",
    )
    LAUT_HAL_AH = Sammlung(
        trace="Hal Ah",
        groups="Lautschrift|Hal Ah",
        kreis="Hal",
        ort="Ah",
    )
    LAUT_HAL_BC = Sammlung(
        trace="Hal Bc",
        groups="Lautschrift|Hal Bc",
        kreis="Hal",
        ort="Bc",
    )
    LAUT_HAL_BH = Sammlung(
        trace="Hal Bh",
        groups="Lautschrift|Hal Bh",
        kreis="Hal",
        ort="Bh",
    )
    LAUT_HAL_BK = Sammlung(
        trace="Hal Bk",
        groups="Lautschrift|Hal Bk",
        kreis="Hal",
        ort="Bk",
    )
    LAUT_HAL_BO = Sammlung(
        trace="Hal Bo",
        groups="Lautschrift|Hal Bo",
        kreis="Hal",
        ort="Bo",
    )
    LAUT_HAL_BV = Sammlung(
        trace="Hal Bv",
        groups="Lautschrift|Hal Bv",
        kreis="Hal",
        ort="Bv",
    )
    LAUT_HAL_EB = Sammlung(
        trace="Hal Eb",
        groups="Lautschrift|Hal Eb",
        kreis="Hal",
        ort="Eb",
    )
    LAUT_HAL_GA = Sammlung(
        trace="Hal Ga",
        groups="Lautschrift|Hal Ga",
        kreis="Hal",
        ort="Ga",
    )
    LAUT_HAL_HA = Sammlung(
        trace="Hal Ha",
        groups="Lautschrift|Hal Ha",
        kreis="Hal",
        ort="Ha",
    )
    LAUT_HAL_HE = Sammlung(
        trace="Hal He",
        groups="Lautschrift|Hal He",
        kreis="Hal",
        ort="He",
    )
    LAUT_HAL_HG = Sammlung(
        trace="Hal Hg",
        groups="Lautschrift|Hal Hg",
        kreis="Hal",
        ort="Hg",
    )
    LAUT_HAL_HÖ = Sammlung(
        trace="Hal Hö",
        groups="Lautschrift|Hal Hö",
        kreis="Hal",
        ort="Hö",
    )
    LAUT_HAL_HT = Sammlung(
        trace="Hal Ht",
        groups="Lautschrift|Hal Ht",
        kreis="Hal",
        ort="Ht",
    )
    LAUT_HAL_IS = Sammlung(
        trace="Hal Is",
        groups="Lautschrift|Hal Is",
        kreis="Hal",
        ort="Is",
    )
    LAUT_HAL_KA = Sammlung(
        trace="Hal Ka",
        groups="Lautschrift|Hal Ka",
        kreis="Hal",
        ort="Ka",
    )
    LAUT_HAL_KK = Sammlung(
        trace="Hal Kk",
        groups="Lautschrift|Hal Kk",
        kreis="Hal",
        ort="Kk",
    )
    LAUT_HAL_KL = Sammlung(
        trace="Hal Kl",
        groups="Lautschrift|Hal Kl",
        kreis="Hal",
        ort="Kl",
    )
    LAUT_HAL_KO = Sammlung(
        trace="Hal Ko",
        groups="Lautschrift|Hal Ko",
        kreis="Hal",
        ort="Ko",
    )
    LAUT_HAL_KÜ = Sammlung(
        trace="Hal Kü",
        groups="Lautschrift|Hal Kü",
        kreis="Hal",
        ort="Kü",
    )
    LAUT_HAL_LH = Sammlung(
        trace="Hal Lh",
        groups="Lautschrift|Hal Lh",
        kreis="Hal",
        ort="Lh",
    )
    LAUT_HAL_LO = Sammlung(
        trace="Hal Lo",
        groups="Lautschrift|Hal Lo",
        kreis="Hal",
        ort="Lo",
    )
    LAUT_HAL_OD = Sammlung(
        trace="Hal Od",
        groups="Lautschrift|Hal Od",
        kreis="Hal",
        ort="Od",
    )
    LAUT_HAL_ÖW = Sammlung(
        trace="Hal Öw",
        groups="Lautschrift|Hal Öw",
        kreis="Hal",
        ort="Öw",
    )
    LAUT_HAL_PH = Sammlung(
        trace="Hal Ph",
        groups="Lautschrift|Hal Ph",
        kreis="Hal",
        ort="Ph",
    )
    LAUT_HAL_PL = Sammlung(
        trace="Hal Pl",
        groups="Lautschrift|Hal Pl",
        kreis="Hal",
        ort="Pl",
    )
    LAUT_HAL_RA = Sammlung(
        trace="Hal Ra",
        groups="Lautschrift|Hal Ra",
        kreis="Hal",
        ort="Ra",
    )
    LAUT_HAL_SF = Sammlung(
        trace="Hal Sf",
        groups="Lautschrift|Hal Sf",
        kreis="Hal",
        ort="Sf",
    )
    LAUT_HAL_SH = Sammlung(
        trace="Hal Sh",
        groups="Lautschrift|Hal Sh",
        kreis="Hal",
        ort="Sh",
    )
    LAUT_HAL_SI = Sammlung(
        trace="Hal Si",
        groups="Lautschrift|Hal Si",
        kreis="Hal",
        ort="Si",
    )
    LAUT_HAL_SR = Sammlung(
        trace="Hal Sr",
        groups="Lautschrift|Hal Sr",
        kreis="Hal",
        ort="Sr",
    )
    LAUT_HAL_ST = Sammlung(
        trace="Hal St",
        groups="Lautschrift|Hal St",
        kreis="Hal",
        ort="St",
    )
    LAUT_HAL_TH = Sammlung(
        trace="Hal Th",
        groups="Lautschrift|Hal Th",
        kreis="Hal",
        ort="Th",
    )
    LAUT_HAL_VM = Sammlung(
        trace="Hal Vm",
        groups="Lautschrift|Hal Vm",
        kreis="Hal",
        ort="Vm",
    )
    LAUT_HAL_WE = Sammlung(
        trace="Hal We",
        groups="Lautschrift|Hal We",
        kreis="Hal",
        ort="We",
    )
    LAUT_HFD_AL = Sammlung(
        trace="Hfd Al",
        groups="Lautschrift|Hfd Al",
        kreis="Hfd",
        ort="Al",
    )
    LAUT_HFD_BB = Sammlung(
        trace="Hfd Bb",
        groups="Lautschrift|Hfd Bb",
        kreis="Hfd",
        ort="Bb",
    )
    LAUT_HFD_BI = Sammlung(
        trace="Hfd Bi",
        groups="Lautschrift|Hfd Bi",
        kreis="Hfd",
        ort="Bi",
    )
    LAUT_HFD_BK = Sammlung(
        trace="Hfd Bk",
        groups="Lautschrift|Hfd Bk",
        kreis="Hfd",
        ort="Bk",
    )
    LAUT_HFD_BO = Sammlung(
        trace="Hfd Bo",
        groups="Lautschrift|Hfd Bo",
        kreis="Hfd",
        ort="Bo",
    )
    LAUT_HFD_BR = Sammlung(
        trace="Hfd Br",
        groups="Lautschrift|Hfd Br",
        kreis="Hfd",
        ort="Br",
    )
    LAUT_HFD_BU = Sammlung(
        trace="Hfd Bu",
        groups="Lautschrift|Hfd Bu",
        kreis="Hfd",
        ort="Bu",
    )
    LAUT_HFD_BÜ = Sammlung(
        trace="Hfd Bü",
        groups="Lautschrift|Hfd Bü",
        kreis="Hfd",
        ort="Bü",
    )
    LAUT_HFD_DB = Sammlung(
        trace="Hfd Db",
        groups="Lautschrift|Hfd Db",
        kreis="Hfd",
        ort="Db",
    )
    LAUT_HFD_DD = Sammlung(
        trace="Hfd Dd",
        groups="Lautschrift|Hfd Dd",
        kreis="Hfd",
        ort="Dd",
    )
    LAUT_HFD_DH = Sammlung(
        trace="Hfd Dh",
        groups="Lautschrift|Hfd Dh",
        kreis="Hfd",
        ort="Dh",
    )
    LAUT_HFD_DO = Sammlung(
        trace="Hfd Do",
        groups="Lautschrift|Hfd Do",
        kreis="Hfd",
        ort="Do",
    )
    LAUT_HFD_DR = Sammlung(
        trace="Hfd Dr",
        groups="Lautschrift|Hfd Dr",
        kreis="Hfd",
        ort="Dr",
    )
    LAUT_HFD_DÜ = Sammlung(
        trace="Hfd Dü",
        groups="Lautschrift|Hfd Dü",
        kreis="Hfd",
        ort="Dü",
    )
    LAUT_HFD_EB = Sammlung(
        trace="Hfd Eb",
        groups="Lautschrift|Hfd Eb",
        kreis="Hfd",
        ort="Eb",
    )
    LAUT_HFD_ED = Sammlung(
        trace="Hfd Ed",
        groups="Lautschrift|Hfd Ed",
        kreis="Hfd",
        ort="Ed",
    )
    LAUT_HFD_EH = Sammlung(
        trace="Hfd Eh",
        groups="Lautschrift|Hfd Eh",
        kreis="Hfd",
        ort="Eh",
    )
    LAUT_HFD_EI = Sammlung(
        trace="Hfd Ei",
        groups="Lautschrift|Hfd Ei",
        kreis="Hfd",
        ort="Ei",
    )
    LAUT_HFD_EL = Sammlung(
        trace="Hfd El",
        groups="Lautschrift|Hfd El",
        kreis="Hfd",
        ort="El",
    )
    LAUT_HFD_EN = Sammlung(
        trace="Hfd En",
        groups="Lautschrift|Hfd En",
        kreis="Hfd",
        ort="En",
    )
    LAUT_HFD_EX = Sammlung(
        trace="Hfd Ex",
        groups="Lautschrift|Hfd Ex",
        kreis="Hfd",
        ort="Ex",
    )
    LAUT_HFD_FA = Sammlung(
        trace="Hfd Fa",
        groups="Lautschrift|Hfd Fa",
        kreis="Hfd",
        ort="Fa",
    )
    LAUT_HFD_FD = Sammlung(
        trace="Hfd Fd",
        groups="Lautschrift|Hfd Fd",
        kreis="Hfd",
        ort="Fd",
    )
    LAUT_HFD_GO = Sammlung(
        trace="Hfd Go",
        groups="Lautschrift|Hfd Go",
        kreis="Hfd",
        ort="Go",
    )
    LAUT_HFD_HA = Sammlung(
        trace="Hfd Ha",
        groups="Lautschrift|Hfd Ha",
        kreis="Hfd",
        ort="Ha",
    )
    LAUT_HFD_HÄ = Sammlung(
        trace="Hfd Hä",
        groups="Lautschrift|Hfd Hä",
        kreis="Hfd",
        ort="Hä",
    )
    LAUT_HFD_HB = Sammlung(
        trace="Hfd Hb",
        groups="Lautschrift|Hfd Hb",
        kreis="Hfd",
        ort="Hb",
    )
    LAUT_HFD_HF = Sammlung(
        trace="Hfd Hf",
        groups="Lautschrift|Hfd Hf",
        kreis="Hfd",
        ort="Hf",
    )
    LAUT_HFD_HH = Sammlung(
        trace="Hfd Hh",
        groups="Lautschrift|Hfd Hh",
        kreis="Hfd",
        ort="Hh",
    )
    LAUT_HFD_HI = Sammlung(
        trace="Hfd Hi",
        groups="Lautschrift|Hfd Hi",
        kreis="Hfd",
        ort="Hi",
    )
    LAUT_HFD_HO = Sammlung(
        trace="Hfd Ho",
        groups="Lautschrift|Hfd Ho",
        kreis="Hfd",
        ort="Ho",
    )
    LAUT_HFD_HS = Sammlung(
        trace="Hfd Hs",
        groups="Lautschrift|Hfd Hs",
        kreis="Hfd",
        ort="Hs",
    )
    LAUT_HFD_HU = Sammlung(
        trace="Hfd Hu",
        groups="Lautschrift|Hfd Hu",
        kreis="Hfd",
        ort="Hu",
    )
    LAUT_HFD_HÜ = Sammlung(
        trace="Hfd Hü",
        groups="Lautschrift|Hfd Hü",
        kreis="Hfd",
        ort="Hü",
    )
    LAUT_HFD_HW = Sammlung(
        trace="Hfd Hw",
        groups="Lautschrift|Hfd Hw",
        kreis="Hfd",
        ort="Hw",
    )
    LAUT_HFD_KL = Sammlung(
        trace="Hfd Kl",
        groups="Lautschrift|Hfd Kl",
        kreis="Hfd",
        ort="Kl",
    )
    LAUT_HFD_LA = Sammlung(
        trace="Hfd La",
        groups="Lautschrift|Hfd La",
        kreis="Hfd",
        ort="La",
    )
    LAUT_HFD_LH = Sammlung(
        trace="Hfd Lh",
        groups="Lautschrift|Hfd Lh",
        kreis="Hfd",
        ort="Lh",
    )
    LAUT_HFD_LÖ = Sammlung(
        trace="Hfd Lö",
        groups="Lautschrift|Hfd Lö",
        kreis="Hfd",
        ort="Lö",
    )
    LAUT_HFD_LZ = Sammlung(
        trace="Hfd Lz",
        groups="Lautschrift|Hfd Lz",
        kreis="Hfd",
        ort="Lz",
    )
    LAUT_HFD_MA = Sammlung(
        trace="Hfd Ma",
        groups="Lautschrift|Hfd Ma",
        kreis="Hfd",
        ort="Ma",
    )
    LAUT_HFD_MB = Sammlung(
        trace="Hfd Mb",
        groups="Lautschrift|Hfd Mb",
        kreis="Hfd",
        ort="Mb",
    )
    LAUT_HFD_MC = Sammlung(
        trace="Hfd Mc",
        groups="Lautschrift|Hfd Mc",
        kreis="Hfd",
        ort="Mc",
    )
    LAUT_HFD_MH = Sammlung(
        trace="Hfd Mh",
        groups="Lautschrift|Hfd Mh",
        kreis="Hfd",
        ort="Mh",
    )
    LAUT_HFD_MT = Sammlung(
        trace="Hfd Mt",
        groups="Lautschrift|Hfd Mt",
        kreis="Hfd",
        ort="Mt",
    )
    LAUT_HFD_NS = Sammlung(
        trace="Hfd Ns",
        groups="Lautschrift|Hfd Ns",
        kreis="Hfd",
        ort="Ns",
    )
    LAUT_HFD_OB = Sammlung(
        trace="Hfd Ob",
        groups="Lautschrift|Hfd Ob",
        kreis="Hfd",
        ort="Ob",
    )
    LAUT_HFD_OH = Sammlung(
        trace="Hfd Oh",
        groups="Lautschrift|Hfd Oh",
        kreis="Hfd",
        ort="Oh",
    )
    LAUT_HFD_ÖH = Sammlung(
        trace="Hfd Öh",
        groups="Lautschrift|Hfd Öh",
        kreis="Hfd",
        ort="Öh",
    )
    LAUT_HFD_OK = Sammlung(
        trace="Hfd Ok",
        groups="Lautschrift|Hfd Ok",
        kreis="Hfd",
        ort="Ok",
    )
    LAUT_HFD_OS = Sammlung(
        trace="Hfd Os",
        groups="Lautschrift|Hfd Os",
        kreis="Hfd",
        ort="Os",
    )
    LAUT_HFD_PH = Sammlung(
        trace="Hfd Ph",
        groups="Lautschrift|Hfd Ph",
        kreis="Hfd",
        ort="Ph",
    )
    LAUT_HFD_QH = Sammlung(
        trace="Hfd Qh",
        groups="Lautschrift|Hfd Qh",
        kreis="Hfd",
        ort="Qh",
    )
    LAUT_HFD_RH = Sammlung(
        trace="Hfd Rh",
        groups="Lautschrift|Hfd Rh",
        kreis="Hfd",
        ort="Rh",
    )
    LAUT_HFD_RL = Sammlung(
        trace="Hfd Rl",
        groups="Lautschrift|Hfd Rl",
        kreis="Hfd",
        ort="Rl",
    )
    LAUT_HFD_SB = Sammlung(
        trace="Hfd Sb",
        groups="Lautschrift|Hfd Sb",
        kreis="Hfd",
        ort="Sb",
    )
    LAUT_HFD_SC = Sammlung(
        trace="Hfd Sc",
        groups="Lautschrift|Hfd Sc",
        kreis="Hfd",
        ort="Sc",
    )
    LAUT_HFD_SD = Sammlung(
        trace="Hfd Sd",
        groups="Lautschrift|Hfd Sd",
        kreis="Hfd",
        ort="Sd",
    )
    LAUT_HFD_SG = Sammlung(
        trace="Hfd Sg",
        groups="Lautschrift|Hfd Sg",
        kreis="Hfd",
        ort="Sg",
    )
    LAUT_HFD_SI = Sammlung(
        trace="Hfd Si",
        groups="Lautschrift|Hfd Si",
        kreis="Hfd",
        ort="Si",
    )
    LAUT_HFD_SL = Sammlung(
        trace="Hfd Sl",
        groups="Lautschrift|Hfd Sl",
        kreis="Hfd",
        ort="Sl",
    )
    LAUT_HFD_SP = Sammlung(
        trace="Hfd Sp",
        groups="Lautschrift|Hfd Sp",
        kreis="Hfd",
        ort="Sp",
    )
    LAUT_HFD_ST = Sammlung(
        trace="Hfd St",
        groups="Lautschrift|Hfd St",
        kreis="Hfd",
        ort="St",
    )
    LAUT_HFD_SU = Sammlung(
        trace="Hfd Su",
        groups="Lautschrift|Hfd Su",
        kreis="Hfd",
        ort="Su",
    )
    LAUT_HFD_SW = Sammlung(
        trace="Hfd Sw",
        groups="Lautschrift|Hfd Sw",
        kreis="Hfd",
        ort="Sw",
    )
    LAUT_HFD_VD = Sammlung(
        trace="Hfd Vd",
        groups="Lautschrift|Hfd Vd",
        kreis="Hfd",
        ort="Vd",
    )
    LAUT_HFD_VL = Sammlung(
        trace="Hfd Vl",
        groups="Lautschrift|Hfd Vl",
        kreis="Hfd",
        ort="Vl",
    )
    LAUT_HFD_WA = Sammlung(
        trace="Hfd Wa",
        groups="Lautschrift|Hfd Wa",
        kreis="Hfd",
        ort="Wa",
    )
    LAUT_HFD_WD = Sammlung(
        trace="Hfd Wd",
        groups="Lautschrift|Hfd Wd",
        kreis="Hfd",
        ort="Wd",
    )
    LAUT_HFD_WE = Sammlung(
        trace="Hfd We",
        groups="Lautschrift|Hfd We",
        kreis="Hfd",
        ort="We",
    )
    LAUT_HFD_WF = Sammlung(
        trace="Hfd Wf",
        groups="Lautschrift|Hfd Wf",
        kreis="Hfd",
        ort="Wf",
    )
    LAUT_HFD_WK = Sammlung(
        trace="Hfd Wk",
        groups="Lautschrift|Hfd Wk",
        kreis="Hfd",
        ort="Wk",
    )
    LAUT_HÖX_AB = Sammlung(
        trace="Höx Ab",
        groups="Lautschrift|Höx Ab",
        kreis="Höx",
        ort="Ab",
    )
    LAUT_HÖX_AH = Sammlung(
        trace="Höx Ah",
        groups="Lautschrift|Höx Ah",
        kreis="Höx",
        ort="Ah",
    )
    LAUT_HÖX_AL = Sammlung(
        trace="Höx Al",
        groups="Lautschrift|Höx Al",
        kreis="Höx",
        ort="Al",
    )
    LAUT_HÖX_AM = Sammlung(
        trace="Höx Am",
        groups="Lautschrift|Höx Am",
        kreis="Höx",
        ort="Am",
    )
    LAUT_HÖX_BB = Sammlung(
        trace="Höx Bb",
        groups="Lautschrift|Höx Bb",
        kreis="Höx",
        ort="Bb",
    )
    LAUT_HÖX_BE = Sammlung(
        trace="Höx Be",
        groups="Lautschrift|Höx Be",
        kreis="Höx",
        ort="Be",
    )
    LAUT_HÖX_BG = Sammlung(
        trace="Höx Bg",
        groups="Lautschrift|Höx Bg",
        kreis="Höx",
        ort="Bg",
    )
    LAUT_HÖX_BH = Sammlung(
        trace="Höx Bh",
        groups="Lautschrift|Höx Bh",
        kreis="Höx",
        ort="Bh",
    )
    LAUT_HÖX_BL = Sammlung(
        trace="Höx Bl",
        groups="Lautschrift|Höx Bl",
        kreis="Höx",
        ort="Bl",
    )
    LAUT_HÖX_BO = Sammlung(
        trace="Höx Bo",
        groups="Lautschrift|Höx Bo",
        kreis="Höx",
        ort="Bo",
    )
    LAUT_HÖX_BÖ = Sammlung(
        trace="Höx Bö",
        groups="Lautschrift|Höx Bö",
        kreis="Höx",
        ort="Bö",
    )
    LAUT_HÖX_BR = Sammlung(
        trace="Höx Br",
        groups="Lautschrift|Höx Br",
        kreis="Höx",
        ort="Br",
    )
    LAUT_HÖX_BS = Sammlung(
        trace="Höx Bs",
        groups="Lautschrift|Höx Bs",
        kreis="Höx",
        ort="Bs",
    )
    LAUT_HÖX_BV = Sammlung(
        trace="Höx Bv",
        groups="Lautschrift|Höx Bv",
        kreis="Höx",
        ort="Bv",
    )
    LAUT_HÖX_BX = Sammlung(
        trace="Höx Bx",
        groups="Lautschrift|Höx Bx",
        kreis="Höx",
        ort="Bx",
    )
    LAUT_HÖX_DB = Sammlung(
        trace="Höx Db",
        groups="Lautschrift|Höx Db",
        kreis="Höx",
        ort="Db",
    )
    LAUT_HÖX_DH = Sammlung(
        trace="Höx Dh",
        groups="Lautschrift|Höx Dh",
        kreis="Höx",
        ort="Dh",
    )
    LAUT_HÖX_DR = Sammlung(
        trace="Höx Dr",
        groups="Lautschrift|Höx Dr",
        kreis="Höx",
        ort="Dr",
    )
    LAUT_HÖX_EN = Sammlung(
        trace="Höx En",
        groups="Lautschrift|Höx En",
        kreis="Höx",
        ort="En",
    )
    LAUT_HÖX_ER = Sammlung(
        trace="Höx Er",
        groups="Lautschrift|Höx Er",
        kreis="Höx",
        ort="Er",
    )
    LAUT_HÖX_FR = Sammlung(
        trace="Höx Fr",
        groups="Lautschrift|Höx Fr",
        kreis="Höx",
        ort="Fr",
    )
    LAUT_HÖX_FÜ = Sammlung(
        trace="Höx Fü",
        groups="Lautschrift|Höx Fü",
        kreis="Höx",
        ort="Fü",
    )
    LAUT_HÖX_GH = Sammlung(
        trace="Höx Gh",
        groups="Lautschrift|Höx Gh",
        kreis="Höx",
        ort="Gh",
    )
    LAUT_HÖX_HA = Sammlung(
        trace="Höx Ha",
        groups="Lautschrift|Höx Ha",
        kreis="Höx",
        ort="Ha",
    )
    LAUT_HÖX_HB = Sammlung(
        trace="Höx Hb",
        groups="Lautschrift|Höx Hb",
        kreis="Höx",
        ort="Hb",
    )
    LAUT_HÖX_HD = Sammlung(
        trace="Höx Hd",
        groups="Lautschrift|Höx Hd",
        kreis="Höx",
        ort="Hd",
    )
    LAUT_HÖX_HE = Sammlung(
        trace="Höx He",
        groups="Lautschrift|Höx He",
        kreis="Höx",
        ort="He",
    )
    LAUT_HÖX_HH = Sammlung(
        trace="Höx Hh",
        groups="Lautschrift|Höx Hh",
        kreis="Höx",
        ort="Hh",
    )
    LAUT_HÖX_HI = Sammlung(
        trace="Höx Hi",
        groups="Lautschrift|Höx Hi",
        kreis="Höx",
        ort="Hi",
    )
    LAUT_HÖX_HM = Sammlung(
        trace="Höx Hm",
        groups="Lautschrift|Höx Hm",
        kreis="Höx",
        ort="Hm",
    )
    LAUT_HÖX_HO = Sammlung(
        trace="Höx Ho",
        groups="Lautschrift|Höx Ho",
        kreis="Höx",
        ort="Ho",
    )
    LAUT_HÖX_HR = Sammlung(
        trace="Höx Hr",
        groups="Lautschrift|Höx Hr",
        kreis="Höx",
        ort="Hr",
    )
    LAUT_HÖX_HS = Sammlung(
        trace="Höx Hs",
        groups="Lautschrift|Höx Hs",
        kreis="Höx",
        ort="Hs",
    )
    LAUT_HÖX_HX = Sammlung(
        trace="Höx Hx",
        groups="Lautschrift|Höx Hx",
        kreis="Höx",
        ort="Hx",
    )
    LAUT_HÖX_IS = Sammlung(
        trace="Höx Is",
        groups="Lautschrift|Höx Is",
        kreis="Höx",
        ort="Is",
    )
    LAUT_HÖX_KB = Sammlung(
        trace="Höx Kb",
        groups="Lautschrift|Höx Kb",
        kreis="Höx",
        ort="Kb",
    )
    LAUT_HÖX_KO = Sammlung(
        trace="Höx Ko",
        groups="Lautschrift|Höx Ko",
        kreis="Höx",
        ort="Ko",
    )
    LAUT_HÖX_LD = Sammlung(
        trace="Höx Ld",
        groups="Lautschrift|Höx Ld",
        kreis="Höx",
        ort="Ld",
    )
    LAUT_HÖX_LM = Sammlung(
        trace="Höx Lm",
        groups="Lautschrift|Höx Lm",
        kreis="Höx",
        ort="Lm",
    )
    LAUT_HÖX_LÖ = Sammlung(
        trace="Höx Lö",
        groups="Lautschrift|Höx Lö",
        kreis="Höx",
        ort="Lö",
    )
    LAUT_HÖX_LÜ = Sammlung(
        trace="Höx Lü",
        groups="Lautschrift|Höx Lü",
        kreis="Höx",
        ort="Lü",
    )
    LAUT_HÖX_MB = Sammlung(
        trace="Höx Mb",
        groups="Lautschrift|Höx Mb",
        kreis="Höx",
        ort="Mb",
    )
    LAUT_HÖX_MH = Sammlung(
        trace="Höx Mh",
        groups="Lautschrift|Höx Mh",
        kreis="Höx",
        ort="Mh",
    )
    LAUT_HÖX_OB = Sammlung(
        trace="Höx Ob",
        groups="Lautschrift|Höx Ob",
        kreis="Höx",
        ort="Ob",
    )
    LAUT_HÖX_OE = Sammlung(
        trace="Höx Oe",
        groups="Lautschrift|Höx Oe",
        kreis="Höx",
        ort="Oe",
    )
    LAUT_HÖX_OH = Sammlung(
        trace="Höx Oh",
        groups="Lautschrift|Höx Oh",
        kreis="Höx",
        ort="Oh",
    )
    LAUT_HÖX_OT = Sammlung(
        trace="Höx Ot",
        groups="Lautschrift|Höx Ot",
        kreis="Höx",
        ort="Ot",
    )
    LAUT_HÖX_PÖ = Sammlung(
        trace="Höx Pö",
        groups="Lautschrift|Höx Pö",
        kreis="Höx",
        ort="Pö",
    )
    LAUT_HÖX_RE = Sammlung(
        trace="Höx Re",
        groups="Lautschrift|Höx Re",
        kreis="Höx",
        ort="Re",
    )
    LAUT_HÖX_RH = Sammlung(
        trace="Höx Rh",
        groups="Lautschrift|Höx Rh",
        kreis="Höx",
        ort="Rh",
    )
    LAUT_HÖX_RI = Sammlung(
        trace="Höx Ri",
        groups="Lautschrift|Höx Ri",
        kreis="Höx",
        ort="Ri",
    )
    LAUT_HÖX_RO = Sammlung(
        trace="Höx Ro",
        groups="Lautschrift|Höx Ro",
        kreis="Höx",
        ort="Ro",
    )
    LAUT_HÖX_SB = Sammlung(
        trace="Höx Sb",
        groups="Lautschrift|Höx Sb",
        kreis="Höx",
        ort="Sb",
    )
    LAUT_HÖX_SH = Sammlung(
        trace="Höx Sh",
        groups="Lautschrift|Höx Sh",
        kreis="Höx",
        ort="Sh",
    )
    LAUT_HÖX_SM = Sammlung(
        trace="Höx Sm",
        groups="Lautschrift|Höx Sm",
        kreis="Höx",
        ort="Sm",
    )
    LAUT_HÖX_SS = Sammlung(
        trace="Höx Ss",
        groups="Lautschrift|Höx Ss",
        kreis="Höx",
        ort="Ss",
    )
    LAUT_HÖX_TI = Sammlung(
        trace="Höx Ti",
        groups="Lautschrift|Höx Ti",
        kreis="Höx",
        ort="Ti",
    )
    LAUT_HÖX_VB = Sammlung(
        trace="Höx Vb",
        groups="Lautschrift|Höx Vb",
        kreis="Höx",
        ort="Vb",
    )
    LAUT_HÖX_VÖ = Sammlung(
        trace="Höx Vö",
        groups="Lautschrift|Höx Vö",
        kreis="Höx",
        ort="Vö",
    )
    LAUT_HÖX_WE = Sammlung(
        trace="Höx We",
        groups="Lautschrift|Höx We",
        kreis="Höx",
        ort="We",
    )
    LAUT_HÖX_WÜ = Sammlung(
        trace="Höx Wü",
        groups="Lautschrift|Höx Wü",
        kreis="Höx",
        ort="Wü",
    )
    LAUT_ISL_AP = Sammlung(
        trace="Isl Ap",
        groups="Lautschrift|Isl Ap",
        kreis="Isl",
        ort="Ap",
    )
    LAUT_ISL_BB = Sammlung(
        trace="Isl Bb",
        groups="Lautschrift|Isl Bb",
        kreis="Isl",
        ort="Bb",
    )
    LAUT_ISL_BC = Sammlung(
        trace="Isl Bc",
        groups="Lautschrift|Isl Bc",
        kreis="Isl",
        ort="Bc",
    )
    LAUT_ISL_BD = Sammlung(
        trace="Isl Bd",
        groups="Lautschrift|Isl Bd",
        kreis="Isl",
        ort="Bd",
    )
    LAUT_ISL_BE = Sammlung(
        trace="Isl Be",
        groups="Lautschrift|Isl Be",
        kreis="Isl",
        ort="Be",
    )
    LAUT_ISL_BG = Sammlung(
        trace="Isl Bg",
        groups="Lautschrift|Isl Bg",
        kreis="Isl",
        ort="Bg",
    )
    LAUT_ISL_BH = Sammlung(
        trace="Isl Bh",
        groups="Lautschrift|Isl Bh",
        kreis="Isl",
        ort="Bh",
    )
    LAUT_ISL_BK = Sammlung(
        trace="Isl Bk",
        groups="Lautschrift|Isl Bk",
        kreis="Isl",
        ort="Bk",
    )
    LAUT_ISL_BÖ = Sammlung(
        trace="Isl Bö",
        groups="Lautschrift|Isl Bö",
        kreis="Isl",
        ort="Bö",
    )
    LAUT_ISL_BP = Sammlung(
        trace="Isl Bp",
        groups="Lautschrift|Isl Bp",
        kreis="Isl",
        ort="Bp",
    )
    LAUT_ISL_BR = Sammlung(
        trace="Isl Br",
        groups="Lautschrift|Isl Br",
        kreis="Isl",
        ort="Br",
    )
    LAUT_ISL_BÜ = Sammlung(
        trace="Isl Bü",
        groups="Lautschrift|Isl Bü",
        kreis="Isl",
        ort="Bü",
    )
    LAUT_ISL_BX = Sammlung(
        trace="Isl Bx",
        groups="Lautschrift|Isl Bx",
        kreis="Isl",
        ort="Bx",
    )
    LAUT_ISL_DA = Sammlung(
        trace="Isl Da",
        groups="Lautschrift|Isl Da",
        kreis="Isl",
        ort="Da",
    )
    LAUT_ISL_DG = Sammlung(
        trace="Isl Dg",
        groups="Lautschrift|Isl Dg",
        kreis="Isl",
        ort="Dg",
    )
    LAUT_ISL_DH = Sammlung(
        trace="Isl Dh",
        groups="Lautschrift|Isl Dh",
        kreis="Isl",
        ort="Dh",
    )
    LAUT_ISL_DÖ = Sammlung(
        trace="Isl Dö",
        groups="Lautschrift|Isl Dö",
        kreis="Isl",
        ort="Dö",
    )
    LAUT_ISL_DP = Sammlung(
        trace="Isl Dp",
        groups="Lautschrift|Isl Dp",
        kreis="Isl",
        ort="Dp",
    )
    LAUT_ISL_DS = Sammlung(
        trace="Isl Ds",
        groups="Lautschrift|Isl Ds",
        kreis="Isl",
        ort="Ds",
    )
    LAUT_ISL_DÜ = Sammlung(
        trace="Isl Dü",
        groups="Lautschrift|Isl Dü",
        kreis="Isl",
        ort="Dü",
    )
    LAUT_ISL_EF = Sammlung(
        trace="Isl Ef",
        groups="Lautschrift|Isl Ef",
        kreis="Isl",
        ort="Ef",
    )
    LAUT_ISL_EL = Sammlung(
        trace="Isl El",
        groups="Lautschrift|Isl El",
        kreis="Isl",
        ort="El",
    )
    LAUT_ISL_ER = Sammlung(
        trace="Isl Er",
        groups="Lautschrift|Isl Er",
        kreis="Isl",
        ort="Er",
    )
    LAUT_ISL_EV = Sammlung(
        trace="Isl Ev",
        groups="Lautschrift|Isl Ev",
        kreis="Isl",
        ort="Ev",
    )
    LAUT_ISL_FB = Sammlung(
        trace="Isl Fb",
        groups="Lautschrift|Isl Fb",
        kreis="Isl",
        ort="Fb",
    )
    LAUT_ISL_GB = Sammlung(
        trace="Isl Gb",
        groups="Lautschrift|Isl Gb",
        kreis="Isl",
        ort="Gb",
    )
    LAUT_ISL_GE = Sammlung(
        trace="Isl Ge",
        groups="Lautschrift|Isl Ge",
        kreis="Isl",
        ort="Ge",
    )
    LAUT_ISL_GF = Sammlung(
        trace="Isl Gf",
        groups="Lautschrift|Isl Gf",
        kreis="Isl",
        ort="Gf",
    )
    LAUT_ISL_GH = Sammlung(
        trace="Isl Gh",
        groups="Lautschrift|Isl Gh",
        kreis="Isl",
        ort="Gh",
    )
    LAUT_ISL_GL = Sammlung(
        trace="Isl Gl",
        groups="Lautschrift|Isl Gl",
        kreis="Isl",
        ort="Gl",
    )
    LAUT_ISL_GM = Sammlung(
        trace="Isl Gm",
        groups="Lautschrift|Isl Gm",
        kreis="Isl",
        ort="Gm",
    )
    LAUT_ISL_GR = Sammlung(
        trace="Isl Gr",
        groups="Lautschrift|Isl Gr",
        kreis="Isl",
        ort="Gr",
    )
    LAUT_ISL_GS = Sammlung(
        trace="Isl Gs",
        groups="Lautschrift|Isl Gs",
        kreis="Isl",
        ort="Gs",
    )
    LAUT_ISL_GX = Sammlung(
        trace="Isl Gx",
        groups="Lautschrift|Isl Gx",
        kreis="Isl",
        ort="Gx",
    )
    LAUT_ISL_HA = Sammlung(
        trace="Isl Ha",
        groups="Lautschrift|Isl Ha",
        kreis="Isl",
        ort="Ha",
    )
    LAUT_ISL_HD = Sammlung(
        trace="Isl Hd",
        groups="Lautschrift|Isl Hd",
        kreis="Isl",
        ort="Hd",
    )
    LAUT_ISL_HE = Sammlung(
        trace="Isl He",
        groups="Lautschrift|Isl He",
        kreis="Isl",
        ort="He",
    )
    LAUT_ISL_HG = Sammlung(
        trace="Isl Hg",
        groups="Lautschrift|Isl Hg",
        kreis="Isl",
        ort="Hg",
    )
    LAUT_ISL_HN = Sammlung(
        trace="Isl Hn",
        groups="Lautschrift|Isl Hn",
        kreis="Isl",
        ort="Hn",
    )
    LAUT_ISL_HO = Sammlung(
        trace="Isl Ho",
        groups="Lautschrift|Isl Ho",
        kreis="Isl",
        ort="Ho",
    )
    LAUT_ISL_HP = Sammlung(
        trace="Isl Hp",
        groups="Lautschrift|Isl Hp",
        kreis="Isl",
        ort="Hp",
    )
    LAUT_ISL_HÜ = Sammlung(
        trace="Isl Hü",
        groups="Lautschrift|Isl Hü",
        kreis="Isl",
        ort="Hü",
    )
    LAUT_ISL_HV = Sammlung(
        trace="Isl Hv",
        groups="Lautschrift|Isl Hv",
        kreis="Isl",
        ort="Hv",
    )
    LAUT_ISL_IM = Sammlung(
        trace="Isl Im",
        groups="Lautschrift|Isl Im",
        kreis="Isl",
        ort="Im",
    )
    LAUT_ISL_IS = Sammlung(
        trace="Isl Is",
        groups="Lautschrift|Isl Is",
        kreis="Isl",
        ort="Is",
    )
    LAUT_ISL_KA = Sammlung(
        trace="Isl Ka",
        groups="Lautschrift|Isl Ka",
        kreis="Isl",
        ort="Ka",
    )
    LAUT_ISL_KB = Sammlung(
        trace="Isl Kb",
        groups="Lautschrift|Isl Kb",
        kreis="Isl",
        ort="Kb",
    )
    LAUT_ISL_KG = Sammlung(
        trace="Isl Kg",
        groups="Lautschrift|Isl Kg",
        kreis="Isl",
        ort="Kg",
    )
    LAUT_ISL_KH = Sammlung(
        trace="Isl Kh",
        groups="Lautschrift|Isl Kh",
        kreis="Isl",
        ort="Kh",
    )
    LAUT_ISL_KO = Sammlung(
        trace="Isl Ko",
        groups="Lautschrift|Isl Ko",
        kreis="Isl",
        ort="Ko",
    )
    LAUT_ISL_KR = Sammlung(
        trace="Isl Kr",
        groups="Lautschrift|Isl Kr",
        kreis="Isl",
        ort="Kr",
    )
    LAUT_ISL_LÄ = Sammlung(
        trace="Isl Lä",
        groups="Lautschrift|Isl Lä",
        kreis="Isl",
        ort="Lä",
    )
    LAUT_ISL_LB = Sammlung(
        trace="Isl Lb",
        groups="Lautschrift|Isl Lb",
        kreis="Isl",
        ort="Lb",
    )
    LAUT_ISL_LD = Sammlung(
        trace="Isl Ld",
        groups="Lautschrift|Isl Ld",
        kreis="Isl",
        ort="Ld",
    )
    LAUT_ISL_LE = Sammlung(
        trace="Isl Le",
        groups="Lautschrift|Isl Le",
        kreis="Isl",
        ort="Le",
    )
    LAUT_ISL_LH = Sammlung(
        trace="Isl Lh",
        groups="Lautschrift|Isl Lh",
        kreis="Isl",
        ort="Lh",
    )
    LAUT_ISL_LK = Sammlung(
        trace="Isl Lk",
        groups="Lautschrift|Isl Lk",
        kreis="Isl",
        ort="Lk",
    )
    LAUT_ISL_LÖ = Sammlung(
        trace="Isl Lö",
        groups="Lautschrift|Isl Lö",
        kreis="Isl",
        ort="Lö",
    )
    LAUT_ISL_LU = Sammlung(
        trace="Isl Lu",
        groups="Lautschrift|Isl Lu",
        kreis="Isl",
        ort="Lu",
    )
    LAUT_ISL_LÜ = Sammlung(
        trace="Isl Lü",
        groups="Lautschrift|Isl Lü",
        kreis="Isl",
        ort="Lü",
    )
    LAUT_ISL_ME = Sammlung(
        trace="Isl Me",
        groups="Lautschrift|Isl Me",
        kreis="Isl",
        ort="Me",
    )
    LAUT_ISL_NI = Sammlung(
        trace="Isl Ni",
        groups="Lautschrift|Isl Ni",
        kreis="Isl",
        ort="Ni",
    )
    LAUT_ISL_OG = Sammlung(
        trace="Isl Og",
        groups="Lautschrift|Isl Og",
        kreis="Isl",
        ort="Og",
    )
    LAUT_ISL_OÖ = Sammlung(
        trace="Isl Oö",
        groups="Lautschrift|Isl Oö",
        kreis="Isl",
        ort="Oö",
    )
    LAUT_ISL_ÖS = Sammlung(
        trace="Isl Ös",
        groups="Lautschrift|Isl Ös",
        kreis="Isl",
        ort="Ös",
    )
    LAUT_ISL_ÖZ = Sammlung(
        trace="Isl Öz",
        groups="Lautschrift|Isl Öz",
        kreis="Isl",
        ort="Öz",
    )
    LAUT_ISL_PI = Sammlung(
        trace="Isl Pi",
        groups="Lautschrift|Isl Pi",
        kreis="Isl",
        ort="Pi",
    )
    LAUT_ISL_RE = Sammlung(
        trace="Isl Re",
        groups="Lautschrift|Isl Re",
        kreis="Isl",
        ort="Re",
    )
    LAUT_ISL_RG = Sammlung(
        trace="Isl Rg",
        groups="Lautschrift|Isl Rg",
        kreis="Isl",
        ort="Rg",
    )
    LAUT_ISL_RH = Sammlung(
        trace="Isl Rh",
        groups="Lautschrift|Isl Rh",
        kreis="Isl",
        ort="Rh",
    )
    LAUT_ISL_RO = Sammlung(
        trace="Isl Ro",
        groups="Lautschrift|Isl Ro",
        kreis="Isl",
        ort="Ro",
    )
    LAUT_ISL_RS = Sammlung(
        trace="Isl Rs",
        groups="Lautschrift|Isl Rs",
        kreis="Isl",
        ort="Rs",
    )
    LAUT_ISL_RÜ = Sammlung(
        trace="Isl Rü",
        groups="Lautschrift|Isl Rü",
        kreis="Isl",
        ort="Rü",
    )
    LAUT_ISL_SA = Sammlung(
        trace="Isl Sa",
        groups="Lautschrift|Isl Sa",
        kreis="Isl",
        ort="Sa",
    )
    LAUT_ISL_SB = Sammlung(
        trace="Isl Sb",
        groups="Lautschrift|Isl Sb",
        kreis="Isl",
        ort="Sb",
    )
    LAUT_ISL_SC = Sammlung(
        trace="Isl Sc",
        groups="Lautschrift|Isl Sc",
        kreis="Isl",
        ort="Sc",
    )
    LAUT_ISL_SI = Sammlung(
        trace="Isl Si",
        groups="Lautschrift|Isl Si",
        kreis="Isl",
        ort="Si",
    )
    LAUT_ISL_SK = Sammlung(
        trace="Isl Sk",
        groups="Lautschrift|Isl Sk",
        kreis="Isl",
        ort="Sk",
    )
    LAUT_ISL_SU = Sammlung(
        trace="Isl Su",
        groups="Lautschrift|Isl Su",
        kreis="Isl",
        ort="Su",
    )
    LAUT_ISL_SÜ = Sammlung(
        trace="Isl Sü",
        groups="Lautschrift|Isl Sü",
        kreis="Isl",
        ort="Sü",
    )
    LAUT_ISL_SW = Sammlung(
        trace="Isl Sw",
        groups="Lautschrift|Isl Sw",
        kreis="Isl",
        ort="Sw",
    )
    LAUT_ISL_UG = Sammlung(
        trace="Isl Ug",
        groups="Lautschrift|Isl Ug",
        kreis="Isl",
        ort="Ug",
    )
    LAUT_ISL_VH = Sammlung(
        trace="Isl Vh",
        groups="Lautschrift|Isl Vh",
        kreis="Isl",
        ort="Vh",
    )
    LAUT_ISL_VI = Sammlung(
        trace="Isl Vi",
        groups="Lautschrift|Isl Vi",
        kreis="Isl",
        ort="Vi",
    )
    LAUT_ISL_WD = Sammlung(
        trace="Isl Wd",
        groups="Lautschrift|Isl Wd",
        kreis="Isl",
        ort="Wd",
    )
    LAUT_ISL_WE = Sammlung(
        trace="Isl We",
        groups="Lautschrift|Isl We",
        kreis="Isl",
        ort="We",
    )
    LAUT_ISL_WH = Sammlung(
        trace="Isl Wh",
        groups="Lautschrift|Isl Wh",
        kreis="Isl",
        ort="Wh",
    )
    LAUT_ISL_WI = Sammlung(
        trace="Isl Wi",
        groups="Lautschrift|Isl Wi",
        kreis="Isl",
        ort="Wi",
    )
    LAUT_ISL_WR = Sammlung(
        trace="Isl Wr",
        groups="Lautschrift|Isl Wr",
        kreis="Isl",
        ort="Wr",
    )
    LAUT_ISL_WU = Sammlung(
        trace="Isl Wu",
        groups="Lautschrift|Isl Wu",
        kreis="Isl",
        ort="Wu",
    )
    LAUT_ISL_WX = Sammlung(
        trace="Isl Wx",
        groups="Lautschrift|Isl Wx",
        kreis="Isl",
        ort="Wx",
    )
    LAUT_KLO_AB = Sammlung(
        trace="Klo Ab",
        groups="Lautschrift|Klo Ab",
        kreis="Klo",
        ort="Ab",
    )
    LAUT_KLO_AD = Sammlung(
        trace="Klo Ad",
        groups="Lautschrift|Klo Ad",
        kreis="Klo",
        ort="Ad",
    )
    LAUT_KLO_AG = Sammlung(
        trace="Klo Ag",
        groups="Lautschrift|Klo Ag",
        kreis="Klo",
        ort="Ag",
    )
    LAUT_KLO_AL = Sammlung(
        trace="Klo Al",
        groups="Lautschrift|Klo Al",
        kreis="Klo",
        ort="Al",
    )
    LAUT_KLO_AM = Sammlung(
        trace="Klo Am",
        groups="Lautschrift|Klo Am",
        kreis="Klo",
        ort="Am",
    )
    LAUT_KLO_AP = Sammlung(
        trace="Klo Ap",
        groups="Lautschrift|Klo Ap",
        kreis="Klo",
        ort="Ap",
    )
    LAUT_KLO_AU = Sammlung(
        trace="Klo Au",
        groups="Lautschrift|Klo Au",
        kreis="Klo",
        ort="Au",
    )
    LAUT_KLO_BB = Sammlung(
        trace="Klo Bb",
        groups="Lautschrift|Klo Bb",
        kreis="Klo",
        ort="Bb",
    )
    LAUT_KLO_BE = Sammlung(
        trace="Klo Be",
        groups="Lautschrift|Klo Be",
        kreis="Klo",
        ort="Be",
    )
    LAUT_KLO_BH = Sammlung(
        trace="Klo Bh",
        groups="Lautschrift|Klo Bh",
        kreis="Klo",
        ort="Bh",
    )
    LAUT_KLO_BL = Sammlung(
        trace="Klo Bl",
        groups="Lautschrift|Klo Bl",
        kreis="Klo",
        ort="Bl",
    )
    LAUT_KLO_BO = Sammlung(
        trace="Klo Bo",
        groups="Lautschrift|Klo Bo",
        kreis="Klo",
        ort="Bo",
    )
    LAUT_KLO_BS = Sammlung(
        trace="Klo Bs",
        groups="Lautschrift|Klo Bs",
        kreis="Klo",
        ort="Bs",
    )
    LAUT_KLO_BU = Sammlung(
        trace="Klo Bu",
        groups="Lautschrift|Klo Bu",
        kreis="Klo",
        ort="Bu",
    )
    LAUT_KLO_BÜ = Sammlung(
        trace="Klo Bü",
        groups="Lautschrift|Klo Bü",
        kreis="Klo",
        ort="Bü",
    )
    LAUT_KLO_BV = Sammlung(
        trace="Klo Bv",
        groups="Lautschrift|Klo Bv",
        kreis="Klo",
        ort="Bv",
    )
    LAUT_KLO_DW = Sammlung(
        trace="Klo Dw",
        groups="Lautschrift|Klo Dw",
        kreis="Klo",
        ort="Dw",
    )
    LAUT_KLO_EB = Sammlung(
        trace="Klo Eb",
        groups="Lautschrift|Klo Eb",
        kreis="Klo",
        ort="Eb",
    )
    LAUT_KLO_EF = Sammlung(
        trace="Klo Ef",
        groups="Lautschrift|Klo Ef",
        kreis="Klo",
        ort="Ef",
    )
    LAUT_KLO_EH = Sammlung(
        trace="Klo Eh",
        groups="Lautschrift|Klo Eh",
        kreis="Klo",
        ort="Eh",
    )
    LAUT_KLO_EL = Sammlung(
        trace="Klo El",
        groups="Lautschrift|Klo El",
        kreis="Klo",
        ort="El",
    )
    LAUT_KLO_EM = Sammlung(
        trace="Klo Em",
        groups="Lautschrift|Klo Em",
        kreis="Klo",
        ort="Em",
    )
    LAUT_KLO_ER = Sammlung(
        trace="Klo Er",
        groups="Lautschrift|Klo Er",
        kreis="Klo",
        ort="Er",
    )
    LAUT_KLO_ES = Sammlung(
        trace="Klo Es",
        groups="Lautschrift|Klo Es",
        kreis="Klo",
        ort="Es",
    )
    LAUT_KLO_EV = Sammlung(
        trace="Klo Ev",
        groups="Lautschrift|Klo Ev",
        kreis="Klo",
        ort="Ev",
    )
    LAUT_KLO_FB = Sammlung(
        trace="Klo Fb",
        groups="Lautschrift|Klo Fb",
        kreis="Klo",
        ort="Fb",
    )
    LAUT_KLO_FR = Sammlung(
        trace="Klo Fr",
        groups="Lautschrift|Klo Fr",
        kreis="Klo",
        ort="Fr",
    )
    LAUT_KLO_GA = Sammlung(
        trace="Klo Ga",
        groups="Lautschrift|Klo Ga",
        kreis="Klo",
        ort="Ga",
    )
    LAUT_KLO_GG = Sammlung(
        trace="Klo Gg",
        groups="Lautschrift|Klo Gg",
        kreis="Klo",
        ort="Gg",
    )
    LAUT_KLO_GL = Sammlung(
        trace="Klo Gl",
        groups="Lautschrift|Klo Gl",
        kreis="Klo",
        ort="Gl",
    )
    LAUT_KLO_GT = Sammlung(
        trace="Klo Gt",
        groups="Lautschrift|Klo Gt",
        kreis="Klo",
        ort="Gt",
    )
    LAUT_KLO_HA = Sammlung(
        trace="Klo Ha",
        groups="Lautschrift|Klo Ha",
        kreis="Klo",
        ort="Ha",
    )
    LAUT_KLO_HB = Sammlung(
        trace="Klo Hb",
        groups="Lautschrift|Klo Hb",
        kreis="Klo",
        ort="Hb",
    )
    LAUT_KLO_HE = Sammlung(
        trace="Klo He",
        groups="Lautschrift|Klo He",
        kreis="Klo",
        ort="He",
    )
    LAUT_KLO_HG = Sammlung(
        trace="Klo Hg",
        groups="Lautschrift|Klo Hg",
        kreis="Klo",
        ort="Hg",
    )
    LAUT_KLO_HH = Sammlung(
        trace="Klo Hh",
        groups="Lautschrift|Klo Hh",
        kreis="Klo",
        ort="Hh",
    )
    LAUT_KLO_HL = Sammlung(
        trace="Klo Hl",
        groups="Lautschrift|Klo Hl",
        kreis="Klo",
        ort="Hl",
    )
    LAUT_KLO_HM = Sammlung(
        trace="Klo Hm",
        groups="Lautschrift|Klo Hm",
        kreis="Klo",
        ort="Hm",
    )
    LAUT_KLO_HO = Sammlung(
        trace="Klo Ho",
        groups="Lautschrift|Klo Ho",
        kreis="Klo",
        ort="Ho",
    )
    LAUT_KLO_HR = Sammlung(
        trace="Klo Hr",
        groups="Lautschrift|Klo Hr",
        kreis="Klo",
        ort="Hr",
    )
    LAUT_KLO_KA = Sammlung(
        trace="Klo Ka",
        groups="Lautschrift|Klo Ka",
        kreis="Klo",
        ort="Ka",
    )
    LAUT_KLO_KF = Sammlung(
        trace="Klo Kf",
        groups="Lautschrift|Klo Kf",
        kreis="Klo",
        ort="Kf",
    )
    LAUT_KLO_KH = Sammlung(
        trace="Klo Kh",
        groups="Lautschrift|Klo Kh",
        kreis="Klo",
        ort="Kh",
    )
    LAUT_KLO_KL = Sammlung(
        trace="Klo Kl",
        groups="Lautschrift|Klo Kl",
        kreis="Klo",
        ort="Kl",
    )
    LAUT_KLO_LA = Sammlung(
        trace="Klo La",
        groups="Lautschrift|Klo La",
        kreis="Klo",
        ort="La",
    )
    LAUT_KLO_LI = Sammlung(
        trace="Klo Li",
        groups="Lautschrift|Klo Li",
        kreis="Klo",
        ort="Li",
    )
    LAUT_KLO_LO = Sammlung(
        trace="Klo Lo",
        groups="Lautschrift|Klo Lo",
        kreis="Klo",
        ort="Lo",
    )
    LAUT_KLO_LÖ = Sammlung(
        trace="Klo Lö",
        groups="Lautschrift|Klo Lö",
        kreis="Klo",
        ort="Lö",
    )
    LAUT_KLO_MA = Sammlung(
        trace="Klo Ma",
        groups="Lautschrift|Klo Ma",
        kreis="Klo",
        ort="Ma",
    )
    LAUT_KLO_MO = Sammlung(
        trace="Klo Mo",
        groups="Lautschrift|Klo Mo",
        kreis="Klo",
        ort="Mo",
    )
    LAUT_KLO_ND = Sammlung(
        trace="Klo Nd",
        groups="Lautschrift|Klo Nd",
        kreis="Klo",
        ort="Nd",
    )
    LAUT_KLO_NM = Sammlung(
        trace="Klo Nm",
        groups="Lautschrift|Klo Nm",
        kreis="Klo",
        ort="Nm",
    )
    LAUT_KLO_NT = Sammlung(
        trace="Klo Nt",
        groups="Lautschrift|Klo Nt",
        kreis="Klo",
        ort="Nt",
    )
    LAUT_KLO_NU = Sammlung(
        trace="Klo Nu",
        groups="Lautschrift|Klo Nu",
        kreis="Klo",
        ort="Nu",
    )
    LAUT_KLO_PD = Sammlung(
        trace="Klo Pd",
        groups="Lautschrift|Klo Pd",
        kreis="Klo",
        ort="Pd",
    )
    LAUT_KLO_PH = Sammlung(
        trace="Klo Ph",
        groups="Lautschrift|Klo Ph",
        kreis="Klo",
        ort="Ph",
    )
    LAUT_KLO_RH = Sammlung(
        trace="Klo Rh",
        groups="Lautschrift|Klo Rh",
        kreis="Klo",
        ort="Rh",
    )
    LAUT_KLO_SE = Sammlung(
        trace="Klo Se",
        groups="Lautschrift|Klo Se",
        kreis="Klo",
        ort="Se",
    )
    LAUT_KLO_SH = Sammlung(
        trace="Klo Sh",
        groups="Lautschrift|Klo Sh",
        kreis="Klo",
        ort="Sh",
    )
    LAUT_KLO_ST = Sammlung(
        trace="Klo St",
        groups="Lautschrift|Klo St",
        kreis="Klo",
        ort="St",
    )
    LAUT_KLO_SW = Sammlung(
        trace="Klo Sw",
        groups="Lautschrift|Klo Sw",
        kreis="Klo",
        ort="Sw",
    )
    LAUT_KLO_TE = Sammlung(
        trace="Klo Te",
        groups="Lautschrift|Klo Te",
        kreis="Klo",
        ort="Te",
    )
    LAUT_KLO_TÜ = Sammlung(
        trace="Klo Tü",
        groups="Lautschrift|Klo Tü",
        kreis="Klo",
        ort="Tü",
    )
    LAUT_KLO_TW = Sammlung(
        trace="Klo Tw",
        groups="Lautschrift|Klo Tw",
        kreis="Klo",
        ort="Tw",
    )
    LAUT_KLO_VA = Sammlung(
        trace="Klo Va",
        groups="Lautschrift|Klo Va",
        kreis="Klo",
        ort="Va",
    )
    LAUT_KLO_VB = Sammlung(
        trace="Klo Vb",
        groups="Lautschrift|Klo Vb",
        kreis="Klo",
        ort="Vb",
    )
    LAUT_KLO_VT = Sammlung(
        trace="Klo Vt",
        groups="Lautschrift|Klo Vt",
        kreis="Klo",
        ort="Vt",
    )
    LAUT_KLO_WI = Sammlung(
        trace="Klo Wi",
        groups="Lautschrift|Klo Wi",
        kreis="Klo",
        ort="Wi",
    )
    LAUT_KLO_WS = Sammlung(
        trace="Klo Ws",
        groups="Lautschrift|Klo Ws",
        kreis="Klo",
        ort="Ws",
    )
    LAUT_KOS_AU = Sammlung(
        trace="Kos Au",
        groups="Lautschrift|Kos Au",
        kreis="Kos",
        ort="Au",
    )
    LAUT_KOS_BA = Sammlung(
        trace="Kos Ba",
        groups="Lautschrift|Kos Ba",
        kreis="Kos",
        ort="Ba",
    )
    LAUT_KOS_BB = Sammlung(
        trace="Kos Bb",
        groups="Lautschrift|Kos Bb",
        kreis="Kos",
        ort="Bb",
    )
    LAUT_KOS_BE = Sammlung(
        trace="Kos Be",
        groups="Lautschrift|Kos Be",
        kreis="Kos",
        ort="Be",
    )
    LAUT_KOS_BÖ = Sammlung(
        trace="Kos Bö",
        groups="Lautschrift|Kos Bö",
        kreis="Kos",
        ort="Bö",
    )
    LAUT_KOS_BU = Sammlung(
        trace="Kos Bu",
        groups="Lautschrift|Kos Bu",
        kreis="Kos",
        ort="Bu",
    )
    LAUT_KOS_BÜ = Sammlung(
        trace="Kos Bü",
        groups="Lautschrift|Kos Bü",
        kreis="Kos",
        ort="Bü",
    )
    LAUT_KOS_DA = Sammlung(
        trace="Kos Da",
        groups="Lautschrift|Kos Da",
        kreis="Kos",
        ort="Da",
    )
    LAUT_KOS_DD = Sammlung(
        trace="Kos Dd",
        groups="Lautschrift|Kos Dd",
        kreis="Kos",
        ort="Dd",
    )
    LAUT_KOS_DF = Sammlung(
        trace="Kos Df",
        groups="Lautschrift|Kos Df",
        kreis="Kos",
        ort="Df",
    )
    LAUT_KOS_DK = Sammlung(
        trace="Kos Dk",
        groups="Lautschrift|Kos Dk",
        kreis="Kos",
        ort="Dk",
    )
    LAUT_KOS_DÜ = Sammlung(
        trace="Kos Dü",
        groups="Lautschrift|Kos Dü",
        kreis="Kos",
        ort="Dü",
    )
    LAUT_KOS_ES = Sammlung(
        trace="Kos Es",
        groups="Lautschrift|Kos Es",
        kreis="Kos",
        ort="Es",
    )
    LAUT_KOS_FL = Sammlung(
        trace="Kos Fl",
        groups="Lautschrift|Kos Fl",
        kreis="Kos",
        ort="Fl",
    )
    LAUT_KOS_GA = Sammlung(
        trace="Kos Ga",
        groups="Lautschrift|Kos Ga",
        kreis="Kos",
        ort="Ga",
    )
    LAUT_KOS_GB = Sammlung(
        trace="Kos Gb",
        groups="Lautschrift|Kos Gb",
        kreis="Kos",
        ort="Gb",
    )
    LAUT_KOS_GE = Sammlung(
        trace="Kos Ge",
        groups="Lautschrift|Kos Ge",
        kreis="Kos",
        ort="Ge",
    )
    LAUT_KOS_GO = Sammlung(
        trace="Kos Go",
        groups="Lautschrift|Kos Go",
        kreis="Kos",
        ort="Go",
    )
    LAUT_KOS_GP = Sammlung(
        trace="Kos Gp",
        groups="Lautschrift|Kos Gp",
        kreis="Kos",
        ort="Gp",
    )
    LAUT_KOS_HA = Sammlung(
        trace="Kos Ha",
        groups="Lautschrift|Kos Ha",
        kreis="Kos",
        ort="Ha",
    )
    LAUT_KOS_HD = Sammlung(
        trace="Kos Hd",
        groups="Lautschrift|Kos Hd",
        kreis="Kos",
        ort="Hd",
    )
    LAUT_KOS_HE = Sammlung(
        trace="Kos He",
        groups="Lautschrift|Kos He",
        kreis="Kos",
        ort="He",
    )
    LAUT_KOS_HI = Sammlung(
        trace="Kos Hi",
        groups="Lautschrift|Kos Hi",
        kreis="Kos",
        ort="Hi",
    )
    LAUT_KOS_HO = Sammlung(
        trace="Kos Ho",
        groups="Lautschrift|Kos Ho",
        kreis="Kos",
        ort="Ho",
    )
    LAUT_KOS_HÖ = Sammlung(
        trace="Kos Hö",
        groups="Lautschrift|Kos Hö",
        kreis="Kos",
        ort="Hö",
    )
    LAUT_KOS_HW = Sammlung(
        trace="Kos Hw",
        groups="Lautschrift|Kos Hw",
        kreis="Kos",
        ort="Hw",
    )
    LAUT_KOS_KA = Sammlung(
        trace="Kos Ka",
        groups="Lautschrift|Kos Ka",
        kreis="Kos",
        ort="Ka",
    )
    LAUT_KOS_KF = Sammlung(
        trace="Kos Kf",
        groups="Lautschrift|Kos Kf",
        kreis="Kos",
        ort="Kf",
    )
    LAUT_KOS_KH = Sammlung(
        trace="Kos Kh",
        groups="Lautschrift|Kos Kh",
        kreis="Kos",
        ort="Kh",
    )
    LAUT_KOS_KL = Sammlung(
        trace="Kos Kl",
        groups="Lautschrift|Kos Kl",
        kreis="Kos",
        ort="Kl",
    )
    LAUT_KOS_LE = Sammlung(
        trace="Kos Le",
        groups="Lautschrift|Kos Le",
        kreis="Kos",
        ort="Le",
    )
    LAUT_KOS_LS = Sammlung(
        trace="Kos Ls",
        groups="Lautschrift|Kos Ls",
        kreis="Kos",
        ort="Ls",
    )
    LAUT_KOS_MF = Sammlung(
        trace="Kos Mf",
        groups="Lautschrift|Kos Mf",
        kreis="Kos",
        ort="Mf",
    )
    LAUT_KOS_MW = Sammlung(
        trace="Kos Mw",
        groups="Lautschrift|Kos Mw",
        kreis="Kos",
        ort="Mw",
    )
    LAUT_KOS_OH = Sammlung(
        trace="Kos Oh",
        groups="Lautschrift|Kos Oh",
        kreis="Kos",
        ort="Oh",
    )
    LAUT_KOS_OW = Sammlung(
        trace="Kos Ow",
        groups="Lautschrift|Kos Ow",
        kreis="Kos",
        ort="Ow",
    )
    LAUT_KOS_RR = Sammlung(
        trace="Kos Rr",
        groups="Lautschrift|Kos Rr",
        kreis="Kos",
        ort="Rr",
    )
    LAUT_KOS_SF = Sammlung(
        trace="Kos Sf",
        groups="Lautschrift|Kos Sf",
        kreis="Kos",
        ort="Sf",
    )
    LAUT_KOS_SK = Sammlung(
        trace="Kos Sk",
        groups="Lautschrift|Kos Sk",
        kreis="Kos",
        ort="Sk",
    )
    LAUT_KOS_ST = Sammlung(
        trace="Kos St",
        groups="Lautschrift|Kos St",
        kreis="Kos",
        ort="St",
    )
    LAUT_KOS_TU = Sammlung(
        trace="Kos Tu",
        groups="Lautschrift|Kos Tu",
        kreis="Kos",
        ort="Tu",
    )
    LAUT_KOS_VI = Sammlung(
        trace="Kos Vi",
        groups="Lautschrift|Kos Vi",
        kreis="Kos",
        ort="Vi",
    )
    LAUT_KOS_WE = Sammlung(
        trace="Kos We",
        groups="Lautschrift|Kos We",
        kreis="Kos",
        ort="We",
    )
    LAUT_LEM_AD = Sammlung(
        trace="Lem Ad",
        groups="Lautschrift|Lem Ad",
        kreis="Lem",
        ort="Ad",
    )
    LAUT_LEM_AL = Sammlung(
        trace="Lem Al",
        groups="Lautschrift|Lem Al",
        kreis="Lem",
        ort="Al",
    )
    LAUT_LEM_AM = Sammlung(
        trace="Lem Am",
        groups="Lautschrift|Lem Am",
        kreis="Lem",
        ort="Am",
    )
    LAUT_LEM_AS = Sammlung(
        trace="Lem As",
        groups="Lautschrift|Lem As",
        kreis="Lem",
        ort="As",
    )
    LAUT_LEM_BA = Sammlung(
        trace="Lem Ba",
        groups="Lautschrift|Lem Ba",
        kreis="Lem",
        ort="Ba",
    )
    LAUT_LEM_BE = Sammlung(
        trace="Lem Be",
        groups="Lautschrift|Lem Be",
        kreis="Lem",
        ort="Be",
    )
    LAUT_LEM_BF = Sammlung(
        trace="Lem Bf",
        groups="Lautschrift|Lem Bf",
        kreis="Lem",
        ort="Bf",
    )
    LAUT_LEM_BG = Sammlung(
        trace="Lem Bg",
        groups="Lautschrift|Lem Bg",
        kreis="Lem",
        ort="Bg",
    )
    LAUT_LEM_BK = Sammlung(
        trace="Lem Bk",
        groups="Lautschrift|Lem Bk",
        kreis="Lem",
        ort="Bk",
    )
    LAUT_LEM_BP = Sammlung(
        trace="Lem Bp",
        groups="Lautschrift|Lem Bp",
        kreis="Lem",
        ort="Bp",
    )
    LAUT_LEM_BR = Sammlung(
        trace="Lem Br",
        groups="Lautschrift|Lem Br",
        kreis="Lem",
        ort="Br",
    )
    LAUT_LEM_BT = Sammlung(
        trace="Lem Bt",
        groups="Lautschrift|Lem Bt",
        kreis="Lem",
        ort="Bt",
    )
    LAUT_LEM_BX = Sammlung(
        trace="Lem Bx",
        groups="Lautschrift|Lem Bx",
        kreis="Lem",
        ort="Bx",
    )
    LAUT_LEM_DÖ = Sammlung(
        trace="Lem Dö",
        groups="Lautschrift|Lem Dö",
        kreis="Lem",
        ort="Dö",
    )
    LAUT_LEM_ER = Sammlung(
        trace="Lem Er",
        groups="Lautschrift|Lem Er",
        kreis="Lem",
        ort="Er",
    )
    LAUT_LEM_GÖ = Sammlung(
        trace="Lem Gö",
        groups="Lautschrift|Lem Gö",
        kreis="Lem",
        ort="Gö",
    )
    LAUT_LEM_GR = Sammlung(
        trace="Lem Gr",
        groups="Lautschrift|Lem Gr",
        kreis="Lem",
        ort="Gr",
    )
    LAUT_LEM_HB = Sammlung(
        trace="Lem Hb",
        groups="Lautschrift|Lem Hb",
        kreis="Lem",
        ort="Hb",
    )
    LAUT_LEM_HD = Sammlung(
        trace="Lem Hd",
        groups="Lautschrift|Lem Hd",
        kreis="Lem",
        ort="Hd",
    )
    LAUT_LEM_HE = Sammlung(
        trace="Lem He",
        groups="Lautschrift|Lem He",
        kreis="Lem",
        ort="He",
    )
    LAUT_LEM_HF = Sammlung(
        trace="Lem Hf",
        groups="Lautschrift|Lem Hf",
        kreis="Lem",
        ort="Hf",
    )
    LAUT_LEM_HG = Sammlung(
        trace="Lem Hg",
        groups="Lautschrift|Lem Hg",
        kreis="Lem",
        ort="Hg",
    )
    LAUT_LEM_HH = Sammlung(
        trace="Lem Hh",
        groups="Lautschrift|Lem Hh",
        kreis="Lem",
        ort="Hh",
    )
    LAUT_LEM_HO = Sammlung(
        trace="Lem Ho",
        groups="Lautschrift|Lem Ho",
        kreis="Lem",
        ort="Ho",
    )
    LAUT_LEM_HÖ = Sammlung(
        trace="Lem Hö",
        groups="Lautschrift|Lem Hö",
        kreis="Lem",
        ort="Hö",
    )
    LAUT_LEM_HT = Sammlung(
        trace="Lem Ht",
        groups="Lautschrift|Lem Ht",
        kreis="Lem",
        ort="Ht",
    )
    LAUT_LEM_KA = Sammlung(
        trace="Lem Ka",
        groups="Lautschrift|Lem Ka",
        kreis="Lem",
        ort="Ka",
    )
    LAUT_LEM_KI = Sammlung(
        trace="Lem Ki",
        groups="Lautschrift|Lem Ki",
        kreis="Lem",
        ort="Ki",
    )
    LAUT_LEM_KN = Sammlung(
        trace="Lem Kn",
        groups="Lautschrift|Lem Kn",
        kreis="Lem",
        ort="Kn",
    )
    LAUT_LEM_LA = Sammlung(
        trace="Lem La",
        groups="Lautschrift|Lem La",
        kreis="Lem",
        ort="La",
    )
    LAUT_LEM_LB = Sammlung(
        trace="Lem Lb",
        groups="Lautschrift|Lem Lb",
        kreis="Lem",
        ort="Lb",
    )
    LAUT_LEM_LC = Sammlung(
        trace="Lem Lc",
        groups="Lautschrift|Lem Lc",
        kreis="Lem",
        ort="Lc",
    )
    LAUT_LEM_LD = Sammlung(
        trace="Lem Ld",
        groups="Lautschrift|Lem Ld",
        kreis="Lem",
        ort="Ld",
    )
    LAUT_LEM_LE = Sammlung(
        trace="Lem Le",
        groups="Lautschrift|Lem Le",
        kreis="Lem",
        ort="Le",
    )
    LAUT_LEM_LF = Sammlung(
        trace="Lem Lf",
        groups="Lautschrift|Lem Lf",
        kreis="Lem",
        ort="Lf",
    )
    LAUT_LEM_LG = Sammlung(
        trace="Lem Lg",
        groups="Lautschrift|Lem Lg",
        kreis="Lem",
        ort="Lg",
    )
    LAUT_LEM_LH = Sammlung(
        trace="Lem Lh",
        groups="Lautschrift|Lem Lh",
        kreis="Lem",
        ort="Lh",
    )
    LAUT_LEM_LI = Sammlung(
        trace="Lem Li",
        groups="Lautschrift|Lem Li",
        kreis="Lem",
        ort="Li",
    )
    LAUT_LEM_LO = Sammlung(
        trace="Lem Lo",
        groups="Lautschrift|Lem Lo",
        kreis="Lem",
        ort="Lo",
    )
    LAUT_LEM_LP = Sammlung(
        trace="Lem Lp",
        groups="Lautschrift|Lem Lp",
        kreis="Lem",
        ort="Lp",
    )
    LAUT_LEM_LR = Sammlung(
        trace="Lem Lr",
        groups="Lautschrift|Lem Lr",
        kreis="Lem",
        ort="Lr",
    )
    LAUT_LEM_LÜ = Sammlung(
        trace="Lem Lü",
        groups="Lautschrift|Lem Lü",
        kreis="Lem",
        ort="Lü",
    )
    LAUT_LEM_MA = Sammlung(
        trace="Lem Ma",
        groups="Lautschrift|Lem Ma",
        kreis="Lem",
        ort="Ma",
    )
    LAUT_LEM_MB = Sammlung(
        trace="Lem Mb",
        groups="Lautschrift|Lem Mb",
        kreis="Lem",
        ort="Mb",
    )
    LAUT_LEM_MT = Sammlung(
        trace="Lem Mt",
        groups="Lautschrift|Lem Mt",
        kreis="Lem",
        ort="Mt",
    )
    LAUT_LEM_ÖR = Sammlung(
        trace="Lem Ör",
        groups="Lautschrift|Lem Ör",
        kreis="Lem",
        ort="Ör",
    )
    LAUT_LEM_RE = Sammlung(
        trace="Lem Re",
        groups="Lautschrift|Lem Re",
        kreis="Lem",
        ort="Re",
    )
    LAUT_LEM_SB = Sammlung(
        trace="Lem Sb",
        groups="Lautschrift|Lem Sb",
        kreis="Lem",
        ort="Sb",
    )
    LAUT_LEM_SC = Sammlung(
        trace="Lem Sc",
        groups="Lautschrift|Lem Sc",
        kreis="Lem",
        ort="Sc",
    )
    LAUT_LEM_SE = Sammlung(
        trace="Lem Se",
        groups="Lautschrift|Lem Se",
        kreis="Lem",
        ort="Se",
    )
    LAUT_LEM_SH = Sammlung(
        trace="Lem Sh",
        groups="Lautschrift|Lem Sh",
        kreis="Lem",
        ort="Sh",
    )
    LAUT_LEM_SI = Sammlung(
        trace="Lem Si",
        groups="Lautschrift|Lem Si",
        kreis="Lem",
        ort="Si",
    )
    LAUT_LEM_SM = Sammlung(
        trace="Lem Sm",
        groups="Lautschrift|Lem Sm",
        kreis="Lem",
        ort="Sm",
    )
    LAUT_LEM_ST = Sammlung(
        trace="Lem St",
        groups="Lautschrift|Lem St",
        kreis="Lem",
        ort="St",
    )
    LAUT_LEM_SU = Sammlung(
        trace="Lem Su",
        groups="Lautschrift|Lem Su",
        kreis="Lem",
        ort="Su",
    )
    LAUT_LEM_SW = Sammlung(
        trace="Lem Sw",
        groups="Lautschrift|Lem Sw",
        kreis="Lem",
        ort="Sw",
    )
    LAUT_LEM_SX = Sammlung(
        trace="Lem Sx",
        groups="Lautschrift|Lem Sx",
        kreis="Lem",
        ort="Sx",
    )
    LAUT_LEM_TA = Sammlung(
        trace="Lem Ta",
        groups="Lautschrift|Lem Ta",
        kreis="Lem",
        ort="Ta",
    )
    LAUT_LEM_VA = Sammlung(
        trace="Lem Va",
        groups="Lautschrift|Lem Va",
        kreis="Lem",
        ort="Va",
    )
    LAUT_LEM_VH = Sammlung(
        trace="Lem Vh",
        groups="Lautschrift|Lem Vh",
        kreis="Lem",
        ort="Vh",
    )
    LAUT_LEM_VO = Sammlung(
        trace="Lem Vo",
        groups="Lautschrift|Lem Vo",
        kreis="Lem",
        ort="Vo",
    )
    LAUT_LEM_WA = Sammlung(
        trace="Lem Wa",
        groups="Lautschrift|Lem Wa",
        kreis="Lem",
        ort="Wa",
    )
    LAUT_LEM_WB = Sammlung(
        trace="Lem Wb",
        groups="Lautschrift|Lem Wb",
        kreis="Lem",
        ort="Wb",
    )
    LAUT_LEM_WD = Sammlung(
        trace="Lem Wd",
        groups="Lautschrift|Lem Wd",
        kreis="Lem",
        ort="Wd",
    )
    LAUT_LEM_WH = Sammlung(
        trace="Lem Wh",
        groups="Lautschrift|Lem Wh",
        kreis="Lem",
        ort="Wh",
    )
    LAUT_LEM_WR = Sammlung(
        trace="Lem Wr",
        groups="Lautschrift|Lem Wr",
        kreis="Lem",
        ort="Wr",
    )
    LAUT_LEM_WÜ = Sammlung(
        trace="Lem Wü",
        groups="Lautschrift|Lem Wü",
        kreis="Lem",
        ort="Wü",
    )
    LAUT_LHS_AB = Sammlung(
        trace="Lhs Ab",
        groups="Lautschrift|Lhs Ab",
        kreis="Lhs",
        ort="Ab",
    )
    LAUT_LHS_AH = Sammlung(
        trace="Lhs Ah",
        groups="Lautschrift|Lhs Ah",
        kreis="Lhs",
        ort="Ah",
    )
    LAUT_LHS_AL = Sammlung(
        trace="Lhs Al",
        groups="Lautschrift|Lhs Al",
        kreis="Lhs",
        ort="Al",
    )
    LAUT_LHS_BB = Sammlung(
        trace="Lhs Bb",
        groups="Lautschrift|Lhs Bb",
        kreis="Lhs",
        ort="Bb",
    )
    LAUT_LHS_BH = Sammlung(
        trace="Lhs Bh",
        groups="Lautschrift|Lhs Bh",
        kreis="Lhs",
        ort="Bh",
    )
    LAUT_LHS_BK = Sammlung(
        trace="Lhs Bk",
        groups="Lautschrift|Lhs Bk",
        kreis="Lhs",
        ort="Bk",
    )
    LAUT_LHS_BO = Sammlung(
        trace="Lhs Bo",
        groups="Lautschrift|Lhs Bo",
        kreis="Lhs",
        ort="Bo",
    )
    LAUT_LHS_DB = Sammlung(
        trace="Lhs Db",
        groups="Lautschrift|Lhs Db",
        kreis="Lhs",
        ort="Db",
    )
    LAUT_LHS_DR = Sammlung(
        trace="Lhs Dr",
        groups="Lautschrift|Lhs Dr",
        kreis="Lhs",
        ort="Dr",
    )
    LAUT_LHS_EI = Sammlung(
        trace="Lhs Ei",
        groups="Lautschrift|Lhs Ei",
        kreis="Lhs",
        ort="Ei",
    )
    LAUT_LHS_EL = Sammlung(
        trace="Lhs El",
        groups="Lautschrift|Lhs El",
        kreis="Lhs",
        ort="El",
    )
    LAUT_LHS_EM = Sammlung(
        trace="Lhs Em",
        groups="Lautschrift|Lhs Em",
        kreis="Lhs",
        ort="Em",
    )
    LAUT_LHS_ER = Sammlung(
        trace="Lhs Er",
        groups="Lautschrift|Lhs Er",
        kreis="Lhs",
        ort="Er",
    )
    LAUT_LHS_FH = Sammlung(
        trace="Lhs Fh",
        groups="Lautschrift|Lhs Fh",
        kreis="Lhs",
        ort="Fh",
    )
    LAUT_LHS_HE = Sammlung(
        trace="Lhs He",
        groups="Lautschrift|Lhs He",
        kreis="Lhs",
        ort="He",
    )
    LAUT_LHS_HO = Sammlung(
        trace="Lhs Ho",
        groups="Lautschrift|Lhs Ho",
        kreis="Lhs",
        ort="Ho",
    )
    LAUT_LHS_HÖ = Sammlung(
        trace="Lhs Hö",
        groups="Lautschrift|Lhs Hö",
        kreis="Lhs",
        ort="Hö",
    )
    LAUT_LHS_HS = Sammlung(
        trace="Lhs Hs",
        groups="Lautschrift|Lhs Hs",
        kreis="Lhs",
        ort="Hs",
    )
    LAUT_LHS_KA = Sammlung(
        trace="Lhs Ka",
        groups="Lautschrift|Lhs Ka",
        kreis="Lhs",
        ort="Ka",
    )
    LAUT_LHS_LA = Sammlung(
        trace="Lhs La",
        groups="Lautschrift|Lhs La",
        kreis="Lhs",
        ort="La",
    )
    LAUT_LHS_LH = Sammlung(
        trace="Lhs Lh",
        groups="Lautschrift|Lhs Lh",
        kreis="Lhs",
        ort="Lh",
    )
    LAUT_LHS_ME = Sammlung(
        trace="Lhs Me",
        groups="Lautschrift|Lhs Me",
        kreis="Lhs",
        ort="Me",
    )
    LAUT_LHS_NB = Sammlung(
        trace="Lhs Nb",
        groups="Lautschrift|Lhs Nb",
        kreis="Lhs",
        ort="Nb",
    )
    LAUT_LHS_NK = Sammlung(
        trace="Lhs Nk",
        groups="Lautschrift|Lhs Nk",
        kreis="Lhs",
        ort="Nk",
    )
    LAUT_LHS_OB = Sammlung(
        trace="Lhs Ob",
        groups="Lautschrift|Lhs Ob",
        kreis="Lhs",
        ort="Ob",
    )
    LAUT_LHS_OL = Sammlung(
        trace="Lhs Ol",
        groups="Lautschrift|Lhs Ol",
        kreis="Lhs",
        ort="Ol",
    )
    LAUT_LHS_ON = Sammlung(
        trace="Lhs On",
        groups="Lautschrift|Lhs On",
        kreis="Lhs",
        ort="On",
    )
    LAUT_LHS_SE = Sammlung(
        trace="Lhs Se",
        groups="Lautschrift|Lhs Se",
        kreis="Lhs",
        ort="Se",
    )
    LAUT_LHS_SK = Sammlung(
        trace="Lhs Sk",
        groups="Lautschrift|Lhs Sk",
        kreis="Lhs",
        ort="Sk",
    )
    LAUT_LHS_SM = Sammlung(
        trace="Lhs Sm",
        groups="Lautschrift|Lhs Sm",
        kreis="Lhs",
        ort="Sm",
    )
    LAUT_LHS_SR = Sammlung(
        trace="Lhs Sr",
        groups="Lautschrift|Lhs Sr",
        kreis="Lhs",
        ort="Sr",
    )
    LAUT_LHS_ST = Sammlung(
        trace="Lhs St",
        groups="Lautschrift|Lhs St",
        kreis="Lhs",
        ort="St",
    )
    LAUT_LHS_TE = Sammlung(
        trace="Lhs Te",
        groups="Lautschrift|Lhs Te",
        kreis="Lhs",
        ort="Te",
    )
    LAUT_LHS_TH = Sammlung(
        trace="Lhs Th",
        groups="Lautschrift|Lhs Th",
        kreis="Lhs",
        ort="Th",
    )
    LAUT_LHS_VE = Sammlung(
        trace="Lhs Ve",
        groups="Lautschrift|Lhs Ve",
        kreis="Lhs",
        ort="Ve",
    )
    LAUT_LHS_VI = Sammlung(
        trace="Lhs Vi",
        groups="Lautschrift|Lhs Vi",
        kreis="Lhs",
        ort="Vi",
    )
    LAUT_LHS_WE = Sammlung(
        trace="Lhs We",
        groups="Lautschrift|Lhs We",
        kreis="Lhs",
        ort="We",
    )
    LAUT_LHS_WI = Sammlung(
        trace="Lhs Wi",
        groups="Lautschrift|Lhs Wi",
        kreis="Lhs",
        ort="Wi",
    )
    LAUT_LHS_WL = Sammlung(
        trace="Lhs Wl",
        groups="Lautschrift|Lhs Wl",
        kreis="Lhs",
        ort="Wl",
    )
    LAUT_LHS_WN = Sammlung(
        trace="Lhs Wn",
        groups="Lautschrift|Lhs Wn",
        kreis="Lhs",
        ort="Wn",
    )
    LAUT_LHS_WP = Sammlung(
        trace="Lhs Wp",
        groups="Lautschrift|Lhs Wp",
        kreis="Lhs",
        ort="Wp",
    )
    LAUT_LHS_WS = Sammlung(
        trace="Lhs Ws",
        groups="Lautschrift|Lhs Ws",
        kreis="Lhs",
        ort="Ws",
    )
    LAUT_LIN_AL = Sammlung(
        trace="Lin Al",
        groups="Lautschrift|Lin Al",
        kreis="Lin",
        ort="Al",
    )
    LAUT_LIN_AV = Sammlung(
        trace="Lin Av",
        groups="Lautschrift|Lin Av",
        kreis="Lin",
        ort="Av",
    )
    LAUT_LIN_AX = Sammlung(
        trace="Lin Ax",
        groups="Lautschrift|Lin Ax",
        kreis="Lin",
        ort="Ax",
    )
    LAUT_LIN_AY = Sammlung(
        trace="Lin Ay",
        groups="Lautschrift|Lin Ay",
        kreis="Lin",
        ort="Ay",
    )
    LAUT_LIN_BA = Sammlung(
        trace="Lin Ba",
        groups="Lautschrift|Lin Ba",
        kreis="Lin",
        ort="Ba",
    )
    LAUT_LIN_BE = Sammlung(
        trace="Lin Be",
        groups="Lautschrift|Lin Be",
        kreis="Lin",
        ort="Be",
    )
    LAUT_LIN_BH = Sammlung(
        trace="Lin Bh",
        groups="Lautschrift|Lin Bh",
        kreis="Lin",
        ort="Bh",
    )
    LAUT_LIN_BI = Sammlung(
        trace="Lin Bi",
        groups="Lautschrift|Lin Bi",
        kreis="Lin",
        ort="Bi",
    )
    LAUT_LIN_BK = Sammlung(
        trace="Lin Bk",
        groups="Lautschrift|Lin Bk",
        kreis="Lin",
        ort="Bk",
    )
    LAUT_LIN_BL = Sammlung(
        trace="Lin Bl",
        groups="Lautschrift|Lin Bl",
        kreis="Lin",
        ort="Bl",
    )
    LAUT_LIN_BR = Sammlung(
        trace="Lin Br",
        groups="Lautschrift|Lin Br",
        kreis="Lin",
        ort="Br",
    )
    LAUT_LIN_BS = Sammlung(
        trace="Lin Bs",
        groups="Lautschrift|Lin Bs",
        kreis="Lin",
        ort="Bs",
    )
    LAUT_LIN_BT = Sammlung(
        trace="Lin Bt",
        groups="Lautschrift|Lin Bt",
        kreis="Lin",
        ort="Bt",
    )
    LAUT_LIN_BW = Sammlung(
        trace="Lin Bw",
        groups="Lautschrift|Lin Bw",
        kreis="Lin",
        ort="Bw",
    )
    LAUT_LIN_BX = Sammlung(
        trace="Lin Bx",
        groups="Lautschrift|Lin Bx",
        kreis="Lin",
        ort="Bx",
    )
    LAUT_LIN_DA = Sammlung(
        trace="Lin Da",
        groups="Lautschrift|Lin Da",
        kreis="Lin",
        ort="Da",
    )
    LAUT_LIN_DP = Sammlung(
        trace="Lin Dp",
        groups="Lautschrift|Lin Dp",
        kreis="Lin",
        ort="Dp",
    )
    LAUT_LIN_EB = Sammlung(
        trace="Lin Eb",
        groups="Lautschrift|Lin Eb",
        kreis="Lin",
        ort="Eb",
    )
    LAUT_LIN_EM = Sammlung(
        trace="Lin Em",
        groups="Lautschrift|Lin Em",
        kreis="Lin",
        ort="Em",
    )
    LAUT_LIN_ES = Sammlung(
        trace="Lin Es",
        groups="Lautschrift|Lin Es",
        kreis="Lin",
        ort="Es",
    )
    LAUT_LIN_FR = Sammlung(
        trace="Lin Fr",
        groups="Lautschrift|Lin Fr",
        kreis="Lin",
        ort="Fr",
    )
    LAUT_LIN_GE = Sammlung(
        trace="Lin Ge",
        groups="Lautschrift|Lin Ge",
        kreis="Lin",
        ort="Ge",
    )
    LAUT_LIN_GL = Sammlung(
        trace="Lin Gl",
        groups="Lautschrift|Lin Gl",
        kreis="Lin",
        ort="Gl",
    )
    LAUT_LIN_HA = Sammlung(
        trace="Lin Ha",
        groups="Lautschrift|Lin Ha",
        kreis="Lin",
        ort="Ha",
    )
    LAUT_LIN_HD = Sammlung(
        trace="Lin Hd",
        groups="Lautschrift|Lin Hd",
        kreis="Lin",
        ort="Hd",
    )
    LAUT_LIN_HH = Sammlung(
        trace="Lin Hh",
        groups="Lautschrift|Lin Hh",
        kreis="Lin",
        ort="Hh",
    )
    LAUT_LIN_HO = Sammlung(
        trace="Lin Ho",
        groups="Lautschrift|Lin Ho",
        kreis="Lin",
        ort="Ho",
    )
    LAUT_LIN_LA = Sammlung(
        trace="Lin La",
        groups="Lautschrift|Lin La",
        kreis="Lin",
        ort="La",
    )
    LAUT_LIN_LE = Sammlung(
        trace="Lin Le",
        groups="Lautschrift|Lin Le",
        kreis="Lin",
        ort="Le",
    )
    LAUT_LIN_LI = Sammlung(
        trace="Lin Li",
        groups="Lautschrift|Lin Li",
        kreis="Lin",
        ort="Li",
    )
    LAUT_LIN_LO = Sammlung(
        trace="Lin Lo",
        groups="Lautschrift|Lin Lo",
        kreis="Lin",
        ort="Lo",
    )
    LAUT_LIN_LS = Sammlung(
        trace="Lin Ls",
        groups="Lautschrift|Lin Ls",
        kreis="Lin",
        ort="Ls",
    )
    LAUT_LIN_LT = Sammlung(
        trace="Lin Lt",
        groups="Lautschrift|Lin Lt",
        kreis="Lin",
        ort="Lt",
    )
    LAUT_LIN_LX = Sammlung(
        trace="Lin Lx",
        groups="Lautschrift|Lin Lx",
        kreis="Lin",
        ort="Lx",
    )
    LAUT_LIN_ME = Sammlung(
        trace="Lin Me",
        groups="Lautschrift|Lin Me",
        kreis="Lin",
        ort="Me",
    )
    LAUT_LIN_MR = Sammlung(
        trace="Lin Mr",
        groups="Lautschrift|Lin Mr",
        kreis="Lin",
        ort="Mr",
    )
    LAUT_LIN_MU = Sammlung(
        trace="Lin Mu",
        groups="Lautschrift|Lin Mu",
        kreis="Lin",
        ort="Mu",
    )
    LAUT_LIN_NL = Sammlung(
        trace="Lin Nl",
        groups="Lautschrift|Lin Nl",
        kreis="Lin",
        ort="Nl",
    )
    LAUT_LIN_PL = Sammlung(
        trace="Lin Pl",
        groups="Lautschrift|Lin Pl",
        kreis="Lin",
        ort="Pl",
    )
    LAUT_LIN_PO = Sammlung(
        trace="Lin Po",
        groups="Lautschrift|Lin Po",
        kreis="Lin",
        ort="Po",
    )
    LAUT_LIN_SB = Sammlung(
        trace="Lin Sb",
        groups="Lautschrift|Lin Sb",
        kreis="Lin",
        ort="Sb",
    )
    LAUT_LIN_SC = Sammlung(
        trace="Lin Sc",
        groups="Lautschrift|Lin Sc",
        kreis="Lin",
        ort="Sc",
    )
    LAUT_LIN_SD = Sammlung(
        trace="Lin Sd",
        groups="Lautschrift|Lin Sd",
        kreis="Lin",
        ort="Sd",
    )
    LAUT_LIN_SL = Sammlung(
        trace="Lin Sl",
        groups="Lautschrift|Lin Sl",
        kreis="Lin",
        ort="Sl",
    )
    LAUT_LIN_SN = Sammlung(
        trace="Lin Sn",
        groups="Lautschrift|Lin Sn",
        kreis="Lin",
        ort="Sn",
    )
    LAUT_LIN_SP = Sammlung(
        trace="Lin Sp",
        groups="Lautschrift|Lin Sp",
        kreis="Lin",
        ort="Sp",
    )
    LAUT_LIN_ST = Sammlung(
        trace="Lin St",
        groups="Lautschrift|Lin St",
        kreis="Lin",
        ort="St",
    )
    LAUT_LIN_SU = Sammlung(
        trace="Lin Su",
        groups="Lautschrift|Lin Su",
        kreis="Lin",
        ort="Su",
    )
    LAUT_LIN_TH = Sammlung(
        trace="Lin Th",
        groups="Lautschrift|Lin Th",
        kreis="Lin",
        ort="Th",
    )
    LAUT_LIN_VA = Sammlung(
        trace="Lin Va",
        groups="Lautschrift|Lin Va",
        kreis="Lin",
        ort="Va",
    )
    LAUT_LIN_VH = Sammlung(
        trace="Lin Vh",
        groups="Lautschrift|Lin Vh",
        kreis="Lin",
        ort="Vh",
    )
    LAUT_LIN_WD = Sammlung(
        trace="Lin Wd",
        groups="Lautschrift|Lin Wd",
        kreis="Lin",
        ort="Wd",
    )
    LAUT_LIN_WE = Sammlung(
        trace="Lin We",
        groups="Lautschrift|Lin We",
        kreis="Lin",
        ort="We",
    )
    LAUT_LST_AG = Sammlung(
        trace="Lst Ag",
        groups="Lautschrift|Lst Ag",
        kreis="Lst",
        ort="Ag",
    )
    LAUT_LST_AN = Sammlung(
        trace="Lst An",
        groups="Lautschrift|Lst An",
        kreis="Lst",
        ort="An",
    )
    LAUT_LST_AR = Sammlung(
        trace="Lst Ar",
        groups="Lautschrift|Lst Ar",
        kreis="Lst",
        ort="Ar",
    )
    LAUT_LST_BB = Sammlung(
        trace="Lst Bb",
        groups="Lautschrift|Lst Bb",
        kreis="Lst",
        ort="Bb",
    )
    LAUT_LST_BF = Sammlung(
        trace="Lst Bf",
        groups="Lautschrift|Lst Bf",
        kreis="Lst",
        ort="Bf",
    )
    LAUT_LST_BG = Sammlung(
        trace="Lst Bg",
        groups="Lautschrift|Lst Bg",
        kreis="Lst",
        ort="Bg",
    )
    LAUT_LST_BH = Sammlung(
        trace="Lst Bh",
        groups="Lautschrift|Lst Bh",
        kreis="Lst",
        ort="Bh",
    )
    LAUT_LST_BÖ = Sammlung(
        trace="Lst Bö",
        groups="Lautschrift|Lst Bö",
        kreis="Lst",
        ort="Bö",
    )
    LAUT_LST_DH = Sammlung(
        trace="Lst Dh",
        groups="Lautschrift|Lst Dh",
        kreis="Lst",
        ort="Dh",
    )
    LAUT_LST_DR = Sammlung(
        trace="Lst Dr",
        groups="Lautschrift|Lst Dr",
        kreis="Lst",
        ort="Dr",
    )
    LAUT_LST_EB = Sammlung(
        trace="Lst Eb",
        groups="Lautschrift|Lst Eb",
        kreis="Lst",
        ort="Eb",
    )
    LAUT_LST_EF = Sammlung(
        trace="Lst Ef",
        groups="Lautschrift|Lst Ef",
        kreis="Lst",
        ort="Ef",
    )
    LAUT_LST_EH = Sammlung(
        trace="Lst Eh",
        groups="Lautschrift|Lst Eh",
        kreis="Lst",
        ort="Eh",
    )
    LAUT_LST_EI = Sammlung(
        trace="Lst Ei",
        groups="Lautschrift|Lst Ei",
        kreis="Lst",
        ort="Ei",
    )
    LAUT_LST_ER = Sammlung(
        trace="Lst Er",
        groups="Lautschrift|Lst Er",
        kreis="Lst",
        ort="Er",
    )
    LAUT_LST_ES = Sammlung(
        trace="Lst Es",
        groups="Lautschrift|Lst Es",
        kreis="Lst",
        ort="Es",
    )
    LAUT_LST_GE = Sammlung(
        trace="Lst Ge",
        groups="Lautschrift|Lst Ge",
        kreis="Lst",
        ort="Ge",
    )
    LAUT_LST_HE = Sammlung(
        trace="Lst He",
        groups="Lautschrift|Lst He",
        kreis="Lst",
        ort="He",
    )
    LAUT_LST_HH = Sammlung(
        trace="Lst Hh",
        groups="Lautschrift|Lst Hh",
        kreis="Lst",
        ort="Hh",
    )
    LAUT_LST_HO = Sammlung(
        trace="Lst Ho",
        groups="Lautschrift|Lst Ho",
        kreis="Lst",
        ort="Ho",
    )
    LAUT_LST_HS = Sammlung(
        trace="Lst Hs",
        groups="Lautschrift|Lst Hs",
        kreis="Lst",
        ort="Hs",
    )
    LAUT_LST_KA = Sammlung(
        trace="Lst Ka",
        groups="Lautschrift|Lst Ka",
        kreis="Lst",
        ort="Ka",
    )
    LAUT_LST_KH = Sammlung(
        trace="Lst Kh",
        groups="Lautschrift|Lst Kh",
        kreis="Lst",
        ort="Kh",
    )
    LAUT_LST_KL = Sammlung(
        trace="Lst Kl",
        groups="Lautschrift|Lst Kl",
        kreis="Lst",
        ort="Kl",
    )
    LAUT_LST_KN = Sammlung(
        trace="Lst Kn",
        groups="Lautschrift|Lst Kn",
        kreis="Lst",
        ort="Kn",
    )
    LAUT_LST_KP = Sammlung(
        trace="Lst Kp",
        groups="Lautschrift|Lst Kp",
        kreis="Lst",
        ort="Kp",
    )
    LAUT_LST_LA = Sammlung(
        trace="Lst La",
        groups="Lautschrift|Lst La",
        kreis="Lst",
        ort="La",
    )
    LAUT_LST_LI = Sammlung(
        trace="Lst Li",
        groups="Lautschrift|Lst Li",
        kreis="Lst",
        ort="Li",
    )
    LAUT_LST_LR = Sammlung(
        trace="Lst Lr",
        groups="Lautschrift|Lst Lr",
        kreis="Lst",
        ort="Lr",
    )
    LAUT_LST_LS = Sammlung(
        trace="Lst Ls",
        groups="Lautschrift|Lst Ls",
        kreis="Lst",
        ort="Ls",
    )
    LAUT_LST_ME = Sammlung(
        trace="Lst Me",
        groups="Lautschrift|Lst Me",
        kreis="Lst",
        ort="Me",
    )
    LAUT_LST_MH = Sammlung(
        trace="Lst Mh",
        groups="Lautschrift|Lst Mh",
        kreis="Lst",
        ort="Mh",
    )
    LAUT_LST_MÖ = Sammlung(
        trace="Lst Mö",
        groups="Lautschrift|Lst Mö",
        kreis="Lst",
        ort="Mö",
    )
    LAUT_LST_MS = Sammlung(
        trace="Lst Ms",
        groups="Lautschrift|Lst Ms",
        kreis="Lst",
        ort="Ms",
    )
    LAUT_LST_MZ = Sammlung(
        trace="Lst Mz",
        groups="Lautschrift|Lst Mz",
        kreis="Lst",
        ort="Mz",
    )
    LAUT_LST_OH = Sammlung(
        trace="Lst Oh",
        groups="Lautschrift|Lst Oh",
        kreis="Lst",
        ort="Oh",
    )
    LAUT_LST_ÖS = Sammlung(
        trace="Lst Ös",
        groups="Lautschrift|Lst Ös",
        kreis="Lst",
        ort="Ös",
    )
    LAUT_LST_RI = Sammlung(
        trace="Lst Ri",
        groups="Lautschrift|Lst Ri",
        kreis="Lst",
        ort="Ri",
    )
    LAUT_LST_RO = Sammlung(
        trace="Lst Ro",
        groups="Lautschrift|Lst Ro",
        kreis="Lst",
        ort="Ro",
    )
    LAUT_LST_RÜ = Sammlung(
        trace="Lst Rü",
        groups="Lautschrift|Lst Rü",
        kreis="Lst",
        ort="Rü",
    )
    LAUT_LST_SC = Sammlung(
        trace="Lst Sc",
        groups="Lautschrift|Lst Sc",
        kreis="Lst",
        ort="Sc",
    )
    LAUT_LST_SL = Sammlung(
        trace="Lst Sl",
        groups="Lautschrift|Lst Sl",
        kreis="Lst",
        ort="Sl",
    )
    LAUT_LST_SM = Sammlung(
        trace="Lst Sm",
        groups="Lautschrift|Lst Sm",
        kreis="Lst",
        ort="Sm",
    )
    LAUT_LST_ST = Sammlung(
        trace="Lst St",
        groups="Lautschrift|Lst St",
        kreis="Lst",
        ort="St",
    )
    LAUT_LST_SU = Sammlung(
        trace="Lst Su",
        groups="Lautschrift|Lst Su",
        kreis="Lst",
        ort="Su",
    )
    LAUT_LST_VÖ = Sammlung(
        trace="Lst Vö",
        groups="Lautschrift|Lst Vö",
        kreis="Lst",
        ort="Vö",
    )
    LAUT_LST_WK = Sammlung(
        trace="Lst Wk",
        groups="Lautschrift|Lst Wk",
        kreis="Lst",
        ort="Wk",
    )
    LAUT_LÜB_AL = Sammlung(
        trace="Lüb Al",
        groups="Lautschrift|Lüb Al",
        kreis="Lüb",
        ort="Al",
    )
    LAUT_LÜB_AR = Sammlung(
        trace="Lüb Ar",
        groups="Lautschrift|Lüb Ar",
        kreis="Lüb",
        ort="Ar",
    )
    LAUT_LÜB_AS = Sammlung(
        trace="Lüb As",
        groups="Lautschrift|Lüb As",
        kreis="Lüb",
        ort="As",
    )
    LAUT_LÜB_BA = Sammlung(
        trace="Lüb Ba",
        groups="Lautschrift|Lüb Ba",
        kreis="Lüb",
        ort="Ba",
    )
    LAUT_LÜB_BH = Sammlung(
        trace="Lüb Bh",
        groups="Lautschrift|Lüb Bh",
        kreis="Lüb",
        ort="Bh",
    )
    LAUT_LÜB_BL = Sammlung(
        trace="Lüb Bl",
        groups="Lautschrift|Lüb Bl",
        kreis="Lüb",
        ort="Bl",
    )
    LAUT_LÜB_BR = Sammlung(
        trace="Lüb Br",
        groups="Lautschrift|Lüb Br",
        kreis="Lüb",
        ort="Br",
    )
    LAUT_LÜB_BÜ = Sammlung(
        trace="Lüb Bü",
        groups="Lautschrift|Lüb Bü",
        kreis="Lüb",
        ort="Bü",
    )
    LAUT_LÜB_DE = Sammlung(
        trace="Lüb De",
        groups="Lautschrift|Lüb De",
        kreis="Lüb",
        ort="De",
    )
    LAUT_LÜB_DI = Sammlung(
        trace="Lüb Di",
        groups="Lautschrift|Lüb Di",
        kreis="Lüb",
        ort="Di",
    )
    LAUT_LÜB_DR = Sammlung(
        trace="Lüb Dr",
        groups="Lautschrift|Lüb Dr",
        kreis="Lüb",
        ort="Dr",
    )
    LAUT_LÜB_EN = Sammlung(
        trace="Lüb En",
        groups="Lautschrift|Lüb En",
        kreis="Lüb",
        ort="En",
    )
    LAUT_LÜB_FA = Sammlung(
        trace="Lüb Fa",
        groups="Lautschrift|Lüb Fa",
        kreis="Lüb",
        ort="Fa",
    )
    LAUT_LÜB_FI = Sammlung(
        trace="Lüb Fi",
        groups="Lautschrift|Lüb Fi",
        kreis="Lüb",
        ort="Fi",
    )
    LAUT_LÜB_FR = Sammlung(
        trace="Lüb Fr",
        groups="Lautschrift|Lüb Fr",
        kreis="Lüb",
        ort="Fr",
    )
    LAUT_LÜB_FS = Sammlung(
        trace="Lüb Fs",
        groups="Lautschrift|Lüb Fs",
        kreis="Lüb",
        ort="Fs",
    )
    LAUT_LÜB_GB = Sammlung(
        trace="Lüb Gb",
        groups="Lautschrift|Lüb Gb",
        kreis="Lüb",
        ort="Gb",
    )
    LAUT_LÜB_GE = Sammlung(
        trace="Lüb Ge",
        groups="Lautschrift|Lüb Ge",
        kreis="Lüb",
        ort="Ge",
    )
    LAUT_LÜB_HA = Sammlung(
        trace="Lüb Ha",
        groups="Lautschrift|Lüb Ha",
        kreis="Lüb",
        ort="Ha",
    )
    LAUT_LÜB_HE = Sammlung(
        trace="Lüb He",
        groups="Lautschrift|Lüb He",
        kreis="Lüb",
        ort="He",
    )
    LAUT_LÜB_HH = Sammlung(
        trace="Lüb Hh",
        groups="Lautschrift|Lüb Hh",
        kreis="Lüb",
        ort="Hh",
    )
    LAUT_LÜB_HL = Sammlung(
        trace="Lüb Hl",
        groups="Lautschrift|Lüb Hl",
        kreis="Lüb",
        ort="Hl",
    )
    LAUT_LÜB_HO = Sammlung(
        trace="Lüb Ho",
        groups="Lautschrift|Lüb Ho",
        kreis="Lüb",
        ort="Ho",
    )
    LAUT_LÜB_HT = Sammlung(
        trace="Lüb Ht",
        groups="Lautschrift|Lüb Ht",
        kreis="Lüb",
        ort="Ht",
    )
    LAUT_LÜB_HÜ = Sammlung(
        trace="Lüb Hü",
        groups="Lautschrift|Lüb Hü",
        kreis="Lüb",
        ort="Hü",
    )
    LAUT_LÜB_IS = Sammlung(
        trace="Lüb Is",
        groups="Lautschrift|Lüb Is",
        kreis="Lüb",
        ort="Is",
    )
    LAUT_LÜB_KL = Sammlung(
        trace="Lüb Kl",
        groups="Lautschrift|Lüb Kl",
        kreis="Lüb",
        ort="Kl",
    )
    LAUT_LÜB_LB = Sammlung(
        trace="Lüb Lb",
        groups="Lautschrift|Lüb Lb",
        kreis="Lüb",
        ort="Lb",
    )
    LAUT_LÜB_LE = Sammlung(
        trace="Lüb Le",
        groups="Lautschrift|Lüb Le",
        kreis="Lüb",
        ort="Le",
    )
    LAUT_LÜB_MO = Sammlung(
        trace="Lüb Mo",
        groups="Lautschrift|Lüb Mo",
        kreis="Lüb",
        ort="Mo",
    )
    LAUT_LÜB_NE = Sammlung(
        trace="Lüb Ne",
        groups="Lautschrift|Lüb Ne",
        kreis="Lüb",
        ort="Ne",
    )
    LAUT_LÜB_NM = Sammlung(
        trace="Lüb Nm",
        groups="Lautschrift|Lüb Nm",
        kreis="Lüb",
        ort="Nm",
    )
    LAUT_LÜB_OB = Sammlung(
        trace="Lüb Ob",
        groups="Lautschrift|Lüb Ob",
        kreis="Lüb",
        ort="Ob",
    )
    LAUT_LÜB_OD = Sammlung(
        trace="Lüb Od",
        groups="Lautschrift|Lüb Od",
        kreis="Lüb",
        ort="Od",
    )
    LAUT_LÜB_OF = Sammlung(
        trace="Lüb Of",
        groups="Lautschrift|Lüb Of",
        kreis="Lüb",
        ort="Of",
    )
    LAUT_LÜB_OM = Sammlung(
        trace="Lüb Om",
        groups="Lautschrift|Lüb Om",
        kreis="Lüb",
        ort="Om",
    )
    LAUT_LÜB_OW = Sammlung(
        trace="Lüb Ow",
        groups="Lautschrift|Lüb Ow",
        kreis="Lüb",
        ort="Ow",
    )
    LAUT_LÜB_PO = Sammlung(
        trace="Lüb Po",
        groups="Lautschrift|Lüb Po",
        kreis="Lüb",
        ort="Po",
    )
    LAUT_LÜB_PS = Sammlung(
        trace="Lüb Ps",
        groups="Lautschrift|Lüb Ps",
        kreis="Lüb",
        ort="Ps",
    )
    LAUT_LÜB_RA = Sammlung(
        trace="Lüb Ra",
        groups="Lautschrift|Lüb Ra",
        kreis="Lüb",
        ort="Ra",
    )
    LAUT_LÜB_SH = Sammlung(
        trace="Lüb Sh",
        groups="Lautschrift|Lüb Sh",
        kreis="Lüb",
        ort="Sh",
    )
    LAUT_LÜB_SI = Sammlung(
        trace="Lüb Si",
        groups="Lautschrift|Lüb Si",
        kreis="Lüb",
        ort="Si",
    )
    LAUT_LÜB_SN = Sammlung(
        trace="Lüb Sn",
        groups="Lautschrift|Lüb Sn",
        kreis="Lüb",
        ort="Sn",
    )
    LAUT_LÜB_ST = Sammlung(
        trace="Lüb St",
        groups="Lautschrift|Lüb St",
        kreis="Lüb",
        ort="St",
    )
    LAUT_LÜB_SU = Sammlung(
        trace="Lüb Su",
        groups="Lautschrift|Lüb Su",
        kreis="Lüb",
        ort="Su",
    )
    LAUT_LÜB_TE = Sammlung(
        trace="Lüb Te",
        groups="Lautschrift|Lüb Te",
        kreis="Lüb",
        ort="Te",
    )
    LAUT_LÜB_TI = Sammlung(
        trace="Lüb Ti",
        groups="Lautschrift|Lüb Ti",
        kreis="Lüb",
        ort="Ti",
    )
    LAUT_LÜB_TO = Sammlung(
        trace="Lüb To",
        groups="Lautschrift|Lüb To",
        kreis="Lüb",
        ort="To",
    )
    LAUT_LÜB_TW = Sammlung(
        trace="Lüb Tw",
        groups="Lautschrift|Lüb Tw",
        kreis="Lüb",
        ort="Tw",
    )
    LAUT_LÜB_VA = Sammlung(
        trace="Lüb Va",
        groups="Lautschrift|Lüb Va",
        kreis="Lüb",
        ort="Va",
    )
    LAUT_LÜB_VE = Sammlung(
        trace="Lüb Ve",
        groups="Lautschrift|Lüb Ve",
        kreis="Lüb",
        ort="Ve",
    )
    LAUT_LÜB_VH = Sammlung(
        trace="Lüb Vh",
        groups="Lautschrift|Lüb Vh",
        kreis="Lüb",
        ort="Vh",
    )
    LAUT_LÜB_WE = Sammlung(
        trace="Lüb We",
        groups="Lautschrift|Lüb We",
        kreis="Lüb",
        ort="We",
    )
    LAUT_LÜB_WH = Sammlung(
        trace="Lüb Wh",
        groups="Lautschrift|Lüb Wh",
        kreis="Lüb",
        ort="Wh",
    )
    LAUT_LÜB_WP = Sammlung(
        trace="Lüb Wp",
        groups="Lautschrift|Lüb Wp",
        kreis="Lüb",
        ort="Wp",
    )
    LAUT_MEL_AM = Sammlung(
        trace="Mel Am",
        groups="Lautschrift|Mel Am",
        kreis="Mel",
        ort="Am",
    )
    LAUT_MEL_BM = Sammlung(
        trace="Mel Bm",
        groups="Lautschrift|Mel Bm",
        kreis="Mel",
        ort="Bm",
    )
    LAUT_MEL_BU = Sammlung(
        trace="Mel Bu",
        groups="Lautschrift|Mel Bu",
        kreis="Mel",
        ort="Bu",
    )
    LAUT_MEL_DD = Sammlung(
        trace="Mel Dd",
        groups="Lautschrift|Mel Dd",
        kreis="Mel",
        ort="Dd",
    )
    LAUT_MEL_DÖ = Sammlung(
        trace="Mel Dö",
        groups="Lautschrift|Mel Dö",
        kreis="Mel",
        ort="Dö",
    )
    LAUT_MEL_DR = Sammlung(
        trace="Mel Dr",
        groups="Lautschrift|Mel Dr",
        kreis="Mel",
        ort="Dr",
    )
    LAUT_MEL_DT = Sammlung(
        trace="Mel Dt",
        groups="Lautschrift|Mel Dt",
        kreis="Mel",
        ort="Dt",
    )
    LAUT_MEL_DÜ = Sammlung(
        trace="Mel Dü",
        groups="Lautschrift|Mel Dü",
        kreis="Mel",
        ort="Dü",
    )
    LAUT_MEL_EB = Sammlung(
        trace="Mel Eb",
        groups="Lautschrift|Mel Eb",
        kreis="Mel",
        ort="Eb",
    )
    LAUT_MEL_FÖ = Sammlung(
        trace="Mel Fö",
        groups="Lautschrift|Mel Fö",
        kreis="Mel",
        ort="Fö",
    )
    LAUT_MEL_GA = Sammlung(
        trace="Mel Ga",
        groups="Lautschrift|Mel Ga",
        kreis="Mel",
        ort="Ga",
    )
    LAUT_MEL_GD = Sammlung(
        trace="Mel Gd",
        groups="Lautschrift|Mel Gd",
        kreis="Mel",
        ort="Gd",
    )
    LAUT_MEL_GE = Sammlung(
        trace="Mel Ge",
        groups="Lautschrift|Mel Ge",
        kreis="Mel",
        ort="Ge",
    )
    LAUT_MEL_HD = Sammlung(
        trace="Mel Hd",
        groups="Lautschrift|Mel Hd",
        kreis="Mel",
        ort="Hd",
    )
    LAUT_MEL_HO = Sammlung(
        trace="Mel Ho",
        groups="Lautschrift|Mel Ho",
        kreis="Mel",
        ort="Ho",
    )
    LAUT_MEL_HU = Sammlung(
        trace="Mel Hu",
        groups="Lautschrift|Mel Hu",
        kreis="Mel",
        ort="Hu",
    )
    LAUT_MEL_KR = Sammlung(
        trace="Mel Kr",
        groups="Lautschrift|Mel Kr",
        kreis="Mel",
        ort="Kr",
    )
    LAUT_MEL_KÜ = Sammlung(
        trace="Mel Kü",
        groups="Lautschrift|Mel Kü",
        kreis="Mel",
        ort="Kü",
    )
    LAUT_MEL_MD = Sammlung(
        trace="Mel Md",
        groups="Lautschrift|Mel Md",
        kreis="Mel",
        ort="Md",
    )
    LAUT_MEL_ME = Sammlung(
        trace="Mel Me",
        groups="Lautschrift|Mel Me",
        kreis="Mel",
        ort="Me",
    )
    LAUT_MEL_NF = Sammlung(
        trace="Mel Nf",
        groups="Lautschrift|Mel Nf",
        kreis="Mel",
        ort="Nf",
    )
    LAUT_MEL_NK = Sammlung(
        trace="Mel Nk",
        groups="Lautschrift|Mel Nk",
        kreis="Mel",
        ort="Nk",
    )
    LAUT_MEL_NS = Sammlung(
        trace="Mel Ns",
        groups="Lautschrift|Mel Ns",
        kreis="Mel",
        ort="Ns",
    )
    LAUT_MEL_OD = Sammlung(
        trace="Mel Od",
        groups="Lautschrift|Mel Od",
        kreis="Mel",
        ort="Od",
    )
    LAUT_MEL_RI = Sammlung(
        trace="Mel Ri",
        groups="Lautschrift|Mel Ri",
        kreis="Mel",
        ort="Ri",
    )
    LAUT_MEL_SA = Sammlung(
        trace="Mel Sa",
        groups="Lautschrift|Mel Sa",
        kreis="Mel",
        ort="Sa",
    )
    LAUT_MEL_SU = Sammlung(
        trace="Mel Su",
        groups="Lautschrift|Mel Su",
        kreis="Mel",
        ort="Su",
    )
    LAUT_MEL_UB = Sammlung(
        trace="Mel Ub",
        groups="Lautschrift|Mel Ub",
        kreis="Mel",
        ort="Ub",
    )
    LAUT_MEL_ÜH = Sammlung(
        trace="Mel Üh",
        groups="Lautschrift|Mel Üh",
        kreis="Mel",
        ort="Üh",
    )
    LAUT_MEL_WD = Sammlung(
        trace="Mel Wd",
        groups="Lautschrift|Mel Wd",
        kreis="Mel",
        ort="Wd",
    )
    LAUT_MEL_WE = Sammlung(
        trace="Mel We",
        groups="Lautschrift|Mel We",
        kreis="Mel",
        ort="We",
    )
    LAUT_MEL_WH = Sammlung(
        trace="Mel Wh",
        groups="Lautschrift|Mel Wh",
        kreis="Mel",
        ort="Wh",
    )
    LAUT_MEL_WT = Sammlung(
        trace="Mel Wt",
        groups="Lautschrift|Mel Wt",
        kreis="Mel",
        ort="Wt",
    )
    LAUT_MEL_WY = Sammlung(
        trace="Mel Wy",
        groups="Lautschrift|Mel Wy",
        kreis="Mel",
        ort="Wy",
    )
    LAUT_MEP_AB = Sammlung(
        trace="Mep Ab",
        groups="Lautschrift|Mep Ab",
        kreis="Mep",
        ort="Ab",
    )
    LAUT_MEP_AD = Sammlung(
        trace="Mep Ad",
        groups="Lautschrift|Mep Ad",
        kreis="Mep",
        ort="Ad",
    )
    LAUT_MEP_AH = Sammlung(
        trace="Mep Ah",
        groups="Lautschrift|Mep Ah",
        kreis="Mep",
        ort="Ah",
    )
    LAUT_MEP_AM = Sammlung(
        trace="Mep Am",
        groups="Lautschrift|Mep Am",
        kreis="Mep",
        ort="Am",
    )
    LAUT_MEP_BH = Sammlung(
        trace="Mep Bh",
        groups="Lautschrift|Mep Bh",
        kreis="Mep",
        ort="Bh",
    )
    LAUT_MEP_BO = Sammlung(
        trace="Mep Bo",
        groups="Lautschrift|Mep Bo",
        kreis="Mep",
        ort="Bo",
    )
    LAUT_MEP_BÜ = Sammlung(
        trace="Mep Bü",
        groups="Lautschrift|Mep Bü",
        kreis="Mep",
        ort="Bü",
    )
    LAUT_MEP_DA = Sammlung(
        trace="Mep Da",
        groups="Lautschrift|Mep Da",
        kreis="Mep",
        ort="Da",
    )
    LAUT_MEP_DK = Sammlung(
        trace="Mep Dk",
        groups="Lautschrift|Mep Dk",
        kreis="Mep",
        ort="Dk",
    )
    LAUT_MEP_DO = Sammlung(
        trace="Mep Do",
        groups="Lautschrift|Mep Do",
        kreis="Mep",
        ort="Do",
    )
    LAUT_MEP_DÖ = Sammlung(
        trace="Mep Dö",
        groups="Lautschrift|Mep Dö",
        kreis="Mep",
        ort="Dö",
    )
    LAUT_MEP_EM = Sammlung(
        trace="Mep Em",
        groups="Lautschrift|Mep Em",
        kreis="Mep",
        ort="Em",
    )
    LAUT_MEP_FU = Sammlung(
        trace="Mep Fu",
        groups="Lautschrift|Mep Fu",
        kreis="Mep",
        ort="Fu",
    )
    LAUT_MEP_GB = Sammlung(
        trace="Mep Gb",
        groups="Lautschrift|Mep Gb",
        kreis="Mep",
        ort="Gb",
    )
    LAUT_MEP_GE = Sammlung(
        trace="Mep Ge",
        groups="Lautschrift|Mep Ge",
        kreis="Mep",
        ort="Ge",
    )
    LAUT_MEP_GF = Sammlung(
        trace="Mep Gf",
        groups="Lautschrift|Mep Gf",
        kreis="Mep",
        ort="Gf",
    )
    LAUT_MEP_GH = Sammlung(
        trace="Mep Gh",
        groups="Lautschrift|Mep Gh",
        kreis="Mep",
        ort="Gh",
    )
    LAUT_MEP_GS = Sammlung(
        trace="Mep Gs",
        groups="Lautschrift|Mep Gs",
        kreis="Mep",
        ort="Gs",
    )
    LAUT_MEP_HA = Sammlung(
        trace="Mep Ha",
        groups="Lautschrift|Mep Ha",
        kreis="Mep",
        ort="Ha",
    )
    LAUT_MEP_HE = Sammlung(
        trace="Mep He",
        groups="Lautschrift|Mep He",
        kreis="Mep",
        ort="He",
    )
    LAUT_MEP_HL = Sammlung(
        trace="Mep Hl",
        groups="Lautschrift|Mep Hl",
        kreis="Mep",
        ort="Hl",
    )
    LAUT_MEP_HM = Sammlung(
        trace="Mep Hm",
        groups="Lautschrift|Mep Hm",
        kreis="Mep",
        ort="Hm",
    )
    LAUT_MEP_HN = Sammlung(
        trace="Mep Hn",
        groups="Lautschrift|Mep Hn",
        kreis="Mep",
        ort="Hn",
    )
    LAUT_MEP_HO = Sammlung(
        trace="Mep Ho",
        groups="Lautschrift|Mep Ho",
        kreis="Mep",
        ort="Ho",
    )
    LAUT_MEP_HS = Sammlung(
        trace="Mep Hs",
        groups="Lautschrift|Mep Hs",
        kreis="Mep",
        ort="Hs",
    )
    LAUT_MEP_HT = Sammlung(
        trace="Mep Ht",
        groups="Lautschrift|Mep Ht",
        kreis="Mep",
        ort="Ht",
    )
    LAUT_MEP_HÜ = Sammlung(
        trace="Mep Hü",
        groups="Lautschrift|Mep Hü",
        kreis="Mep",
        ort="Hü",
    )
    LAUT_MEP_KH = Sammlung(
        trace="Mep Kh",
        groups="Lautschrift|Mep Kh",
        kreis="Mep",
        ort="Kh",
    )
    LAUT_MEP_KS = Sammlung(
        trace="Mep Ks",
        groups="Lautschrift|Mep Ks",
        kreis="Mep",
        ort="Ks",
    )
    LAUT_MEP_LA = Sammlung(
        trace="Mep La",
        groups="Lautschrift|Mep La",
        kreis="Mep",
        ort="La",
    )
    LAUT_MEP_LÄ = Sammlung(
        trace="Mep Lä",
        groups="Lautschrift|Mep Lä",
        kreis="Mep",
        ort="Lä",
    )
    LAUT_MEP_LE = Sammlung(
        trace="Mep Le",
        groups="Lautschrift|Mep Le",
        kreis="Mep",
        ort="Le",
    )
    LAUT_MEP_LG = Sammlung(
        trace="Mep Lg",
        groups="Lautschrift|Mep Lg",
        kreis="Mep",
        ort="Lg",
    )
    LAUT_MEP_LL = Sammlung(
        trace="Mep Ll",
        groups="Lautschrift|Mep Ll",
        kreis="Mep",
        ort="Ll",
    )
    LAUT_MEP_LO = Sammlung(
        trace="Mep Lo",
        groups="Lautschrift|Mep Lo",
        kreis="Mep",
        ort="Lo",
    )
    LAUT_MEP_LT = Sammlung(
        trace="Mep Lt",
        groups="Lautschrift|Mep Lt",
        kreis="Mep",
        ort="Lt",
    )
    LAUT_MEP_MP = Sammlung(
        trace="Mep Mp",
        groups="Lautschrift|Mep Mp",
        kreis="Mep",
        ort="Mp",
    )
    LAUT_MEP_RB = Sammlung(
        trace="Mep Rb",
        groups="Lautschrift|Mep Rb",
        kreis="Mep",
        ort="Rb",
    )
    LAUT_MEP_RM = Sammlung(
        trace="Mep Rm",
        groups="Lautschrift|Mep Rm",
        kreis="Mep",
        ort="Rm",
    )
    LAUT_MEP_RT = Sammlung(
        trace="Mep Rt",
        groups="Lautschrift|Mep Rt",
        kreis="Mep",
        ort="Rt",
    )
    LAUT_MEP_RÜ = Sammlung(
        trace="Mep Rü",
        groups="Lautschrift|Mep Rü",
        kreis="Mep",
        ort="Rü",
    )
    LAUT_MEP_SD = Sammlung(
        trace="Mep Sd",
        groups="Lautschrift|Mep Sd",
        kreis="Mep",
        ort="Sd",
    )
    LAUT_MEP_SF = Sammlung(
        trace="Mep Sf",
        groups="Lautschrift|Mep Sf",
        kreis="Mep",
        ort="Sf",
    )
    LAUT_MEP_SP = Sammlung(
        trace="Mep Sp",
        groups="Lautschrift|Mep Sp",
        kreis="Mep",
        ort="Sp",
    )
    LAUT_MEP_SW = Sammlung(
        trace="Mep Sw",
        groups="Lautschrift|Mep Sw",
        kreis="Mep",
        ort="Sw",
    )
    LAUT_MEP_TE = Sammlung(
        trace="Mep Te",
        groups="Lautschrift|Mep Te",
        kreis="Mep",
        ort="Te",
    )
    LAUT_MEP_TW = Sammlung(
        trace="Mep Tw",
        groups="Lautschrift|Mep Tw",
        kreis="Mep",
        ort="Tw",
    )
    LAUT_MEP_VA = Sammlung(
        trace="Mep Va",
        groups="Lautschrift|Mep Va",
        kreis="Mep",
        ort="Va",
    )
    LAUT_MEP_VE = Sammlung(
        trace="Mep Ve",
        groups="Lautschrift|Mep Ve",
        kreis="Mep",
        ort="Ve",
    )
    LAUT_MEP_VI = Sammlung(
        trace="Mep Vi",
        groups="Lautschrift|Mep Vi",
        kreis="Mep",
        ort="Vi",
    )
    LAUT_MEP_WA = Sammlung(
        trace="Mep Wa",
        groups="Lautschrift|Mep Wa",
        kreis="Mep",
        ort="Wa",
    )
    LAUT_MEP_WE = Sammlung(
        trace="Mep We",
        groups="Lautschrift|Mep We",
        kreis="Mep",
        ort="We",
    )
    LAUT_MEP_WL = Sammlung(
        trace="Mep Wl",
        groups="Lautschrift|Mep Wl",
        kreis="Mep",
        ort="Wl",
    )
    LAUT_MES_AF = Sammlung(
        trace="Mes Af",
        groups="Lautschrift|Mes Af",
        kreis="Mes",
        ort="Af",
    )
    LAUT_MES_AI = Sammlung(
        trace="Mes Ai",
        groups="Lautschrift|Mes Ai",
        kreis="Mes",
        ort="Ai",
    )
    LAUT_MES_BA = Sammlung(
        trace="Mes Ba",
        groups="Lautschrift|Mes Ba",
        kreis="Mes",
        ort="Ba",
    )
    LAUT_MES_BB = Sammlung(
        trace="Mes Bb",
        groups="Lautschrift|Mes Bb",
        kreis="Mes",
        ort="Bb",
    )
    LAUT_MES_BD = Sammlung(
        trace="Mes Bd",
        groups="Lautschrift|Mes Bd",
        kreis="Mes",
        ort="Bd",
    )
    LAUT_MES_BE = Sammlung(
        trace="Mes Be",
        groups="Lautschrift|Mes Be",
        kreis="Mes",
        ort="Be",
    )
    LAUT_MES_BF = Sammlung(
        trace="Mes Bf",
        groups="Lautschrift|Mes Bf",
        kreis="Mes",
        ort="Bf",
    )
    LAUT_MES_BH = Sammlung(
        trace="Mes Bh",
        groups="Lautschrift|Mes Bh",
        kreis="Mes",
        ort="Bh",
    )
    LAUT_MES_BK = Sammlung(
        trace="Mes Bk",
        groups="Lautschrift|Mes Bk",
        kreis="Mes",
        ort="Bk",
    )
    LAUT_MES_BL = Sammlung(
        trace="Mes Bl",
        groups="Lautschrift|Mes Bl",
        kreis="Mes",
        ort="Bl",
    )
    LAUT_MES_BÖ = Sammlung(
        trace="Mes Bö",
        groups="Lautschrift|Mes Bö",
        kreis="Mes",
        ort="Bö",
    )
    LAUT_MES_BR = Sammlung(
        trace="Mes Br",
        groups="Lautschrift|Mes Br",
        kreis="Mes",
        ort="Br",
    )
    LAUT_MES_BS = Sammlung(
        trace="Mes Bs",
        groups="Lautschrift|Mes Bs",
        kreis="Mes",
        ort="Bs",
    )
    LAUT_MES_BÜ = Sammlung(
        trace="Mes Bü",
        groups="Lautschrift|Mes Bü",
        kreis="Mes",
        ort="Bü",
    )
    LAUT_MES_BW = Sammlung(
        trace="Mes Bw",
        groups="Lautschrift|Mes Bw",
        kreis="Mes",
        ort="Bw",
    )
    LAUT_MES_DO = Sammlung(
        trace="Mes Do",
        groups="Lautschrift|Mes Do",
        kreis="Mes",
        ort="Do",
    )
    LAUT_MES_DT = Sammlung(
        trace="Mes Dt",
        groups="Lautschrift|Mes Dt",
        kreis="Mes",
        ort="Dt",
    )
    LAUT_MES_EH = Sammlung(
        trace="Mes Eh",
        groups="Lautschrift|Mes Eh",
        kreis="Mes",
        ort="Eh",
    )
    LAUT_MES_ES = Sammlung(
        trace="Mes Es",
        groups="Lautschrift|Mes Es",
        kreis="Mes",
        ort="Es",
    )
    LAUT_MES_EV = Sammlung(
        trace="Mes Ev",
        groups="Lautschrift|Mes Ev",
        kreis="Mes",
        ort="Ev",
    )
    LAUT_MES_FB = Sammlung(
        trace="Mes Fb",
        groups="Lautschrift|Mes Fb",
        kreis="Mes",
        ort="Fb",
    )
    LAUT_MES_FH = Sammlung(
        trace="Mes Fh",
        groups="Lautschrift|Mes Fh",
        kreis="Mes",
        ort="Fh",
    )
    LAUT_MES_FI = Sammlung(
        trace="Mes Fi",
        groups="Lautschrift|Mes Fi",
        kreis="Mes",
        ort="Fi",
    )
    LAUT_MES_FR = Sammlung(
        trace="Mes Fr",
        groups="Lautschrift|Mes Fr",
        kreis="Mes",
        ort="Fr",
    )
    LAUT_MES_FT = Sammlung(
        trace="Mes Ft",
        groups="Lautschrift|Mes Ft",
        kreis="Mes",
        ort="Ft",
    )
    LAUT_MES_GE = Sammlung(
        trace="Mes Ge",
        groups="Lautschrift|Mes Ge",
        kreis="Mes",
        ort="Ge",
    )
    LAUT_MES_GH = Sammlung(
        trace="Mes Gh",
        groups="Lautschrift|Mes Gh",
        kreis="Mes",
        ort="Gh",
    )
    LAUT_MES_GL = Sammlung(
        trace="Mes Gl",
        groups="Lautschrift|Mes Gl",
        kreis="Mes",
        ort="Gl",
    )
    LAUT_MES_GR = Sammlung(
        trace="Mes Gr",
        groups="Lautschrift|Mes Gr",
        kreis="Mes",
        ort="Gr",
    )
    LAUT_MES_HB = Sammlung(
        trace="Mes Hb",
        groups="Lautschrift|Mes Hb",
        kreis="Mes",
        ort="Hb",
    )
    LAUT_MES_HE = Sammlung(
        trace="Mes He",
        groups="Lautschrift|Mes He",
        kreis="Mes",
        ort="He",
    )
    LAUT_MES_HH = Sammlung(
        trace="Mes Hh",
        groups="Lautschrift|Mes Hh",
        kreis="Mes",
        ort="Hh",
    )
    LAUT_MES_HO = Sammlung(
        trace="Mes Ho",
        groups="Lautschrift|Mes Ho",
        kreis="Mes",
        ort="Ho",
    )
    LAUT_MES_KA = Sammlung(
        trace="Mes Ka",
        groups="Lautschrift|Mes Ka",
        kreis="Mes",
        ort="Ka",
    )
    LAUT_MES_KL = Sammlung(
        trace="Mes Kl",
        groups="Lautschrift|Mes Kl",
        kreis="Mes",
        ort="Kl",
    )
    LAUT_MES_KO = Sammlung(
        trace="Mes Ko",
        groups="Lautschrift|Mes Ko",
        kreis="Mes",
        ort="Ko",
    )
    LAUT_MES_KR = Sammlung(
        trace="Mes Kr",
        groups="Lautschrift|Mes Kr",
        kreis="Mes",
        ort="Kr",
    )
    LAUT_MES_KÜ = Sammlung(
        trace="Mes Kü",
        groups="Lautschrift|Mes Kü",
        kreis="Mes",
        ort="Kü",
    )
    LAUT_MES_LA = Sammlung(
        trace="Mes La",
        groups="Lautschrift|Mes La",
        kreis="Mes",
        ort="La",
    )
    LAUT_MES_LH = Sammlung(
        trace="Mes Lh",
        groups="Lautschrift|Mes Lh",
        kreis="Mes",
        ort="Lh",
    )
    LAUT_MES_ME = Sammlung(
        trace="Mes Me",
        groups="Lautschrift|Mes Me",
        kreis="Mes",
        ort="Me",
    )
    LAUT_MES_MS = Sammlung(
        trace="Mes Ms",
        groups="Lautschrift|Mes Ms",
        kreis="Mes",
        ort="Ms",
    )
    LAUT_MES_NA = Sammlung(
        trace="Mes Na",
        groups="Lautschrift|Mes Na",
        kreis="Mes",
        ort="Na",
    )
    LAUT_MES_NF = Sammlung(
        trace="Mes Nf",
        groups="Lautschrift|Mes Nf",
        kreis="Mes",
        ort="Nf",
    )
    LAUT_MES_NH = Sammlung(
        trace="Mes Nh",
        groups="Lautschrift|Mes Nh",
        kreis="Mes",
        ort="Nh",
    )
    LAUT_MES_NI = Sammlung(
        trace="Mes Ni",
        groups="Lautschrift|Mes Ni",
        kreis="Mes",
        ort="Ni",
    )
    LAUT_MES_NL = Sammlung(
        trace="Mes Nl",
        groups="Lautschrift|Mes Nl",
        kreis="Mes",
        ort="Nl",
    )
    LAUT_MES_NO = Sammlung(
        trace="Mes No",
        groups="Lautschrift|Mes No",
        kreis="Mes",
        ort="No",
    )
    LAUT_MES_NS = Sammlung(
        trace="Mes Ns",
        groups="Lautschrift|Mes Ns",
        kreis="Mes",
        ort="Ns",
    )
    LAUT_MES_NU = Sammlung(
        trace="Mes Nu",
        groups="Lautschrift|Mes Nu",
        kreis="Mes",
        ort="Nu",
    )
    LAUT_MES_ÖD = Sammlung(
        trace="Mes Öd",
        groups="Lautschrift|Mes Öd",
        kreis="Mes",
        ort="Öd",
    )
    LAUT_MES_OH = Sammlung(
        trace="Mes Oh",
        groups="Lautschrift|Mes Oh",
        kreis="Mes",
        ort="Oh",
    )
    LAUT_MES_OK = Sammlung(
        trace="Mes Ok",
        groups="Lautschrift|Mes Ok",
        kreis="Mes",
        ort="Ok",
    )
    LAUT_MES_OS = Sammlung(
        trace="Mes Os",
        groups="Lautschrift|Mes Os",
        kreis="Mes",
        ort="Os",
    )
    LAUT_MES_OT = Sammlung(
        trace="Mes Ot",
        groups="Lautschrift|Mes Ot",
        kreis="Mes",
        ort="Ot",
    )
    LAUT_MES_OW = Sammlung(
        trace="Mes Ow",
        groups="Lautschrift|Mes Ow",
        kreis="Mes",
        ort="Ow",
    )
    LAUT_MES_RA = Sammlung(
        trace="Mes Ra",
        groups="Lautschrift|Mes Ra",
        kreis="Mes",
        ort="Ra",
    )
    LAUT_MES_RB = Sammlung(
        trace="Mes Rb",
        groups="Lautschrift|Mes Rb",
        kreis="Mes",
        ort="Rb",
    )
    LAUT_MES_RE = Sammlung(
        trace="Mes Re",
        groups="Lautschrift|Mes Re",
        kreis="Mes",
        ort="Re",
    )
    LAUT_MES_RH = Sammlung(
        trace="Mes Rh",
        groups="Lautschrift|Mes Rh",
        kreis="Mes",
        ort="Rh",
    )
    LAUT_MES_SC = Sammlung(
        trace="Mes Sc",
        groups="Lautschrift|Mes Sc",
        kreis="Mes",
        ort="Sc",
    )
    LAUT_MES_SD = Sammlung(
        trace="Mes Sd",
        groups="Lautschrift|Mes Sd",
        kreis="Mes",
        ort="Sd",
    )
    LAUT_MES_SH = Sammlung(
        trace="Mes Sh",
        groups="Lautschrift|Mes Sh",
        kreis="Mes",
        ort="Sh",
    )
    LAUT_MES_SM = Sammlung(
        trace="Mes Sm",
        groups="Lautschrift|Mes Sm",
        kreis="Mes",
        ort="Sm",
    )
    LAUT_MES_SR = Sammlung(
        trace="Mes Sr",
        groups="Lautschrift|Mes Sr",
        kreis="Mes",
        ort="Sr",
    )
    LAUT_MES_ST = Sammlung(
        trace="Mes St",
        groups="Lautschrift|Mes St",
        kreis="Mes",
        ort="St",
    )
    LAUT_MES_VE = Sammlung(
        trace="Mes Ve",
        groups="Lautschrift|Mes Ve",
        kreis="Mes",
        ort="Ve",
    )
    LAUT_MES_WA = Sammlung(
        trace="Mes Wa",
        groups="Lautschrift|Mes Wa",
        kreis="Mes",
        ort="Wa",
    )
    LAUT_MES_WB = Sammlung(
        trace="Mes Wb",
        groups="Lautschrift|Mes Wb",
        kreis="Mes",
        ort="Wb",
    )
    LAUT_MES_WE = Sammlung(
        trace="Mes We",
        groups="Lautschrift|Mes We",
        kreis="Mes",
        ort="We",
    )
    LAUT_MES_WF = Sammlung(
        trace="Mes Wf",
        groups="Lautschrift|Mes Wf",
        kreis="Mes",
        ort="Wf",
    )
    LAUT_MES_WH = Sammlung(
        trace="Mes Wh",
        groups="Lautschrift|Mes Wh",
        kreis="Mes",
        ort="Wh",
    )
    LAUT_MES_WO = Sammlung(
        trace="Mes Wo",
        groups="Lautschrift|Mes Wo",
        kreis="Mes",
        ort="Wo",
    )
    LAUT_MES_WP = Sammlung(
        trace="Mes Wp",
        groups="Lautschrift|Mes Wp",
        kreis="Mes",
        ort="Wp",
    )
    LAUT_MES_WS = Sammlung(
        trace="Mes Ws",
        groups="Lautschrift|Mes Ws",
        kreis="Mes",
        ort="Ws",
    )
    LAUT_MIN_BA = Sammlung(
        trace="Min Ba",
        groups="Lautschrift|Min Ba",
        kreis="Min",
        ort="Ba",
    )
    LAUT_MIN_BH = Sammlung(
        trace="Min Bh",
        groups="Lautschrift|Min Bh",
        kreis="Min",
        ort="Bh",
    )
    LAUT_MIN_BI = Sammlung(
        trace="Min Bi",
        groups="Lautschrift|Min Bi",
        kreis="Min",
        ort="Bi",
    )
    LAUT_MIN_BK = Sammlung(
        trace="Min Bk",
        groups="Lautschrift|Min Bk",
        kreis="Min",
        ort="Bk",
    )
    LAUT_MIN_BN = Sammlung(
        trace="Min Bn",
        groups="Lautschrift|Min Bn",
        kreis="Min",
        ort="Bn",
    )
    LAUT_MIN_BÖ = Sammlung(
        trace="Min Bö",
        groups="Lautschrift|Min Bö",
        kreis="Min",
        ort="Bö",
    )
    LAUT_MIN_DA = Sammlung(
        trace="Min Da",
        groups="Lautschrift|Min Da",
        kreis="Min",
        ort="Da",
    )
    LAUT_MIN_DE = Sammlung(
        trace="Min De",
        groups="Lautschrift|Min De",
        kreis="Min",
        ort="De",
    )
    LAUT_MIN_DÖ = Sammlung(
        trace="Min Dö",
        groups="Lautschrift|Min Dö",
        kreis="Min",
        ort="Dö",
    )
    LAUT_MIN_DÜ = Sammlung(
        trace="Min Dü",
        groups="Lautschrift|Min Dü",
        kreis="Min",
        ort="Dü",
    )
    LAUT_MIN_EH = Sammlung(
        trace="Min Eh",
        groups="Lautschrift|Min Eh",
        kreis="Min",
        ort="Eh",
    )
    LAUT_MIN_EI = Sammlung(
        trace="Min Ei",
        groups="Lautschrift|Min Ei",
        kreis="Min",
        ort="Ei",
    )
    LAUT_MIN_EL = Sammlung(
        trace="Min El",
        groups="Lautschrift|Min El",
        kreis="Min",
        ort="El",
    )
    LAUT_MIN_EN = Sammlung(
        trace="Min En",
        groups="Lautschrift|Min En",
        kreis="Min",
        ort="En",
    )
    LAUT_MIN_FR = Sammlung(
        trace="Min Fr",
        groups="Lautschrift|Min Fr",
        kreis="Min",
        ort="Fr",
    )
    LAUT_MIN_FW = Sammlung(
        trace="Min Fw",
        groups="Lautschrift|Min Fw",
        kreis="Min",
        ort="Fw",
    )
    LAUT_MIN_GO = Sammlung(
        trace="Min Go",
        groups="Lautschrift|Min Go",
        kreis="Min",
        ort="Go",
    )
    LAUT_MIN_GR = Sammlung(
        trace="Min Gr",
        groups="Lautschrift|Min Gr",
        kreis="Min",
        ort="Gr",
    )
    LAUT_MIN_HA = Sammlung(
        trace="Min Ha",
        groups="Lautschrift|Min Ha",
        kreis="Min",
        ort="Ha",
    )
    LAUT_MIN_HÄ = Sammlung(
        trace="Min Hä",
        groups="Lautschrift|Min Hä",
        kreis="Min",
        ort="Hä",
    )
    LAUT_MIN_HB = Sammlung(
        trace="Min Hb",
        groups="Lautschrift|Min Hb",
        kreis="Min",
        ort="Hb",
    )
    LAUT_MIN_HD = Sammlung(
        trace="Min Hd",
        groups="Lautschrift|Min Hd",
        kreis="Min",
        ort="Hd",
    )
    LAUT_MIN_HE = Sammlung(
        trace="Min He",
        groups="Lautschrift|Min He",
        kreis="Min",
        ort="He",
    )
    LAUT_MIN_HH = Sammlung(
        trace="Min Hh",
        groups="Lautschrift|Min Hh",
        kreis="Min",
        ort="Hh",
    )
    LAUT_MIN_HI = Sammlung(
        trace="Min Hi",
        groups="Lautschrift|Min Hi",
        kreis="Min",
        ort="Hi",
    )
    LAUT_MIN_HM = Sammlung(
        trace="Min Hm",
        groups="Lautschrift|Min Hm",
        kreis="Min",
        ort="Hm",
    )
    LAUT_MIN_HO = Sammlung(
        trace="Min Ho",
        groups="Lautschrift|Min Ho",
        kreis="Min",
        ort="Ho",
    )
    LAUT_MIN_HS = Sammlung(
        trace="Min Hs",
        groups="Lautschrift|Min Hs",
        kreis="Min",
        ort="Hs",
    )
    LAUT_MIN_HZ = Sammlung(
        trace="Min Hz",
        groups="Lautschrift|Min Hz",
        kreis="Min",
        ort="Hz",
    )
    LAUT_MIN_IH = Sammlung(
        trace="Min Ih",
        groups="Lautschrift|Min Ih",
        kreis="Min",
        ort="Ih",
    )
    LAUT_MIN_IL = Sammlung(
        trace="Min Il",
        groups="Lautschrift|Min Il",
        kreis="Min",
        ort="Il",
    )
    LAUT_MIN_IS = Sammlung(
        trace="Min Is",
        groups="Lautschrift|Min Is",
        kreis="Min",
        ort="Is",
    )
    LAUT_MIN_JÖ = Sammlung(
        trace="Min Jö",
        groups="Lautschrift|Min Jö",
        kreis="Min",
        ort="Jö",
    )
    LAUT_MIN_KB = Sammlung(
        trace="Min Kb",
        groups="Lautschrift|Min Kb",
        kreis="Min",
        ort="Kb",
    )
    LAUT_MIN_KH = Sammlung(
        trace="Min Kh",
        groups="Lautschrift|Min Kh",
        kreis="Min",
        ort="Kh",
    )
    LAUT_MIN_KO = Sammlung(
        trace="Min Ko",
        groups="Lautschrift|Min Ko",
        kreis="Min",
        ort="Ko",
    )
    LAUT_MIN_LA = Sammlung(
        trace="Min La",
        groups="Lautschrift|Min La",
        kreis="Min",
        ort="La",
    )
    LAUT_MIN_LB = Sammlung(
        trace="Min Lb",
        groups="Lautschrift|Min Lb",
        kreis="Min",
        ort="Lb",
    )
    LAUT_MIN_LF = Sammlung(
        trace="Min Lf",
        groups="Lautschrift|Min Lf",
        kreis="Min",
        ort="Lf",
    )
    LAUT_MIN_LO = Sammlung(
        trace="Min Lo",
        groups="Lautschrift|Min Lo",
        kreis="Min",
        ort="Lo",
    )
    LAUT_MIN_MA = Sammlung(
        trace="Min Ma",
        groups="Lautschrift|Min Ma",
        kreis="Min",
        ort="Ma",
    )
    LAUT_MIN_MB = Sammlung(
        trace="Min Mb",
        groups="Lautschrift|Min Mb",
        kreis="Min",
        ort="Mb",
    )
    LAUT_MIN_ME = Sammlung(
        trace="Min Me",
        groups="Lautschrift|Min Me",
        kreis="Min",
        ort="Me",
    )
    LAUT_MIN_MI = Sammlung(
        trace="Min Mi",
        groups="Lautschrift|Min Mi",
        kreis="Min",
        ort="Mi",
    )
    LAUT_MIN_ML = Sammlung(
        trace="Min Ml",
        groups="Lautschrift|Min Ml",
        kreis="Min",
        ort="Ml",
    )
    LAUT_MIN_MO = Sammlung(
        trace="Min Mo",
        groups="Lautschrift|Min Mo",
        kreis="Min",
        ort="Mo",
    )
    LAUT_MIN_MW = Sammlung(
        trace="Min Mw",
        groups="Lautschrift|Min Mw",
        kreis="Min",
        ort="Mw",
    )
    LAUT_MIN_NA = Sammlung(
        trace="Min Na",
        groups="Lautschrift|Min Na",
        kreis="Min",
        ort="Na",
    )
    LAUT_MIN_NB = Sammlung(
        trace="Min Nb",
        groups="Lautschrift|Min Nb",
        kreis="Min",
        ort="Nb",
    )
    LAUT_MIN_NE = Sammlung(
        trace="Min Ne",
        groups="Lautschrift|Min Ne",
        kreis="Min",
        ort="Ne",
    )
    LAUT_MIN_NH = Sammlung(
        trace="Min Nh",
        groups="Lautschrift|Min Nh",
        kreis="Min",
        ort="Nh",
    )
    LAUT_MIN_NK = Sammlung(
        trace="Min Nk",
        groups="Lautschrift|Min Nk",
        kreis="Min",
        ort="Nk",
    )
    LAUT_MIN_NS = Sammlung(
        trace="Min Ns",
        groups="Lautschrift|Min Ns",
        kreis="Min",
        ort="Ns",
    )
    LAUT_MIN_OB = Sammlung(
        trace="Min Ob",
        groups="Lautschrift|Min Ob",
        kreis="Min",
        ort="Ob",
    )
    LAUT_MIN_ÖH = Sammlung(
        trace="Min Öh",
        groups="Lautschrift|Min Öh",
        kreis="Min",
        ort="Öh",
    )
    LAUT_MIN_OL = Sammlung(
        trace="Min Ol",
        groups="Lautschrift|Min Ol",
        kreis="Min",
        ort="Ol",
    )
    LAUT_MIN_OS = Sammlung(
        trace="Min Os",
        groups="Lautschrift|Min Os",
        kreis="Min",
        ort="Os",
    )
    LAUT_MIN_PÄ = Sammlung(
        trace="Min Pä",
        groups="Lautschrift|Min Pä",
        kreis="Min",
        ort="Pä",
    )
    LAUT_MIN_PH = Sammlung(
        trace="Min Ph",
        groups="Lautschrift|Min Ph",
        kreis="Min",
        ort="Ph",
    )
    LAUT_MIN_QU = Sammlung(
        trace="Min Qu",
        groups="Lautschrift|Min Qu",
        kreis="Min",
        ort="Qu",
    )
    LAUT_MIN_RD = Sammlung(
        trace="Min Rd",
        groups="Lautschrift|Min Rd",
        kreis="Min",
        ort="Rd",
    )
    LAUT_MIN_RE = Sammlung(
        trace="Min Re",
        groups="Lautschrift|Min Re",
        kreis="Min",
        ort="Re",
    )
    LAUT_MIN_RH = Sammlung(
        trace="Min Rh",
        groups="Lautschrift|Min Rh",
        kreis="Min",
        ort="Rh",
    )
    LAUT_MIN_RO = Sammlung(
        trace="Min Ro",
        groups="Lautschrift|Min Ro",
        kreis="Min",
        ort="Ro",
    )
    LAUT_MIN_SB = Sammlung(
        trace="Min Sb",
        groups="Lautschrift|Min Sb",
        kreis="Min",
        ort="Sb",
    )
    LAUT_MIN_SF = Sammlung(
        trace="Min Sf",
        groups="Lautschrift|Min Sf",
        kreis="Min",
        ort="Sf",
    )
    LAUT_MIN_SH = Sammlung(
        trace="Min Sh",
        groups="Lautschrift|Min Sh",
        kreis="Min",
        ort="Sh",
    )
    LAUT_MIN_ST = Sammlung(
        trace="Min St",
        groups="Lautschrift|Min St",
        kreis="Min",
        ort="St",
    )
    LAUT_MIN_TO = Sammlung(
        trace="Min To",
        groups="Lautschrift|Min To",
        kreis="Min",
        ort="To",
    )
    LAUT_MIN_UF = Sammlung(
        trace="Min Uf",
        groups="Lautschrift|Min Uf",
        kreis="Min",
        ort="Uf",
    )
    LAUT_MIN_UL = Sammlung(
        trace="Min Ul",
        groups="Lautschrift|Min Ul",
        kreis="Min",
        ort="Ul",
    )
    LAUT_MIN_VE = Sammlung(
        trace="Min Ve",
        groups="Lautschrift|Min Ve",
        kreis="Min",
        ort="Ve",
    )
    LAUT_MIN_VH = Sammlung(
        trace="Min Vh",
        groups="Lautschrift|Min Vh",
        kreis="Min",
        ort="Vh",
    )
    LAUT_MIN_VO = Sammlung(
        trace="Min Vo",
        groups="Lautschrift|Min Vo",
        kreis="Min",
        ort="Vo",
    )
    LAUT_MIN_WE = Sammlung(
        trace="Min We",
        groups="Lautschrift|Min We",
        kreis="Min",
        ort="We",
    )
    LAUT_MIN_WG = Sammlung(
        trace="Min Wg",
        groups="Lautschrift|Min Wg",
        kreis="Min",
        ort="Wg",
    )
    LAUT_MIN_WH = Sammlung(
        trace="Min Wh",
        groups="Lautschrift|Min Wh",
        kreis="Min",
        ort="Wh",
    )
    LAUT_MIN_WK = Sammlung(
        trace="Min Wk",
        groups="Lautschrift|Min Wk",
        kreis="Min",
        ort="Wk",
    )
    LAUT_MIN_WL = Sammlung(
        trace="Min Wl",
        groups="Lautschrift|Min Wl",
        kreis="Min",
        ort="Wl",
    )
    LAUT_MIN_WÖ = Sammlung(
        trace="Min Wö",
        groups="Lautschrift|Min Wö",
        kreis="Min",
        ort="Wö",
    )
    LAUT_MIN_WT = Sammlung(
        trace="Min Wt",
        groups="Lautschrift|Min Wt",
        kreis="Min",
        ort="Wt",
    )
    LAUT_MIN_WU = Sammlung(
        trace="Min Wu",
        groups="Lautschrift|Min Wu",
        kreis="Min",
        ort="Wu",
    )
    LAUT_MÜN_AB = Sammlung(
        trace="Mün Ab",
        groups="Lautschrift|Mün Ab",
        kreis="Mün",
        ort="Ab",
    )
    LAUT_MÜN_AD = Sammlung(
        trace="Mün Ad",
        groups="Lautschrift|Mün Ad",
        kreis="Mün",
        ort="Ad",
    )
    LAUT_MÜN_AK = Sammlung(
        trace="Mün Ak",
        groups="Lautschrift|Mün Ak",
        kreis="Mün",
        ort="Ak",
    )
    LAUT_MÜN_AL = Sammlung(
        trace="Mün Al",
        groups="Lautschrift|Mün Al",
        kreis="Mün",
        ort="Al",
    )
    LAUT_MÜN_AM = Sammlung(
        trace="Mün Am",
        groups="Lautschrift|Mün Am",
        kreis="Mün",
        ort="Am",
    )
    LAUT_MÜN_AN = Sammlung(
        trace="Mün An",
        groups="Lautschrift|Mün An",
        kreis="Mün",
        ort="An",
    )
    LAUT_MÜN_AP = Sammlung(
        trace="Mün Ap",
        groups="Lautschrift|Mün Ap",
        kreis="Mün",
        ort="Ap",
    )
    LAUT_MÜN_BB = Sammlung(
        trace="Mün Bb",
        groups="Lautschrift|Mün Bb",
        kreis="Mün",
        ort="Bb",
    )
    LAUT_MÜN_BO = Sammlung(
        trace="Mün Bo",
        groups="Lautschrift|Mün Bo",
        kreis="Mün",
        ort="Bo",
    )
    LAUT_MÜN_BR = Sammlung(
        trace="Mün Br",
        groups="Lautschrift|Mün Br",
        kreis="Mün",
        ort="Br",
    )
    LAUT_MÜN_BS = Sammlung(
        trace="Mün Bs",
        groups="Lautschrift|Mün Bs",
        kreis="Mün",
        ort="Bs",
    )
    LAUT_MÜN_DB = Sammlung(
        trace="Mün Db",
        groups="Lautschrift|Mün Db",
        kreis="Mün",
        ort="Db",
    )
    LAUT_MÜN_GB = Sammlung(
        trace="Mün Gb",
        groups="Lautschrift|Mün Gb",
        kreis="Mün",
        ort="Gb",
    )
    LAUT_MÜN_GE = Sammlung(
        trace="Mün Ge",
        groups="Lautschrift|Mün Ge",
        kreis="Mün",
        ort="Ge",
    )
    LAUT_MÜN_GI = Sammlung(
        trace="Mün Gi",
        groups="Lautschrift|Mün Gi",
        kreis="Mün",
        ort="Gi",
    )
    LAUT_MÜN_GR = Sammlung(
        trace="Mün Gr",
        groups="Lautschrift|Mün Gr",
        kreis="Mün",
        ort="Gr",
    )
    LAUT_MÜN_GS = Sammlung(
        trace="Mün Gs",
        groups="Lautschrift|Mün Gs",
        kreis="Mün",
        ort="Gs",
    )
    LAUT_MÜN_GU = Sammlung(
        trace="Mün Gu",
        groups="Lautschrift|Mün Gu",
        kreis="Mün",
        ort="Gu",
    )
    LAUT_MÜN_HA = Sammlung(
        trace="Mün Ha",
        groups="Lautschrift|Mün Ha",
        kreis="Mün",
        ort="Ha",
    )
    LAUT_MÜN_HB = Sammlung(
        trace="Mün Hb",
        groups="Lautschrift|Mün Hb",
        kreis="Mün",
        ort="Hb",
    )
    LAUT_MÜN_HD = Sammlung(
        trace="Mün Hd",
        groups="Lautschrift|Mün Hd",
        kreis="Mün",
        ort="Hd",
    )
    LAUT_MÜN_HI = Sammlung(
        trace="Mün Hi",
        groups="Lautschrift|Mün Hi",
        kreis="Mün",
        ort="Hi",
    )
    LAUT_MÜN_HO = Sammlung(
        trace="Mün Ho",
        groups="Lautschrift|Mün Ho",
        kreis="Mün",
        ort="Ho",
    )
    LAUT_MÜN_HP = Sammlung(
        trace="Mün Hp",
        groups="Lautschrift|Mün Hp",
        kreis="Mün",
        ort="Hp",
    )
    LAUT_MÜN_KH = Sammlung(
        trace="Mün Kh",
        groups="Lautschrift|Mün Kh",
        kreis="Mün",
        ort="Kh",
    )
    LAUT_MÜN_KÖ = Sammlung(
        trace="Mün Kö",
        groups="Lautschrift|Mün Kö",
        kreis="Mün",
        ort="Kö",
    )
    LAUT_MÜN_KW = Sammlung(
        trace="Mün Kw",
        groups="Lautschrift|Mün Kw",
        kreis="Mün",
        ort="Kw",
    )
    LAUT_MÜN_MB = Sammlung(
        trace="Mün Mb",
        groups="Lautschrift|Mün Mb",
        kreis="Mün",
        ort="Mb",
    )
    LAUT_MÜN_MS = Sammlung(
        trace="Mün Ms",
        groups="Lautschrift|Mün Ms",
        kreis="Mün",
        ort="Ms",
    )
    LAUT_MÜN_MÜ = Sammlung(
        trace="Mün Mü",
        groups="Lautschrift|Mün Mü",
        kreis="Mün",
        ort="Mü",
    )
    LAUT_MÜN_MZ = Sammlung(
        trace="Mün Mz",
        groups="Lautschrift|Mün Mz",
        kreis="Mün",
        ort="Mz",
    )
    LAUT_MÜN_NB = Sammlung(
        trace="Mün Nb",
        groups="Lautschrift|Mün Nb",
        kreis="Mün",
        ort="Nb",
    )
    LAUT_MÜN_NO = Sammlung(
        trace="Mün No",
        groups="Lautschrift|Mün No",
        kreis="Mün",
        ort="No",
    )
    LAUT_MÜN_RO = Sammlung(
        trace="Mün Ro",
        groups="Lautschrift|Mün Ro",
        kreis="Mün",
        ort="Ro",
    )
    LAUT_MÜN_RR = Sammlung(
        trace="Mün Rr",
        groups="Lautschrift|Mün Rr",
        kreis="Mün",
        ort="Rr",
    )
    LAUT_MÜN_SB = Sammlung(
        trace="Mün Sb",
        groups="Lautschrift|Mün Sb",
        kreis="Mün",
        ort="Sb",
    )
    LAUT_MÜN_SD = Sammlung(
        trace="Mün Sd",
        groups="Lautschrift|Mün Sd",
        kreis="Mün",
        ort="Sd",
    )
    LAUT_MÜN_SH = Sammlung(
        trace="Mün Sh",
        groups="Lautschrift|Mün Sh",
        kreis="Mün",
        ort="Sh",
    )
    LAUT_MÜN_SP = Sammlung(
        trace="Mün Sp",
        groups="Lautschrift|Mün Sp",
        kreis="Mün",
        ort="Sp",
    )
    LAUT_MÜN_TE = Sammlung(
        trace="Mün Te",
        groups="Lautschrift|Mün Te",
        kreis="Mün",
        ort="Te",
    )
    LAUT_MÜN_WB = Sammlung(
        trace="Mün Wb",
        groups="Lautschrift|Mün Wb",
        kreis="Mün",
        ort="Wb",
    )
    LAUT_MÜN_WL = Sammlung(
        trace="Mün Wl",
        groups="Lautschrift|Mün Wl",
        kreis="Mün",
        ort="Wl",
    )
    LAUT_MÜN_WO = Sammlung(
        trace="Mün Wo",
        groups="Lautschrift|Mün Wo",
        kreis="Mün",
        ort="Wo",
    )
    LAUT_NIE_AM = Sammlung(
        trace="Nie Am",
        groups="Lautschrift|Nie Am",
        kreis="Nie",
        ort="Am",
    )
    LAUT_NIE_BH = Sammlung(
        trace="Nie Bh",
        groups="Lautschrift|Nie Bh",
        kreis="Nie",
        ort="Bh",
    )
    LAUT_NIE_BO = Sammlung(
        trace="Nie Bo",
        groups="Lautschrift|Nie Bo",
        kreis="Nie",
        ort="Bo",
    )
    LAUT_NIE_BR = Sammlung(
        trace="Nie Br",
        groups="Lautschrift|Nie Br",
        kreis="Nie",
        ort="Br",
    )
    LAUT_NIE_DH = Sammlung(
        trace="Nie Dh",
        groups="Lautschrift|Nie Dh",
        kreis="Nie",
        ort="Dh",
    )
    LAUT_NIE_DI = Sammlung(
        trace="Nie Di",
        groups="Lautschrift|Nie Di",
        kreis="Nie",
        ort="Di",
    )
    LAUT_NIE_DL = Sammlung(
        trace="Nie Dl",
        groups="Lautschrift|Nie Dl",
        kreis="Nie",
        ort="Dl",
    )
    LAUT_NIE_DT = Sammlung(
        trace="Nie Dt",
        groups="Lautschrift|Nie Dt",
        kreis="Nie",
        ort="Dt",
    )
    LAUT_NIE_ES = Sammlung(
        trace="Nie Es",
        groups="Lautschrift|Nie Es",
        kreis="Nie",
        ort="Es",
    )
    LAUT_NIE_GV = Sammlung(
        trace="Nie Gv",
        groups="Lautschrift|Nie Gv",
        kreis="Nie",
        ort="Gv",
    )
    LAUT_NIE_HH = Sammlung(
        trace="Nie Hh",
        groups="Lautschrift|Nie Hh",
        kreis="Nie",
        ort="Hh",
    )
    LAUT_NIE_HI = Sammlung(
        trace="Nie Hi",
        groups="Lautschrift|Nie Hi",
        kreis="Nie",
        ort="Hi",
    )
    LAUT_NIE_HO = Sammlung(
        trace="Nie Ho",
        groups="Lautschrift|Nie Ho",
        kreis="Nie",
        ort="Ho",
    )
    LAUT_NIE_HÖ = Sammlung(
        trace="Nie Hö",
        groups="Lautschrift|Nie Hö",
        kreis="Nie",
        ort="Hö",
    )
    LAUT_NIE_HS = Sammlung(
        trace="Nie Hs",
        groups="Lautschrift|Nie Hs",
        kreis="Nie",
        ort="Hs",
    )
    LAUT_NIE_HT = Sammlung(
        trace="Nie Ht",
        groups="Lautschrift|Nie Ht",
        kreis="Nie",
        ort="Ht",
    )
    LAUT_NIE_HU = Sammlung(
        trace="Nie Hu",
        groups="Lautschrift|Nie Hu",
        kreis="Nie",
        ort="Hu",
    )
    LAUT_NIE_JH = Sammlung(
        trace="Nie Jh",
        groups="Lautschrift|Nie Jh",
        kreis="Nie",
        ort="Jh",
    )
    LAUT_NIE_LA = Sammlung(
        trace="Nie La",
        groups="Lautschrift|Nie La",
        kreis="Nie",
        ort="La",
    )
    LAUT_NIE_LH = Sammlung(
        trace="Nie Lh",
        groups="Lautschrift|Nie Lh",
        kreis="Nie",
        ort="Lh",
    )
    LAUT_NIE_LO = Sammlung(
        trace="Nie Lo",
        groups="Lautschrift|Nie Lo",
        kreis="Nie",
        ort="Lo",
    )
    LAUT_NIE_MH = Sammlung(
        trace="Nie Mh",
        groups="Lautschrift|Nie Mh",
        kreis="Nie",
        ort="Mh",
    )
    LAUT_NIE_MÜ = Sammlung(
        trace="Nie Mü",
        groups="Lautschrift|Nie Mü",
        kreis="Nie",
        ort="Mü",
    )
    LAUT_NIE_ND = Sammlung(
        trace="Nie Nd",
        groups="Lautschrift|Nie Nd",
        kreis="Nie",
        ort="Nd",
    )
    LAUT_NIE_NO = Sammlung(
        trace="Nie No",
        groups="Lautschrift|Nie No",
        kreis="Nie",
        ort="No",
    )
    LAUT_NIE_SA = Sammlung(
        trace="Nie Sa",
        groups="Lautschrift|Nie Sa",
        kreis="Nie",
        ort="Sa",
    )
    LAUT_NIE_SH = Sammlung(
        trace="Nie Sh",
        groups="Lautschrift|Nie Sh",
        kreis="Nie",
        ort="Sh",
    )
    LAUT_NIE_ST = Sammlung(
        trace="Nie St",
        groups="Lautschrift|Nie St",
        kreis="Nie",
        ort="St",
    )
    LAUT_NIE_UC = Sammlung(
        trace="Nie Uc",
        groups="Lautschrift|Nie Uc",
        kreis="Nie",
        ort="Uc",
    )
    LAUT_NIE_WA = Sammlung(
        trace="Nie Wa",
        groups="Lautschrift|Nie Wa",
        kreis="Nie",
        ort="Wa",
    )
    LAUT_NIE_WF = Sammlung(
        trace="Nie Wf",
        groups="Lautschrift|Nie Wf",
        kreis="Nie",
        ort="Wf",
    )
    LAUT_NIE_WH = Sammlung(
        trace="Nie Wh",
        groups="Lautschrift|Nie Wh",
        kreis="Nie",
        ort="Wh",
    )
    LAUT_NIE_WI = Sammlung(
        trace="Nie Wi",
        groups="Lautschrift|Nie Wi",
        kreis="Nie",
        ort="Wi",
    )
    LAUT_OLP_AB = Sammlung(
        trace="Olp Ab",
        groups="Lautschrift|Olp Ab",
        kreis="Olp",
        ort="Ab",
    )
    LAUT_OLP_AH = Sammlung(
        trace="Olp Ah",
        groups="Lautschrift|Olp Ah",
        kreis="Olp",
        ort="Ah",
    )
    LAUT_OLP_AK = Sammlung(
        trace="Olp Ak",
        groups="Lautschrift|Olp Ak",
        kreis="Olp",
        ort="Ak",
    )
    LAUT_OLP_AT = Sammlung(
        trace="Olp At",
        groups="Lautschrift|Olp At",
        kreis="Olp",
        ort="At",
    )
    LAUT_OLP_BB = Sammlung(
        trace="Olp Bb",
        groups="Lautschrift|Olp Bb",
        kreis="Olp",
        ort="Bb",
    )
    LAUT_OLP_BE = Sammlung(
        trace="Olp Be",
        groups="Lautschrift|Olp Be",
        kreis="Olp",
        ort="Be",
    )
    LAUT_OLP_BH = Sammlung(
        trace="Olp Bh",
        groups="Lautschrift|Olp Bh",
        kreis="Olp",
        ort="Bh",
    )
    LAUT_OLP_BL = Sammlung(
        trace="Olp Bl",
        groups="Lautschrift|Olp Bl",
        kreis="Olp",
        ort="Bl",
    )
    LAUT_OLP_BS = Sammlung(
        trace="Olp Bs",
        groups="Lautschrift|Olp Bs",
        kreis="Olp",
        ort="Bs",
    )
    LAUT_OLP_BÜ = Sammlung(
        trace="Olp Bü",
        groups="Lautschrift|Olp Bü",
        kreis="Olp",
        ort="Bü",
    )
    LAUT_OLP_DA = Sammlung(
        trace="Olp Da",
        groups="Lautschrift|Olp Da",
        kreis="Olp",
        ort="Da",
    )
    LAUT_OLP_DH = Sammlung(
        trace="Olp Dh",
        groups="Lautschrift|Olp Dh",
        kreis="Olp",
        ort="Dh",
    )
    LAUT_OLP_DÜ = Sammlung(
        trace="Olp Dü",
        groups="Lautschrift|Olp Dü",
        kreis="Olp",
        ort="Dü",
    )
    LAUT_OLP_EB = Sammlung(
        trace="Olp Eb",
        groups="Lautschrift|Olp Eb",
        kreis="Olp",
        ort="Eb",
    )
    LAUT_OLP_EH = Sammlung(
        trace="Olp Eh",
        groups="Lautschrift|Olp Eh",
        kreis="Olp",
        ort="Eh",
    )
    LAUT_OLP_EL = Sammlung(
        trace="Olp El",
        groups="Lautschrift|Olp El",
        kreis="Olp",
        ort="El",
    )
    LAUT_OLP_EN = Sammlung(
        trace="Olp En",
        groups="Lautschrift|Olp En",
        kreis="Olp",
        ort="En",
    )
    LAUT_OLP_FÖ = Sammlung(
        trace="Olp Fö",
        groups="Lautschrift|Olp Fö",
        kreis="Olp",
        ort="Fö",
    )
    LAUT_OLP_GB = Sammlung(
        trace="Olp Gb",
        groups="Lautschrift|Olp Gb",
        kreis="Olp",
        ort="Gb",
    )
    LAUT_OLP_GE = Sammlung(
        trace="Olp Ge",
        groups="Lautschrift|Olp Ge",
        kreis="Olp",
        ort="Ge",
    )
    LAUT_OLP_GI = Sammlung(
        trace="Olp Gi",
        groups="Lautschrift|Olp Gi",
        kreis="Olp",
        ort="Gi",
    )
    LAUT_OLP_HA = Sammlung(
        trace="Olp Ha",
        groups="Lautschrift|Olp Ha",
        kreis="Olp",
        ort="Ha",
    )
    LAUT_OLP_HB = Sammlung(
        trace="Olp Hb",
        groups="Lautschrift|Olp Hb",
        kreis="Olp",
        ort="Hb",
    )
    LAUT_OLP_HE = Sammlung(
        trace="Olp He",
        groups="Lautschrift|Olp He",
        kreis="Olp",
        ort="He",
    )
    LAUT_OLP_HG = Sammlung(
        trace="Olp Hg",
        groups="Lautschrift|Olp Hg",
        kreis="Olp",
        ort="Hg",
    )
    LAUT_OLP_HI = Sammlung(
        trace="Olp Hi",
        groups="Lautschrift|Olp Hi",
        kreis="Olp",
        ort="Hi",
    )
    LAUT_OLP_HO = Sammlung(
        trace="Olp Ho",
        groups="Lautschrift|Olp Ho",
        kreis="Olp",
        ort="Ho",
    )
    LAUT_OLP_HP = Sammlung(
        trace="Olp Hp",
        groups="Lautschrift|Olp Hp",
        kreis="Olp",
        ort="Hp",
    )
    LAUT_OLP_HS = Sammlung(
        trace="Olp Hs",
        groups="Lautschrift|Olp Hs",
        kreis="Olp",
        ort="Hs",
    )
    LAUT_OLP_HÜ = Sammlung(
        trace="Olp Hü",
        groups="Lautschrift|Olp Hü",
        kreis="Olp",
        ort="Hü",
    )
    LAUT_OLP_KH = Sammlung(
        trace="Olp Kh",
        groups="Lautschrift|Olp Kh",
        kreis="Olp",
        ort="Kh",
    )
    LAUT_OLP_KV = Sammlung(
        trace="Olp Kv",
        groups="Lautschrift|Olp Kv",
        kreis="Olp",
        ort="Kv",
    )
    LAUT_OLP_LA = Sammlung(
        trace="Olp La",
        groups="Lautschrift|Olp La",
        kreis="Olp",
        ort="La",
    )
    LAUT_OLP_LE = Sammlung(
        trace="Olp Le",
        groups="Lautschrift|Olp Le",
        kreis="Olp",
        ort="Le",
    )
    LAUT_OLP_LI = Sammlung(
        trace="Olp Li",
        groups="Lautschrift|Olp Li",
        kreis="Olp",
        ort="Li",
    )
    LAUT_OLP_LS = Sammlung(
        trace="Olp Ls",
        groups="Lautschrift|Olp Ls",
        kreis="Olp",
        ort="Ls",
    )
    LAUT_OLP_LÜ = Sammlung(
        trace="Olp Lü",
        groups="Lautschrift|Olp Lü",
        kreis="Olp",
        ort="Lü",
    )
    LAUT_OLP_MA = Sammlung(
        trace="Olp Ma",
        groups="Lautschrift|Olp Ma",
        kreis="Olp",
        ort="Ma",
    )
    LAUT_OLP_MB = Sammlung(
        trace="Olp Mb",
        groups="Lautschrift|Olp Mb",
        kreis="Olp",
        ort="Mb",
    )
    LAUT_OLP_ME = Sammlung(
        trace="Olp Me",
        groups="Lautschrift|Olp Me",
        kreis="Olp",
        ort="Me",
    )
    LAUT_OLP_MH = Sammlung(
        trace="Olp Mh",
        groups="Lautschrift|Olp Mh",
        kreis="Olp",
        ort="Mh",
    )
    LAUT_OLP_MK = Sammlung(
        trace="Olp Mk",
        groups="Lautschrift|Olp Mk",
        kreis="Olp",
        ort="Mk",
    )
    LAUT_OLP_NE = Sammlung(
        trace="Olp Ne",
        groups="Lautschrift|Olp Ne",
        kreis="Olp",
        ort="Ne",
    )
    LAUT_OLP_NH = Sammlung(
        trace="Olp Nh",
        groups="Lautschrift|Olp Nh",
        kreis="Olp",
        ort="Nh",
    )
    LAUT_OLP_NK = Sammlung(
        trace="Olp Nk",
        groups="Lautschrift|Olp Nk",
        kreis="Olp",
        ort="Nk",
    )
    LAUT_OLP_OE = Sammlung(
        trace="Olp Oe",
        groups="Lautschrift|Olp Oe",
        kreis="Olp",
        ort="Oe",
    )
    LAUT_OLP_OF = Sammlung(
        trace="Olp Of",
        groups="Lautschrift|Olp Of",
        kreis="Olp",
        ort="Of",
    )
    LAUT_OLP_OH = Sammlung(
        trace="Olp Oh",
        groups="Lautschrift|Olp Oh",
        kreis="Olp",
        ort="Oh",
    )
    LAUT_OLP_OL = Sammlung(
        trace="Olp Ol",
        groups="Lautschrift|Olp Ol",
        kreis="Olp",
        ort="Ol",
    )
    LAUT_OLP_OM = Sammlung(
        trace="Olp Om",
        groups="Lautschrift|Olp Om",
        kreis="Olp",
        ort="Om",
    )
    LAUT_OLP_OV = Sammlung(
        trace="Olp Ov",
        groups="Lautschrift|Olp Ov",
        kreis="Olp",
        ort="Ov",
    )
    LAUT_OLP_RB = Sammlung(
        trace="Olp Rb",
        groups="Lautschrift|Olp Rb",
        kreis="Olp",
        ort="Rb",
    )
    LAUT_OLP_RE = Sammlung(
        trace="Olp Re",
        groups="Lautschrift|Olp Re",
        kreis="Olp",
        ort="Re",
    )
    LAUT_OLP_RH = Sammlung(
        trace="Olp Rh",
        groups="Lautschrift|Olp Rh",
        kreis="Olp",
        ort="Rh",
    )
    LAUT_OLP_RI = Sammlung(
        trace="Olp Ri",
        groups="Lautschrift|Olp Ri",
        kreis="Olp",
        ort="Ri",
    )
    LAUT_OLP_RL = Sammlung(
        trace="Olp Rl",
        groups="Lautschrift|Olp Rl",
        kreis="Olp",
        ort="Rl",
    )
    LAUT_OLP_RO = Sammlung(
        trace="Olp Ro",
        groups="Lautschrift|Olp Ro",
        kreis="Olp",
        ort="Ro",
    )
    LAUT_OLP_RÖ = Sammlung(
        trace="Olp Rö",
        groups="Lautschrift|Olp Rö",
        kreis="Olp",
        ort="Rö",
    )
    LAUT_OLP_RP = Sammlung(
        trace="Olp Rp",
        groups="Lautschrift|Olp Rp",
        kreis="Olp",
        ort="Rp",
    )
    LAUT_OLP_RÜ = Sammlung(
        trace="Olp Rü",
        groups="Lautschrift|Olp Rü",
        kreis="Olp",
        ort="Rü",
    )
    LAUT_OLP_SB = Sammlung(
        trace="Olp Sb",
        groups="Lautschrift|Olp Sb",
        kreis="Olp",
        ort="Sb",
    )
    LAUT_OLP_SC = Sammlung(
        trace="Olp Sc",
        groups="Lautschrift|Olp Sc",
        kreis="Olp",
        ort="Sc",
    )
    LAUT_OLP_SH = Sammlung(
        trace="Olp Sh",
        groups="Lautschrift|Olp Sh",
        kreis="Olp",
        ort="Sh",
    )
    LAUT_OLP_SM = Sammlung(
        trace="Olp Sm",
        groups="Lautschrift|Olp Sm",
        kreis="Olp",
        ort="Sm",
    )
    LAUT_OLP_SP = Sammlung(
        trace="Olp Sp",
        groups="Lautschrift|Olp Sp",
        kreis="Olp",
        ort="Sp",
    )
    LAUT_OLP_SR = Sammlung(
        trace="Olp Sr",
        groups="Lautschrift|Olp Sr",
        kreis="Olp",
        ort="Sr",
    )
    LAUT_OLP_TE = Sammlung(
        trace="Olp Te",
        groups="Lautschrift|Olp Te",
        kreis="Olp",
        ort="Te",
    )
    LAUT_OLP_TH = Sammlung(
        trace="Olp Th",
        groups="Lautschrift|Olp Th",
        kreis="Olp",
        ort="Th",
    )
    LAUT_OLP_TI = Sammlung(
        trace="Olp Ti",
        groups="Lautschrift|Olp Ti",
        kreis="Olp",
        ort="Ti",
    )
    LAUT_OLP_VA = Sammlung(
        trace="Olp Va",
        groups="Lautschrift|Olp Va",
        kreis="Olp",
        ort="Va",
    )
    LAUT_OLP_WE = Sammlung(
        trace="Olp We",
        groups="Lautschrift|Olp We",
        kreis="Olp",
        ort="We",
    )
    LAUT_OLP_WI = Sammlung(
        trace="Olp Wi",
        groups="Lautschrift|Olp Wi",
        kreis="Olp",
        ort="Wi",
    )
    LAUT_OLP_WN = Sammlung(
        trace="Olp Wn",
        groups="Lautschrift|Olp Wn",
        kreis="Olp",
        ort="Wn",
    )
    LAUT_OSN_AD = Sammlung(
        trace="Osn Ad",
        groups="Lautschrift|Osn Ad",
        kreis="Osn",
        ort="Ad",
    )
    LAUT_OSN_AF = Sammlung(
        trace="Osn Af",
        groups="Lautschrift|Osn Af",
        kreis="Osn",
        ort="Af",
    )
    LAUT_OSN_AL = Sammlung(
        trace="Osn Al",
        groups="Lautschrift|Osn Al",
        kreis="Osn",
        ort="Al",
    )
    LAUT_OSN_AS = Sammlung(
        trace="Osn As",
        groups="Lautschrift|Osn As",
        kreis="Osn",
        ort="As",
    )
    LAUT_OSN_AT = Sammlung(
        trace="Osn At",
        groups="Lautschrift|Osn At",
        kreis="Osn",
        ort="At",
    )
    LAUT_OSN_BD = Sammlung(
        trace="Osn Bd",
        groups="Lautschrift|Osn Bd",
        kreis="Osn",
        ort="Bd",
    )
    LAUT_OSN_BE = Sammlung(
        trace="Osn Be",
        groups="Lautschrift|Osn Be",
        kreis="Osn",
        ort="Be",
    )
    LAUT_OSN_BO = Sammlung(
        trace="Osn Bo",
        groups="Lautschrift|Osn Bo",
        kreis="Osn",
        ort="Bo",
    )
    LAUT_OSN_ED = Sammlung(
        trace="Osn Ed",
        groups="Lautschrift|Osn Ed",
        kreis="Osn",
        ort="Ed",
    )
    LAUT_OSN_ER = Sammlung(
        trace="Osn Er",
        groups="Lautschrift|Osn Er",
        kreis="Osn",
        ort="Er",
    )
    LAUT_OSN_GA = Sammlung(
        trace="Osn Ga",
        groups="Lautschrift|Osn Ga",
        kreis="Osn",
        ort="Ga",
    )
    LAUT_OSN_GB = Sammlung(
        trace="Osn Gb",
        groups="Lautschrift|Osn Gb",
        kreis="Osn",
        ort="Gb",
    )
    LAUT_OSN_GH = Sammlung(
        trace="Osn Gh",
        groups="Lautschrift|Osn Gh",
        kreis="Osn",
        ort="Gh",
    )
    LAUT_OSN_GL = Sammlung(
        trace="Osn Gl",
        groups="Lautschrift|Osn Gl",
        kreis="Osn",
        ort="Gl",
    )
    LAUT_OSN_GN = Sammlung(
        trace="Osn Gn",
        groups="Lautschrift|Osn Gn",
        kreis="Osn",
        ort="Gn",
    )
    LAUT_OSN_GR = Sammlung(
        trace="Osn Gr",
        groups="Lautschrift|Osn Gr",
        kreis="Osn",
        ort="Gr",
    )
    LAUT_OSN_HA = Sammlung(
        trace="Osn Ha",
        groups="Lautschrift|Osn Ha",
        kreis="Osn",
        ort="Ha",
    )
    LAUT_OSN_HB = Sammlung(
        trace="Osn Hb",
        groups="Lautschrift|Osn Hb",
        kreis="Osn",
        ort="Hb",
    )
    LAUT_OSN_HD = Sammlung(
        trace="Osn Hd",
        groups="Lautschrift|Osn Hd",
        kreis="Osn",
        ort="Hd",
    )
    LAUT_OSN_HE = Sammlung(
        trace="Osn He",
        groups="Lautschrift|Osn He",
        kreis="Osn",
        ort="He",
    )
    LAUT_OSN_HG = Sammlung(
        trace="Osn Hg",
        groups="Lautschrift|Osn Hg",
        kreis="Osn",
        ort="Hg",
    )
    LAUT_OSN_HI = Sammlung(
        trace="Osn Hi",
        groups="Lautschrift|Osn Hi",
        kreis="Osn",
        ort="Hi",
    )
    LAUT_OSN_HL = Sammlung(
        trace="Osn Hl",
        groups="Lautschrift|Osn Hl",
        kreis="Osn",
        ort="Hl",
    )
    LAUT_OSN_HR = Sammlung(
        trace="Osn Hr",
        groups="Lautschrift|Osn Hr",
        kreis="Osn",
        ort="Hr",
    )
    LAUT_OSN_HS = Sammlung(
        trace="Osn Hs",
        groups="Lautschrift|Osn Hs",
        kreis="Osn",
        ort="Hs",
    )
    LAUT_OSN_HT = Sammlung(
        trace="Osn Ht",
        groups="Lautschrift|Osn Ht",
        kreis="Osn",
        ort="Ht",
    )
    LAUT_OSN_IB = Sammlung(
        trace="Osn Ib",
        groups="Lautschrift|Osn Ib",
        kreis="Osn",
        ort="Ib",
    )
    LAUT_OSN_IK = Sammlung(
        trace="Osn Ik",
        groups="Lautschrift|Osn Ik",
        kreis="Osn",
        ort="Ik",
    )
    LAUT_OSN_JE = Sammlung(
        trace="Osn Je",
        groups="Lautschrift|Osn Je",
        kreis="Osn",
        ort="Je",
    )
    LAUT_OSN_KK = Sammlung(
        trace="Osn Kk",
        groups="Lautschrift|Osn Kk",
        kreis="Osn",
        ort="Kk",
    )
    LAUT_OSN_KL = Sammlung(
        trace="Osn Kl",
        groups="Lautschrift|Osn Kl",
        kreis="Osn",
        ort="Kl",
    )
    LAUT_OSN_LA = Sammlung(
        trace="Osn La",
        groups="Lautschrift|Osn La",
        kreis="Osn",
        ort="La",
    )
    LAUT_OSN_LE = Sammlung(
        trace="Osn Le",
        groups="Lautschrift|Osn Le",
        kreis="Osn",
        ort="Le",
    )
    LAUT_OSN_LÜ = Sammlung(
        trace="Osn Lü",
        groups="Lautschrift|Osn Lü",
        kreis="Osn",
        ort="Lü",
    )
    LAUT_OSN_MB = Sammlung(
        trace="Osn Mb",
        groups="Lautschrift|Osn Mb",
        kreis="Osn",
        ort="Mb",
    )
    LAUT_OSN_ME = Sammlung(
        trace="Osn Me",
        groups="Lautschrift|Osn Me",
        kreis="Osn",
        ort="Me",
    )
    LAUT_OSN_MY = Sammlung(
        trace="Osn My",
        groups="Lautschrift|Osn My",
        kreis="Osn",
        ort="My",
    )
    LAUT_OSN_NA = Sammlung(
        trace="Osn Na",
        groups="Lautschrift|Osn Na",
        kreis="Osn",
        ort="Na",
    )
    LAUT_OSN_NE = Sammlung(
        trace="Osn Ne",
        groups="Lautschrift|Osn Ne",
        kreis="Osn",
        ort="Ne",
    )
    LAUT_OSN_NH = Sammlung(
        trace="Osn Nh",
        groups="Lautschrift|Osn Nh",
        kreis="Osn",
        ort="Nh",
    )
    LAUT_OSN_NT = Sammlung(
        trace="Osn Nt",
        groups="Lautschrift|Osn Nt",
        kreis="Osn",
        ort="Nt",
    )
    LAUT_OSN_OB = Sammlung(
        trace="Osn Ob",
        groups="Lautschrift|Osn Ob",
        kreis="Osn",
        ort="Ob",
    )
    LAUT_OSN_OF = Sammlung(
        trace="Osn Of",
        groups="Lautschrift|Osn Of",
        kreis="Osn",
        ort="Of",
    )
    LAUT_OSN_OK = Sammlung(
        trace="Osn Ok",
        groups="Lautschrift|Osn Ok",
        kreis="Osn",
        ort="Ok",
    )
    LAUT_OSN_OR = Sammlung(
        trace="Osn Or",
        groups="Lautschrift|Osn Or",
        kreis="Osn",
        ort="Or",
    )
    LAUT_OSN_ÖS = Sammlung(
        trace="Osn Ös",
        groups="Lautschrift|Osn Ös",
        kreis="Osn",
        ort="Ös",
    )
    LAUT_OSN_PI = Sammlung(
        trace="Osn Pi",
        groups="Lautschrift|Osn Pi",
        kreis="Osn",
        ort="Pi",
    )
    LAUT_OSN_RE = Sammlung(
        trace="Osn Re",
        groups="Lautschrift|Osn Re",
        kreis="Osn",
        ort="Re",
    )
    LAUT_OSN_RF = Sammlung(
        trace="Osn Rf",
        groups="Lautschrift|Osn Rf",
        kreis="Osn",
        ort="Rf",
    )
    LAUT_OSN_RU = Sammlung(
        trace="Osn Ru",
        groups="Lautschrift|Osn Ru",
        kreis="Osn",
        ort="Ru",
    )
    LAUT_OSN_SC = Sammlung(
        trace="Osn Sc",
        groups="Lautschrift|Osn Sc",
        kreis="Osn",
        ort="Sc",
    )
    LAUT_OSN_SD = Sammlung(
        trace="Osn Sd",
        groups="Lautschrift|Osn Sd",
        kreis="Osn",
        ort="Sd",
    )
    LAUT_OSN_SE = Sammlung(
        trace="Osn Se",
        groups="Lautschrift|Osn Se",
        kreis="Osn",
        ort="Se",
    )
    LAUT_OSN_SF = Sammlung(
        trace="Osn Sf",
        groups="Lautschrift|Osn Sf",
        kreis="Osn",
        ort="Sf",
    )
    LAUT_OSN_SH = Sammlung(
        trace="Osn Sh",
        groups="Lautschrift|Osn Sh",
        kreis="Osn",
        ort="Sh",
    )
    LAUT_OSN_SL = Sammlung(
        trace="Osn Sl",
        groups="Lautschrift|Osn Sl",
        kreis="Osn",
        ort="Sl",
    )
    LAUT_OSN_SP = Sammlung(
        trace="Osn Sp",
        groups="Lautschrift|Osn Sp",
        kreis="Osn",
        ort="Sp",
    )
    LAUT_OSN_SU = Sammlung(
        trace="Osn Su",
        groups="Lautschrift|Osn Su",
        kreis="Osn",
        ort="Su",
    )
    LAUT_OSN_SW = Sammlung(
        trace="Osn Sw",
        groups="Lautschrift|Osn Sw",
        kreis="Osn",
        ort="Sw",
    )
    LAUT_OSN_UH = Sammlung(
        trace="Osn Uh",
        groups="Lautschrift|Osn Uh",
        kreis="Osn",
        ort="Uh",
    )
    LAUT_OSN_VE = Sammlung(
        trace="Osn Ve",
        groups="Lautschrift|Osn Ve",
        kreis="Osn",
        ort="Ve",
    )
    LAUT_OSN_VO = Sammlung(
        trace="Osn Vo",
        groups="Lautschrift|Osn Vo",
        kreis="Osn",
        ort="Vo",
    )
    LAUT_OSN_WD = Sammlung(
        trace="Osn Wd",
        groups="Lautschrift|Osn Wd",
        kreis="Osn",
        ort="Wd",
    )
    LAUT_OSN_WE = Sammlung(
        trace="Osn We",
        groups="Lautschrift|Osn We",
        kreis="Osn",
        ort="We",
    )
    LAUT_OSN_WF = Sammlung(
        trace="Osn Wf",
        groups="Lautschrift|Osn Wf",
        kreis="Osn",
        ort="Wf",
    )
    LAUT_OSN_WH = Sammlung(
        trace="Osn Wh",
        groups="Lautschrift|Osn Wh",
        kreis="Osn",
        ort="Wh",
    )
    LAUT_OSN_WS = Sammlung(
        trace="Osn Ws",
        groups="Lautschrift|Osn Ws",
        kreis="Osn",
        ort="Ws",
    )
    LAUT_PAD_AB = Sammlung(
        trace="Pad Ab",
        groups="Lautschrift|Pad Ab",
        kreis="Pad",
        ort="Ab",
    )
    LAUT_PAD_AL = Sammlung(
        trace="Pad Al",
        groups="Lautschrift|Pad Al",
        kreis="Pad",
        ort="Al",
    )
    LAUT_PAD_BH = Sammlung(
        trace="Pad Bh",
        groups="Lautschrift|Pad Bh",
        kreis="Pad",
        ort="Bh",
    )
    LAUT_PAD_BO = Sammlung(
        trace="Pad Bo",
        groups="Lautschrift|Pad Bo",
        kreis="Pad",
        ort="Bo",
    )
    LAUT_PAD_BU = Sammlung(
        trace="Pad Bu",
        groups="Lautschrift|Pad Bu",
        kreis="Pad",
        ort="Bu",
    )
    LAUT_PAD_DA = Sammlung(
        trace="Pad Da",
        groups="Lautschrift|Pad Da",
        kreis="Pad",
        ort="Da",
    )
    LAUT_PAD_DB = Sammlung(
        trace="Pad Db",
        groups="Lautschrift|Pad Db",
        kreis="Pad",
        ort="Db",
    )
    LAUT_PAD_DH = Sammlung(
        trace="Pad Dh",
        groups="Lautschrift|Pad Dh",
        kreis="Pad",
        ort="Dh",
    )
    LAUT_PAD_EL = Sammlung(
        trace="Pad El",
        groups="Lautschrift|Pad El",
        kreis="Pad",
        ort="El",
    )
    LAUT_PAD_ES = Sammlung(
        trace="Pad Es",
        groups="Lautschrift|Pad Es",
        kreis="Pad",
        ort="Es",
    )
    LAUT_PAD_HH = Sammlung(
        trace="Pad Hh",
        groups="Lautschrift|Pad Hh",
        kreis="Pad",
        ort="Hh",
    )
    LAUT_PAD_HÖ = Sammlung(
        trace="Pad Hö",
        groups="Lautschrift|Pad Hö",
        kreis="Pad",
        ort="Hö",
    )
    LAUT_PAD_KB = Sammlung(
        trace="Pad Kb",
        groups="Lautschrift|Pad Kb",
        kreis="Pad",
        ort="Kb",
    )
    LAUT_PAD_KL = Sammlung(
        trace="Pad Kl",
        groups="Lautschrift|Pad Kl",
        kreis="Pad",
        ort="Kl",
    )
    LAUT_PAD_LI = Sammlung(
        trace="Pad Li",
        groups="Lautschrift|Pad Li",
        kreis="Pad",
        ort="Li",
    )
    LAUT_PAD_LP = Sammlung(
        trace="Pad Lp",
        groups="Lautschrift|Pad Lp",
        kreis="Pad",
        ort="Lp",
    )
    LAUT_PAD_ML = Sammlung(
        trace="Pad Ml",
        groups="Lautschrift|Pad Ml",
        kreis="Pad",
        ort="Ml",
    )
    LAUT_PAD_NB = Sammlung(
        trace="Pad Nb",
        groups="Lautschrift|Pad Nb",
        kreis="Pad",
        ort="Nb",
    )
    LAUT_PAD_NE = Sammlung(
        trace="Pad Ne",
        groups="Lautschrift|Pad Ne",
        kreis="Pad",
        ort="Ne",
    )
    LAUT_PAD_NH = Sammlung(
        trace="Pad Nh",
        groups="Lautschrift|Pad Nh",
        kreis="Pad",
        ort="Nh",
    )
    LAUT_PAD_NS = Sammlung(
        trace="Pad Ns",
        groups="Lautschrift|Pad Ns",
        kreis="Pad",
        ort="Ns",
    )
    LAUT_PAD_NT = Sammlung(
        trace="Pad Nt",
        groups="Lautschrift|Pad Nt",
        kreis="Pad",
        ort="Nt",
    )
    LAUT_PAD_OL = Sammlung(
        trace="Pad Ol",
        groups="Lautschrift|Pad Ol",
        kreis="Pad",
        ort="Ol",
    )
    LAUT_PAD_OM = Sammlung(
        trace="Pad Om",
        groups="Lautschrift|Pad Om",
        kreis="Pad",
        ort="Om",
    )
    LAUT_PAD_PB = Sammlung(
        trace="Pad Pb",
        groups="Lautschrift|Pad Pb",
        kreis="Pad",
        ort="Pb",
    )
    LAUT_PAD_RI = Sammlung(
        trace="Pad Ri",
        groups="Lautschrift|Pad Ri",
        kreis="Pad",
        ort="Ri",
    )
    LAUT_PAD_SA = Sammlung(
        trace="Pad Sa",
        groups="Lautschrift|Pad Sa",
        kreis="Pad",
        ort="Sa",
    )
    LAUT_PAD_SC = Sammlung(
        trace="Pad Sc",
        groups="Lautschrift|Pad Sc",
        kreis="Pad",
        ort="Sc",
    )
    LAUT_PAD_SH = Sammlung(
        trace="Pad Sh",
        groups="Lautschrift|Pad Sh",
        kreis="Pad",
        ort="Sh",
    )
    LAUT_PAD_SL = Sammlung(
        trace="Pad Sl",
        groups="Lautschrift|Pad Sl",
        kreis="Pad",
        ort="Sl",
    )
    LAUT_PAD_ST = Sammlung(
        trace="Pad St",
        groups="Lautschrift|Pad St",
        kreis="Pad",
        ort="St",
    )
    LAUT_PAD_SU = Sammlung(
        trace="Pad Su",
        groups="Lautschrift|Pad Su",
        kreis="Pad",
        ort="Su",
    )
    LAUT_PAD_SW = Sammlung(
        trace="Pad Sw",
        groups="Lautschrift|Pad Sw",
        kreis="Pad",
        ort="Sw",
    )
    LAUT_PAD_WH = Sammlung(
        trace="Pad Wh",
        groups="Lautschrift|Pad Wh",
        kreis="Pad",
        ort="Wh",
    )
    LAUT_PAD_WL = Sammlung(
        trace="Pad Wl",
        groups="Lautschrift|Pad Wl",
        kreis="Pad",
        ort="Wl",
    )
    LAUT_PAD_WW = Sammlung(
        trace="Pad Ww",
        groups="Lautschrift|Pad Ww",
        kreis="Pad",
        ort="Ww",
    )
    LAUT_REK_AD = Sammlung(
        trace="Rek Ad",
        groups="Lautschrift|Rek Ad",
        kreis="Rek",
        ort="Ad",
    )
    LAUT_REK_AL = Sammlung(
        trace="Rek Al",
        groups="Lautschrift|Rek Al",
        kreis="Rek",
        ort="Al",
    )
    LAUT_REK_AS = Sammlung(
        trace="Rek As",
        groups="Lautschrift|Rek As",
        kreis="Rek",
        ort="As",
    )
    LAUT_REK_BA = Sammlung(
        trace="Rek Ba",
        groups="Lautschrift|Rek Ba",
        kreis="Rek",
        ort="Ba",
    )
    LAUT_REK_BD = Sammlung(
        trace="Rek Bd",
        groups="Lautschrift|Rek Bd",
        kreis="Rek",
        ort="Bd",
    )
    LAUT_REK_BM = Sammlung(
        trace="Rek Bm",
        groups="Lautschrift|Rek Bm",
        kreis="Rek",
        ort="Bm",
    )
    LAUT_REK_BO = Sammlung(
        trace="Rek Bo",
        groups="Lautschrift|Rek Bo",
        kreis="Rek",
        ort="Bo",
    )
    LAUT_REK_BP = Sammlung(
        trace="Rek Bp",
        groups="Lautschrift|Rek Bp",
        kreis="Rek",
        ort="Bp",
    )
    LAUT_REK_BS = Sammlung(
        trace="Rek Bs",
        groups="Lautschrift|Rek Bs",
        kreis="Rek",
        ort="Bs",
    )
    LAUT_REK_BU = Sammlung(
        trace="Rek Bu",
        groups="Lautschrift|Rek Bu",
        kreis="Rek",
        ort="Bu",
    )
    LAUT_REK_BX = Sammlung(
        trace="Rek Bx",
        groups="Lautschrift|Rek Bx",
        kreis="Rek",
        ort="Bx",
    )
    LAUT_REK_DA = Sammlung(
        trace="Rek Da",
        groups="Lautschrift|Rek Da",
        kreis="Rek",
        ort="Da",
    )
    LAUT_REK_DE = Sammlung(
        trace="Rek De",
        groups="Lautschrift|Rek De",
        kreis="Rek",
        ort="De",
    )
    LAUT_REK_DI = Sammlung(
        trace="Rek Di",
        groups="Lautschrift|Rek Di",
        kreis="Rek",
        ort="Di",
    )
    LAUT_REK_DO = Sammlung(
        trace="Rek Do",
        groups="Lautschrift|Rek Do",
        kreis="Rek",
        ort="Do",
    )
    LAUT_REK_ER = Sammlung(
        trace="Rek Er",
        groups="Lautschrift|Rek Er",
        kreis="Rek",
        ort="Er",
    )
    LAUT_REK_ES = Sammlung(
        trace="Rek Es",
        groups="Lautschrift|Rek Es",
        kreis="Rek",
        ort="Es",
    )
    LAUT_REK_FH = Sammlung(
        trace="Rek Fh",
        groups="Lautschrift|Rek Fh",
        kreis="Rek",
        ort="Fh",
    )
    LAUT_REK_GB = Sammlung(
        trace="Rek Gb",
        groups="Lautschrift|Rek Gb",
        kreis="Rek",
        ort="Gb",
    )
    LAUT_REK_GL = Sammlung(
        trace="Rek Gl",
        groups="Lautschrift|Rek Gl",
        kreis="Rek",
        ort="Gl",
    )
    LAUT_REK_HA = Sammlung(
        trace="Rek Ha",
        groups="Lautschrift|Rek Ha",
        kreis="Rek",
        ort="Ha",
    )
    LAUT_REK_HB = Sammlung(
        trace="Rek Hb",
        groups="Lautschrift|Rek Hb",
        kreis="Rek",
        ort="Hb",
    )
    LAUT_REK_HE = Sammlung(
        trace="Rek He",
        groups="Lautschrift|Rek He",
        kreis="Rek",
        ort="He",
    )
    LAUT_REK_HH = Sammlung(
        trace="Rek Hh",
        groups="Lautschrift|Rek Hh",
        kreis="Rek",
        ort="Hh",
    )
    LAUT_REK_HL = Sammlung(
        trace="Rek Hl",
        groups="Lautschrift|Rek Hl",
        kreis="Rek",
        ort="Hl",
    )
    LAUT_REK_HM = Sammlung(
        trace="Rek Hm",
        groups="Lautschrift|Rek Hm",
        kreis="Rek",
        ort="Hm",
    )
    LAUT_REK_HO = Sammlung(
        trace="Rek Ho",
        groups="Lautschrift|Rek Ho",
        kreis="Rek",
        ort="Ho",
    )
    LAUT_REK_HR = Sammlung(
        trace="Rek Hr",
        groups="Lautschrift|Rek Hr",
        kreis="Rek",
        ort="Hr",
    )
    LAUT_REK_HU = Sammlung(
        trace="Rek Hu",
        groups="Lautschrift|Rek Hu",
        kreis="Rek",
        ort="Hu",
    )
    LAUT_REK_HÜ = Sammlung(
        trace="Rek Hü",
        groups="Lautschrift|Rek Hü",
        kreis="Rek",
        ort="Hü",
    )
    LAUT_REK_HV = Sammlung(
        trace="Rek Hv",
        groups="Lautschrift|Rek Hv",
        kreis="Rek",
        ort="Hv",
    )
    LAUT_REK_HX = Sammlung(
        trace="Rek Hx",
        groups="Lautschrift|Rek Hx",
        kreis="Rek",
        ort="Hx",
    )
    LAUT_REK_KH = Sammlung(
        trace="Rek Kh",
        groups="Lautschrift|Rek Kh",
        kreis="Rek",
        ort="Kh",
    )
    LAUT_REK_LA = Sammlung(
        trace="Rek La",
        groups="Lautschrift|Rek La",
        kreis="Rek",
        ort="La",
    )
    LAUT_REK_LB = Sammlung(
        trace="Rek Lb",
        groups="Lautschrift|Rek Lb",
        kreis="Rek",
        ort="Lb",
    )
    LAUT_REK_LD = Sammlung(
        trace="Rek Ld",
        groups="Lautschrift|Rek Ld",
        kreis="Rek",
        ort="Ld",
    )
    LAUT_REK_LH = Sammlung(
        trace="Rek Lh",
        groups="Lautschrift|Rek Lh",
        kreis="Rek",
        ort="Lh",
    )
    LAUT_REK_MA = Sammlung(
        trace="Rek Ma",
        groups="Lautschrift|Rek Ma",
        kreis="Rek",
        ort="Ma",
    )
    LAUT_REK_MH = Sammlung(
        trace="Rek Mh",
        groups="Lautschrift|Rek Mh",
        kreis="Rek",
        ort="Mh",
    )
    LAUT_REK_OF = Sammlung(
        trace="Rek Of",
        groups="Lautschrift|Rek Of",
        kreis="Rek",
        ort="Of",
    )
    LAUT_REK_PE = Sammlung(
        trace="Rek Pe",
        groups="Lautschrift|Rek Pe",
        kreis="Rek",
        ort="Pe",
    )
    LAUT_REK_PO = Sammlung(
        trace="Rek Po",
        groups="Lautschrift|Rek Po",
        kreis="Rek",
        ort="Po",
    )
    LAUT_REK_RA = Sammlung(
        trace="Rek Ra",
        groups="Lautschrift|Rek Ra",
        kreis="Rek",
        ort="Ra",
    )
    LAUT_REK_RH = Sammlung(
        trace="Rek Rh",
        groups="Lautschrift|Rek Rh",
        kreis="Rek",
        ort="Rh",
    )
    LAUT_REK_RS = Sammlung(
        trace="Rek Rs",
        groups="Lautschrift|Rek Rs",
        kreis="Rek",
        ort="Rs",
    )
    LAUT_REK_SI = Sammlung(
        trace="Rek Si",
        groups="Lautschrift|Rek Si",
        kreis="Rek",
        ort="Si",
    )
    LAUT_REK_SM = Sammlung(
        trace="Rek Sm",
        groups="Lautschrift|Rek Sm",
        kreis="Rek",
        ort="Sm",
    )
    LAUT_REK_ST = Sammlung(
        trace="Rek St",
        groups="Lautschrift|Rek St",
        kreis="Rek",
        ort="St",
    )
    LAUT_REK_SY = Sammlung(
        trace="Rek Sy",
        groups="Lautschrift|Rek Sy",
        kreis="Rek",
        ort="Sy",
    )
    LAUT_REK_WD = Sammlung(
        trace="Rek Wd",
        groups="Lautschrift|Rek Wd",
        kreis="Rek",
        ort="Wd",
    )
    LAUT_REK_WH = Sammlung(
        trace="Rek Wh",
        groups="Lautschrift|Rek Wh",
        kreis="Rek",
        ort="Wh",
    )
    LAUT_REK_WP = Sammlung(
        trace="Rek Wp",
        groups="Lautschrift|Rek Wp",
        kreis="Rek",
        ort="Wp",
    )
    LAUT_REK_WU = Sammlung(
        trace="Rek Wu",
        groups="Lautschrift|Rek Wu",
        kreis="Rek",
        ort="Wu",
    )
    LAUT_SCH_AL = Sammlung(
        trace="Sch Al",
        groups="Lautschrift|Sch Al",
        kreis="Sch",
        ort="Al",
    )
    LAUT_SCH_AN = Sammlung(
        trace="Sch An",
        groups="Lautschrift|Sch An",
        kreis="Sch",
        ort="An",
    )
    LAUT_SCH_AP = Sammlung(
        trace="Sch Ap",
        groups="Lautschrift|Sch Ap",
        kreis="Sch",
        ort="Ap",
    )
    LAUT_SCH_AU = Sammlung(
        trace="Sch Au",
        groups="Lautschrift|Sch Au",
        kreis="Sch",
        ort="Au",
    )
    LAUT_SCH_BA = Sammlung(
        trace="Sch Ba",
        groups="Lautschrift|Sch Ba",
        kreis="Sch",
        ort="Ba",
    )
    LAUT_SCH_BD = Sammlung(
        trace="Sch Bd",
        groups="Lautschrift|Sch Bd",
        kreis="Sch",
        ort="Bd",
    )
    LAUT_SCH_BO = Sammlung(
        trace="Sch Bo",
        groups="Lautschrift|Sch Bo",
        kreis="Sch",
        ort="Bo",
    )
    LAUT_SCH_DB = Sammlung(
        trace="Sch Db",
        groups="Lautschrift|Sch Db",
        kreis="Sch",
        ort="Db",
    )
    LAUT_SCH_EN = Sammlung(
        trace="Sch En",
        groups="Lautschrift|Sch En",
        kreis="Sch",
        ort="En",
    )
    LAUT_SCH_ES = Sammlung(
        trace="Sch Es",
        groups="Lautschrift|Sch Es",
        kreis="Sch",
        ort="Es",
    )
    LAUT_SCH_EX = Sammlung(
        trace="Sch Ex",
        groups="Lautschrift|Sch Ex",
        kreis="Sch",
        ort="Ex",
    )
    LAUT_SCH_FI = Sammlung(
        trace="Sch Fi",
        groups="Lautschrift|Sch Fi",
        kreis="Sch",
        ort="Fi",
    )
    LAUT_SCH_FU = Sammlung(
        trace="Sch Fu",
        groups="Lautschrift|Sch Fu",
        kreis="Sch",
        ort="Fu",
    )
    LAUT_SCH_GB = Sammlung(
        trace="Sch Gb",
        groups="Lautschrift|Sch Gb",
        kreis="Sch",
        ort="Gb",
    )
    LAUT_SCH_GH = Sammlung(
        trace="Sch Gh",
        groups="Lautschrift|Sch Gh",
        kreis="Sch",
        ort="Gh",
    )
    LAUT_SCH_GN = Sammlung(
        trace="Sch Gn",
        groups="Lautschrift|Sch Gn",
        kreis="Sch",
        ort="Gn",
    )
    LAUT_SCH_GW = Sammlung(
        trace="Sch Gw",
        groups="Lautschrift|Sch Gw",
        kreis="Sch",
        ort="Gw",
    )
    LAUT_SCH_HA = Sammlung(
        trace="Sch Ha",
        groups="Lautschrift|Sch Ha",
        kreis="Sch",
        ort="Ha",
    )
    LAUT_SCH_HD = Sammlung(
        trace="Sch Hd",
        groups="Lautschrift|Sch Hd",
        kreis="Sch",
        ort="Hd",
    )
    LAUT_SCH_HE = Sammlung(
        trace="Sch He",
        groups="Lautschrift|Sch He",
        kreis="Sch",
        ort="He",
    )
    LAUT_SCH_HH = Sammlung(
        trace="Sch Hh",
        groups="Lautschrift|Sch Hh",
        kreis="Sch",
        ort="Hh",
    )
    LAUT_SCH_HO = Sammlung(
        trace="Sch Ho",
        groups="Lautschrift|Sch Ho",
        kreis="Sch",
        ort="Ho",
    )
    LAUT_SCH_HÖ = Sammlung(
        trace="Sch Hö",
        groups="Lautschrift|Sch Hö",
        kreis="Sch",
        ort="Hö",
    )
    LAUT_SCH_HR = Sammlung(
        trace="Sch Hr",
        groups="Lautschrift|Sch Hr",
        kreis="Sch",
        ort="Hr",
    )
    LAUT_SCH_HT = Sammlung(
        trace="Sch Ht",
        groups="Lautschrift|Sch Ht",
        kreis="Sch",
        ort="Ht",
    )
    LAUT_SCH_KA = Sammlung(
        trace="Sch Ka",
        groups="Lautschrift|Sch Ka",
        kreis="Sch",
        ort="Ka",
    )
    LAUT_SCH_KH = Sammlung(
        trace="Sch Kh",
        groups="Lautschrift|Sch Kh",
        kreis="Sch",
        ort="Kh",
    )
    LAUT_SCH_KR = Sammlung(
        trace="Sch Kr",
        groups="Lautschrift|Sch Kr",
        kreis="Sch",
        ort="Kr",
    )
    LAUT_SCH_LF = Sammlung(
        trace="Sch Lf",
        groups="Lautschrift|Sch Lf",
        kreis="Sch",
        ort="Lf",
    )
    LAUT_SCH_LI = Sammlung(
        trace="Sch Li",
        groups="Lautschrift|Sch Li",
        kreis="Sch",
        ort="Li",
    )
    LAUT_SCH_LY = Sammlung(
        trace="Sch Ly",
        groups="Lautschrift|Sch Ly",
        kreis="Sch",
        ort="Ly",
    )
    LAUT_SCH_MB = Sammlung(
        trace="Sch Mb",
        groups="Lautschrift|Sch Mb",
        kreis="Sch",
        ort="Mb",
    )
    LAUT_SCH_ND = Sammlung(
        trace="Sch Nd",
        groups="Lautschrift|Sch Nd",
        kreis="Sch",
        ort="Nd",
    )
    LAUT_SCH_OB = Sammlung(
        trace="Sch Ob",
        groups="Lautschrift|Sch Ob",
        kreis="Sch",
        ort="Ob",
    )
    LAUT_SCH_OT = Sammlung(
        trace="Sch Ot",
        groups="Lautschrift|Sch Ot",
        kreis="Sch",
        ort="Ot",
    )
    LAUT_SCH_PÖ = Sammlung(
        trace="Sch Pö",
        groups="Lautschrift|Sch Pö",
        kreis="Sch",
        ort="Pö",
    )
    LAUT_SCH_RA = Sammlung(
        trace="Sch Ra",
        groups="Lautschrift|Sch Ra",
        kreis="Sch",
        ort="Ra",
    )
    LAUT_SCH_RD = Sammlung(
        trace="Sch Rd",
        groups="Lautschrift|Sch Rd",
        kreis="Sch",
        ort="Rd",
    )
    LAUT_SCH_RE = Sammlung(
        trace="Sch Re",
        groups="Lautschrift|Sch Re",
        kreis="Sch",
        ort="Re",
    )
    LAUT_SCH_RH = Sammlung(
        trace="Sch Rh",
        groups="Lautschrift|Sch Rh",
        kreis="Sch",
        ort="Rh",
    )
    LAUT_SCH_RI = Sammlung(
        trace="Sch Ri",
        groups="Lautschrift|Sch Ri",
        kreis="Sch",
        ort="Ri",
    )
    LAUT_SCH_RN = Sammlung(
        trace="Sch Rn",
        groups="Lautschrift|Sch Rn",
        kreis="Sch",
        ort="Rn",
    )
    LAUT_SCH_RO = Sammlung(
        trace="Sch Ro",
        groups="Lautschrift|Sch Ro",
        kreis="Sch",
        ort="Ro",
    )
    LAUT_SCH_RS = Sammlung(
        trace="Sch Rs",
        groups="Lautschrift|Sch Rs",
        kreis="Sch",
        ort="Rs",
    )
    LAUT_SCH_RU = Sammlung(
        trace="Sch Ru",
        groups="Lautschrift|Sch Ru",
        kreis="Sch",
        ort="Ru",
    )
    LAUT_SCH_SD = Sammlung(
        trace="Sch Sd",
        groups="Lautschrift|Sch Sd",
        kreis="Sch",
        ort="Sd",
    )
    LAUT_SCH_SH = Sammlung(
        trace="Sch Sh",
        groups="Lautschrift|Sch Sh",
        kreis="Sch",
        ort="Sh",
    )
    LAUT_SCH_WA = Sammlung(
        trace="Sch Wa",
        groups="Lautschrift|Sch Wa",
        kreis="Sch",
        ort="Wa",
    )
    LAUT_SCH_WB = Sammlung(
        trace="Sch Wb",
        groups="Lautschrift|Sch Wb",
        kreis="Sch",
        ort="Wb",
    )
    LAUT_SCH_WD = Sammlung(
        trace="Sch Wd",
        groups="Lautschrift|Sch Wd",
        kreis="Sch",
        ort="Wd",
    )
    LAUT_SCH_WE = Sammlung(
        trace="Sch We",
        groups="Lautschrift|Sch We",
        kreis="Sch",
        ort="We",
    )
    LAUT_SCH_WK = Sammlung(
        trace="Sch Wk",
        groups="Lautschrift|Sch Wk",
        kreis="Sch",
        ort="Wk",
    )
    LAUT_SOS_AL = Sammlung(
        trace="Sos Al",
        groups="Lautschrift|Sos Al",
        kreis="Sos",
        ort="Al",
    )
    LAUT_SOS_AM = Sammlung(
        trace="Sos Am",
        groups="Lautschrift|Sos Am",
        kreis="Sos",
        ort="Am",
    )
    LAUT_SOS_BA = Sammlung(
        trace="Sos Ba",
        groups="Lautschrift|Sos Ba",
        kreis="Sos",
        ort="Ba",
    )
    LAUT_SOS_BE = Sammlung(
        trace="Sos Be",
        groups="Lautschrift|Sos Be",
        kreis="Sos",
        ort="Be",
    )
    LAUT_SOS_BG = Sammlung(
        trace="Sos Bg",
        groups="Lautschrift|Sos Bg",
        kreis="Sos",
        ort="Bg",
    )
    LAUT_SOS_BH = Sammlung(
        trace="Sos Bh",
        groups="Lautschrift|Sos Bh",
        kreis="Sos",
        ort="Bh",
    )
    LAUT_SOS_BK = Sammlung(
        trace="Sos Bk",
        groups="Lautschrift|Sos Bk",
        kreis="Sos",
        ort="Bk",
    )
    LAUT_SOS_BL = Sammlung(
        trace="Sos Bl",
        groups="Lautschrift|Sos Bl",
        kreis="Sos",
        ort="Bl",
    )
    LAUT_SOS_BM = Sammlung(
        trace="Sos Bm",
        groups="Lautschrift|Sos Bm",
        kreis="Sos",
        ort="Bm",
    )
    LAUT_SOS_BN = Sammlung(
        trace="Sos Bn",
        groups="Lautschrift|Sos Bn",
        kreis="Sos",
        ort="Bn",
    )
    LAUT_SOS_BO = Sammlung(
        trace="Sos Bo",
        groups="Lautschrift|Sos Bo",
        kreis="Sos",
        ort="Bo",
    )
    LAUT_SOS_BR = Sammlung(
        trace="Sos Br",
        groups="Lautschrift|Sos Br",
        kreis="Sos",
        ort="Br",
    )
    LAUT_SOS_BS = Sammlung(
        trace="Sos Bs",
        groups="Lautschrift|Sos Bs",
        kreis="Sos",
        ort="Bs",
    )
    LAUT_SOS_BT = Sammlung(
        trace="Sos Bt",
        groups="Lautschrift|Sos Bt",
        kreis="Sos",
        ort="Bt",
    )
    LAUT_SOS_BÜ = Sammlung(
        trace="Sos Bü",
        groups="Lautschrift|Sos Bü",
        kreis="Sos",
        ort="Bü",
    )
    LAUT_SOS_BW = Sammlung(
        trace="Sos Bw",
        groups="Lautschrift|Sos Bw",
        kreis="Sos",
        ort="Bw",
    )
    LAUT_SOS_DE = Sammlung(
        trace="Sos De",
        groups="Lautschrift|Sos De",
        kreis="Sos",
        ort="De",
    )
    LAUT_SOS_DI = Sammlung(
        trace="Sos Di",
        groups="Lautschrift|Sos Di",
        kreis="Sos",
        ort="Di",
    )
    LAUT_SOS_DL = Sammlung(
        trace="Sos Dl",
        groups="Lautschrift|Sos Dl",
        kreis="Sos",
        ort="Dl",
    )
    LAUT_SOS_DW = Sammlung(
        trace="Sos Dw",
        groups="Lautschrift|Sos Dw",
        kreis="Sos",
        ort="Dw",
    )
    LAUT_SOS_EB = Sammlung(
        trace="Sos Eb",
        groups="Lautschrift|Sos Eb",
        kreis="Sos",
        ort="Eb",
    )
    LAUT_SOS_EH = Sammlung(
        trace="Sos Eh",
        groups="Lautschrift|Sos Eh",
        kreis="Sos",
        ort="Eh",
    )
    LAUT_SOS_EI = Sammlung(
        trace="Sos Ei",
        groups="Lautschrift|Sos Ei",
        kreis="Sos",
        ort="Ei",
    )
    LAUT_SOS_EK = Sammlung(
        trace="Sos Ek",
        groups="Lautschrift|Sos Ek",
        kreis="Sos",
        ort="Ek",
    )
    LAUT_SOS_EL = Sammlung(
        trace="Sos El",
        groups="Lautschrift|Sos El",
        kreis="Sos",
        ort="El",
    )
    LAUT_SOS_EM = Sammlung(
        trace="Sos Em",
        groups="Lautschrift|Sos Em",
        kreis="Sos",
        ort="Em",
    )
    LAUT_SOS_EN = Sammlung(
        trace="Sos En",
        groups="Lautschrift|Sos En",
        kreis="Sos",
        ort="En",
    )
    LAUT_SOS_EO = Sammlung(
        trace="Sos Eo",
        groups="Lautschrift|Sos Eo",
        kreis="Sos",
        ort="Eo",
    )
    LAUT_SOS_EP = Sammlung(
        trace="Sos Ep",
        groups="Lautschrift|Sos Ep",
        kreis="Sos",
        ort="Ep",
    )
    LAUT_SOS_FL = Sammlung(
        trace="Sos Fl",
        groups="Lautschrift|Sos Fl",
        kreis="Sos",
        ort="Fl",
    )
    LAUT_SOS_GA = Sammlung(
        trace="Sos Ga",
        groups="Lautschrift|Sos Ga",
        kreis="Sos",
        ort="Ga",
    )
    LAUT_SOS_GÜ = Sammlung(
        trace="Sos Gü",
        groups="Lautschrift|Sos Gü",
        kreis="Sos",
        ort="Gü",
    )
    LAUT_SOS_HA = Sammlung(
        trace="Sos Ha",
        groups="Lautschrift|Sos Ha",
        kreis="Sos",
        ort="Ha",
    )
    LAUT_SOS_HE = Sammlung(
        trace="Sos He",
        groups="Lautschrift|Sos He",
        kreis="Sos",
        ort="He",
    )
    LAUT_SOS_HH = Sammlung(
        trace="Sos Hh",
        groups="Lautschrift|Sos Hh",
        kreis="Sos",
        ort="Hh",
    )
    LAUT_SOS_HI = Sammlung(
        trace="Sos Hi",
        groups="Lautschrift|Sos Hi",
        kreis="Sos",
        ort="Hi",
    )
    LAUT_SOS_HN = Sammlung(
        trace="Sos Hn",
        groups="Lautschrift|Sos Hn",
        kreis="Sos",
        ort="Hn",
    )
    LAUT_SOS_HO = Sammlung(
        trace="Sos Ho",
        groups="Lautschrift|Sos Ho",
        kreis="Sos",
        ort="Ho",
    )
    LAUT_SOS_HÖ = Sammlung(
        trace="Sos Hö",
        groups="Lautschrift|Sos Hö",
        kreis="Sos",
        ort="Hö",
    )
    LAUT_SOS_HP = Sammlung(
        trace="Sos Hp",
        groups="Lautschrift|Sos Hp",
        kreis="Sos",
        ort="Hp",
    )
    LAUT_SOS_HT = Sammlung(
        trace="Sos Ht",
        groups="Lautschrift|Sos Ht",
        kreis="Sos",
        ort="Ht",
    )
    LAUT_SOS_HU = Sammlung(
        trace="Sos Hu",
        groups="Lautschrift|Sos Hu",
        kreis="Sos",
        ort="Hu",
    )
    LAUT_SOS_IL = Sammlung(
        trace="Sos Il",
        groups="Lautschrift|Sos Il",
        kreis="Sos",
        ort="Il",
    )
    LAUT_SOS_KA = Sammlung(
        trace="Sos Ka",
        groups="Lautschrift|Sos Ka",
        kreis="Sos",
        ort="Ka",
    )
    LAUT_SOS_KL = Sammlung(
        trace="Sos Kl",
        groups="Lautschrift|Sos Kl",
        kreis="Sos",
        ort="Kl",
    )
    LAUT_SOS_KÖ = Sammlung(
        trace="Sos Kö",
        groups="Lautschrift|Sos Kö",
        kreis="Sos",
        ort="Kö",
    )
    LAUT_SOS_KU = Sammlung(
        trace="Sos Ku",
        groups="Lautschrift|Sos Ku",
        kreis="Sos",
        ort="Ku",
    )
    LAUT_SOS_KW = Sammlung(
        trace="Sos Kw",
        groups="Lautschrift|Sos Kw",
        kreis="Sos",
        ort="Kw",
    )
    LAUT_SOS_LE = Sammlung(
        trace="Sos Le",
        groups="Lautschrift|Sos Le",
        kreis="Sos",
        ort="Le",
    )
    LAUT_SOS_LH = Sammlung(
        trace="Sos Lh",
        groups="Lautschrift|Sos Lh",
        kreis="Sos",
        ort="Lh",
    )
    LAUT_SOS_LO = Sammlung(
        trace="Sos Lo",
        groups="Lautschrift|Sos Lo",
        kreis="Sos",
        ort="Lo",
    )
    LAUT_SOS_LT = Sammlung(
        trace="Sos Lt",
        groups="Lautschrift|Sos Lt",
        kreis="Sos",
        ort="Lt",
    )
    LAUT_SOS_LÜ = Sammlung(
        trace="Sos Lü",
        groups="Lautschrift|Sos Lü",
        kreis="Sos",
        ort="Lü",
    )
    LAUT_SOS_MC = Sammlung(
        trace="Sos Mc",
        groups="Lautschrift|Sos Mc",
        kreis="Sos",
        ort="Mc",
    )
    LAUT_SOS_ME = Sammlung(
        trace="Sos Me",
        groups="Lautschrift|Sos Me",
        kreis="Sos",
        ort="Me",
    )
    LAUT_SOS_ML = Sammlung(
        trace="Sos Ml",
        groups="Lautschrift|Sos Ml",
        kreis="Sos",
        ort="Ml",
    )
    LAUT_SOS_MÜ = Sammlung(
        trace="Sos Mü",
        groups="Lautschrift|Sos Mü",
        kreis="Sos",
        ort="Mü",
    )
    LAUT_SOS_MY = Sammlung(
        trace="Sos My",
        groups="Lautschrift|Sos My",
        kreis="Sos",
        ort="My",
    )
    LAUT_SOS_NA = Sammlung(
        trace="Sos Na",
        groups="Lautschrift|Sos Na",
        kreis="Sos",
        ort="Na",
    )
    LAUT_SOS_NB = Sammlung(
        trace="Sos Nb",
        groups="Lautschrift|Sos Nb",
        kreis="Sos",
        ort="Nb",
    )
    LAUT_SOS_ND = Sammlung(
        trace="Sos Nd",
        groups="Lautschrift|Sos Nd",
        kreis="Sos",
        ort="Nd",
    )
    LAUT_SOS_NE = Sammlung(
        trace="Sos Ne",
        groups="Lautschrift|Sos Ne",
        kreis="Sos",
        ort="Ne",
    )
    LAUT_SOS_NG = Sammlung(
        trace="Sos Ng",
        groups="Lautschrift|Sos Ng",
        kreis="Sos",
        ort="Ng",
    )
    LAUT_SOS_NW = Sammlung(
        trace="Sos Nw",
        groups="Lautschrift|Sos Nw",
        kreis="Sos",
        ort="Nw",
    )
    LAUT_SOS_OB = Sammlung(
        trace="Sos Ob",
        groups="Lautschrift|Sos Ob",
        kreis="Sos",
        ort="Ob",
    )
    LAUT_SOS_OH = Sammlung(
        trace="Sos Oh",
        groups="Lautschrift|Sos Oh",
        kreis="Sos",
        ort="Oh",
    )
    LAUT_SOS_ÖH = Sammlung(
        trace="Sos Öh",
        groups="Lautschrift|Sos Öh",
        kreis="Sos",
        ort="Öh",
    )
    LAUT_SOS_OÖ = Sammlung(
        trace="Sos Oö",
        groups="Lautschrift|Sos Oö",
        kreis="Sos",
        ort="Oö",
    )
    LAUT_SOS_OP = Sammlung(
        trace="Sos Op",
        groups="Lautschrift|Sos Op",
        kreis="Sos",
        ort="Op",
    )
    LAUT_SOS_PA = Sammlung(
        trace="Sos Pa",
        groups="Lautschrift|Sos Pa",
        kreis="Sos",
        ort="Pa",
    )
    LAUT_SOS_RE = Sammlung(
        trace="Sos Re",
        groups="Lautschrift|Sos Re",
        kreis="Sos",
        ort="Re",
    )
    LAUT_SOS_RL = Sammlung(
        trace="Sos Rl",
        groups="Lautschrift|Sos Rl",
        kreis="Sos",
        ort="Rl",
    )
    LAUT_SOS_RÖ = Sammlung(
        trace="Sos Rö",
        groups="Lautschrift|Sos Rö",
        kreis="Sos",
        ort="Rö",
    )
    LAUT_SOS_RU = Sammlung(
        trace="Sos Ru",
        groups="Lautschrift|Sos Ru",
        kreis="Sos",
        ort="Ru",
    )
    LAUT_SOS_SB = Sammlung(
        trace="Sos Sb",
        groups="Lautschrift|Sos Sb",
        kreis="Sos",
        ort="Sb",
    )
    LAUT_SOS_SC = Sammlung(
        trace="Sos Sc",
        groups="Lautschrift|Sos Sc",
        kreis="Sos",
        ort="Sc",
    )
    LAUT_SOS_SD = Sammlung(
        trace="Sos Sd",
        groups="Lautschrift|Sos Sd",
        kreis="Sos",
        ort="Sd",
    )
    LAUT_SOS_SI = Sammlung(
        trace="Sos Si",
        groups="Lautschrift|Sos Si",
        kreis="Sos",
        ort="Si",
    )
    LAUT_SOS_SK = Sammlung(
        trace="Sos Sk",
        groups="Lautschrift|Sos Sk",
        kreis="Sos",
        ort="Sk",
    )
    LAUT_SOS_SL = Sammlung(
        trace="Sos Sl",
        groups="Lautschrift|Sos Sl",
        kreis="Sos",
        ort="Sl",
    )
    LAUT_SOS_SO = Sammlung(
        trace="Sos So",
        groups="Lautschrift|Sos So",
        kreis="Sos",
        ort="So",
    )
    LAUT_SOS_ST = Sammlung(
        trace="Sos St",
        groups="Lautschrift|Sos St",
        kreis="Sos",
        ort="St",
    )
    LAUT_SOS_SW = Sammlung(
        trace="Sos Sw",
        groups="Lautschrift|Sos Sw",
        kreis="Sos",
        ort="Sw",
    )
    LAUT_SOS_TH = Sammlung(
        trace="Sos Th",
        groups="Lautschrift|Sos Th",
        kreis="Sos",
        ort="Th",
    )
    LAUT_SOS_TÖ = Sammlung(
        trace="Sos Tö",
        groups="Lautschrift|Sos Tö",
        kreis="Sos",
        ort="Tö",
    )
    LAUT_SOS_VE = Sammlung(
        trace="Sos Ve",
        groups="Lautschrift|Sos Ve",
        kreis="Sos",
        ort="Ve",
    )
    LAUT_SOS_VÖ = Sammlung(
        trace="Sos Vö",
        groups="Lautschrift|Sos Vö",
        kreis="Sos",
        ort="Vö",
    )
    LAUT_SOS_WA = Sammlung(
        trace="Sos Wa",
        groups="Lautschrift|Sos Wa",
        kreis="Sos",
        ort="Wa",
    )
    LAUT_SOS_WB = Sammlung(
        trace="Sos Wb",
        groups="Lautschrift|Sos Wb",
        kreis="Sos",
        ort="Wb",
    )
    LAUT_SOS_WD = Sammlung(
        trace="Sos Wd",
        groups="Lautschrift|Sos Wd",
        kreis="Sos",
        ort="Wd",
    )
    LAUT_SOS_WE = Sammlung(
        trace="Sos We",
        groups="Lautschrift|Sos We",
        kreis="Sos",
        ort="We",
    )
    LAUT_SOS_WH = Sammlung(
        trace="Sos Wh",
        groups="Lautschrift|Sos Wh",
        kreis="Sos",
        ort="Wh",
    )
    LAUT_SOS_WI = Sammlung(
        trace="Sos Wi",
        groups="Lautschrift|Sos Wi",
        kreis="Sos",
        ort="Wi",
    )
    LAUT_SOS_WL = Sammlung(
        trace="Sos Wl",
        groups="Lautschrift|Sos Wl",
        kreis="Sos",
        ort="Wl",
    )
    LAUT_SOS_WÖ = Sammlung(
        trace="Sos Wö",
        groups="Lautschrift|Sos Wö",
        kreis="Sos",
        ort="Wö",
    )
    LAUT_SOS_WP = Sammlung(
        trace="Sos Wp",
        groups="Lautschrift|Sos Wp",
        kreis="Sos",
        ort="Wp",
    )
    LAUT_SOS_WV = Sammlung(
        trace="Sos Wv",
        groups="Lautschrift|Sos Wv",
        kreis="Sos",
        ort="Wv",
    )
    LAUT_STF_AB = Sammlung(
        trace="Stf Ab",
        groups="Lautschrift|Stf Ab",
        kreis="Stf",
        ort="Ab",
    )
    LAUT_STF_AR = Sammlung(
        trace="Stf Ar",
        groups="Lautschrift|Stf Ar",
        kreis="Stf",
        ort="Ar",
    )
    LAUT_STF_BO = Sammlung(
        trace="Stf Bo",
        groups="Lautschrift|Stf Bo",
        kreis="Stf",
        ort="Bo",
    )
    LAUT_STF_BU = Sammlung(
        trace="Stf Bu",
        groups="Lautschrift|Stf Bu",
        kreis="Stf",
        ort="Bu",
    )
    LAUT_STF_DU = Sammlung(
        trace="Stf Du",
        groups="Lautschrift|Stf Du",
        kreis="Stf",
        ort="Du",
    )
    LAUT_STF_EL = Sammlung(
        trace="Stf El",
        groups="Lautschrift|Stf El",
        kreis="Stf",
        ort="El",
    )
    LAUT_STF_EM = Sammlung(
        trace="Stf Em",
        groups="Lautschrift|Stf Em",
        kreis="Stf",
        ort="Em",
    )
    LAUT_STF_HA = Sammlung(
        trace="Stf Ha",
        groups="Lautschrift|Stf Ha",
        kreis="Stf",
        ort="Ha",
    )
    LAUT_STF_HB = Sammlung(
        trace="Stf Hb",
        groups="Lautschrift|Stf Hb",
        kreis="Stf",
        ort="Hb",
    )
    LAUT_STF_HH = Sammlung(
        trace="Stf Hh",
        groups="Lautschrift|Stf Hh",
        kreis="Stf",
        ort="Hh",
    )
    LAUT_STF_HL = Sammlung(
        trace="Stf Hl",
        groups="Lautschrift|Stf Hl",
        kreis="Stf",
        ort="Hl",
    )
    LAUT_STF_HO = Sammlung(
        trace="Stf Ho",
        groups="Lautschrift|Stf Ho",
        kreis="Stf",
        ort="Ho",
    )
    LAUT_STF_KA = Sammlung(
        trace="Stf Ka",
        groups="Lautschrift|Stf Ka",
        kreis="Stf",
        ort="Ka",
    )
    LAUT_STF_LA = Sammlung(
        trace="Stf La",
        groups="Lautschrift|Stf La",
        kreis="Stf",
        ort="La",
    )
    LAUT_STF_LE = Sammlung(
        trace="Stf Le",
        groups="Lautschrift|Stf Le",
        kreis="Stf",
        ort="Le",
    )
    LAUT_STF_LH = Sammlung(
        trace="Stf Lh",
        groups="Lautschrift|Stf Lh",
        kreis="Stf",
        ort="Lh",
    )
    LAUT_STF_LS = Sammlung(
        trace="Stf Ls",
        groups="Lautschrift|Stf Ls",
        kreis="Stf",
        ort="Ls",
    )
    LAUT_STF_ME = Sammlung(
        trace="Stf Me",
        groups="Lautschrift|Stf Me",
        kreis="Stf",
        ort="Me",
    )
    LAUT_STF_MS = Sammlung(
        trace="Stf Ms",
        groups="Lautschrift|Stf Ms",
        kreis="Stf",
        ort="Ms",
    )
    LAUT_STF_NK = Sammlung(
        trace="Stf Nk",
        groups="Lautschrift|Stf Nk",
        kreis="Stf",
        ort="Nk",
    )
    LAUT_STF_NW = Sammlung(
        trace="Stf Nw",
        groups="Lautschrift|Stf Nw",
        kreis="Stf",
        ort="Nw",
    )
    LAUT_STF_OC = Sammlung(
        trace="Stf Oc",
        groups="Lautschrift|Stf Oc",
        kreis="Stf",
        ort="Oc",
    )
    LAUT_STF_RH = Sammlung(
        trace="Stf Rh",
        groups="Lautschrift|Stf Rh",
        kreis="Stf",
        ort="Rh",
    )
    LAUT_STF_RO = Sammlung(
        trace="Stf Ro",
        groups="Lautschrift|Stf Ro",
        kreis="Stf",
        ort="Ro",
    )
    LAUT_STF_SE = Sammlung(
        trace="Stf Se",
        groups="Lautschrift|Stf Se",
        kreis="Stf",
        ort="Se",
    )
    LAUT_STF_VE = Sammlung(
        trace="Stf Ve",
        groups="Lautschrift|Stf Ve",
        kreis="Stf",
        ort="Ve",
    )
    LAUT_STF_WB = Sammlung(
        trace="Stf Wb",
        groups="Lautschrift|Stf Wb",
        kreis="Stf",
        ort="Wb",
    )
    LAUT_STF_WH = Sammlung(
        trace="Stf Wh",
        groups="Lautschrift|Stf Wh",
        kreis="Stf",
        ort="Wh",
    )
    LAUT_STF_WT = Sammlung(
        trace="Stf Wt",
        groups="Lautschrift|Stf Wt",
        kreis="Stf",
        ort="Wt",
    )
    LAUT_STH_EN = Sammlung(
        trace="Sth En",
        groups="Lautschrift|Sth En",
        kreis="Sth",
        ort="En",
    )
    LAUT_STH_GH = Sammlung(
        trace="Sth Gh",
        groups="Lautschrift|Sth Gh",
        kreis="Sth",
        ort="Gh",
    )
    LAUT_STH_HB = Sammlung(
        trace="Sth Hb",
        groups="Lautschrift|Sth Hb",
        kreis="Sth",
        ort="Hb",
    )
    LAUT_STH_HH = Sammlung(
        trace="Sth Hh",
        groups="Lautschrift|Sth Hh",
        kreis="Sth",
        ort="Hh",
    )
    LAUT_STH_HS = Sammlung(
        trace="Sth Hs",
        groups="Lautschrift|Sth Hs",
        kreis="Sth",
        ort="Hs",
    )
    LAUT_STH_LA = Sammlung(
        trace="Sth La",
        groups="Lautschrift|Sth La",
        kreis="Sth",
        ort="La",
    )
    LAUT_STH_LF = Sammlung(
        trace="Sth Lf",
        groups="Lautschrift|Sth Lf",
        kreis="Sth",
        ort="Lf",
    )
    LAUT_STH_LH = Sammlung(
        trace="Sth Lh",
        groups="Lautschrift|Sth Lh",
        kreis="Sth",
        ort="Lh",
    )
    LAUT_STH_MB = Sammlung(
        trace="Sth Mb",
        groups="Lautschrift|Sth Mb",
        kreis="Sth",
        ort="Mb",
    )
    LAUT_STH_NB = Sammlung(
        trace="Sth Nb",
        groups="Lautschrift|Sth Nb",
        kreis="Sth",
        ort="Nb",
    )
    LAUT_STH_NH = Sammlung(
        trace="Sth Nh",
        groups="Lautschrift|Sth Nh",
        kreis="Sth",
        ort="Nh",
    )
    LAUT_STH_NI = Sammlung(
        trace="Sth Ni",
        groups="Lautschrift|Sth Ni",
        kreis="Sth",
        ort="Ni",
    )
    LAUT_STH_NO = Sammlung(
        trace="Sth No",
        groups="Lautschrift|Sth No",
        kreis="Sth",
        ort="No",
    )
    LAUT_STH_NW = Sammlung(
        trace="Sth Nw",
        groups="Lautschrift|Sth Nw",
        kreis="Sth",
        ort="Nw",
    )
    LAUT_STH_OB = Sammlung(
        trace="Sth Ob",
        groups="Lautschrift|Sth Ob",
        kreis="Sth",
        ort="Ob",
    )
    LAUT_STH_PH = Sammlung(
        trace="Sth Ph",
        groups="Lautschrift|Sth Ph",
        kreis="Sth",
        ort="Ph",
    )
    LAUT_STH_PO = Sammlung(
        trace="Sth Po",
        groups="Lautschrift|Sth Po",
        kreis="Sth",
        ort="Po",
    )
    LAUT_STH_SH = Sammlung(
        trace="Sth Sh",
        groups="Lautschrift|Sth Sh",
        kreis="Sth",
        ort="Sh",
    )
    LAUT_STH_ST = Sammlung(
        trace="Sth St",
        groups="Lautschrift|Sth St",
        kreis="Sth",
        ort="St",
    )
    LAUT_STH_SÜ = Sammlung(
        trace="Sth Sü",
        groups="Lautschrift|Sth Sü",
        kreis="Sth",
        ort="Sü",
    )
    LAUT_STH_VO = Sammlung(
        trace="Sth Vo",
        groups="Lautschrift|Sth Vo",
        kreis="Sth",
        ort="Vo",
    )
    LAUT_STH_WH = Sammlung(
        trace="Sth Wh",
        groups="Lautschrift|Sth Wh",
        kreis="Sth",
        ort="Wh",
    )
    LAUT_STH_WI = Sammlung(
        trace="Sth Wi",
        groups="Lautschrift|Sth Wi",
        kreis="Sth",
        ort="Wi",
    )
    LAUT_STH_WÖ = Sammlung(
        trace="Sth Wö",
        groups="Lautschrift|Sth Wö",
        kreis="Sth",
        ort="Wö",
    )
    LAUT_TEK_AD = Sammlung(
        trace="Tek Ad",
        groups="Lautschrift|Tek Ad",
        kreis="Tek",
        ort="Ad",
    )
    LAUT_TEK_AL = Sammlung(
        trace="Tek Al",
        groups="Lautschrift|Tek Al",
        kreis="Tek",
        ort="Al",
    )
    LAUT_TEK_BB = Sammlung(
        trace="Tek Bb",
        groups="Lautschrift|Tek Bb",
        kreis="Tek",
        ort="Bb",
    )
    LAUT_TEK_BC = Sammlung(
        trace="Tek Bc",
        groups="Lautschrift|Tek Bc",
        kreis="Tek",
        ort="Bc",
    )
    LAUT_TEK_BE = Sammlung(
        trace="Tek Be",
        groups="Lautschrift|Tek Be",
        kreis="Tek",
        ort="Be",
    )
    LAUT_TEK_BI = Sammlung(
        trace="Tek Bi",
        groups="Lautschrift|Tek Bi",
        kreis="Tek",
        ort="Bi",
    )
    LAUT_TEK_BO = Sammlung(
        trace="Tek Bo",
        groups="Lautschrift|Tek Bo",
        kreis="Tek",
        ort="Bo",
    )
    LAUT_TEK_BR = Sammlung(
        trace="Tek Br",
        groups="Lautschrift|Tek Br",
        kreis="Tek",
        ort="Br",
    )
    LAUT_TEK_BÜ = Sammlung(
        trace="Tek Bü",
        groups="Lautschrift|Tek Bü",
        kreis="Tek",
        ort="Bü",
    )
    LAUT_TEK_DL = Sammlung(
        trace="Tek Dl",
        groups="Lautschrift|Tek Dl",
        kreis="Tek",
        ort="Dl",
    )
    LAUT_TEK_DÖ = Sammlung(
        trace="Tek Dö",
        groups="Lautschrift|Tek Dö",
        kreis="Tek",
        ort="Dö",
    )
    LAUT_TEK_DR = Sammlung(
        trace="Tek Dr",
        groups="Lautschrift|Tek Dr",
        kreis="Tek",
        ort="Dr",
    )
    LAUT_TEK_GH = Sammlung(
        trace="Tek Gh",
        groups="Lautschrift|Tek Gh",
        kreis="Tek",
        ort="Gh",
    )
    LAUT_TEK_HA = Sammlung(
        trace="Tek Ha",
        groups="Lautschrift|Tek Ha",
        kreis="Tek",
        ort="Ha",
    )
    LAUT_TEK_HB = Sammlung(
        trace="Tek Hb",
        groups="Lautschrift|Tek Hb",
        kreis="Tek",
        ort="Hb",
    )
    LAUT_TEK_HD = Sammlung(
        trace="Tek Hd",
        groups="Lautschrift|Tek Hd",
        kreis="Tek",
        ort="Hd",
    )
    LAUT_TEK_HF = Sammlung(
        trace="Tek Hf",
        groups="Lautschrift|Tek Hf",
        kreis="Tek",
        ort="Hf",
    )
    LAUT_TEK_HH = Sammlung(
        trace="Tek Hh",
        groups="Lautschrift|Tek Hh",
        kreis="Tek",
        ort="Hh",
    )
    LAUT_TEK_HO = Sammlung(
        trace="Tek Ho",
        groups="Lautschrift|Tek Ho",
        kreis="Tek",
        ort="Ho",
    )
    LAUT_TEK_HÖ = Sammlung(
        trace="Tek Hö",
        groups="Lautschrift|Tek Hö",
        kreis="Tek",
        ort="Hö",
    )
    LAUT_TEK_HP = Sammlung(
        trace="Tek Hp",
        groups="Lautschrift|Tek Hp",
        kreis="Tek",
        ort="Hp",
    )
    LAUT_TEK_HT = Sammlung(
        trace="Tek Ht",
        groups="Lautschrift|Tek Ht",
        kreis="Tek",
        ort="Ht",
    )
    LAUT_TEK_HV = Sammlung(
        trace="Tek Hv",
        groups="Lautschrift|Tek Hv",
        kreis="Tek",
        ort="Hv",
    )
    LAUT_TEK_IB = Sammlung(
        trace="Tek Ib",
        groups="Lautschrift|Tek Ib",
        kreis="Tek",
        ort="Ib",
    )
    LAUT_TEK_KV = Sammlung(
        trace="Tek Kv",
        groups="Lautschrift|Tek Kv",
        kreis="Tek",
        ort="Kv",
    )
    LAUT_TEK_LA = Sammlung(
        trace="Tek La",
        groups="Lautschrift|Tek La",
        kreis="Tek",
        ort="La",
    )
    LAUT_TEK_LB = Sammlung(
        trace="Tek Lb",
        groups="Lautschrift|Tek Lb",
        kreis="Tek",
        ort="Lb",
    )
    LAUT_TEK_LD = Sammlung(
        trace="Tek Ld",
        groups="Lautschrift|Tek Ld",
        kreis="Tek",
        ort="Ld",
    )
    LAUT_TEK_LE = Sammlung(
        trace="Tek Le",
        groups="Lautschrift|Tek Le",
        kreis="Tek",
        ort="Le",
    )
    LAUT_TEK_LH = Sammlung(
        trace="Tek Lh",
        groups="Lautschrift|Tek Lh",
        kreis="Tek",
        ort="Lh",
    )
    LAUT_TEK_LI = Sammlung(
        trace="Tek Li",
        groups="Lautschrift|Tek Li",
        kreis="Tek",
        ort="Li",
    )
    LAUT_TEK_LO = Sammlung(
        trace="Tek Lo",
        groups="Lautschrift|Tek Lo",
        kreis="Tek",
        ort="Lo",
    )
    LAUT_TEK_LT = Sammlung(
        trace="Tek Lt",
        groups="Lautschrift|Tek Lt",
        kreis="Tek",
        ort="Lt",
    )
    LAUT_TEK_LX = Sammlung(
        trace="Tek Lx",
        groups="Lautschrift|Tek Lx",
        kreis="Tek",
        ort="Lx",
    )
    LAUT_TEK_ME = Sammlung(
        trace="Tek Me",
        groups="Lautschrift|Tek Me",
        kreis="Tek",
        ort="Me",
    )
    LAUT_TEK_MT = Sammlung(
        trace="Tek Mt",
        groups="Lautschrift|Tek Mt",
        kreis="Tek",
        ort="Mt",
    )
    LAUT_TEK_MW = Sammlung(
        trace="Tek Mw",
        groups="Lautschrift|Tek Mw",
        kreis="Tek",
        ort="Mw",
    )
    LAUT_TEK_NB = Sammlung(
        trace="Tek Nb",
        groups="Lautschrift|Tek Nb",
        kreis="Tek",
        ort="Nb",
    )
    LAUT_TEK_OB = Sammlung(
        trace="Tek Ob",
        groups="Lautschrift|Tek Ob",
        kreis="Tek",
        ort="Ob",
    )
    LAUT_TEK_OL = Sammlung(
        trace="Tek Ol",
        groups="Lautschrift|Tek Ol",
        kreis="Tek",
        ort="Ol",
    )
    LAUT_TEK_OR = Sammlung(
        trace="Tek Or",
        groups="Lautschrift|Tek Or",
        kreis="Tek",
        ort="Or",
    )
    LAUT_TEK_OS = Sammlung(
        trace="Tek Os",
        groups="Lautschrift|Tek Os",
        kreis="Tek",
        ort="Os",
    )
    LAUT_TEK_OW = Sammlung(
        trace="Tek Ow",
        groups="Lautschrift|Tek Ow",
        kreis="Tek",
        ort="Ow",
    )
    LAUT_TEK_PÜ = Sammlung(
        trace="Tek Pü",
        groups="Lautschrift|Tek Pü",
        kreis="Tek",
        ort="Pü",
    )
    LAUT_TEK_RB = Sammlung(
        trace="Tek Rb",
        groups="Lautschrift|Tek Rb",
        kreis="Tek",
        ort="Rb",
    )
    LAUT_TEK_RE = Sammlung(
        trace="Tek Re",
        groups="Lautschrift|Tek Re",
        kreis="Tek",
        ort="Re",
    )
    LAUT_TEK_SB = Sammlung(
        trace="Tek Sb",
        groups="Lautschrift|Tek Sb",
        kreis="Tek",
        ort="Sb",
    )
    LAUT_TEK_SC = Sammlung(
        trace="Tek Sc",
        groups="Lautschrift|Tek Sc",
        kreis="Tek",
        ort="Sc",
    )
    LAUT_TEK_SE = Sammlung(
        trace="Tek Se",
        groups="Lautschrift|Tek Se",
        kreis="Tek",
        ort="Se",
    )
    LAUT_TEK_SL = Sammlung(
        trace="Tek Sl",
        groups="Lautschrift|Tek Sl",
        kreis="Tek",
        ort="Sl",
    )
    LAUT_TEK_ST = Sammlung(
        trace="Tek St",
        groups="Lautschrift|Tek St",
        kreis="Tek",
        ort="St",
    )
    LAUT_TEK_TB = Sammlung(
        trace="Tek Tb",
        groups="Lautschrift|Tek Tb",
        kreis="Tek",
        ort="Tb",
    )
    LAUT_TEK_UF = Sammlung(
        trace="Tek Uf",
        groups="Lautschrift|Tek Uf",
        kreis="Tek",
        ort="Uf",
    )
    LAUT_TEK_WE = Sammlung(
        trace="Tek We",
        groups="Lautschrift|Tek We",
        kreis="Tek",
        ort="We",
    )
    LAUT_TEK_WK = Sammlung(
        trace="Tek Wk",
        groups="Lautschrift|Tek Wk",
        kreis="Tek",
        ort="Wk",
    )
    LAUT_TEK_WT = Sammlung(
        trace="Tek Wt",
        groups="Lautschrift|Tek Wt",
        kreis="Tek",
        ort="Wt",
    )
    LAUT_UNN_AB = Sammlung(
        trace="Unn Ab",
        groups="Lautschrift|Unn Ab",
        kreis="Unn",
        ort="Ab",
    )
    LAUT_UNN_AD = Sammlung(
        trace="Unn Ad",
        groups="Lautschrift|Unn Ad",
        kreis="Unn",
        ort="Ad",
    )
    LAUT_UNN_AF = Sammlung(
        trace="Unn Af",
        groups="Lautschrift|Unn Af",
        kreis="Unn",
        ort="Af",
    )
    LAUT_UNN_AH = Sammlung(
        trace="Unn Ah",
        groups="Lautschrift|Unn Ah",
        kreis="Unn",
        ort="Ah",
    )
    LAUT_UNN_AR = Sammlung(
        trace="Unn Ar",
        groups="Lautschrift|Unn Ar",
        kreis="Unn",
        ort="Ar",
    )
    LAUT_UNN_BE = Sammlung(
        trace="Unn Be",
        groups="Lautschrift|Unn Be",
        kreis="Unn",
        ort="Be",
    )
    LAUT_UNN_BI = Sammlung(
        trace="Unn Bi",
        groups="Lautschrift|Unn Bi",
        kreis="Unn",
        ort="Bi",
    )
    LAUT_UNN_BK = Sammlung(
        trace="Unn Bk",
        groups="Lautschrift|Unn Bk",
        kreis="Unn",
        ort="Bk",
    )
    LAUT_UNN_BR = Sammlung(
        trace="Unn Br",
        groups="Lautschrift|Unn Br",
        kreis="Unn",
        ort="Br",
    )
    LAUT_UNN_BT = Sammlung(
        trace="Unn Bt",
        groups="Lautschrift|Unn Bt",
        kreis="Unn",
        ort="Bt",
    )
    LAUT_UNN_DH = Sammlung(
        trace="Unn Dh",
        groups="Lautschrift|Unn Dh",
        kreis="Unn",
        ort="Dh",
    )
    LAUT_UNN_DL = Sammlung(
        trace="Unn Dl",
        groups="Lautschrift|Unn Dl",
        kreis="Unn",
        ort="Dl",
    )
    LAUT_UNN_DW = Sammlung(
        trace="Unn Dw",
        groups="Lautschrift|Unn Dw",
        kreis="Unn",
        ort="Dw",
    )
    LAUT_UNN_FB = Sammlung(
        trace="Unn Fb",
        groups="Lautschrift|Unn Fb",
        kreis="Unn",
        ort="Fb",
    )
    LAUT_UNN_FH = Sammlung(
        trace="Unn Fh",
        groups="Lautschrift|Unn Fh",
        kreis="Unn",
        ort="Fh",
    )
    LAUT_UNN_FL = Sammlung(
        trace="Unn Fl",
        groups="Lautschrift|Unn Fl",
        kreis="Unn",
        ort="Fl",
    )
    LAUT_UNN_FR = Sammlung(
        trace="Unn Fr",
        groups="Lautschrift|Unn Fr",
        kreis="Unn",
        ort="Fr",
    )
    LAUT_UNN_HA = Sammlung(
        trace="Unn Ha",
        groups="Lautschrift|Unn Ha",
        kreis="Unn",
        ort="Ha",
    )
    LAUT_UNN_HD = Sammlung(
        trace="Unn Hd",
        groups="Lautschrift|Unn Hd",
        kreis="Unn",
        ort="Hd",
    )
    LAUT_UNN_HE = Sammlung(
        trace="Unn He",
        groups="Lautschrift|Unn He",
        kreis="Unn",
        ort="He",
    )
    LAUT_UNN_HH = Sammlung(
        trace="Unn Hh",
        groups="Lautschrift|Unn Hh",
        kreis="Unn",
        ort="Hh",
    )
    LAUT_UNN_HI = Sammlung(
        trace="Unn Hi",
        groups="Lautschrift|Unn Hi",
        kreis="Unn",
        ort="Hi",
    )
    LAUT_UNN_HM = Sammlung(
        trace="Unn Hm",
        groups="Lautschrift|Unn Hm",
        kreis="Unn",
        ort="Hm",
    )
    LAUT_UNN_HN = Sammlung(
        trace="Unn Hn",
        groups="Lautschrift|Unn Hn",
        kreis="Unn",
        ort="Hn",
    )
    LAUT_UNN_HO = Sammlung(
        trace="Unn Ho",
        groups="Lautschrift|Unn Ho",
        kreis="Unn",
        ort="Ho",
    )
    LAUT_UNN_HR = Sammlung(
        trace="Unn Hr",
        groups="Lautschrift|Unn Hr",
        kreis="Unn",
        ort="Hr",
    )
    LAUT_UNN_HW = Sammlung(
        trace="Unn Hw",
        groups="Lautschrift|Unn Hw",
        kreis="Unn",
        ort="Hw",
    )
    LAUT_UNN_HX = Sammlung(
        trace="Unn Hx",
        groups="Lautschrift|Unn Hx",
        kreis="Unn",
        ort="Hx",
    )
    LAUT_UNN_KA = Sammlung(
        trace="Unn Ka",
        groups="Lautschrift|Unn Ka",
        kreis="Unn",
        ort="Ka",
    )
    LAUT_UNN_KB = Sammlung(
        trace="Unn Kb",
        groups="Lautschrift|Unn Kb",
        kreis="Unn",
        ort="Kb",
    )
    LAUT_UNN_LA = Sammlung(
        trace="Unn La",
        groups="Lautschrift|Unn La",
        kreis="Unn",
        ort="La",
    )
    LAUT_UNN_LE = Sammlung(
        trace="Unn Le",
        groups="Lautschrift|Unn Le",
        kreis="Unn",
        ort="Le",
    )
    LAUT_UNN_LN = Sammlung(
        trace="Unn Ln",
        groups="Lautschrift|Unn Ln",
        kreis="Unn",
        ort="Ln",
    )
    LAUT_UNN_LÜ = Sammlung(
        trace="Unn Lü",
        groups="Lautschrift|Unn Lü",
        kreis="Unn",
        ort="Lü",
    )
    LAUT_UNN_MA = Sammlung(
        trace="Unn Ma",
        groups="Lautschrift|Unn Ma",
        kreis="Unn",
        ort="Ma",
    )
    LAUT_UNN_ME = Sammlung(
        trace="Unn Me",
        groups="Lautschrift|Unn Me",
        kreis="Unn",
        ort="Me",
    )
    LAUT_UNN_MH = Sammlung(
        trace="Unn Mh",
        groups="Lautschrift|Unn Mh",
        kreis="Unn",
        ort="Mh",
    )
    LAUT_UNN_MS = Sammlung(
        trace="Unn Ms",
        groups="Lautschrift|Unn Ms",
        kreis="Unn",
        ort="Ms",
    )
    LAUT_UNN_NB = Sammlung(
        trace="Unn Nb",
        groups="Lautschrift|Unn Nb",
        kreis="Unn",
        ort="Nb",
    )
    LAUT_UNN_ND = Sammlung(
        trace="Unn Nd",
        groups="Lautschrift|Unn Nd",
        kreis="Unn",
        ort="Nd",
    )
    LAUT_UNN_NI = Sammlung(
        trace="Unn Ni",
        groups="Lautschrift|Unn Ni",
        kreis="Unn",
        ort="Ni",
    )
    LAUT_UNN_NM = Sammlung(
        trace="Unn Nm",
        groups="Lautschrift|Unn Nm",
        kreis="Unn",
        ort="Nm",
    )
    LAUT_UNN_OA = Sammlung(
        trace="Unn Oa",
        groups="Lautschrift|Unn Oa",
        kreis="Unn",
        ort="Oa",
    )
    LAUT_UNN_OB = Sammlung(
        trace="Unn Ob",
        groups="Lautschrift|Unn Ob",
        kreis="Unn",
        ort="Ob",
    )
    LAUT_UNN_OF = Sammlung(
        trace="Unn Of",
        groups="Lautschrift|Unn Of",
        kreis="Unn",
        ort="Of",
    )
    LAUT_UNN_OH = Sammlung(
        trace="Unn Oh",
        groups="Lautschrift|Unn Oh",
        kreis="Unn",
        ort="Oh",
    )
    LAUT_UNN_OÖ = Sammlung(
        trace="Unn Oö",
        groups="Lautschrift|Unn Oö",
        kreis="Unn",
        ort="Oö",
    )
    LAUT_UNN_OT = Sammlung(
        trace="Unn Ot",
        groups="Lautschrift|Unn Ot",
        kreis="Unn",
        ort="Ot",
    )
    LAUT_UNN_OV = Sammlung(
        trace="Unn Ov",
        groups="Lautschrift|Unn Ov",
        kreis="Unn",
        ort="Ov",
    )
    LAUT_UNN_OW = Sammlung(
        trace="Unn Ow",
        groups="Lautschrift|Unn Ow",
        kreis="Unn",
        ort="Ow",
    )
    LAUT_UNN_PE = Sammlung(
        trace="Unn Pe",
        groups="Lautschrift|Unn Pe",
        kreis="Unn",
        ort="Pe",
    )
    LAUT_UNN_RO = Sammlung(
        trace="Unn Ro",
        groups="Lautschrift|Unn Ro",
        kreis="Unn",
        ort="Ro",
    )
    LAUT_UNN_RÜ = Sammlung(
        trace="Unn Rü",
        groups="Lautschrift|Unn Rü",
        kreis="Unn",
        ort="Rü",
    )
    LAUT_UNN_RY = Sammlung(
        trace="Unn Ry",
        groups="Lautschrift|Unn Ry",
        kreis="Unn",
        ort="Ry",
    )
    LAUT_UNN_SB = Sammlung(
        trace="Unn Sb",
        groups="Lautschrift|Unn Sb",
        kreis="Unn",
        ort="Sb",
    )
    LAUT_UNN_SC = Sammlung(
        trace="Unn Sc",
        groups="Lautschrift|Unn Sc",
        kreis="Unn",
        ort="Sc",
    )
    LAUT_UNN_SD = Sammlung(
        trace="Unn Sd",
        groups="Lautschrift|Unn Sd",
        kreis="Unn",
        ort="Sd",
    )
    LAUT_UNN_SI = Sammlung(
        trace="Unn Si",
        groups="Lautschrift|Unn Si",
        kreis="Unn",
        ort="Si",
    )
    LAUT_UNN_SK = Sammlung(
        trace="Unn Sk",
        groups="Lautschrift|Unn Sk",
        kreis="Unn",
        ort="Sk",
    )
    LAUT_UNN_SÖ = Sammlung(
        trace="Unn Sö",
        groups="Lautschrift|Unn Sö",
        kreis="Unn",
        ort="Sö",
    )
    LAUT_UNN_ST = Sammlung(
        trace="Unn St",
        groups="Lautschrift|Unn St",
        kreis="Unn",
        ort="St",
    )
    LAUT_UNN_SÜ = Sammlung(
        trace="Unn Sü",
        groups="Lautschrift|Unn Sü",
        kreis="Unn",
        ort="Sü",
    )
    LAUT_UNN_ÜL = Sammlung(
        trace="Unn Ül",
        groups="Lautschrift|Unn Ül",
        kreis="Unn",
        ort="Ül",
    )
    LAUT_UNN_UN = Sammlung(
        trace="Unn Un",
        groups="Lautschrift|Unn Un",
        kreis="Unn",
        ort="Un",
    )
    LAUT_UNN_ÜN = Sammlung(
        trace="Unn Ün",
        groups="Lautschrift|Unn Ün",
        kreis="Unn",
        ort="Ün",
    )
    LAUT_UNN_VÖ = Sammlung(
        trace="Unn Vö",
        groups="Lautschrift|Unn Vö",
        kreis="Unn",
        ort="Vö",
    )
    LAUT_UNN_WB = Sammlung(
        trace="Unn Wb",
        groups="Lautschrift|Unn Wb",
        kreis="Unn",
        ort="Wb",
    )
    LAUT_UNN_WD = Sammlung(
        trace="Unn Wd",
        groups="Lautschrift|Unn Wd",
        kreis="Unn",
        ort="Wd",
    )
    LAUT_UNN_WE = Sammlung(
        trace="Unn We",
        groups="Lautschrift|Unn We",
        kreis="Unn",
        ort="We",
    )
    LAUT_UNN_WH = Sammlung(
        trace="Unn Wh",
        groups="Lautschrift|Unn Wh",
        kreis="Unn",
        ort="Wh",
    )
    LAUT_UNN_WK = Sammlung(
        trace="Unn Wk",
        groups="Lautschrift|Unn Wk",
        kreis="Unn",
        ort="Wk",
    )
    LAUT_UNN_WR = Sammlung(
        trace="Unn Wr",
        groups="Lautschrift|Unn Wr",
        kreis="Unn",
        ort="Wr",
    )
    LAUT_UNN_WS = Sammlung(
        trace="Unn Ws",
        groups="Lautschrift|Unn Ws",
        kreis="Unn",
        ort="Ws",
    )
    LAUT_VCH_AB = Sammlung(
        trace="Vch Ab",
        groups="Lautschrift|Vch Ab",
        kreis="Vch",
        ort="Ab",
    )
    LAUT_VCH_AS = Sammlung(
        trace="Vch As",
        groups="Lautschrift|Vch As",
        kreis="Vch",
        ort="As",
    )
    LAUT_VCH_BA = Sammlung(
        trace="Vch Ba",
        groups="Lautschrift|Vch Ba",
        kreis="Vch",
        ort="Ba",
    )
    LAUT_VCH_BF = Sammlung(
        trace="Vch Bf",
        groups="Lautschrift|Vch Bf",
        kreis="Vch",
        ort="Bf",
    )
    LAUT_VCH_BH = Sammlung(
        trace="Vch Bh",
        groups="Lautschrift|Vch Bh",
        kreis="Vch",
        ort="Bh",
    )
    LAUT_VCH_BI = Sammlung(
        trace="Vch Bi",
        groups="Lautschrift|Vch Bi",
        kreis="Vch",
        ort="Bi",
    )
    LAUT_VCH_BK = Sammlung(
        trace="Vch Bk",
        groups="Lautschrift|Vch Bk",
        kreis="Vch",
        ort="Bk",
    )
    LAUT_VCH_BL = Sammlung(
        trace="Vch Bl",
        groups="Lautschrift|Vch Bl",
        kreis="Vch",
        ort="Bl",
    )
    LAUT_VCH_BO = Sammlung(
        trace="Vch Bo",
        groups="Lautschrift|Vch Bo",
        kreis="Vch",
        ort="Bo",
    )
    LAUT_VCH_BR = Sammlung(
        trace="Vch Br",
        groups="Lautschrift|Vch Br",
        kreis="Vch",
        ort="Br",
    )
    LAUT_VCH_DA = Sammlung(
        trace="Vch Da",
        groups="Lautschrift|Vch Da",
        kreis="Vch",
        ort="Da",
    )
    LAUT_VCH_DD = Sammlung(
        trace="Vch Dd",
        groups="Lautschrift|Vch Dd",
        kreis="Vch",
        ort="Dd",
    )
    LAUT_VCH_DL = Sammlung(
        trace="Vch Dl",
        groups="Lautschrift|Vch Dl",
        kreis="Vch",
        ort="Dl",
    )
    LAUT_VCH_DÜ = Sammlung(
        trace="Vch Dü",
        groups="Lautschrift|Vch Dü",
        kreis="Vch",
        ort="Dü",
    )
    LAUT_VCH_EI = Sammlung(
        trace="Vch Ei",
        groups="Lautschrift|Vch Ei",
        kreis="Vch",
        ort="Ei",
    )
    LAUT_VCH_EL = Sammlung(
        trace="Vch El",
        groups="Lautschrift|Vch El",
        kreis="Vch",
        ort="El",
    )
    LAUT_VCH_EN = Sammlung(
        trace="Vch En",
        groups="Lautschrift|Vch En",
        kreis="Vch",
        ort="En",
    )
    LAUT_VCH_FL = Sammlung(
        trace="Vch Fl",
        groups="Lautschrift|Vch Fl",
        kreis="Vch",
        ort="Fl",
    )
    LAUT_VCH_GH = Sammlung(
        trace="Vch Gh",
        groups="Lautschrift|Vch Gh",
        kreis="Vch",
        ort="Gh",
    )
    LAUT_VCH_GO = Sammlung(
        trace="Vch Go",
        groups="Lautschrift|Vch Go",
        kreis="Vch",
        ort="Go",
    )
    LAUT_VCH_HA = Sammlung(
        trace="Vch Ha",
        groups="Lautschrift|Vch Ha",
        kreis="Vch",
        ort="Ha",
    )
    LAUT_VCH_HB = Sammlung(
        trace="Vch Hb",
        groups="Lautschrift|Vch Hb",
        kreis="Vch",
        ort="Hb",
    )
    LAUT_VCH_HD = Sammlung(
        trace="Vch Hd",
        groups="Lautschrift|Vch Hd",
        kreis="Vch",
        ort="Hd",
    )
    LAUT_VCH_HG = Sammlung(
        trace="Vch Hg",
        groups="Lautschrift|Vch Hg",
        kreis="Vch",
        ort="Hg",
    )
    LAUT_VCH_HH = Sammlung(
        trace="Vch Hh",
        groups="Lautschrift|Vch Hh",
        kreis="Vch",
        ort="Hh",
    )
    LAUT_VCH_HI = Sammlung(
        trace="Vch Hi",
        groups="Lautschrift|Vch Hi",
        kreis="Vch",
        ort="Hi",
    )
    LAUT_VCH_HN = Sammlung(
        trace="Vch Hn",
        groups="Lautschrift|Vch Hn",
        kreis="Vch",
        ort="Hn",
    )
    LAUT_VCH_HO = Sammlung(
        trace="Vch Ho",
        groups="Lautschrift|Vch Ho",
        kreis="Vch",
        ort="Ho",
    )
    LAUT_VCH_HS = Sammlung(
        trace="Vch Hs",
        groups="Lautschrift|Vch Hs",
        kreis="Vch",
        ort="Hs",
    )
    LAUT_VCH_HT = Sammlung(
        trace="Vch Ht",
        groups="Lautschrift|Vch Ht",
        kreis="Vch",
        ort="Ht",
    )
    LAUT_VCH_HX = Sammlung(
        trace="Vch Hx",
        groups="Lautschrift|Vch Hx",
        kreis="Vch",
        ort="Hx",
    )
    LAUT_VCH_IH = Sammlung(
        trace="Vch Ih",
        groups="Lautschrift|Vch Ih",
        kreis="Vch",
        ort="Ih",
    )
    LAUT_VCH_KA = Sammlung(
        trace="Vch Ka",
        groups="Lautschrift|Vch Ka",
        kreis="Vch",
        ort="Ka",
    )
    LAUT_VCH_KF = Sammlung(
        trace="Vch Kf",
        groups="Lautschrift|Vch Kf",
        kreis="Vch",
        ort="Kf",
    )
    LAUT_VCH_KL = Sammlung(
        trace="Vch Kl",
        groups="Lautschrift|Vch Kl",
        kreis="Vch",
        ort="Kl",
    )
    LAUT_VCH_KR = Sammlung(
        trace="Vch Kr",
        groups="Lautschrift|Vch Kr",
        kreis="Vch",
        ort="Kr",
    )
    LAUT_VCH_LD = Sammlung(
        trace="Vch Ld",
        groups="Lautschrift|Vch Ld",
        kreis="Vch",
        ort="Ld",
    )
    LAUT_VCH_LF = Sammlung(
        trace="Vch Lf",
        groups="Lautschrift|Vch Lf",
        kreis="Vch",
        ort="Lf",
    )
    LAUT_VCH_LM = Sammlung(
        trace="Vch Lm",
        groups="Lautschrift|Vch Lm",
        kreis="Vch",
        ort="Lm",
    )
    LAUT_VCH_LO = Sammlung(
        trace="Vch Lo",
        groups="Lautschrift|Vch Lo",
        kreis="Vch",
        ort="Lo",
    )
    LAUT_VCH_LU = Sammlung(
        trace="Vch Lu",
        groups="Lautschrift|Vch Lu",
        kreis="Vch",
        ort="Lu",
    )
    LAUT_VCH_LW = Sammlung(
        trace="Vch Lw",
        groups="Lautschrift|Vch Lw",
        kreis="Vch",
        ort="Lw",
    )
    LAUT_VCH_MD = Sammlung(
        trace="Vch Md",
        groups="Lautschrift|Vch Md",
        kreis="Vch",
        ort="Md",
    )
    LAUT_VCH_MÜ = Sammlung(
        trace="Vch Mü",
        groups="Lautschrift|Vch Mü",
        kreis="Vch",
        ort="Mü",
    )
    LAUT_VCH_ND = Sammlung(
        trace="Vch Nd",
        groups="Lautschrift|Vch Nd",
        kreis="Vch",
        ort="Nd",
    )
    LAUT_VCH_NH = Sammlung(
        trace="Vch Nh",
        groups="Lautschrift|Vch Nh",
        kreis="Vch",
        ort="Nh",
    )
    LAUT_VCH_NK = Sammlung(
        trace="Vch Nk",
        groups="Lautschrift|Vch Nk",
        kreis="Vch",
        ort="Nk",
    )
    LAUT_VCH_NL = Sammlung(
        trace="Vch Nl",
        groups="Lautschrift|Vch Nl",
        kreis="Vch",
        ort="Nl",
    )
    LAUT_VCH_OE = Sammlung(
        trace="Vch Oe",
        groups="Lautschrift|Vch Oe",
        kreis="Vch",
        ort="Oe",
    )
    LAUT_VCH_OF = Sammlung(
        trace="Vch Of",
        groups="Lautschrift|Vch Of",
        kreis="Vch",
        ort="Of",
    )
    LAUT_VCH_OY = Sammlung(
        trace="Vch Oy",
        groups="Lautschrift|Vch Oy",
        kreis="Vch",
        ort="Oy",
    )
    LAUT_VCH_RD = Sammlung(
        trace="Vch Rd",
        groups="Lautschrift|Vch Rd",
        kreis="Vch",
        ort="Rd",
    )
    LAUT_VCH_RF = Sammlung(
        trace="Vch Rf",
        groups="Lautschrift|Vch Rf",
        kreis="Vch",
        ort="Rf",
    )
    LAUT_VCH_SC = Sammlung(
        trace="Vch Sc",
        groups="Lautschrift|Vch Sc",
        kreis="Vch",
        ort="Sc",
    )
    LAUT_VCH_SH = Sammlung(
        trace="Vch Sh",
        groups="Lautschrift|Vch Sh",
        kreis="Vch",
        ort="Sh",
    )
    LAUT_VCH_SL = Sammlung(
        trace="Vch Sl",
        groups="Lautschrift|Vch Sl",
        kreis="Vch",
        ort="Sl",
    )
    LAUT_VCH_ST = Sammlung(
        trace="Vch St",
        groups="Lautschrift|Vch St",
        kreis="Vch",
        ort="St",
    )
    LAUT_VCH_SW = Sammlung(
        trace="Vch Sw",
        groups="Lautschrift|Vch Sw",
        kreis="Vch",
        ort="Sw",
    )
    LAUT_VCH_VA = Sammlung(
        trace="Vch Va",
        groups="Lautschrift|Vch Va",
        kreis="Vch",
        ort="Va",
    )
    LAUT_VCH_VB = Sammlung(
        trace="Vch Vb",
        groups="Lautschrift|Vch Vb",
        kreis="Vch",
        ort="Vb",
    )
    LAUT_VCH_VE = Sammlung(
        trace="Vch Ve",
        groups="Lautschrift|Vch Ve",
        kreis="Vch",
        ort="Ve",
    )
    LAUT_VCH_VH = Sammlung(
        trace="Vch Vh",
        groups="Lautschrift|Vch Vh",
        kreis="Vch",
        ort="Vh",
    )
    LAUT_VCH_VP = Sammlung(
        trace="Vch Vp",
        groups="Lautschrift|Vch Vp",
        kreis="Vch",
        ort="Vp",
    )
    LAUT_VCH_WE = Sammlung(
        trace="Vch We",
        groups="Lautschrift|Vch We",
        kreis="Vch",
        ort="We",
    )
    LAUT_VCH_WÖ = Sammlung(
        trace="Vch Wö",
        groups="Lautschrift|Vch Wö",
        kreis="Vch",
        ort="Wö",
    )
    LAUT_VCH_WU = Sammlung(
        trace="Vch Wu",
        groups="Lautschrift|Vch Wu",
        kreis="Vch",
        ort="Wu",
    )
    LAUT_WAL_AD = Sammlung(
        trace="Wal Ad",
        groups="Lautschrift|Wal Ad",
        kreis="Wal",
        ort="Ad",
    )
    LAUT_WAL_AF = Sammlung(
        trace="Wal Af",
        groups="Lautschrift|Wal Af",
        kreis="Wal",
        ort="Af",
    )
    LAUT_WAL_AL = Sammlung(
        trace="Wal Al",
        groups="Lautschrift|Wal Al",
        kreis="Wal",
        ort="Al",
    )
    LAUT_WAL_AM = Sammlung(
        trace="Wal Am",
        groups="Lautschrift|Wal Am",
        kreis="Wal",
        ort="Am",
    )
    LAUT_WAL_AR = Sammlung(
        trace="Wal Ar",
        groups="Lautschrift|Wal Ar",
        kreis="Wal",
        ort="Ar",
    )
    LAUT_WAL_AS = Sammlung(
        trace="Wal As",
        groups="Lautschrift|Wal As",
        kreis="Wal",
        ort="As",
    )
    LAUT_WAL_BA = Sammlung(
        trace="Wal Ba",
        groups="Lautschrift|Wal Ba",
        kreis="Wal",
        ort="Ba",
    )
    LAUT_WAL_BB = Sammlung(
        trace="Wal Bb",
        groups="Lautschrift|Wal Bb",
        kreis="Wal",
        ort="Bb",
    )
    LAUT_WAL_BD = Sammlung(
        trace="Wal Bd",
        groups="Lautschrift|Wal Bd",
        kreis="Wal",
        ort="Bd",
    )
    LAUT_WAL_BH = Sammlung(
        trace="Wal Bh",
        groups="Lautschrift|Wal Bh",
        kreis="Wal",
        ort="Bh",
    )
    LAUT_WAL_BÖ = Sammlung(
        trace="Wal Bö",
        groups="Lautschrift|Wal Bö",
        kreis="Wal",
        ort="Bö",
    )
    LAUT_WAL_BR = Sammlung(
        trace="Wal Br",
        groups="Lautschrift|Wal Br",
        kreis="Wal",
        ort="Br",
    )
    LAUT_WAL_BÜ = Sammlung(
        trace="Wal Bü",
        groups="Lautschrift|Wal Bü",
        kreis="Wal",
        ort="Bü",
    )
    LAUT_WAL_DE = Sammlung(
        trace="Wal De",
        groups="Lautschrift|Wal De",
        kreis="Wal",
        ort="De",
    )
    LAUT_WAL_DF = Sammlung(
        trace="Wal Df",
        groups="Lautschrift|Wal Df",
        kreis="Wal",
        ort="Df",
    )
    LAUT_WAL_DH = Sammlung(
        trace="Wal Dh",
        groups="Lautschrift|Wal Dh",
        kreis="Wal",
        ort="Dh",
    )
    LAUT_WAL_DI = Sammlung(
        trace="Wal Di",
        groups="Lautschrift|Wal Di",
        kreis="Wal",
        ort="Di",
    )
    LAUT_WAL_DT = Sammlung(
        trace="Wal Dt",
        groups="Lautschrift|Wal Dt",
        kreis="Wal",
        ort="Dt",
    )
    LAUT_WAL_EI = Sammlung(
        trace="Wal Ei",
        groups="Lautschrift|Wal Ei",
        kreis="Wal",
        ort="Ei",
    )
    LAUT_WAL_EL = Sammlung(
        trace="Wal El",
        groups="Lautschrift|Wal El",
        kreis="Wal",
        ort="El",
    )
    LAUT_WAL_EN = Sammlung(
        trace="Wal En",
        groups="Lautschrift|Wal En",
        kreis="Wal",
        ort="En",
    )
    LAUT_WAL_EP = Sammlung(
        trace="Wal Ep",
        groups="Lautschrift|Wal Ep",
        kreis="Wal",
        ort="Ep",
    )
    LAUT_WAL_FB = Sammlung(
        trace="Wal Fb",
        groups="Lautschrift|Wal Fb",
        kreis="Wal",
        ort="Fb",
    )
    LAUT_WAL_FL = Sammlung(
        trace="Wal Fl",
        groups="Lautschrift|Wal Fl",
        kreis="Wal",
        ort="Fl",
    )
    LAUT_WAL_FR = Sammlung(
        trace="Wal Fr",
        groups="Lautschrift|Wal Fr",
        kreis="Wal",
        ort="Fr",
    )
    LAUT_WAL_GB = Sammlung(
        trace="Wal Gb",
        groups="Lautschrift|Wal Gb",
        kreis="Wal",
        ort="Gb",
    )
    LAUT_WAL_GD = Sammlung(
        trace="Wal Gd",
        groups="Lautschrift|Wal Gd",
        kreis="Wal",
        ort="Gd",
    )
    LAUT_WAL_GH = Sammlung(
        trace="Wal Gh",
        groups="Lautschrift|Wal Gh",
        kreis="Wal",
        ort="Gh",
    )
    LAUT_WAL_GI = Sammlung(
        trace="Wal Gi",
        groups="Lautschrift|Wal Gi",
        kreis="Wal",
        ort="Gi",
    )
    LAUT_WAL_HA = Sammlung(
        trace="Wal Ha",
        groups="Lautschrift|Wal Ha",
        kreis="Wal",
        ort="Ha",
    )
    LAUT_WAL_HB = Sammlung(
        trace="Wal Hb",
        groups="Lautschrift|Wal Hb",
        kreis="Wal",
        ort="Hb",
    )
    LAUT_WAL_HE = Sammlung(
        trace="Wal He",
        groups="Lautschrift|Wal He",
        kreis="Wal",
        ort="He",
    )
    LAUT_WAL_HH = Sammlung(
        trace="Wal Hh",
        groups="Lautschrift|Wal Hh",
        kreis="Wal",
        ort="Hh",
    )
    LAUT_WAL_HI = Sammlung(
        trace="Wal Hi",
        groups="Lautschrift|Wal Hi",
        kreis="Wal",
        ort="Hi",
    )
    LAUT_WAL_HM = Sammlung(
        trace="Wal Hm",
        groups="Lautschrift|Wal Hm",
        kreis="Wal",
        ort="Hm",
    )
    LAUT_WAL_HÖ = Sammlung(
        trace="Wal Hö",
        groups="Lautschrift|Wal Hö",
        kreis="Wal",
        ort="Hö",
    )
    LAUT_WAL_HP = Sammlung(
        trace="Wal Hp",
        groups="Lautschrift|Wal Hp",
        kreis="Wal",
        ort="Hp",
    )
    LAUT_WAL_HR = Sammlung(
        trace="Wal Hr",
        groups="Lautschrift|Wal Hr",
        kreis="Wal",
        ort="Hr",
    )
    LAUT_WAL_HS = Sammlung(
        trace="Wal Hs",
        groups="Lautschrift|Wal Hs",
        kreis="Wal",
        ort="Hs",
    )
    LAUT_WAL_HZ = Sammlung(
        trace="Wal Hz",
        groups="Lautschrift|Wal Hz",
        kreis="Wal",
        ort="Hz",
    )
    LAUT_WAL_IM = Sammlung(
        trace="Wal Im",
        groups="Lautschrift|Wal Im",
        kreis="Wal",
        ort="Im",
    )
    LAUT_WAL_IT = Sammlung(
        trace="Wal It",
        groups="Lautschrift|Wal It",
        kreis="Wal",
        ort="It",
    )
    LAUT_WAL_KB = Sammlung(
        trace="Wal Kb",
        groups="Lautschrift|Wal Kb",
        kreis="Wal",
        ort="Kb",
    )
    LAUT_WAL_KG = Sammlung(
        trace="Wal Kg",
        groups="Lautschrift|Wal Kg",
        kreis="Wal",
        ort="Kg",
    )
    LAUT_WAL_KI = Sammlung(
        trace="Wal Ki",
        groups="Lautschrift|Wal Ki",
        kreis="Wal",
        ort="Ki",
    )
    LAUT_WAL_KÜ = Sammlung(
        trace="Wal Kü",
        groups="Lautschrift|Wal Kü",
        kreis="Wal",
        ort="Kü",
    )
    LAUT_WAL_LA = Sammlung(
        trace="Wal La",
        groups="Lautschrift|Wal La",
        kreis="Wal",
        ort="La",
    )
    LAUT_WAL_LB = Sammlung(
        trace="Wal Lb",
        groups="Lautschrift|Wal Lb",
        kreis="Wal",
        ort="Lb",
    )
    LAUT_WAL_LF = Sammlung(
        trace="Wal Lf",
        groups="Lautschrift|Wal Lf",
        kreis="Wal",
        ort="Lf",
    )
    LAUT_WAL_LH = Sammlung(
        trace="Wal Lh",
        groups="Lautschrift|Wal Lh",
        kreis="Wal",
        ort="Lh",
    )
    LAUT_WAL_ME = Sammlung(
        trace="Wal Me",
        groups="Lautschrift|Wal Me",
        kreis="Wal",
        ort="Me",
    )
    LAUT_WAL_MH = Sammlung(
        trace="Wal Mh",
        groups="Lautschrift|Wal Mh",
        kreis="Wal",
        ort="Mh",
    )
    LAUT_WAL_ML = Sammlung(
        trace="Wal Ml",
        groups="Lautschrift|Wal Ml",
        kreis="Wal",
        ort="Ml",
    )
    LAUT_WAL_MN = Sammlung(
        trace="Wal Mn",
        groups="Lautschrift|Wal Mn",
        kreis="Wal",
        ort="Mn",
    )
    LAUT_WAL_MS = Sammlung(
        trace="Wal Ms",
        groups="Lautschrift|Wal Ms",
        kreis="Wal",
        ort="Ms",
    )
    LAUT_WAL_MÜ = Sammlung(
        trace="Wal Mü",
        groups="Lautschrift|Wal Mü",
        kreis="Wal",
        ort="Mü",
    )
    LAUT_WAL_NB = Sammlung(
        trace="Wal Nb",
        groups="Lautschrift|Wal Nb",
        kreis="Wal",
        ort="Nb",
    )
    LAUT_WAL_NE = Sammlung(
        trace="Wal Ne",
        groups="Lautschrift|Wal Ne",
        kreis="Wal",
        ort="Ne",
    )
    LAUT_WAL_NF = Sammlung(
        trace="Wal Nf",
        groups="Lautschrift|Wal Nf",
        kreis="Wal",
        ort="Nf",
    )
    LAUT_WAL_NR = Sammlung(
        trace="Wal Nr",
        groups="Lautschrift|Wal Nr",
        kreis="Wal",
        ort="Nr",
    )
    LAUT_WAL_NS = Sammlung(
        trace="Wal Ns",
        groups="Lautschrift|Wal Ns",
        kreis="Wal",
        ort="Ns",
    )
    LAUT_WAL_NW = Sammlung(
        trace="Wal Nw",
        groups="Lautschrift|Wal Nw",
        kreis="Wal",
        ort="Nw",
    )
    LAUT_WAL_OB = Sammlung(
        trace="Wal Ob",
        groups="Lautschrift|Wal Ob",
        kreis="Wal",
        ort="Ob",
    )
    LAUT_WAL_OE = Sammlung(
        trace="Wal Oe",
        groups="Lautschrift|Wal Oe",
        kreis="Wal",
        ort="Oe",
    )
    LAUT_WAL_OT = Sammlung(
        trace="Wal Ot",
        groups="Lautschrift|Wal Ot",
        kreis="Wal",
        ort="Ot",
    )
    LAUT_WAL_OW = Sammlung(
        trace="Wal Ow",
        groups="Lautschrift|Wal Ow",
        kreis="Wal",
        ort="Ow",
    )
    LAUT_WAL_RA = Sammlung(
        trace="Wal Ra",
        groups="Lautschrift|Wal Ra",
        kreis="Wal",
        ort="Ra",
    )
    LAUT_WAL_RE = Sammlung(
        trace="Wal Re",
        groups="Lautschrift|Wal Re",
        kreis="Wal",
        ort="Re",
    )
    LAUT_WAL_RG = Sammlung(
        trace="Wal Rg",
        groups="Lautschrift|Wal Rg",
        kreis="Wal",
        ort="Rg",
    )
    LAUT_WAL_RO = Sammlung(
        trace="Wal Ro",
        groups="Lautschrift|Wal Ro",
        kreis="Wal",
        ort="Ro",
    )
    LAUT_WAL_RT = Sammlung(
        trace="Wal Rt",
        groups="Lautschrift|Wal Rt",
        kreis="Wal",
        ort="Rt",
    )
    LAUT_WAL_SA = Sammlung(
        trace="Wal Sa",
        groups="Lautschrift|Wal Sa",
        kreis="Wal",
        ort="Sa",
    )
    LAUT_WAL_SB = Sammlung(
        trace="Wal Sb",
        groups="Lautschrift|Wal Sb",
        kreis="Wal",
        ort="Sb",
    )
    LAUT_WAL_SC = Sammlung(
        trace="Wal Sc",
        groups="Lautschrift|Wal Sc",
        kreis="Wal",
        ort="Sc",
    )
    LAUT_WAL_SE = Sammlung(
        trace="Wal Se",
        groups="Lautschrift|Wal Se",
        kreis="Wal",
        ort="Se",
    )
    LAUT_WAL_SF = Sammlung(
        trace="Wal Sf",
        groups="Lautschrift|Wal Sf",
        kreis="Wal",
        ort="Sf",
    )
    LAUT_WAL_SM = Sammlung(
        trace="Wal Sm",
        groups="Lautschrift|Wal Sm",
        kreis="Wal",
        ort="Sm",
    )
    LAUT_WAL_ST = Sammlung(
        trace="Wal St",
        groups="Lautschrift|Wal St",
        kreis="Wal",
        ort="St",
    )
    LAUT_WAL_SU = Sammlung(
        trace="Wal Su",
        groups="Lautschrift|Wal Su",
        kreis="Wal",
        ort="Su",
    )
    LAUT_WAL_TI = Sammlung(
        trace="Wal Ti",
        groups="Lautschrift|Wal Ti",
        kreis="Wal",
        ort="Ti",
    )
    LAUT_WAL_TW = Sammlung(
        trace="Wal Tw",
        groups="Lautschrift|Wal Tw",
        kreis="Wal",
        ort="Tw",
    )
    LAUT_WAL_US = Sammlung(
        trace="Wal Us",
        groups="Lautschrift|Wal Us",
        kreis="Wal",
        ort="Us",
    )
    LAUT_WAL_VA = Sammlung(
        trace="Wal Va",
        groups="Lautschrift|Wal Va",
        kreis="Wal",
        ort="Va",
    )
    LAUT_WAL_VH = Sammlung(
        trace="Wal Vh",
        groups="Lautschrift|Wal Vh",
        kreis="Wal",
        ort="Vh",
    )
    LAUT_WAL_VÖ = Sammlung(
        trace="Wal Vö",
        groups="Lautschrift|Wal Vö",
        kreis="Wal",
        ort="Vö",
    )
    LAUT_WAL_WB = Sammlung(
        trace="Wal Wb",
        groups="Lautschrift|Wal Wb",
        kreis="Wal",
        ort="Wb",
    )
    LAUT_WAL_WD = Sammlung(
        trace="Wal Wd",
        groups="Lautschrift|Wal Wd",
        kreis="Wal",
        ort="Wd",
    )
    LAUT_WAL_WE = Sammlung(
        trace="Wal We",
        groups="Lautschrift|Wal We",
        kreis="Wal",
        ort="We",
    )
    LAUT_WAL_WH = Sammlung(
        trace="Wal Wh",
        groups="Lautschrift|Wal Wh",
        kreis="Wal",
        ort="Wh",
    )
    LAUT_WAL_WI = Sammlung(
        trace="Wal Wi",
        groups="Lautschrift|Wal Wi",
        kreis="Wal",
        ort="Wi",
    )
    LAUT_WAL_WL = Sammlung(
        trace="Wal Wl",
        groups="Lautschrift|Wal Wl",
        kreis="Wal",
        ort="Wl",
    )
    LAUT_WAL_WR = Sammlung(
        trace="Wal Wr",
        groups="Lautschrift|Wal Wr",
        kreis="Wal",
        ort="Wr",
    )
    LAUT_WAL_WT = Sammlung(
        trace="Wal Wt",
        groups="Lautschrift|Wal Wt",
        kreis="Wal",
        ort="Wt",
    )
    LAUT_WBG_AH = Sammlung(
        trace="Wbg Ah",
        groups="Lautschrift|Wbg Ah",
        kreis="Wbg",
        ort="Ah",
    )
    LAUT_WBG_BB = Sammlung(
        trace="Wbg Bb",
        groups="Lautschrift|Wbg Bb",
        kreis="Wbg",
        ort="Bb",
    )
    LAUT_WBG_BG = Sammlung(
        trace="Wbg Bg",
        groups="Lautschrift|Wbg Bg",
        kreis="Wbg",
        ort="Bg",
    )
    LAUT_WBG_BH = Sammlung(
        trace="Wbg Bh",
        groups="Lautschrift|Wbg Bh",
        kreis="Wbg",
        ort="Bh",
    )
    LAUT_WBG_BO = Sammlung(
        trace="Wbg Bo",
        groups="Lautschrift|Wbg Bo",
        kreis="Wbg",
        ort="Bo",
    )
    LAUT_WBG_BÜ = Sammlung(
        trace="Wbg Bü",
        groups="Lautschrift|Wbg Bü",
        kreis="Wbg",
        ort="Bü",
    )
    LAUT_WBG_DA = Sammlung(
        trace="Wbg Da",
        groups="Lautschrift|Wbg Da",
        kreis="Wbg",
        ort="Da",
    )
    LAUT_WBG_DB = Sammlung(
        trace="Wbg Db",
        groups="Lautschrift|Wbg Db",
        kreis="Wbg",
        ort="Db",
    )
    LAUT_WBG_DÖ = Sammlung(
        trace="Wbg Dö",
        groups="Lautschrift|Wbg Dö",
        kreis="Wbg",
        ort="Dö",
    )
    LAUT_WBG_DS = Sammlung(
        trace="Wbg Ds",
        groups="Lautschrift|Wbg Ds",
        kreis="Wbg",
        ort="Ds",
    )
    LAUT_WBG_EI = Sammlung(
        trace="Wbg Ei",
        groups="Lautschrift|Wbg Ei",
        kreis="Wbg",
        ort="Ei",
    )
    LAUT_WBG_EN = Sammlung(
        trace="Wbg En",
        groups="Lautschrift|Wbg En",
        kreis="Wbg",
        ort="En",
    )
    LAUT_WBG_FÖ = Sammlung(
        trace="Wbg Fö",
        groups="Lautschrift|Wbg Fö",
        kreis="Wbg",
        ort="Fö",
    )
    LAUT_WBG_FR = Sammlung(
        trace="Wbg Fr",
        groups="Lautschrift|Wbg Fr",
        kreis="Wbg",
        ort="Fr",
    )
    LAUT_WBG_GE = Sammlung(
        trace="Wbg Ge",
        groups="Lautschrift|Wbg Ge",
        kreis="Wbg",
        ort="Ge",
    )
    LAUT_WBG_GM = Sammlung(
        trace="Wbg Gm",
        groups="Lautschrift|Wbg Gm",
        kreis="Wbg",
        ort="Gm",
    )
    LAUT_WBG_GR = Sammlung(
        trace="Wbg Gr",
        groups="Lautschrift|Wbg Gr",
        kreis="Wbg",
        ort="Gr",
    )
    LAUT_WBG_HA = Sammlung(
        trace="Wbg Ha",
        groups="Lautschrift|Wbg Ha",
        kreis="Wbg",
        ort="Ha",
    )
    LAUT_WBG_HE = Sammlung(
        trace="Wbg He",
        groups="Lautschrift|Wbg He",
        kreis="Wbg",
        ort="He",
    )
    LAUT_WBG_HH = Sammlung(
        trace="Wbg Hh",
        groups="Lautschrift|Wbg Hh",
        kreis="Wbg",
        ort="Hh",
    )
    LAUT_WBG_HO = Sammlung(
        trace="Wbg Ho",
        groups="Lautschrift|Wbg Ho",
        kreis="Wbg",
        ort="Ho",
    )
    LAUT_WBG_IK = Sammlung(
        trace="Wbg Ik",
        groups="Lautschrift|Wbg Ik",
        kreis="Wbg",
        ort="Ik",
    )
    LAUT_WBG_KA = Sammlung(
        trace="Wbg Ka",
        groups="Lautschrift|Wbg Ka",
        kreis="Wbg",
        ort="Ka",
    )
    LAUT_WBG_KÖ = Sammlung(
        trace="Wbg Kö",
        groups="Lautschrift|Wbg Kö",
        kreis="Wbg",
        ort="Kö",
    )
    LAUT_WBG_KÜ = Sammlung(
        trace="Wbg Kü",
        groups="Lautschrift|Wbg Kü",
        kreis="Wbg",
        ort="Kü",
    )
    LAUT_WBG_LÖ = Sammlung(
        trace="Wbg Lö",
        groups="Lautschrift|Wbg Lö",
        kreis="Wbg",
        ort="Lö",
    )
    LAUT_WBG_LÜ = Sammlung(
        trace="Wbg Lü",
        groups="Lautschrift|Wbg Lü",
        kreis="Wbg",
        ort="Lü",
    )
    LAUT_WBG_ME = Sammlung(
        trace="Wbg Me",
        groups="Lautschrift|Wbg Me",
        kreis="Wbg",
        ort="Me",
    )
    LAUT_WBG_MU = Sammlung(
        trace="Wbg Mu",
        groups="Lautschrift|Wbg Mu",
        kreis="Wbg",
        ort="Mu",
    )
    LAUT_WBG_NA = Sammlung(
        trace="Wbg Na",
        groups="Lautschrift|Wbg Na",
        kreis="Wbg",
        ort="Na",
    )
    LAUT_WBG_NH = Sammlung(
        trace="Wbg Nh",
        groups="Lautschrift|Wbg Nh",
        kreis="Wbg",
        ort="Nh",
    )
    LAUT_WBG_NI = Sammlung(
        trace="Wbg Ni",
        groups="Lautschrift|Wbg Ni",
        kreis="Wbg",
        ort="Ni",
    )
    LAUT_WBG_NÖ = Sammlung(
        trace="Wbg Nö",
        groups="Lautschrift|Wbg Nö",
        kreis="Wbg",
        ort="Nö",
    )
    LAUT_WBG_NZ = Sammlung(
        trace="Wbg Nz",
        groups="Lautschrift|Wbg Nz",
        kreis="Wbg",
        ort="Nz",
    )
    LAUT_WBG_OS = Sammlung(
        trace="Wbg Os",
        groups="Lautschrift|Wbg Os",
        kreis="Wbg",
        ort="Os",
    )
    LAUT_WBG_PE = Sammlung(
        trace="Wbg Pe",
        groups="Lautschrift|Wbg Pe",
        kreis="Wbg",
        ort="Pe",
    )
    LAUT_WBG_RI = Sammlung(
        trace="Wbg Ri",
        groups="Lautschrift|Wbg Ri",
        kreis="Wbg",
        ort="Ri",
    )
    LAUT_WBG_RÖ = Sammlung(
        trace="Wbg Rö",
        groups="Lautschrift|Wbg Rö",
        kreis="Wbg",
        ort="Rö",
    )
    LAUT_WBG_SF = Sammlung(
        trace="Wbg Sf",
        groups="Lautschrift|Wbg Sf",
        kreis="Wbg",
        ort="Sf",
    )
    LAUT_WBG_SH = Sammlung(
        trace="Wbg Sh",
        groups="Lautschrift|Wbg Sh",
        kreis="Wbg",
        ort="Sh",
    )
    LAUT_WBG_SI = Sammlung(
        trace="Wbg Si",
        groups="Lautschrift|Wbg Si",
        kreis="Wbg",
        ort="Si",
    )
    LAUT_WBG_SS = Sammlung(
        trace="Wbg Ss",
        groups="Lautschrift|Wbg Ss",
        kreis="Wbg",
        ort="Ss",
    )
    LAUT_WBG_WB = Sammlung(
        trace="Wbg Wb",
        groups="Lautschrift|Wbg Wb",
        kreis="Wbg",
        ort="Wb",
    )
    LAUT_WBG_WE = Sammlung(
        trace="Wbg We",
        groups="Lautschrift|Wbg We",
        kreis="Wbg",
        ort="We",
    )
    LAUT_WBG_WG = Sammlung(
        trace="Wbg Wg",
        groups="Lautschrift|Wbg Wg",
        kreis="Wbg",
        ort="Wg",
    )
    LAUT_WBG_WI = Sammlung(
        trace="Wbg Wi",
        groups="Lautschrift|Wbg Wi",
        kreis="Wbg",
        ort="Wi",
    )
    LAUT_WBG_WO = Sammlung(
        trace="Wbg Wo",
        groups="Lautschrift|Wbg Wo",
        kreis="Wbg",
        ort="Wo",
    )
    LAUT_WDF_BE = Sammlung(
        trace="Wdf Be",
        groups="Lautschrift|Wdf Be",
        kreis="Wdf",
        ort="Be",
    )
    LAUT_WDF_BL = Sammlung(
        trace="Wdf Bl",
        groups="Lautschrift|Wdf Bl",
        kreis="Wdf",
        ort="Bl",
    )
    LAUT_WDF_BR = Sammlung(
        trace="Wdf Br",
        groups="Lautschrift|Wdf Br",
        kreis="Wdf",
        ort="Br",
    )
    LAUT_WDF_BS = Sammlung(
        trace="Wdf Bs",
        groups="Lautschrift|Wdf Bs",
        kreis="Wdf",
        ort="Bs",
    )
    LAUT_WDF_DM = Sammlung(
        trace="Wdf Dm",
        groups="Lautschrift|Wdf Dm",
        kreis="Wdf",
        ort="Dm",
    )
    LAUT_WDF_EI = Sammlung(
        trace="Wdf Ei",
        groups="Lautschrift|Wdf Ei",
        kreis="Wdf",
        ort="Ei",
    )
    LAUT_WDF_EV = Sammlung(
        trace="Wdf Ev",
        groups="Lautschrift|Wdf Ev",
        kreis="Wdf",
        ort="Ev",
    )
    LAUT_WDF_FR = Sammlung(
        trace="Wdf Fr",
        groups="Lautschrift|Wdf Fr",
        kreis="Wdf",
        ort="Fr",
    )
    LAUT_WDF_FÜ = Sammlung(
        trace="Wdf Fü",
        groups="Lautschrift|Wdf Fü",
        kreis="Wdf",
        ort="Fü",
    )
    LAUT_WDF_GF = Sammlung(
        trace="Wdf Gf",
        groups="Lautschrift|Wdf Gf",
        kreis="Wdf",
        ort="Gf",
    )
    LAUT_WDF_GR = Sammlung(
        trace="Wdf Gr",
        groups="Lautschrift|Wdf Gr",
        kreis="Wdf",
        ort="Gr",
    )
    LAUT_WDF_HO = Sammlung(
        trace="Wdf Ho",
        groups="Lautschrift|Wdf Ho",
        kreis="Wdf",
        ort="Ho",
    )
    LAUT_WDF_HW = Sammlung(
        trace="Wdf Hw",
        groups="Lautschrift|Wdf Hw",
        kreis="Wdf",
        ort="Hw",
    )
    LAUT_WDF_MF = Sammlung(
        trace="Wdf Mf",
        groups="Lautschrift|Wdf Mf",
        kreis="Wdf",
        ort="Mf",
    )
    LAUT_WDF_MI = Sammlung(
        trace="Wdf Mi",
        groups="Lautschrift|Wdf Mi",
        kreis="Wdf",
        ort="Mi",
    )
    LAUT_WDF_MÜ = Sammlung(
        trace="Wdf Mü",
        groups="Lautschrift|Wdf Mü",
        kreis="Wdf",
        ort="Mü",
    )
    LAUT_WDF_OB = Sammlung(
        trace="Wdf Ob",
        groups="Lautschrift|Wdf Ob",
        kreis="Wdf",
        ort="Ob",
    )
    LAUT_WDF_OF = Sammlung(
        trace="Wdf Of",
        groups="Lautschrift|Wdf Of",
        kreis="Wdf",
        ort="Of",
    )
    LAUT_WDF_RH = Sammlung(
        trace="Wdf Rh",
        groups="Lautschrift|Wdf Rh",
        kreis="Wdf",
        ort="Rh",
    )
    LAUT_WDF_SB = Sammlung(
        trace="Wdf Sb",
        groups="Lautschrift|Wdf Sb",
        kreis="Wdf",
        ort="Sb",
    )
    LAUT_WDF_SC = Sammlung(
        trace="Wdf Sc",
        groups="Lautschrift|Wdf Sc",
        kreis="Wdf",
        ort="Sc",
    )
    LAUT_WDF_VE = Sammlung(
        trace="Wdf Ve",
        groups="Lautschrift|Wdf Ve",
        kreis="Wdf",
        ort="Ve",
    )
    LAUT_WDF_VO = Sammlung(
        trace="Wdf Vo",
        groups="Lautschrift|Wdf Vo",
        kreis="Wdf",
        ort="Vo",
    )
    LAUT_WDF_WD = Sammlung(
        trace="Wdf Wd",
        groups="Lautschrift|Wdf Wd",
        kreis="Wdf",
        ort="Wd",
    )
    LAUT_WDF_WK = Sammlung(
        trace="Wdf Wk",
        groups="Lautschrift|Wdf Wk",
        kreis="Wdf",
        ort="Wk",
    )
    LAUT_WIE_AL = Sammlung(
        trace="Wie Al",
        groups="Lautschrift|Wie Al",
        kreis="Wie",
        ort="Al",
    )
    LAUT_WIE_AV = Sammlung(
        trace="Wie Av",
        groups="Lautschrift|Wie Av",
        kreis="Wie",
        ort="Av",
    )
    LAUT_WIE_BA = Sammlung(
        trace="Wie Ba",
        groups="Lautschrift|Wie Ba",
        kreis="Wie",
        ort="Ba",
    )
    LAUT_WIE_BH = Sammlung(
        trace="Wie Bh",
        groups="Lautschrift|Wie Bh",
        kreis="Wie",
        ort="Bh",
    )
    LAUT_WIE_BL = Sammlung(
        trace="Wie Bl",
        groups="Lautschrift|Wie Bl",
        kreis="Wie",
        ort="Bl",
    )
    LAUT_WIE_BO = Sammlung(
        trace="Wie Bo",
        groups="Lautschrift|Wie Bo",
        kreis="Wie",
        ort="Bo",
    )
    LAUT_WIE_BR = Sammlung(
        trace="Wie Br",
        groups="Lautschrift|Wie Br",
        kreis="Wie",
        ort="Br",
    )
    LAUT_WIE_DR = Sammlung(
        trace="Wie Dr",
        groups="Lautschrift|Wie Dr",
        kreis="Wie",
        ort="Dr",
    )
    LAUT_WIE_EH = Sammlung(
        trace="Wie Eh",
        groups="Lautschrift|Wie Eh",
        kreis="Wie",
        ort="Eh",
    )
    LAUT_WIE_EM = Sammlung(
        trace="Wie Em",
        groups="Lautschrift|Wie Em",
        kreis="Wie",
        ort="Em",
    )
    LAUT_WIE_FR = Sammlung(
        trace="Wie Fr",
        groups="Lautschrift|Wie Fr",
        kreis="Wie",
        ort="Fr",
    )
    LAUT_WIE_GR = Sammlung(
        trace="Wie Gr",
        groups="Lautschrift|Wie Gr",
        kreis="Wie",
        ort="Gr",
    )
    LAUT_WIE_GÜ = Sammlung(
        trace="Wie Gü",
        groups="Lautschrift|Wie Gü",
        kreis="Wie",
        ort="Gü",
    )
    LAUT_WIE_HB = Sammlung(
        trace="Wie Hb",
        groups="Lautschrift|Wie Hb",
        kreis="Wie",
        ort="Hb",
    )
    LAUT_WIE_HD = Sammlung(
        trace="Wie Hd",
        groups="Lautschrift|Wie Hd",
        kreis="Wie",
        ort="Hd",
    )
    LAUT_WIE_HO = Sammlung(
        trace="Wie Ho",
        groups="Lautschrift|Wie Ho",
        kreis="Wie",
        ort="Ho",
    )
    LAUT_WIE_KL = Sammlung(
        trace="Wie Kl",
        groups="Lautschrift|Wie Kl",
        kreis="Wie",
        ort="Kl",
    )
    LAUT_WIE_KS = Sammlung(
        trace="Wie Ks",
        groups="Lautschrift|Wie Ks",
        kreis="Wie",
        ort="Ks",
    )
    LAUT_WIE_KZ = Sammlung(
        trace="Wie Kz",
        groups="Lautschrift|Wie Kz",
        kreis="Wie",
        ort="Kz",
    )
    LAUT_WIE_LB = Sammlung(
        trace="Wie Lb",
        groups="Lautschrift|Wie Lb",
        kreis="Wie",
        ort="Lb",
    )
    LAUT_WIE_LE = Sammlung(
        trace="Wie Le",
        groups="Lautschrift|Wie Le",
        kreis="Wie",
        ort="Le",
    )
    LAUT_WIE_LI = Sammlung(
        trace="Wie Li",
        groups="Lautschrift|Wie Li",
        kreis="Wie",
        ort="Li",
    )
    LAUT_WIE_LK = Sammlung(
        trace="Wie Lk",
        groups="Lautschrift|Wie Lk",
        kreis="Wie",
        ort="Lk",
    )
    LAUT_WIE_LT = Sammlung(
        trace="Wie Lt",
        groups="Lautschrift|Wie Lt",
        kreis="Wie",
        ort="Lt",
    )
    LAUT_WIE_MH = Sammlung(
        trace="Wie Mh",
        groups="Lautschrift|Wie Mh",
        kreis="Wie",
        ort="Mh",
    )
    LAUT_WIE_MÖ = Sammlung(
        trace="Wie Mö",
        groups="Lautschrift|Wie Mö",
        kreis="Wie",
        ort="Mö",
    )
    LAUT_WIE_NH = Sammlung(
        trace="Wie Nh",
        groups="Lautschrift|Wie Nh",
        kreis="Wie",
        ort="Nh",
    )
    LAUT_WIE_NK = Sammlung(
        trace="Wie Nk",
        groups="Lautschrift|Wie Nk",
        kreis="Wie",
        ort="Nk",
    )
    LAUT_WIE_NR = Sammlung(
        trace="Wie Nr",
        groups="Lautschrift|Wie Nr",
        kreis="Wie",
        ort="Nr",
    )
    LAUT_WIE_ÖW = Sammlung(
        trace="Wie Öw",
        groups="Lautschrift|Wie Öw",
        kreis="Wie",
        ort="Öw",
    )
    LAUT_WIE_PA = Sammlung(
        trace="Wie Pa",
        groups="Lautschrift|Wie Pa",
        kreis="Wie",
        ort="Pa",
    )
    LAUT_WIE_PI = Sammlung(
        trace="Wie Pi",
        groups="Lautschrift|Wie Pi",
        kreis="Wie",
        ort="Pi",
    )
    LAUT_WIE_QH = Sammlung(
        trace="Wie Qh",
        groups="Lautschrift|Wie Qh",
        kreis="Wie",
        ort="Qh",
    )
    LAUT_WIE_RB = Sammlung(
        trace="Wie Rb",
        groups="Lautschrift|Wie Rb",
        kreis="Wie",
        ort="Rb",
    )
    LAUT_WIE_RH = Sammlung(
        trace="Wie Rh",
        groups="Lautschrift|Wie Rh",
        kreis="Wie",
        ort="Rh",
    )
    LAUT_WIE_RÖ = Sammlung(
        trace="Wie Rö",
        groups="Lautschrift|Wie Rö",
        kreis="Wie",
        ort="Rö",
    )
    LAUT_WIE_SA = Sammlung(
        trace="Wie Sa",
        groups="Lautschrift|Wie Sa",
        kreis="Wie",
        ort="Sa",
    )
    LAUT_WIE_SE = Sammlung(
        trace="Wie Se",
        groups="Lautschrift|Wie Se",
        kreis="Wie",
        ort="Se",
    )
    LAUT_WIE_SH = Sammlung(
        trace="Wie Sh",
        groups="Lautschrift|Wie Sh",
        kreis="Wie",
        ort="Sh",
    )
    LAUT_WIE_SP = Sammlung(
        trace="Wie Sp",
        groups="Lautschrift|Wie Sp",
        kreis="Wie",
        ort="Sp",
    )
    LAUT_WIE_SU = Sammlung(
        trace="Wie Su",
        groups="Lautschrift|Wie Su",
        kreis="Wie",
        ort="Su",
    )
    LAUT_WIE_SV = Sammlung(
        trace="Wie Sv",
        groups="Lautschrift|Wie Sv",
        kreis="Wie",
        ort="Sv",
    )
    LAUT_WIE_VL = Sammlung(
        trace="Wie Vl",
        groups="Lautschrift|Wie Vl",
        kreis="Wie",
        ort="Vl",
    )
    LAUT_WIE_VS = Sammlung(
        trace="Wie Vs",
        groups="Lautschrift|Wie Vs",
        kreis="Wie",
        ort="Vs",
    )
    LAUT_WIE_WB = Sammlung(
        trace="Wie Wb",
        groups="Lautschrift|Wie Wb",
        kreis="Wie",
        ort="Wb",
    )
    LAUT_WIE_WH = Sammlung(
        trace="Wie Wh",
        groups="Lautschrift|Wie Wh",
        kreis="Wie",
        ort="Wh",
    )
    LAUT_WIE_WW = Sammlung(
        trace="Wie Ww",
        groups="Lautschrift|Wie Ww",
        kreis="Wie",
        ort="Ww",
    )
    LAUT_WIT_BO = Sammlung(
        trace="Wit Bo",
        groups="Lautschrift|Wit Bo",
        kreis="Wit",
        ort="Bo",
    )
    LAUT_WIT_HE = Sammlung(
        trace="Wit He",
        groups="Lautschrift|Wit He",
        kreis="Wit",
        ort="He",
    )
    LAUT_WIT_RH = Sammlung(
        trace="Wit Rh",
        groups="Lautschrift|Wit Rh",
        kreis="Wit",
        ort="Rh",
    )
    LAUT_WIT_ST = Sammlung(
        trace="Wit St",
        groups="Lautschrift|Wit St",
        kreis="Wit",
        ort="St",
    )
    LAUT_WIT_WI = Sammlung(
        trace="Wit Wi",
        groups="Lautschrift|Wit Wi",
        kreis="Wit",
        ort="Wi",
    )
    LAUT_WLG_BH = Sammlung(
        trace="Wlg Bh",
        groups="Lautschrift|Wlg Bh",
        kreis="Wlg",
        ort="Bh",
    )
    LAUT_WLG_BO = Sammlung(
        trace="Wlg Bo",
        groups="Lautschrift|Wlg Bo",
        kreis="Wlg",
        ort="Bo",
    )
    LAUT_WLG_BR = Sammlung(
        trace="Wlg Br",
        groups="Lautschrift|Wlg Br",
        kreis="Wlg",
        ort="Br",
    )
    LAUT_WLG_BX = Sammlung(
        trace="Wlg Bx",
        groups="Lautschrift|Wlg Bx",
        kreis="Wlg",
        ort="Bx",
    )
    LAUT_WLG_ES = Sammlung(
        trace="Wlg Es",
        groups="Lautschrift|Wlg Es",
        kreis="Wlg",
        ort="Es",
    )
    LAUT_WLG_HA = Sammlung(
        trace="Wlg Ha",
        groups="Lautschrift|Wlg Ha",
        kreis="Wlg",
        ort="Ha",
    )
    LAUT_WLG_HB = Sammlung(
        trace="Wlg Hb",
        groups="Lautschrift|Wlg Hb",
        kreis="Wlg",
        ort="Hb",
    )
    LAUT_WLG_HH = Sammlung(
        trace="Wlg Hh",
        groups="Lautschrift|Wlg Hh",
        kreis="Wlg",
        ort="Hh",
    )
    LAUT_WLG_HI = Sammlung(
        trace="Wlg Hi",
        groups="Lautschrift|Wlg Hi",
        kreis="Wlg",
        ort="Hi",
    )
    LAUT_WLG_LI = Sammlung(
        trace="Wlg Li",
        groups="Lautschrift|Wlg Li",
        kreis="Wlg",
        ort="Li",
    )
    LAUT_WLG_LN = Sammlung(
        trace="Wlg Ln",
        groups="Lautschrift|Wlg Ln",
        kreis="Wlg",
        ort="Ln",
    )
    LAUT_WLG_LO = Sammlung(
        trace="Wlg Lo",
        groups="Lautschrift|Wlg Lo",
        kreis="Wlg",
        ort="Lo",
    )
    LAUT_WLG_ME = Sammlung(
        trace="Wlg Me",
        groups="Lautschrift|Wlg Me",
        kreis="Wlg",
        ort="Me",
    )
    LAUT_WLG_NW = Sammlung(
        trace="Wlg Nw",
        groups="Lautschrift|Wlg Nw",
        kreis="Wlg",
        ort="Nw",
    )
    LAUT_WLG_OC = Sammlung(
        trace="Wlg Oc",
        groups="Lautschrift|Wlg Oc",
        kreis="Wlg",
        ort="Oc",
    )
    LAUT_WLG_RA = Sammlung(
        trace="Wlg Ra",
        groups="Lautschrift|Wlg Ra",
        kreis="Wlg",
        ort="Ra",
    )
    LAUT_WLG_SW = Sammlung(
        trace="Wlg Sw",
        groups="Lautschrift|Wlg Sw",
        kreis="Wlg",
        ort="Sw",
    )
    LAUT_WLG_VE = Sammlung(
        trace="Wlg Ve",
        groups="Lautschrift|Wlg Ve",
        kreis="Wlg",
        ort="Ve",
    )
    LAUT_WLG_WD = Sammlung(
        trace="Wlg Wd",
        groups="Lautschrift|Wlg Wd",
        kreis="Wlg",
        ort="Wd",
    )
    LAUT_WLG_WE = Sammlung(
        trace="Wlg We",
        groups="Lautschrift|Wlg We",
        kreis="Wlg",
        ort="We",
    )
    LAUT_WLG_WI = Sammlung(
        trace="Wlg Wi",
        groups="Lautschrift|Wlg Wi",
        kreis="Wlg",
        ort="Wi",
    )
    LAUT_WOL_AH = Sammlung(
        trace="Wol Ah",
        groups="Lautschrift|Wol Ah",
        kreis="Wol",
        ort="Ah",
    )
    LAUT_WOL_BH = Sammlung(
        trace="Wol Bh",
        groups="Lautschrift|Wol Bh",
        kreis="Wol",
        ort="Bh",
    )
    LAUT_WOL_EH = Sammlung(
        trace="Wol Eh",
        groups="Lautschrift|Wol Eh",
        kreis="Wol",
        ort="Eh",
    )
    LAUT_WOL_ER = Sammlung(
        trace="Wol Er",
        groups="Lautschrift|Wol Er",
        kreis="Wol",
        ort="Er",
    )
    LAUT_WOL_IP = Sammlung(
        trace="Wol Ip",
        groups="Lautschrift|Wol Ip",
        kreis="Wol",
        ort="Ip",
    )
    LAUT_WOL_NE = Sammlung(
        trace="Wol Ne",
        groups="Lautschrift|Wol Ne",
        kreis="Wol",
        ort="Ne",
    )
    LAUT_WOL_NF = Sammlung(
        trace="Wol Nf",
        groups="Lautschrift|Wol Nf",
        kreis="Wol",
        ort="Nf",
    )
    LAUT_WOL_NL = Sammlung(
        trace="Wol Nl",
        groups="Lautschrift|Wol Nl",
        kreis="Wol",
        ort="Nl",
    )
    LAUT_WOL_OE = Sammlung(
        trace="Wol Oe",
        groups="Lautschrift|Wol Oe",
        kreis="Wol",
        ort="Oe",
    )
    LAUT_WOL_ÖL = Sammlung(
        trace="Wol Öl",
        groups="Lautschrift|Wol Öl",
        kreis="Wol",
        ort="Öl",
    )
    LAUT_WOL_VB = Sammlung(
        trace="Wol Vb",
        groups="Lautschrift|Wol Vb",
        kreis="Wol",
        ort="Vb",
    )
    LAUT_WOL_VO = Sammlung(
        trace="Wol Vo",
        groups="Lautschrift|Wol Vo",
        kreis="Wol",
        ort="Vo",
    )
    LAUT_WOL_WE = Sammlung(
        trace="Wol We",
        groups="Lautschrift|Wol We",
        kreis="Wol",
        ort="We",
    )
    LAUT_WOL_WH = Sammlung(
        trace="Wol Wh",
        groups="Lautschrift|Wol Wh",
        kreis="Wol",
        ort="Wh",
    )
    LAUT_WOL_WO = Sammlung(
        trace="Wol Wo",
        groups="Lautschrift|Wol Wo",
        kreis="Wol",
        ort="Wo",
    )
    LAUT_WTG_LW = Sammlung(
        trace="Wtg Lw",
        groups="Lautschrift|Wtg Lw",
        kreis="Wtg",
        ort="Lw",
    )
    LAUT_WTG_NA = Sammlung(
        trace="Wtg Na",
        groups="Lautschrift|Wtg Na",
        kreis="Wtg",
        ort="Na",
    )

    ##############################################################
    # Unbestimmte lautschriftliche Orte
    ##############################################################
    LAUT_AHS_XY = Sammlung(
        trace="Ahs Xy",
        groups="Lautschrift|Ahs Xy",
        kreis="Ahs",
        ort="Xy",
    )
    LAUT_ALT_XY = Sammlung(
        trace="Alt Xy",
        groups="Lautschrift|Alt Xy",
        kreis="Alt",
        ort="Xy",
    )
    LAUT_ARN_XY = Sammlung(
        trace="Arn Xy",
        groups="Lautschrift|Arn Xy",
        kreis="Arn",
        ort="Xy",
    )
    LAUT_ASD_XY = Sammlung(
        trace="Asd Xy",
        groups="Lautschrift|Asd Xy",
        kreis="Asd",
        ort="Xy",
    )
    LAUT_BBR_XY = Sammlung(
        trace="Bbr Xy",
        groups="Lautschrift|Bbr Xy",
        kreis="Bbr",
        ort="Xy",
    )
    LAUT_BCH_XY = Sammlung(
        trace="Bch Xy",
        groups="Lautschrift|Bch Xy",
        kreis="Bch",
        ort="Xy",
    )
    LAUT_BEK_XY = Sammlung(
        trace="Bek Xy",
        groups="Lautschrift|Bek Xy",
        kreis="Bek",
        ort="Xy",
    )
    LAUT_BEN_XY = Sammlung(
        trace="Ben Xy",
        groups="Lautschrift|Ben Xy",
        kreis="Ben",
        ort="Xy",
    )
    LAUT_BIE_XY = Sammlung(
        trace="Bie Xy",
        groups="Lautschrift|Bie Xy",
        kreis="Bie",
        ort="Xy",
    )
    LAUT_BOR_XY = Sammlung(
        trace="Bor Xy",
        groups="Lautschrift|Bor Xy",
        kreis="Bor",
        ort="Xy",
    )
    LAUT_BRG_XY = Sammlung(
        trace="Brg Xy",
        groups="Lautschrift|Brg Xy",
        kreis="Brg",
        ort="Xy",
    )
    LAUT_BRI_XY = Sammlung(
        trace="Bri Xy",
        groups="Lautschrift|Bri Xy",
        kreis="Bri",
        ort="Xy",
    )
    LAUT_BÜK_XY = Sammlung(
        trace="Bük Xy",
        groups="Lautschrift|Bük Xy",
        kreis="Bük",
        ort="Xy",
    )
    LAUT_BÜR_XY = Sammlung(
        trace="Bür Xy",
        groups="Lautschrift|Bür Xy",
        kreis="Bür",
        ort="Xy",
    )
    LAUT_DET_XY = Sammlung(
        trace="Det Xy",
        groups="Lautschrift|Det Xy",
        kreis="Det",
        ort="Xy",
    )
    LAUT_DIE_XY = Sammlung(
        trace="Die Xy",
        groups="Lautschrift|Die Xy",
        kreis="Die",
        ort="Xy",
    )
    LAUT_DOR_XY = Sammlung(
        trace="Dor Xy",
        groups="Lautschrift|Dor Xy",
        kreis="Dor",
        ort="Xy",
    )
    LAUT_ENR_XY = Sammlung(
        trace="Enr Xy",
        groups="Lautschrift|Enr Xy",
        kreis="Enr",
        ort="Xy",
    )
    LAUT_ESS_XY = Sammlung(
        trace="Ess Xy",
        groups="Lautschrift|Ess Xy",
        kreis="Ess",
        ort="Xy",
    )
    LAUT_GEL_XY = Sammlung(
        trace="Gel Xy",
        groups="Lautschrift|Gel Xy",
        kreis="Gel",
        ort="Xy",
    )
    LAUT_HAG_XY = Sammlung(
        trace="Hag Xy",
        groups="Lautschrift|Hag Xy",
        kreis="Hag",
        ort="Xy",
    )
    LAUT_HAL_XY = Sammlung(
        trace="Hal Xy",
        groups="Lautschrift|Hal Xy",
        kreis="Hal",
        ort="Xy",
    )
    LAUT_HFD_XY = Sammlung(
        trace="Hfd Xy",
        groups="Lautschrift|Hfd Xy",
        kreis="Hfd",
        ort="Xy",
    )
    LAUT_HÖX_XY = Sammlung(
        trace="Höx Xy",
        groups="Lautschrift|Höx Xy",
        kreis="Höx",
        ort="Xy",
    )
    LAUT_ISL_XY = Sammlung(
        trace="Isl Xy",
        groups="Lautschrift|Isl Xy",
        kreis="Isl",
        ort="Xy",
    )
    LAUT_KLO_XY = Sammlung(
        trace="Klo Xy",
        groups="Lautschrift|Klo Xy",
        kreis="Klo",
        ort="Xy",
    )
    LAUT_KOS_XY = Sammlung(
        trace="Kos Xy",
        groups="Lautschrift|Kos Xy",
        kreis="Kos",
        ort="Xy",
    )
    LAUT_LEM_XY = Sammlung(
        trace="Lem Xy",
        groups="Lautschrift|Lem Xy",
        kreis="Lem",
        ort="Xy",
    )
    LAUT_LHS_XY = Sammlung(
        trace="Lhs Xy",
        groups="Lautschrift|Lhs Xy",
        kreis="Lhs",
        ort="Xy",
    )
    LAUT_LIN_XY = Sammlung(
        trace="Lin Xy",
        groups="Lautschrift|Lin Xy",
        kreis="Lin",
        ort="Xy",
    )
    LAUT_LST_XY = Sammlung(
        trace="Lst Xy",
        groups="Lautschrift|Lst Xy",
        kreis="Lst",
        ort="Xy",
    )
    LAUT_LÜB_XY = Sammlung(
        trace="Lüb Xy",
        groups="Lautschrift|Lüb Xy",
        kreis="Lüb",
        ort="Xy",
    )
    LAUT_MEL_XY = Sammlung(
        trace="Mel Xy",
        groups="Lautschrift|Mel Xy",
        kreis="Mel",
        ort="Xy",
    )
    LAUT_MEP_XY = Sammlung(
        trace="Mep Xy",
        groups="Lautschrift|Mep Xy",
        kreis="Mep",
        ort="Xy",
    )
    LAUT_MES_XY = Sammlung(
        trace="Mes Xy",
        groups="Lautschrift|Mes Xy",
        kreis="Mes",
        ort="Xy",
    )
    LAUT_MIN_XY = Sammlung(
        trace="Min Xy",
        groups="Lautschrift|Min Xy",
        kreis="Min",
        ort="Xy",
    )
    LAUT_MÜN_XY = Sammlung(
        trace="Mün Xy",
        groups="Lautschrift|Mün Xy",
        kreis="Mün",
        ort="Xy",
    )
    LAUT_NIE_XY = Sammlung(
        trace="Nie Xy",
        groups="Lautschrift|Nie Xy",
        kreis="Nie",
        ort="Xy",
    )
    LAUT_OLP_XY = Sammlung(
        trace="Olp Xy",
        groups="Lautschrift|Olp Xy",
        kreis="Olp",
        ort="Xy",
    )
    LAUT_OSN_XY = Sammlung(
        trace="Osn Xy",
        groups="Lautschrift|Osn Xy",
        kreis="Osn",
        ort="Xy",
    )
    LAUT_PAD_XY = Sammlung(
        trace="Pad Xy",
        groups="Lautschrift|Pad Xy",
        kreis="Pad",
        ort="Xy",
    )
    LAUT_REK_XY = Sammlung(
        trace="Rek Xy",
        groups="Lautschrift|Rek Xy",
        kreis="Rek",
        ort="Xy",
    )
    LAUT_SCH_XY = Sammlung(
        trace="Sch Xy",
        groups="Lautschrift|Sch Xy",
        kreis="Sch",
        ort="Xy",
    )
    LAUT_SOS_XY = Sammlung(
        trace="Sos Xy",
        groups="Lautschrift|Sos Xy",
        kreis="Sos",
        ort="Xy",
    )
    LAUT_STF_XY = Sammlung(
        trace="Stf Xy",
        groups="Lautschrift|Stf Xy",
        kreis="Stf",
        ort="Xy",
    )
    LAUT_STH_XY = Sammlung(
        trace="Sth Xy",
        groups="Lautschrift|Sth Xy",
        kreis="Sth",
        ort="Xy",
    )
    LAUT_TEK_XY = Sammlung(
        trace="Tek Xy",
        groups="Lautschrift|Tek Xy",
        kreis="Tek",
        ort="Xy",
    )
    LAUT_UNN_XY = Sammlung(
        trace="Unn Xy",
        groups="Lautschrift|Unn Xy",
        kreis="Unn",
        ort="Xy",
    )
    LAUT_VCH_XY = Sammlung(
        trace="Vch Xy",
        groups="Lautschrift|Vch Xy",
        kreis="Vch",
        ort="Xy",
    )
    LAUT_WAL_XY = Sammlung(
        trace="Wal Xy",
        groups="Lautschrift|Wal Xy",
        kreis="Wal",
        ort="Xy",
    )
    LAUT_WBG_XY = Sammlung(
        trace="Wbg Xy",
        groups="Lautschrift|Wbg Xy",
        kreis="Wbg",
        ort="Xy",
    )
    LAUT_WDF_XY = Sammlung(
        trace="Wdf Xy",
        groups="Lautschrift|Wdf Xy",
        kreis="Wdf",
        ort="Xy",
    )
    LAUT_WIE_XY = Sammlung(
        trace="Wie Xy",
        groups="Lautschrift|Wie Xy",
        kreis="Wie",
        ort="Xy",
    )
    LAUT_WIT_XY = Sammlung(
        trace="Wit Xy",
        groups="Lautschrift|Wit Xy",
        kreis="Wit",
        ort="Xy",
    )
    LAUT_WLG_XY = Sammlung(
        trace="Wlg Xy",
        groups="Lautschrift|Wlg Xy",
        kreis="Wlg",
        ort="Xy",
    )
    LAUT_WOL_XY = Sammlung(
        trace="Wol Xy",
        groups="Lautschrift|Wol Xy",
        kreis="Wol",
        ort="Xy",
    )
    LAUT_WTG_XY = Sammlung(
        trace="Wtg Xy",
        groups="Lautschrift|Wtg Xy",
        kreis="Wtg",
        ort="Xy",
    )
