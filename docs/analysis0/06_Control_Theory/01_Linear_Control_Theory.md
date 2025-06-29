# 线性控制理论

## 1. 形式化定义

### 1.1 线性系统

**定义 1.1 (线性时不变系统)**

\[
\dot{x}(t) = A x(t) + B u(t), \quad y(t) = C x(t) + D u(t)
\]
其中 \( x(t) \in \mathbb{R}^n \) 为状态，\( u(t) \in \mathbb{R}^m \) 为输入，\( y(t) \in \mathbb{R}^p \) 为输出。

### 1.2 状态空间与传递函数

**定义 1.2 (传递函数)**

\[
G(s) = C (sI - A)^{-1} B + D
\]

## 2. 主要定理与证明

### 2.1 可控性

**定理 2.1 (可控性判据)**

系统 \( (A, B) \) 可控当且仅当
\[
\operatorname{rank}\left([B, AB, \ldots, A^{n-1}B]\right) = n
\]

**证明**：
略。详见 Kailath (1980)。

### 2.2 可观性

**定理 2.2 (可观性判据)**

系统 \( (A, C) \) 可观当且仅当
\[
\operatorname{rank}\left(\begin{bmatrix}C \\ CA \\ \vdots \\ CA^{n-1}\end{bmatrix}\right) = n
\]

**证明**：
略。

### 2.3 极点配置

**定理 2.3 (极点配置可行性)**

若系统可控，则任意极点可配置。

## 3. 典型算法

### 3.1 LQR 最优控制

```haskell
-- LQR 最优控制伪代码
lqr :: Matrix -> Matrix -> Matrix -> Matrix -> (Matrix, Matrix)
lqr a b q r =
  let p = solveRiccati a b q r
      k = inv r * transpose b * p
  in (k, p)
```

### 3.2 极点配置

```haskell
-- 极点配置伪代码
placePoles :: Matrix -> Matrix -> [Complex] -> Matrix
placePoles a b poles =
  let k = computeGain a b poles
  in k
```

## 4. 复杂度与极限分析

- Riccati方程求解复杂度：\( O(n^3) \)
- 极点配置算法复杂度：\( O(n^3) \)
- 线性系统理论极限：仅适用于线性、时不变系统

## 5. 工程实践与案例

- 飞行器姿态控制
- 电机伺服系统
- 自动驾驶车辆线性控制

## 6. 参考文献

1. Kailath, T. (1980). Linear Systems.
2. Ogata, K. (2010). Modern Control Engineering.
3. Zhou, K., Doyle, J. C., & Glover, K. (1996). Robust and Optimal Control.

## 7. 交叉引用

- [非线性控制理论](./02_Nonlinear_Control_Theory.md)
- [自适应控制理论](./03_Adaptive_Control_Theory.md)
- [鲁棒控制理论](./04_Robust_Control_Theory.md) 