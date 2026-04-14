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
    ARENS = Sammlung(
        description="Arens, J., Der Vokalismus der Mundarten im Kreise Olpe unter Zugrundelegung der Mundart von Elspe.",
        alias="Arens",
        kreis="Olp",
    )
    ASSINGHAUSEN = Sammlung(
        description="Assinghausen, Kr. Brilon (Frau Knoche)",
        alias="Bri Ah",
        kreis="Bri",
        ort="Ah",
    )

    BAADER = Sammlung(
        description="Baader-Fragebögen und Baader-Nachlass",
        alias="Baader|BaaderOsnabr",
        title="Baader",
    )
    BAHLMANN = Sammlung(
        description="?Bahlmann, P., Münsterische Lieder und Sprichwörter in plattdeutscher Sprache. Mit einer Einleitung über Münster's niederdeutsche Litteratur.",
        alias="Bahlmann",
        landschaft="Münsterl",
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
    BUELD = Sammlung(
        description="Büld, H., Volk und Sprache im nördlichen Westfalen. Westfälische Ortschaften im Spiegel ihrer Sprache.",
        alias="Büld: Volk u. Spr.",
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

    CRAMER = Sammlung(
        description="Mittelschulrektor H. Cramer (Niedersfeld, Kr. Brilon)",
        alias="Niedersfeld / Bri C.",
        kreis="Bri",
        ort="Nf",
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

    FREDERKING = Sammlung(
        description="Frederking, Ch., Plattdeutsches Dorfwörterbuch des Dorfes Hahlen bei Minden in Westfalen. Wortschatz, Spruchweisheit, Volkskunde.",
        alias="Frdk|Min Ha",
        kreis="Min",
        ort="Ha",
    )

    GESCHER = Sammlung(
        description="Pastor Eing (Gescher, Kr. Coesfeld, und Umgegend)",
        alias="Gescher",
        kreis="Kos",
        ort="Ge",
    )
    GLAEN = Sammlung(
        description="Glaen, K., Das Bild des Menschen in der Sprache von Dahl.",
        alias="Glaen",
        kreis="Pad",
        ort="Da",
    )
    GOEHNER = Sammlung(
        description="Lehrer A. Göhner (Gohfeld, Kr. Herford)",
        alias="Göhner",
        kreis="Hfd",
        ort="Go",
    )
    GREGORY = Sammlung(
        description="Gregory, O., Flächengrammatik des Gebietes von Plettenberg in Westfalen.",
        alias="Gregory",
        kreis="Alt",
        ort="Im",
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

    JOERM = Sammlung(
        description="Rhynern Joermann",
        alias="Rhy. Joer.",
        kreis="Unn",
        ort="Ry",
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

    LIP_OE = Sammlung(
        description="Lip Oe",
        alias="Lip Oe S|Lipp Oe",
    )
    LYRA = Sammlung(
        description="Lyra, F. W., Plattdeutsche Briefe, Erzählungen und Gedichte mit besonderer Rücksicht auf Sprichwörter und eigenthümliche Redensarten des Landvolks in Westphalen.",
        alias="Lyra",
        kreis="Osn",
        ort="Ly",
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
    NOLTE = Sammlung(
        description="Nolte",
        alias="Nolte",
        kreis="Arn",
        ort="Hg",
    )
    NWA = Sammlung(
        description="Niederdeutscher Wortatlas",
        title="NWA",
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
    OSTENDORF = Sammlung(
        description="Ostendorf, J., Den Wäwedamp. Ein Volksspiel in fünf Aufzügen.",
        alias="Ost Wä",
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
    RAUB_SP = Sammlung(
        description="Raub Sp",
        alias="Raub Sp",
    )
    RECKELS = Sammlung(
        description="Reckels, H., Volkskunde des Kreises Steinfurt.",
        alias="Reckels",
        kreis="Stf",
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
    SOESTER_BOERDE_WB = Sammlung(
        description="Schmoeckel, H., u. A. Blesken, Wörterbuch der Soester Börde, ein Beitrag zur westfälischen Mundartenforschung. Soest 1952",
        alias="Wb. Soester Börde",
        kreis="Sos",
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
    WOESTE_WB = Sammlung(
        description="Woeste, F. (J. F. L.), Wörterbuch der westfälischen Mundart. Neu bearb. u. hrsg. v. E. Nörrenberg.",
        alias="Woeste Wb.",
    )
