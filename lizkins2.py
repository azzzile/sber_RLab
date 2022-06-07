import matplotlib.pyplot as plt
import networkx as nx
import random


def draw_graph(cells):
    for i in range(int(cells[len(cells)-1][4])):
        a=[]
        pos={}
        w=[]
        for q in cells:
            print(q)
            if int(q[4])==(i+1):
                a.append(q[0])
                if q[7]=='L':
                    pos[q[0]]=[(int(q[5])-1)*2,int(q[6])-1]
                else:
                    pos[q[0]]=[int(q[5])*2-1,int(q[6])-1]
                w.append(q[2])
        for j in range(1,int(cells[len(cells)-1][5])+1):
            m='1_CS_'
            m=m+str(i+1)+'_'
            m=m+str(j)
            m=m+'_0'
            a.append(m)
            pos[m]=[(pos[a[(j-1)*int(cells[len(cells)-1][6])*2]][0]+pos[a[(j-1)*int(cells[len(cells)-1][6])*2+1]][0])/2, -2]
        l=random.randint(1, int(cells[len(cells)-1][5]))
        h=[]
        b=[]
        while len(h)<l:
            t=random.randint(1, int(cells[len(cells)-1][5]))
            if t not in h:
                h.append(t)
        for j in h:
            m='1_L_'
            m=m+str(i+1)+'_'
            m=m+str(j)
            m=m+'_1'
            a.append(m)
            pos[m]=[(pos[a[(j-1)*int(cells[len(cells)-1][6])*2]][0]+pos[a[(j-1)*int(cells[len(cells)-1][6])*2+1]][0])/2, -4]
            k='1_CS_'
            k=k+str(i+1)+'_'
            k=k+str(j)
            k=k+'_0'
            b.append((m,k))
        for j in range(1,int(cells[len(cells)-1][5])+1):
            for o in range(1,int(cells[len(cells)-1][6])):
                m='1_A_'
                m=m+str(i+1)+'_'+str(j)+'_'+str(o)+'_'
                u=m+'R'
                m=m+'L'
                e='1_A_'
                e=e+str(i+1)+'_'+str(j)+'_'+str(o+1)+'_'
                y=e+'R'
                e=e+'L'
                b.append((m,e))
                b.append((u,y))
            m='1_A_'
            m=m+str(i+1)+'_'+str(j)+'_1_'
            u=m+'R'
            m=m+'L'
            d='1_CS_'
            d=d+str(i+1)+'_'+str(j)+'_'+'0'
            b.append((d,m))
            b.append((d,u))
        m='1_A_'
        m=m+str(i+1)+'_'+cells[len(cells)-1][5]+'_1_'
        u=m+'R'
        m=m+'L'
        d='1_CS_'
        d=d+str(i+1)+'_'+cells[len(cells)-1][5]+'_'+'0'
        b.append((d,m))
        b.append((d,u))
        pos_small = {k: v for k, v in pos.items() if k in a}
        G = nx.Graph()
        G.add_nodes_from(a)
        G.add_edges_from(b)
        color_map = []
        for node in G:
            if a[a.index(node)][2]=='A':
                if w[a.index(node)]=='True' :
                    color_map.append('limegreen')
                else:
                    color_map.append('firebrick')
            elif a[a.index(node)][2]=='C':
                color_map.append('darkorange')
            else:
                color_map.append('lightblue')
        plt.figure(i+1)
        nx.draw(G,pos, node_color=color_map, node_size=300)
        nx.draw_networkx_labels(G.subgraph(a), pos_small, font_size=7)