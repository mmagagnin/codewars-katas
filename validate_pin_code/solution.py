def validate_pin(pin):
    if len(pin)==4 or len(pin)==6:
        for n in pin:
            if n not in "0123456789":
                return False
        return True
    return False