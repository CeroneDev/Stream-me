#chars
define j = Character("Starboy")
define v = Character("XxP3arl")
define c = Character("MsDestiny")
define m = Character("Dynapaw")

label start:
    #black fade to mc's room
    scene bg black
    with Pause(0.5)
    scene bg mc
    with Dissolve(1)
    play music "audio/bgmusic.mp3"
    #internal monologing starts here (this is the most final version i could find on the server (i did some editing))
    "It's been three days since you got layed off from your awful office job. These couple days have been a wreck, sure, but it's also been ever so relieving."
    "The freedom that comes with uncertainty washing over you, spending your time watching a group of your favorite streamers:"
    "{b}[j]{/b}, the gruff and cocky ex athlete with a knack for old fighter-type games, and an attitude just as feisty. Piercings covering his face, and tattoos covering his arm and body."
    "{b}[v]{/b}, coder and viewer-dubbed total nerd! She streams weird indie team-based games, and flocks over the intricate programs used to code them. She's meek and flushes at the slightest compliments from her chat."
    "{b}[c]{/b}, heartthrob and beauty queen extraordinaire. A variety streamer with a mega-fanbase and the current number one female streamer!"
    "And lastly; {b}[m]{/b}. The almost off-putting scruffy man. Tall, lean, dark, and handsome. He barely streams, but when he does, he sits down and talks about his awful everyday office job-- a kind of story you've always related to."
    #announcement post
    show intro post
    "Recently, due to an influx of viewers, the group sent out a notice: They needed mods. Out of a job, and without any clear path in life, you applied. That's how you ended up here."
    "In a video chat."
    stop music fadeout 1
    "With your favorite streamers."
    #flashes in the streamers
    scene bg white
    with Pause(0.25)
    scene bg mc

    show j normal:
        xalign 0.05
    with Pause(0.5)

    show v normal:
        xalign 0.35
    with Pause(0.5)

    show c normal:
        xalign 0.65
    with Pause(0.5)

    show m normal:
        xalign 0.95
    with Pause(0.5)
    
    scene bg logo
    with Pause(1)
    
    scene bg nextscene
    "next dialogue goes here"

    #end of game is over here
    return