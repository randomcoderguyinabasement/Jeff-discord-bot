import random

facts = [
    "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion",
    "A snail breathes through its foot", 
    "Australia is wider than the moon",
    "||your mom||",
    "Sunsets on Mars are blue",
    "A mix between a Chihuahua and a dachshund is called a “chiweenie”",
    "There are no seagulls in Hawaii",
    "Dragonflies have six legs but cannot walk",
    "Gummy bears were originally called “dancing bears”",
    "There is a McDonalds in every continent except Antarctica",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted only 38 minutes",
    "The worlds largest snowflake on record measured 15 inches wide and 8 inches thick",
    "The longest wedding veil was the same length as 63.5 football fields",
    "The worlds largest grand piano was built by a 15-year-old in New Zealand. It is nine feet long and has 85 keys",
    "The worlds largest chocolate bar weighed over 12,000 pounds and was made in Armenia in 2010",
    "Honey never spoils and can last for thousands of years.",
    "Octopi have three hearts.",
    "Bananas are berries, but strawberries aren't.",
    "There are more possible iterations of a game of chess than there are atoms in the observable universe.",
    "Koalas have fingerprints similar to human fingerprints.",
    "The Great Wall of China is not visible from space with the naked eye.",
    "The unicorn is Scotland's national animal.",
    "The world's largest desert is Antarctica.",
    "A group of flamingos is called a 'flamboyance'.",
    "The name 'Bluetooth' comes from a 10th-century Danish king, King Harald 'Bluetooth' Gormsson.",
    "Cows have best friends.",
    "There is a species of jellyfish known as 'Turritopsis dohrnii' that is biologically immortal.",
    "The smell of freshly-cut grass is actually a plant distress call.",
    "The world's largest recorded snowflake was 15 inches wide.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896, lasting only 38 minutes.",
    "The fear of long words is called 'hippopotomonstrosesquipedaliophobia'.",
    "The word 'nerd' was first coined by Dr. Seuss in his book 'If I Ran the Zoo.'",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896, lasting only 38 minutes.",
    "Bananas are berries, but strawberries aren't.",
    "Honey never spoils and can last for thousands of years.",
    "There are more possible iterations of a game of chess than there are atoms in the observable universe.",
    "The unicorn is Scotland's national animal.",
    "The Great Wall of China is not visible from space with the naked eye.",
]

insults = [
    "your mom",
    "You're so slow, it takes you two hours to watch '60 Minutes",
    "I'd roast you, but my mom told me not to burn trash",
    "You're like a human napkin because everyone uses you and throws you away",
    "your hair is like a solar panel for a personality that needs recharging",
    "They say everyone has a hidden talent, but I'm still waiting for you to find yours",
]

jokes = [
    "Q. How does a computer get drunk? ||A. It takes screenshots.||",
    "Why did the tomato turn red? ||it saw salad dressing||",
    "What do you call a fake noodle? ||an impasta||",
    "Why did the scarecrow win an award? ||because he was outstanding in his field||",
]

responses = [
    "omg look at this ^",
    "the person below me does not have W rizz",
    "L imagine",
    "dude what",
    "what do yuw awANT!!!",
    "wussup",
    "your mom",
    "hola",
    "hey there",
    "hi",
    "i like trains",
    "my name is actually Bobothy",
]

def handle_response(message) -> str:
    p_message = message.lower()
    # customize response handling by returns
    if p_message == '.info':
        return('Commands: \n.fact - gives you a random fact \n.insult: gives you a random insult \n.num: gives you a random number \n.joke: gives you a random joke \nMore commands to come soon!')
    if p_message == 'hi':
        return('hi')
    if p_message == 'jeff':
        response = random.choice(responses)
        return(response)
    if p_message == '/graph':
        return('im not graphing for you, bud')
    if p_message == 'hello':
        return('hey there bestie!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    if p_message == '.num':
        return str(random.randint(0, 10000000000000000000000))
    if p_message == '.fact':
        fact = random.choice(facts)
        return(fact)
    if p_message == '.insult':
        insult = random.choice(insults)
        return(insult)
    if p_message == '.joke':
        joke = random.choice(jokes)
        return(joke)
    if p_message == 'lol':
        return('thats funny!!!!!!')
    if p_message == 'that was painfull to watch':
        return('agreed.')
    if p_message == 'oh the cringe ^':
        return('oof......')
    if p_message == '.spam':
        for i in range(10):
            return('MUAHAHAHAHAHAHAHAHAHAHAH\nMUAHAHAHAHAHAHAHAHAHAHAH\nMUAHAHAHAHAHAHAHAHAHAHAH\nMUAHAHAHAHAHAHAHAHAHAHAH')
    if random.randint(1, 10) == 1:
        resp = random.choice(responses)
        return(resp)
