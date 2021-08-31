from CORONA import measure,assessment,m_a,prevent,feedback,roles

file=open('details.txt','a')
print('NAMASTHE\nWelcome To SAHAYOG\n\t-Always on Service\nSTAY HOME - STAY SAFE')
print('-'*20)
print('Please provide us some information about yourself\n')
red_zones={'andhra pradesh':['kurnool','guntur','krishna','chittoor','spsr nellore'],'telangana':['chandanagar','yousufguda','mayurinagar','qutubullahpur-Gajularamaram','kukatpally','moosapet','alwal','chandrayanggutta','malakpet-santoshnagar','red hills','sheikpet', 'ramhopalpet','suryapet','ranga reddy','medchal malkajgiri','vikarabad','warangal urban']}
orange_zones={'andhra pradesh':['west godavari', 'kadapa','anantapur','prakasham','east godavari','srikakulam','vishakapatnam'],'telangana':['nizamabad', 'jogulamba gadwal','nirmal','nalgonda','adilabad','sangareddy','kamareddy','kumuram bheem asifbad','karimnagar','khammam','mahabubnagar','jagitial','rajanna sircilla','jayashankar bhupalapally','medak','jangoan','narayanpet','mancherial']}
green_zones={'andhra pradesh':['vizianagaram'],'telangana':['peddapalli','nagarkurnool','mulugu','bhadradri kothagudem','mahabubabad','siddipet','warangal rural','wanaparthy','yadadri bhuvanagiri']}

#pd = Personal Details
class pd:   
    def __init__(self,name=''):
        self.rf=0 
        self.name=input('Enter your name')
        try:
            self.phone=input('Enter your Phone Number')
            if len(self.phone)!=10:
                raise ValueError
            else:
                file.write('\nPhone Number: {}\n'.format(self.phone))
        except:
            print('phone number cannot be less than 10 digits')
        self.state=input('Enter your state')
        self.state=self.state.lower()
        self.district=input('Enter your district')
        self.district=self.district.lower()
        try:
            self.age=int(input("enter age"))
            if (self.age)<0:
                raise ValueError
            else:
                file.write('Age: {}\n'.format(self.age))
        except:
            print('age can not be less than 0')
        if self.district in red_zones['andhra pradesh'] or self.district in red_zones['telangana']:
            self.rf+=4
        elif self.district in orange_zones['andhra pradesh'] or self.district in orange_zones['telangana']:
            self.rf+=2
        file.write('Name: {}\nState: {}\nDistrict:{}\n'.format(self.name,self.state,self.district))

m=True
#p=pd()
m=True
while m==True:
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    option=int(input('''Enter\n1. Self Assess\n2. Preventive Measures\n3. Measures taken by Government to support people from other states\n4. To know the Role of Police, Doctors, Media\n5. Myths and Apprehensions
6. Donation\n7. FeedBack\n8. Help-Line\n9. To get information regarding Red, Orange, Green zones\n10. COVID-19 cases in India\n11. Risk Factor\n12. State wise plot\n13. Exit'''))
    if option==1:
        k=assessment.assess(p)
    elif option==2:
        prevent.preventions()
    elif option==3:
        measure.measures()
    elif option==4:
        roles.mem_roles()
    elif option==5:
        m_a.gov()
    elif option==6:
        from CORONA import donation
    elif option==7:
        feedback.feed()
    elif option==8:
        import webbrowser
        webbrowser.open('https://www.mohfw.gov.in/pdf/coronvavirushelplinenumber.pdf')
    elif option==9:
        import webbrowser
        webbrowser.open('https://static.mygov.in/rest/s3fs-public/mygov_158831498053877021.pdf')
    elif option==10:
        from CORONA import covid_19
    elif option==11:
        print('For accurate risk factor you must take assessment\n')
        print('Risk factor scale: \n0-3(safe) \n4-7(partially safe) \n>7(unsafe)')
        
        print('your Risk Factor is: {}/10'.format(p.rf))
        try:
            file.write('\nRisk factor: {}'.format(p.rf))
        except:
            print('you should give your details')
    elif option==12:
        from CORONA import plot
    elif option==13:
        file.close() 
        print("Thank You for using SAHAYOG app")
        m=False

