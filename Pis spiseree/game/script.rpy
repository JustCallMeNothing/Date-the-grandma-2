# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gui.dialogue_text_outlines = [ (3, "#000005", 0, 0) ]
define gui.dialogue_outline_scaling = "linear"
define gui.charaters_text_outlines = [ (3, "#000005", 0, 0) ]
define gui.characters_outline_scaling = "linear"
style say_label:
    outlines [ ( 3, "#000005", 0, 0) ]
    outline_scaling "linear"




define j = Character("[player_name]")
define n = Character(" ")
define g1 = Character("???")
define g = Character("Grandma")

# Transform er størrelsen på de forskellige sprites

transform wolfleftsexyplace: 
    zoom 0.55 #adjust as required
    xalign 0
    yalign 1.0

define longer_easein = MoveTransition(0.5, enter=offscreenright, enter_time_warp=_warper.easein)




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
            g "You know i can go on and on and on and on and on and on about this child for hours without end, btw im writing this in the middle of class, yknow you prolly arent gonna read this which is so fair"
            g "shes sooooo cute i cant get enough of her eyes, face cheecks yknow all of it makes my day i cant wait until i meet her again, its gonna be so much fun oh wont you join us please"
            j "Mhm"
            jump endofday1
        "Basement":
            j "I'll look around downstairs"
            g "Okay, Just dont get lost! d:"
            scene bg basement:
                zoom 3
            show wolf placeholder at wolfleftsexyplace
            "You slowly make your way down into the basement."
            j "Jeez"
            j "It's so dark in here"
            "You notice a small drawer sitting in the corner of the room"
            menu:
                "Should i open it?"

                "Yes":
                    "The drawer creeks open and you see a old retro-style photo"
                    j "Woah..."
                    g "What was that dragging sound!?"
                    "You quickly pocket the photo"
                    j "Nothing!"
                    jump endofday1
                "No":
                    "You decide not to look"
                    jump endofday1
        "Grandma's room'":
            j "I'm just gonna..."
            j "Look around."
            scene bg grandmaroom
            show wolf placeholder at wolfleftsexyplace
            play music "Tensesadness.mp3" fadeout 1
            "The eerieness of the room, and the feeling that if grandma found out you were up here, colminates into a sense of terror."
            j "God i really hope she doesn't hear me up here"
            hide wolf placeholder
            "You look around Grandma’s room, you see a drawer and a cabinet. "
            show wolf placeholder at wolfleftsexyplace
            menu:
                "Check the drawer":
                    "You open the drawer and see grandma's diapers"
                    "You hastily close drawer"
                    jump endofday1
                "Check the cabinet":
                    "You open the cabinet and see a little ornate box with a picture inside."

                    j "Who is this guy...?"
                    jump endofday1
                "Go back before grandma finds out!":
                    jump endofday1
            $affection -= 5
        "Attic":
            j "Maybe i should check out the attic"
            "You head up the stairs and open the door to the attic."
            scene bg attic
            show wolf placeholder at wolfleftsexyplace
            "Immidietly you are overwhelmed by books"
            menu:
                "Pick up one of the books":
                    "You pick up one of the cutesy looking books and open it"
                    "Even though you can’t read, you see pictures of small crochet animals."
                    j "I didn't know she liked crochet"
                    j "Maybe i should head back"
                "Make a mess":
                    j "Who am i kidding, I can't even read!"
                    "You make a mess of the place"

return

label bathroom:
    g "Oh sure, its just over there"
    j "Thanks, i really have to take a dump"
    hide wolf placeholder
    "You hurredly run towards the bathroom"
    "*Plopping and explosion sounds*"
    g "oh."
    jump endofday1  
return


# ----------------------------------------------------------------------------END OF DAY 1---------------------------------------------------------------------------------------------

label endofday1:
    scene bg livingroomnight
    hide wolf placeholder
    hide grandma placeholder
    "You make your way back to the livingroom couch"
    
    show grandma placeholder at scarygrandmaright
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
return
