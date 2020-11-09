class Transition:
    def __init__(self, _from, _value, _to):
        self._from = _from
        self._value = _value
        self._to = _to

    def __str__(self):
        return self._from + " -" + self._value + "-> " + self._to

    def get_from_state(self):
        return self._from

    def get_to_state(self):
        return self._to

    def get_value(self):
        return self._value
