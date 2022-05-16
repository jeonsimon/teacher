from winsound import Beep
import re


class Note:
    notes = ('도', '도#', '레', '레#', '미', '파', '파#', '솔', '솔#', '라', '라#', '시')

    @staticmethod
    def play(note: str, duration: int, octave: int = 0):
        if mat := Note._get_octave(note):
            note, octave = mat

        freq = 2 ** (4 + int(octave)) * 55 * 2 ** ((Note.notes.index(note) - 10) / 12)
        Beep(int(freq), duration)
        print(f"{note} {octave}")

    @staticmethod
    def _get_octave(note: str):
        if mat := re.search(r"(?P<note>\S+)(?P<octave>\d)$", note):
            return mat.groups()


class Player:
    sharp = ('파', '도', '솔', '레', '라', '미', '시')

    def __init__(self):
        self.song = ''
        self.num_sharp = 0

    def add_song(self, song: str):
        self.song = song
        return self

    def set_sharp(self, num: int):
        self.num_sharp = num
        return self

    def _to_major(self):
        for i in range(self.num_sharp):
            self.song = self.song.replace(Player.sharp[i], f"{Player.sharp[i]}#")

    def play(self):
        self._to_major()
        for note in re.findall("[가-힣]\#?\d?", self.song):
            Note().play(note, 500)


if __name__ == '__main__':
    song = """
    레시시도1시라솔미레솔파솔라
    레시시도1시라솔미파솔라시솔
    솔파미미미솔도1미1레1도1미미파솔라
    레레1시라시도1시라솔미레파라솔
    시도1레1시도1레1솔라레도1시라시레1
    시시시미1레1도1시라레라시솔
    """

    Player().add_song(song).set_sharp(1).play()
