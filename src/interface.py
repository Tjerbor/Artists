from artist import Artist

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

    frame = tk.Frame(root, width=200, height=200)
    frame.pack(padx=10, pady=10)

    a = Artist(
        ["hi", "isisiu", "laskdjflsa", "alsdkfj", "alsdjfl;askjdf"],
        links=["https://iwiwiwi.net"],
    )

    create_artist_frame(a, frame)

    # image = tk.PhotoImage(file="bleh.png")
    # tk.Label(frame, image=image).pack()

    root.mainloop()


def create_artist_frame(artist, root):
    artist_frame = tk.Frame(root)
    artist_frame.pack()
    alias_frame = tk.Frame(artist_frame)
    alias_frame.pack()
    alias_label = tk.Label(alias_frame, text="Alias")
    alias_label.pack(anchor="s")
    first_alias_frame = tk.Frame(alias_frame, padx=10)
    first_alias_frame.pack(anchor="w")
    additional_aliases_frame = tk.Frame(alias_frame, padx=10, pady=5)
    additional_aliases_frame.pack()

    widgets = {}

    add_button_index = len(artist.get_aliases())
    for i, alias in enumerate(artist.get_aliases()):

        if i == 0:
            frame = tk.Frame(first_alias_frame, padx=10)
            # first alias

            aliasvar = alias.get_alias()
            entry = tk.Entry(
                frame,
                textvariable=aliasvar,
            )
            entry.pack(side=tk.LEFT)

            def show_update(*args):
                print(aliasvar.get())
                print(artist)

            aliasvar.trace("w", show_update)

            # necessary step, otherwise artist won't get updated
            boolvar = alias.get_default_copy_to_clipboard()

            checkbox = tk.Checkbutton(
                frame,
                variable=boolvar,
            )
            checkbox.pack()
            frame.pack()

        # second alias
        else:
            frame = tk.Frame(additional_aliases_frame, padx=10)

            aliasvar = alias.get_alias()
            entry = tk.Entry(
                frame,
                textvariable=aliasvar,
            )
            entry.pack(side=tk.LEFT)

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

            checkbox = tk.Checkbutton(frame, variable=boolvar)
            checkbox.pack(side=tk.LEFT)
            button = tk.Button(frame, bg="red")
            button.pack(side=tk.LEFT)

            frame.grid(column=i, row=0)

    add_button_frame = tk.Frame(additional_aliases_frame, padx=10)
    add_button_frame.grid(column=add_button_index, row=0)
    add_button = tk.Button(
        add_button_frame,
        bg="green",
    )
    add_button.pack()


def bool_to_select_tkinter_checkbox(checkbox, b: bool):
    if b:
        checkbox.select()
    else:
        checkbox.deselect()


if __name__ == "__main__":
    main()
