from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent
from TTSHandler import SayText
from utils.debug import DebugPrint
from pygame import mixer
import json
import asyncio
from TextValidation import validate
from collections import deque
import keyboard as kb
import threading

# TODO Adicionar sistema de blacklist e whitelist de texto

with open('config.json', 'r', encoding='UTF-8') as f:
    content = json.load(f)

tiktokUsername = content['username']
ttsCommand = content['command'].strip()
ttsLang = content.get('language') or "en"
skipkey = content.get("skipShortCut")
if not tiktokUsername:
    raise ConnectionError('Username inválido')

mixer.init()
audio_queue = deque()
is_playing = False

client = TikTokLiveClient(unique_id=tiktokUsername)

def extract_user_names(event):
    user = getattr(event, "user_info", None)

    if not user:
        return None, None

    nick = getattr(user, "nick_name", None)
    username = getattr(user, "username", None)

    return nick, username

@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    comment = event.comment
    print(event.user.display_id)
    if ttsCommand == '' or comment.startswith(ttsCommand + ' '):
        print(extract_user_names(event))
        legalText = validate(comment)
        DebugPrint(legalText)
        if legalText:
            audio_path = SayText(legalText, ttsLang)
            audio_queue.append(audio_path)

async def audio_player_loop():
    global is_playing

    while True:
        if not mixer.music.get_busy() and audio_queue:
            next_audio = audio_queue.popleft()
            mixer.music.load(next_audio)
            mixer.music.play()

        await asyncio.sleep(1)


async def main():
    await asyncio.gather(
        client.start(),
        audio_player_loop()
    )

kb.add_hotkey(skipkey,lambda x=1:mixer.music.stop())
asyncio.run(main())
