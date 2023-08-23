class Card(object):
    
    values = {1: 'Ace', 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:'Jack', 12:'Queen', 13:'King'}
    suits = {'d':'Diamonds', 's':'Spades', 'c':'Clubs', 'h':'Hearts'}
    
    
    # initializes the variables value and suit
    def __init__(self, value, suit): 
        
        self.value = value
        self.suit = suit
        
    
    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit
        
    
    #this is a special class that allows for us to create a string value and be able to print that value later
    def __str__(self):
        
        my_card = str(Card.values[self.value]) + ' of ' + str(Card.suits[self.suit])
        return my_card
    
    
my_card = Card(3,'d')
print(my_card)
        
