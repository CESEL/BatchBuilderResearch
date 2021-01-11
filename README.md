# Replication Package

Paper Title: "Software Batch Testing to Reduce Build Test Executions"

Authors: Mohammad Javad Beheshtian, Amir Hossein Bavand, and Peter C. Rigby

Contact us: <s_ehesht@encs.concordia.ca>, <a_bavand@encs.concordia.ca>, <peter.rigby@concordia.ca>

GitHub app to create batches for Travis CI ([app](https://github.com/apps/batchbuilder), [source code](https://github.com/CESEL/BatchBuilder))

### RQ 1 and RQ 2

RQ 1. Batching: How well does simple bisection and batching improve resource utilization?

RQ2. Risk Models: Can commit risk models improvethe resource utilization during batching?

In these research questions, we examine how many build test executions can be saved relative to testing each build individually. In RQ 1 we simple batching and bisection in RQ 2 we use risk based models to do predict builds that are likely to fail.

1. [Code and Instructions](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ1and2)

2. [Data](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ1and2/data)

### RQ3 FailureRate: How does the failure rate effect resource utilization during batching?

On all projects with more than 1000 builds on Travis CI, we investigate the relationship between batching effiectiveness and potential to save build test executions.

[Code and Instructions](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ3)

[Data](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ3/data/extracted_project_travis)

### RQ4 Feedback: What is the impact of batching on feedback time?

We examine the change in feedback time for the simple batching approaches relative to testing each commit individually.

[Code and Instructions](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ4)

[Data](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ4/data)
