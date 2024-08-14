from manim import *

class DrawPolygon(SpecialThreeDScene):
    def construct(self):


        def Polygon3D(listOfPoints, z, aes_color = RED,opacity = 0.5):
            H1 =   listOfPoints

            H2 =   []
            for i in range(len(H1)):
                H2.append([H1[i][0],H1[i][1],(H1[i][2]+z)])

            S=[]

            for i in range(len(H2)-1):
                s1= [(H2[i][0],H2[i][1],H2[i][2]),
                    (H2[i+1][0],H2[i+1][1],H2[i+1][2]),
                    (H2[i+1][0],H2[i+1][1],H1[i+1][2]),
                    (H2[i][0],H2[i][1],H1[i][2])]
                S.append(Polygon(*s1,fill_color=aes_color, fill_opacity=opacity, color=aes_color,stoke_width=0.1))


            b = Polygon(*H1,fill_color=aes_color, fill_opacity=opacity, color=aes_color,stoke_width=0.1)
            h = Polygon(*H2,fill_color=aes_color, fill_opacity=opacity, color=aes_color,stoke_width=0.1)
            s = VGroup(*S)
            poly3D = VGroup(*[b,h,s])
            return poly3D


        Hexagon =   [(0,0,0),   #P1
                    (1,1,0),    #P2
                    (2,1,0),    #P3
                    (3,0,0),    #P4
                    (2,-1,0),   #P5
                    (1,-1,0)    #P6
                    ]

        poly = Polygon3D(Hexagon)
        self.play(ShowCreation(poly))