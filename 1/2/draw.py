#coding=utf-8

import numpy as np
from numpy import cross, pi, sin ,cos, sqrt


f = open('rose','w')
head = """
camera { location <1.2,-1.5,1.6>
         look_at <0,0,0>
         right x*image_width/image_height
         up z 
         sky z}

light_source{ <1.2,-1.5,1.6>, 1 } 

"""
f.write(head)

def hue(x):
    """
    ��һ��[0,1]�����ڵ�ֵxӳ��Ϊһ��rgb�ռ����ɫֵ,����������ɶ���.
    """
    return np.array([1,(1-x)/3,x/3])

def DrawMesh(Mesh,color):
    """
    ���з�Ϊ����״�Ĳ���������������ʷ�, ÿ����λ�����ν�һ���öԽ����з�Ϊ����
    С������, �������ַ�ʽ, ���ݶ����ľ�����ѡ������һ��.
    ���㷨�����Ļ�, ���ÿ���������ĸ������ƽ��ֵ��Ϊ���������ĵ�ֵ, Ȼ�����ĸ�
    �����ֵ��ȥ����ֵ��Ϊ du, dv �Ľ���ֵ, ���ڵ�֮����һ����Ϊ�ĸ������Ĵ���    �������Ľ���ֵ, ����ÿ������ķ������ͽ��Ƶ������������������Ĵ��ķ������ĺ�(    ��Ҫ�ٵ�λ��һ��).
    """
    normals = np.zeros(Mesh.shape)
    LeftTop = Mesh[0:-1,0:-1]
    RightTop = Mesh[0:-1,1:]
    LeftBot = Mesh[1:,0:-1]
    RightBot = Mesh[1:,1:]

    cen = (LeftTop + RightTop + LeftBot + RightBot)/4
    E = cross(RightTop-cen, RightBot-cen)
    S = cross(RightBot-cen, LeftBot-cen)
    W = cross(LeftBot-cen, LeftTop-cen)
    N = cross(LeftTop-cen, RightBot-cen)

    normals[0:-1,0:-1] += (E+W)
    normals[0:-1,1:] += (N+E)
    normals[1:,0:-1] += (S+W)
    normals[1:,1:] += (S+E)

    normals /= np.linalg.norm(normals,axis=2,keepdims=True)
    for i in range(Mesh.shape[0]-1):
        for j in range(Mesh.shape[1]-1):
            color_quad( \
                        Mesh[i,j],normals[i,j],hue(color[i,j]),\
                        Mesh[i+1,j],normals[i+1,j],hue(color[i+1,j]),\
                        Mesh[i+1,j+1],normals[i+1,j+1],hue(color[i+1,j+1]),\
                        Mesh[i,j+1],normals[i,j+1],hue(color[i,j+1]) )

def color_triangle(p1,n1,c1, p2,n2,c2, p3,n3,c3):
    nx = p2-p1
    ny = p3-p1
    nz = cross(nx,ny)
    det = np.linalg.det([nx,ny,nz])
    if abs(det) < 1e-5:
        pigment="""pigment {{ rgb <{},{},{}> }}""".format(*c1)
    else:
        pigment="""pigment{{ 
        average pigment_map{{
        [1 gradient x color_map{{[0 rgbt <0,0,0,0.1>][1 rgbt <{},{},{},0.1>]}}]
 
        [1 gradient y color_map{{[0 rgbt <0,0,0,0.1>][1 rgbt <{},{},{},0.1>]}}]

        [1 gradient z color_map{{[0 rgbt <0,0,0,0.1>][1 rgbt <{},{},{},0.1>]}}]}}
        matrix <1.01,0,1, 0,1.01,1, 0,0,1, -0.002,-0.002,-1>
        matrix <{},{},{},{},{},{},{},{},{},{},{},{}>}}\n""".format(*np.concatenate((3*c2,3*c3,3*c1,nx,ny,nz,p1)))
        finish = """finish { phong 0.4
        phong_size 0.2
        specular 0.25
        reflection 0.3}\n"""
    
        f.write("""smooth_triangle{{ <{},{},{}>,<{},{},{}>,<{},{},{}>,<{},{},{}>,<{},{},{}>,<{},{},{}> texture{{ {s} }}}}\n""".format(*np.concatenate((p1,n1,p2,n2,p3,n3)), s=pigment+finish))
    
                
def color_quad(p1,n1,c1, p2,n2,c2, p3,n3,c3, p4,n4,c4):
    if np.linalg.norm(p3-p1) < np.linalg.norm(p4-p2):
        color_triangle(p1,n1,c1, p2,n2,c2, p3,n3,c3)
        color_triangle(p1,n1,c1, p3,n3,c3, p4,n4,c4)
    else:
        color_triangle(p1,n1,c1, p2,n2,c2, p4,n4,c4)
        color_triangle(p2,n2,c2, p3,n3,c3, p4,n4,c4)


theta1 = -20*pi/9
theta2= 15*pi

def rose(x1,theta):
    phi = pi/2*np.exp(-theta/8/pi)
    y1 = 1.95653*x1**2*((1.27687*x1-1)**2*sin(phi))
    X = 1-(1.25*(1-(3.6*theta%(2*pi)/pi))**2-0.25)**2 /2
    r = X*(x1*sin(phi)+y1*cos(phi))
    return r*sin(theta),r*cos(theta),X*(x1*cos(phi)-y1*sin(phi))

x = np.linspace(0,1,24)
y = np.linspace(theta1,theta2,575)
X,Y = np.meshgrid(x,y)
Z = rose(X,Y)
Mesh = np.dstack((Z[0],Z[1],Z[2]))
color = X
DrawMesh(Mesh,color)        
f.close()