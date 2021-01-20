# Replication Package for RQ 3

On all projects with more than 1000 builds on Travis CI, we investigate the relationship between batching effiectiveness and potential to save build test executions.

### Instalation and running

1. Install [Docker](https://docs.docker.com/get-docker/) on your computer.
2. Clone this github repo, this includes both the code and the [data](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ3/data/extracted_project_travis)
3. In the terminal, go to this directory and run the commands below

<code> docker build -t rq3 .</code>

In which "rq1and" is the name of the docker image

5. After completing the build process, run the following command, with project ID

<code> docker run -it rq3 </code>
