#tuning #codegen #cpu #gpu #fpga

## TVM: An automated end-to-end optimizing compiler for deep learning
## Bibtex
```
@inproceedings{chen2018tvm,
  title={$\{$TVM$\}$: An automated end-to-end optimizing compiler for deep learning},
  author={Chen, Tianqi and Moreau, Thierry and Jiang, Ziheng and Zheng, Lianmin and Yan, Eddie and Shen, Haichen and Cowan, Meghan and Wang, Leyuan and Hu, Yuwei and Ceze, Luis and others},
  booktitle={13th $\{$USENIX$\}$ Symposium on Operating Systems Design and Implementation ($\{$OSDI$\}$ 18)},
  pages={578--594},
  year={2018}
}
```

## Paper
https://www.usenix.org/system/files/osdi18-chen.pdf

## Summary
There is an increasing need to bring machine learning to a wide diversity of hardware devices. Current frameworks rely on vendor-specific operator libraries and optimize for a narrow range of server-class GPUs. Deploying workloads to new platforms -- such as mobile phones, embedded devices, and accelerators (e.g., FPGAs, ASICs) -- requires significant manual effort. We propose TVM, a compiler that exposes graph-level and operator-level optimizations to provide performance portability to deep learning workloads across diverse hardware back-ends. TVM solves optimization challenges specific to deep learning, such as high-level operator fusion, mapping to arbitrary hardware primitives, and memory latency hiding. It also automates optimization of low-level programs to hardware characteristics by employing a novel, learning-based cost modeling method for rapid exploration of code optimizations. Experimental results show that TVM delivers performance across hardware back-ends that are competitive with state-of-the-art, hand-tuned libraries for low-power CPU, mobile GPU, and server-class GPUs. We also demonstrate TVM's ability to target new accelerator back-ends, such as the FPGA-based generic deep learning accelerator. The system is open sourced and in production use inside several major companies.

## Comments
N/A