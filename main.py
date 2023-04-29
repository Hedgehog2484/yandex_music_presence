import time

from pypresence import Presence
from yandex_music import Client


def main():
    client = Client("").init()

    client_id = ""
    RPC = Presence(client_id)
    RPC.connect()

    cur_track_id = 0
    started = time.time()
    artists = "None"
    title = "None"

    while True:
        try:
            queues = client.queues_list()
            last_queue = client.queue(queues[0].id)
            last_track_id = last_queue.get_current_track()
            if last_track_id != cur_track_id:
                cur_track_id = last_track_id
                last_track = last_track_id.fetch_track()
                started = time.time()
                artists = ', '.join(last_track.artists_name())
                title = last_track.title

            RPC.update(
                state=f"{artists} - {title}",
                large_image="logo",
                start=int(started)
            )
            time.sleep(1)
        except:
            time.sleep(1)
