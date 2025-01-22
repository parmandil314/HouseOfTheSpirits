import re

from src.term import clear


class Dialogue:
    def __init__(self, tree: dict):
        self.tree = tree


esteban = {
    "start": {
        "text": f"Who are you? Are you one of those crazy friends of Clara?",
        "options": {
            1: ["I'm <NAME>. Who are you?", "i-am"],
            2: ["No. Who's she?", "who-is"],
            3: ["Yes. I see kidney failure in your future.", "kidney-failure"],
            4: ["Bye.", "abrupt-bye"]
        }
    },
    "i-am": {
        "text": f"I'm Esteban Trueba. You haven't heard of me? I'm one of the most important members of the Conservative Party.",
        "options": {
            1: ["Nice to meet you. Who's Clara?", "who-is"],
            2: ["I've heard you on the radio a few times. You were ranting about Marxism, if I remember correctly.", "opinions"],
            3: ["Bye.", "bye"]
        }
    },
    "who-is": {
        "text": f"She's my wife. She's in the back of the house reading tarot.\nI wouldn't interrupt her if I were you.\nShe'll just fill up your head with her spiritualism. I'm fine with her doing it every now and then, but her friends are insufferable. They're these three sisters who swear they're related to her somehow. They're Marxists in disguise; I'm sure of it.",
        "options": {
            1: ["You shouldn't hate on your wife like that.", "hate-on"],
            2: ["What's this about Marxists?", "opinions"],
            4: ["Bye.", "bye"]
        }
    },
    "kidney-failure": {
        "text": "What? I'm one of the healthiest people I know!",
        "options": {
            1: ["I'm going now. Remember what I told you.", "remember-bye"]
        }
    },
    "opinions": {
        "text": "Don't get me started on Marxism! It's this thing the working-class have come up with where they try to trick the rich into sharing their wealth, so that they can obtain a higher standing in society and eventually depose the very people who have given them everything they possess! It's crazy and it needs to be stopped, and it seems like I'm the only one who's smart enough to realize what the working class really wants.",
        "options": {
            1: ["Wow.", "more-opinions"],
            2: ["But from what I've heard of Marxism, the claim is that the working class is being exploited and that the workers need to control the means of production.", "more-opinions-2"],
            3: ["Bye.", "bye"]
        }
    },
    "more-opinions": {
        "text": "'Wow' is correct. I need to work now; I'm prepping for my latest essay.",
        "options": {
            1: ["Bye.", "bye"]
        }
    },
    "more-opinions-2": {
        "text": "It's all a lie, and don't question me on that. Anyway, I need to work now; I'm prepping for my latest essay.",
        "options": {
            1: ["Bye.", "bye"]
        }
    },
    "hate-on": {
        "text": "Don't question my behavior towards my wife! If you were married, I wouldn't question yours!",
        "options": {
            1: ["Now I want to ask her what she thinks of you.", "bye-2"]
        }
    },
    "abrupt-bye": {
        "text": "Wait- what? Who are you?"
    },
    "remember-bye": {
        "text": "Clara needs to keep her friends' spiritualist crap out of my face. Get out of my study!"
    },
    "bye": {
        "text": "Bye."
    },
    "bye-2": {
        "text": "Hey!"
    }
}

clara =  {
    "start": {
        "text": "The Lightning-Struck Tower... Oh, hello! Who are you?",
        "options": {
            1: ["I'm <NAME>. Who are you?", "i-am"],
            2: ["What are you doing?", "tarot"],
            3: ["Bye.", "bye"]
        }
    },
    "i-am": {
        "text": "I'm Clara.",
        "options": {
            1: ["What are you doing?", "tarot"],
            2: ["I'm just looking around.", "bye"]
        }
    },
    "tarot": {
        "text": "This is tarot. It's a way I can see the future.",
        "options": {
            1: ["What's the Lightning-Struck Tower?", "lst"],
            2: ["You can see the future?", "future"],
            3: ["...Ok.", "doubts"],
            4: ["Cool; I'm going now. Bye.", "bye"]
        }
    },
    "future": {
        "text": "Yes; I was born with the gift of clairvoyance.",
        "options": {
            1: ["What's the Lightning-Struck Tower?", "lst"],
            2: ["...Ok.", "doubts"],
            3: ["Cool; I'm going now. Bye", "bye"]
        }
    },
    "lst": {
        "text": "It means impending doom; a great tragedy or disaster. It's worrying; but it's not clear at the moment what the tragedy could be. I hope it isn't too severe.",
        "options": {
            1: ["Oh my.", "distracted-bye"],
            2: ["Yeah, right.", "doubts"],
            3: ["I hope everything ends up in a good place. I need to go.", "bye"]
        }
    },
    "doubts": {
        "text": "You may doubt it, but it's real.",
        "options": {
            1: ["What's the Lightning-Struck Tower?", "lst"],
            2: ["I need to go now.", "bye"]
        }
    },
    "bye": {
        "text": "Bye."
    },
    "distracted-bye": {
        "text": "I can't seem to figure this out... I wonder what will happen.\n\tShe clearly isn't paying attention to you anymore."
    }
}

