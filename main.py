import pygame
import math
import random
import sys, os
from datetime import *

class Button():
    def __init__(self, x, y, str):
        self.ps = (int(x), int(y))
        self.str = str
        font4 = pygame.font.SysFont("comicsansms", 40) # 按鈕字體、大小
        #self.off = font4.render(str, True, (170,0,0),(0,0,0)) 
        self.off = font4.render(str, True, (170,0,0)) 
        #self.on = font4.render(str, True, (255,255,255),(255,0,0))  
        self.on = font4.render(str, True, (0,0,0))  
        self.size = (97,56)

    def range(self, x1, y1):
        if x1 >= self.ps[0] and x1 <= self.ps[0]+self.size[0] and y1 >= self.ps[1] and y1 <=self.ps[1]+self.size[1]:
            return True

class Button1():
    def __init__(self, x, y, str):
        self.ps = (int(x), int(y))
        self.ps2 = (int(x)+35, int(y)+5)
        self.str = str
        font4 = pygame.font.SysFont("comicsansms", 25) # 按鈕字體、大小
        #self.off = font4.render(str, True, (170,0,0),(0,0,0)) 
        self.off = font4.render(str, True, (170,0,0)) 
        #self.on = font4.render(str, True, (255,255,255),(255,0,0))  
        self.on = font4.render(str, True, (0,0,0))  
        self.size = (115,70)

    def range(self, x1, y1):
        if x1 >= self.ps[0] and x1 <= self.ps[0]+self.size[0] and y1 >= self.ps[1] and y1 <=self.ps[1]+self.size[1]:
            return True


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    folder_path = os.path.join(base_path, "materials")
    return os.path.join(folder_path, relative_path)


FLOWER_DICT = {
    "康乃馨" :{'previous_price': '62.6','lower_limit': 53, 'upper_limit': 78,'seller': "Chen", "photo" : resource_path("4.png")},
    "小菊" :{'previous_price' : '39.4','lower_limit': 24, 'upper_limit': 49,'seller': "Lin", "photo" : resource_path("1.png")},
    "玫瑰" : {'previous_price': '28.5','lower_limit': 19,'upper_limit': 39, 'seller': "Lee", "photo" : resource_path("2.png")},
    "劍蘭" : {'previous_price': '50.4','lower_limit': 40, 'upper_limit': 60,'seller': "Huang", "photo" : resource_path("5.png")},
    "洋桔梗": {'previous_price': '141.5','lower_limit': 131, 'upper_limit': 162,'seller': "Weng", "photo" :resource_path("3.png")},
    }


win_width = 900     # 可調整, 注意背景圖片要調成一樣的大小
win_height = 600   # As above

pygame.init()

win = pygame.display.set_mode((win_width,win_height)) # 遊戲視窗
pygame.display.set_caption("Flower Auction") # 给視窗取名
clock = pygame.time.Clock() # 遊戲更新速度

print(resource_path("startphoto.png"))
start_bg = pygame.image.load(resource_path("startphoto.png")) #遊戲起始圖片(w*h = win_w*win_h) 存進materials資料夾
start_bg.convert()


truck = pygame.image.load(resource_path("truck.png")) 
truck.convert()
truckmove = pygame.image.load(resource_path("truckmove.png")) 
truckmove.convert()
Button1.imgoff =  truck
Button1.imgon = truckmove


win.blit(start_bg, (0, 0))

#預設值
to_run = True
n1 = True
font = pygame.font.SysFont("comicsansms", 40) # 按鈕字體、大小

