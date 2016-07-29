import torch
from torch.legacy import nn

class SmoothL1Criterion(nn.Criterion):

    def __init__(self, sizeAverage=True):
        super(SmoothL1Criterion, self).__init__()
        self.sizeAverage = sizeAverage
        self.output_tensor = None

    def updateOutput(self, input, target):
        self.output_tensor = self.output_tensor or input.new(1)
        self._backend.SmoothL1Criterion_updateOutput(
            self._backend.library_state,
            input,
            target,
            self.output_tensor,
            self.sizeAverage
        )
        self.output = self.output_tensor[0]
        return self.output

    def updateGradInput(self, input, target):
        self._backend.SmoothL1Criterion_updateGradInput(
            self._backend.library_state,
            input,
            target,
            self.gradInput,
            self.sizeAverage
        )
        return self.gradInput
