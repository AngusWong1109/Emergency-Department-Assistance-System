import PySimpleGUI as gui

layout = [[gui.Text("Hello from PySimpleGUI")], [gui.Button("OK")]]

# Create the window
window = gui.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == gui.WIN_CLOSED:
        break

window.close()