import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()


# alexaVoices = engine.getProperty('voices')
# engine.setProperty('voice', alexaVoices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening to you, boss...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '')
                # print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    # print(command)
    if 'play' in command:
        song_request = command.replace('play', '')
        talk('playing' + song_request)
        print(song_request)
        pywhatkit.playonyt(song_request)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('The time right now is ' + time)

    elif 'who is' in command:
        wiki_person = command.replace('who is', '')
        request1 = wikipedia.summary(wiki_person, 1)  # 1 is for one line from wikipedia
        print(request1)
        talk(request1)

    elif 'what is' in command:
        wiki_object = command.replace('what is', '')
        request2 = wikipedia.summary(wiki_object, 1)  # 1 is for one line from wikipedia
        print(request2)
        talk(request2)

    elif 'do you have a boyfriend' in command:
        print('Sorry, i am lesbian')
        talk('Sorry, i am lesbian')

    elif 'joke' in command:
        random_joke = pyjokes.get_joke()
        print(random_joke)
        talk(random_joke)

    elif 'stop' in command:
        raise SystemExit  # end the script

    else:
        talk('Please repeat')


while True:
    run_alexa()
