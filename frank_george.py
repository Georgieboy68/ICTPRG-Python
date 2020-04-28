#Start
#INPUT Frank or George
  #PRINT Welcome
#ELSE
 
       #PRINT Not Recognised
 #End
 
Username_1='Frank'
Username_2='George'
Username=input ('Enter your Username: ')
if Username==Username_1 or Username==Username_2:
        print ('Welcome:' , Username)
else:
    print('Name is not recognised',)

