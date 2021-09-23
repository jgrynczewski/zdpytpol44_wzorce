from video_file import VideoFile
from audio_mixer import AudioMixer

# Fasada
class VideoConverter:
    def __init__(self):
        self._video_file = VideoFile()
        self._audio_mixer = AudioMixer()

    def convert_video(self):
        result = []

        result.append(self._video_file.get_file())
        result.append(self._audio_mixer.remove_noise())
        result.append(self._audio_mixer.render_sound())

        return "\n".join(result)