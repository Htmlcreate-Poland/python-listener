import speech_recognition as sr


def text_to_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("czekaj......")
    
        recognizer.adjust_for_ambient_noise(source, duration=1)
    
        print("mów teraz")
    
        audio_data = recognizer.listen(source)
    
        print("rozpoznawanie mowy!  ")
    
        try:
            tekst = recognizer.recognize_google(audio_data, language="pl-PL")
        
            print(f"Rozpoznany tekst: {tekst}")
        
            return tekst
    
        except sr.UnknownValueError:
                print("Google Speech Recognition nie zrozumiał dźwięku (brak mowy lub niewyraźnie).")
        except sr.RequestError as e:
            print(f"Nie można pobrać wyników z serwisu Google; {e}")
        
if __name__ == "__main__":
    text_to_speech()