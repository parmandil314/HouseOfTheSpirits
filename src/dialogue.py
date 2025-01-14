class Dialogue:
    def __init__(self, tree: dict):
        self.tree = tree

esteban_1 = {
    "start" : {
        "text" : f"Who are you? Are you one of those crazy friends of Clara?",
        "options" : {

        }
    }
}

dialogue_map = {
    "Esteban" : Dialogue(esteban_1)
}