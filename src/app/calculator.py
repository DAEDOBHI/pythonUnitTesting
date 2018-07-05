#Test Driven DEvelopment

#Prueba -> Código -> Refactoring

class Calculator():
    def get_iva(self, price, rate = .16):
        return price * rate
    def get_interest(self,initial,rate,periods,compound = False):
        if compound:
            result = 0
            for i in range(0, periods):
                result += initial * rate
                initial += initial * rate

            return round(result,2)    
        else:
            result = (initial * rate)* periods
            return result

  
