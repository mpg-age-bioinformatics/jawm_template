import jawm

template_p=jawm.Process( 
    name="template",
    script="""#!/bin/bash
echo "{{extra_args}} {{my_demo_argument}}" 2>&1 | tee {{mk.output}}/demo.txt
""",

    # arguments for the script above :
    
    # var={
    #     "extra_args": "",
    #     "my_demo_argument":"This is just a demo.", 
    #     "mk.output":"<output_folder>", # the prefix "mk." leads to the creation of this folder and volume mapping if you are using containers
                                         # simple file mapping can be achieved with the prefix map. eg. map.my_file.txt
    # },
    
    # example arguments for jawn

    # manager="slurm",
    # manager_slurm={
    #     "-p":"cluster,dedicated", 
    #     "--mem":"20GB", 
    #     "-t":"1:00:00", 
    #     "-c":"8" 
    # },
    
    # container="docker://mpgagebioinformatics/fastqc:0.11.9",
    # environmnent="apptainer",
    # environment_apptainer={ '-B': [input_file, output_folder] }
    
    # container="mpgagebioinformatics/fastqc:0.11.9",
    # environmnent="docker",
    # environment_docker={ '-v': [input_file, output_folder] },


    # param_file="yaml/apptainer.params.yaml" ,
    # param_file=[ "yaml/apptainer.params.yaml" , "yaml/slurm.params.yaml" ],
  
)



if __name__ == "__main__":
    import sys
    from jawm.utils import workflow

    workflows, args, unknown_args = jawm.utils.parse_arguments(["main","template","test"],)

    # usage: 

    if workflow( ["main","template","test"], workflows ) :

        # execute process
        template_p.execute()

        # # execute a process with dependencies
        # demo_p2.depends_on=[demo_p1.hash]
        # demo_p2.execute()

        # wait for all above processes to complete
        jawm.Process.wait()

        # print the output
        print(template_p.get_output())

    if workflow( "test", workflows ) :

        # for the test workflow we might also do something more
        print("Test completed.")


    sys.exit(0)