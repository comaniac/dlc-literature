#cpu #tvm #autotvm #tuning #dynamic-programming #graph-tuning

## Optimizing CNN Model Inference on CPUs

## Bibtex
```
@inproceedings{liu2019optimizing,
  title={Optimizing $\{$CNN$\}$ Model Inference on CPUs},
  author={Liu, Yizhi and Wang, Yao and Yu, Ruofei and Li, Mu and Sharma, Vin and Wang, Yida},
  booktitle={2019 $\{$USENIX$\}$ Annual Technical Conference ($\{$USENIX$\}$$\{$ATC$\}$ 19)},
  pages={1025--1040},
  year={2019}
}
```

## Paper
https://www.usenix.org/system/files/atc19-liu-yizhi.pdf

## Summary
- [[TVM]] graph tuner for Conv2D with NCHW layout on CPU.
- Based on the [[AutoTVM]] tuning results.
- Benchmark layout transform (`NCHW[x]c` to `NCHW[y]c`) overheads.
- Use dynamic programming to optimize the `c`.
