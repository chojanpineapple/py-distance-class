class Distance:
    def __init__(self, km) -> str:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # --- helpers ---
    def _get_km(self, other) -> str:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    # --- arithmetic ---
    def __add__(self, other) -> str:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return Distance(self.km + km)

    def __iadd__(self, other) -> str:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        self.km += km
        return self

    def __mul__(self, other) -> str:
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)

    def __truediv__(self, other) -> str:
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(round(self.km / other, 2))

    # --- comparisons ---
    def __lt__(self, other) -> str:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km < km

    def __le__(self, other) -> str:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km <= km

    def __gt__(self, other) -> str:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km > km

    def __ge__(self, other) -> str:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km >= km

    def __eq__(self, other) -> str:
        km = self._get_km(other)
        if km is NotImplemented:
            return NotImplemented
        return self.km == km
