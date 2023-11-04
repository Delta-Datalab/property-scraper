from bs4 import BeautifulSoup

class Property:
    
    def __init__(self, property_type, property_data):
        self.property_type = property_type
        self.data = property_data
    
    def get_price(self):
        return self.property_type.get_price(self.data)
        
        
class ZonaPropProperty:
    
    def get_price(self, data):
        price = str(data.find('div', {'data-qa': 'POSTING_CARD_PRICE'}).text)
        return price