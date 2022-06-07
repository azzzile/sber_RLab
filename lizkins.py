import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(cells):
    a=[]
    pos={}
    for j in range(int(cells[len(cells)-1][5])):
        for i in range(int(cells[len(cells)-1][6])*2):
            a.append(cells[i+j*int(cells[len(cells)-1][6])*2][0])
            r=cells[i+j*int(cells[len(cells)-1][6])*2][0]
            if i%2==0:
                if i==0:
                    pos[r]=[(int(cells[i+j*int(cells[len(cells)-1][6])*2][5])-1)*2, int(cells[i+j*int(cells[len(cells)-1][6])*2][6])-1]
                    n=int(cells[i+j*int(cells[len(cells)-1][6])*2][6])-1
                else:
                    pos[cells[i+j*int(cells[len(cells)-1][6])*2][0]]=[(int(cells[i+j*int(cells[len(cells)-1][6])*2][5])-1)*2,n+6]
                    n+=6
            else:
                if i==1:
                    pos[cells[i+j*int(cells[len(cells)-1][6])*2][0]]=[int(cells[i+j*int(cells[len(cells)-1][6])*2][5])*2-1, int(cells[i+j*int(cells[len(cells)-1][6])*2][6])-1]
                    h=int(cells[i+j*int(cells[len(cells)-1][6])*2][6])-1
                else:
                    pos[cells[i+j*int(cells[len(cells)-1][6])*2][0]]=[int(cells[i+j*int(cells[len(cells)-1][6])*2][5])*2-1,h+6]
                    h+=6
    b=[]
    for j in range(1,int(cells[len(cells)-1][5])+1):
        m='1_CS_'
        m=m+'1'+'_'
        m=m+str(j)
        m=m+'_0'
        a.append(m)
        pos[m]=[(pos[a[(j-1)*int(cells[len(cells)-1][6])*2]][0]+pos[a[(j-1)*int(cells[len(cells)-1][6])*2+1]][0])/2, -4]
        b.append((m,a[(j-1)*int(cells[len(cells)-1][6])*2]))
        b.append((m,a[(j-1)*int(cells[len(cells)-1][6])*2+1]))
        if j!=1:
            b.append((m,a[len(a)-2]))
    for j in range(2,int(cells[len(cells)-1][5])+1, 2):
        m='1_L_'
        m=m+'1'+'_'
        m=m+str(j)
        m=m+'_1'
        a.append(m)
        pos[m]=[(pos[a[(j-1)*int(cells[len(cells)-1][6])*2]][0]+pos[a[(j-1)*int(cells[len(cells)-1][6])*2+1]][0])/2, -10]
        k='1_CS_'
        k=k+'1'+'_'
        k=k+str(j)
        k=k+'_0'
        b.append((m,k))
    for j in range(int(cells[len(cells)-1][5])):
        for i in range(0,int(cells[len(cells)-1][6])*2-2,2):
            b.append((a[i+j*int(cells[len(cells)-1][6])*2], a[i+j*int(cells[len(cells)-1][6])*2+2]))
        for i in range(1,int(cells[len(cells)-1][6])*2-2,2):
            b.append((a[i+j*int(cells[len(cells)-1][6])*2], a[i+j*int(cells[len(cells)-1][6])*2+2]))
    pos_small = {k: v for k, v in pos.items() if k in a}
    G = nx.Graph()
    G.add_nodes_from(a)
    G.add_edges_from(b)
    color_map = []
    for node in G:
        if a[a.index(node)][2]=='A':
            if cells[a.index(node)][2]=='True' :
                color_map.append('limegreen')
            else:
                color_map.append('firebrick')
        elif a[a.index(node)][2]=='C':
            color_map.append('darkorange')
        else:
            color_map.append('lightblue')

    nx.draw(G,pos, node_color=color_map, node_size=300)
    nx.draw_networkx_labels(G.subgraph(a), pos_small, font_size=7)
    plt.draw()
