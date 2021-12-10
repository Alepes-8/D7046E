from ChatBotTrainer import *

#load saved states of trained network
network = torch.load("network.pth")  
word_vectorizer = pickle.load(open("word_vectorizer.pickle", "rb"))   

while True:
    print("BOT:is there a problem with the product or service here at amazon?")
    x = input()
    #preprocessing of reply needs to added, i suppose
    validation_data = word_vectorizer.transform([x])
    validation_data = validation_data.todense()
    validation_x_tensor = torch.from_numpy(np.array(validation_data)).type(torch.FloatTensor)  
    prediction= network(validation_x_tensor)
    guess = torch.argmax(prediction, dim=-1)
    #logic for handling the bots' reply 
    #print(prediction) #to check if statement below is correct
    if ((guess.item()==0 and prediction[0][0]>0.9) or (guess.item()==1 and prediction[0][1]>0.9)):  #the network be more than 80% about its reply otherwise the user need to elaborate          
        if(guess.item()==0):
            print("BOT:Im very sorry to hear that, we will take it into consideration")
        else:
            print("BOT:Glad to Hear that")

        print("BOT:Anything else? Y/N")
        x = input()
        if(x=="N"):
            break
    else:
        print("BOT:I did not understand, Try to be more specific")