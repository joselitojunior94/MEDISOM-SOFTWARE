import matplotlib.pyplot as plt
import matplotlib.patches as patches
import ttk
import matplotlib.gridspec as gridspec
import tkMessageBox
import math
import sys
from functools import partial
from Tkinter import *
from tkFileDialog import *
from mpl_toolkits.mplot3d import Axes3D

"""
Desenvolvidor por : Joselito Mota Junior  BCC  UFBA

"""

def out():
        sys.exit(0)
def generate_new():
        axis = float(combobox.get())
        mapa2Dfor3D(X, Y, Z, axis, intes)        
def combobox_handler(event):   
        if((combobox.get()) == 'Todos os discos(3D)'):
                button.config(state='disable')
                mapa3D(X, Y, Z, intes)               
        else:
                button.config(state='normal')
                axis = float(combobox.get())
                mapa2D(X, Y, Z, intes, axis, radius)
def abertura_de_arquivo():
        try:
                fileName = askopenfilename( filetypes = (("*","*.txt"), ("All files","*.*")))
                arq = open(fileName)
                return arq
        except Exception:
                sys.exit(0)          
def mapa2D(X, Y, Z, intes, disco, radius):
        gs = gridspec.GridSpec(2, 2, width_ratios=[1,4], height_ratios=[50,1])   
        fig = plt.figure()
        fig.canvas.mpl_connect('close_event', out)
        ax = plt.subplot(gs[0])
        plt.tight_layout(pad=1.5, w_pad = 1.5, h_pad=-2)
        ax.set_xticks([0, 30, 50])
        ax.set_yticks([-8, 20]) 

        X0 = []
        Y0 = [] 
        
        X1 = [] 
        Y1 = [] 
        
        X2 = [] 
        Y2 = [] 
        
        X3 = [] 
        Y3 = [] 
        
        X4 = [] 
        Y4 = [] 
        
        X5 = [] 
        Y5 = [] 
        
        X6 = [] 
        Y6 = [] 
        
        X7 = [] 
        Y7 = [] 
        
        X8 = [] 
        Y8 = [] 
        
        X9 = [] 
        Y9 = [] 
        
        X10 = [] 
        Y10 = [] 
        
        X11 = [] 
        Y11 = [] 
        
        X12 = [] 
        Y12 = [] 
       
        X13 = [] 
        Y13 = [] 
        
        X14 = [] 
        Y14 = [] 
        
        X15 = [] 
        Y15 = [] 
        
        X16 = [] 
        Y16 = [] 
        
        X17 = [] 
        Y17 = [] 
        
        X18 = [] 
        Y18 = [] 
        
        X19= [] 
        Y19= [] 
        
        i = 0
        while(i<len(Z)):
                if(Z[i] == disco):
                        value = math.ceil((intes[i]-MIN)/DELTA)
                        if(value == 0):
                                X0.append(X[i])
                                Y0.append(Y[i]) 
                        elif(value == 1):
                                X1.append(X[i])
                                Y1.append(Y[i])   
                        elif(value == 2):
                                X2.append(X[i])
                                Y2.append(Y[i])
                        elif(value == 3):
                                X3.append(X[i])
                                Y3.append(Y[i])
                        elif(value == 4):
                                X4.append(X[i])
                                Y4.append(Y[i])
                        elif(value == 5):
                                X5.append(X[i])
                                Y5.append(Y[i])
                        elif(value == 6):
                                X6.append(X[i])
                                Y6.append(Y[i])
                        elif(value == 7):
                                X7.append(X[i])
                                Y7.append(Y[i])
                        elif(value == 8):
                                X8.append(X[i])
                                Y8.append(Y[i]) 
                        elif(value == 9):
                                X9.append(X[i])
                                Y9.append(Y[i])
                        elif(value == 10):
                                X10.append(X[i])
                                Y10.append(Y[i]) 
                        elif(value == 11):
                                X11.append(X[i])
                                Y11.append(Y[i])
                        elif(value == 12):
                                X12.append(X[i])
                                Y12.append(Y[i])
                        elif(value == 13):
                                X13.append(X[i])
                                Y13.append(Y[i]) 
                        elif(value == 14):
                                X14.append(X[i])
                                Y14.append(Y[i])      
                        elif(value == 15):
                                X15.append(X[i])
                                Y15.append(Y[i])
                        elif(value == 16):
                                X16.append(X[i])
                                Y16.append(Y[i])  
                        elif(value == 17):
                                X17.append(X[i])
                                Y17.append(Y[i])
                        elif(value == 18):
                                X18.append(X[i])
                                Y18.append(Y[i]) 
                        elif(value == 19):
                                X19.append(X[i])
                                Y19.append(Y[i])
                i +=1
        colors = ('#1a237e', '#0000FF', '#1565c0', '#0288d1', '#0097a7', '#00acc1', '#00bcd4'
          , '#009688', '#4caf50', '#66bb6a', '#7cb342', '#c0ca33', '#fff176', '#fdd835'
          ,'#fb8c00' , '#ff8f00', '#f57f17', '#e65100', '#d84315', '#b71c1c')
        r = 13.0
        ax.text(12.5, 17 ,'Intensidade', fontsize=10)

        ax.text(r +3.5, (r/2) - 10 ,'0,00 V -|'+str(round((MIN*0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 8.9 ,str(round((MIN*0.00488),2))+'V -|'+str(round(((MIN+(DELTA*2)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 7.9 ,str(round(((MIN+(DELTA*2))) *0.00488,2))+'V -|'+str(round(((MIN+(DELTA*3)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 6.9 ,str(round(((MIN+(DELTA*3)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*4)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 5.9 ,str(round(((MIN+(DELTA*4)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*5)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 4.9 ,str(round(((MIN+(DELTA*5)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*6)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 3.9 ,str(round(((MIN+(DELTA*6)) *0.00488),2))+'V -|'+str(round((MIN+(DELTA*7)) *0.00488,2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 2.9 ,str(round(((MIN+(DELTA*7)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*8)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 1.9 ,str(round(((MIN+(DELTA*8)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*9)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 0.9,str(round(((MIN+(DELTA*9)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*10)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2) ,str(round(((MIN+(DELTA*10)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*11)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+0.9 ,str(round(((MIN+(DELTA*11)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*12)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 1.9 ,str(round(((MIN+(DELTA*12)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*13)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 2.9 ,str(round(((MIN+(DELTA*13)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*14)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 3.9 ,str(round(((MIN+(DELTA*14)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*15)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 4.9 ,str(round(((MIN+(DELTA*15)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*16)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 5.9 ,str(round(((MIN+(DELTA*16)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*17)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 6.9 ,str(round(((MIN+(DELTA*17)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*18)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 7.9 ,str(round(((MIN+(DELTA*18)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*19)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 8.9 ,str(round(((MIN+(DELTA*19)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*20)) *0.00488),2))+'V', fontsize=8)
        
        for p in [
            patches.Rectangle((r, (r/2) - 10), r/4, r/16, color = colors [0], alpha=0.8),
            patches.Rectangle((r, (r/2)- 8.9999), r/4, r/16, color = colors [1], alpha=0.8),
            patches.Rectangle((r, (r/2)-7.99999), r/4, r/16, color = colors [2], alpha=0.8),
            patches.Rectangle((r, (r/2)-6.999999), r/4, r/16, color = colors [3], alpha=0.8),
            patches.Rectangle((r, (r/2)-5.999999), r/4, r/16, color = colors [4], alpha=0.8),
            patches.Rectangle((r, (r/2)-4.999999), r/4, r/16, color = colors [5], alpha=0.8),
            patches.Rectangle((r, (r/2)-3.999999), r/4, r/16, color = colors [6], alpha=0.8),
            patches.Rectangle((r, (r/2)-2.999999), r/4, r/16, color = colors [7], alpha=0.8),
            patches.Rectangle((r, (r/2)-1.999999), r/4, r/16, color = colors [8], alpha=0.8),
            patches.Rectangle((r, (r/2)-0.999999), r/4, r/16, color = colors [9], alpha=0.8),
            patches.Rectangle((r, (r/2)), r/4, r/16, color = colors [10], alpha=0.8),
            patches.Rectangle((r, (r/2)+0.999999), r/4, r/16, color = colors [11], alpha=0.8),
            patches.Rectangle((r, (r/2)+1.999999), r/4, r/16, color = colors [12], alpha=0.8),
            patches.Rectangle((r, (r/2)+2.999999), r/4, r/16, color = colors [13], alpha=0.8),
            patches.Rectangle((r, (r/2)+3.999999), r/4, r/16, color = colors [14], alpha=0.8),
            patches.Rectangle((r, (r/2)+4.999999), r/4, r/16, color = colors [15], alpha=0.8),
            patches.Rectangle((r, (r/2)+5.999999), r/4, r/16, color = colors [16], alpha=0.8),
            patches.Rectangle((r, (r/2)+6.999999), r/4, r/16, color = colors [17], alpha=0.8),
            patches.Rectangle((r, (r/2)+7.999999), r/4, r/16, color = colors [18], alpha=0.8),
            patches.Rectangle((r, (r/2)+8.999999), r/4, r/16,color = colors [19], alpha=0.8),      
        ]:
            ax.add_patch(p)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.draw()
        ax = fig.add_subplot(gs[1])
        circle =  plt.Circle((0,0), radius, fc='none')
        plt.gca().add_patch(circle)
        
        ax.scatter(X0, Y0, c = colors[0], s = 50, alpha=0.8)
        ax.scatter(X1, Y1, c = colors[1], s = 50, alpha=0.8)
        ax.scatter(X2, Y2, c = colors[2], s = 50, alpha=0.8)
        ax.scatter(X3, Y3, c = colors[3], s = 50, alpha=0.8)
        ax.scatter(X4, Y4, c= colors[4], s = 50, alpha=0.8)
        ax.scatter(X5, Y5, c = colors[5], s = 50, alpha=0.8)
        ax.scatter(X6, Y6, c = colors[6], s = 50, alpha=0.8)
        ax.scatter(X7, Y7, c = colors[7], s = 50, alpha=0.8)
        ax.scatter(X8, Y8, c = colors[8], s = 50, alpha=0.8)
        ax.scatter(X9, Y9, c = colors[9], s = 50, alpha=0.8)
        ax.scatter(X10, Y10, c = colors[10], s = 50, alpha=0.8)
        ax.scatter(X11, Y11, c = colors[11], s = 50, alpha=0.8)
        ax.scatter(X12, Y12, c = colors[12], s = 50, alpha=0.8)
        ax.scatter(X13, Y13, c = colors[13], s = 50, alpha=0.8)
        ax.scatter(X14, Y14, c = colors[14], s = 50, alpha=0.8)
        ax.scatter(X15, Y15, c = colors[15], s = 50, alpha=0.8)
        ax.scatter(X16, Y16, c = colors[16], s = 50, alpha=0.8)
        ax.scatter(X17, Y17, c = colors[17], s = 50, alpha=0.8)
        ax.scatter(X18, Y18, c = colors[18], s = 50, alpha=0.8)
        ax.scatter(X19, Y19, c = colors[19], s = 50, alpha=0.8)
        
        title = "DISCO: " + str(disco)
        plt.title(title) 
       
        plt.draw()
        plt.show(block = False)

def mapa3D(X, Y, Z, intes):
        gs = gridspec.GridSpec(2, 2, width_ratios=[1,4], height_ratios=[50,1])
        fig = plt.figure()
        fig.canvas.mpl_connect('close_event', out)
        ax = plt.subplot(gs[0])
        plt.tight_layout(pad=0.5, w_pad=0.5, h_pad=0.5)
        ax.set_xticks([0, 30, 50])
        ax.set_yticks([-8, 20])   

        X0 = [] 
        Y0 = [] 
        Z0 = []

        X1 = [] 
        Y1 = [] 
        Z1 = []

        X2 = [] 
        Y2 = [] 
        Z2 = []

        X3 = [] 
        Y3 = [] 
        Z3 = []

        X4 = [] 
        Y4 = [] 
        Z4 = []

        X5 = [] 
        Y5 = [] 
        Z5 = []

        X6 = [] 
        Y6 = [] 
        Z6 = []

        X7 = [] 
        Y7 = [] 
        Z7 = []

        X8 = [] 
        Y8 = [] 
        Z8 = []

        X9 = [] 
        Y9 = [] 
        Z9 = []

        X10 = [] 
        Y10 = [] 
        Z10 = []

        X11 = [] 
        Y11 = [] 
        Z11 = []

        X12 = [] 
        Y12 = [] 
        Z12 = []

        X13 = [] 
        Y13 = [] 
        Z13 = []

        X14 = []
        Y14 = [] 
        Z14 = []

        X15 = [] 
        Y15 = [] 
        Z15 = []

        X16 = [] 
        Y16 = [] 
        Z16 = []

        X17 = [] 
        Y17 = [] 
        Z17 = []

        X18 = [] 
        Y18 = [] 
        Z18 = []

        X19 = [] 
        Y19 = [] 
        Z19 = []

        i = 0
        while(i<len(intes)):
                value = math.ceil((intes[i]-MIN)/DELTA)
                if(value == 0):
                        X0.append(X[i])
                        Y0.append(Y[i])
                        Z0.append(Z[i]) 
                elif(value == 1):
                        X1.append(X[i])
                        Y1.append(Y[i])
                        Z1.append(Z[i]) 
                elif(value == 2):
                        X2.append(X[i])
                        Y2.append(Y[i])
                        Z2.append(Z[i]) 
                elif(value == 3):
                        X3.append(X[i])
                        Y3.append(Y[i])
                        Z3.append(Z[i]) 
                elif(value == 4):
                        X4.append(X[i])
                        Y4.append(Y[i])
                        Z4.append(Z[i]) 
                elif(value == 5):
                        X5.append(X[i])
                        Y5.append(Y[i])
                        Z5.append(Z[i]) 
                elif(value == 6):
                        X6.append(X[i])
                        Y6.append(Y[i])
                        Z6.append(Z[i]) 
                elif(value == 7):
                        X7.append(X[i])
                        Y7.append(Y[i])
                        Z7.append(Z[i]) 
                elif(value == 8):
                        X8.append(X[i])
                        Y8.append(Y[i])
                        Z8.append(Z[i]) 
                elif(value == 9):
                        X9.append(X[i])
                        Y9.append(Y[i])
                        Z9.append(Z[i]) 
                elif(value == 10):
                        X10.append(X[i])
                        Y10.append(Y[i])
                        Z10.append(Z[i]) 
                elif(value == 11):
                        X11.append(X[i])
                        Y11.append(Y[i])
                        Z11.append(Z[i]) 
                elif(value == 12):
                        X12.append(X[i])
                        Y12.append(Y[i])
                        Z12.append(Z[i]) 
                elif(value == 13):
                        X13.append(X[i])
                        Y13.append(Y[i])
                        Z13.append(Z[i]) 
                elif(value == 14):
                        X14.append(X[i])
                        Y14.append(Y[i])
                        Z14.append(Z[i]) 
                elif(value == 15):
                        X15.append(X[i])
                        Y15.append(Y[i])
                        Z15.append(Z[i]) 
                elif(value == 16):
                        X16.append(X[i])
                        Y16.append(Y[i])
                        Z16.append(Z[i]) 
                elif(value == 17):
                        X17.append(X[i])
                        Y17.append(Y[i])
                        Z17.append(Z[i]) 
                elif(value == 18):
                        X18.append(X[i])
                        Y18.append(Y[i])
                        Z18.append(Z[i]) 
                elif(value == 19):
                        X19.append(X[i])
                        Y19.append(Y[i])
                        Z19.append(Z[i]) 
                
                i +=1
        colors = ('#1a237e', '#0000FF', '#1565c0', '#0288d1', '#0097a7', '#00acc1', '#00bcd4'
          , '#009688', '#4caf50', '#66bb6a', '#7cb342', '#c0ca33', '#fff176', '#fdd835'
          ,'#fb8c00' , '#ff8f00', '#f57f17', '#e65100', '#d84315', '#b71c1c')
        
        r = 13.0
        ax.text(12.5, 17 ,'Intensidade', fontsize=10)

        ax.text(r +3.5, (r/2) - 10 ,'0,00 V -|'+str(round((MIN*0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 8.9 ,str(round((MIN*0.00488),2))+'V -|'+str(round(((MIN+(DELTA*2)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 7.9 ,str(round(((MIN+(DELTA*2))) *0.00488,2))+'V -|'+str(round(((MIN+(DELTA*3)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 6.9 ,str(round(((MIN+(DELTA*3)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*4)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 5.9 ,str(round(((MIN+(DELTA*4)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*5)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 4.9 ,str(round(((MIN+(DELTA*5)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*6)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 3.9 ,str(round(((MIN+(DELTA*6)) *0.00488),2))+'V -|'+str(round((MIN+(DELTA*7)) *0.00488,2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 2.9 ,str(round(((MIN+(DELTA*7)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*8)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 1.9 ,str(round(((MIN+(DELTA*8)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*9)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 0.9,str(round(((MIN+(DELTA*9)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*10)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2) ,str(round(((MIN+(DELTA*10)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*11)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+0.9 ,str(round(((MIN+(DELTA*11)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*12)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 1.9 ,str(round(((MIN+(DELTA*12)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*13)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 2.9 ,str(round(((MIN+(DELTA*13)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*14)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 3.9 ,str(round(((MIN+(DELTA*14)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*15)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 4.9 ,str(round(((MIN+(DELTA*15)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*16)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 5.9 ,str(round(((MIN+(DELTA*16)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*17)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 6.9 ,str(round(((MIN+(DELTA*17)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*18)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 7.9 ,str(round(((MIN+(DELTA*18)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*19)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 8.9 ,str(round(((MIN+(DELTA*19)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*20)) *0.00488),2))+'V', fontsize=8)
        
        for p in [
            patches.Rectangle(
                (r, (r/2) - 10), r/4, r/16,
                color = colors [0],
                alpha=0.8,
                
            ),
            patches.Rectangle(
                (r, (r/2)- 8.9999), r/4, r/16,
                color = colors [1],
                alpha=0.8,
                
            ),
            patches.Rectangle(
                (r, (r/2)-7.99999), r/4, r/16,
                color = colors [2],
                alpha=0.8,
                
                ),
            patches.Rectangle(
                (r, (r/2)-6.999999), r/4, r/16,
                color = colors [3],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)-5.999999), r/4, r/16,
                color = colors [4],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)-4.999999), r/4, r/16,
                color = colors [5],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)-3.999999), r/4, r/16,
                color = colors [6],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)-2.999999), r/4, r/16,
                color = colors [7],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)-1.999999), r/4, r/16,
                color = colors [8],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)-0.999999), r/4, r/16,
                color = colors [9],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)), r/4, r/16,
                color = colors [10],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+0.999999), r/4, r/16,
                color = colors [11],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+1.999999), r/4, r/16,
                color = colors [12],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+2.999999), r/4, r/16,
                color = colors [13],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+3.999999), r/4, r/16,
                color = colors [14],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+4.999999), r/4, r/16,
                color = colors [15],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+5.999999), r/4, r/16,
                color = colors [16],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+6.999999), r/4, r/16,
                color = colors [17],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+7.999999), r/4, r/16,
                color = colors [18],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+8.999999), r/4, r/16,
                color = colors [19],
                alpha=0.8
            ),
            
        ]:
                ax.add_patch(p)
        ax.set_xticks([])
        ax.set_yticks([])
        ax = fig.add_subplot(gs[1], projection='3d')
        ax.scatter(X0, Y0, Z0,c = colors[0], s = 60, alpha=.5)
        ax.scatter(X1, Y1, Z1,c = colors[1], s = 60, alpha=.5)
        ax.scatter(X2, Y2, Z2,c = colors[2], s = 60, alpha=.5)
        ax.scatter(X3, Y3, Z3,c = colors[3], s = 60, alpha=.5)
        ax.scatter(X4, Y4, Z4,c= colors[4], s = 60, alpha=.5)
        ax.scatter(X5, Y5, Z5,c = colors[5], s = 60, alpha=.5)
        ax.scatter(X6, Y6, Z6,c = colors[6], s = 60, alpha=.5)
        ax.scatter(X7, Y7, Z7,c = colors[7], s = 60, alpha=.5)
        ax.scatter(X8, Y8, Z8,c = colors[8], s = 60, alpha=.5)
        ax.scatter(X9, Y9, Z9,c = colors[9], s = 60, alpha=.5)
        ax.scatter(X10, Y10, Z10,c = colors[10], s = 60, alpha=.5)
        ax.scatter(X11, Y11, Z11,c = colors[11], s = 60, alpha=.5)
        ax.scatter(X12, Y12, Z12,c = colors[12], s = 60, alpha=.5)
        ax.scatter(X13, Y13, Z13,c = colors[13], s = 60, alpha=.5)
        ax.scatter(X14, Y14, Z14,c = colors[14], s = 60, alpha=.5)
        ax.scatter(X15, Y15, Z15,c = colors[15], s = 60, alpha=.5)
        ax.scatter(X16, Y16, Z16,c = colors[16], s = 60, alpha=.5)
        ax.scatter(X17, Y17, Z17,c = colors[17], s = 60, alpha=.5)
        ax.scatter(X18, Y18, Z18,c = colors[18], s = 60, alpha=.5)
        ax.scatter(X19, Y19, Z19,c = colors[19], s = 80, alpha=.5)
       
        plt.get_current_fig_manager().window.wm_geometry("+450+200")
        plt.draw()
        plt.show(block = False)

def mapa2Dfor3D(X, Y, D, Z, intes):

        gs = gridspec.GridSpec(2, 2,
                       width_ratios=[1,4],
                       height_ratios=[50,1]
        )
        
        fig = plt.figure()
        ax = plt.subplot(gs[0])
        fig.canvas.mpl_connect('close_event', out)

        plt.tight_layout(pad=0.5, w_pad=0.5, h_pad=0.5)

        ax.set_xticks([0, 30, 50])

        ax.set_yticks([-8, 20])        
        X0 = [] 
        Y0 = [] 
        Z0 = []

        X1 = [] 
        Y1 = [] 
        Z1 = []

        X2 = [] 
        Y2 = [] 
        Z2 = []

        X3 = [] 
        Y3 = [] 
        Z3 = []

        X4 = [] 
        Y4 = [] 
        Z4 = []

        X5 = [] 
        Y5 = [] 
        Z5 = []

        X6 = [] 
        Y6 = [] 
        Z6 = []

        X7 = [] 
        Y7 = [] 
        Z7 = []

        X8 = [] 
        Y8 = [] 
        Z8 = []

        X9 = [] 
        Y9 = [] 
        Z9 = []

        X10 = [] 
        Y10 = [] 
        Z10 = []

        X11 = [] 
        Y11 = [] 
        Z11 = []

        X12 = [] 
        Y12 = [] 
        Z12 = []

        X13 = [] 
        Y13 = [] 
        Z13 = []

        X14 = [] 
        Y14 = [] 
        Z14 = []

        X15 = [] 
        Y15 = [] 
        Z15 = []

        X16 = [] 
        Y16 = [] 
        Z16 = []

        X17 = [] 
        Y17 = [] 
        Z17 = []

        X18 = [] 
        Y18 = [] 
        Z18 = []

        X19 = [] 
        Y19 = [] 
        Z19 = []

        i = 0
        while(i<len(D)):
                if(D[i] == Z):
                        value = math.ceil((intes[i]-MIN)/DELTA)
                        if(value == 0):
                                X0.append(X[i])
                                Y0.append(Y[i])
                                Z0.append(Z) 
                        elif(value == 1):
                                X1.append(X[i])
                                Y1.append(Y[i])
                                Z1.append(Z) 
                        elif(value == 2):
                                X2.append(X[i])
                                Y2.append(Y[i])
                                Z2.append(Z) 
                        elif(value == 3):
                                X3.append(X[i])
                                Y3.append(Y[i])
                                Z3.append(Z) 
                        elif(value == 4):
                                X4.append(X[i])
                                Y4.append(Y[i])
                                Z4.append(Z) 
                        elif(value == 5):
                                X5.append(X[i])
                                Y5.append(Y[i])
                                Z5.append(Z) 
                        elif(value == 6):
                                X6.append(X[i])
                                Y6.append(Y[i])
                                Z6.append(Z) 
                        elif(value == 7):
                                X7.append(X[i])
                                Y7.append(Y[i])
                                Z7.append(Z) 
                        elif(value == 8):
                                X8.append(X[i])
                                Y8.append(Y[i])
                                Z8.append(Z) 
                        elif(value == 9):
                                X9.append(X[i])
                                Y9.append(Y[i])
                                Z9.append(Z) 
                        elif(value == 10):
                                X10.append(X[i])
                                Y10.append(Y[i])
                                Z10.append(Z) 
                        elif(value == 11):
                                X11.append(X[i])
                                Y11.append(Y[i])
                                Z11.append(Z) 
                        elif(value == 12):
                                X12.append(X[i])
                                Y12.append(Y[i])
                                Z12.append(Z) 
                        elif(value == 13):
                                X13.append(X[i])
                                Y13.append(Y[i])
                                Z13.append(Z) 
                        elif(value == 14):
                                X14.append(X[i])
                                Y14.append(Y[i])
                                Z14.append(Z) 
                        elif(value == 15):
                                X15.append(X[i])
                                Y15.append(Y[i])
                                Z15.append(Z) 
                        elif(value == 16):
                                X16.append(X[i])
                                Y16.append(Y[i])
                                Z16.append(Z) 
                        elif(value == 17):
                                X17.append(X[i])
                                Y17.append(Y[i])
                                Z17.append(Z) 
                        elif(value == 18):
                                X18.append(X[i])
                                Y18.append(Y[i])
                                Z18.append(Z) 
                        elif(value == 19):
                                X19.append(X[i])
                                Y19.append(Y[i])
                                Z19.append(Z)            
                i +=1
        colors = ('#1a237e', '#0000FF', '#1565c0', '#0288d1', '#0097a7', '#00acc1', '#00bcd4'
          , '#009688', '#4caf50', '#66bb6a', '#7cb342', '#c0ca33', '#fff176', '#fdd835'
          ,'#fb8c00' , '#ff8f00', '#f57f17', '#e65100', '#d84315', '#b71c1c')

        r = 13.0
        ax.text(12.5, 17 ,'Intensidade', fontsize=10)
        ax.text(r +3.5, (r/2) - 10 ,'0,00 V -|'+str(round((MIN*0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 8.9 ,str(round((MIN*0.00488),2))+'V -|'+str(round(((MIN+(DELTA*2)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 7.9 ,str(round(((MIN+(DELTA*2))) *0.00488,2))+'V -|'+str(round(((MIN+(DELTA*3)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 6.9 ,str(round(((MIN+(DELTA*3)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*4)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 5.9 ,str(round(((MIN+(DELTA*4)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*5)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 4.9 ,str(round(((MIN+(DELTA*5)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*6)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 3.9 ,str(round(((MIN+(DELTA*6)) *0.00488),2))+'V -|'+str(round((MIN+(DELTA*7)) *0.00488,2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 2.9 ,str(round(((MIN+(DELTA*7)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*8)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 1.9 ,str(round(((MIN+(DELTA*8)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*9)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)- 0.9,str(round(((MIN+(DELTA*9)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*10)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2) ,str(round(((MIN+(DELTA*10)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*11)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+0.9 ,str(round(((MIN+(DELTA*11)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*12)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 1.9 ,str(round(((MIN+(DELTA*12)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*13)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 2.9 ,str(round(((MIN+(DELTA*13)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*14)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 3.9 ,str(round(((MIN+(DELTA*14)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*15)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 4.9 ,str(round(((MIN+(DELTA*15)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*16)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 5.9 ,str(round(((MIN+(DELTA*16)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*17)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 6.9 ,str(round(((MIN+(DELTA*17)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*18)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 7.9 ,str(round(((MIN+(DELTA*18)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*19)) *0.00488),2))+'V', fontsize=8)
        ax.text(r +3.5, (r/2)+ 8.9 ,str(round(((MIN+(DELTA*19)) *0.00488),2))+'V -|'+str(round(((MIN+(DELTA*20)) *0.00488),2))+'V', fontsize=8)
        for p in [
            patches.Rectangle(
                (r, (r/2) - 10), r/4, r/16,
                color = colors [0],
                alpha=0.8,
                
            ),
            patches.Rectangle(
                (r, (r/2)- 8.9999), r/4, r/16,
                color = colors [1],
                alpha=0.8,
                
            ),
            patches.Rectangle(
                (r, (r/2)-7.99999), r/4, r/16,
                color = colors [2],
                alpha=0.8,
                
                ),
            patches.Rectangle(
                (r, (r/2)-6.999999), r/4, r/16,
                color = colors [3],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)-5.999999), r/4, r/16,
                color = colors [4],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)-4.999999), r/4, r/16,
                color = colors [5],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)-3.999999), r/4, r/16,
                color = colors [6],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)-2.999999), r/4, r/16,
                color = colors [7],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)-1.999999), r/4, r/16,
                color = colors [8],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)-0.999999), r/4, r/16,
                color = colors [9],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)), r/4, r/16,
                color = colors [10],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+0.999999), r/4, r/16,
                color = colors [11],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+1.999999), r/4, r/16,
                color = colors [12],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+2.999999), r/4, r/16,
                color = colors [13],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+3.999999), r/4, r/16,
                color = colors [14],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+4.999999), r/4, r/16,
                color = colors [15],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+5.999999), r/4, r/16,
                color = colors [16],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+6.999999), r/4, r/16,
                color = colors [17],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+7.999999), r/4, r/16,
                color = colors [18],
                alpha=0.8
            ),
            patches.Rectangle(
                (r, (r/2)+8.999999), r/4, r/16,
                color = colors [19],
                alpha=0.8
            ),
            
        ]:
                ax.add_patch(p)

        ax.set_xticks([])
        ax.set_yticks([])

        plt.draw()

        ax = fig.add_subplot(gs[1], projection='3d')

        ax.scatter(X0, Y0, Z0,c = colors[0], s = 60, alpha=.5)
        ax.scatter(X1, Y1, Z1,c = colors[1], s = 60, alpha=.5)
        ax.scatter(X2, Y2, Z2,c = colors[2], s = 60, alpha=.5)
        ax.scatter(X3, Y3, Z3,c = colors[3], s = 60, alpha=.5)
        ax.scatter(X4, Y4, Z4,c= colors[4], s = 60, alpha=.5)
        ax.scatter(X5, Y5, Z5,c = colors[5], s = 60, alpha=.5)
        ax.scatter(X6, Y6, Z6,c = colors[6], s = 60, alpha=.5)
        ax.scatter(X7, Y7, Z7,c = colors[7], s = 60, alpha=.5)
        ax.scatter(X8, Y8, Z8,c = colors[8], s = 60, alpha=.5)
        ax.scatter(X9, Y9, Z9,c = colors[9], s = 60, alpha=.5)
        ax.scatter(X10, Y10, Z10,c = colors[10], s = 60, alpha=.5)
        ax.scatter(X11, Y11, Z11,c = colors[11], s = 60, alpha=.5)
        ax.scatter(X12, Y12, Z12,c = colors[12], s = 60, alpha=.5)
        ax.scatter(X13, Y13, Z13,c = colors[13], s = 60, alpha=.5)
        ax.scatter(X14, Y14, Z14,c = colors[14], s = 60, alpha=.5)
        ax.scatter(X15, Y15, Z15,c = colors[15], s = 60, alpha=.5)
        ax.scatter(X16, Y16, Z16,c = colors[16], s = 60, alpha=.5)
        ax.scatter(X17, Y17, Z17,c = colors[17], s = 60, alpha=.5)
        ax.scatter(X18, Y18, Z18,c = colors[18], s = 60, alpha=.5)
        ax.scatter(X19, Y19, Z19,c = colors[19], s = 80, alpha=.5)
        
        title = "DISCO: " + str(Z)
        plt.title(title)
     
        plt.draw()
        plt.show(block = False)

def dest():
    if tkMessageBox.askokcancel("Sair", "Deseja sair?*"):
        plt.close('all')
        root.destroy()
        sys.exit(0)
        
def maximo_lista(lista):
      i = 0
      r = 0
      while(i< len(lista)):
              r = max(r, lista[i])
              i+=1
      return r

def minimo_lista(lista):
      i = 0
      r = lista[0]
      while(i< len(lista)):
              r = min(r, lista[i])
              i+=1
      return r
    
root = Tk()
root.withdraw()
vfile = abertura_de_arquivo()

line = vfile.readline()

radius = float(line)/2

X = [] 
Y = [] 
Z = [] 
intes = [] 

line = vfile.readline()

while (line):

    a = line.split(',')  
    X.append(float(a[0]))
    Y.append(float(a[1]))
    Z.append(float(a[2]))
    intes.append(float(a[3]))
    line = vfile.readline()
 
vfile.close()

MAXIMO = maximo_lista(intes)

MIN = minimo_lista(intes)

DELTA = math.ceil((MAXIMO - MIN) / 19)

axis = 0
root = Tk()
root.geometry("350x70+600+80")
root.resizable(0,0)
root.title("Medisom/Medic Software Viewer Beta")
mlabel = Label(root, text = 'Selecione o disco para exibir:').pack()
text = StringVar()
combobox = ttk.Combobox(root, textvariable = text)
i = 0
current = Z[i]
Zs = []
text = 'Todos os discos(3D)'
Zs.append(text)
Zs.append(current)

i+=1
while(i<len(Z)):
        if(Z[i] != current):
                current = Z[i]
                Zs.append(current)
                
        i+=1       
        
combobox.config(values = tuple(Zs))
combobox.bind('<<ComboboxSelected>>', combobox_handler)
combobox.pack()
menubar = Menu(root)
root.config(menu=menubar)
fileMenu = Menu(menubar)
fileMenu.add_command(label="Desenvolvido por: Joselito Junior - Aluno BCC UFBA")
menubar.add_cascade(label="About", menu=fileMenu)
button = Button(root, text = 'Gerar 3D',command = generate_new)
button.config(state='disable')
button.pack()
root.protocol("WM_DELETE_WINDOW", dest)
root.mainloop()
