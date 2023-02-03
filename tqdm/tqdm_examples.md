# tqdm 示例

## IPython/Jupyter 集成

通过 tqdm.notebook 子模块支持 IPython/Jupyter：

```python
from tqdm.notebook import trange, tqdm
from time import sleep

for i in trange(3, desc='1st loop'):
    for j in tqdm(range(100), desc='2nd loop'):
        sleep(0.01)
```

除了 `tqdm` 特性，`tqdm.notebook` 还提供了原生 Jupyter 小部件（兼容 IPython v1-v4 和 Jupyter），支持嵌套和不同颜色（blue: normal, green: completed, red: error/interrupt, light blue: no ETA）。