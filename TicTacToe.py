#Minal Kondawar
#mkondawa@indiana.edu
#Homework-1

#Decision making Agent for Tic Tac Toe


import random


def print_board():			#prints the board
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""


def check_done():			#check for winner
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " " \
        or map[0][i] == map[1][i] == map[2][i] != " ":
            print turn, "won!!!"
            return True

        
    if map[0][0] == map[1][1] == map[2][2] != " " \
    or map[0][2] == map[1][1] == map[2][0] != " ":
        print turn, "won!!!"
        return True
	

    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        print "Draw"
        return True
	        

    return False


def centerattack():		#in this function,Agent attack and win that is "Trying to Win"
	
#all rows
    
    for i in range(0,3):
        if map[i][0]==map[i][1]==computer \
	or map[i][1]==map[i][2]==computer \
	or map[i][2]==map[i][0]==computer:
	    for j in range(0,3):
	        if map[i][j]==" ":
		    map[i][j]=computer
		    return True
#all columns
    
    for i in range(0,3):
        if map[0][i]==map[1][i]==computer \
	or map[1][i]==map[2][i]==computer \
	or map[2][i]==map[0][i]==computer:
	    for j in range(0,3):
	        if map[j][i]==" ":
		    map[j][i]=computer
		    return True
#first diagonal
    
    if map[0][0]==map[1][1]==computer \
    or map[0][0]==map[2][2]==computer \
    or map[1][1]==map[2][2]==computer:
         for j in range(0,3):
	     if map[j][j]==" ":
	         map[j][j]=computer
		 return True

#second diagonal
    
    if map[0][2]==map[1][1]==computer or map[0][2]==map[2][0]==computer or map[1][1]==map[2][0]==computer:
        #print "in if second diagonal"
	if map[0][2]==" ":
            map[0][2]=computer
	    return True
	if map[1][1]==" ":
	    map[1][1]=computer
	    return True
	if map[2][0]==" ":
	    map[2][0]=computer
	    return True
    return False


def defence():		# this function is for "Trying not to lose"
    
#all rows
    for i in range(0,3):
        if map[i][0]==map[i][1]==human \
	or map[i][1]==map[i][2]==human \
	or map[i][2]==map[i][0]==human:
	    for j in range(0,3):
	        if map[i][j]==" ":
		    map[i][j]=computer
		    return True
          		        
#all columns
    for i in range(0,3):
        if map[0][i]==map[1][i]==human or map[1][i]==map[2][i]==human or map[2][i]==map[0][i]==human:
	    for j in range(0,3):
	        if map[j][i]==" ":
		    map[j][i]=computer
		    return True
    

#first diagonal
    if map[0][0]==map[1][1]==human \
    or map[0][0]==map[2][2]==human \
    or map[1][1]==map[2][2]==human:
	for j in range(0,3):
	    if map[j][j]==" ":
	        map[j][j]=computer
		return True
    
