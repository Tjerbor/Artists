from ast import alias
from datetime import date
import datetime
import json
import tkinter as tk


class Alias:

    def __init__(
        self,
        alias: str,
        parent_artist=None,  # parent artist self is part of
        default_copy_to_clipboard: bool = False,
    ):
        self.parent_artist = parent_artist
        self.alias = tk.StringVar(value=alias)
        self.default_copy_to_clipboard = tk.BooleanVar(value=default_copy_to_clipboard)
        self.add_bool_tracer()

    def set_parent_artist(self, value):
        self.parent_artist = value

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
        def on_boolean_update_alias(var, index, mode):
            self_val = self.default_copy_to_clipboard.get()
            if self_val:
                self.parent_artist.set_new_default(self)
            else:
                if not self.parent_artist.has_default_copy_to_clipboard():
                    self.parent_artist.make_first_alias_default()

        self.default_copy_to_clipboard.trace_add(
            "write", callback=on_boolean_update_alias
        )

    def __repr__(self):
        return f"<Alias alias:{self.alias.get()} bool:{self.default_copy_to_clipboard.get()}>"

    def to_json(self):
        json = {"alias": self.alias.get()}
        if self.is_default_copy_to_clipboard():
            json["is_default"] = self.default_copy_to_clipboard.get()
        return json


class Link:

    def __init__(
        self,
        link: str,
        parent_artist=None,  # parent artist self is part of
        note: str = None,
        default_copy_to_clipboard: bool = False,
    ):
        self.parent_artist = parent_artist
        self.link = tk.StringVar(value=link)
        self.note = tk.StringVar(value=note)
        self.default_copy_to_clipboard = tk.BooleanVar(value=default_copy_to_clipboard)
        self.add_bool_tracer()

    def set_parent_artist(self, value):
        self.parent_artist = value

    def get_note(self):
        return self.note

    def set_note(self, value):
        self.note.set(value)

    def has_note(self):
        return self.note.get() is not None and self.note.get() != ""

    def get_link(self):
        return self.link

    def set_link(self, value):
        self.link.set(value)

    def is_default_copy_to_clipboard(self):
        return self.default_copy_to_clipboard.get()

    def set_default_copy_to_clipboard(self, value):
        self.default_copy_to_clipboard.set(value)

    def get_default_copy_to_clipboard(self):
        return self.default_copy_to_clipboard

    def add_bool_tracer(self):
        def on_boolean_update_link(var, index, mode):
            self_val = self.default_copy_to_clipboard.get()
            if self_val:
                self.parent_artist.set_new_default(self)
            else:
                if not self.parent_artist.has_default_copy_to_clipboard():
                    self.parent_artist.make_first_alias_default()

        self.default_copy_to_clipboard.trace_add(
            "write", callback=on_boolean_update_link
        )

    def __repr__(self):
        return f"<Link link:{self.link.get()} bool:{self.default_copy_to_clipboard.get()} note:{self.note.get()}>"

    def to_json(self):
        json = {"link": self.link.get()}
        if self.is_default_copy_to_clipboard():
            json["is_default"] = self.default_copy_to_clipboard.get()
        if self.has_note():
            json["note"] = self.note.get()
        return json


