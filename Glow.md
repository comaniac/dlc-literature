#codegen #cpu 

## Glow: Graph lowering compiler techniques for neural networks

## Bibtex
```
@article{rotem2018glow,
  title={Glow: Graph lowering compiler techniques for neural networks},
  author={Rotem, Nadav and Fix, Jordan and Abdulrasool, Saleem and Catron, Garret and Deng, Summer and Dzhabarov, Roman and Gibson, Nick and Hegeman, James and Lele, Meghan and Levenstein, Roman and others},
  journal={arXiv preprint arXiv:1805.00907},
  year={2018}
}
```

## Paper
https://arxiv.org/pdf/1805.00907.pdf

## Summary
- A new IR for deep learning workloads presented by Facebook. Different from TVM or Halide IR, Glow IR is instruction-based, so it is more similar to LLVM IR.
- Lack of details in the paper.
- Only provide CPU backend. By the time the paper was published, only single thread is supported. Now it seems support multithreading, but still CPU only.
- Support heterogeneous execution.
