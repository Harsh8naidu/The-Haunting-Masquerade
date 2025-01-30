# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Intro")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg main with dissolve:
        size (1920, 1080)

    # These display lines of dialogue.

    e "In the small, secluded town of Ravenbrook, Halloween was more than just a holiday; it was a tradition deeply rooted in the town's eerie history."

    scene bg manor with dissolve:
        size (1920, 1080)

    e "Every year, as the full moon cast its silver glow upon the town, an extravagant masquerade ball was held at the mysterious Ravenwood Manor, an ancient mansion that sat atop a hill overlooking the town."


    e "Legend had it that the manor was haunted, but the allure of the masquerade was too powerful to resist."

    scene bg chapter_1 with dissolve:
        size (1920, 1080)

    define x = Character("")

    x ""

    scene bg evelyn_intro with dissolve:
        size (1920, 1080)

    define evelyn = Character("Evelyn")

    show evelyn_img at center:
        size (360, 800)

    x "Evelyn is an ordinary young woman living in the quiet town of Ravenbrook. She's always had a curious nature, eager to explore the mysteries that the world holds."

    x "Currently, she's pursuing her passion for art at the local college, where she spends her days sketching and painting scenes inspired by the town's serene landscapes."

    x "But there's one thing that sets Evelyn apart from the rest: her deep anticipation for Halloween. Every year, she eagerly awaits the arrival of this spooky holiday."

    x "It's not just about the costumes, candies, or the playful scares; for Evelyn, Halloween represents the allure of the unknown, the chance to uncover secrets hidden in the shadows."

    x "Little does she know that this Halloween will bring more mystery and adventure than she ever imagined."

    # Transition to college scene
    scene bg classroom with dissolve:
        size (1920, 1080)

    # Scene transition to college
    show evelyn_img at center:
        size (360, 800)

    x "One sunny afternoon, after her college classes were over,"

    x "Evelyn decided to relax in the campus courtyard."

    
    scene bg college with dissolve:
        size (1920, 1080)

    # Dialogue with Amelia's introduction
    define amelia = Character("Amelia")

    show amelia_img at right:
        size (500, 800)
        xpos 1800

    show evelyn_img at left:
        size (360, 800)
        xpos 100

    amelia "Hey, Evelyn!"

    x "Amelia, her best friend, waved energetically as she approached."
    x "The two friends were happy to see each other, ready for their usual chat."

    # Friendly chat between Evelyn and Amelia
    amelia "How's art class going, Evelyn?"
    evelyn "It's been great, Amelia! I've been working on a new painting,"
    evelyn "and I can't wait to show it to you."
    amelia "I can't wait to see it! By the way, have you heard about the Ravenwood Manor ball?"

    # Amelia invites Evelyn to the ball
    evelyn "The Ravenwood Manor ball? Tell me more!"
    amelia "It's this amazing masquerade ball that happens every Halloween night."
    amelia "I got an invitation, and I thought it would be so much fun to go together."
    evelyn "Sounds intriguing! I've always been curious about the manor."
    evelyn "Count me in, Amelia! Let's make it a memorable Halloween."

    # Narrative about the invitation and costume selection
    x "The invitation was signed by Sir Lucius Blackwood,"
    x "the enigmatic host of the event. Curiosity got the better of her,"
    x "and she decided to attend, with her best friend Amelia by her side."

    x "As the night of the masquerade approached,"
    x "Evelyn and Amelia excitedly prepared their costumes."
    
    scene bg ravenwood_hall with dissolve:
        size (1920, 1080)

    show evelyn_ball_img at center:
            size(800, 800)
    
    x "Evelyn chose to dress as a mysterious sorceress,"

    scene bg ravenwood_hall with dissolve:
        size (1920, 1080)

    show amelia_ball_img at center:
            size (600, 700)

    x "while Amelia opted for a classic ghostly bride attire."


    # End of Chapter 1
    x "Little did they know that this Halloween would be unlike any other."
    x "What awaits Evelyn and Amelia in the dark corners of Ravenwood Manor?"

    # Choice to proceed to the next chapter
    menu:
        "Continue to Chapter 2":
            jump chapter_2_start


    # Define Chapter 2 start label
    label chapter_2_start:

        # Show the chapter_2 image with a specified size
        scene bg chapter_2 with dissolve:
            size(1920, 1080)

        # Wait for a click before transitioning to bg manor
        pause

        # Background setup for the masquerade ball
        scene bg manor with dissolve:
            size (1920, 1080)

        # Narrative to set the scene
        x "The night of the masquerade arrived, and the moon hung low in the sky,"
        x "casting an eerie glow over the town of Ravenbrook."

        # Transistion to the ballroom
        scene bg ballroom with dissolve:
            size (1920, 1080)

        x "Guests in elaborate masks and costumes filled the manor's grand ballroom,"
        x "their laughter and chatter echoing through the halls."

        # Evelyn and Amelia blend in with the crowd
        x "Evelyn and Amelia blended in seamlessly with the crowd,"
        x "their masks concealing their identities among the masquerade-goers."


        # Introduction of Gideon
        define gideon = Character("Gideon")

        scene bg gideon_in_ballroom with dissolve:
            size(1920, 1080)

        show gideon_img at left:
            size (450, 800)
            xpos 100

        gideon "Evening, ladies."
        x "Evelyn couldn't help but be captivated by the charm of Gideon,"
        x "a charming and charismatic guest who had just approached."
        x "They struck up a conversation, and it became clear that Gideon had"
        x "a genuine interest in the supernatural and the mysteries of Ravenwood Manor."

        # Conversation between Evelyn and Gideon
        show evelyn_ball_img:
            size (800, 800)
            xpos 1100 ypos 280
        
        gideon "You know, Evelyn, Ravenwood Manor has a long history of secrets."
        evelyn "Secrets? Tell me more."
        gideon "Legend has it that the manor is haunted by restless spirits,"
        gideon "and there are hidden passages that few have explored."
        evelyn "That sounds thrilling! Have you ever encountered anything supernatural here?"
        gideon "Not yet, but I've always been drawn to the mysteries of this place."
        gideon "I believe that there's more to Ravenwood Manor than meets the eye."

        # Evelyn's observation of strange occurrences
        scene bg ravenwood_hall with dissolve:
            size (1920, 1080)

        x "As the evening progressed, Evelyn began to notice strange occurrences."

        show evelyn_ball_img at left:
            size(800, 800)

        x "A flickering candle that wouldn't stay lit, whispers in the shadows,"
        x "and fleeting glimpses of a phantom figure."
        x "Each encounter sent shivers down her spine, but Gideon remained steadfast,"
        x "reassuring her that it was all part of the masquerade's mystique."

        scene bg candles_in_corridor:
            size (1920, 1080)

        show evelyn_ball_img at left:
            size(800, 800)

        evelyn "What was that? A flickering candle... but there's no draft in here."

        scene bg manor_corridor_2:
            size (1920, 1080)

        show evelyn_ball_img at left:
            size(800, 800)

        evelyn "The shadows danced ominously on the walls, and she continued to explore."
        evelyn "Whispers in the shadows... Is someone there?"

        scene bg manor_corridors:
            size (1920, 1080)

        show evelyn_ball_img at left:
            size(800, 800)

        evelyn "The flicker of a candle revealed a fleeting glimpse of a phantom figure."
        evelyn "I must be imagining things. Gideon said it's all part of the masquerade's mystique."

            # Gideon finds Evelyn in the manor
        show gideon_img at right:
            size (450, 800)

        gideon "Evelyn! There you are. You look a bit worried. Is everything alright?"
        x "Evelyn turned to see Gideon, her heart racing from her unsettling encounters."
        evelyn "Gideon, it's just... I've seen some strange things in this manor."
        gideon "Strange things? What have you seen?"

        # Evelyn shares her experiences
        x "Evelyn recounted her encounters: the flickering candles,"
        x "the whispers in the shadows, and the phantom figure."

        # Gideon's response
        gideon "It sounds like you've stumbled upon the manor's mysteries."
        gideon "But fear not, Evelyn. We'll discover the truth behind these strange occurrences together."
        
        x "Evelyn's worries began to ease as she realized she wasn't alone in this adventure."

        # End of Chapter 2
        x "Little did they know that the secrets of Ravenwood Manor would soon reveal themselves,"
        x "unfolding a tale of darkness and enchantment they could never have imagined."

        # Choice to proceed to the next chapter
        menu:
            "Continue to Chapter 3":
                jump chapter_3_start

    # Chapter 3: Unveiling the Secrets

    label chapter_3_start:

        # Background setup for Chapter 3
        scene bg ravenwood_hall with dissolve

        # Evelyn and Gideon continue their exploration
        x "Evelyn and Gideon ventured further into Ravenwood Manor,"
        x "their footsteps echoing in the dimly lit hallways."

        # Dialogue between Evelyn and Gideon
        scene bg manor_corridor_3:
            size (1920, 1080)

        show evelyn_ball_img at left:
            size (800, 800)

        show gideon_img at right:
            size (450, 800)

        evelyn "Gideon, do you think there's any truth to the legends about this place?"
        gideon "Legends often have a kernel of truth, Evelyn."
        gideon "I believe we're on the cusp of discovering something extraordinary."

        x "As they walked, Evelyn noticed a series of intricate paintings on the walls."
        evelyn "These paintings, they seem to tell a story."
        gideon "Yes, each one holds a piece of Ravenwood Manor's history."

        x "Evelyn stopped before a particularly captivating portrait."
        evelyn "Who is this? She seems important."
        gideon "That's Lady Seraphina, a former resident of the manor."
        gideon "Legend has it she had a connection to the supernatural."


        # Evelyn and Gideon explore hidden passages
        x "As they continued their exploration, Evelyn noticed a loose bookshelf."
        evelyn "Gideon, look at this bookshelf. It seems out of place."
        gideon "Let's see if it hides a secret."
        e "Together, they pushed the bookshelf aside, revealing a hidden passage."

        # Dialogue while exploring hidden passages
        evelyn "This is incredible! I've never seen anything like it."
        gideon "It appears Ravenwood Manor has many secrets yet to be uncovered."

        scene bg manor_library:
            size (1920, 1080)

        show evelyn_ball_img at left:
            size (800, 800)

        show gideon_img at right:
            size (450, 800)

        # Deciphering cryptic messages
        e "In one chamber, they discovered a room filled with ancient tomes and scrolls."
        evelyn "These scrolls have cryptic messages. Can you decipher them, Gideon?"
        x "Gideon carefully studied the scrolls and began to decipher their meaning."

        # Dialogue while deciphering
        gideon "It seems these scrolls hold clues to the manor's history."
        evelyn "What do they say?"
        gideon "They speak of a hidden chamber beneath the manor, where great power lies."

        # Uncovering diaries of former residents
        x "In a dusty attic, they stumbled upon a collection of diaries."
        evelyn "These diaries must belong to former residents of Ravenwood Manor."
        gideon "Let's see if they reveal any secrets."

        # Dialogue while reading diaries
        x "Evelyn and Gideon took turns reading the diaries, each one unveiling more mysteries."
        gideon "It seems Lady Seraphina knew more than anyone suspected."
        evelyn "What secrets did she hold?"
        gideon "We're about to find out."

        # Amelia's concern and Evelyn's determination
        scene bg manor_library:
            size (1920, 1080)

        show evelyn_ball_img at left:
            size (800, 800)

        show amelia_ball_img at right:
            size (600, 700)
            xpos 1900

        amelia "Evelyn, this place is giving me the creeps. We should leave."
        x "Amelia grew increasingly concerned about Evelyn's safety."
        evelyn "I appreciate your worry, Amelia, but I can't turn back now."
        evelyn "I need to confront the phantom of Ravenwood."

        # Amelia's plea
        amelia "But what if it's dangerous? What if we get hurt?"
        evelyn "I can't explain it, Amelia, but there's something drawing me deeper."
        evelyn "I need to uncover the truth about this place."

        # End of Chapter 3
        x "Their conversation hung in the air, tension building between worry and determination."
        x "As they ventured further into the heart of the manor, Evelyn couldn't shake the feeling"
        x "that they were on the verge of a revelation—one that would change everything."

        # Choice to proceed to the next chapter
        menu:
            "Continue to Chapter 4":
                jump chapter_4_start

    # Chapter 4: Confronting the Phantom

    label chapter_4_start:
        
        define phantom = Character("Phantom")

        # Background setup for Chapter 4
        scene bg manor_corridor_4 with dissolve:
            size (1920, 1080)

        # Evelyn and Gideon's fateful encounter
        x "One fateful night, Evelyn and Gideon ventured deep into the heart of the manor."
        x "In the shadowy corridors, their footsteps echoed eerily."

        show evelyn_ball_img at left:
            size (800, 800)

        show gideon_img at right:
            size (450, 800)

        # Dialogue between Evelyn and Gideon
        evelyn "Gideon, do you believe we'll find the Phantom of Ravenwood here?"
        gideon "I believe so. The clues have led us to this very spot."

        # Encounter with the Phantom
        scene bg manor_corridor_5:
            size (1920, 1080)

        show evelyn_ball_img at left:
            size (800, 800)

        show gideon_img at right:
            size (450, 800)

        x "Suddenly, there it was—the Phantom of Ravenwood."
        x "A ghostly figure draped in tattered robes, its eyes filled with torment."

        # Dialogue during the encounter
        evelyn "Who are you? What happened to you?"
        phantom "I am the tormented soul of a former resident,"
        phantom "cursed to wander these halls for eternity."

        # Evelyn and Gideon's determination
        evelyn "We can help you break the curse, find peace."
        gideon "We need to uncover the truth behind the curse."

        evelyn "Would you tell us your story? What exactly happened?"

        # The Phantom's revelation
        phantom "The curse... it was cast by the very Lady Seraphina we spoke of."
        phantom "She sought power beyond imagination, and it came at a great cost."

        # The Phantom reveals its tragic tale
        phantom "Listen to my tale of betrayal and revenge,"
        phantom "one that has bound me to this manor for centuries."

        # The Phantom's tale
        phantom "I was once a servant in this very manor, loyal to Lady Seraphina."
        phantom "But when she sought power beyond imagination, she made a dark pact."
        phantom "In her quest for supremacy, she betrayed those who served her faithfully,"
        phantom "including me."

        # Evelyn and Gideon's determination
        x "Evelyn and Gideon, filled with empathy, resolved to break the curse"
        x "and free the spirit from its eternal torment."

        # End of Chapter 4
        x "Their encounter with the Phantom marked a turning point in their journey."
        x "As they delved deeper into the manor's secrets, they realized the true extent"
        x "of the darkness that shrouded Ravenwood."        

        # Choice to proceed to the next chapter
        menu:
            "Continue to Chapter 5":
                jump chapter_5_start

        # Chapter 5: The Resolution

    label chapter_5_start:

        # Background setup for Chapter 5
        scene bg manor_library with dissolve

        # Evelyn and Gideon's determination
        x "Evelyn and Gideon stood in the manor's library, determined to break the curse."

        # Evelyn and Gideon perform the ritual
        show evelyn_ball_img at left:
            size (800, 800)

        show gideon_img at right:
            size (450, 800)

        evelyn "Gideon, are you ready for this?"
        gideon "We must do it, Evelyn, to set the spirit free."

        x "They began the intricate ritual, reciting ancient incantations and following cryptic instructions."

        # The Phantom's release
        show phantom_relieved at center:
            size (500, 900)

        # Dialogue during the ritual
        evelyn "Gideon, do you feel that? The energy in the room is changing."
        gideon "Yes, Evelyn. We're close. Keep going."

        phantom "Thank you, Evelyn and Gideon. You've set me free."
        phantom "I can finally rest in peace."

        # Evelyn and Gideon's moment
        scene bg manor_library with dissolve

        show evelyn_ball_img at left:
            size (800, 800)

        show gideon_img at right:
            size (450, 800)

        show golden_particles at center:
            size (200, 500)
            ypos 900

        x "Evelyn and Gideon watched as the ghostly figure slowly dissipated,"
        x "their hearts filled with a sense of accomplishment and closure."

        # End of Chapter 5
        x "Their journey in Ravenwood Manor had come to an end, but the lessons they"
        x "learned and the bond they formed would stay with them forever."

    # This ends the game.

    return
