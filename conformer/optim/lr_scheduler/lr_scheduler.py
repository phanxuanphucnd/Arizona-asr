# -*- coding: utf-8 -*

class LearningRateScheduler(object):
    """
    Provides inteface of learning rate scheduler.
    Note:
        Do not use this class directly, use one of the sub classes.
    """
    def __init__(self, optimizer, init_lr):
        self.optimizer = optimizer
        self.init_lr = init_lr

    def step(self, *args, **kwargs):
        raise NotImplementedError

    @staticmethod
    def set_lr(optimizer, lr):
        for g in optimizer.param_groups:
            g['lr'] = lr

    def get_lr(self):
        for g in self.optimizer.param_groups:
            return g['lr']