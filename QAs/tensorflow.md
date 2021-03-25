# TensorFlow

## Could not load dynamic library 'cudart64_101.dll'

```
2021-03-23 17:14:44.872550: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'cudart64_101.dll'; dlerror: cudart64_101.dll not found
2021-03-23 17:14:44.872663: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
2021-03-23 17:14:46.412124: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
2021-03-23 17:14:46.418588: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x24ac55257f0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2021-03-23 17:14:46.418733: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2021-03-23 17:14:46.420560: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'nvcuda.dll'; dlerror: nvcuda.dll not found
2021-03-23 17:14:46.420675: E tensorflow/stream_executor/cuda/cuda_driver.cc:313] failed call to cuInit: UNKNOWN ERROR (303)
2021-03-23 17:14:46.423628: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:169] retrieving CUDA diagnostic information for host: maojiawei-work
2021-03-23 17:14:46.423788: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:176] hostname: maojiawei-work
```

在 `tensorflow` 2.1+ 默认包含 CPU 和 GPU。在之前的 TF 版本中，如果没找到 CUDA 库会抛出错误，而现在或动态查找 CUDA，如果没找到，抛出警告（**W** 开头表示警告），然后使用 CPU模式。

如果你没有 GPU，完全可以不在意该警告，如果希望启用 GPU 加速，则需要安装 CUDA。