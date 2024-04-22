from dataclasses import dataclass, field, asdict

@dataclass
class ISOData:
    alpha_2: str = field(default=None)
    alpha_3: str = field(default=None)
    numeric: str = field(default=None)

@dataclass
class FlagData:
    emoji: str = field(default=None)
    url: str = field(default=None)


"""
    "AX": {
        "name": "\u00c5land Islands",
        "region": "Europe",
        "timezones": {
            "Europe\/Mariehamn": "+03:00"
        },
        "iso": {
            "alpha_2": "AX",
            "alpha_3": "ALA",
            "numeric": "248"
        },
        "phone": [
            "+358-18"
        ],
        "emoji": "\ud83c\udde6\ud83c\uddfd",
        "image": "https:\/\/cdn.jsdelivr.net\/npm\/country-flag-emoji-json@2.0.0\/dist\/images\/AX.svg"
    }
"""

@dataclass
class CountryData:
    name: str = field(default=None, init=False)
    iso: ISOData = field(default_factory=ISOData, init=False)
    dial_codes: list[str] = field(default_factory=list, init=False)
    flag: FlagData = field(default_factory=FlagData, init=False)
    __data: dict = field(repr=False)

    def __post_init__(self):
        self.name = self.__data.get("name")
        iso = self.__data.get("iso")
        self.iso.alpha_2 = iso.get("alpha_2")
        self.iso.alpha_3 = iso.get("alpha_3")
        self.iso.numeric = iso.get("numeric")
        self.dial_codes = self.__data.get("dial_codes")
        self.flag.emoji = self.__data.get("emoji")
        self.flag.url = self.__data.get("image")
        del self.__data

    def as_dict(self):
        return asdict(self)
    
    
