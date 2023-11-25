class Property:
    
    def __init__(self, property_data, domain):
        self.data = property_data
        
        if domain == 'www.zonaprop.com.ar': self.property_type = ZonaPropProperty()
        else: raise ValueError("Invalid type of Property")
    
    def get_price(self):
        return (self.property_type).get_price(self.data)
        
        
class ZonaPropProperty:
    
    def get_price(self, data):
        price = str(data.find('div', {'data-qa': 'POSTING_CARD_PRICE'}).text)
        return price