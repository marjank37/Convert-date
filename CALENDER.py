from ttkbootstrap import Window, Labelframe, Combobox, SUCCESS, Button, Entry, DANGER, Label, PRIMARY
import jdatetime
import datetime


bootstyle_color = DANGER

window = Window(title='Chang the Date')

window.grid_rowconfigure(0, weight=1, minsize=100)
for i in range(3):
    window.grid_columnconfigure(i, weight=1, minsize=100)

# Calendar Type Frame
calendar_type_frame = Labelframe(window, text='Calendar Type', bootstyle=bootstyle_color)
calendar_type_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

calendar_type_combobox = Combobox(calendar_type_frame, values=['Persian to Gregorian', 'Gregorian to Persian'])
calendar_type_combobox.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

def calendar_type_selected(event):
    month_list = []
    month_list_English = ['1-January', '2-February', '3-March', '4-April', '5-May', '6-June',
                          '7-July', '8-August', '9-September', '10-October', '11-November', '12-December']
    month_list_farsi = ['1-فروردین', '2-اردیبهشت', '3-خرداد', '4-تیر', '5-مرداد', '6-شهریور',
                        '7-مهر', '8-آبان', '9-آذر', '10-دی', '11-بهمن', '12-اسفند']

    if calendar_type_combobox.get() == 'Persian to Gregorian':
        month_list.extend(month_list_farsi)
    else:
        month_list.extend(month_list_English)

    month_combobox.config(values=month_list)

calendar_type_combobox.bind('<<ComboboxSelected>>', calendar_type_selected)

# Year Frame
year_frame = Labelframe(window, text='Year', bootstyle=bootstyle_color)
year_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
year_entry = Entry(year_frame)
year_entry.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

# Month Frame
month_frame = Labelframe(window, text='Month', bootstyle=bootstyle_color)
month_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
month_combobox = Combobox(month_frame)
month_combobox.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

# Day Frame
day_frame = Labelframe(window, text='Day', bootstyle=bootstyle_color)
day_frame.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')
day_combobox = Combobox(day_frame, values=[str(i) for i in range(1, 32)])
day_combobox.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

# Labels for output
persian_label = Label(window, text='Persian date', bootstyle=bootstyle_color, font=20)
persian_label.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

gregorian_label = Label(window, text='Gregorian date', bootstyle=bootstyle_color, font=20)
gregorian_label.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')

persian_date_label = Label(window, bootstyle=bootstyle_color)
persian_date_label.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')

gregorian_date_label = Label(window, bootstyle=bootstyle_color)
gregorian_date_label.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

# CHANGE BUTTON
def Change_button_clicked():
    calendar_type = calendar_type_combobox.get()
    year = int(year_entry.get())
    month_split = month_combobox.get().split('-')
    month = int(month_split[0])
    day = int(day_combobox.get())

    if calendar_type == 'Persian to Gregorian':
        persian_date = jdatetime.date(year, month, day)
        gregorian_date = persian_date.togregorian()
        gregorian_date_label.config(text=f'{gregorian_date.strftime("%Y-%m-%d")}')
        persian_date_label.config(text=f'{year}-{month}-{day}')
    else:
        gregorian_date = datetime.date(year, month, day)
        persian_date = jdatetime.date.fromgregorian(date=gregorian_date)
        gregorian_date_label.config(text=f'{year}-{month}-{day}')
        persian_date_label.config(text=f'{persian_date.strftime("%Y-%m-%d")}')

convert_button = Button(window, text='Change', bootstyle=bootstyle_color, command=Change_button_clicked)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

today_label = Label(window, text=f'Today: {datetime.datetime.today().strftime("%Y-%m-%d")}', bootstyle="SECONDARY")
today_label.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')

window.mainloop()
