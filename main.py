## source ~/.pyenv/versions/myvirtualenvproject/bin/activate

from enum import Enum
from fastapi import FastAPI, HTTPException, Query
from typing import Optional, List
import json
from pydantic import BaseModel

app = FastAPI()

groups =['Isinku', 'Ibere Isin ati Akunleko', 'Ile Orun', 'Coming of Jesus Christ', 'Ojo Isinmi Ope', 'Orin Ajodun Oluwa Temi Kii Saseti', 'Ojo Ibi Kristi', 'Agbara Emi Mimo Olorun', 'Power of Holy Spirit', 'Orin Ikore', 'Orin Osoji', 'Burial', 'Ojo Oluwa', 'Last Super', 'Sunday School', 'Night Hymns', 'Orin Akole', 'Ise Isin', 'Orin Igbeyawo', 'Children Hymns', 'Praise & Thanksgiving Hymns', 'Foundation laying/Church Dedication', 'Additional Hymns', 'Orin Owuro', 'Prayer', 'Kiko tabi Sisi Ile Olorun', 'Orin Omode', 'Orin Isoji', 'Various Hymns', 'Victory Hymns', 'Orin Akokun', 'Oro Olorun', 'The Day of the Lord', 'Faith Hymns', 'Revival Hymns', 'Birth of Christ', 'My God Never Fails Hymns', 'Ojo Awon Eniyan Mimo', 'Ajinde Jesu Oluwa', 'Baptism (Emersion)', 'Opin Odun/Odun Titun', 'Living Water', 'Introit Hymns', 'Day of the Saint', 'Omi Iye', 'End of the Year/New Year', 'Word of God', 'Ipadabo Jesu Kristi', 'Church', 'Orin Ope ati Iyin', 'Morning Hymns', 'Heavenly Home', 'Ijiya ati Iku Jesu', 'Palm Sunday', 'Ounje Ale Oluwa', 'Lent and Repentance', 'Orin Oniruru', 'Marriage Hymns', 'Ile Eko Ojo Isinmi', 'Harvest', 'Baptisimu (Iribomi)', 'Lenti ati Ironupiwada', 'Orin Igbagbo', 'Resurrection of Jesus Christ', 'Worship', 'Adura', 'Crucifixion and Death of Jesus', 'Orin Isegun', 'Ijo Olorun', 'Orin Ale']

class Language(Enum):
    YORUBA = "yoruba"
    ENGLISH = "english"

class Group(Enum):
    ISINKU = "Isinku"
    IBERE_ISIN_ATI_AKUNLEKO = "Ibere Isin ati Akunleko"
    ILE_ORUN = "Ile Orun"
    COMING_OF_JESUS_CHRIST = "Coming of Jesus Christ"
    OJO_ISINMI_OPE = "Ojo Isinmi Ope"
    ORIN_AJODUN_OLUWA_TEMI_KII_SASETI = "Orin Ajodun Oluwa Temi Kii Saseti"
    OJO_IBI_KRISTI = "Ojo Ibi Kristi"
    AGBARA_EMI_MIMO_OLORUN = "Agbara Emi Mimo Olorun"
    POWER_OF_HOLY_SPIRIT = "Power of Holy Spirit"
    ORIN_IKORE = "Orin Ikore"
    ORIN_OSOJI = "Orin Osoji"
    BURIAL = "Burial"
    OJO_OLUWA = "Ojo Oluwa"
    LAST_SUPER = "Last Super"
    SUNDAY_SCHOOL = "Sunday School"
    NIGHT_HYMNS = "Night Hymns"
    ORIN_AKOLE = "Orin Akole"
    ISE_ISIN = "Ise Isin"
    ORIN_IGBEYAWO = "Orin Igbeyawo"
    CHILDREN_HYMNS = "Children Hymns"
    PRAISE_AND_THANKSGIVING_HYMNS = "Praise & Thanksgiving Hymns"
    FOUNDATION_LAYING_CHURCH_DEDICATION = "Foundation laying/Church Dedication"
    ADDITIONAL_HYMNS = "Additional Hymns"
    ORIN_OWURO = "Orin Owuro"
    PRAYER = "Prayer"
    KIKO_TABI_SISI_ILE_OLORUN = "Kiko tabi Sisi Ile Olorun"
    ORIN_OMODE = "Orin Omode"
    ORIN_ISOJI = "Orin Isoji"
    VARIOUS_HYMNS = "Various Hymns"
    VICTORY_HYMNS = "Victory Hymns"
    ORIN_AKOKUN = "Orin Akokun"
    ORO_OLORUN = "Oro Olorun"

