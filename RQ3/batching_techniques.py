


def runbatch(batch):

    for test in batch:
        if (test == False):
            return False
    return True


def batch_bisect(batch):
    rc =0
    lc =0


    if (len(batch) <= 2):
        return len(batch)
    else:
        sub_batch_right = batch[0:(int)(len(batch) / 2)]
        sub_batch_left = batch[(int)(len(batch) / 2):len(batch)]
        if (runbatch(sub_batch_right) == False):
            rc= batch_bisect(sub_batch_right)

        if (runbatch(sub_batch_left) == False):
            lc= batch_bisect(sub_batch_left)

        return (rc +lc +2)





def batch_stop4(batch):
    rc =0
    lc =0


    if (len(batch) <= 4):
        return len(batch)
    else:
        sub_batch_right = batch[0:(int)(len(batch) / 2)]
        sub_batch_left = batch[(int)(len(batch) / 2):len(batch)]
        if (runbatch(sub_batch_right) == False):
            rc= batch_stop4(sub_batch_right)

        if (runbatch(sub_batch_left) == False):
            lc= batch_stop4(sub_batch_left)

        return (rc +lc +2)


