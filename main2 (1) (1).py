import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
from pydub import AudioSegment 
from pydub.playback import play


genai.configure(api_key="AIzaSyDy59cCQyu38wVj55e92kafXawRA_ZoAbM")


r = sr.Recognizer()
engine = pyttsx3.init()


rate = engine.getProperty('rate')
engine.setProperty('rate', int(rate * 0.7))


model = genai.GenerativeModel("gemini-1.5-flash")

initial_prompt = """
I am giving you a script. You have to speak the lines of Cheetos. 
You might get some wrong words, so work with an 80% word accuracy.  only say ok with first prompt.
Continuously listen and recognize the line before you and speak your line accordingly YOU ARE SPEAKING THE LINES WITH ONLY A WORD DUMBASS RECOGNISE THE PREVIOUS LINE THAT IS BEFORE THE CHEETOS LINE AND THEN SAY THE CHEETOS LINE ACCORDINGLY.
 
**Script:**
 
Narrator: Uh, can I just ask What exactly is this place Looks like a vacay stay for ghosts if you what i mean 
Trainer : What is this place Its a place I manage, for all those ghosts out there lurking in the shadows. Hiding from the persecution of humankind. A place for them and their families to come to and be themselves. Where a scream echoes louder than your alarm on winter morning  a screaming sound made by someone backstage, narrator chuckles  A void of torches, pitchforks, angry mobs. A place of peace, relaxation, and tranquility.
Narrator: Cool, so like i said its like a hotel for ghosts OHH THIS IS GONNA BE FUN 
Trainer : irritated Yes, exactly. A hotel for ghosts, way to sum it up.
 
BOSS - WHAT FOOD ARE YOU SERVING
 
NARRATOR - WOAH WOAH hey man, im just the narrator and im not getting paid enough to deal with you.The trainer is behind you
 
BOSS - Oh sorry my bad
 
BOSS -  WHAT FOOD ARE YOU SERVING IS THIS WHY I HAVE HIRED YOU YOU ARE THE MANAGER OF THE HOTEL AND YOU CANT MANAGE TO SERVE ME A SINGLE DISH WITHOUT YOUR 1000 TANTRUMS AND EXCUSES
 
TRAINER - I am sorry boss, please do forgive me. This is just a small mistake. It will never happen again.
 
BOSS - SHUT UP AND GET LOST
 
NARRATOR - I think someone needs a Snickers...or a vacation, maybe a nap, poor childs cranky. Too bad this boss is the one who owns the most "relaxing" place in town—a haunted hotel Stay tuned, folks. This train of chaos has only just left the station.
 
BOSS - IM NOT A CHILD
 
NARRATOR - YEA YOU ARE
 
SCENE 2
 
LEO - OH COME ON GUYS, STOP BEING SCAREDY CATS I AM TIRED OF YOUR GIRLY DRAMA NOW LETS GO
 
MIA - Oh please Look whos talking, the one who cries after seeing PEPPA PIG losing her favourite toy. Do I need to call you a wahmbulance WAH WAH
 
Leo - RUDEEcries
 
ANNE - Guys please stop fighting. Wait a minute did PEPPA lose her toy
 
LEO - YES Wait, is that a snake rustling in the leaves ACCIDENTLY DROPS HIS PEPPA PIG TOY
 
ANNE - WHAT
 
MIA - Oh, relax, its just a—wait...is that...a cheetah
 
CHEETOS- HELLO EVERYONE Dont be scared of me And Leo to make you happy, Peppa finds back her stuff toy.
 
LEO - really
 
Trainer- Hello Everyone Welcome to this exotic hotel. Im the manager here. Ahhhh I see youve met my pet CHEETOS. You left your toy in the lobby cheetos. POINTS TO HIS STARFISH TOY
 
MIA- Dont wanna be rude but, this is anything but exotic. 
 
ANNE TUGS HER SIGNALLING HER TO SHUT UP. THEY MAKE THEIR WAY TO THE
INSIDE OF THE HOTEL WHILE THE TRAINER NARRATES THE STORY OF THE HOTEL.
 
Trainer - What brings you to this horrendous - I mean marvellous property.
 
LEO - Well we wanted to check out this uhhhh unique property
Trainer- Well the doors are open, come on in, would you like bloody mary
 
ANNE - B-B-B-BLOODY MARY
 
Trainer- We give it to all guests upon their arrival.
 
ANNE - WHAT  Are we checking in a hotel or joining a vampire club
 
MIA - He is talking about the drink Anne. Come on
 
Trainer - You know, you lack humour and its not the only thing you lack points to her dress
 
Anne - HEY COME ON MAN,, NOT COOL
 
NARRATOR: Its official—Anne might need just a hot cocoa and a blanket instead of the drink. For the chaos t~hat lies ahead, she might need something stronger 
 
Trainer - Why do you guys look so scared 
 
LEO- Well we have heard some rumours —-
 
Trainers- Oh those are just stories nosy teenagers like you have created. Its not as if ALL of them are true.EVIL SMIRK
 
LEO - whispers to the others This guy is definitely giving me some shady vibes. 
 
LEO - Whats our room number
 
Trainer - Your room number is 13. 
 
ANNE - Room 13 Really Thats a little spooky, isnt it
 
Servant- Oh, dont be superstitious. Its just a number. Besides, ghosts dont check into hotels. they just float in, scare the guests, and skip out on the bill Bunch of freeloaders scoffs
 
MIA - Can you just lead us to our room This bag is killing me. It is heavier than Leos appetite so you can imagine and I really dont understand why Leo needs so many stuffed animals to sleep. 
 
ANNE - Speaking of animals, wheres that lil cheetah 
 
Trainer - WHAT DO YOU MEAN CHEETOS,                                                                                                                                               
 
MIA - Myths, what myths 
 
NARRATOR- They make their way inside, the heavy doors groaning shut behind them as the trainer begins to weave the hotels eerie tale.
 
Trainer - Oh its a long long long story, but for our special guest, lets put it in a song. 
PICKS UP GUITAR AND STARTS PLAYING A TUNE OF VAMPIRE
 
SERVANT: 
An old man came here for a thrill, 
 
But suddenly died without writing a will.
 
The story here becomes a little blur
 
The old mans ghost makes spooky things occur. 
 
Mia –  I dont believe that you are telling the truth. Also that was the most terrible song Ive ever heard in my 13 years of existence. 
 
Leo – And as for the rumours, well see for ourselves whether they are true or not
 
Trainer – All right then, the servant will lead you all to your room. But dont say I didnt warn you 
 
Leo - Uhh, I am a bit hungry, can we first proceed to the restaurant
Anne - Leo, you just ate around 10 family packs of chips and drank 5 litres of cola, you are again hungry Oh God Is your stomach a black hole that swallows everything
 
Leo - Ok yeah, but you forgot those 5 burgers, and no need to be so rude  cries . Can we please go, with his hand on his stomach
 
LEO AND ANNE AGREE AND ALL THREE HEAD DOWNSTAIRS FOR DINNER, SUDDENLY THEY NOTICE CHEETOS STUFF TOY LYING ON THE GROUND TORN INTO PIECES. THEY FOLLOW ITS TRAIL WHICH LEADS THEM BACK TO A BASEMENT 
 
Narrator - If youve ever wondered where bad decisions are born,scoff sound it usually starts with a creepy trail and an even more creepy basement with bone piles and dim lighting. Onto our brave trio, they are walking headfirst into trouble.
 
THEY ENTER THE ROOM TO FIND CHEETOS IN A PILE OF BONES.
 
Leo - Pls dont tell me these belong to the people Cheetos has eaten. STARTS CRYING. HEARING THIS THE TRAINER AND SERVANT COME. 
 
Trainer - OMG You shouldnt have come here. 
 
Anne - See, I knew I was right. IN. YOUR. FACE. MIA, wait, I was right.
 
Mia - Dont tell me this place is actually haunted, also, not a really good time to rub it in. 
 
Leo - crying loudly. 
 
Mia - By the way do you know why cemeteries have gates
 
Leo - because people are dying to get in
 
Mia - wow, leo you are becoming smarter.
 
Leo - really, thanks, but cries
 
Trainer - Stop it you little annoying insects. Now you three will stay here forever locked in this basement for eternity. 
 
Mia  - Now since youve challenged me, I will expose you, even if it is the last thing I do before ‘the ghost catches me. 
 
Leo - ITS OVER. WERE ALL GONNA DIE IN THE BASEMENT WITH STUFFED ANIMALS. I DONT WANT TO SHARE MY COFFIN WITH A GHOST
 
Anne - Leo is right. 
 
"""
 
def get_user_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech Service; {e}")
        return ""

def get_gemini_response(message):
    full_prompt = f"{initial_prompt}\n\n{message}"
    response = model.generate_content(full_prompt)
    return response.text

def speak_response(response):
    engine.say(response)
    engine.runAndWait()

def play_bruh_sound():
    try:
        sound = AudioSegment.from_mp3("FUCKYOU.mp3")  
        play(sound)
    except Exception as e:
        print(f"Error playing audio file: {e}")

if __name__ == "__main__":
    while True:
        user_input = get_user_input()
        if not user_input:
            continue

        if "bruh" in user_input.lower():
            play_bruh_sound()

        gemini_response = get_gemini_response(user_input)
        speak_response(gemini_response) 