import datetime
from functools import partial
import json
from pydoc import text
from random import Random, random
import webbrowser

import pyperclip
from artist import Artist, load_data_file, write_data_file

import tkinter as tk


def main():
    root = tk.Tk()
    root.title("TJ Artist Collection :)")
    root.configure(background="skyblue")
    root.minsize(200, 200)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.maxsize(screen_width, screen_height)
    root.geometry(
        f"{int(screen_width* 2/3)}x{int(screen_height* 2/3)}+{int(screen_width * 1/6)}+{int(screen_height*1/6)}"
    )

    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack(padx=10, pady=10)

    def on_closing():
        # print(write_data_file(runtime_artists))
        write_data_file(runtime_artists)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # runtime_artists = [
    #     Artist(
    #         ["hi", "1", "2", "3", "4"],
    #         links=[
    #             "https://iwiwiwi.net",
    #             "https://www.youtube.com/watch?v=jE-SpRI3K5g",
    #         ],
    #     ),
    #     Artist(["damn son"]),
    # ]

    runtime_artists = load_data_file("data/data.json")
    # runtime_artists = []
    # with open(
    #     "data/artist to check out regularly.txt", "r", encoding="utf-8"
    # ) as regular:
    #     runtime_artists.extend(
    #         list(map(lambda x: Artist([x]), regular.read().splitlines()))
    #     )

    for artist in runtime_artists:
        orderframe = tk.Frame(canvas, bg="grey", padx=10, pady=5)
        orderframe.pack()
        create_artist_frame(artist, orderframe)

    # image = tk.PhotoImage(file="bleh.png")
    # tk.Label(frame, image=image).pack()

    root.mainloop()


def create_artist_frame(artist, root):
    artist_top_frame = tk.Frame(root, bg="skyblue")
    artist_top_frame.pack()
    create_alias_frame(artist, artist_top_frame)
    create_links_frame(artist, root)


def create_alias_frame(artist, root):
    alias_frame = tk.Frame(root)
    alias_frame.pack()
    alias_label = tk.Label(alias_frame, text="Alias")
    alias_label.pack(anchor="s")
    first_alias_frame = tk.Frame(alias_frame, padx=10)
    first_alias_frame.pack(anchor="w")
    additional_aliases_frame = tk.Frame(alias_frame, padx=10, pady=5)
    additional_aliases_frame.pack()

    add_button_index = len(artist.get_aliases())

    def copy_alias(alias_variable):
        pyperclip.copy(alias_variable.get())

    def open_url(url):
        webbrowser.open(url)

    for i, alias in enumerate(artist.get_aliases()):

        if i == 0:
            frame = tk.Frame(first_alias_frame, padx=10)
            frame.pack()
            # first alias

            aliasvar = alias.get_alias()
            entry = tk.Entry(
                frame,
                textvariable=aliasvar,
            )
            entry.pack(side=tk.LEFT, fill="x", expand=True)

            def show_update(*args):
                print(aliasvar.get())
                print(artist)

            aliasvar.trace("w", show_update)

            copy_button = tk.Button(
                frame,
                bg="skyblue",
                text="C",
                compound=tk.LEFT,
                command=partial(copy_alias, aliasvar),
            )
            copy_button.pack(side=tk.LEFT, fill="x", expand=True)

            # necessary step, otherwise artist won't get updated
            boolvar = alias.get_default_copy_to_clipboard()

            checkbox = tk.Checkbutton(
                frame,
                variable=boolvar,
            )
            checkbox.pack(side=tk.LEFT, fill="x", expand=True)

            soundcloud_button = tk.Button(
                frame,
                bg="#FF6103",
                text="sc",
                command=partial(
                    open_url, f"https://soundcloud.com/search/people?q={aliasvar.get()}"
                ),
            )
            soundcloud_button.pack(side=tk.LEFT, fill="x", expand=True)

            deezer_button = tk.Button(
                frame,
                bg="#8A2BE2",
                text="D",
                command=partial(
                    open_url, f"https://www.deezer.com/search/{aliasvar.get()}"
                ),
            )
            deezer_button.pack(side=tk.LEFT, fill="x", expand=True)

        # second alias
        else:
            frame = tk.Frame(additional_aliases_frame, padx=10)

            aliasvar = alias.get_alias()
            entry = tk.Entry(
                frame,
                textvariable=aliasvar,
            )
            entry.pack(side=tk.LEFT, fill="x", expand=True)

            def show_update(*args):
                print(aliasvar.get())
                print(artist)

            aliasvar.trace("w", show_update)

            boolvar = alias.get_default_copy_to_clipboard()

            # def update_bool(var, index, mode):
            #     if widgets[var].get():
            #         artist.set_new_default(widgets[var])
            #         print(artist)

            # boolvar.trace_add(
            #     "write",
            #     callback=lambda x, y, z: update_bool(x, y, z),
            # )

            # widgets[str(boolvar)] = boolvar

            copy_button = tk.Button(
                frame,
                bg="skyblue",
                text="C",
                compound=tk.LEFT,
                command=partial(copy_alias, aliasvar),
            )
            copy_button.pack(side=tk.LEFT, fill="x", expand=True)

            def remove_alias(index: int):
                artist.remove_alias(index)
                alias_frame.destroy()
                create_alias_frame(artist, root)

            checkbox = tk.Checkbutton(frame, variable=boolvar)
            checkbox.pack(side=tk.LEFT)
            button = tk.Button(
                frame, bg="red", text="-", command=partial(remove_alias, i)
            )
            button.pack(side=tk.LEFT)
            frame.grid(column=i, row=0)

    add_button_frame = tk.Frame(additional_aliases_frame, padx=10)
    add_button_frame.grid(column=add_button_index, row=0)

    def add_alias():
        artist.add_alias("")
        alias_frame.destroy()
        create_alias_frame(artist, root)

    add_button = tk.Button(
        add_button_frame,
        command=add_alias,
        text="+",
        bg="light green",
    )

    add_button.pack()


