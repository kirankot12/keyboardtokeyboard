import pyautogui
import mido

midi_note_to_key = {
    59: "w",
    60: "a",
    62:"d",
    64:"s",
    57:"shift",
    65:"space"

}

input_port_name = "USB Keyboard 0"

with mido.open_input(input_port_name) as port:
    for message in port:
        if message.type == 'note_on':
            midi_note = message.note
            if midi_note in midi_note_to_key:
                key = midi_note_to_key[midi_note]
                pyautogui.press(key)