# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define config.play_channel = "audio"

# Declare the video here: A


define gui.dialogue_text_outlines = [ (3, "#000005", 0, 0) ]
define gui.dialogue_outline_scaling = "linear"
define gui.charaters_text_outlines = [ (3, "#000005", 0, 0) ]
define gui.characters_outline_scaling = "linear"
style say_label:
    outlines [ ( 3, "#000005", 0, 0) ]
    outline_scaling "linear"


init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

#



init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)


define j = Character("[player_name]")
define n = Character(" ")
define g1 = Character("???")
define g = Character("Grandma")
define h = Character("Hunter")

# Transform er størrelsen på de forskellige sprites

transform wolfleftsexyplace: 
    zoom 0.55 #adjust as required
    xalign 0
    yalign 1.0

transform hunterscarysex: 
    zoom 0.95 #adjust as required
    xalign 0.05
    yalign 1.0

transform hunterscarysex2: 
    zoom 0.95 #adjust as required
    xalign 0.5
    yalign 1.0

define longer_easein = MoveTransition(0.5, enter=offscreenright, enter_time_warp=_warper.easein)

image example = Movie(play="ednding.webm", size=(1920,1080), loop=False, xalign=0.10, yalign=0.10)


transform rødhætteplace:
    zoom 0.5
    xalign 0.5
    yalign 0.5

transform rødhætteplacewall:
    zoom 0.3
    xalign 0.5
    yalign 0.4


 
transform scarygrandmaright: 
    zoom 0.55 #adjust as required
    xalign 0.99
    yalign 1.0
    alpha 0.5
    matrixcolor TintMatrix("#080808") * SaturationMatrix(1.0)

transform grandmaright: 
    zoom 0.55 #adjust as required
    xalign 0.99
    yalign 1.0

    


label start:



    $affection = 0




    # Viser baggrunden og spiller "rain.ogg" så venter et halvt sekundt

    scene bg forest 
    with Dissolve(1)
    play music "rain.mp3" fadeout 0.2
    pause .5


    # Viser josh med størrelsen af halfsize 

    show wolf placeholder at wolfleftsexyplace
    with Dissolve(.1)

    # These display lines of dialogue.

    n "I hate the rain, gosh it always hits at the worst time."

    n "I need to find cover until the storm passes."
    hide wolf placeholder
    n "You quickly run towards the centre of the forest,"
    scene cabin bg
    n "in the horizon you see a small but comfortable house"
    show wolf placeholder at wolfleftsexyplace
    n "I’ve never seen a house out here before.. Better check it out"
    hide wolf placeholder
    n "..."
    show wolf placeholder at wolfleftsexyplace
    n "Anybody in there? It’s cold as hell out here"
    show grandma placeholder at scarygrandmaright
    g1 "Who are you? Why are you out at this time?"
    hide grandma placeholder

    $ player_name = renpy.input("My name is...")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Josh"
    j "I’m just a poor bypasser who got lost in the forest,"
    j "Care to let me in for the night?"
    show grandma placeholder at scarygrandmaright
    g1 "..."
    hide grandma placeholder
    play sound "Door1.mp3"
    n "The door slowly creeks open..."
    show grandma placeholder at grandmaright
    g "You can stay for this night"
    g "But I want you gone by tomorrow morning"
    hide grandma placeholder
    hide wolf placeholder
    n "You enter grandma’s house with caution"
    scene bg livingroomnight
    play music "Livelymusic.mp3" fadeout 1
    n "But as soon as you enter the house you feel a wave of comfortability"
    show grandma placeholder at grandmaright
    show wolf placeholder at wolfleftsexyplace
    j "Nice and comfy hut you have here..."
    g "Thanks, I built it myself with the help of my granddaughter"
    j "It's a bit dark tho.'"
    g "Well i did just get out of bed..."
    g "Could I bid you anything?"
    
    jump choice
    return



label choice:
    menu:
        "What should i do..."

        "Do you have anything to drink?":
            j "Could i get a uhhh..."
            jump drinks
        "Could I take a look around the house?":
            jump house
        "Excuse me, could I use the bathroom?":
            jump bathroom
return


label drinks:
    menu:
        "Choose your drink of choice"

        "Water":
            j "Just some water would be nice."
            jump drinkend
        "Coffee":
            j "Could I get some coffee?"
            g "Coffee?"
            g "At this hour?"
            j "I just like the taste."
            g "You'd better, i don't want you staying up all night."
            j "I won't, i promise"
            $affection -= 5
            jump drinkend

        "Tea":
            j "Could I get some tea?"
            g "Good choice!"
            $affection += 10
            jump drinkend

        "Actually nevermind...":
            j "Actually, nevermind, I don’t think you have anything I like."
            g "???"
            jump choice

