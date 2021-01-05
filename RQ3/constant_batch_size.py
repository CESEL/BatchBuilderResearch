from batching_techniques import batch_stop4

class ConstantBatching():

    def __init__(self,batch,batch_size=4,method='batch_stop4'):

        self.batch=batch
        self.batch_size=batch_size
        self.method=method
        self.disspatcher={'batch_stop4':batch_stop4}






    @staticmethod
    def runbatch(batch):

        for test in batch:
            if (test == False):
                return False
        return True


    def run(self):
        test_number=0
        batch_size=self.batch_size
        counter = 0
        flag = True
        i = 0
        while (flag):
            i = i + 1

            test_number = test_number + 1
            slicebatch = self.batch[counter:(counter + batch_size)]
            counter = counter + batch_size

            if (self.runbatch(slicebatch) == False and batch_size != 1):
                test_number+=4


            if (counter >= len(self.batch)):
                flag = False
        return test_number







