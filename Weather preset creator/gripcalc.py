import random

def calcDynGrip(num_drivers,racelength,avglap):
    #Where we aim to start
    raceStartGrip = 98
    num_drivers = float(num_drivers)
    estimatedLaps = (racelength*60.0)/avglap
    #Hoping the race will be 100% between a,b % distance
    maxGripAtLap = (random.randint(58,68)/100.0)*estimatedLaps
    #Random estimate of how much "continous" running ala quali it would be in practice
    practiceLength = random.randint(20,25)
    qualiLength = 25.0
    
    gain = int(maxGripAtLap*num_drivers)
    
    #Estimating they do about a,b % of "continous" running
    estimatedQPLaps = ((((practiceLength+qualiLength)*60)/avglap)
                    *num_drivers)*(random.randint(50,60)/100.0)
    transfer = estimatedQPLaps/gain*100
    
    count = 0
    tlist = []
    #Make sure its not too low, nor invalid
    while 90>transfer or transfer>100:
        estimatedQPLaps = ((((practiceLength+qualiLength)*60)/avglap)
                        *num_drivers)*(random.randint(50,60)/100.0)
        transfer = estimatedQPLaps/gain*100
        count+=1
        tlist.append(int(transfer))
        if count==100:
                print "No valid found, highest was "+str(max(tlist))+".."
                break
    #For now this might get stuck... check the prints.
    transfer = int(transfer)
    print "estimated laps:",estimatedLaps
    print "max grip at lap:",maxGripAtLap
    print "estimatedQPLaps:", estimatedQPLaps
    print "gain:",gain
    print "transfer:",transfer
    return gain, transfer

calcDynGrip(21,60,90)