return

label drinkend:
    g "Coming right up"
    "She leaves for the kitchen, and you hear the clanging of pots and pans."
    "A second later she comes back with a cup in hand."
    g "Here you go"
    j "Thanks"
    jump endofday1



return

label house:
    j "Could i maybe take a look around the house?"
    g "Oh!"
    g "Sure, just don't go into my room"
    menu:
        "Hell yeah, Where should i go..."

        "Living Room":
            "Maybe i should look around in here"
            hide wolf placeholder
            hide grandma placeholder
            "You walk around the room for a bit, hovering your eyes above anything slightly interesting."
            scene bg wall 
            show redhead at rødhætteplacewall
            with Dissolve(1)
            
            "As your eyes rest on a painting, sitting on the living room wall."
            show wolf placeholder at wolfleftsexyplace
            j "What is this?"
            hide wolf placeholder
            window hide
            show redhead at rødhætteplace with longer_easein
            pause
            window show
            g "Oh my!"
            g "You found a picture of my sweet grandaughter, isn't she cute? She came into my life when i was at the spry age of 84, and she's the most adorable little girl you'll ever meet and i mean it!"
            g "Our first ever road trip was when she was 3 and we went to the beach, but on our way she threw up in the car and we had to get her a napkin, it was hallarious to see her cute face covered in ice cream"
            g "Y'know she was the angel of my life, the absolute peak, i cannot tell you how much i adore this little tiny baby, angel, cakes, poppy, sunrise, creamball, shortcake, pookiebear, cookiemonster"
            g "babycakes, angelchild, son of god, cinnamon bun, lawyer, candybag, popsicle stick, demonchild, car-repairman, diety, redhead, organism, cult activist, teacher, hair strand, beauty"
            g "Huff puff"
            g "You know i can go on and on and on and on and on and on about this child for hours without end, and shes the best in the whole entire universal godversal world, no one is as cute as her my cheesecake uf undying happiness i really do belive everything i've ever done is for this little girls little hearts because she's just the best isn't she oh my goodness look at the time its too late! btw im writing this in the middle of class, yknow you prolly arent gonna read this which is so fair"
            g "shes sooooo cute i cant get enough of her eyes, face cheecks yknow all of it makes my day i cant wait until i meet her again, its gonna be so much fun oh wont you join us please"
            j "Mhm"
            jump endofday1
        "Basement":
            j "I'll look around downstairs"
            g "Okay, Just dont get lost! d:"
            scene bg basement:
                zoom 3
            play sound "Door2.mp3"
            "You slowly make your way down into the basement."
            show wolf placeholder at wolfleftsexyplace
            j "Jeez"
            j "It's so dark in here"
            hide wolf placeholder
            "You notice a small drawer sitting in the corner of the room"
            show wolf placeholder at wolfleftsexyplace
            menu:
                "Should i open it?"

                "Yes":
                    play sound "Door2.mp3"
                    "The drawer creeks open and you see a old retro-style photo"
                    show grandma old at rødhætteplace
                    hide wolf placeholder
                    pause
                    show wolf placeholder at wolfleftsexyplace 
                    j "Woah..."
                    g "What was that dragging sound!?"
                    hide grandma old
                    "You quickly pocket the photo"
                    j "Nothing!"
                    play sound "Door2.mp3"
                    jump endofday1
                "No":
                    "You decide not to look"
                    play sound "Door2.mp3"
                    jump endofday1
        "Grandma's room'":
            j "I'm just gonna..."
            j "Look around."
            scene bg grandmaroom
            show wolf placeholder at wolfleftsexyplace
            play sound "Door2.mp3"
            play music "Tensesadness.mp3" fadeout 1
            "The eerieness of the room, and the feeling that if grandma found out you were up here, colminates into a sense of terror."
            j "God i really hope she doesn't hear me up here"
            hide wolf placeholder
            "You look around Grandma’s room, you see a drawer and a cabinet. "
            show wolf placeholder at wolfleftsexyplace
            menu:
                "Check the drawer":
                    play sound "Door2.mp3"
                    show diapers at rødhætteplace
                    "You open the drawer and see grandma's diapers"
                    pause 0.5
                    hide diapers
                    play sound "Door1.mp3"
                    "You hastily close drawer"
                    play sound "Door2.mp3"
                    jump endofday1
                "Check the cabinet":
                    play sound "Door2.mp3"
                    "You open the cabinet and see a little ornate box with a picture inside."
                    play sound "Paper.mp3"
                    show hunter guy at rødhætteplace
                    j "Who is this guy...?"
                    j "And why does he look so..."
                    j "Familiar?"
                    j "..."
                    hide hunter guy
                    play sound "Paper.mp3"
                    "You put the photo back"
                    play sound "Door2.mp3"
                    jump endofday1
                "Go back before grandma finds out!":
                    jump endofday1
            $affection -= 5
        "Attic":
            j "Maybe i should check out the attic"
            "You head up the stairs and open the door to the attic."
            play sound "Door2.mp3"
            scene bg attic
            show wolf placeholder at wolfleftsexyplace
            "Immidietly you are overwhelmed by books"
            menu:
                "Pick up one of the books":
                    "You pick up one of the cutesy looking books and open it"
                    play sound "Paper.mp3"
                    show page placeholder at rødhætteplace
                    "Even though you can’t read, you see pictures of small crochet animals."
                    j "I didn't know she liked crochet"
                    hide page placeholder
                    play sound "Paper.mp3"
                    j "Maybe i should head back"
                    play sound "Door2.mp3"
                    jump endofday1
                "Make a mess":
                    j "Who am i kidding, I can't even read!"
                    play sound "Paper.mp3"
                    "You make a mess of the place"
                    play sound "Door2.mp3"
                    jump endofday1

