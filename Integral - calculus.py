#The function
def function(x):
    #type whatever function you want
    return((x**3)+9)
    
#upper limit or  bound or higher number ? I don't realy know what it's called !
print('enter higher limit')
upper_limit = float(input())

# x is used as both the lower limit because it is the starting value and  then it is used as an input
print('enter lower limit')
x = float(input())

#dx , the smaller dx the better the approximation
dx = 0.0001






#approximated result
app_res = 0


#real result

while x <= upper_limit:
    #variable y stores the output of the function for each loop
    y = function(x)

    #variable to store the area of the region for each loop
    area_of_region = dx*y

    #adding theresult to the previous results 
    app_res = app_res + area_of_region

    #increase the input by dx
    x += dx




print()
#printing the final result
print(app_res)
print()
print('Done')


    
