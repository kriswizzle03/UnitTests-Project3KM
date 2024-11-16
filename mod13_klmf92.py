import unittest
import userInput

class TestUserInput(unittest.TestCase):
    # initialize variables that are read in fron user Input in userInput.py file
    

    # symbol: capitalized, 1-7 alpha characters
    def test_symbol_capitalized(self):
        symbol = userInput.stock_symbol
        self.assertTrue(symbol.isupper(), f"Stock symbol '{symbol}' is not all capital letters.")

    def test_symbol_alpha(self):
        symbol = userInput.stock_symbol
        self.assertTrue(symbol.isalpha(), f"Stock symbol {symbol} is not made up of only alpha characters")
        

    def test_symbol_length(self):
        symbol = userInput.stock_symbol
        self.assertTrue(1 <= len(symbol) <= 7, f"Stock symbol '{symbol}' is not between 1 and 7 characters.")

    # chart type: 1 numeric character, 1 or 2
    def test_chart_type_num(self):
        chart_type = userInput.chart_type
        self.assertTrue(chart_type == "1" or chart_type == "2", f"The selection {chart_type} for chart_type is not 1 or 2.")

    # time series: 1 numeric character, 1 - 4

    # start date: date type YYYY-MM-DD

    # end date: date type YYYY-MM-DD



if __name__ == '__main__':
    unittest.main()