#second diagonal
    if map[0][2]==map[1][1]==human \
    or map[0][2]==map[2][0]==human \
    or map[1][1]==map[2][0]==human:
	
	if map[0][2]==" ":
            map[0][2]=computer
	    return True
	if map[1][1]==" ":
	    map[1][1]=computer
	    return True
	if map[2][0]==" ":
	    map[2][0]=computer
	    return True
	    

   	
    if map[0][0]!=map[1][1] and map[1][1]!=map[2][2] and map[0][0]!=" " and map[1][1]!=" " and map[2][2]!=" ":
        while True:				#check if diagonal is block
	    y=[2,4,8,6]
    	    z=random.choice(y)	
	    if z <=9 and z >=1:
                Y = z/3
                X = z%3
                if X != 0:
                    X -=1
                else:
                    X = 2
                    Y -=1
                   
                if map[Y][X] == " ":	
                    map[Y][X] = computer
		    return True
    

    if map[2][0]!=map[1][1]and map[1][1]!=map[0][2] and map[2][0]!=" " and map[1][1]!=" " and map[0][2]!=" ":
        while True:				#check if diagonal is block
	    y=[2,4,6,8]
    	    z=random.choice(y)
	    if z <=9 and z >=1:
                Y = z/3
                X = z%3
                if X != 0:
                    X -=1
                else:
                    X = 2
                    Y -=1
                   
                if map[Y][X] == " ":	
                    map[Y][X] = computer
		    return True

    
    if map[2][1]!=map[1][1] and map[1][1]!=map[0][1] and map[2][1]!=" " and map[1][1]!=" " and map[0][1]!=" ":
        while True:			#check if middle column is blocked
	    y=[1,3,9,7]
    	    z=random.choice(y)
	    if z <=9 and z >=1:
                Y = z/3
                X = z%3
                if X != 0:
                    X -=1
                else:
                    X = 2
                    Y -=1
                   
                if map[Y][X] == " ":	
                    map[Y][X] = computer
		    return True
    
    if map[1][0]!=map[1][1] and map[1][1]!=map[1][2] and map[1][0]!=" " and map[1][1]!=" " and map[1][2]!=" ":
        while True:			#check if middle row is blocked(X 0 X)
	    y=[1,9,7,3]
    	    z=random.choice(y)
	    if z <=9 and z >=1:
                Y = z/3
                X = z%3
                if X != 0:
                    X -=1
                else:
                    X = 2
                    Y -=1
                   
                if map[Y][X] == " ":	
                    map[Y][X] = computer	
		    return True
   #condition to check for small L and big L: strategy to block player from winning
    
    if map[0][1]==map[2][2]!=" ":
	if map[0][2]==" ":
	    map[0][2]=computer
	    return True
		
    if map[2][0]==map[1][2]!=" ":
	if map[2][2]==" ":
	    map[2][2]=computer
	    return True
    if map[2][2]==map[0][1]!=" ":
	if map[0][2]==" ":
	    map[0][2]=computer
       	    return True
    if map[2][2]==map[1][0]!=" ":
	if map[2][0]==" ":
	    map[2][0]=computer
	    return True	
    
    if map[2][2]==map[0][1]!=" ":
	if map[0][2]==" ":
	    map[0][2]=computer
            return True	
    if map[0][2]==map[1][0]!=" ":
	if map[0][0]==" ":
	    map[0][0]=computer
	    return True
    if map[2][0]==map[0][1]!=" ":
        if map[0][0]==" ":
            map[0][0]=computer
	    return True
    if map[0][2]==map[2][1]!=" ":
	if map[2][2]==" ":           
	    map[2][2]=computer
	    return True
    if map[0][0]==map[2][1]!=" ":
        if map[2][0]==" ":
 	    map[2][0]=computer
	    return True
    if map[0][0]==map[1][2]!=" ":
        if map[0][2]==" ":
	    map[0][2]=computer
	    return True
    if map[1][0]==map[2][1]!=" ":
        if map[2][0]==" ":
	   map[2][0]=computer
	   return True

    if map[2][1]==map[1][2]!=" ":
        if map[2][2]==" ":       
	    map[2][2]=computer
	    return True		
    if map[1][2]==map[0][1]!=" ":
        if map[0][2]==" ":
	    map[0][2]=computer
	    return True

    if map[1][0]==map[0][1]!=" ":
	if map[0][0]==" ":
	    map[0][0]=computer
	    return True
    
    if map[0][0]==map[1][0]==" ":
	map[0][0]=computer
	return True


    else:
        while True:
	    ran=random.randint(0,9)
	    if ran <=9 and ran >=1:
                Y = ran/3
                X = ran%3
                if X != 0:
                    X -=1
                else:
                    X = 2
                    Y -=1
                   
                if map[Y][X] == " ":	
                    map[Y][X] = computer
		    return True
		    
    