class Hymn(BaseModel):
    id: int
    title: str
    language: Language
    group: Group
    tunelink: str
    verses: list[str]
    chorus: str
    addedChorus: str

test_hymns = {
    0: Hymn(
        id=1,
        title="Orin Adura",
        language=Language.YORUBA,
        group=Group.ORO_OLORUN,
        tunelink="https://www.youtube.com/watch?v=1",
        verses=[
            "Orin adura ni mo fe fi han",
            "Ki n le fi han, ki n le fi han",
            "Orin adura ni mo fe fi han",
            "Ki n le fi han, ki n le fi han"
        ],
        chorus="Orin adura ni mo fe fi han",
        addedChorus="Ki n le fi han, ki n le fi han"
    ),
    1: Hymn(
        id=1,
        title="Prayer Hymn",
        language=Language.ENGLISH,
        group=Group.PRAYER,
        tunelink="https://www.youtube.com/watch?v=2",
        verses=[
            "Prayer hymn is what I want to sing",
            "So I can sing, so I can sing",
            "Prayer hymn is what I want to sing",
            "So I can sing, so I can sing"
        ],
        chorus="Prayer hymn is what I want to sing",
        addedChorus="So I can sing, so I can sing"
    ),
    2: Hymn(
        id=2,
        title="Orin Isegun",
        language=Language.YORUBA,
        group=Group.ORIN_ISOJI,
        tunelink="https://www.youtube.com/watch?v=3",
        verses=[
            "Orin isegun ni mo fe fi han",
            "Ki n le fi han, ki n le fi han",
            "Orin isegun ni mo fe fi han",
            "Ki n le fi han, ki n le fi han"
        ],
        chorus="Orin isegun ni mo fe fi han",
        addedChorus="Ki n le fi han, ki n le fi han"
    ),
    3: Hymn(
        id=2,
        title="Victory Hymn",
        language=Language.ENGLISH,
        group=Group.VICTORY_HYMNS,
        tunelink="https://www.youtube.com/watch?v=4",
        verses=[
            "Victory hymn is what I want to sing",
            "So I can sing, so I can sing",
            "Victory hymn is what I want to sing",
            "So I can sing, so I can sing"
        ],
        chorus="Victory hymn is what I want to sing",
        addedChorus="So I can sing, so I can sing"
    )
}

@app.get("/")
def index() -> dict[str,dict[int, Hymn]]:
    return {"hymns": test_hymns}

@app.get("/hymns/{hymn_id}")
def query_hymn_by_id(hymn_id: int) -> Hymn:
    if hymn_id not in test_hymns:
        raise HTTPException(status_code=404, detail=f"Hymn with id {hymn_id} not found")
    return test_hymns[hymn_id]

Selection = dict[str, int |str | Language | Group |str|str|str|str| None]

@app.get("/hymns/")
def query_hymn_by_parameters(
    title: str | None = None,
    language: Language | None = None,
    group: Group | None = None,
    tunelink: str | None = None,
    #verses: list[str] | None = None,
    chorus: str | None = None,
    addedChorus: str | None = None) -> dict[str, Selection]:
    
    def check_hymn(hymn: Hymn) -> bool:
        return all((
            title is None or hymn.title == title,
            language is None or hymn.language == language,
            group is None or hymn.group == group,
            tunelink is None or hymn.tunelink == tunelink,
            #verses is None or hymn.verses == verses,
            chorus is None or hymn.chorus == chorus,
            addedChorus is None or hymn.addedChorus == addedChorus
        ))
    selection = [hymn for hymn in test_hymns.values() if check_hymn(hymn)]
    return {
        "query": {
            "title": title,
            "language": language,
            "group": group,
            "tunelink": tunelink,
            #"verses": verses,
            "chorus": chorus,
            "addedChorus": addedChorus
        },
        "selection": selection
    }

