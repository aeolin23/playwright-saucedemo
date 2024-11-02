from locators.locator import InventoryLocators

class InventoryPage:
    def __init__(self, page):
        self.page = page
    
    def check_page_title(self):
        return self.page.locator(InventoryLocators.inventory_page_title).inner_text()
    
    def add_bolt_tshirt(self):
        self.page.locator(InventoryLocators.bolt_tshirt).click()
    
    def add_fleece_jacket(self):
        self.page.locator(InventoryLocators.fleece_jacket).click()
    
    def check_cart_qty(self):
        return self.page.locator(InventoryLocators.cart_qty).inner_text()
    
    def click_cart(self):
        self.page.locator(InventoryLocators.cart).click()