def computerdefence():		#"trying not to lose" when computer playes first
    for i in range(0,3):				#check for all rows
        if map[i][0]==map[i][1]==human \
	or map[i][1]==map[i][2]==human \
	or map[i][2]==map[i][0]==human:
	    for j in range(0,3):
	        if map[i][j]==" ":
		    map[i][j]=computer
		    return True
          		        
    for i in range(0,3):	#check for all columns
        if map[0][i]==map[1][i]==human or map[1][i]==map[2][i]==human or map[2][i]==map[0][i]==human:
	    for j in range(0,3):
	        if map[j][i]==" ":
		    map[j][i]=computer
		    return True
    
		            
    #check for first diagonal
    if map[0][0]==map[1][1]==human or map[0][0]==map[2][2]==human or map[1][1]==map[2][2]==human:
	for j in range(0,3):
	    if map[j][j]==" ":
	        map[j][j]=computer
		return True
   #check for secong diagonal
    if map[0][2]==map[1][1]==human \
    or map[0][2]==map[2][0]==human \
    or map[1][1]==map[2][0]==human:
	
	if map[0][2]==" ":
            map[0][2]=computer
	    return True
	if map[1][1]==" ":
	    map[1][1]=computer
	    return True
	if map[2][0]==" ":
	    map[2][0]=computer
	    return True
    return False           		

turn = "X"
human="X"
computer="O"
map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
done = False
flag=0
symbol=raw_input("What you wan to be X or O?")
print symbol
        
if symbol=='X':
    print "You play first" #flag 1 for human
    human=symbol
    computer="O"
else:
    print "Computer plays first"	#flag 0 for computer
    human=symbol
    computer="X"
    flag=1
print

