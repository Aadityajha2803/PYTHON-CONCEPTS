print("Whatsup! I'm your Personal ChatBot Assistant.")
print("You can ask me whatever you feel like")

responses = {
    "hello" : "Hi, Welcome. How can I help you?",
    "how are you?": "I'm fine. Thank you",
    "who are you" : "I'm a smart AI ChatBot",
    "motivate me" : "Keep going! The secret of getting ahead is getting started",
    "happy" : "Great to know",
    "what is python?" : "Python is a programming language"
}
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I'm not able to tell that yet. I'll learn it soon"

while True:

    userInput = input("Please ask your question: ")
    reply = getResponseOfBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
        break