from __future__ import annotations
def apply(entries, opening=0):
    bal = opening
    for e in entries:
        bal += int(e["amount"])
    return bal
