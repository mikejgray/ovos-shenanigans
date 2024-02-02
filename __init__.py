from ovos_utils.skill import OVOSSkill


class NewSkill(OVOSSkill):
    def __init__(self, *args, bus=None, **kwargs):
        super().__init__(*args, bus=bus, **kwargs)
