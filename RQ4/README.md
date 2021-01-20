# Replication Package for RQ 4

We examine the change in feedback time for the simple batching approaches relative to testing each commit individually.

### Instalation and running

1. Install [Docker](https://docs.docker.com/get-docker/) on your computer.
2. Clone this github repo, this includes both the code and the [data](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ4/data)
3. In the terminal, go to this directory and run the commands below

<code> docker build -t rq4 </code>

In which "rq1and" is the name of the docker image

5. After completing the build process, run the following command, with project ID

<code> docker run -it rq4 </code>
