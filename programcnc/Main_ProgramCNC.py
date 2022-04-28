import tkinter as tk
import function_generate as fp


def start_generate():
    """
    Стартовая функция, которая принимает значения "Смещение по Х", "Смещенеие по У",
    "Смещение по Z", "Угол поворота" и передает их в функцию генерации, очищает панель вывода
    затем выводит изменный текст управляющей программы.
    """

    text_input = text_box_input.get("1.0", tk.END)
    try:
        bias_x = float(bias_x_box.get())
        bias_y = float(bias_y_box.get())
        bias_z = float(bias_z_box.get())
        bias_angle = float(bias_angle_box.get())
    except ValueError:
        print("Fuck")

    text_output = fp.generate_nc(text_input, bias_x, bias_y, bias_z, bias_angle)
    text_box_output.delete("1.0", tk.END)
    text_box_output.insert("1.0", text_output)


main_window = tk.Tk()
main_window.title("ProgramCNC")
main_window.minsize(1090, 525)

frame1 = tk.Frame(master=main_window)
frame1.pack(side=tk.TOP, fill=tk.BOTH)

all_sub_frame = ["frame_1", "frame_2", "frame_3", "frame_4", "frame_5"]
all_bias_box = ["bias_x_box", "bias_y_box", "bias_z_box", "bias_angle_box"]

for i, fr_name in enumerate(all_sub_frame):
    if i == 0:
        label_text = "Смещение по X:"
    elif i == 1:
        label_text = "Смещение по Y:"
    elif i == 2:
        label_text = "Смещение по Z:"
    elif i == 3:
        label_text = """Угол поворота:
(по час.+/против-)"""

    locals()[fr_name] = tk.Frame(master=frame1)
    locals()[fr_name].pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    if i < len(all_bias_box):
        label = tk.Label(master=locals()[fr_name], text=label_text, width=15)
        label.config(font=14)
        label.pack(side=tk.LEFT, padx=10, pady=5)

        locals()[all_bias_box[i]] = tk.Entry(master=locals()[fr_name], width=7)
        locals()[all_bias_box[i]].config(font=14)
        locals()[all_bias_box[i]].insert(0, "0")
        locals()[all_bias_box[i]].pack(side=tk.LEFT, padx=5)

else:
    btn_generate_nc = tk.Button(master=locals()[fr_name], text="Сгенерировать", command=start_generate)
    btn_generate_nc.config(width=15, font=14)
    btn_generate_nc.pack(side=tk.RIGHT, padx=10, pady=5)

frame2 = tk.Frame(master=main_window)
frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

text_box_input = tk.Text(frame2, width=50)
text_box_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

text_box_output = tk.Text(frame2, width=50)
text_box_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

frame3 = tk.Frame(master=main_window)
frame3.pack(side=tk.BOTTOM, fill=tk.BOTH)

text_box_output_err = tk.Text(frame3, height=10)
text_box_output_err.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)


main_window.mainloop()