def create_links_frame(artist, root):
    links_top_frame = tk.Frame(root, bg="skyblue")
    links_top_frame.pack()
    label = tk.Label(links_top_frame, text="Links")
    label.pack()
    links_frame = tk.Frame(links_top_frame)
    links_frame.pack()

    def copy_link(link_variable):
        pyperclip.copy(link_variable.get())

    def open_link(link_varible):
        webbrowser.open(link_varible.get())

    add_button_index = len(artist.get_links())
    for i, link in enumerate(artist.get_links()):
        frame = tk.Frame(links_frame)
        frame.pack()

        notevar = link.get_note()
        note_entry = tk.Entry(frame, textvariable=notevar)
        note_entry.grid(column=0, row=i)

        linkvar = link.get_link()
        link_entry = tk.Entry(frame, textvariable=linkvar)
        link_entry.grid(column=1, row=i)

        copy_button = tk.Button(
            frame, bg="skyblue", text="C", command=partial(copy_link, linkvar)
        )
        copy_button.grid(column=2, row=i)

        open_link_button = tk.Button(
            frame, bg="grey", text="->", command=partial(open_link, linkvar)
        )
        open_link_button.grid(column=3, row=i)

        boolvar = link.get_default_copy_to_clipboard()

        checkbox = tk.Checkbutton(frame, variable=boolvar)
        checkbox.grid(column=4, row=i)

        def remove_link(index):
            artist.remove_link(index)
            links_top_frame.destroy()
            create_links_frame(artist, root)

        delete_button = tk.Button(
            frame, bg="red", text="-", command=partial(remove_link, i)
        )
        delete_button.grid(column=5, row=i)

    add_button_frame = tk.Frame(links_frame)
    add_button_frame.pack()

    def add_link():
        artist.add_link("")
        links_top_frame.destroy()
        create_links_frame(artist, root)

    add_button = tk.Button(
        add_button_frame, bg="light green", text="C", command=add_link
    )
    add_button.pack()


def bool_to_select_tkinter_checkbox(checkbox, b: bool):
    if b:
        checkbox.select()
    else:
        checkbox.deselect()


if __name__ == "__main__":
    main()
