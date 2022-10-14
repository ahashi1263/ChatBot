import random

R_EATING = "Not a big eater as you can imagine (I'm a bot haha)"
R_ADVICE = "Ask your peers for help, I don't have all the answers sorry"

def unknown():
    response = ["Could you please re-phrase that?",
                "...",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response