blanca = {
    "start" : {
        "text": "Who are you?",
        "options": {
            1: ["I'm <NAME>. Who are you?", "i-am"],
            2: ["What are you reading?", "book"],
            3: ["Sorry to interrupt your reading! Bye.", "bye"]
        }
    },
    "bye": {
        "text": "Bye."
    },
    "keep-reading-bye": {
        "text": "Anyway, can I resume my reading? I want to see what gruesome fate the children meet next.\n\tShe acts as though you have said yes and reverts her attention to the book. You see an illustration of a witch carrying off a crying child."
    },
    "i-am": {
        "text": "I'm Blanca.",
        "options": {
            1: ["What book is that?", "book"],
            2: ["Nice to meet you; I have to go.", "bye"]
        }
    },
    "book": {
        "text": "This came from my uncle Marcos. He traveled all over the world and collected a lot of different books.",
        "options": {
            1: ["What's it about?", "book-about"],
            2: ["Cool! I'm going now. Bye!", "bye"]
        }
    },
    "book-about": {
        "text": "This one's a book of stories from Europe. It seems like the kind of thing parents would tell their kids to keep them in line. I'm glad Mama doesn't treat me like that.",
        "options": {
            1: ["You are remarkably mature for your age, you know. Maybe that's why.", "mature-toddler"],
            3: ["Sounds interesting.", "keep-reading-bye"]
        }
    },
    "mature-toddler": {
        "text": "Thanks! Mama says the way to raise a child is to treat them like an adult from the start, and judging from your compliment, it seems to be working.",
        "options": {
            1: ["I guess so.", "keep-reading-bye"]
        }
    }
}

jaime = {
    "start": {
        "text": "Oh, hi. Who are you?",
        "options": {
            1: ["I'm <NAME>. Who are you?", "i-am"],
            2: ["What are you writing?", "essay"],
            3: ["Bye.", "confused-bye"]
        }
    },
    "i-am": {
        "text": "I'm Jaime.",
        "options": {
            1: ["What are you working on?", "essay"],
            2: ["Nice to meet you; I need to go.", "bye"]
        }
    },
    "essay": {
        "text": "It's an essay for my medical school. It's about the ethics of various medical practices.",
        "options": {
            1: ["Cool! So do you like philosophy?", "ethics"],
            2: ["Ethics?", "ethics"],
            3: ["Interesting. I have to go now.", "bye"]
        }
    },
    "ethics": {
        "text": "I find philosophy really interesting. Talking about right and wrong and so on can be really practical for decisions of policy in and out of medical practice, and it's not dull at all. I've been getting into Marxist economic philosophy recently, and I think it provides a lot of interesting ideas that deserve a lot more recognition than they get.",
        "options": {
            1: ["Cool!", "essay-bye"],
            2: ["Marxism? But doesn't that kind of political philosophy tend to idealize our society a little too much?", "marxism"],
        }
    },
    "marxism": {
        "text": "Not necessarily. Although nothing is as black-and-white as its description, the bourgeoisie and the proletariat are very real parts of society.",
        "options": {
            1: ["I guess that's true. The line between them is blurred, though.", "essay-bye"]
        }
    },
    "essay-bye": {
        "text": "It's been nice talking, but I need to keep working on this essay. See you later!"
    },
    "confused-bye": {
        "text": "...Bye?"
    },
    "bye": {
        "text": "Bye."
    }
}

nicolas = {
    "start": {
        "text": "Hello! Care to join my flamenco class?",
        "options": {
            1: ["No thanks.", "nope"],
            2: ["Sure. How much is it?", "cost"],
            3: ["I'm <NAME>. Who are you?", "i-am"]
        }
    },
    "i-am": {
        "text": "I'm Nicolas.",
        "options": {
            1: ["So, how much money is it to participate in your class?", "cost"],
            2: ["Nice to meet you, but I need to go now.", "bye"]
        }
    },
    "nope": {
        "text": "Well, come back any time! I need to continue my lesson now. See you later!",
        "options": {
            1: ["Bye!", "bye"]
        }
    },
    "cost": {
        "text": "For one lesson it's merely...\n\tIt seems pretty expensive, but affordable.",
        "options": {
            1: ["Sure! I'll pay.", "participate-bye"],
            2: ["No thanks; I'll pass.", "nope"]
        }
    },
    "bye": {
        "text": "See you later!"
    },
    "participate-bye": {
        "text": "Great! So, the first thing you need to know about flamenco dancing is...\n\tHe begins to explain and demonstrate in great detail, and you learn a lot."
    }
}

dialogue_map = {
    "Esteban": Dialogue(esteban),
    "Clara": Dialogue(clara),
    "Blanca": Dialogue(blanca),
    "Jaime": Dialogue(jaime),
    "Nicolas": Dialogue(nicolas)
}


def run_dialogue(player, character):
    clear()
    print(f"You speak to {character.name}:")
    current_node = "start"
    while "bye" not in current_node:
        node = character.dialogue.tree[current_node]
        text = re.sub(r"<NAME>", player.name, node['text'])
        print(f"{character.name} says: {text}")
        for option in node['options']:
            text = re.sub(r"<NAME>", player.name, node['options'][option][0])
            if character.name in text:
                player.known_names.append(character.name)
            print(f"{option}: {text}")

        choice = int(input("> "))
        if 0 < choice <= len(node['options'].keys()):
            print(f"You respond: {re.sub("<NAME>", player.name, node['options'][choice][0])}")
            current_node = node['options'][choice][1]
        else:
            print("Invalid option. Please try again.")

    text = re.sub(r"<NAME>", player.name, character.dialogue.tree[current_node]["text"])
    print(f"{character.name}: {text}")
    input("Press Enter to continue.\n")
    clear()