@app.get("/filters")
async def filter_data(
    title: Optional[str] = Query(None, min_length=3, max_length=50),
    #age: Optional[int] = Query(None, gt=0),
    language: Optional[str] = Query(None),
    group: Optional[str] = Query(None, min_length=3, max_length=50),
    tunelink: Optional[str] = Query(None, min_length=3, max_length=500),
    verses: Optional[str] = Query(None),
    chorus: Optional[str] = Query(None),
    addedChorus: Optional[str] = Query(None),
):
    # Filter the dataset based on query parameters
    filtered_data = test_hymns.values()

    if title:
        filtered_data = [item for item in filtered_data if title.lower() in item["title"].lower()]
    if language:
        filtered_data = [item for item in filtered_data if language.lower() in item["language"].lower()]
    if group:
        filtered_data = [item for item in filtered_data if group.lower() in item["group"].lower()]
    if tunelink:
        filtered_data = [item for item in filtered_data if tunelink.lower() in item["tunelink"].lower()]
    if verses:
        filtered_data = [item for item in filtered_data if verses.lower() in item["verses"].lower()]
    if chorus:
        filtered_data = [item for item in filtered_data if chorus.lower() in item["chorus"].lower()]
    if addedChorus:
        filtered_data = [item for item in filtered_data if addedChorus.lower() in item["addedChorus"].lower()]
    return filtered_data
'''
    if age:
        filtered_data = [item for item in filtered_data if item["age"] == age]
    if verses:
        filtered_data = [item for item in filtered_data if verses.lower() in [s.lower() for s in item["verses"]]]
'''
hymns =[{
    "id": 170,
    "title": "Ife pipe to ta ero gbogbo yo",
    "language": "yoruba",
    "group": "Orin Igbeyawo",
    "tunelink": [
        "https://www.ileewe.org/hymns/101-150/audios/Hymn%20150.mp3"
    ],
    "verses": [
        [
            "1.Ife pipe to ta ero gbogbo yo",
            "N' irele a wole n' waju 'te Re",
            "Je k'ife won je ife ti ko lopin",
            "Awon wonyii ti 'Wo dapo sokan."
        ],
        [
            "2.'Wo orisun iye satilehin won",
            "Fun won n' Ife oun gbagbo ailopin",
            "Suuru ireti pelu ipamora",
            "Ifokantan tiko siyemeji,"
        ],
        [
            "3.Fun won l'ayo t' o bori gbogbo ara",
            "Alaafia to bori wahala",
            "F’adun ife mimo si ojo aye won",
            "Titi won o wole ayeraye.    Amin."
        ]
    ],
    "chorus": [
        "Ife mimo, ife mimo, ife mimo",
        "Ife didan, ife didan, ife didan",
        "Ife pipe, ife pipe, ife pipe",
        "Ife titan, ife titan, ife titan"
    ],
    "addedChorus": [
                "D'odi mu, Emi rere de,",
                "Beni Jesu wi",
                "Ran 'dahun pada s'orun pe",
                "Awa o dimu."
    ]
},
{
    "id": 170,
    "title": "O perfect Love, all human thought transcending,",
    "language": "english",
    "group": "Marriage Hymns",
    "tunelink": [
        "https://www.ileewe.org/hymns/101-150/audios/Hymn%20150.mp3"
    ],
    "verses": [
        [
            "1. O perfect Love, all human thought transcending,",
            "Lowly we kneel in prayer before Thy throne,",
            "That theirs may be the love which knows no ending,",
            "Whom Thou forevermore dost join in one."
        ],
        [
            "2.O perfect Life, be Thou their full assurance,",
            "Of tender charity and steadfast faith,",
            "Of patient hope and quiet, brave endurance,",
            "With childlike trust that fears nor pain nor death."
        ],
        [
            "3.Grant them the joy which brightens earthly sorrow;",
            "Grant them the peace which calms all earthly strife,",
            "And to life’s day the glorious unknown morrow",
            "That dawns upon eternal love and life.",
            "Amen."
        ]
    ],
    "chorus": [
        "O perfect Love, all human thought transcending,",
        "Lowly we kneel in prayer before Thy throne,",
        "That theirs may be the love which knows no ending,",
        "Whom Thou forevermore dost join in one."

    ],
    "addedChorus": [
        "Hold the fort, for I am coming,",
        "Jesus signals still",
        "Wave the answer back to Heaven,",
        "By Thy grace we will."
    ]
}]

