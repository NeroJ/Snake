# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:43:27 2011

@author: Administrator
"""
from Tkinter import *
import random 
words_list=open('words.txt','r')
lines=words_list.readline()
lst=lines.split()
#lst=['clear','cat','move','dog','chemistry','flur','right','heal','python','jerk','land','mark','player','pear','glue','project']
y=0
username=[]
usernumber=[]
highscore=[0]
highscore0=[0]
class SnakeGameStudyEnglish:
        
    

    def __init__(self):
        
        self.memoryscore=[]
        self.step=15
        # game score
        self.gamescore=-10
        self.gamelevel=-1
        
        # to initialize the snake in the range of (x1,y1,x2,y1)                
        r=random.randrange(191,191+15*10,self.step)
        self.snakeX=[r,r+self.step,r+self.step*2]
        self.snakeY=[r,r,r]
        
        # to initialize the moving direction
        self.snakeDirection = 'left'  
        self.snakeMove = [-1,0]
        # to draw the game frame 
        window = Tk()
        window.geometry("600x400+10+10")
        window.maxsize(600,400)
        window.minsize(600,400)
        window.title("Snake game")
        
        self.frame1=Frame(window)
        self.frame2=Frame(window)
        self.canvas=Canvas(self.frame1,width=590,height=375,bg="yellow")
        self.score_label=Label(self.frame2,text="Score:")
        self.level_label=Label(self.frame2,text="Level:")
        self.username_label=Label(self.frame2,text="Please Eat Each Letter In Right Order")
        
        self.frame1.pack()
        self.frame2.pack(fill=BOTH)
        self.score_label.pack(side=LEFT) 
        self.level_label.pack(side=RIGHT)
        self.username_label.pack()
        self.canvas.pack(fill=BOTH)
         
        self.draw_wall()
        self.draw_score()
        self.draw_food()
        self.draw_snake()
        self.draw_level()
        
        self.play()
        
        window.mainloop()

    "=== View Part ==="
   
            
    def draw_wall(self):
        self.canvas.create_line(10,10,582,10,fill='blue',width=5)
        self.canvas.create_line(10,359,582,359,fill='blue',width=5)
        self.canvas.create_line(10,10,10,359,fill="blue",width=5)
        self.canvas.create_line(582,10,582,359,fill="blue",width=5)
    def draw_level(self):
        self.level()
        self.level_label.config(self.level_label,text="Level: "+str(self.gamelevel))
        
        
        
        
    def draw_score(self):
        self.score()                       
        self.score_label.config(self.score_label,text="Score: "+str(self.gamescore))
    
            
        
    def draw_food(self):
        
        #lst=['clear','cat','move','dog','chemistry','flur','right','heal','python','jerk','land','mark','plyer','pear','glue','project']
        #p=random.randrange(0,15,1)
        self.Ew=random.choice(lst)
        self.lst1=[]
        
        for x in range(len(self.Ew)):
             self.foodx,self.foody=self.random_food()
             self.canvas.create_rectangle(self.foodx,self.foody,self.foodx+self.step,self.foody+self.step ,tags="food"+str(x),fill='red')
             self.canvas.create_text(self.foodx+7,self.foody+7,text=self.Ew[x],tags='food'+str(x))
             self.lst1.append([self.foodx,self.foody,'food'+str(x)])
        print self.Ew     
           
            
             
             
  
    def draw_snake(self):
        self.canvas.delete("snake")
        x,y=self.snake()                    
        for i in range(len(x)):             
            self.canvas.create_rectangle(x[i],y[i],x[i]+self.step,y[i]+self.step\
            , fill='orange',tags='snake')    
    
    "=== Model Part ==="
    # food model
    def random_food(self):      
        return(random.randrange(11,570,self.step),random.randrange(11,340,self.step))
    
    # snake model
    def snake(self):
        for i in range(len(self.snakeX)-1,0,-1):
            self.snakeX[i] = self.snakeX[i-1]
            self.snakeY[i] = self.snakeY[i-1]
        self.snakeX[0] += self.snakeMove[0]*self.step
        self.snakeY[0] += self.snakeMove[1]*self.step
        return(self.snakeX,self.snakeY)
        
    #score model    
    def score(self):
        self.gamescore+=10
    def level(self):
        self.gamelevel+=1
        
    
    "=== Control Part ==="  
    def iseated(self):
        #global c
        #for c in range(len(self.Ew)):
        if self.snakeX[0]==self.lst1[0][0] and self.snakeY[0]==self.lst1[0][1]:
            
            
            return True
        else:
            return False
    
    def isdead(self):
        if self.snakeX[0]<8 or self.snakeX[0] >580 or\
        self.snakeY[0]<8 or self.snakeY[0]>350 :
            return True
        
        for i in range(1,len(self.snakeX)):
            if self.snakeX[0]==self.snakeX[i] and self.snakeY[0]==self.snakeY[i] :
                return True
        else:
            return False
    def delete(self):
        self.canvas.delete(self.lst1[0][2])
        self.lst1.remove(self.lst1[0])
        if len(self.lst1)==0:
            self.draw_food()
            
              
    
    def move(self,event):
    # left:[-1,0],right:[1,0],up:[0,1],down:[0,-1] 
    
        if (event.keycode == 39 or event.keycode == 68) and self.snakeDirection != 'left':
            self.snakeMove = [1,0]
            self.snakeDirection = "right"
        elif (event.keycode == 38 or event.keycode == 87) and self.snakeDirection != 'down':
            self.snakeMove = [0,-1]
            self.snakeDirection = "up"
        elif (event.keycode == 37 or event.keycode == 65) and self.snakeDirection != 'right':
            self.snakeMove = [-1,0]
            self.snakeDirection = "left"
        elif (event.keycode == 40 or event.keycode == 83) and self.snakeDirection != 'up':
            self.snakeMove = [0,1]
            self.snakeDirection = "down"
        else:
            pass

#       above codes can be insteaded by the following codes 
        
#        if (event.keysym == 'Right' or event.keysym == 'd') and self.snakeDirection != 'left':
#            self.snakeMove = [1,0]
#            self.snakeDirection = "right"
#        elif (event.keysym == 'Up' or event.keysym == 'w') and self.snakeDirection != 'down':
#            self.snakeMove = [0,-1]
#            self.snakeDirection = "up"
#        elif (event.keysym == 'Left' or event.keysym == 'a') and self.snakeDirection != 'right':
#            self.snakeMove = [-1,0]
#            self.snakeDirection = "left"
#        elif (event.keysym == 'Down' or event.keysym == 's') and self.snakeDirection != 'up':
#            self.snakeMove = [0,1]
#            self.snakeDirection = "down"
#        else:
#            pass
             
    def play(self):
        self.canvas.bind("<Key>",self.move)
        self.canvas.focus_set()
        

        while True:
            
            if self.isdead():
                self.gameover()
                break
       
            elif self.iseated():
               
                self.snakeX[0] += self.snakeMove[0]*self.step
                self.snakeY[0] += self.snakeMove[1]*self.step   
                self.snakeX.insert(1,self.lst1[0][0])
                self.snakeY.insert(1,self.lst1[0][1])

                self.draw_score()
                self.delete()
                self.draw_snake()
                if self.gamescore%30==0:
                   self.draw_level()
                
                
            else:
                self.draw_snake() 
                self.canvas.after(200-10*self.gamelevel)
                self.canvas.update()
        
    def gameover(self):
        highscoreE=0
        self.memoryscore.append(self.gamescore)
        for element in self.memoryscore:
            if element>highscoreE:
                highscoreE=element
        
        if self.gamescore==highscoreE:
            highscore.remove(highscore[0])
            highscore.append(highscoreE)
            file_name='highscoreE.txt'
            text=open(file_name,'a')
            text.write(str(highscoreE)+'、'+str(username[0])+ '、'+str(usernumber[0])+'   \n')
            text.close()
        self.canvas.unbind('<Key>')
        self.canvas.bind("<Key>",self.restart)
        self.canvas.create_text(270,180,text="                   Game Over!\n \
        Press any key to continue",font='Helvetica -30 bold',tags='text')

    def restart(self,event):
        
        self.canvas.delete("snake","text")
        for u in range(len(self.lst1)):
             self.canvas.delete(self.lst1[u][2])
        self.lst1=[]     
        self.canvas.unbind('<Key>')

        # to initialize the snake in the range of (191,191,341,341)                
        r=random.randrange(191,191+15*10,self.step)
        self.snakeX=[r,r+self.step,r+self.step*2]
        self.snakeY=[r,r,r]
        
        # to initialize the moving direction
        self.snakeDirection = 'left'  
        self.snakeMove = [-1,0]
        
        # reset the score to zero
        self.gamelevel=-1
        self.gamescore=-10 
        self.draw_score()
        self.draw_level()
        
        # to initialize the game (food and snake)
        self.draw_food()
        
        self.draw_snake()
        
        # to play the game
        self.play()
class SnakeGameClassical:
    

    def __init__(self):
        self.memoryscore0=[]
        self.step=15
        # game score
        self.gamescore0=-10
        self.gamelevel=1
        
        # to initialize the snake in the range of (x1,y1,x2,y1)                
        r=random.randrange(191,191+15*10,self.step)
        self.snakeX=[r,r+self.step,r+self.step*2]
        self.snakeY=[r,r,r]
        
        # to initialize the moving direction
        self.snakeDirection = 'left'  
        self.snakeMove = [-1,0]
        # to draw the game frame 
        window = Tk()
        window.geometry("600x400+10+10")
        window.maxsize(600,400)
        window.minsize(600,400)
        window.title("Snake game")
        
        self.frame1=Frame(window)
        self.frame2=Frame(window)
        self.canvas=Canvas(self.frame1,width=590,height=375,bg="yellow")
        self.score_label=Label(self.frame2,text="Score:")
        self.level_label=Label(self.frame2,text="Level:")
        
        self.frame1.pack()
        self.frame2.pack(fill=BOTH)
        self.score_label.pack(side=LEFT) 
        self.level_label.pack()
        self.canvas.pack(fill=BOTH)
         
        self.draw_wall()
        self.draw_score()
        self.draw_food()
        self.draw_snake()
        self.draw_level()
        
        self.play()
        
        window.mainloop()

    "=== View Part ==="        
    def draw_wall(self):
        self.canvas.create_line(10,10,582,10,fill='blue',width=5)
        self.canvas.create_line(10,359,582,359,fill='blue',width=5)
        self.canvas.create_line(10,10,10,359,fill="blue",width=5)
        self.canvas.create_line(582,10,582,359,fill="blue",width=5)
    def draw_level(self):
        self.level()
        self.level_label.config(self.level_label,text="Level: "+str(self.gamelevel))
        
        
        
        
    def draw_score(self):
        self.score()                        # score model
        self.score_label.config(self.score_label,text="Score: "+str(self.gamescore0))
        
    def draw_food(self):
        self.position=[]
        for f in range(self.gamelevel):
            self.foodx,self.foody=self.random_food()    #food model
            self.canvas.create_rectangle(self.foodx,self.foody,self.foodx+self.step,self.foody+self.step,fill='red' ,tags="food"+str(f))     #food view
            self.position.append([self.foodx,self.foody,'food'+str(f)])
        #print self.position    
    def draw_snake(self):
        self.canvas.delete("snake")
        x,y=self.snake()                    # snake model
        for i in range(len(x)):             # snake view
            self.canvas.create_rectangle(x[i],y[i],x[i]+self.step,y[i]+self.step\
            , fill='orange',tags='snake')    
    
    "=== Model Part ==="
    # food model
    def random_food(self):      
        return(random.randrange(11,570,self.step),random.randrange(11,340,self.step))
    
    # snake model
    def snake(self):
        for i in range(len(self.snakeX)-1,0,-1):
            self.snakeX[i] = self.snakeX[i-1]
            self.snakeY[i] = self.snakeY[i-1]
        self.snakeX[0] += self.snakeMove[0]*self.step
        self.snakeY[0] += self.snakeMove[1]*self.step
        return(self.snakeX,self.snakeY)
        
    #score model    
    def score(self):
        self.gamescore0+=10
    def level(self):
        self.gamelevel+=1
        
    
    "=== Control Part ==="     
    def iseated(self):
        for self.d in range(len(self.position)):
            if self.snakeX[0]==self.position[self.d][0] and self.snakeY[0]==self.position[self.d][1]:
                
                return True
        else:
            return False
    def ruin(self):
     
        self.canvas.delete(self.position[self.d][2])
        self.position.remove(self.position[self.d])
        #print self.position
        if self.position==[]:
            self.draw_food()        
    
    def isdead(self):
        if self.snakeX[0]<8 or self.snakeX[0] >580 or\
        self.snakeY[0]<8 or self.snakeY[0]>350 :
            return True
        
        for i in range(1,len(self.snakeX)):
            if self.snakeX[0]==self.snakeX[i] and self.snakeY[0]==self.snakeY[i] :
                return True
        else:
            return False
    
    def move(self,event):
    # left:[-1,0],right:[1,0],up:[0,1],down:[0,-1] 
    
        if (event.keycode == 39 or event.keycode == 68) and self.snakeDirection != 'left':
            self.snakeMove = [1,0]
            self.snakeDirection = "right"
        elif (event.keycode == 38 or event.keycode == 87) and self.snakeDirection != 'down':
            self.snakeMove = [0,-1]
            self.snakeDirection = "up"
        elif (event.keycode == 37 or event.keycode == 65) and self.snakeDirection != 'right':
            self.snakeMove = [-1,0]
            self.snakeDirection = "left"
        elif (event.keycode == 40 or event.keycode == 83) and self.snakeDirection != 'up':
            self.snakeMove = [0,1]
            self.snakeDirection = "down"
        else:
            pass

#       above codes can be insteaded by the following codes 
        
#        if (event.keysym == 'Right' or event.keysym == 'd') and self.snakeDirection != 'left':
#            self.snakeMove = [1,0]
#            self.snakeDirection = "right"
#        elif (event.keysym == 'Up' or event.keysym == 'w') and self.snakeDirection != 'down':
#            self.snakeMove = [0,-1]
#            self.snakeDirection = "up"
#        elif (event.keysym == 'Left' or event.keysym == 'a') and self.snakeDirection != 'right':
#            self.snakeMove = [-1,0]
#            self.snakeDirection = "left"
#        elif (event.keysym == 'Down' or event.keysym == 's') and self.snakeDirection != 'up':
#            self.snakeMove = [0,1]
#            self.snakeDirection = "down"
#        else:
#            pass
             
    def play(self):
        self.canvas.bind("<Key>",self.move)
        self.canvas.focus_set()

        

        while True:
            if self.isdead():
                self.gameover()
                break
            elif self.iseated():
           
                self.snakeX[0] += self.snakeMove[0]*self.step
                self.snakeY[0] += self.snakeMove[1]*self.step   
                self.snakeX.insert(1,self.position[self.d][0])
                self.snakeY.insert(1,self.position[self.d][1])

                self.draw_score()
                self.ruin()
                
                self.draw_snake()
                if self.gamescore0%50==0:
                   self.draw_level()
                
                
            else:
                self.draw_snake() 
                self.canvas.after(200-15*(self.gamelevel))
                self.canvas.update()
        
    def gameover(self):
        highscoreC=0
        self.memoryscore0.append(self.gamescore0)
        for el in self.memoryscore0:
            if el > highscoreC:
                highscoreC=el
        if self.gamescore0==highscoreC:
            highscore0.remove(highscore0[0])
            highscore0.append(highscoreC)
        file_name0='highscoreC.txt'
        text0=open(file_name0,'a')
        text0.write(str(highscoreC)+'、'+str(username[0])+ '、'+str(usernumber[0])+'   \n')
        text0.close()    
        self.canvas.unbind('<Key>')
        self.canvas.bind("<Key>",self.restart)
        self.canvas.create_text(270,180,text="                   Game Over!\n \
        Press any key to continue",font='Helvetica -30 bold',tags='text')

    def restart(self,event):
        self.canvas.delete("snake",'text')
        for t in range(len(self.position)):
            self.canvas.delete(self.position[t][2])
        self.canvas.unbind('<Key>')

        # to initialize the snake in the range of (191,191,341,341)                
        r=random.randrange(191,191+15*10,self.step)
        self.snakeX=[r,r+self.step,r+self.step*2]
        self.snakeY=[r,r,r]
        
        # to initialize the moving direction
        self.snakeDirection = 'left'  
        self.snakeMove = [-1,0]
        
        # reset the score to zero
        self.gamelevel=1
        self.gamescore0=-10 
        self.draw_score()
        self.draw_level()
        
        # to initialize the game (food and snake)
        self.draw_food()
        self.draw_snake()
        
        # to play the game
        self.play()        
class HighScore:
     def __init__(self):
         
          window=Tk()
          window.title('HighScore')
          self.canvas = Canvas(window, width = 400, height = 300,bg='white')
          self.canvas.pack()
          self.canvas.create_text(120,30,text="EglishModdle Highest Score:      "+str(highscore[0]))
          self.canvas.create_text(120,100,text="ClassicalModdle Highest Score:      "+str(highscore0[0]))
          self.canvas.create_text(120,170,text="Your Name:    "+str(username[0]))
          self.canvas.create_text(120,240,text="Your Number:    "+str(usernumber[0]))
          window.mainloop()
class WordsList:
      def __init__(self):
          window=Tk()
          window.title('WordsList')
          self.canvas = Canvas(window, width = 300, height = 300,bg='white')
          self.canvas.pack()
          for self.u in range(len(lst)):
              if self.u<=3: 
                  self.canvas.create_text(50,60+40*self.u,text=lst[self.u])
              elif 3<self.u<=7:
                  self.canvas.create_text(150,60+40*(self.u-4),text=lst[self.u])
              elif 7<self.u<=11:
                  self.canvas.create_text(200,60+40*(self.u-8),text=lst[self.u])
              elif 11<self.u<=15:
                  self.canvas.create_text(250,60+40*(self.u-12),text=lst[self.u])
                  
#          self.canvas.create_text(50,60,text='clear')
#          self.canvas.create_text(50,100,text='cat')
#          self.canvas.create_text(50,140,text='move')
#          self.canvas.create_text(50,180,text='dog')
#          self.canvas.create_text(150,60,text='chemistry')
#          self.canvas.create_text(150,100,text='flur')
#          self.canvas.create_text(150,140,text='right')
#          self.canvas.create_text(150,180,text='heal')
#          self.canvas.create_text(200,60,text='python')
#          self.canvas.create_text(200,100,text='jerk')
#          self.canvas.create_text(200,140,text='land')
#          self.canvas.create_text(200,180,text='mark')
#          self.canvas.create_text(250,60,text='player')
#          self.canvas.create_text(250,100,text='pear')
#          self.canvas.create_text(250,140,text='glue')
#          self.canvas.create_text(250,180,text='project')
          window.mainloop()
class UserName:
      def __init__(self): 
          self.window=Tk()
          self.window.title("UserInformation")
          self.canvas = Canvas(self.window, width = 300, height = 100,bg='yellow') 
          frame=Frame(self.window)
          self.canvas.pack()
          frame.pack()
          self.canvas.create_text(150,50,text='Welcome To SnakeGame')
          Label(frame,text = "Your Name:").grid(row=1,column=1)
          Label(frame,text = 'Your Number:').grid(row=2,column=1)
          self.usernameVar=StringVar()
          entry1=Entry(frame,textvariable=self.usernameVar).grid(row=1,column=3)
         
          self.usernumberVar=StringVar()
          entry2=Entry(frame,textvariable=self.usernumberVar).grid(row=2,column=3)
          
          button=Button(frame,text="StudyEnglish Moddle",command=self.StudyEnglish).grid(row=4,column=3)
          button1=Button(frame,text="HighScore",command=self.highscore).grid(row=3,column=1)
          button2=Button(frame,text="WordsList",command=self.wordslist).grid(row=3,column=3)
          button3=Button(frame,text="Classical Moddle",command=self.Classical).grid(row=4,column=1)
          self.window.mainloop()
      def StudyEnglish(self):
          username.append(self.usernameVar.get())
          usernumber.append(self.usernumberVar.get())
          #self.window.destroy()
          SnakeGameStudyEnglish()
      def highscore(self):
          username.append(self.usernameVar.get())
          usernumber.append(self.usernumberVar.get())
          HighScore()
      def wordslist(self):
          username.append(self.usernameVar.get())
          usernumber.append(self.usernumberVar.get())
          WordsList()
      def Classical(self):
          username.append(self.usernameVar.get())
          usernumber.append(self.usernumberVar.get())
          SnakeGameClassical()
          
UserName()          
      
          
      
          


          

