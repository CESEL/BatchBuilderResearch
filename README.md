The [BatchBuilder app](https://github.com/apps/batchbuilder) for developers is also available. The source code for the app is [here](https://github.com/CESEL/BatchBuilder)

# Replication Package 

"Software Batch Testing to Reduce Build Test Executions"  

Mohammad Javad Beheshtian, Amir Hossein Bavand, and Peter C. Rigby

<s_ehesht@encs.concordia.ca>, <a_bavand@encs.concordia.ca>, <peter.rigby@concordia.ca>

### RQ 1 and RQ 2

RQ 1. Batching: How well does simple bisection and batching improve resource utilization?

RQ2. Risk Models: Can commit risk models improvethe resource utilization during batching?

In these research questions, we examine how many build test executions can be saved relative to testing each build individually. In RQ 1 we simple batching and bisection in RQ 2 we use risk based models to do predict builds that are likely to fail. 

1. [Code and Instructions](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ1%2C2)

2. [Data](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ1%2C2/data)

### RQ3 FailureRate: How does the failure rate effect resource utilization during batching?

On all projects with more than 1000 builds on Travis CI, we investigate the relationship between batching effiectiveness and potential to save build test executions.

[Code and Instructions](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ3)

[Data](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ3/data/extracted_project_travis)

### RQ4 Feedback: What is the impact of batching on feedback time?

We examine the change in feedback time for the simple batching approaches relative to testing each commit individually.

[Code and Instructions](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ4)

[Data](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ4/data)
