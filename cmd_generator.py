#!/bin/python

# generating the commands with the -e option
# also writes an bash script that creates the output folders

list_scheduler = ['baseline' , 'recursive-remain-flow']
list_jobs = ['BigBench', 'FB' , 'TPC-DS' , 'TPC-H']
list_gml = ['swan' , 'gb4' , 'ntt_new' , 'AttMpls']

f = file ('make_output_dir.sh' , 'w')

for s in list_scheduler:
    
    for g in list_gml:
        print '\n--scheduler: ' + s + ' -gml: ' + g
        
        for j in list_jobs:             
            f.write('mkdir -p ~/output/' + s+'/'+g+'/'+j+'\n'  )
            print 'CTRL java -cp target/gaia_ctrl-jar-with-dependencies.jar gaiasim.GaiaSim -e -g data/gml/' + g + '.gml -j data/combined_traces_fb/' + j + '-' + g +'.txt -s ' + s + ' -o ' + '~/output/' + s+'/'+g+'/'+j + ' > ~/output/' + s+'/'+g+'/'+j+'/exec_log.txt'

    print

f.close()