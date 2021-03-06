from maya import cmds
from pyblish_magenta.vendor import inflection


# (key, value, help)
defaults = [
    ("name", lambda name, family: name,
        "Name of instance"),
    ("family", lambda name, family: family,
        "Which family to associate this instance with"),
    ("label", lambda name, family: inflection.titleize(name),
        "Optional label for this instance, used in GUIs"),
    ("subset", lambda name, family: "default",
        "Which subset to associate this instance with"),
    ("category", lambda name, family: "",
        "Optional category used as metadata by other tools"),
    ("tags", lambda name, family: "",
        "A space-separated series of tags to imprint with cQuery"),
]

families = {
    "model": [],
    "rig": [],
    "look": [],
    "pointcache": [],
    "animation": []
}


def create(name, family, use_selection=False):
    if not use_selection:
        cmds.select(deselect=True)

    instance = cmds.sets(name=name + "_INST")

    for key, value, _ in defaults + families[family]:
        cmds.addAttr(instance, ln=key, **attributes[key]["add"])
        cmds.setAttr(instance + "." + key,
                     value(name, family),
                     **attributes[key]["set"])


attributes = {
    "publish": {
        "add": {"attributeType": "bool"},
        "set": {}
    },
    "family": {
        "add": {"dataType": "string"},
        "set": {"type": "string"}
    },
    "category": {
        "add": {"dataType": "string"},
        "set": {"type": "string"}
    },
    "name": {
        "add": {"dataType": "string"},
        "set": {"type": "string"}
    },
    "label": {
        "add": {"dataType": "string"},
        "set": {"type": "string"}
    },
    "subset": {
        "add": {"dataType": "string"},
        "set": {"type": "string"}
    },
    "tags": {
        "add": {"dataType": "string"},
        "set": {"type": "string"}
    },
}
