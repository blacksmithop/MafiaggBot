options = {
    "daylength": {
        "true": "dayLength",
        "minmax": [3, 20],
        "allowed": "int",
    },  # day length
    "daystart": {
        "true": "dayStart",
        "allowed": "str",
        "options": ["informed", "uninformed", "off", "nokill"],
        "translate": {
            "uninformed": "dayStart",
            "off": "off",
            "informed": "dawnStart",
            "nokill": "mafiaNKn1",
        },
    },
    "deadlock": {
        "true": "deadlockPreventionLimit",
        "translate": {"random": -1, "initiator": 5, "responder": 6, "meteor": -2},
        "allowed": "str",
        "options": ["random", "initiator", "responder", "meteor"],
    },
    "votelock": {  # toggle vote lock
        "true": "disableVoteLock",
        "allowed": "bool",
    },
    "scaletimer": {  # auto-scale timer
        "true": "scaleTimer",
        "allowed": "bool",
    },
    "nightlength": {
        "true": "nightLength",
        "minmax": [1, 9],
        "allowed": "int",
    },  # night length
    "nighttalk": {  # toggle night talk
        "true": "noNightTalk",
        "allowed": "bool",
    },
    "hidesetup": {"true": "hideSetup", "allowed": "bool"},  # hide setups
    "hostrole": {
        "true": "hostRoleSelection",
        "allowed": "bool",
    },  # allow host to select role
    "mustvote": {"true": "mustVote", "allowed": "bool"},  # must vote
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
        "options": ["yes", "no", "2", "3", "5", "6", "7"],
        "translate": {
            "yes": "1",
            "no": "0",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
        },
    },
    "majority": {
        "true": "majorityRule",
        "allowed": "str",
        "translate": {"simple": "51", "off": "-1", "2/3": "66", "3/4": "75"},
        "options": ["simple", "off", "2/3", "3/4"],
    },
    "townlosesafter": {  # town loses after
        "true": "killAllTownAfterTooManyMiscondemns",
        "minmax": [0, 20],
        "allowed": "int",
    },
    "mafialosesafter": {  # mafia loses after
        "true": "killAllMafiaAfterSomeDie",
        "minmax": [0, 10],
        "allowed": "int",
    },
}

str2bool = {"True": True, "False": False}


class EditSetting:
    edits = options

    def __init__(self) -> None:
        self.allowed_values = list(self.edits.keys())
        
    def is_valid(self, option):
        return self.edits.get(option)

    def edit_options(self, option, newvalue) -> [None, dict, bool]:
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
