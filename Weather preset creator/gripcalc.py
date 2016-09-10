import random

def calcDynGrip(num_drivers,racelength,avglap):
    #Where we aim to start
    raceStartGrip = 98
    num_drivers = float(num_drivers)
    estimatedLaps = (racelength*60.0)/avglap
    #Hoping the race will be 100% between a,b % distance
    maxGripAtLap = (random.randint(58,68)/100.0)*estimatedLaps
    #Random estimate of how much "continous" running ala quali it would be in practice
    practiceLength = 60.0
    qualiLength = 25.0
    
    gain = int(maxGripAtLap*num_drivers)
    
    #Estimating they do about a,b % of "continous" running
    pRatio =  0.30 #(random.randint(50,60)/100.0)
    qRatio =  0.60 #(random.randint(50,60)/100.0)
    estimatedPLaps = (((practiceLength*60.0)/avglap)
                    *num_drivers)*pRatio
    estimatedQLaps = (((qualiLength*60.0)/avglap)
                    *num_drivers)*qRatio
    print( "estimatedPLaps: ", estimatedPLaps)
    print( "estimatedQLaps: ", estimatedQLaps)
    
    transfer = 1
    raceEstStartGrip = 0.0
    
    pStartGrip = 97.5
    
    while raceEstStartGrip<raceStartGrip and transfer<=100:
        pEndGrip = pStartGrip + (estimatedPLaps/gain)
        qStartGrip = pStartGrip + (pEndGrip-pStartGrip)*(transfer/100)
        qEndGrip = qStartGrip + (estimatedQLaps/gain)
        raceEstStartGrip = qStartGrip + (qEndGrip-qStartGrip)*(transfer/100)
        estMaxGripLap = (100 - raceEstStartGrip)*gain/num_drivers
        transfer+=1
    
    while (maxGripAtLap>estMaxGripLap+1 or estMaxGripLap-1>maxGripAtLap) and gain>5:
        if maxGripAtLap > estMaxGripLap:
            gain += 1
        else:
            gain -= 1
        
        transfer = 1
        raceEstStartGrip = 0.0
    
        while raceEstStartGrip<raceStartGrip and transfer<=100:
            pEndGrip = pStartGrip + (estimatedPLaps/gain)
            qStartGrip = pStartGrip + (pEndGrip-pStartGrip)*(transfer/100)
            qEndGrip = qStartGrip + (estimatedQLaps/gain)
            raceEstStartGrip = qStartGrip + (qEndGrip-qStartGrip)*(transfer/100)
            estMaxGripLap = (100 - raceEstStartGrip)*gain/num_drivers
            transfer+=1
        
    #count = 0
    #tlist = []
    ##Make sure its not too low, nor invalid
    #while 90>transfer or transfer>100:
    #    estimatedQPLaps = ((((practiceLength+qualiLength)*60)/avglap)
    #                    *num_drivers)*pqRatio
    #    transfer = estimatedQPLaps/gain*100
    #    count+=1
    #    tlist.append(int(transfer))
    #    if count==100:
                #print "No valid found, highest was "+str(max(tlist))+".."
    #            print("No valid found, highest was ", str(max(tlist)))
    #            break
    
    #For now this might get stuck... check the prints.
    transfer -= 1
    transfer = int(transfer)
    #print "estimated laps:",estimatedLaps
    #print "max grip at lap:",maxGripAtLap
    #print "estimatedQPLaps:", estimatedQPLaps
    #print "gain:",gain
    #print "transfer:",transfer
    print( "estimated laps: ",estimatedLaps)
    print( "max grip at lap: " ,maxGripAtLap)
    print( "estimatedPLaps: ", estimatedPLaps)
    print( "estimatedQLaps: ", estimatedQLaps)
    print( "gain: ",gain)
    print( "transfer: ",transfer)
    print( "prac start grip: ", pStartGrip)
    print( "prac end grip: ", pEndGrip)
    print( "quli start grip: ", qStartGrip)
    print( "quli end grip: ", qEndGrip)
    print( "Race est start grip: ", raceEstStartGrip)
    print( "Aimed for: ", raceStartGrip)
    print( "100% grip at lap: ", estMaxGripLap)
    return gain, transfer

calcDynGrip(30.0,120.0,121.0)
