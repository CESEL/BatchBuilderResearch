from constant_batch_size import ConstantBatching
import pandas as pd
import os
data=pd.read_csv("./data/extracted_project_travis/traccar.csv")
projects=(os.listdir("./data/extracted_project_travis"))
print(len(projects))
print(len(data))
data = data.build_successful
data = pd.Series.tolist(data)
i=0
for project in projects:
    project_path='./data/extracted_project_travis/'+project
    data = pd.read_csv(project_path)
    data = data.build_successful
    data = pd.Series.tolist(data)

    cb=ConstantBatching(data,4,method="batch_stop4")
    test_number=(cb.run())
    print(project,1 - (test_number / (len(data))))








