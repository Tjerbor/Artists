from datetime import date
from encodings import aliases
import tkinter as tk


class Alias:
    def __init__(
        self,
        aliases: list,  # parent list self is part of
        alias: str,
        default_copy_to_clipboard: bool = False,
    ):
        self.aliases = aliases
        self.alias = tk.StringVar(value=alias)
        self.default_copy_to_clipboard = tk.BooleanVar(value=default_copy_to_clipboard)
        self.add_bool_tracer()

    def get_alias(self):
        return self.alias

    def set_alias(self, value):
        self.alias.set(value)

    def is_default_copy_to_clipboard(self):
        return self.default_copy_to_clipboard.get()

    def set_default_copy_to_clipboard(self, value):
        self.default_copy_to_clipboard.set(value)

    def get_default_copy_to_clipboard(self):
        return self.default_copy_to_clipboard

    def add_bool_tracer(self):
        def on_boolean_update(var, index, mode):
            self_val = self.default_copy_to_clipboard.get()

            for aliax in self.aliases:
                aliax.set_default_copy_to_clipboard(False)
            if self_val:
                self.default_copy_to_clipboard.set(True)

        self.default_copy_to_clipboard.trace_add("write", callback=on_boolean_update)

    def __repr__(self):
        return f"<Alias alias:{self.alias.get()} bool:{self.default_copy_to_clipboard.get()}>"


class Link:

    def __init__(
        self, link: str, note: str = None, default_copy_to_clipboard: bool = False
    ):
        self.link = tk.StringVar(value=link)
        self.note = tk.StringVar(value=note)
        self.default_copy_to_clipboard = tk.BooleanVar(value=default_copy_to_clipboard)

    def get_note(self):
        return self.note

    def set_note(self, value):
        self.note.set(value)

    def has_note(self):
        return self.note.get() is not None or self.note.get != ""

    def get_link(self):
        return self.link

    def set_link(self, value):
        self.link.set(value)

    def is_default_copy_to_clipboard(self):
        return self.default_copy_to_clipboard.get()

    def set_default_copy_to_clipboard(self, value):
        self.default_copy_to_clipboard.set(value)

    def __repr__(self):
        return f"<Link link:{self.link.get()} bool:{self.default_copy_to_clipboard.get()} note:{self.note.get()}>"


class Artist:
    def __init__(
        self,
        aliases: list = [""],
        note: str = None,
        links: list = [],
        date_last_checked: date = None,
    ):

        aliaxes = []
        for i, alias in enumerate(aliases):
            if i == 0:
                aliaxes.append(Alias(aliaxes, alias, True))
            else:
                aliaxes.append(Alias(aliaxes, alias, False))

        self.aliases = aliaxes

        self.note = tk.StringVar(value=note)

        if links is not None:
            self.links = list(map(lambda a: Link(a), links))

        else:
            self.links = links

        self.date_last_checked = date_last_checked

    def get_aliases(self):
        return self.aliases

    def set_aliases(self, value):
        self.aliases = value

    def get_note(self):
        return self.note

    def set_note(self, value):
        self.note.set(value)

    def has_note(self):
        return self.note.get() is not None or self.note.get() != ""

    def get_links(self):
        return self.links

    def set_links(self, value):
        self.links = value

    def has_links(self):
        return self.links is not None or len(self.links) > 0

    def get_date_last_checked(self):
        return self.date_last_checked

    def set_date_last_checked(self, value):
        self.date_last_checked = value

    def has_date_last_checked(self):
        return self.date_last_checked is not None

    def has_default_copy_to_clipboard(self) -> bool:
        alias_bools = [
            alias.is_default_copy_to_clipboard() for alias in self.get_ALIASES()
        ]
        links_bools = [link.is_default_copy_to_clipboard() for link in self.get_LINKS()]

        all_bools = alias_bools.extend(links_bools)
        return True in all_bools

    def __repr__(self):
        return f"<Aritst Aliases:{self.aliases} Note:{self.note.get()} Links:{self.links} last_checked:{self.date_last_checked}>"
