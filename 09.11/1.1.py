from copy import deepcopy

from constants import *


class Note:
    """Музыкальная нота с возможностью копирования."""

    def __init__(self,
                 *,
                 pitch: Pitch,
                 octave: Octave,
                 accidental: Accidental = None,
                 duration: Duration = Duration.QUARTER):
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental
        self.duration = duration

    def __str__(self):
        if self.accidental is not None:
            return f"Высота: {self.pitch}\n" \
                    f"Октава: {self.octave}\n" \
                    f"Изменение тона: {self.accidental}\n" \
                    f"Продолжительность: {self.duration}\n"
        else:
            return f"Высота: {self.pitch}\n"\
                    f"Октава: {self.octave}\n" \
                    f"Продолжительность: {self.duration}\n"


    def clone(self, **params):
        """Создаёт новый экземпляр ноты с теми же параметрами."""
        copy_object = deepcopy(self)
        # ОТВЕТИТЬ: вам понятно, что именно происходит в этой строке?
        copy_object.__dict__.update(params)
        return copy_object


class ScoreNote(Note):
    """Изображение музыкальной ноты в партитуре."""
    def __init__(self,
                 *,
                 pitch: Pitch,
                 octave: Octave,
                 stem_up: bool,
                 beam: bool = False,
                 accidental: Accidental = None,
                 duration: Duration = Duration.QUARTER):
        super().__init__(pitch=pitch, octave=octave, accidental=accidental, duration=duration)
        self.stem_up = stem_up
        self.beam = beam

    def __str__(self):
        par_str = super().__str__()
        return f"{par_str}" \
               f"Штиль: {self.stem_up}\n" \
               f"Ребро: {self.beam}"


class MIDINote(Note):
    """Кодирование музыкальной ноты в MIDI протоколе."""
    def __init__(self,
                 *,
                 pitch: Pitch,
                 octave: Octave,
                 velocity: int,
                 accidental: Accidental = None,
                 duration: Duration = Duration.QUARTER):
        super().__init__(pitch=pitch, octave=octave, accidental=accidental, duration=duration)
        self.velocity = velocity

    def __str__(self):
        par_str = super().__str__()
        return f"{par_str}" \
               f"Атака звука: {self.velocity}"


score_note_d = ScoreNote(
    pitch=Pitch.D,
    octave=Octave.LINE_2,
    accidental=Accidental.D_FLAT,
    duration=Duration.EIGHTH,
    stem_up=True
)

midi_note_e = MIDINote(
    pitch=Pitch.E,
    octave=Octave.LINE_4,
    velocity=65,
    duration=Duration.EIGHTH,
    accidental=Accidental.SHARP
)

score_note_f = score_note_d.clone(pitch=Pitch.G, octave=Octave.LINE_1)
midi_note_d = midi_note_e.clone(pitch=Pitch.D,  accidental=Accidental.D_FLAT, octave=Octave.LINE_5, velocity=110)


print('Нота в партитуре:')
print(score_note_d, '\n')
print('Клонированная нота в партитуре с изменениями:')
print(score_note_f, '\n')
print('Нота в MIDI протоколе:')
print(midi_note_e, '\n')
print('Клонированная нота в MIDI протоколе с изменениями:')
print(midi_note_d)


# stdout:
"""
Нота в партитуре:
Высота: 2
Октава: 4
Изменение тона: double flat
Продолжительность: 8
Штиль: True
Ребро: False 

Клонированная нота в партитуре с изменениями:
Высота: 5
Октава: 3
Изменение тона: double flat
Продолжительность: 8
Штиль: True
Ребро: False 

Нота в MIDI протоколе:
Высота: 3
Октава: 6
Изменение тона: sharp
Продолжительность: 8
Атака звука: 65 

Клонированная нота в MIDI протоколе с изменениями:
Высота: 2
Октава: 7
Изменение тона: double flat
Продолжительность: 8
Атака звука: 110
"""


# ИТОГ: очень хорошо — 12/12
