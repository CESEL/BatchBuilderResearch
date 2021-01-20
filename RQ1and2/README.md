# Replication Package for RQ 1 and 2

In these research questions, we examine how many build test executions can be saved relative to testing each build individually. In RQ 1 we simple batching and bisection in RQ 2 we use risk based models to do predict builds that are likely to fail.

### Instalation and running

1. Install [Docker](https://docs.docker.com/get-docker/) on your computer.
2. Clone this github repo, this includes both the code and the [data](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ1%2C2/data)
3. In the terminal, go to this directory and run the commands below

<code> docker build -t rq1and2 </code>

In which "rq1and" is the name of the docker mage

5. After completing the build process, run the following command, with project ID

<code> docker run -it rq1and2 </code>
