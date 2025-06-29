# 鲁棒控制理论

## 1. 形式化定义

### 1.1 不确定系统

**定义 1.1 (不确定系统)**

\[
\dot{x}(t) = (A + \Delta A)x(t) + (B + \Delta B)u(t)
\]
其中 \( \Delta A, \Delta B \) 表示系统参数不确定性。

### 1.2 H∞控制

**定义 1.2 (H∞范数)**

\[
\|G(s)\|_{H^\infty} = \sup_{\omega \in \mathbb{R}} \bar{\sigma}(G(j\omega))
\]

## 2. 主要定理与证明

### 2.1 小增益定理

**定理 2.1 (小增益定理)**
若两个系统的增益乘积小于1，则闭环系统稳定。

**证明**：
略。详见 Zhou, Doyle & Glover (1996)。

### 2.2 μ分析

**定理 2.2 (μ分析鲁棒性判据)**
若 \( \mu(\Delta) < 1 \)，则系统鲁棒稳定。

## 3. 典型算法

### 3.1 H∞控制器设计

```haskell
-- H∞控制伪代码
hinfControl :: System -> Weighting -> Controller
hinfControl sys w =
  let p = augmentPlant sys w
      k = solveHinfSynthesis p
  in k
```

### 3.2 μ综合

```haskell
-- μ综合伪代码
muSynthesis :: System -> Uncertainty -> Controller
muSynthesis sys delta =
  let k = solveMuSynthesis sys delta
  in k
```

## 4. 复杂度与极限分析

- H∞综合复杂度高，依赖于LMI求解器
- μ综合为NP难问题
- 鲁棒极限：无法对所有不确定性完全鲁棒

## 5. 工程实践与案例

- 航空航天鲁棒飞控
- 电力系统鲁棒调节
- 汽车主动安全鲁棒控制

## 6. 参考文献

1. Zhou, K., Doyle, J. C., & Glover, K. (1996). Robust and Optimal Control.
2. Skogestad, S., & Postlethwaite, I. (2005). Multivariable Feedback Control.
3. Basar, T., & Bernhard, P. (2008). H∞-Optimal Control and Related Minimax Design Problems.

## 7. 交叉引用

- [线性控制理论](./01_Linear_Control_Theory.md)
- [非线性控制理论](./02_Nonlinear_Control_Theory.md)
- [自适应控制理论](./03_Adaptive_Control_Theory.md) 