return

label bathroom:
    g "Oh sure, its just over there"
    j "Thanks, i really have to take a dump"
    hide wolf placeholder
    play sound "Door2.mp3"
    "You hurredly run towards the bathroom"
    stop music
    play audio "Poop1.mp3"
    play audio "Poop2.mp3"
    play audio "Poop3.mp3"
    play audio "Poop4.mp3"
    play audio "Poop5.mp3"
    play audio "Poop6.mp3"
    "*Plopping and explosion sounds*"
    stop audio
    stop music
    stop sound
    g "oh."
    jump endofday1  
return


# ----------------------------------------------------------------------------END OF DAY 1---------------------------------------------------------------------------------------------

label endofday1:
    scene bg livingroomnight
    hide wolf placeholder
    stop music
    play music "Breezy.mp3"
    hide grandma placeholder
    "You make your way back to the livingroom couch"
    
    show grandma placeholder at grandmaright
    g "*Yawn*"
    show wolf placeholder at wolfleftsexyplace
    j "Getting tired?"
    g "Yes, we should get some sleep, the storm settles in a few days"
    g "so for now you can just sleep on the couch"
    g "I'll get you a blanket"
    j "Thanks..."
    hide grandma placeholder
    n "Jeez everything is happening so fast"
    n "..."
    n "Grandma's kinda cute"
    show grandma placeholder at grandmaright
    g "Here, you can sleep on the couch for tonight."
    stop music
    jump duringnight
return


label endofday1affection:
    g "*Yawn*"
    j "Getting tired?"
    g "Yes, we should get some sleep, the storm settles in a few days"
    g "so for now..."
    g "If you want you could sleep in my room..."

    g "I'll get you a blankët"
    j "Thanks..."
    hide grandma placeholder
    n "Jeez everything is happening so fast"
    n "..."
    n "Grandma's kinda cute"
    stop music
    jump duringnight
return




label duringnight:
    scene bg basement:
                zoom 50
    play music "Heartbeat.mp3"
    pause
    j "Huiff puff"
    "You feel a strange sensation during your slumber "
    j "Must... hhmn"
    j "Eat..."
    "Your stomach growls in anticipation"
    j "ah, eat... eat... cannot.. Ngh"
    j "Food. Where is food..."
    j "..."
    j "Old lady..."
    "At the thought of the sweet old grandma, your chest burst into a sudden pain."
    "But you managed to keep yourself calm during the night. "
    stop music
    jump morningtime

return


