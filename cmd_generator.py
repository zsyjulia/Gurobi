#!/bin/python

# generating the commands with the -e option
# also writes an bash script that creates the output folders

#list_scheduler = ['baseline' , 'recursive-remain-flow']
#list_jobs = ['BigBench', 'FB' , 'TPC-DS' , 'TPC-H']
#list_gml = ['swan' , 'gb4' , 'ntt_new' , 'AttMpls']

list_scheduler = ['baseline', 'recursive-remain-flow']
list_gml = ['swan']
list_jobs = ['BigBench', 'FB' , 'TPC-DS' , 'TPC-H']

f = file ('make_output_dir.sh' , 'w')

for s in list_scheduler:
    
    for g in list_gml:
        #print '\n--scheduler: ' + s + ' -gml: ' + g
        
        for j in list_jobs:             
            f.write('mkdir -p ../output-halfbw/' + s+'/'+g+'/'+j+'\n'  )
            print 'java -cp target/gaiasim-0.0.9-SNAPSHOT-jar-with-dependencies.jar gaiasim.GaiaSim -g data/gml/' + g + '.gml -j data/combined_traces_fb/' + j + '-' + g +'.txt -s ' + s + ' -o ' + '../output-halfbw/' + s+'/'+g+'/'+j + ' > ../output-halfbw/' + s+'/'+g+'/'+j+'/exec_log.txt'


f.close()