class Artist:
    def __init__(
        self,
        aliases: list = [""],
        note: str = None,
        links: list = [],
        date_last_checked: date = None,
    ):

        self.aliases = []
        for alias in aliases:
            if isinstance(alias, str):
                self.aliases.append(Alias(alias, self))
            else:
                alias.set_parent_artist(self)
                self.aliases.append(alias)

        self.note = tk.StringVar(value=note)

        self.links = []
        for link in links:
            if isinstance(link, str):
                self.links.append(Link(link, self))
            else:
                link.set_parent_artist(self)
                self.links.append(link)

        if not self.has_default_copy_to_clipboard():
            self.make_first_alias_default()

        self.date_last_checked = date_last_checked

    def get_aliases(self):
        return self.aliases

    def set_aliases(self, value):
        self.aliases = value

    def add_alias(self, alias):
        self.aliases.append(Alias(alias, self, False))

    def remove_alias(self, index):
        del self.aliases[index]
        if not self.has_default_copy_to_clipboard():
            self.make_first_alias_default()

    def get_note(self):
        return self.note

    def set_note(self, value):
        self.note.set(value)

    def has_note(self):
        return self.note.get() is not None and self.note.get() != ""

    def get_links(self):
        return self.links

    def set_links(self, value):
        self.links = value

    def add_link(self, link):
        self.links.append(Link(link, self, default_copy_to_clipboard=False))

    def remove_link(self, index):
        del self.links[index]
        if not self.has_default_copy_to_clipboard():
            self.make_first_alias_default()

    def has_links(self):
        if self.links is not None:
            return len(self.links) > 0

    def get_date_last_checked(self):
        return self.date_last_checked

    def set_date_last_checked(self, value):
        self.date_last_checked = value

    def has_date_last_checked(self):
        return self.date_last_checked is not None

    def has_default_copy_to_clipboard(self) -> bool:
        alias_bools = [
            alias.is_default_copy_to_clipboard() for alias in self.get_aliases()
        ]
        if self.has_links():
            links_bools = [
                link.is_default_copy_to_clipboard() for link in self.get_links()
            ]
            all_bools = alias_bools.extend(links_bools)

        all_bools = alias_bools
        return True in all_bools

    def set_new_default(self, var_new_default):
        if self.has_links():
            aliases_and_links = self.aliases[
                :
            ]  # shallow copy because extend() returns none
            aliases_and_links.extend(self.links)

        else:
            aliases_and_links = self.aliases

        for alias_link in aliases_and_links:
            if (
                alias_link.is_default_copy_to_clipboard()
                and alias_link is not var_new_default
            ):
                alias_link.set_default_copy_to_clipboard(False)
        # var_new_default.set_default_copy_to_clipboard(True)

        # for aliax in self.parent_artist.get_aliases():
        #     if aliax.is_default_copy_to_clipboard():
        #         aliax.set_default_copy_to_clipboard(False)
        #     self.default_copy_to_clipboard.set(True)

    def make_first_alias_default(self):
        if len(self.aliases) > 0:
            self.aliases[0].set_default_copy_to_clipboard(True)

    def __repr__(self):
        return f"<Aritst Aliases:{self.aliases} Note:{self.note.get()} Links:{self.links} last_checked:{self.date_last_checked}>"

    def to_json(self):
        json = {"aliases": [alias.to_json() for alias in self.aliases]}
        if self.has_note():
            json["note"] = self.note.get()
        if self.has_links():
            json["links"] = [link.to_json() for link in self.links]
        if self.has_date_last_checked():
            json["date_last_checked"] = self.date_last_checked
        return json


def write_data_file(list_of_artists):
    json_artists = json.dumps(
        {"artists": [artist.to_json() for artist in list_of_artists]}
    )
    with open(
        f"data/backup_{datetime.datetime.now().timestamp()}.json", "w", encoding="utf-8"
    ) as backup_file:
        backup_file.write(json_artists)
    with open("data/data.json", "w", encoding="utf-8") as data_file:
        data_file.write(json_artists)
    return json_artists


def load_data_file(filepath):
    artists = []
    with open(filepath, "r", encoding="utf-8") as data_file:
        artists_json = json.load(data_file)
    for artist in artists_json["artists"]:
        aliases = []
        for alias in artist["aliases"]:
            alias_string = alias["alias"]
            if "is_default" in alias.keys():
                alias_object = Alias(
                    alias=alias_string, default_copy_to_clipboard=alias["is_default"]
                )
            else:
                alias_object = Alias(alias=alias_string)
            aliases.append(alias_object)

        links = []
        if "links" in artist.keys():
            for link in artist["links"]:
                link_str = link["link"]
                link_object = Link(link=link_str)
                if "note" in link.keys():
                    link_object.set_note(link["note"])
                if "is_default" in link.keys():
                    link_object.set_default_copy_to_clipboard(link["is_default"])
                links.append(link_object)

        note = None
        if "note" in artist.keys():
            note = artist["note"]

        date_last_checked = None
        if "date_last_checked" in artist.keys():
            date_last_checked = artist["date_last_checked"]

        artists.append(
            Artist(
                aliases=aliases,
                note=note,
                links=links,
                date_last_checked=date_last_checked,
            )
        )

    return artists
