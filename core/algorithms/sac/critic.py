from typing import Tuple

from torch import Tensor
from torch.nn import Module

from ...value_functions import QFunction, VFunction

ImageType = Tuple[int, int, int]


class CriticQ(Module):
    def __init__(
        self, obs_features: ImageType, action_dim: int, device=None, dtype=None
    ) -> None:
        super(CriticQ, self).__init__()
        factor_kwargs = {"device": device, "dtype": dtype}
        self.q = QFunction(obs_features, action_dim, **factor_kwargs)

    def forward(self, obs: Tensor, action: Tensor) -> Tensor:
        return self.q(obs, action)


class CriticV(Module):
    def __init__(self, obs_features: ImageType, device=None, dtype=None) -> None:
        super(CriticV, self).__init__()
        factor_kwargs = {"device": device, "dtype": dtype}
        self.v = VFunction(obs_features, **factor_kwargs)

    def forward(self, obs: Tensor) -> Tensor:
        return self.v(obs)
