class Configuration(object):
    event_id = ""


gch_config = Configuration()


def create_config_object(config):
    gch_config.event_id = (config["event"])["event-id"]
    gch_config.owner_id = (config["event"])["owner-id"]
    gch_config.token = (config["account"])["token"]
    gch_config.frequency = int((config["search"])["frequency"])
    event = config["event"]
    gch_config.wednesday = event.get("wednesday", "")
    gch_config.thursday  = event.get("thursday", "")
    gch_config.friday    = event.get("friday", "")
    gch_config.saturday  = event.get("saturday", "")
    gch_config.sunday    = event.get("sunday", "")
    gch_config.stay_dates = [d.strip() for d in [
        gch_config.wednesday,
        gch_config.thursday,
        gch_config.friday,
        gch_config.saturday,
        gch_config.sunday
    ] if d and d.strip()]
    gch_config.json_output = (config["web"])["formatted"]
    gch_config.timestamp = (config["web"])["timestamp"]
    return gch_config
