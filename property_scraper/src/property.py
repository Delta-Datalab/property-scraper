import numpy as np

class Property:
    
    def __init__(self, property_data, domain):
        self.data = property_data
        
        if domain == 'www.zonaprop.com.ar': self.property_type = ZonaPropProperty()
        else: raise ValueError("Invalid type of Property")
    
    def get_price(self):
        return (self.property_type).get_price(self.data)
    
    def get_expenses(self):
        return (self.property_type).get_expenses(self.data)
        
        
class ZonaPropProperty:
    
    def get_price(self, data):
        price = str(data.find('div', {'data-qa': 'POSTING_CARD_PRICE'}).text)
        return price
    
    def get_expenses(self, data):
        expenses_element = data.find('div', {'data-qa': 'expensas'})
        
        if expenses_element: expenses = str(expenses_element.text.strip()) # Extract text and remove leading/trailing spaces
        else: expenses = f'{np.nan}'  # Assign NaN if expenses_element is not found
        
        return expenses