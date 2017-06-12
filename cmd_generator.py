#!/bin/python

# generating the commands with the -e option
# also writes an bash script that creates the output folders

list_scheduler = ['baseline' , 'recursive-remain-flow', 'varys', 'multipath']
list_jobs = ['BigBench', 'FB' , 'TPC-DS' , 'TPC-H']
list_gml = ['swan']

f = file ('make_output_dir.sh' , 'w')

for g in list_gml:
    
    for j in list_jobs:
        #print '\n--scheduler: ' + s + ' -gml: ' + g
        
        for s in list_scheduler:             
            f.write('mkdir -p ~/output/' + g+'/'+j+'/'+s+'\n'  )
            print 'java -cp target/gaia_ctrl-jar-with-dependencies.jar gaiasim.GaiaSim -g data/gml/' + g + '.gml -j data/combined_traces_fb/' + j + '-' + g +'.txt -s ' + s + ' -o ' + '~/output/' + g+'/'+j+'/'+s + ' > ~/output/' + g+'/'+j+'/'+s+'/exec_log.txt'

    

f.close()
