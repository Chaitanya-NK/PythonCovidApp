red_zones={'andhra pradesh':['kurnool','guntur','krishna','chittoor','spsr nellore'],'telangana':['chadannagar','yousufguda','mayurinagar','qutubullahpur-Gajularamaram','kukatpally','moosapet','alwal','chandrayanggutta','malakpet-santoshnagar','red hills','sheikpet', 'ramhopalpet','suryapet','ranga reddy','medchal malkajgiri','vikarabad','warangal urban']}
orange_zones={'andhra pradesh':['west godavari', 'kadapa','anantapur','prakasham','east godavari','srikakulam','vishakapatnam'],'telangana':['nizamabad', 'jogulamba gadwal','nirmal','nalgonda','adilabad','sangareddy','kamareddy','kumuram bheem asifbad','karimnagar','khammam','mahabubnagar','jagitial','rajanna sircilla','jayashankar bhupalapally','medak','jangoan','narayanpet','mancherial']}
green_zones={'andhra pradesh':['vizianagaram'],'telangana':['peddapalli','nagarkurnool','mulugu','bhadradri kothagudem','mahabubabad','siddipet','warangal rural','wanaparthy','yadadri bhuvanagiri']}
class assess():
    def __init__(self,other):
        print('Kindly provide correct information')
        t=input("Did you travel in the past 15 days?")
        if(t=="yes" or t=='YES' or t=='Yes'):
            b=input("domestic or international?")
            if(b=="domestic"):
                other.city,other.state=map(str,input("enter the city and state to which you have travelled:").split())
                if other.city in red_zones['andhra pradesh'] or other.city in red_zones['telangana']:
                    other.rf+=3
                elif other.city in orange_zones['andhra pradesh'] or other.city in orange_zones['telangana']:
                    other.rf+=2
            elif(b=="international"):
                other.rf+=3
                other.country=input("enter the country to which you have travelled:")
                other.place=input('Where are you currently staying?')
        print('The test below is a very important one. Please give correct answers\n\n')
        print('Are you experiencing any of the following symptoms?\n')
        other.prob=list(map(int,input('1)Cough\n2)Fever\n3)Difficulty in breathing\n4)None of the above\n').split()))
        print('Have you ever had any of the following:')
        other.disease=list(map(int,input('1)Diabetes\n2)Hypertension\n3)Lung Disease\n4)Heart Disease\n5)None of the above').split()))
        print('What is your profession?')
        other.profession=int(input('1)Police\n2)Doctor\n3)Other\n'))
        print('Thank you for taking this test')
        print('\n')
        if(4 in other.prob and 5 in other.disease and other.profession==3):
            print('Your risk of infection is low')
            print('Take precautionary measures and consult a doctor if any symptoms develop')
        else:
            other.rf+=2
            print('You are likely to get infected. Taking proper precautions can prevent the same.')
            print('Contact our helpline if symptmoms develop\nWe will help you in suggesting near hospitals available')

