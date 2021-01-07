# Replication Package for RQ 3

On all projects with more than 1000 builds on Travis CI, we investigate the relationship between batching effiectiveness and potential to save build test executions.

### Instalation and running

1. Install [Docker](https://docs.docker.com/get-docker/) on your computer.
2. Clone this github repo, this includes both the code and the [data](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ3/data/extracted_project_travis)
3. In the terminal, go to this directory and run the commands below

```
  docker build .

```

4. Copy the ID of the built conatainer like the following figure
   ![Image description](https://github.com/CESEL/BatchBuilderResearch/blob/master/RQ1%2C2/container_id.png)
5. Run the following command, with project ID

<code> docker run -it \<ID\> </code>

For example, from the figure above the ID is 

<code> docker run -it 3f5987129fd3b27872fed0f71f1135f128dbb9ffd75bf </code>



