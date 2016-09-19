import tools


hs = (168,148,160,109,138,91,0,40,240)
names = ('a','b','c','d','e','f','g','h','s')

edges = {
    'a':(('d',75),),
    'b':(('d',79),('f',68)),
    'c':(('e',61),('f',86)),
    'd':(('a',75),('b',79),('f',93),('g',124)),
    'e':(('c',61),('f',55)),
    'f':(('b',68),('c',86),('d',93),('e',55),('h',111)),
    'g':(('d',124),('h',42)),
    'h':(('f',111),('g',42)),
    's':(('a',105),('b',97),('c',80))
}

states = {}
for i in zip(hs,names):
    states[i[1]] = tools.State(h=i[0], name=i[1])

for i in names:
    state = states[i[0]]
    state.setEdges(edges[i])

print(tools.A(states['s'],states['g'], states))