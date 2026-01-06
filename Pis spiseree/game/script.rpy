# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("[player_name]")
define n = Character(" ")
define g1 = Character("???")
define g = Character("Grandma")

# Transform er størrelsen på de forskellige sprites

transform wolfleftsexyplace: 
    zoom 0.55 #adjust as required
    xalign 0
    yalign 1.0

 
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


    "I've been thinking about changing my name"

    $ player_name = renpy.input("What is your name, Magical Boy?")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Josh"


    # Viser baggrunden og spiller "rain.ogg" så venter et halvt sekundt

    scene bg forest 
    with Dissolve(1)
    play music "rain.mp3" fadeout 0.2
    pause .5


    # Viser josh med størrelsen af halfsize 

    show wolf placeholder at wolfleftsexyplace
    with Dissolve(.1)

    # These display lines of dialogue.

    j "I hate the rain, gosh it always hits at the worst time."

    j "I need to find cover until the storm passes."
    hide wolf placeholder
    n "You quickly run towards the centre of the forest,"
    scene cabin bg
    n "in the horizon you see a small but comfortable house"
    show wolf placeholder at wolfleftsexyplace
    j "I’ve never seen a house out here before.. Better check it out"
    hide wolf placeholder
    n "..."
    show wolf placeholder at wolfleftsexyplace
    j "Anybody in there? It’s cold as hell out here"
    show grandma placeholder at scarygrandmaright
    g1 "Who are you? Why are you out at this time?"
    hide grandma placeholder
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
    play music "sadmusic.mp3" fadeout 1
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
        "Coffee":
            j "Could I get some coffee?"
            g "Coffee?"
            g "At this hour?"
            j "I just like the taste."
            g "You'd better, i don't want you staying up all night."
            j "I won't, i promise"
            $affection -= 5

        "Tea":
            j "Could I get some tea?"
            g "Good choice!"
            $affection += 10

        "Actually nevermind...":
            j "Actually, nevermind, I don’t think you have anything I like."
            g "???"
            jump choice



return

label house:
    j "go"
return

label bathroom:
    j "toilet attack"
return