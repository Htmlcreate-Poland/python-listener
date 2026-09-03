import sys
import speech_recognition as sr

def loguj_mowe_w_cmd():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("=== Uruchomiono logowanie mowy do CMD ===")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Gotowe! Zacznij mówić. (Ctrl+C przerywa)\n")

        while True:
            try:
                print("[Słucham...]", end="", flush=True)
                audio_data = recognizer.listen(source, timeout=None, phrase_time_limit=None)
                
                print("\r[Przetwarzam...]", end="", flush=True)
                tekst = recognizer.recognize_google(audio_data, language="pl-PL")
                
                print(f"\r> {tekst}")
                
            except sr.UnknownValueError:
                print("\r", end="", flush=True)
            except sr.RequestError as e:
                print(f"\n[Błąd]: {e}")
            except KeyboardInterrupt:
                print("\n\n=== Zakończono logowanie ===")
                sys.exit(0)

if __name__ == "__main__":
    loguj_mowe_w_cmd()