while to_run: 
    run = [True]
    n2 = True
    while n1:
        n1_set = False
        clock.tick(30)
        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos()
        win.blit(start_bg,(0,0))
        button1 = Button1(int(win_width/7*1), int(win_height/7*5.5), "PLAY")  # 按鈕位置、文字修改處
        button2 = Button1(int(win_width/7*2.8), int(win_height/7*5.5), "QUIT")# 2.8 --> 比較對齊
        button3 = Button1(int(win_width/7*5), int(win_height/7*5.5), "HELP")

        win.blit(button1.imgoff, button1.ps)
        win.blit(button1.off , button1.ps2)

        win.blit(button2.imgoff, button2.ps)
        win.blit(button2.off , button2.ps2)

        win.blit(button3.imgoff, button3.ps) 
        win.blit(button3.off , button3.ps2)  

        if button1.range(x1,y1):
            win.blit(button1.imgon, button1.ps)
            win.blit(button1.on, button1.ps2)
            if buttons[0]:  #若按下 進入
                n1 = False
        if button2.range(x1,y1):
            win.blit(button2.imgon, button2.ps)
            win.blit(button2.on, button2.ps2)         
            if buttons[0]:  #若按下 退出
                print("exiting...")
                to_run = False
                break
        if button3.range(x1,y1):
            win.blit(button3.imgon, button3.ps)
            win.blit(button3.on, button3.ps2)
            if buttons[0]:                
                print("set")
                n1_set = True
                break
                
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exiting")
                to_run = False
                n1 = False
                n1_set = False
                run = [False]
                n2 = False 
                pygame.quit()

    while n1_set:    #set model    
        clock.tick(30)
        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos() 
        
       
        help_bg = pygame.image.load(resource_path("help.png"))
        help_bg.convert()
        win.blit(help_bg,(0,0))
        button3 = Button(750, 450, "BACK")
        win.blit(button3.off, button3.ps) 
        if button3.range(x1,y1):
            win.blit(button3.on, button3.ps)
            if buttons[0]:  #若按下 進入
                n1_set = False
                run = [False]
                n1 = True
                n2 = False
                
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exiting")
                to_run = False
                n1 = False
                n1_set = False
                run = [False]
                n2 = False   
                pygame.quit()
                
    if to_run == False:
        break


    """""" #遊戲設定

    font2 = pygame.font.SysFont("comicsansms", 20)   # display font for info
    font3 = pygame.font.SysFont("comicsansms", 60)
    chin = pygame.font.Font(resource_path("Noto.otf"),25)
    chin2 =  pygame.font.Font(resource_path("Noto.otf"),40)
    budget = random.randrange(200, 500, 100)
    goal = budget//100 + 1
    goal_f = random.choice(list(FLOWER_DICT.keys())) # random select the goal flower in this round
    number = 0 # 設定拍賣次數
    flower_list = list(FLOWER_DICT.keys())
    random.shuffle(flower_list)
    bought_list = []
    system_bought = []
    system_bid = 0
    bg = pygame.image.load(resource_path("bg.png")) 
    bg.convert()


    cpt = (400,225) # the center point of the clock 
    angle = 0
    radius = 180
    time_circle = []
    cir_list = [[(330,280),(0, 255, 0)],[(400,280),(255, 255, 0)],[(480,280),(255, 0, 0)]] #position, color


    def drawclock():
        for angle in range(0,100):
            vec = pygame.math.Vector2(0, -radius).rotate(angle*3.6)
            pt_x, pt_y = cpt[0] + vec.x, cpt[1] + vec.y
            time_circle.append(( pt_x, pt_y))

        for i in range(0,100):
            pygame.draw.circle(win, (0, 0, 0), time_circle[i], radius*math.pi/100, 2)
        
        pygame.draw.circle(win, (0, 0, 0), (400,280), 30,2)
        pygame.draw.circle(win, (0, 0, 0), (330,280), 30,2)
        pygame.draw.circle(win, (0, 0, 0), (480,280), 30,2)
        text2 = chin.render("每斤", True, (255, 0, 0))
        text3 = chin.render("元", True, (255, 0, 0))
        win.blit(text2, text2.get_rect(center = (320,220)))
        win.blit(text3, text3.get_rect(center = (520,220)))

        text4 = chin.render(f"目標 : {goal_f}", True, (255, 0, 0))
        text7 = chin.render(f"          {goal}種", True, (255, 0, 0))
        text5 = chin.render(f"預算 : {budget}", True, (255, 0, 0))
        if goal_f in bought_list:
            text6 = chin.render("√", True, (0, 255, 0))
        else:
            text6 = chin.render("Ⅹ", True, (255, 0, 0))

        if len(bought_list) >= goal:
            text8 = chin.render("√", True, (0, 255, 0))
        else:
            text8 = chin.render("Ⅹ", True, (255, 0, 0))
        

        win.blit(text4, text4.get_rect(center = (280,450)))
        win.blit(text6, text6.get_rect(center = (430,450)))
        win.blit(text7, text7.get_rect(center = (280,490)))
        win.blit(text8, text8.get_rect(center = (430,490)))
        win.blit(text5, text5.get_rect(center = (280,550)))

        #pygame.display.update()
 
    def show_info(flower):
            img = pygame.image.load(FLOWER_DICT[flower]['photo'])
            img.convert()

            win.blit(img,(600, 30))

            # text part
            # ---------------------------------------------    賣家info
            text4 = chin.render("賣家", True, (0, 0, 0))
            text5 = chin2.render(FLOWER_DICT[flower]['seller'], True, (0,0,0))
            # ---------------------------------------------    次數
            text6 = chin2.render("已買 :", True, (0, 0, 0))
            text14 = chin2.render(str(len(bought_list)), True, (0, 0, 0))
            text7 = chin2.render("未買 :", True, (0, 0, 0))
            text15 = chin2.render(str(len(system_bought)), True, (0, 0, 0))
            text8 = chin2.render("剩餘 :", True, (0, 0, 0))
            text16 = chin2.render(str(5-number), True, (0, 0, 0))
            # ---------------------------------------------    flower info
            text9 = chin.render("品名", True, (0, 0, 0))
            text10 = chin2.render(flower, True, (0, 0, 0))
            text11 = chin.render("上次成交價格", True, (0, 0, 0))
            text12 = chin2.render(FLOWER_DICT[flower]['previous_price'], True, (0, 0, 0))

            # position part
            # ---------------------------------------------    賣家info
            win.blit(text4, text.get_rect(center = (60,50)))
            win.blit(text5, text.get_rect(center = (100,70)))
            pygame.draw.rect(win, (0, 0, 0), pygame.Rect(5, 0, 170, 100), 2)

            # ---------------------------------------------    次數
            win.blit(text6, text.get_rect(center = (60,160)))
            win.blit(text14, text.get_rect(center = (180,160)))
            win.blit(text7, text.get_rect(center = (60,210)))
            win.blit(text15, text.get_rect(center = (180,210)))
            win.blit(text8, text.get_rect(center = (60,260)))
            win.blit(text16, text.get_rect(center = (180,260)))
            pygame.draw.rect(win, (0, 0, 0), pygame.Rect(5, 120, 170, 180), 2)

            # ---------------------------------------------    flower info
            win.blit(text9, text.get_rect(center = (60,370)))
            win.blit(text10, text.get_rect(center = (110,390)))
            win.blit(text11, text.get_rect(center = (60,450)))
            win.blit(text12, text.get_rect(center = (110,480)))
            pygame.draw.rect(win, (0, 0, 0), pygame.Rect(5, 330, 180, 180), 2)

            #pygame.display.update()

    def win_the_bid(flower,ind):
        for i in range(0,3):
            clock.tick(5)
            pygame.draw.circle(win, cir_list[i][1], cir_list[i][0], 30)
            pygame.display.update()


        for i in range(1,6):
            clock.tick(2.5)
            win.blit(bg,(0,0))
            if i%2 ==1:
                drawclock()
                text = font3.render(str(startprice+2-ind), True, (255, 0, 0))
                win.blit(text, text.get_rect(center = (405,180))) 
                show_info(flower)
                pygame.display.update()
            else:
                drawclock()
                show_info(flower)
                pygame.display.update()

    def system_win_the_bid(flower,ind):
        for i in range(0,3):
            clock.tick(5)
            pygame.draw.circle(win, cir_list[i][1], cir_list[i][0], 30)
            pygame.display.update()

        for i in range(1,6):
            clock.tick(2.5)
            win.blit(bg,(0,0))
            if i%2 ==1:
                drawclock()
                text = font3.render(str(startprice+2-ind), True, (255, 0, 0))
                text2 = font.render("U Are Late !", True, (255, 0, 0))
                win.blit(text, text.get_rect(center = (405,180))) 
                win.blit(text2, text.get_rect(center = (350,350))) 
                show_info(flower)
                pygame.display.update()
            else:
                drawclock()
                show_info(flower)
                pygame.display.update()
    
    def set_sys_bid(i):
        return random.randrange(FLOWER_DICT[flower_list[i]]['lower_limit'],FLOWER_DICT[flower_list[i]]['upper_limit'], 1)  # 自訂系統出價範圍


    lower_price = True
    keys = pygame.key.get_pressed()
    ind = 0                             # for running clock display    
    i = 0                               # flower index 
    system_bid = set_sys_bid(0)
    startprice = 99

    # 遊戲開始
    while run[0]:

        win.blit(bg,(0,0))      
        flower = flower_list[i]

        if FLOWER_DICT[flower]['lower_limit'] == 131:
            startprice = 199
        else:
            startprice = 99

        if lower_price :
            drawclock()

            clock.tick(10) # Set FPS 調畫面更新速度
            ind += 1    
            if ind >= startprice:
                ind = 0

            pygame.draw.circle(win, (0, 0, 0), time_circle[99-ind], radius*math.pi/100)
            text = font3.render(str(startprice+2-ind), True, (255, 0, 0))
            pygame.draw.rect(win, (0, 0, 0), pygame.Rect(355, 150, 110, 80), 2)
            win.blit(text, text.get_rect(center = (405,185)))                           #cpt(x,y-25)

            show_info(flower)
            
            if (startprice+2-ind) == system_bid:
                lower_price = False
                drawclock()
                system_win_the_bid(flower,ind)
                system_bought.append(flower)
                ind = 0
                number += 1
                i += 1
                lower_price = True
                if i == 5:
                    break
                system_bid = set_sys_bid(i)

            else:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and ind>5:
                            lower_price = False    
                            drawclock()
                            win_the_bid(flower, ind)
                            FLOWER_DICT[flower]['bid_price'] = (101-ind)
                            budget -= (startprice+2-ind)
                            ind = 0
                            if budget>0:
                                bought_list.append(flower)

                            i += 1
                            number += 1
                            if i ==5:
                                break
                            system_bid = set_sys_bid(i)

                            lower_price = True                       
            pygame.display.update()
            if number == 5 or budget <= 0:
                run[0] = False


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("exiting")
                    to_run = False
                    n1 = False
                    n1_set = False
                    run = [False]
                    n2 = False 
                    break
                    pygame.quit()

 

                            
    """"""  #處理分數


    """"""  #結束畫面
    bg_over = pygame.image.load(resource_path("overphoto.png"))
    bg_over.convert()
    yes = pygame.image.load(resource_path("yes.png"))
    yes.convert()
    bg_score = pygame.image.load(resource_path("score.png"))
    bg_score.convert()

    if len(bought_list) >= goal and goal_f in bought_list:
        end = yes
    else:
        end = bg_over



    n2_score = False

    while n2:        
        clock.tick(30)
        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos()
        if n2_score == False:    
            win.blit(end, (0, 0))
            font3 = pygame.font.SysFont("comicsansms", 40)
            text3 = font3.render("Game Over", True, (0,0,0))  #GameOver文字            
            
            if len(bought_list) >= goal and goal_f in bought_list:
                text4 = font3.render("Mission Completed" , True, (0,0,0))  #score文字
                text5 = chin2.render("我是拍賣小達人！" , True, (0,0,0))
            else:
                text4 = font3.render("Mission Failed" , True, (0,0,0))  #score文字
                text5 = chin2.render("回去再練練吧！" , True, (0,0,0))
                win.blit(text3, (570,220))  
                
            win.blit(text4, (530,310))
            win.blit(text5,(480,100)) 
            
            button1 = Button(int(win_width/7*0.5), int(win_height/7*5.5), "AGAIN")
            button2 = Button(int(win_width/7*2.8), int(win_height/7*5.5), "SCORE")
            button3 = Button(int(win_width/7*5), int(win_height/7*5.5), "QUIT")
            button4 = Button(5, 5, "BACK")
            win.blit(button1.off, button1.ps)
            win.blit(button2.off, button2.ps)
            win.blit(button3.off, button3.ps)
            win.blit(button4.off, button4.ps)
            
            if button1.range(x1,y1):
                win.blit(button1.on, button1.ps)
                if buttons[0]: # 若按下 進入                
                    break
            if button2.range(x1,y1):
                win.blit(button2.on, button2.ps)
                if buttons[0]:                
                    print("score")
                    n2_score = True
                    continue           
            if button3.range(x1,y1):
                win.blit(button3.on, button3.ps)
                if buttons[0]: # 若按下 退出
                    to_run = False
                    break
            if button4.range(x1,y1):
                win.blit(button4.on, button4.ps)
                if buttons[0]: # 若按下 退出
                    n1 = True
                    break                       
            pygame.display.update()

            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        else:   #score     
            win.blit(bg_score,(0,0))
            chin = pygame.font.Font(resource_path("Noto.otf"),30)

            for i in range(len(bought_list)):
                flower = bought_list[i]
                text = chin.render(flower, True, (0,0,0))
                text2 = chin.render(str(FLOWER_DICT[flower]['bid_price']), True, (0,0,0))
                text3 = chin.render(str(FLOWER_DICT[flower]['previous_price']), True, (0,0,0))

                win.blit(text, (200,220 +75*i))   
                win.blit(text2, (430,220 +75*i))                   
                win.blit(text3, (650,220 +75*i))   

                       
            button1 = Button(700, 50, "BACK")       
            win.blit(button1.off, button1.ps)  
            if button1.range(x1,y1):
                win.blit(button1.on, button1.ps)
                if buttons[0]:  #若按下 進入
                    print("BACK")
                    n2_score = False
   
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exiting")
                to_run = False
                n1 = False
                n1_set = False
                run = [False]
                n2 = False   
                pygame.quit()
            
    if to_run == False:
        break
pygame.quit()
