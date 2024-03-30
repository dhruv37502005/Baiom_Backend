# from django.shortcuts import render
# from django.http import HttpResponse
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# import time 

# time.clock = time.time
# testing

# bot = ChatBot('chatbot',read_only=False,logic_adapters=['chatterbot.logic.BestMatch'])


# list_to_train = [
#      "hi",
#      "hi,there",
#      "what is your name?",
#      "I'm just a chatbot",
#      "what is fav food",
#      "cheese",
#  ]

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)

# def chatbot(request):
#     return render(request,'chatbot.html')

# def getResponse(request):
#     userMessage = request.GET.get('userMessage')
#     chatResponse = str(bot.get_response(userMessage))
#     return HttpResponse(chatResponse)