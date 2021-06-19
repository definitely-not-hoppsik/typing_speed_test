import PySimpleGUI as sg
import time
import string_comparisons as sc


def calculate_cpm(text, time):
    return len(text)/(time/60)


def calculate_wpm(text, time):
    return (len(text)/5)/(time/60)


sg.theme('DarkAmber')

original_text = 'typing test, type what you see'
layout = [[sg.Text(original_text, size=(80, 10), key='original_text')],
          [sg.Input(key='text_input', size=(80, 10))],
          [sg.Button('start'), sg.Button('stop'), sg.Exit()],
          [sg.Text(size=(10, 1), key='time'),
          sg.Text(size=(10, 1), key='cpm'),
          sg.Text(size=(10, 1), key='wpm'),
          sg.Text(size=(15, 1), key='acc')]]

window = sg.Window('typing speed test', layout)

while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'start':
        start_time = time.time()
        window['text_input']('')

    if event == 'stop':
        stop_time = time.time()
        time_result = stop_time-start_time
        typed_text = values['text_input']

        window['time']('{:.2f}s'.format(time_result))

        cpm = calculate_cpm(
            typed_text, time_result)
        window['cpm'](
            '{:.2f}cpm'.format(cpm))

        wpm = calculate_wpm(
            typed_text, time_result)
        window['wpm'](
            '{:.2f}wpm'.format(wpm))

        acc = sc.naive_comparison(original_text, typed_text)
        window['acc']('{}%'.format(acc))

window.close()
