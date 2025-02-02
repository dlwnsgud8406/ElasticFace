import logging
import os
import sys


class AverageMeter(object):
    """Computes and stores the average and current value
    """

    def __init__(self):
        self.val = None
        self.avg = None
        self.sum = None
        self.count = None
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


# def init_logging(log_root, rank, models_root, logfile=None):
def init_logging(log_root, models_root, logfile=None):
    # if rank is 0:
    log_root.setLevel(logging.INFO)
    formatter = logging.Formatter("Training: %(asctime)s-%(message)s")
    file_name = "training.log" if logfile is None else logfile
    print('this is models_root and file_name', models_root, file_name)
    # handler_file = logging.FileHandler("output/R100_ElasticArcFace")
    handler_stream = logging.StreamHandler(sys.stdout)
    # handler_file.setFormatter(formatter)
    handler_stream.setFormatter(formatter)
    # log_root.addHandler(handler_file)
    log_root.addHandler(handler_stream)
    # log_root.info('rank_id: %d' % rank)
