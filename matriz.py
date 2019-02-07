# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
def cargar_archivo(lab):
	return [[int(x) for x in y] for y in [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]][:]]

def go_up(x,y):
	try:
                if x-1<0:
                        return -4
                else:
                        return int(cargar_archivo("mat.in")[x-1][y])
	except:
		return -4

def go_down(x,y):
	try:
		return int(cargar_archivo("mat.in")[x+1][y])
	except:
		return -3

def go_right(x,y):
	try:
		return int(cargar_archivo("mat.in")[x][y+1])
	except:
		return -1

def go_left(x,y):
	try:
                if y-1 <0:
                        return -2
                else:
                        return int(cargar_archivo("mat.in")[x][y-1])
	except:
		return -2

def hayLimite(limite,pos):
        for i in limite:
                if pos==i:
                        return True
        return False


def cambiarPosicion(pos,sentido):
        if sentido=="derecha":
                pos.insert((pos[1]+1),0)
                pos.remove(1)
                return pos
        elif sentido=="izquierda":
                pos.insert((pos[1]-1),0)
                pos.remove(1)
                return pos
        elif sentido=="abajo":
                pos.insert((pos[0]+1),1)
                pos.remove(1)
                return pos
        elif sentido=="arriba":
                pos.insert((pos[0]-1),1)
                pos.remove(1)
                return pos
        else:
                return "Error"

def resolver(pos,mover,sentido,limite):
        if mover>=0 and hayLimite(limite,pos)==False:
                try:
                        limite.append([pos[0],pos[1]])
                        print int(cargar_archivo("mat.in")[pos[0]][pos[1]])
                        if sentido=="derecha":
                                pos[0]+=1
                                resolver(pos,go_right(pos[0],(pos[1]+1)),"derecha",limite)
                        elif sentido=="izquierda":
                                resolver(pos,go_left(pos[0],(pos[1]-1)),"izquierda",limite)
                        elif sentido=="arriba":
                                resolver(pos,go_up((pos[0]-1),pos[1]),"arriba",limite)
                        elif sentido=="abajo":
                                resolver(pos,go_down((pos[0]+1),pos[1]),"abajo",limite)
                        else:
                                print "Error"
                except:
                        print "FIN"
        elif mover==-1 or sentido=="derecha":
                limite.append([pos[0],pos[1]])
                print int(cargar_archivo("mat.in")[pos[0]][pos[1]])
                print "cambio de sentido hacia abajo"
                print pos
                resolver(pos,go_down((pos[0]+1),pos[1]),"abajo",limite)
        elif mover==-2 or sentido=="izquierda":
                limite.append([pos[0],pos[1]])
                print int(cargar_archivo("mat.in")[pos[0]][pos[1]])
                print "cambio de sentido hacia arriba"
                resolver(pos,go_up((pos[0]-1),pos[1]),"arriba",limite)
        elif mover==-3 or sentido=="abajo":
                limite.append([pos[0],pos[1]])
                print int(cargar_archivo("mat.in")[pos[0]][pos[1]])
                print "cambio de sentido hacia izquierda"
                resolver(pos,go_left(pos[0],(pos[1]-1)),"izquierda",limite)
        elif mover==-4 or sentido=="derecha":
                limite.append([pos[0],pos[1]])
                print int(cargar_archivo("mat.in")[pos[0]][pos[1]])
                print "cambio de sentido hacia derecha"
                resolver(pos,go_right(pos[0],(pos[1]+1)),"derecha",limite)
        else:
                try:
                        print "ERROR HORRIBLE"
                except:
                       print "FIN AUN PEOR"

print cambiarPosicion([3,4],"arriba")
#print go_left(1,0)
#resolver([0,0],go_right(0,0),"derecha",[])