def fizz_buzz(n):
    for x in range(1, n+1):
        if(x%5==0 and x%3==0):
            print("FizzBuzz")
        else:
            if(x%3==0):
                print("Fizz")
            else:
                if(x%5==0):
                    print("Buzz")
                else:
                    (print(x))
          
fizz_buzz(30)