while done != True:
    print_board()
  

    moved = False
    while moved != True:
	if computer=="X" and flag==1:
	    map[2][0]=computer
	    print "Game Starts"
	    print 
	    print_board()
	    turn="O"
            flag=0
	print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
        print "7|8|9"
        print "4|5|6"
        print "1|2|3"
        print
	

	if human=="X":		#if human plays first
	    turn="X"
            try:
                pos = input("Select: ")
                if pos <=9 and pos >=1:
                    Y = pos/3
                    X = pos%3
                    if X != 0:
                        X -=1
                    else:
                        X = 2
                        Y -=1
                    
                    if map[Y][X] == " ":	
                        map[Y][X] = turn
                        moved = True
                        done = check_done()

                        if done == False:
                            if turn == "X":
                                turn = "O"
			   		    
			        try:
				
			            if pos==1 or pos == 3 or pos == 7 or pos == 9: 
				        if map[1][1]==" ":
				            map[1][1]=computer
					    moved=True
			    		    done=check_done()
                            		    turn = human
				        else:
				            attack=centerattack()
					    if attack==True:
					        moved=True
			    		    	done=check_done()
					    	print_board()
					    	turn=human
						break                            		    	
						
					    defe=defence()    
					    if defe==True:
                                            	moved = True
					    	done = check_done()
                                            	turn=human
					    	break
				#egde opening move of player
				    if pos == 2 or pos == 4 or pos == 6 or pos==8:
				        if map[1][1]==" ": 
				            map[1][1]=computer
					    moved=True
			    		    done=check_done()
                            		    turn = human
				        else:
				            atta=centerattack()
					    if atta==True:
					    	print_board()
				            	moved=True
					    	done=check_done()
                            		    	turn = human
						break					    	
						
					    defe=defence()
					    if defe==True:
                                           
					    	moved = True
                                            	done = check_done()
                                            	turn=human
				            	break
					#center move by player	
		            	    if pos==5:
				        if map[1][1]==human:
				            map[0][0]=computer
					    moved=True
			    		    done=check_done()
                            		    turn = human
				        else:
				            
					    attack=centerattack()
					    if attack==True:
					        moved=True
			    		    	done=check_done()
						print_board()
                            		    	turn = human
					    	print_board()	
						break                            		    	
						
					    defe=defence()
					    if defe==True:
                                            	moved = True
                                            	done = check_done()
                                            	turn=human
					    	break
					
			        except:
			            print"something went wrong: computer"

			                
            except:
                print "You need to add a numeric value"
        else:
	    try:
		#if computer plays first
                pos = input("Select: ")
                if pos <=9 and pos >=1:
                    Y = pos/3
                    X = pos%3
                    if X != 0:
                        X -=1
                    else:
                        X = 2
                        Y -=1
                    
                    if map[Y][X] == " ":	
                        map[Y][X] = turn
                        moved = True
                        done = check_done()
		
			if done==False:
			    if turn=="O":
				turn="X"
				try:
				   
				    if pos==5:
					if map[0][2]==" ":
					    map[0][2]=computer
					    moved=True
					    done=check_done()
					    turn=human
				    	else:
				            attack=centerattack()
                                            if attack==True:
                                     		moved=True
                                                done=check_done()
                                                turn = human
                                                print_board()
                                                break
                                                
                                            defe=defence()
                                            if defe==True:
                                                moved = True
                                                done = check_done()
                                                turn=human
                                                break
				    if pos==1:
				       
					attack=centerattack()
					if attack==True:
					    moved=True
					    done=check_done()
					    turn=human
					    print_board()
					    break
					defe=computerdefence()
					if defe==True:
					    moved = True
                                            done = check_done()
                                            turn=human
                                            break
					if map[2][1]==" " and map[1][0]==" ":
					    map[2][1]=computer
					    moved=True
					    done=check_done()
					    turn=human
					else:
					    if map[1][1]==" ":
					    	map[1][1]=computer
					    	moved=True
					    	done=check_done()
					    	turn=human
					         
				    if pos==9:
				     
					attack=centerattack()
					if attack==True:
					 
					    moved=True
					    done=check_done()
					    turn=human
					    print_board()
					    break
					defe=computerdefence()
					if defe==True:
					    moved = True
                                            done = check_done()
                                            turn=human
                                            break
					if map[1][0]==" " and map[2][1]==" ":
					    map[1][0]=computer
					    moved=True
					    done=check_done()
					    turn=human
					else:
					    if map[1][1]==" ":
					    	map[1][1]=computer
					    	moved=True
					    	done=check_done()
					    	turn=human
				    
				    if pos==4:
					
					attack=centerattack()
					if attack==True:
					    moved=True
					    done=check_done()
					    turn=human
					    print_board()
					    break
					defe=computerdefence()
					if defe==True:
					    moved = True
                                            done = check_done()
                                            turn=human
                                            break
					if map[2][1]==" ": 
					    map[2][1]=computer
					    moved=True
					    done=check_done()
					    turn=human
										    
				    if pos==8:
					attack=centerattack()
					if attack==True:
					    moved=True
					    done=check_done()
					    turn=human
					    print_board()
					    break
					defe=computerdefence()
					if defe==True:
					    moved = True
                                            done = check_done()
                                            turn=human
                                            break
					if map[1][0]==" ":
					    map[1][0]=computer
					    moved=True
					    done=check_done()
					    turn=human
				    if pos==6:
  					attack=centerattack()
					if attack==True:
					    moved=True
					    done=check_done()
					    turn=human
					    print_board()
					    break
					defe=computerdefence()
					if defe==True:
					    moved = True
                                            done = check_done()
                                            turn=human
                                            break
					if map[0][0]==" ":
					    map[0][0]=computer
					    moved=True
					    done=check_done()
					    turn=human
			            if pos==2:				   	
					attack=centerattack()
					if attack==True:
					    moved=True
					    done=check_done()
					    turn=human
					    print_board()
					    break
					defe=computerdefence()
					if defe==True:
					    moved = True
                                            done = check_done()
                                            turn=human
                                            break
					if map[2][2]==" ":
					    map[2][2]=computer
					    moved=True
					    done=check_done()
					    turn=human
				    if pos==3:
					attack=centerattack()
					if attack==True:
					    moved=True
					    done=check_done()
					    turn=human
					    print_board()
					    break
					defe=computerdefence()
					if defe==True:
					    moved = True
                                            done = check_done()
                                            turn=human
                                            break
					if map[1][1]==" ":
					    map[1][1]=computer
					    moved=True
					    done=check_done()
					    turn=human	       
				except:
				   print "Something went wrong :Computer playing first"

	    except:
	        print "Enter numeric value"
	  
