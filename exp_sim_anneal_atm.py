

import sys
n=int(sys.argv[1])

with open('gen_files/exp_sim_anneal_atm'+str(n)+'.prism', 'w') as f:
    f.write('dtmc\n\n')

    f.write('const int N;\n')

    for i in range(n):
        f.write('global q'+str(i+1)+'x : [1..'+str(n)+'] init '+str(i+1)+';\n')
        f.write('const int q'+str(i+1)+'y = '+str(i+1)+';\n')
    #f.write('\n')
    #for i in range(n):
    #    f.write('global p'+str(i+1)+' : [1..'+str(n)+'] init '+str(i+1)+';\n')
    #f.write('\n')
    #for i in range(n):
        #f.write('global a'+str(i+1)+' : [1..'+str(n)+'] init '+str(n)+';\n')
    f.write('\n')
    for i in range(n):
        f.write('global v'+str(i+1)+' : [0..2] init 1;\n')

    f.write('\n')
    f.write('global success_swap_counter : [0..N] init 0;\n')
    f.write('global attempted_swap_counter : [0..N] init 0;\n')
    f.write('global valid : [0..8] init 0;\n')#0 means base, 1 means swap selected
    f.write('global probability : [1..100] init 100;\n')
    f.write('const int probability_max = 100;\n')
    f.write('global cur_atk : [0..'+str(n)+'] init 0;\n')
    f.write('global prev_atk : [0..'+str(n)+'] init '+str(n)+';\n')
    f.write('global prev_atk1 : [0..'+str(n)+'] init '+str(n)+';\n')
    f.write('global stor1 : [1..'+str(n)+'] init 1;\n')
    f.write('global stor2 : [1..'+str(n)+'] init 1;\n')
    
    f.write('module q1\n\n')

    f.write('\t[] (valid=0) & (total_atk > 0) & (attempted_swap_counter<N) -> ')
    #tot=0
    for i in range(n-2):
        #val=1/(n-1)
        #tot=tot+float(str(val)[:6])
        #f.write(str(val)[:6]+': (prev_atk\' = total_atk) & (v1\' = 0) & (valid\' = 1) & (v'+str(i+2)+'\'= 2) & (stor1\'=q1x)  & (stor2\'=q'+str(i+2)+'x) + ')
        f.write('1/'+str(n-1)+': (prev_atk\' = total_atk) & (v1\' = 0) & (valid\' = 1) & (v'+str(i+2)+'\'= 2) & (stor1\'=q1x)  & (stor2\'=q'+str(i+2)+'x) + ')
    #f.write(str(1-tot)[:6]+': (prev_atk\' = total_atk)  & (v1\' = 0) & (valid\' = 1) & (v'+str(n)+'\'= 2)  & (stor1\'=q1x) & (stor2\'=q'+str(n)+'x);\n\n')
    f.write('1/'+str(n-1)+': (prev_atk\' = total_atk)  & (v1\' = 0) & (valid\' = 1) & (v'+str(n)+'\'= 2)  & (stor1\'=q1x) & (stor2\'=q'+str(n)+'x);\n\n')

    f.write('\t[] (valid=1) & (v1=2) -> (attempted_swap_counter\'=attempted_swap_counter+1) & (prev_atk1\'=total_atk) & (valid\'=2);\n')
    f.write('\t[] (valid=2) & (v1=0) -> (q1x\'=stor2)& (valid\'=3);\n')
    f.write('\t[] (valid=3) & (v1=2) -> (q1x\'=stor1) & (valid\'=4);\n')
    f.write('\t[] (valid=4) & (v1=2) -> (cur_atk\'=total_atk) & (valid\'=5);\n')

    f.write('\t[] (valid=5) & ((prev_atk + prev_atk1) >= (total_atk+cur_atk)) & (v1 = 0)-> (v1\'=1) & (valid\'=6);\n')
    f.write('\t[] (valid=5) & ((prev_atk + prev_atk1) < (total_atk+cur_atk)) & (v1 = 0) -> probability/probability_max: (valid\'=6) & (v1\'=1) + (1-probability/probability_max): (valid\'=7);\n')
    f.write('\t[] (valid=6) & (v1=2) -> (valid\'=0) & (v1\'=1) & (success_swap_counter\'=success_swap_counter+1) & (probability\'=max(1, probability-1));\n')
    #f.write('\t[] (valid=7) & (v1=0) -> (valid\'=0) & (v1\'=1);\n')
    f.write('\t[] (valid=7) & (v1=2) -> (valid\'=8) & (q1x\'=stor2) & (v1\'=1);\n')
    f.write('\t[] (valid=8) & (v1=0) -> (valid\'=0) & (q1x\'=stor1) & (v1\'=1);\n')
    
    #f.write('\t[] valid=0 -> ')
    #tot=0
    #for i in range(n-2):
    #    val=1/(n-1)
    #    tot=tot+float(str(val)[:6])
    #    f.write(str(val)[:6]+': (prev_atk\' = total_atk)  & (q1x\' = q'+str(i+2)+'x) & (q'+str(i+2)+'x\' = q1x) & (v1\' = 0) & (valid\' = 0) & (v'+str(i+2)+'\'= 2) & (stor1\'=q1x) + ')
    #f.write(str(1-tot)[:6]+': (prev_atk\' = total_atk)  & (q1x\' = q'+str(n)+'x) & (q'+str(n)+'x\' = q1x) & (v1\' = 0) & (valid\' = 0) & (v'+str(n)+'\'= 2)  & (stor1\'=q1x);\n\n')

    #f.write('\t [] (valid=0) & (prev_attack >= total_atk) & (v1 = 0) & (probability >= 1)-> (probability\'=probability-1) & (valid\'=1) & (prev_atk\' = cur_atk) & (cur_atk\' = total_atk);\n')
    #f.write('\t [] (valid=0) & (prev_attack >= total_atk) & (v1 = 0) & (probability = 1)-> (valid\'=1) & (prev_atk\' = cur_atk) & (cur_atk\' = total_atk);\n')
    #f.write('\t [] (valid=0) & (prev_attack < total_atk) & (v1 = 0) & (probability >= 1)-> (probability\'=probability-1) & (valid\'=1) & (prev_atk\' = cur_atk) & (cur_atk\' = total_atk);\n')
    #f.write('\t [] (valid=0) & (prev_attack < total_atk) & (v1 = 0) & (probability = 1)-> (valid\'=1) & (prev_atk\' = cur_atk) & (cur_atk\' = total_atk);\n')

    
    
    
    f.write('endmodule\n\n')
    
    f.write('formula total_atk = ')
    for i in range(n-2):
       f.write('(((q1x-q'+str(i+2)+'x) = (q1y-q'+str(i+2)+'y) | (q1x-q'+str(i+2)+'x) = -(q1y-q'+str(i+2)+'y))?1:0)+ ')
    f.write('(((q1x-q'+str(n)+'x) = (q1y-q'+str(n)+'y) | (q1x-q'+str(n)+'x) = -(q1y-q'+str(n)+'y))?1:0);\n')



    
    f.write('label overall_attack = ')
    for j in range(1, n):
        for i in range(j+1, n+1):
            f.write('((q'+str(j)+'x-q'+str(i)+'x) = (q'+str(j)+'y-q'+str(i)+'y) | (q'+str(j)+'x-q'+str(i)+'x) = -(q'+str(j)+'y-q'+str(i)+'y)) | ')
            if j==n-1 and i==n:
                f.write('(q'+str(j)+'x = q'+str(i)+'x);\n\n')
            else:
                f.write('(q'+str(j)+'x = q'+str(i)+'x)| ')


                
    for i in range(n-1):
        f.write('module q'+str(i+2)+' = q1 [ q1x=q'+str(i+2)+'x, q'+str(i+2)+'x=q1x, q1y=q'+str(i+2)+'y, q'+str(i+2)+'y=q1y, v1=v'+str(i+2)+', v'+str(i+2)+'=v1] endmodule\n')
    
