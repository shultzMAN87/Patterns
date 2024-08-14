class DVDPlayer:
    def on(self):
        print("DVD-плеер включён.")

    def play(self, movie: str):
        print(f"Воспроизведение фильма: {movie}")

    def off(self):
        print("DVD-плеер выключён.")


class SurroundSoundSystem:
    def on(self):
        print("Система объемного звучания включена.")

    def set_volume(self, level: int):
        print(f"Громкость установлена на уровень {level}")

    def off(self):
        print("Система объемного звучания выключена.")


class HomeTheaterFacade:
    def __init__(self, dvd: DVDPlayer, sound_system: SurroundSoundSystem):
        self._dvd = dvd
        self._sound_system = sound_system

    def watch_movie(self, movie: str):
        print("Подготовка к просмотру фильма...")
        self._dvd.on()
        self._sound_system.on()
        self._sound_system.set_volume(5)
        self._dvd.play(movie)

    def end_movie(self):
        print("Завершение просмотра фильма...")
        self._dvd.off()
        self._sound_system.off()

# Пример использования
if __name__ == "__main__":
    # Создание объектов подсистемы
    dvd = DVDPlayer()
    sound_system = SurroundSoundSystem()

    # Создание фасада
    home_theater = HomeTheaterFacade(dvd, sound_system)

    # Управление системой через фасад
    home_theater.watch_movie("Inception")
    print("\n--- Фильм завершен ---\n")
    home_theater.end_movie()