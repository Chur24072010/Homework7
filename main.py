def arithmeticOperation(symbol: str):

   typeOperation = symbol

   def operation(a: int, b: int) -> float:

       try:
           a = float(a)
           b = float(b)
       except ValueError:
           return 'One of the values cannot be converted to float'
       match typeOperation:

           case '+':
               return a + b

           case '-':
               return a - b

           case '*':
               return a * b

           case '/':
               if b == 0:
                   return 'You cannot divide by 0'
               return a / b

           case _:
               return f'Operation {typeOperation} has no realization'
   return operation