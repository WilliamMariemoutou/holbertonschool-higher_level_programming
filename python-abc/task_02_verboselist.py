#!/usr/bin/python3
"""creates the verboselist class"""


class VerboseList(list):
    """appends an item to the list"""
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """extends the list"""
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        """remove an item from the list"""
        if item in self:
            super().remove(item)
            print(f"Removed {item} from the list.")

    def pop(self, index=-1):
        """pop an item from the list"""
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
