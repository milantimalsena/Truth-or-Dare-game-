import random

truths = [
    "What is your biggest fear? Answer truthfully.",
    "Have you ever cheated on a test? Answer truthfully.",
    "What is a secret you've never told anyone? Answer truthfully.",
    "Have you ever lied to get out of trouble? Answer truthfully.",
    "Who was your first crush? Answer truthfully.",
    "Have you ever stolen something, even small? Answer truthfully.",
    "Have you ever kept a secret from your best friend? Answer truthfully.",
    "Do you have a secret talent no one knows about? Answer truthfully.",
    "Have you ever pretended to like someone when you didn’t? Answer truthfully.",
    "Have you ever broken a promise? Answer truthfully.",
    "What’s the most embarrassing thing you’ve ever done? Answer truthfully.",
    "Who is the last person you stalked on social media? Answer truthfully.",
    "Have you ever been jealous of a friend? Answer truthfully.",
    "Have you ever had a crush on a friend’s partner? Answer truthfully.",
    "Have you ever cried over something silly? Answer truthfully.",
    "What’s the biggest secret you’ve kept from your parents? Answer truthfully.",
    "Have you ever been caught lying? Answer truthfully.",
    "Have you ever had a fake laugh in a conversation? Answer truthfully.",
    "Have you ever talked about someone behind their back? Answer truthfully.",
    "Do you have a guilty pleasure song? Answer truthfully.",
    "Have you ever read someone’s private messages without permission? Answer truthfully.",
    "Have you ever been rejected by someone you liked? Answer truthfully.",
    "Have you ever said ‘I love you’ and didn’t mean it? Answer truthfully.",
    "Have you ever embarrassed yourself in public? Answer truthfully.",
    "Have you ever wished someone would fail at something? Answer truthfully.",
    "Do you have an irrational fear? Answer truthfully.",
    "Have you ever regretted meeting someone? Answer truthfully.",
    "Have you ever cried for no reason? Answer truthfully.",
    "Have you ever wanted to quit something important to you? Answer truthfully.",
    "Have you ever ignored a friend’s text on purpose? Answer truthfully.",
    "Do you have a habit you’re ashamed of? Answer truthfully.",
    "Have you ever blamed someone else for your mistake? Answer truthfully.",
    "Have you ever laughed at a serious moment? Answer truthfully.",
    "Have you ever pretended to know something you didn’t? Answer truthfully.",
    "Do you have a secret nickname for someone? Answer truthfully.",
    "Have you ever been caught daydreaming in a serious situation? Answer truthfully.",
    "Have you ever ruined a surprise for someone? Answer truthfully.",
    "Have you ever been jealous of someone’s success? Answer truthfully.",
    "Have you ever skipped an important event without a good reason? Answer truthfully.",
    "Have you ever wished you could swap lives with someone? Answer truthfully.",
    "Have you ever avoided someone in public? Answer truthfully.",
    "Do you have a crush right now? Answer truthfully.",
    "Have you ever laughed so hard you cried? Answer truthfully.",
    "Have you ever said something you instantly regretted? Answer truthfully.",
    "Have you ever been caught talking to yourself? Answer truthfully.",
    "Have you ever kept a gift you didn’t like? Answer truthfully.",
    "Have you ever sent a text to the wrong person? Answer truthfully.",
    "Have you ever had a silly argument that turned serious? Answer truthfully.",
    "Have you ever snooped through someone’s stuff? Answer truthfully.",
    "Have you ever lied in a game of Truth or Dare? Answer truthfully.",
    "Have you ever wished you could erase a memory? Answer truthfully."
]

dares = [
    "Do 10 push-ups right now",
    "Sing the chorus of your favorite song out loud",
    "Post an embarrassing photo on your social media",
    "Send a random emoji to the 5th person in your contacts",
    "Talk in an accent for the next 10 minutes",
    "Eat a spoonful of a condiment of the group’s choice",
    "Do your best dance move for 30 seconds",
    "Text someone ‘I have a secret’ and don’t explain",
    "Balance a book on your head for one minute",
    "Speak only in questions for the next 5 minutes",
    "Swap an item of clothing with someone in the room",
    "Call a random contact and sing ‘Happy Birthday’",
    "Imitate a celebrity until someone guesses who it is",
    "Put an ice cube down your back",
    "Take a silly selfie and set it as your profile picture",
    "Eat something without using your hands",
    "Talk without moving your lips for 1 minute",
    "Do a runway walk across the room",
    "Act like a cat until your next turn",
    "Spin around 10 times and try to walk straight",
    "Let someone write on your forehead with a marker",
    "Do your best impression of a baby crying",
    "Smell another player’s shoes",
    "Post ‘I love broccoli’ on your social media",
    "Let the group choose something for you to eat blindfolded",
    "Keep your eyes closed until your next turn",
    "Speak in rhyme for the next 3 minutes",
    "Let someone redo your hairstyle",
    "Eat a raw onion slice",
    "Let someone tickle you for 20 seconds",
    "Hold a plank for 30 seconds",
    "Send a voice note singing the alphabet to someone",
    "Say the alphabet backwards as fast as you can",
    "Hop on one leg for 1 minute",
    "Let another player DM someone from your account",
    "Eat a spoonful of something spicy",
    "Put socks on your hands until your next turn",
    "Draw something on your face with lipstick",
    "Talk like a robot for the next 5 minutes",
    "Imitate someone in the room until they guess it’s them",
    "Do your best evil laugh",
    "Do the chicken dance for 30 seconds",
    "Walk across the room like a model",
    "Drink a mystery mix made by the group",
    "Draw a mustache on your face",
    "Let someone choose your phone wallpaper",
    "Do 20 squats right now",
    "Pretend to be a waiter and take everyone’s ‘order’",
    "Say something in a made-up language",
    "Eat a piece of lemon without making a face"
]


while True:
      choice = input("Choose 'truth' or 'dare' or 'quit':  ").strip().lower()

      if choice == "0" or choice == "quit" or choice == "exit":
      
          break
  
      else:
          if choice == "truth":
              print("Truth: " + random.choice(truths))
          elif choice == "dare":
              print("Dare: " + random.choice(dares))
          
              continue
print("Thanks for playing Truth or Dare!")

