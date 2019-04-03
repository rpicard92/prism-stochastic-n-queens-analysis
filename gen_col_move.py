

import sys

n=int(sys.argv[1])

with open('gen_files/col_move'+str(n)+'.prism', 'w') as f:
    f.write('dtmc\n\n')

    for i in range(n):
        f.write('global q'+str(i+1)+'x : [1..'+str(n)+'] init '+str(i+1)+';\n')
        f.write('global q'+str(i+1)+'y : [1..'+str(n)+'] init '+str(i+1)+';\n')
    f.write('\n')
    f.write('module q1\n\n')
    for j in range(n):
        f.write('\t [] (under_attack_diag | under_attack_column) & q1x = '+str(j+1)+' -> ')
        #tot=0
        for i in range(n-2):
            #val=1/(n-1)
            #tot=tot+float(str(val)[:6])
            if not i+2==j+1:
                #f.write(str(val)[:6]+': (q1x\' = '+str(i+2)+') + ')
                f.write('1/'+str(n-1)+': (q1x\' = '+str(i+2)+') + ')
            else:
                #f.write(str(val)[:6]+': (q1x\' = 1) + ')
                f.write('1/'+str(n-1)+': (q1x\' = 1) + ')
        if not j==n-1:
            #f.write(str(1-tot)[:6]+': (q1x\' = '+str(n)+');\n')
            f.write('1/'+str(n-1)+': (q1x\' = '+str(n)+');\n')
        else:
            #f.write(str(1-tot)[:6]+': (q1x\' = 1);\n\n')
            f.write('1/'+str(n-1)+': (q1x\' = 1);\n\n')
    f.write('endmodule\n\n')
    f.write('formula under_attack_diag = ')
    for i in range(n-2):
       f.write('((q1x-q'+str(i+2)+'x) = (q1y-q'+str(i+2)+'y) | (q1x-q'+str(i+2)+'x) = -(q1y-q'+str(i+2)+'y)) | ')
    f.write('((q1x-q'+str(n)+'x) = (q1y-q'+str(n)+'y) | (q1x-q'+str(n)+'x) = -(q1y-q'+str(n)+'y));\n')
    
    f.write('formula under_attack_column = ')
    for i in range(n-2):
       f.write('(q1x = q'+str(i+2)+'x)| ')
    f.write('(q1x = q'+str(n)+'x);\n\n')

    for i in range(n-1):
        f.write('module q'+str(i+2)+' = q1 [ q1x=q'+str(i+2)+'x, q'+str(i+2)+'x=q1x, q1y=q'+str(i+2)+'y, q'+str(i+2)+'y=q1y ] endmodule\n')
    