label morningtime:
    pause
    "Your eyes slowly creep open"
    scene bg livingroom
    play music "Breezy.mp3"
    "*You hear Grandma out in the kitchen*"
    show wolf placeholder at wolfleftsexyplace
    j "Jeez, my eyes are so heavy"
    j "Grandma was a lifesaver. If it weren't for her generosity i would have damn near frozen to death."
    hide wolf placeholder
    "exhausted you crawl out of bed to greet grandma in the morning"
    show grandma placeholder at grandmaright
    g "Sleep well?"
    show wolf placeholder at wolfleftsexyplace

    menu:
        "How did i sleep..."


        "Pillow was not too comfortable but it was alright nonetheless":
            g "I’m sorry, it was all i had ill make sure to make guest visits more comfortable in the future, but nobody visits me other than my sweet granddaughter"
            jump continuation1

        "The couch sucked; couldn’t you have gotten me a mattress?":
            g "You could have slept out in the rain if it was so bad!"
            jump continuation1

        "I did! How about you?":
            g "That’s splendid. I slept well myself darling"
            jump continuation1
return

label continuation1:
    g "Well, a new day is upon us, when do you plan on heading out?"
    g "you can stay till lunch if you’d like, i prepared some extra yesterday, i hope you like eggs as i put a lot of them in the sandwiches, from my granddaughter's chicken coop too! I think their quite deli- "
    stop music
    hide wolf placeholder
    hide grandma placeholder
    play audio "HunterDoor.mp3"
    scene bg door:
        zoom 1.7, xalign 0.5, yalign 0.5
    pause
    play music "Tense.mp3"
    show wolf placeholder at wolfleftsexyplace
    j "Who is that??!"
    show grandma placeholder at grandmaright
    g "Oh gosh, i didn’t expect a visit from him today, quickly hide!!"

    menu:
        "Shit! Should i listen?"

        "Hide":
            hide wolf placeholder
            "You follow grandma’s advice and quickly climb underneath the staircase"
            show hunter at hunterscarysex
            play sound "Door1.mp3"
            h "I’m home sweetie did ya make breakfast yet."
            g "Oh yes... I prepared some apple pie just upstairs.."
            g "How did your morning hunt go?"
            h "It went how it usually does, funny thing-"
            
            
            play audio "Burp.mp3"
            h "*Burp*" with sshake
            h "We almost caught ya a lope of werewolf meat yesterday, but he trailed off before we could get a good angle."
            g "Why were you hunting him, I've heard werewolves are quite nice. "
            h "It’s a werewolf, how are they nice, they eat us?!"
            show hunter at hunterscarysex2
            hide grandma placeholder
            "The hunter frustrated with the conversation, moves up the staircase towards the delicious apple pie. "

            menu:
                "I gotta do something fast!"

                "Run away":
                    jump runaway
                "Ambush":
                    jump ambushh


        "Confront":
            "hi"

        "Devour":
            "hello"

    $ renpy.movie_cutscene("ednding.webm")
    n "The end"


return


# --------------------------------------------------------------------------------ENDINGS-----------------------------------------------------------------------------------------------

#                     RUN AWAY
label runaway:
stop music
hide hunter
hide grandma placeholder
scene bg basement:
                zoom 50
play audio "Door1.mp3"
play audio "Running.mp3"
"You take this chance to escape, leaving everything behind. Deep into the forest, you lie down from exhaustion. "
play audio "Runaway.mp3"
$ renpy.movie_cutscene("runending.webm")
stop audio
return

#                     AMBUSH

label ambushh:
show wolf placeholder at wolfleftsexyplace
"You lunge towards the hunter swiping your claws at him."
play audio "Hit1.mp3"
menu:
    "He groans in pain, its clear he will bleed out like this. "
    with sshake
    "Excecute":
        j "No one disturbs the peace in this house. Grandma deserves better you brute"
        play audio "Hit1.mp3"
        pause 0.5
        hide hunter
        play audio "Death.mp3"
        stop music
        "You mercilessly swipe your claws one more time, and the massive hunter falls flat over." with sshake
        show grandma placeholder at grandmaright
        g "..."
        play music "Tensesadness.mp3"
        j "im so sorry grandma i-"
        j "i didnt want it to end this way."
        g "its fine... it was self defense, had you not hidden he wouldn’t have hesitated either, im just happy its over."
        j "ehm.."
        j "would you mind if i stay for a bit longer?"
        g "Not at all. Your company is the best ive had in years"

    "Spare":
        j "Look! i jus-"
        stop music
        play audio "Shotgun.mp3"
        pause(1)
        hide wolf placeholder
        play audio "Death.mp3"
        "The hunter with no time to spare fires his shotgun into you, tossing you across the room killing you on the spot" with sshake
        $ renpy.movie_cutscene("ednding.webm")
        

    "Run away":
        jump runaway


return