try:  
    result = 5/0
    print(result)  
except ZeroDivisionError:  
    print("Denominator can't be 0")  
except:  
    print("Unhandled Exception")