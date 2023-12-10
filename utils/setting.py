from utils.customtypes import DeckDict

options = {
    "daylength": {"true": "dayLength", "minmax": [3, 20], "allowed": "int"},
    "nightlength": {"true": "nightLength", "minmax": [3, 20], "allowed": "int"},
    "daystart": {
        "true": "dayStart",
        "allowed": "str",
        "options": ["informed", "uninformed", "off"],
        "translate": {"uninformed": "dayStart", "off": "off", "informed": "dawnStart"},
    },
    "deadlock": {
        "true": "deadlockPreventionLimit",
        "translate": {"random": -1, "initiator": 5, "responder": 6, "meteor": -2},
        "allowed": "str",
        "options": ["random", "initiator", "responder", "meteor"],
    },
    "votelock": {
        "true": "disableVoteLock",
        "allowed": "bool",
    },
    "hidesetup": {"true": "hideSetup", "allowed": "bool"},
    "hostrole": {"true": "hostRoleSelection", "allowed": "bool"},
    "mustvote": {"true": "mustVote", "allowed": "bool"},
    "nonighttalk": {"true": "noNightTalk", "allowed": "bool"},
    "scaletimer": {"true": "scaleTimer", "allowed": "bool"},
    "reveal": {
        "true": "revealSetting",
        "allowed": "str",
        "options": ["on", "alignment", "off"],
        "translate": {
            "alignment": "alignmentReveal",
            "on": "allReveal",
            "off": "noReveal",
        },
    },
    "killpower": {
        "true": "twoKp",
        "allowed": "str",
        "options": ["yes", "no"],
        "translate": {"yes": "1", "no": "0"},
    },
    "majority": {
        "true": "majorityRule",
        "allowed": "str",
        "translate": {"simple": "51", "off": "-1", "2/3": "66", "3/4": "75"},
        "options": ["simple", "off", "2/3", "3/4"],
    },
}

str2bool = {"True": True, "False": False}


class Setting:
    edits = DeckDict(options)

    def is_valid(self, option):
        return self.edits.get(option)

    def edit_option(self, option, newvalue) -> [None, dict, bool]:
        option = self.is_valid(option)
        if option is None:
            return
        if option["allowed"] == "str":
            if newvalue in option["options"]:
                if "translate" in option:
                    newvalue = option["translate"][newvalue]
            else:
                return False
        elif option["allowed"] == "bool":
            if newvalue.title() in ["True", "False"]:
                newvalue = str2bool[newvalue.title()]
            else:
                return False
        elif option["allowed"] == "int":
            try:
                newvalue = int(newvalue)
            except ValueError:
                return False
            if not option["minmax"][0] <= newvalue <= option["minmax"][1]:
                return False

        return {"type": "options", option["true"]: newvalue}
