import PySimpleGUI as sg
import converter
sg.theme('Black')
feet_text = sg.Text('Enter Feet')
feet_text_input = sg.InputText(key='Feet')
inches_text = sg.Text('Enter inches')
inches_text_input = sg.InputText(key='Inches')
conver_button = sg.Button('Convert')
exit_button = sg.Button('Exit', key='exit_button')

output = sg.Text(key='Output')
window = sg.Window(title='Converter', layout=[[feet_text,feet_text_input],
                                              [inches_text,inches_text_input],[conver_button,exit_button, output]])

while True:
    event, values = window.read()
    print(event, values)
    inches = values['Inches']
    feet = values['Feet']
    print(inches, feet)
    match event:
        case 'Convert':
            window['Output'].update(value=f'{converter.converter(int(feet), int(inches))} m', text_color='red')
        case 'exit_button':
            break
window.Close

