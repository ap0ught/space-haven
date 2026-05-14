#!/usr/bin/env python3

import io
import xml.etree.ElementTree as ET

SAVE_FILE_NAME = "game"

# Default values as constants
DEFAULT_POINTS = "5"
DEFAULT_TRAIT_ID = "1041"
DEFAULT_SKILL_LEVEL = "10"
DEFAULT_PRIORITY = "Normal"


def process_character(char):
    print("Character:", char.get("name"))
    pers = char.find("pers")
    if pers is None:
        return

    attrs = pers.find("attr")
    if attrs is not None:
        for attr in attrs.findall(".//a"):
            if attr.get("points") != DEFAULT_POINTS:
                print("Attribute:", attr.get("points"), "==>", DEFAULT_POINTS)
                attr.set("points", DEFAULT_POINTS)

    traits = pers.find("traits/t")
    if traits is not None and traits.get("id") != DEFAULT_TRAIT_ID:
        print("Traits:", traits.get("id"), "==>", DEFAULT_TRAIT_ID)
        traits.set("id", DEFAULT_TRAIT_ID)

    edit_jobsettings = False
    skills = pers.find("skills")
    if skills is not None:
        for skill in skills.findall(".//s"):
            if skill.get("level") != DEFAULT_SKILL_LEVEL:
                print("Skill:", skill.attrib, "==>", DEFAULT_SKILL_LEVEL)
                skill.set("level", DEFAULT_SKILL_LEVEL)
                skill.set("mxn", DEFAULT_SKILL_LEVEL)
                edit_jobsettings = True

    if edit_jobsettings:
        jobsetting = pers.find("jobsetting")
        if jobsetting is not None:
            for job in jobsetting.findall(".//j"):
                if job.get("priority") != DEFAULT_PRIORITY:
                    print("Job priority:", job.attrib)
                    job.set("priority", DEFAULT_PRIORITY)


tree = ET.parse(SAVE_FILE_NAME)
root = tree.getroot()

for ship in root.findall(".//ships/ship"):
    if ship.find("settings").get("owner") == "Player":
        print("Ship:", ship.get("sname"))
        for character in ship.findall(".//characters/c"):
            process_character(character)
    else:
        print("Skip:", ship.get("sname"), "owner", ship.find("settings").get("owner"))

xml_buffer = io.BytesIO()
tree.write(xml_buffer, encoding="utf-8", xml_declaration=True)
xml_content = xml_buffer.getvalue().decode("utf-8").replace(" />", "/>")

xml_content = xml_content[xml_content.find(">") + 1 :].strip()

with open(SAVE_FILE_NAME, "w", encoding="utf-8") as file:
    file.write(xml_content)
