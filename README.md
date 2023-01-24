# ganglia (name still needs voted on)
placeholder repo - can turn into the ML-engineering monorepo

## directory structure for jobs 
* every job (i.e. transformation) of input > output is one directory on the instance.
* job directories are synced to an S3 bucket after workflow completion. 
* the structure of job directories integrates with the Bacalhau spec. Each job has a 8-digit hex code. 

### proposed implementation of the control node
* a daemon.py listens to whatever SQS queue or takes a command line prompt - either way, the request is a instruction.json
* when prompted, a job is started that: 
    * creates a job directory with job-903fd982/inputs and job-903fd982/outputs
    * syncs the input data from a bucket into job-903fd982/inputs
    * runs a container on top of the inputs directory
    * exports the results to the outputs directory
* a new job could then be started based on the outputs of job-903fd982

### proposed break down
