import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser

import random

import math

from dataclasses import dataclass, field


class Vectors(tk.Frame):

    # Vector dataclass storing all the vector's widgets and values.
    @dataclass
    class Vector(object):

        @dataclass
        class VectorField:

            _vectors: object

            vector_field_frame: tk.Frame  # Frame of the vector field.
            vector_field_left_frame: tk.Frame = field(init=False)  # Left frame of the vector field
            vector_field_right_frame: tk.Frame = field(init=False)  # Right frame of the vector field.
            vector_name_label: tk.Label or tk.Entry = field(init=False)  # Label representing the name of the vector.
            vector_edit_button: tk.Button = field(init=False)  # Button for entering edit mode of name and color.
            vector_color: tk.Frame or tk.Button = field(init=False)  # Frame containing the color of the vector.
            vector_module_label: tk.Label = field(init=False)  # Module label.
            vector_direction_label: tk.Label = field(init=False)  # Direction label.
            vector_x_label: tk.Label = field(init=False)  # x label.
            vector_y_label: tk.Label = field(init=False)  # y label.
            vector_module_stringvar: tk.StringVar  # StringVar of the module's entry.
            vector_direction_stringvar: tk.StringVar  # StringVar of the direction entry.
            vector_x_stringvar: tk.StringVar  # StringVar of the x entry.
            vector_y_stringvar: tk.StringVar  # StringVar of the y entry.
            vector_module_entry: tk.Entry = field(init=False)  # Entry of the vector's module.
            vector_direction_entry: tk.Entry = field(init=False)  # Entry of the vector's direction.
            vector_x_entry: tk.Entry = field(init=False)  # Entry of the vector's x.
            vector_y_entry: tk.Entry = field(init=False)  # Entry of the vector's y.
            vector_button_del: tk.Button = field(init=False)  # Vector's delete button frame.

            COLOR = lambda spam: "#%02X%02X%02X" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            def __post_init__(self):

                def _create_vectorfield_widgets():

                    self.vector_field_left_frame = tk.Frame(self.vector_field_frame)
                    self.vector_field_right_frame = tk.Frame(self.vector_field_frame)
                    self.vector_name_label = tk.Label(self.vector_field_left_frame, text="Vector")
                    self.vector_edit_button = tk.Button(self.vector_field_right_frame, text="Edit", command=lambda: self._vectors.edit_name_color(self))
                    self.vector_color = tk.Frame(self.vector_field_right_frame, width=10, height=10, bg=self.COLOR())
                    self.vector_module_label = tk.Label(self.vector_field_right_frame, text="Module:")
                    self.vector_direction_label = tk.Label(self.vector_field_right_frame, text="Direction:")
                    self.vector_x_label = tk.Label(self.vector_field_right_frame, text="x:", padx=5)
                    self.vector_y_label = tk.Label(self.vector_field_right_frame, text="y:", padx=5)
                    self.vector_module_entry = tk.Entry(self.vector_field_right_frame, text=self.vector_module_stringvar, width=5)
                    self.vector_direction_entry = tk.Entry(self.vector_field_right_frame, text=self.vector_direction_stringvar, width=5)
                    self.vector_x_entry = tk.Entry(self.vector_field_right_frame, text=self.vector_x_stringvar, width=5)
                    self.vector_y_entry = tk.Entry(self.vector_field_right_frame, text=self.vector_y_stringvar, width=5)

                    # del_button_frame = tk.Frame(self.vector_field_left_frame, width=10, height=5)
                    del_button = tk.Button(self.vector_field_left_frame, text="x", fg="red", command=lambda: self._vectors.delete_vector(self))
                    del_button.pack(expand=True, fill="both")

                    self.vector_button_del = del_button

                    return

                def _render_vectorfield_widgets():

                    self.vector_field_frame.pack(fill="x")

                    # Pack left frame

                    self.vector_field_left_frame.place(anchor=tk.NW, width=70, height=70)

                    self.vector_name_label.place(anchor=tk.NW, relx=0.1, rely=0.05)
                    self.vector_button_del.place(anchor=tk.SE, relx=0.5, rely=0.8, width=15, height=15)

                    # Pack right frame

                    self.vector_field_right_frame.place(anchor=tk.NE, relx=1.0, width=150, height=70)

                    # Pack row 0

                    self.vector_edit_button.grid(row=0, column=1)
                    self.vector_color.grid(row=0, column=4)

                    # Pack row 1

                    self.vector_module_label.grid(row=1, column=1)
                    self.vector_module_entry.grid(row=1, column=2)
                    self.vector_x_label.grid(row=1, column=3)
                    self.vector_x_entry.grid(row=1, column=4)

                    # Pack row 2

                    self.vector_direction_label.grid(row=2, column=1)
                    self.vector_direction_entry.grid(row=2, column=2)
                    self.vector_y_label.grid(row=2, column=3)
                    self.vector_y_entry.grid(row=2, column=4)

                    return

                def _trace_vectorfield_entries():

                    self.vector_module_stringvar.trace('w', lambda _, __, ___: self._vectors.compute_components(False, self))
                    self.vector_direction_stringvar.trace('w', lambda _, __, ___: self._vectors.compute_components(False, self))
                    self.vector_x_stringvar.trace('w', lambda _, __, ___: self._vectors.compute_components(True, self))
                    self.vector_y_stringvar.trace('w', lambda _, __, ___: self._vectors.compute_components(True, self))

                    return

                _create_vectorfield_widgets()
                _render_vectorfield_widgets()
                _trace_vectorfield_entries()

                return

        _vectors: object

        _vector_field_frame: tk.Frame

        vector_module: int = 0
        vector_direction: int = 0
        vector_x: int = 0
        vector_y: int = 0

        vector_field: VectorField = None

        def __post_init__(self):
            self.vector_field = self.VectorField(self._vectors,
                                                 tk.Frame(self._vector_field_frame, borderwidth=2, relief='ridge', height=75),
                                                 tk.StringVar(value=self.vector_module),
                                                 tk.StringVar(value=self.vector_direction),
                                                 tk.StringVar(value=self.vector_x),
                                                 tk.StringVar(value=self.vector_y))

            return

    # Initializing constants.
    # Operation names tuple used in the operation_dropdown.
    OPERATIONS = ("Add", "Subtract", "Inner Product", "Scalar Product")

    def __init__(self, master=None):
        super().__init__(master)  # Don't actually know what this does lol

        # Method for setting up the master windows's parameters.
        def _setup_master():

            self.master = master  # Storing the master window variable.

            self.master.title("Vectooors")  # Setting window's title.
            self.master.iconbitmap("icon.ico")
            self.master.geometry("520x300")  # Setting window's dimensions.
            self.master.resizable(False, False)  # Setting the window to non-resizable.

            return

        # Method for creating all the main window's widgets.
        def _create_widgets():

            # Method for initializing the widgets.
            def _init_elements():

                # Initializing the Graph frame.
                self.canvas_frame = tk.Frame(self.master, width=300, height=300)

                # Initializing and resetting the canvas.
                self.canvas = tk.Canvas(self.canvas_frame, bg="black", height=300, width=300)
                self.clear_canvas()

                # Initializing the frame containing the vector fields.
                self.data_frame = tk.Frame(self.master)

                self.visible_vector_fields_frame = tk.Frame(self.data_frame, highlightthickness=0, relief=tk.FLAT)

                self.scrollable_data_frame = tk.Canvas(self.visible_vector_fields_frame, highlightthickness=0, relief=tk.FLAT)

                self.data_frame_scrollbar = tk.Scrollbar(self.visible_vector_fields_frame, command=self.scrollable_data_frame.yview)

                self.vector_field_frame = tk.Frame(self.scrollable_data_frame, highlightthickness=0, relief=tk.FLAT)

                self.vector_field_frame.bind(
                    "<Configure>",
                    lambda e: self.scrollable_data_frame.configure(
                        scrollregion=self.scrollable_data_frame.bbox("all")
                    )
                )

                self.scrollable_data_frame.configure(yscrollcommand=self.data_frame_scrollbar.set)

                # Initializing the frame containing the action buttons.
                self.action_frame = tk.Frame(self.data_frame, borderwidth=1, relief=tk.GROOVE)

                # Initializing the action section:
                # Button to create new vector_fields.
                self.button_new = tk.Button(self.action_frame, text="New", command=self.create_vector)
                # Button to select operation members and compute the operation.
                self.button_select_compute = tk.Button(self.action_frame, text="Select", command=self.select_op_members)
                # Dropdown menu to select the operation.
                self.operation_dropdown = tk.OptionMenu(self.action_frame, self.op, *self.OPERATIONS)

                return

            # Method for rendering the main window's widgets.
            def _render_elements():

                self.button_new.pack(side="right")
                self.operation_dropdown.pack(side="right", expand=True, fill="x")
                self.button_select_compute.pack(side="left")

                self.action_frame.place(anchor=tk.S, relx=0.5, rely=1.0, height=30, width=225)

                self.canvas.pack(side="left")

                self.canvas_frame.place(rely=0.0, relx=0.0, width=300, height=300, anchor=tk.NW)

                self.data_frame.place(relx=1.0, rely=0.0, width=225, height=300, anchor=tk.NE)

                self.visible_vector_fields_frame.place(anchor=tk.NW, height=270, width=225)

                self.data_frame_scrollbar.pack(side="right", fill="y")

                self.scrollable_data_frame.pack()

                self.scrollable_data_frame.create_window((0, 0), window=self.vector_field_frame, anchor=tk.NW, width=205)

                return

            _init_elements()  # Calling the _init_elements method.
            _render_elements()  # Calling the _render_elements method.

            return

        _setup_master()  # Setting up the main window.

        self.modifying_entry = False  # Boolean flag to prevent recursion in the compute_components method.

        # Operation StringVar used in the operation_dropdown.
        self.op = tk.StringVar()
        self.op.set(self.OPERATIONS[0])

        self.vector_fields = []  # List to store Vector objects.

        self.op_members = []  # List to store operation members.

        _create_widgets()  # Creating the main window's widgets.

        return

    # Method for creating new vector_fields.
    """
    # If the vector is created as the result of an operation, the module,
    # direction, x coordinate and y coordinate StringVars are passed as arguments.
    # Else they are initialized to None.
    """
    def create_vector(self, x: int = 0, y: int = 0):

        # Initialize a new vector object.
        current_vector = self.Vector(self, self.vector_field_frame, vector_x=x, vector_y=y).vector_field

        # Stores the vector index in the vector list for reference in the del_button initialization.
        self.vector_fields.append(current_vector)

        return current_vector

    # Method for deleting a Vector object.
    def delete_vector(self, current_vector):

        # Method for removing the vector field and the vector object from the vector list.
        def _forget_vector_field_frame(_current_vector):

            _current_vector.vector_field_frame.pack_forget()  # Remove the vector field.
            self.vector_fields.remove(_current_vector)  # Remove the vector from the vector list.

            return
        
        _forget_vector_field_frame(current_vector)  # Remove the wanted vector.

        # Reset the canvas and redraw the vector_fields with the new colors.
        self.clear_canvas()
        self.draw_on_canvas()

        return

    def edit_name_color(self, current_vector):

        def _finish_edit(_vector_name):

            current_vector.vector_name_label.place_forget()
            _color_button.place_forget()

            current_vector.vector_name_label = tk.Label(current_vector.vector_field_left_frame, text=_vector_name)

            current_vector.vector_name_label.place(anchor=tk.NW, relx=0.1, rely=0.05)

            current_vector.vector_edit_button.configure(command=lambda: self.edit_name_color(current_vector))

            return

        def _get_new_color(_color):
            new_color = tk.colorchooser.askcolor(_color)

            current_vector.vector_color.configure(bg=new_color[1])
            _color_button.configure(bg=new_color[1])

            self.clear_canvas()
            self.draw_on_canvas()

            return

        _current_vector_name = tk.StringVar(value=current_vector.vector_name_label.cget("text"))

        current_vector.vector_name_label.place_forget()

        current_vector.vector_name_label = tk.Entry(current_vector.vector_field_left_frame,
                                                    text=_current_vector_name, width=0)

        current_vector.vector_name_label.place(anchor=tk.NW, relx=0.1, rely=0.05)

        _current_color = current_vector.vector_color["bg"]

        _color_button = tk.Button(current_vector.vector_color, bg=_current_color, command=lambda: _get_new_color(_current_color))
        _color_button.place(width=10, height=10)

        current_vector.vector_edit_button.configure(command=lambda: _finish_edit(_current_vector_name.get()))

        return

    # Method for computing the components of the vector after a parameter modification.
    def compute_components(self, e: bool, current_vector):

        # Checking if another entry is being modified to prevent recursion.
        if self.modifying_entry:
            # If another entry is being modified, return without doing anything.
            return

        # If no other entry is being modified set the modifying_entry variable to True to
        self.modifying_entry = True

        # Check if the cartesian coordinates are being modified.
        if not e:

            # Method for converting the StringVar value to a computable integer.
            def _get_params(_current_vector):

                _m_stringvar_value = _current_vector.vector_module_entry.get()
                _d_stringvar_value = _current_vector.vector_direction_entry.get()

                # Input validation. Checking if the StringVar value is not only numbers.
                if not _m_stringvar_value.isdigit() or not _d_stringvar_value.isdigit():
                    # If any of the StringVar values are not only numbers the input is not validated thus return zeroes.
                    return 0, 0

                # If the input is validated then convert it to a computable integer.
                m = int(_m_stringvar_value)
                d = math.radians(int(_d_stringvar_value))

                # Return the computable integers.
                return m, d

            # Method for computing the cartesian coordinates.
            def _compute_cartesian(_m, _d):

                _x = int(_m * math.cos(_d))
                _y = int(_m * math.sin(_d))

                return _x, _y

            # Methods for updating the vector entries with the new ones.
            def _update_entries(_x, _y, _current_vector):

                _current_vector.vector_x_entry.delete(0, tk.END)
                _current_vector.vector_x_entry.insert(0, _x)

                _current_vector.vector_y_entry.delete(0, tk.END)
                _current_vector.vector_y_entry.insert(0, _y)

                return

            module, direction = _get_params(current_vector)

            x, y = _compute_cartesian(module, direction)

            _update_entries(x, y, current_vector)

        # Else does the same thing but computes the other components.
        else:

            def _get_params(_current_vector):

                _x_stringvar_value = _current_vector.vector_x_entry.get()
                _y_stringvar_value = _current_vector.vector_y_entry.get()

                if not _x_stringvar_value.isdigit() or not _y_stringvar_value.isdigit():
                    return 0, 0

                _x = int(_x_stringvar_value)
                _y = int(_y_stringvar_value)

                return _x, _y

            def _compute_vector(_x, _y):

                _m = int(math.sqrt(math.pow(_x, 2) + math.pow(_y, 2)))
                _d = (int(math.degrees(math.atan((_y / _x)))) if _x != 0 else 90)

                return _m, _d

            def _update_entries(_m, _d, _current_vector):

                _current_vector.vector_module_entry.delete(0, tk.END)
                _current_vector.vector_module_entry.insert(0, _m)
                _current_vector.vector_direction_entry.delete(0, tk.END)
                _current_vector.vector_direction_entry.insert(0, _d)

                return

            x, y = _get_params(current_vector)

            module, direction = _compute_vector(x, y)

            _update_entries(module, direction, current_vector)

        self.draw_on_canvas()

        self.modifying_entry = False

        return

    # Method for drawing the vector_fields on the canvas.
    def draw_on_canvas(self):

        center_x = center_y = 150

        self.clear_canvas()

        for v in range(len(self.vector_fields)):
            if self.vector_fields[v].vector_x_entry.get() != '' and self.vector_fields[v].vector_y_entry.get() != '':
                self.canvas.create_line(center_x, center_y,
                                        (center_x + int(self.vector_fields[v].vector_x_entry.get())),
                                        (center_y - int(self.vector_fields[v].vector_y_entry.get())),
                                        arrow=tk.LAST, fill=self.vector_fields[v].vector_color["bg"])

        return

    # Method for clearing the canvas and redrawing the cartesian axes.
    def clear_canvas(self):

        def _draw_axes():
            self.canvas.create_line(150, 0, 150, 300, fill="#FFF")
            self.canvas.create_line(0, 150, 300, 150, fill="#FFF")

            self.canvas.create_line(200, 148, 200, 153, fill="#FFF")
            self.canvas.create_line(250, 148, 250, 153, fill="#FFF")

            self.canvas.create_line(100, 148, 100, 153, fill="#FFF")
            self.canvas.create_line(50, 148, 50, 153, fill="#FFF")

            self.canvas.create_line(148, 200, 153, 200, fill="#FFF")
            self.canvas.create_line(148, 250, 153, 250, fill="#FFF")

            self.canvas.create_line(148, 100, 153, 100, fill="#FFF")
            self.canvas.create_line(148, 50, 153, 50, fill="#FFF")

            return

        # Clearing the canvas
        self.canvas.delete("all")

        # Redrawing the axes
        _draw_axes()

        return

    # Method fro selecting the operation members.
    def select_op_members(self):

        # Method for selecting or deselecting a vector by adding or removing it from
        # the op_members list and highlighting it in yellow.
        def select(i):
            # If the vector is already selected, deselect it
            if i in self.op_members:
                self.vector_fields[i].vector_field_frame.config(highlightbackground="SystemButtonFace", highlightthickness=0)
                self.op_members.remove(i)
            # If the vector is not in selected, select it.
            else:
                self.vector_fields[i].vector_field_frame.config(highlightbackground="yellow", highlightthickness=1)
                self.op_members.append(i)

        # Go trough the vector list and bind to the right click on the frame of every vector the execution of the select method.
        for v in range(len(self.vector_fields)):
            """
            # This method prevents the vector index from getting "captured" by the lambda function resulting in the
            # selection of only the last vector regardless of the one you click.
            # In other words: the vector index passed to the select method in the lambda function would always be the
            # last one, using the make_lambda method the correct index is memorized and the code runs properly.
            """
            def make_lambda(x):
                return lambda event: select(x)
            self.vector_fields[v].vector_field_frame.bind("<Button-1>", make_lambda(v))
            self.vector_fields[v].vector_field_left_frame.bind("<Button-1>", make_lambda(v))

        # After the selection configure the select button to compute the operation.
        self.button_select_compute.config(text="Compute", command=self.compute_operation)

        return

    def compute_operation(self):

        # Method for resetting the button compute button to the select state and
        # unbinding the vector_fields frame from the select method.
        def _reset():
            for v in range(len(self.vector_fields)):
                self.vector_fields[v].vector_field_frame.unbind("<Button-1>")
                self.vector_fields[v].vector_field_frame.config(highlightbackground="SystemButtonFace", highlightthickness=0)
                self.vector_fields[v].vector_field_left_frame.unbind("<Button-1>")
                self.vector_fields[v].vector_field_left_frame.config(highlightbackground="SystemButtonFace", highlightthickness=0)

            self.button_select_compute.config(text="Select", command=self.select_op_members)

        _reset()

        if not len(self.op_members) == 2:
            tk.messagebox.showerror("Selection Error", "You must select two vector_fields to compute")
            self.op_members.clear()
        else:

            # Memorize the operation to perform.
            _op = self.op.get()

            # Method for adding or subtracting two vector_fields.
            def add_sub():
                _v1_x = int(self.vector_fields[self.op_members[0]].vector_x_entry.get())
                _v1_y = int(self.vector_fields[self.op_members[0]].vector_y_entry.get())

                _v2_x = int(self.vector_fields[self.op_members[1]].vector_x_entry.get())
                _v2_y = int(self.vector_fields[self.op_members[1]].vector_y_entry.get())

                _vr_x = _v1_x + _v2_x if _op == "Add" else _v1_x - _v2_x
                _vr_y = _v1_y + _v2_y if _op == "Add" else _v1_y - _v2_y

                return _vr_x, _vr_y

            # Method for computing the scalar product of two vector_fields.
            def scalar_prod():

                _v1_m = int(self.vector_fields[self.op_members[0]].vector_module_entry.get())
                _v2_m = int(self.vector_fields[self.op_members[1]].vector_module_entry.get())

                _v1_d = int(self.vector_fields[self.op_members[0]].vector_direction_entry.get())
                _v2_d = int(self.vector_fields[self.op_members[1]].vector_direction_entry.get())

                _r = _v1_m * _v2_m * (math.cos(abs((math.radians(_v1_d) - math.radians(_v2_d)))))

                tk.messagebox.showinfo("Scalar Product Result",
                                       f"The scalar product of the two selected vector_fields is \n {_r}")

                return 0, 0

            # Method for computing the inner product of two vector_fields. To be implemented.
            def inner_prod():

                tk.messagebox.showwarning("Work in Progress", "The inner product function has still not been implemented")

                return 0, 0

            # Dictionary to sort the operation method based on the operation name.
            _sort_operation = {
                "Add": add_sub,
                "Subtract": add_sub,
                "Inner Prod.": inner_prod,
                "Scalar Prod.": scalar_prod
            }

            # Performing the operation.
            _r_x, _r_y = _sort_operation[_op]()

            # Empty the op_members list for future operation.
            self.op_members.clear()

            # Finally, if the operation is Add or Subtract, create a new vector with the newly computed components.
            if _op == "Add" or _op == "Subtract":
                _current_vector = self.create_vector(x=_r_x, y=_r_y)
                self.compute_components(e=True, current_vector=_current_vector)

        return


def __main__():

    root = tk.Tk()
    app = Vectors(master=root)
    app.mainloop()

    return


if __name__ == '__main__':
    __main__()
