#gpu #halide #tuning #auto-scheduling #cost-model #image-proc 

## Learning to Schedule Halide Pipelines for the GPU

## Bibtex
```
@article{anderson2020learning,
  title={Learning to Schedule Halide Pipelines for the GPU},
  author={Anderson, Luke and Adams, Andrew and Ma, Karima and Li, Tzu-Mao and Ragan-Kelley, Jonathan},
  journal={arXiv preprint arXiv:2012.07145},
  year={2020}
}
```

## Paper
https://arxiv.org/pdf/2012.07145.pdf

## Summary
- A more accurate GPU performance model.
- Three modes tuning on GPU: one-shot, top-5, autotuned.
- Claim to be more efficient than previous work due to a more accurate cost model.
- Quote arguments to previous work:
  - [[Halide-Auto-Schedule-CPU]] focuses on CPU schedules and its algorithm does not scale to evaluate all the nested parallel tiling options for GPUs.
  - [[Halide-Auto-Schedule-GPU]] only uses block level tiling and does not consider optimizations such as register blocking.