dataset = [
    {"name": "John", "age": 30, "skills": ["Python", "Java", "C++"]},
    {"name": "Jane", "age": 25, "skills": ["Python", "JavaScript"]},
    {"name": "Alice", "age": 28, "skills": ["Python", "Ruby", "Go"]},
    {"name": "Bob", "age": 35, "skills": ["Java", "C++"]},
]

# Define a route that handles filtering of the dataset
@app.get("/filter")
async def filter_data(
    name: Optional[str] = Query(None, min_length=3, max_length=50),
    age: Optional[int] = Query(None, gt=0),
    skill: Optional[str] = Query(None)
):
    # Filter the dataset based on query parameters
    filtered_data = dataset

    if name: #<arg>
        filtered_data = [item for item in filtered_data if name.lower() in item["name"].lower()]
    if age:#<arg>
        filtered_data = [item for item in filtered_data if item["age"] == age]
    if skill:#<arg>
        filtered_data = [item for item in filtered_data if skill.lower() in [s.lower() for s in item["skills"]]]

    return filtered_data


# Define a route that handles filtering of the dataset
@app.get("/filterx")
async def filter_data(
    title: Optional[str] = Query(None, min_length=3, max_length=50),
    language: Optional[str] = Query(None),
    group: Optional[str] = Query(None),
    #age: Optional[int] = Query(None, gt=0),
    verses: Optional[str] = Query(None),
    chorus: Optional[str] = Query(None),
    addedChorus: Optional[str] = Query(None)
):
    # Filter the dataset based on query parameters
    filtered_hymns = hymns
    
    if title: #<arg>
        filtered_hymns = [item for item in filtered_hymns if title.lower() in item["title"].lower()]
    if language:#<arg>
        filtered_hymns = [item for item in filtered_hymns if language.lower() in item["language"].lower()]
    if group: #<arg>
        filtered_hymns = [item for item in filtered_hymns if group.lower() in item["group"].lower()]
    if verses:#<arg>
        filtered_hymns = [item for item in filtered_hymns if any(verses.lower() in verse_line for verse_line in [t.lower()  for s in item["verses"] for t in s])]
    if chorus: #<arg>
        filtered_hymns = [item for item in filtered_hymns if any(chorus.lower() in verse_line for verse_line in [s.lower() for s in item["chorus"]])]
    if addedChorus: #<arg>
        filtered_hymns = [item for item in filtered_hymns if any(addedChorus.lower() in verse_line for verse_line in [s.lower() for s in item["addedChorus"]])]
    #if verses:#<arg>
        #filtered_hymns = [item for item in filtered_hymns if verses.lower() in [t.lower() for verse in item["verses"] for s in verse for t in s]]
    #if verses:#<arg>
        #filtered_hymns = [item for item in filtered_hymns if any(verses.lower() in verse_line for verse_line in [t.lower() for verse in item["verses"] for s in verse for t in s])]
    #if verses:#<arg>
        #filtered_hymns = [item for item in filtered_hymns if any(verses.lower() in verse_line for verse_line in [s.lower() for verse in item["verses"] for s in verse])]
    #if verses:#<arg>
        #filtered_hymns = [item for item in filtered_hymns if verses.lower() in [s.lower() for verse in item["verses"] for s in verse]]
    #if skill:#<arg>
        #filtered_hymns = [item for item in filtered_hymns if skill.lower() in [s.lower() for s in item["skills"]]]

    return filtered_hymns