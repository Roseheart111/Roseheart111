# -*- coding: utf-8 -*-
import time
#This is a comment
def unSin():
    print("The year is 1697. The witch trials era just ended but a new evil has arise, the Sinners.")
    time.sleep(3)
    print('  _    _             ')                  
    print(' | |  | |          ')               
    print(' | |  | | ___        ')     
    print(' | |  | || _ \    ')     
    print(' | |__| || | |   ')     
    print(' |_____/ |_|_|       ')   
     
    print('   ____   _      ')
    print(' / ____| (_)           ')   
    print(' |(___    _   ___       ')
    print(' \___  \ | | | _ \     ') 
    print('  ____)| | | | | |  ') 
    print(' |_____/ |_| |_|_|     ') 
    time.sleep(2)
    print('You are a saint playing by the graveyard until you get the idea to go out and explore.')
    time.sleep(1)
    choice=raw_input('You hear footsteps near you. Do you ignore it and keep playing with the dead?(Y/N)')
    while choice == 'Y':
        print('You get even more paranoid')
        time.sleep(1)
        choice=raw_input('Do you keep playing or check on where the footsteps are coming from?(Y/N)')
    print('Time to investigate!')
    time.sleep(1)
    choice=raw_input('You sneak around to find some Catholic Priests. What do you do?(Attack Them/Run Away)')
    while choice != 'Run Away' and choice !='Attack Them':
        choice=raw_input('Invalid Answer. Try again(Run Away/Attack Them)')
    if choice == 'Attack Them':
        print('You attack one of the priest that walks by.')
        time.sleep(1)
        print('You got beaten down, taken to church, had an exorcism, went crazy, hanged yourself.')
        time.sleep(1)
        print('You are dead.')
        return
    else: #you chose Run Away
        choice=raw_input('You successfully ran away. Where to go next?(Devil Punch Bowl/Sunday Service):')
        while choice != 'Devil Punch Bowl' and choice != 'Sunday Service':
            choice=raw_input('Invalid Answer.Try again. (Devil Punch Bowl/Sunday Service)')
        if choice == 'Devil Punch Bowl':
            print('You start your journey to the Devil Punch Bowl.')
            time.sleep(1)
            print('You hitch a ride with a witch riding on her broom.')
            time.sleep(1)
            print('The Priests you ran away from earlier spotted you and the witch flying.')
            time.sleep(1)
            print('You are shot down by the Priests.')
            time.sleep(1)
            print('You are dead.')
            return
        else: #you chose Sunday Service
            print('You make your way to Sunday Service at Church.')
        time.sleep(3)
        print('You are very late!')
        time.sleep(2)
        for priest in ['Priest Hamlet','Priest Romeo','Priest Brophy']:
            print('The '+priest+' approaches you with open arms and gives you a warm welcome to the church.')
            time.sleep(2)
        print('You feel loved for once in your miserable life.')
        time.sleep(1)
        choice=raw_input('What do you preach about?(Devil/ God)')
        while choice != 'Devil' and choice != 'God':
            choice=raw_input('Invalid Answer.Try again. (Devil/God)')
        if choice =='Devil':
            print('You preach about the Devil to the Catholic people.')
            time.sleep(1)
            print('They arrest you and burn you to the stake.')
            time.sleep(1)
            print('You are dead.')
            return
        else: #choice was God
            print('You preach about God to the Catholic people')
            time.sleep(1)
            print('They have made you the new priest of the Catholic Church') 
            print('You continue to live a faithful life with your husband and kids until death do you apart')  
            print ('The End') 
    