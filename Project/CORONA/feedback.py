file=open('details.txt','a')
pin=0
landmark=0
feba=0
def feed():
    print('As a result of lockdown, many vegetable vendors fear coming to the places they generally supply and find an alternative place, generally near to their homes.')
    print('Due to this, many people find it difficult to buy groceries, especially the people below the poverty line.')
    print('Hence, the government has taken an initiative in which vegetable and grocery vendors would be assigned at a loction entered.')
    print('Rationing services would also be provided')
    print('Is there a shortage of groceries and vegetables in your area?')
    var=input('If Yes, Press Y')
    if(var=='y' or var=='Y'):
        class feedback:
            def __init__(self,pc,lm,fb):
                self.pc=pc
                self.lm=lm
                self.fb=fb
            def confirm(self):
                print('Pin Code:',self.pc)
                print('Landmark:',self.lm)
                print('Comments:',self.fb)
                x=input('Confirm (Press Y or N)')
                if (x=='Y' or x=='y'):
                    file.write('\nPin Code: {} \nLandmark: {} \nComments:{}'.format(self.pc,self.lm,self.fb))
                    file.close()
                    print('Thank you, your response has been recorded')
                elif(x=='N' or x=='n'):
                    objectt()
                else:
                    print('Enter valid option')
                    confirm()
        def objectt():
            pin=int(input('Enter pin code'))
            landmark=input('Enter landmark')
            feba=input('Enter comments')
            ob=feedback(pin,landmark,feba)
            
            ob.confirm()
        objectt()
    else:
        print('Thank You')
