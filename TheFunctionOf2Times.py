from manim import *

class Main(Scene):
    def construct(self):
        # LaTex中文支持
        config.tex_template = TexTemplate()
        config.tex_template.add_to_preamble(r"\usepackage{ctex}")
    
        # 创建坐标轴
        axes = Axes(
            x_range = [-6, 6],  # x 轴范围
            y_range = [-6, 6],  # y 轴范围
            x_length = 6,
            y_length = 6
        ).scale(0.95).to_edge(LEFT)

        # 定义常量
        a = 0.5
        b = -1.5
        c = -2

        # 定义抛物线、判别式、求根公式
        def parabola(x):
            return a*x**2 + b*x + c  # 你可以根据需要调整函数
        
        def delta(a=a,b=b,c=c):
            return b**2 - 4*a*c
        
        def solves(a=a,b=b,c=c):
            S = (b**2-4*a*c)**0.5
            x1 = (-b + S) / (2*a)
            x2 = (-b - S) / (2*a)
            return x1, x2
        
        def vertexs(a=a,b=b,c=c):
            x = -b/(2*a)
            y = (4*a*c-b**2)/(4*a)
            return x,y

        # 绘制抛物线
        graph = axes.plot(parabola, x_range=[-3,6], color=BLUE)

        # 添加标签
        x_label = axes.get_x_axis_label('x')
        y_label = axes.get_y_axis_label('y')

        # 添加顶点
        vertex = axes.c2p(vertexs()[0], vertexs()[1])
        dot1 = Dot(vertex, color=RED)

        # 添加与x轴交点
        if delta() >= 0:
            solve1 = axes.c2p(solves()[0],0)
            solve2 = axes.c2p(solves()[1],0)
            dot2 = Dot(solve1, color=GREEN)
            dot3 = Dot(solve2, color=GREEN)

        # 添加与y轴交点
        intercept = axes.c2p(0,c)
        dot4 = Dot(intercept, color=YELLOW)

        # 添加对称轴
        symmetry1 = axes.get_vertical_line(axes.c2p(vertexs()[0], 6), color=YELLOW)
        symmetry2 = axes.get_vertical_line(axes.c2p(vertexs()[0], -6), color=YELLOW)

        # 添加文字、标志
        t1 = MathTex(r'l').next_to(symmetry1,direction=UR,buff=0.1).shift(0.5*DOWN).scale(0.75)
        t1_1 = Text('对称轴').next_to(t1,direction=RIGHT,buff=-0.25).scale(0.5)
        t2 = MathTex(r'P_{1}').next_to(dot1,direction=UR,buff=0).scale(0.65)
        t2_1 = Text('顶点').next_to(t2,direction=RIGHT,buff=-0.25).scale(0.5)
        t3 = MathTex(r'P_{2}').next_to(dot4,direction=UR,buff=0).scale(0.65)
        t3_1 = Text('截距').next_to(t3,direction=LEFT,buff=-0.25).scale(0.5)
        t4 = MathTex(r'x_{1}').next_to(dot2,direction=UR,buff=0).scale(0.75)
        t5 = MathTex(r'x_{2}').next_to(dot3,direction=UR,buff=0).scale(0.75)
        t4_t5_1 = Text('根').next_to(symmetry1,direction=DOWN,buff=-0.8).scale(0.5)

        l1 = Arrow(start=axes.c2p(vertexs()[0]-0.25,0.75), end=solve1)
        l2 = Arrow(start=axes.c2p(vertexs()[0]+0.25,0.75), end=solve2)
        l3 = Line(start=axes.c2p(vertexs()[0]+0.5,2.5), end=solve1+1.75*UP+0.5*LEFT)
        l4 = Line(start=axes.c2p(vertexs()[0]-0.5,2.5), end=solve2+1.75*UP-0.5*LEFT)
        t6 = Text('开口').next_to(symmetry1,direction=UP,buff=-1.5).scale(0.5)

        # 添加标题
        t7 = Text('什么是二次函数').to_corner(UR).shift(1*DOWN+1*LEFT).scale(1.25)
        r1 = Rectangle(height=0.36,width=0.1,color=RED,fill_opacity = 1).next_to(t7,direction=DR,buff=0).shift(0.25*DOWN+0.25*LEFT)
        t8 = Text('ShiHao Alpha.002').next_to(r1,direction=LEFT,buff=-1.25).scale(0.5)

        # # 添加到场景
        # # 坐标轴
        # self.add(axes)
        # # 函数图像
        # self.add(graph)
        # # 轴标签
        # self.add(x_label, y_label)
        # # 顶点
        # self.add(dot1)
        # # 根
        # if delta() >= 0:
        #     self.add(dot2,dot3)
        # # 截距
        # self.add(dot4)
        # # 对称轴
        # self.add(symmetry1, symmetry2)
        # # 文字说明
        # self.add(t1,t2,t3,t4,t5)
        # self.add(t1_1,t2_1,t3_1,t4_t5_1)
        # # 箭头
        # self.add(l1,l2,l3,l4,t6)
        # # 标题
        # self.add(t7,r1,t8)

        # 函数图像
        self.play(Create(axes),
                  Write(x_label))
        self.play(Write(y_label))
        self.play(Write(graph))
        
        # self.play(Create(dot1),
        #           Write(t2),
        #           Write(t2_1))
        # self.play(Create(dot4),
        #           Write(t3),
        #           Write(t3_1))
        # self.play(Create(dot2),
        #           Create(dot3),
        #           Write(t4),
        #           Write(t5),
        #           Create(l1),
        #           Create(l2),
        #           Write(t4_t5_1))

        # # 对称轴
        # self.play(Create(symmetry1),
        #           Create(symmetry2),
        #           Write(t1),
        #           Write(t1_1))
        # # 顶点
        # self.play(Create(dot1),
        #           Write(t2),
        #           Write(t2_1))
        # # 截距
        # self.play(Create(dot4),
        #           Write(t3),
        #           Write(t3_1))
        # # 根
        # self.play(Create(dot2),
        #           Create(dot3),
        #           Write(t4),
        #           Write(t5),
        #           Create(l1),
        #           Create(l2),
        #           Write(t4_t5_1))

        self.play(Create(symmetry1),
                  Create(symmetry2),
                  Write(t1),
                  Write(t1_1),
                  Create(dot1),
                  Write(t2),
                  Write(t2_1),
                  Create(dot4),
                  Write(t3),
                  Write(t3_1),
                  Create(dot2),
                  Create(dot3),
                  Write(t4),
                  Write(t5),
                  Create(l1),
                  Create(l2),
                  Write(t4_t5_1))

        # 标题
        self.play(Write(t7))
        self.play(Create(r1))
        self.play(FadeIn(t8))
        self.wait(2.5)

        trackX = ValueTracker()
        trackY = ValueTracker()

        t9 = Text('什么是函数？').to_corner(UR).shift(1*DOWN+1*LEFT).scale(1.25)
        t10 = Text('二元（一次）方程').to_corner(UR).shift(1*DOWN+1*LEFT).scale(1.25)
        t10_1 = Text('二元（一次）函数').to_corner(UR).shift(1*DOWN+1*LEFT).scale(1.25)
        t11 = MathTex('y=2x').next_to(t10, direction=DOWN, buff=1).shift(0.3*LEFT).scale(1.25)
        
        p1 = always_redraw(lambda: Dot(axes.c2p(trackX.get_value(), trackY.get_value()),color=RED))
        t12 = always_redraw(lambda: MathTex(fr'x={round(trackX.get_value(),1)}').next_to(t11, direction=DOWN, buff=1))
        t12_1 = always_redraw(lambda: MathTex(fr'x={round(trackY.get_value(),1)}\div 2={round(trackX.get_value(),1)}').next_to(t11, direction=DOWN, buff=1))
        t13 = always_redraw(lambda: MathTex(fr'y={round(trackY.get_value(),1)}').next_to(t12, direction=DOWN, buff=0.5))
        t13_1 = always_redraw(lambda: MathTex(fr'y={round(trackX.get_value(),1)}\times 2={round(trackY.get_value(),1)}').next_to(t12, direction=DOWN, buff=0.5))
        t14 = always_redraw(lambda: MathTex(fr'({round(trackX.get_value(),1)},{round(trackY.get_value(),1)})').next_to(p1, direction=UR, buff=0).scale(0.65))
        t12_t13 = always_redraw(lambda: MathTex(fr'({round(trackX.get_value(),1)},{round(trackY.get_value(),1)})').next_to(t13, direction=DOWN, buff=0.5))

        g1 = axes.plot(lambda x:x*2, x_range=[-6,6], color=BLUE)
        r2 = Rectangle(width=1.89, height=0.64)

        # self.play(FadeOut(symmetry1, symmetry2, t1, t1_1, dot1, t2, t2_1, dot4, t3, t3_1, dot2, dot3, t4, t5, l1, l2, t4_t5_1))
        self.play(FadeOut(t4_t5_1, l2, l1, t5, t4, dot3, dot2, t3_1, t3, dot4, t2_1, t2, dot1, t1_1, t1, symmetry2, symmetry1, graph))
        self.play(FadeOut(t8), Uncreate(r1))
        self.play(ReplacementTransform(t7, t9))
        self.wait(2.5)
        self.play(ReplacementTransform(t9, t10))
        self.play(Write(t11))
        self.play(Write(t12), Write(t13_1))
        self.wait(1)
        # 演示改变x
        self.play(Create(r2.next_to(t12, buff=-1.7)))
        self.play(trackX.animate.set_value(2), trackY.animate.set_value(4))
        self.wait(1)
        self.play(trackX.animate.set_value(2.5), trackY.animate.set_value(5))
        self.wait(0.5)
        self.play(trackX.animate.set_value(4), trackY.animate.set_value(8))
        
        # 演示改变y
        self.play(ReplacementTransform(t12, t12_1), 
                  ReplacementTransform(t13_1, t13), 
                  r2.animate.next_to(t13, buff=-1.7))
        self.play(trackX.animate.set_value(1.5), trackY.animate.set_value(3))
        self.wait(1)
        self.play(trackX.animate.set_value(1), trackY.animate.set_value(2))
        self.wait(0.5)
        self.play(trackX.animate.set_value(2), trackY.animate.set_value(4))

        self.play(ReplacementTransform(t10, t10_1))

        self.wait(2.5)
        self.play(trackX.animate.set_value(0), trackY.animate.set_value(0))
        self.play(ReplacementTransform(t12_1, t12), FadeOut(r2))
        self.play(Write(t12_t13))
        self.wait(1)
        self.play(Create(p1), Write(t14))
        self.play(trackX.animate.set_value(1.5), trackY.animate.set_value(3))
        self.play(trackX.animate.set_value(-2), trackY.animate.set_value(-4))
        self.play(FadeIn(g1), Unwrite(t14), Uncreate(p1), Unwrite(t12_t13))
        self.wait(2.5)

        trackA = ValueTracker(0)
        trackB = ValueTracker(0)
        trackC = ValueTracker(0)

        t15 = Text('（二元）二次函数').to_corner(UR).shift(1*DOWN+1*LEFT).scale(1.25)
        t16 =  MathTex('y=ax^2+bx^2+c').next_to(t10_1, direction=DOWN, buff=1).shift(0.3*LEFT).scale(1.25)
        t17 = always_redraw(lambda: MathTex(fr'a={round(trackA.get_value(),1)}').next_to(t11, direction=DOWN, buff=1).shift(1.5*LEFT))
        t18 = always_redraw(lambda: MathTex(fr'b={round(trackB.get_value(),1)}').next_to(t17, direction=DOWN, buff=0.5))
        t19 = always_redraw(lambda: MathTex(fr'c={round(trackC.get_value(),1)}').next_to(t18, direction=DOWN, buff=0.5))

        group1 = VGroup(t12, t13)
        group2 = VGroup(t17, t18, t19)
        
        self.play(FadeOut(g1))
        self.play(ReplacementTransform(t10_1, t15))
        self.play(ReplacementTransform(t11, t16))
        self.play(ReplacementTransform(group1,group2))

        a1 = Arrow(start=t17.get_right(), end=t17.get_right()+1.5*RIGHT)
        a2 = Arrow(start=t18.get_right(), end=t18.get_right()+1.5*RIGHT+0.5*DOWN)
        a3 = Arrow(start=t19.get_right(), end=t19.get_right()+1.5*RIGHT-0.5*DOWN)
        a4 = Arrow(start=t19.get_right(), end=t19.get_right()+1.5*RIGHT)

        t20 = Text('开口').next_to(a1).scale(0.75)
        t21 = Text('顶点').next_to(a2).scale(0.75)
        t22 = Text('截距').next_to(a4).scale(0.75)

        g2 = always_redraw(lambda: axes.plot(lambda x:trackA.get_value()*x**2+trackB.get_value()*x+trackC.get_value(), x_range=[-6,6], color=BLUE))

        p2 = always_redraw(lambda: Dot(axes.c2p(-trackB.get_value()/(2*trackA.get_value()+0.01), (4*trackA.get_value()*trackC.get_value()-trackB.get_value()**2) / (4*trackA.get_value()+0.01)), color=RED))
        p3 = always_redraw(lambda: Dot(axes.c2p(0,trackC.get_value()), color=YELLOW))
        
        t23_1 = always_redraw(lambda: MathTex(r'P_{1}').next_to(p2,direction=UR,buff=0).scale(0.65))
        t24_1 = always_redraw(lambda: MathTex(r'P_{2}').next_to(p3,direction=UR,buff=0).scale(0.65))

        t23 = always_redraw(lambda: Text('顶点').next_to(t23_1,direction=RIGHT,buff=-0.25).scale(0.5))
        t24 = always_redraw(lambda: Text('截距').next_to(t24_1,direction=RIGHT,buff=-0.25).scale(0.5))

        t25 = always_redraw(lambda: Text('开口').next_to(p2, direction=UP, buff=(-1)**(trackA.get_value()>0)*(-0.75)).scale(0.5))
        a5 = always_redraw(lambda: Arrow(start=p2.get_center()+0.33*LEFT+(-1)**(trackA.get_value()<0)*0.25*UP,
                                         end=p2.get_center()+1.2*LEFT+(-1)**(trackA.get_value()<0)*1.75*UP).scale(0.8))
        a6 = always_redraw(lambda: Arrow(start=p2.get_center()-0.33*LEFT+(-1)**(trackA.get_value()<0)*0.25*UP,
                                         end=p2.get_center()-1.2*LEFT+(-1)**(trackA.get_value()<0)*1.75*UP).scale(0.8))

        # 开口
        self.play(Create(g2))
        self.play(Create(a1), Write(t20))
        self.play(Create(a5), Create(a6), Write(t25))
        self.play(trackA.animate.set_value(2))
        self.play(trackA.animate.set_value(0))
        self.play(trackA.animate.set_value(-1))
        self.play(trackA.animate.set_value(0.5))
        self.play(Uncreate(a5), Uncreate(a6), Unwrite(t25))
        self.wait(1)

        # 顶点
        self.play(Create(a2), 
                  Create(a3), Write(t21))
        self.play(Create(p2), Write(t23), Write(t23_1))
        self.play(trackB.animate.set_value(2), trackC.animate.set_value(1))
        self.play(trackB.animate.set_value(-2), trackC.animate.set_value(1))
        self.play(trackB.animate.set_value(-1), trackC.animate.set_value(-2))
        self.play(trackB.animate.set_value(1), trackC.animate.set_value(-2))
        self.play(trackB.animate.set_value(-1.5))
        self.play(Uncreate(p2), Unwrite(t23), Unwrite(t23_1))
        self.wait(1)

        # 截距
        self.play(Create(a4), Write(t22))
        self.play(Create(p3), Write(t24), Write(t24_1))
        self.play(trackC.animate.set_value(3))
        self.play(trackC.animate.set_value(-1))
        self.play(trackC.animate.set_value(-2))
        self.play(Uncreate(p3), Unwrite(t24), Unwrite(t24_1))

        self.wait(1)
        self.play(FadeOut(t15, t16, group2, a1, a2, a3, a4, t20, t21, t22))

        null = Dot()

        # 截距（Y轴上）
        t26 = Text('截距（Y轴上）').next_to(axes,direction=RIGHT).to_edge(DOWN).shift(2.5*DOWN).scale(0.75)
        l5 = always_redraw(lambda: Line(start=t26.get_left()+0.5*DOWN,end=t26.get_left()+0.5*DOWN+7.5*RIGHT))
        self.add(t26, l5)
        self.play(t26.animate.to_edge(UP))

        t26_0 = MathTex(r'\text{截距}\, P_{2}(0,y)').next_to(l5,direction=DOWN).scale(0.75)
        t26_1 = MathTex(r'y=ax^2+bx+c').next_to(t26_0,direction=DOWN,buff=0).scale(0.75)
        t26_2 = MathTex(r'y=a0^2+b0+c').next_to(t26_1,direction=DOWN,buff=0).scale(0.75)
        t26_3 = MathTex(r'y=0+c').next_to(t26_2,direction=DOWN,buff=0).scale(0.75)
        t26_4 = MathTex(r'y=c').next_to(t26_3,direction=DOWN,buff=0).scale(0.75)
        t26_5 = MathTex(r'\text{截距}\, P_{2}(0,c)').next_to(l5,direction=DOWN).scale(0.75)

        self.play(Create(p3), Write(t24), Write(t24_1))

        self.wait(2.5)
        self.play(Transform(null,t26_0))
        self.wait(2.5)
        self.play(Transform(t26_0,t26_1))
        self.play(Transform(t26_1,t26_2))
        self.play(Transform(t26_2,t26_3))
        self.play(Transform(t26_3,t26_4))
        self.wait(2)
        self.play(ReplacementTransform(null,t26_5))
        self.wait(1)
        self.play(FadeOut(null,t26_0,t26_1,t26_2,t26_3,t26_4,t26_5))     

        self.play(Uncreate(p3), Unwrite(t24), Unwrite(t24_1))

        self.wait(1)
        self.play(t26.animate.shift(2.5*UP))
        self.remove(t26, l5)

        # 开口
        t27 = Text('开口').next_to(axes,direction=RIGHT).to_edge(DOWN).shift(2.5*DOWN).scale(0.75)
        l6 = always_redraw(lambda: Line(start=t27.get_left()+0.5*DOWN,end=t27.get_left()+0.5*DOWN+7.5*RIGHT))

        self.add(t27, l6)
        self.play(t27.animate.to_edge(UP))

        t27_0 = MathTex(r'y=ax^2+bx+c').next_to(l6,direction=DOWN).scale(0.75)
        t27_1 = MathTex(r'y=ax^2').next_to(t27_0,direction=DOWN,buff=0).scale(0.75)
        t27_2 = MathTex(r'(a>0)y=ax^2>0').next_to(t27_1,direction=DOWN,buff=0).scale(0.75)
        t27_3 = MathTex(r'(a=0)y=ax^2=0').next_to(t27_2,direction=DOWN,buff=0).scale(0.75)
        t27_4 = MathTex(r'(a<0)y=ax^2<0').next_to(t27_3,direction=DOWN,buff=0).scale(0.75)

        self.play(Create(a5), Create(a6), Write(t25))

        self.wait(1)
        self.play(Transform(null,t27_0))
        self.wait(2)
        self.play(Transform(t27_0,t27_1))
        self.wait(2)
        self.play(Transform(t27_1,t27_2))
        self.wait(2)
        self.play(Transform(t27_2,t27_3))
        self.wait(2)
        self.play(Transform(t27_3,t27_4))
        self.wait(2)
        self.play(FadeOut(null,t27_0,t27_1,t27_2,t27_3))

        self.play(Uncreate(a5), Uncreate(a6), Unwrite(t25))

        self.wait(1)
        self.play(t27.animate.shift(2.5*UP))
        self.remove(t27, l6)

        # 顶点
        t28 = Text('顶点').next_to(axes,direction=RIGHT).to_edge(DOWN).shift(2.5*DOWN).scale(0.75)
        l7 = always_redraw(lambda: Line(start=t28.get_left()+0.5*DOWN,end=t28.get_left()+0.5*DOWN+7.5*RIGHT))

        self.add(t28, l7)
        self.play(t28.animate.to_edge(UP))

        t28_00 = MathTex(r'\text{顶点}\, P_{1}(k,h)').next_to(l7,direction=DOWN).scale(0.75)
        t28_0 = MathTex(r'\text{顶点式}\, y=a(x-h)^2+k').next_to(t28_00,direction=DOWN,buff=0).scale(0.75)
        t28_1 = MathTex(r'y=a(x^2-2axh+h^2)+k').next_to(t28_0,direction=DOWN,buff=0).scale(0.75)
        t28_2 = MathTex(r'y=ax^2-2ahx+ah^2+k').next_to(t28_1,direction=DOWN,buff=0).scale(0.75)
        t28_3 = MathTex(r'y=ax^2+(-2ah)x+(ah^2+k)').next_to(t28_2,direction=DOWN,buff=0).scale(0.75)
        t28_4 = MathTex(r'\text{原式}\, y=ax^2+bx^2+c').next_to(t28_3,direction=DOWN,buff=0).scale(0.75)
        t28_5 = MathTex(r'b=-2ah').next_to(t28_4,direction=DOWN,buff=0).scale(0.75)
        t28_6 = MathTex(r'c=ah^2+k').next_to(t28_5,direction=DOWN,buff=0).scale(0.75)
        t28_7 = MathTex(r'h=-\frac{b}{2a}').next_to(t28_6,direction=DOWN,buff=0).scale(0.75)
        t28_8 = MathTex(r'k=\frac{4ac-b^2}{4a}').next_to(t28_7,direction=DOWN,buff=0).scale(0.75)
        t28_9 = MathTex(r'\text{顶点}\, P_{1}(\frac{4ac-b^2}{4a},-\frac{b}{2a})').next_to(l7,direction=DOWN,buff=-0.25).scale(0.75)
        
        self.play(Create(p2), Write(t23), Write(t23_1))

        self.wait(2)
        self.play(Transform(null,t28_00))
        self.wait(1)
        self.play(Transform(t28_00,t28_0))
        self.wait(2)
        self.play(Transform(t28_0,t28_1))
        self.wait(2)
        self.play(Transform(t28_1,t28_2))
        self.wait(2)
        self.play(Transform(t28_2,t28_3))
        self.wait(2)
        self.play(Transform(t28_3,t28_4))
        self.wait(2)
        self.play(Transform(t28_4,t28_5))
        self.wait(2)
        self.play(Transform(t28_5,t28_6))
        self.wait(2)
        self.play(Transform(t28_6,t28_7))
        self.wait(2)
        self.play(Transform(t28_7,t28_8))
        self.wait(2)
        self.play(ReplacementTransform(null,t28_9))
        self.wait(2)
        self.play(FadeOut(null,t28_00,t28_0,t28_1,t28_2,t28_3,t28_4,t28_5,t28_6,t28_7,t28_8,t28_9))
        
        self.play(Uncreate(p2), Unwrite(t23), Unwrite(t23_1))

        self.wait(1)
        self.play(t28.animate.shift(2.5*UP))
        self.remove(t28, l7)

        # 根
        t29 = Text('根').next_to(axes,direction=RIGHT).to_edge(DOWN).shift(2.5*DOWN).scale(0.75)
        l8 = always_redraw(lambda: Line(start=t29.get_left()+0.5*DOWN,end=t29.get_left()+0.5*DOWN+7.5*RIGHT))
        self.add(t29, l8)
        self.play(t29.animate.to_edge(UP))

        t29_0 = MathTex(r'\text{根}\, (x,0)').next_to(l8,direction=DOWN).scale(0.75)
        t29_1 = MathTex(r'y=ax^2+bx+c').next_to(t29_0,direction=DOWN,buff=0).scale(0.75)
        t29_2 = MathTex(r'0=ax^2+bx+c').next_to(t29_1,direction=DOWN,buff=0).scale(0.75)
        t29_3 = MathTex(r'-c=ax^2+bx').next_to(t29_2,direction=DOWN,buff=0).scale(0.75)
        t29_4 = MathTex(r'-\frac{c}{a}=x^2+\frac{b}{a}x').next_to(t29_3,direction=DOWN,buff=0).scale(0.75)
        t29_5 = MathTex(r'-\frac{c}{a}+(\frac{b}{2a})^2=x^2+\frac{b}{a}x+(\frac{b}{2a})^2').next_to(t29_4,direction=DOWN,buff=0).scale(0.75)
        t29_6 = MathTex(r'\frac{b^2-4ac}{4a^2}=(x+\frac{b}{2a})^2').next_to(t29_5,direction=DOWN,buff=0).scale(0.75)
        t29_7 = MathTex(r'\pm\sqrt{\frac{b^2-4ac}{4a^2}}=x+\frac{b}{2a}').next_to(t29_6,direction=DOWN,buff=0).scale(0.75)
        t29_8 = MathTex(r'\frac{\pm\sqrt{b^2-4ac}}{2a}-\frac{b}{2a}=x').next_to(t29_6,direction=DOWN,buff=0).scale(0.75)
        t29_9 = MathTex(r'\frac{-b\pm\sqrt{b^2-4ac}}{2a}=x').next_to(t29_6,direction=DOWN,buff=0).scale(0.75)
        t29_10 = MathTex(r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}').next_to(t29_6,direction=DOWN,buff=0).scale(0.75)
        t29_11 = MathTex(r'x_{1},x_{2}=\frac{-b\pm\sqrt{b^2-4ac}}{2a}').next_to(t29_6,direction=DOWN,buff=0).scale(0.75)

        self.play(Create(dot2),
                  Create(dot3),
                  Write(t4),
                  Write(t5),
                  Create(l1),
                  Create(l2),
                  Write(t4_t5_1))

        self.wait(2)
        self.play(Transform(null,t29_0))
        self.wait(2.5)
        self.play(Transform(t29_0,t29_1))
        self.play(Transform(t29_1,t29_2))
        self.play(Transform(t29_2,t29_3))
        self.play(Transform(t29_3,t29_4))
        self.play(Transform(t29_4,t29_5))
        self.play(Transform(t29_5,t29_6))
        self.play(ReplacementTransform(t29_6,t29_7))
        self.play(ReplacementTransform(t29_7,t29_8))
        self.play(ReplacementTransform(t29_8,t29_9))
        self.play(ReplacementTransform(t29_9,t29_10))
        self.play(ReplacementTransform(t29_10,t29_11))
        self.play(FadeOut(null,t29_0,t29_1,t29_2,t29_3,t29_4,t29_5,t29_11))

        self.play(Uncreate(dot2),
                  Uncreate(dot3),
                  Unwrite(t4),
                  Unwrite(t5),
                  Uncreate(l1),
                  Uncreate(l2),
                  Unwrite(t4_t5_1))

        self.wait(1)
        self.play(t29.animate.shift(2.5*UP))
        self.remove(t29, l8)

        # 判别式
        t30 = Text('判别式').next_to(axes,direction=RIGHT).to_edge(DOWN).shift(2.5*DOWN).scale(0.75)
        l9 = always_redraw(lambda: Line(start=t30.get_left()+0.5*DOWN,end=t30.get_left()+0.5*DOWN+7.5*RIGHT))
        self.add(t30, l9)
        self.play(t30.animate.to_edge(UP))

        t30_0 = MathTex(r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}').next_to(l9,direction=DOWN).scale(0.75)
        t30_1 = MathTex(r'\sqrt{b^2-4ac}').next_to(t30_0,direction=DOWN,buff=0).scale(0.75)
        t30_2 = MathTex(r'(b^2-4ac>0)\sqrt{b^2-4ac}=\sqrt{b^2-4ac}').next_to(t30_1,direction=DOWN,buff=0).scale(0.75)
        t30_3 = MathTex(r'(b^2-4ac=0)\sqrt{b^2-4ac}=0').next_to(t30_2,direction=DOWN,buff=0).scale(0.75)
        t30_4 = MathTex(r'(b^2-4ac<0)\sqrt{b^2-4ac}\notin\mathbb{R}').next_to(t30_3,direction=DOWN,buff=0).scale(0.75)
        t30_5 = MathTex(r'\Delta=b^2-4ac').next_to(t30_4,direction=DOWN,buff=0).scale(0.75)
        t30_6 = MathTex(r'(\Delta>0)\exists x_{1},x_{2}\in\mathbb{R}').next_to(t30_5,direction=DOWN,buff=0).scale(0.75)
        t30_7 = MathTex(r'(\Delta=0)\exists x\in\mathbb{R}').next_to(t30_6,direction=DOWN,buff=0).scale(0.75)
        t30_8 = MathTex(r'(\Delta<0)\not\exists x\in\mathbb{R}').next_to(t30_7,direction=DOWN,buff=0).scale(0.75)

        self.wait(1)
        self.play(Transform(null,t30_0))
        self.wait(2.5)
        self.play(Transform(t30_0,t30_1))
        self.wait(1)
        self.play(Transform(t30_1,t30_2))
        self.wait(2.5)
        self.play(Transform(t30_2,t30_3))
        self.wait(2.5)
        self.play(Transform(t30_3,t30_4))
        self.wait(2)
        self.play(Transform(t30_4,t30_5))
        self.wait(2.5)
        self.play(Transform(t30_5,t30_6))
        self.wait(2.5)
        self.play(Transform(t30_6,t30_7))
        self.wait(2.5)
        self.play(Transform(t30_7,t30_8))
        self.wait(2)
        self.play(FadeOut(null,t30_0,t30_1,t30_2,t30_3,t30_4,t30_5,t30_6,t30_7))

        self.wait(1)
        self.play(t30.animate.shift(2.5*UP))
        self.remove(t30, l9)

        # 韦达定理
        t31 = Text('韦达定理').next_to(axes,direction=RIGHT).to_edge(DOWN).shift(2.5*DOWN).scale(0.75)
        l10 = always_redraw(lambda: Line(start=t31.get_left()+0.5*DOWN,end=t31.get_left()+0.5*DOWN+7.5*RIGHT))
        self.add(t31, l10)
        self.play(t31.animate.to_edge(UP))

        t31_1 = MathTex(r'x_{1}=\frac{-b+\sqrt{b^2-4ac}}{2a}').next_to(l10,direction=DOWN).scale(0.75)
        t31_2 = MathTex(r'x_{2}=\frac{-b-\sqrt{b^2-4ac}}{2a}').next_to(t31_1,direction=DOWN,buff=0).scale(0.75)
        t31_3 = MathTex(r'x_{1}+x_{2}=\frac{-b+\sqrt{b^2-4ac}}{2a}+\frac{-b-\sqrt{b^2-4ac}}{2a}').next_to(t31_2,direction=DOWN,buff=0).scale(0.75)
        t31_4 = MathTex(r'x_{1}\cdot x_{2}=\frac{-b+\sqrt{b^2-4ac}}{2a}\cdot \frac{-b-\sqrt{b^2-4ac}}{2a}').next_to(t31_3,direction=DOWN,buff=0).scale(0.75)
        t31_5 = MathTex(r'x_{1}+x_{2}=-\frac{b}{a}').next_to(t31_2,direction=DOWN,buff=0).scale(0.75)
        t31_6 = MathTex(r'x_{1}\cdot x_{2}=-\frac{c}{a}').next_to(t31_3,direction=DOWN,buff=0).scale(0.75)

        null_0 = Dot()

        self.play(Transform(null,t31_1))
        self.play(Transform(t31_1,t31_2))
        self.play(ReplacementTransform(t31_2,t31_3)) #
        self.play(ReplacementTransform(t31_3,t31_5)) #
        self.play(ReplacementTransform(null_0,t31_4))
        self.play(ReplacementTransform(t31_4,t31_6))
        self.play(FadeOut(null,t31_1,t31_2,t31_3,t31_5,t31_6))

        self.wait(1)
        self.play(t31.animate.shift(2.5*UP))
        self.remove(t31, l10)

        # 结尾
        self.play(FadeOut(g2,y_label,axes,x_label))
        # self.play(Unwrite(g2))
        # self.play(Unwrite(y_label))
        # self.play(Uncreate(axes),
        #           Unwrite(x_label))
        banner = ManimBanner().scale(0.5)
        self.play(Create(banner))
        # self.play(banner.create())
