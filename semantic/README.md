# Lean 语法与语义理论文档库 / Lean Syntax and Semantics Documentation

## 概述 / Overview

本目录包含 Lean 语言语法与语义理论的完整文档，采用维基风格与 Lean 4（2025）规范对齐，涵盖类型论、证明论、模型论、范畴论、同伦类型论等核心理论。

## 文档结构 / Document Structure

### 1. 理论基础 / Theoretical Foundations

- [1.1 Lean 理论基础与语义模型](1-lean-grammar-and-semantics/1.1-lean-理论基础与语义模型.md) - 依赖类型理论、Curry-Howard 同构
- [1.2 Lean 类型系统与证明系统](1-lean-grammar-and-semantics/1.2-lean-类型系统与证明系统.md) - 依赖类型、归纳类型、宇宙层级
- [1.3 Lean 语法结构与表达式分析](1-lean-grammar-and-semantics/1.3-lean-语法结构与表达式分析.md) - BNF、AST、类型推断
- [1.4 Lean 元编程与策略系统](1-lean-grammar-and-semantics/1.4-lean-元编程与策略系统.md) - syntax/macro_rules、elab tactic

### 2. 实践应用 / Practical Applications

- [1.5 Lean 与主流语言对比](1-lean-grammar-and-semantics/1.5-lean-与主流语言对比.md) - 与 Coq、Agda、Haskell 等对比
- [1.6 Lean 工程案例与应用](1-lean-grammar-and-semantics/1.6-lean-工程案例与应用.md) - 软件验证、密码学、分布式系统
- [1.7 Lean 生态与工具链](1-lean-grammar-and-semantics/1.7-lean-生态与工具链.md) - mathlib4、Lake、IDE 支持

### 3. 类型论理论 / Type Theory

- [1.8 类型论理论模型](1-lean-grammar-and-semantics/1.8-类型论理论模型.md) - STT、DTT、MLTT、HoTT
- [1.8.1 简单类型理论](1-lean-grammar-and-semantics/1.8.1-简单类型理论.md) - λ-演算、函数类型
- [1.8.2 依赖类型理论](1-lean-grammar-and-semantics/1.8.2-依赖类型理论.md) - Π/Σ 类型、归纳类型
- [1.8.4 Martin-Löf 类型论](1-lean-grammar-and-semantics/1.8.4-Martin-Löf类型论.md) - 归纳类型、宇宙层级
- [1.8.5 Curry-Howard 对应](1-lean-grammar-and-semantics/1.8.5-Curry-Howard对应.md) - 类型=命题、程序=证明

### 4. 证明论 / Proof Theory

- [1.9 证明论与推理系统](1-lean-grammar-and-semantics/1.9-证明论与推理系统.md) - 自然演绎、序列演算、归纳证明
- [1.9.1 自然演绎系统](1-lean-grammar-and-semantics/1.9.1-自然演绎系统.md) - 引入/消解规则
- [1.9.2 序列演算](1-lean-grammar-and-semantics/1.9.2-序列演算.md) - Γ ⊢ Δ、结构规则
- [1.9.3 归纳证明与递归原理](1-lean-grammar-and-semantics/1.9.3-归纳证明与递归原理.md) - 数学归纳、结构归纳
- [1.9.4 自动化证明与策略](1-lean-grammar-and-semantics/1.9.4-自动化证明与策略.md) - tactic 语言、AI 辅助

### 5. 模型论 / Model Theory

- [1.10 模型论与语义模型](1-lean-grammar-and-semantics/1.10-模型论与语义模型.md) - 操作语义、指称语义、公理语义
- [1.10.1 操作语义](1-lean-grammar-and-semantics/1.10.1-操作语义.md) - 小步/大步语义
- [1.10.2 指称语义](1-lean-grammar-and-semantics/1.10.2-指称语义.md) - 域理论、函数映射
- [1.10.3 公理语义](1-lean-grammar-and-semantics/1.10.3-公理语义.md) - Hoare 逻辑、前置/后置条件
- [1.10.4 语法-语义映射](1-lean-grammar-and-semantics/1.10.4-语法-语义映射.md) - 解释函数、一致性
- [1.10.5 语义一致性与可判定性](1-lean-grammar-and-semantics/1.10.5-语义一致性与可判定性.md) - 一致性证明、可判定性

### 6. 范畴论 / Category Theory

- [1.11 范畴论与类型理论](1-lean-grammar-and-semantics/1.11-范畴论与类型理论.md) - 范畴、函子、自然变换
- [1.11.1 范畴与函子](1-lean-grammar-and-semantics/1.11.1-范畴与函子.md) - 对象、态射、函子
- [1.11.2 自然变换与极限](1-lean-grammar-and-semantics/1.11.2-自然变换与极限.md) - 极限、余极限
- [1.11.3 Curry-Howard-Lambek 对应](1-lean-grammar-and-semantics/1.11.3-Curry-Howard-Lambek对应.md) - 类型-命题-对象三重对应

### 7. 同伦类型论 / Homotopy Type Theory

- [1.12 同伦类型论](1-lean-grammar-and-semantics/1.12-同伦类型论.md) - 路径类型、单值性公理
- [1.12.1 路径类型与等价](1-lean-grammar-and-semantics/1.12.1-路径类型与等价.md) - Path 类型、等价
- [1.12.2 单值性公理](1-lean-grammar-and-semantics/1.12.2-单值性公理.md) - Univalence Axiom
- [1.12.3 高阶等价与∞-范畴](1-lean-grammar-and-semantics/1.12.3-高阶等价与∞-范畴.md) - n-路径、∞-范畴
- [1.12.4 HoTT 在 Lean 及数学中的应用](1-lean-grammar-and-semantics/1.12.4-HoTT在Lean及数学中的应用.md) - 同伦、拓扑、代数结构

## 2. Lean形式化理论基础 / Lean Formal Theory Foundations

基于docs目录中的丰富理论内容，构建Lean语言的形式化理论统一框架。

### 2.1 形式化理论统一框架 / Formal Theory Unified Framework

- [2.1 形式化理论统一框架](2-lean-形式化理论基础/2.1-形式化理论统一框架.md) - 统一形式系统、类型理论与证明论统一、依赖类型理论实现

### 2.2 类型论与证明论基础 / Type Theory and Proof Theory Foundations

- [2.2 类型论与证明论基础](2-lean-形式化理论基础/2.2-类型论与证明论基础.md) - 简单类型理论、依赖类型理论、Martin-Löf类型论、Curry-Howard对应

### 2.3 模型论与语义分析 / Model Theory and Semantic Analysis

- [2.3 模型论与语义分析](2-lean-形式化理论基础/2.3-模型论与语义分析.md) - 操作语义、指称语义、公理语义、语义一致性

### 2.4 范畴论与类型理论 / Category Theory and Type Theory

- [2.4 范畴论与类型理论](2-lean-形式化理论基础/2.4-范畴论与类型理论.md) - 范畴与函子、自然变换与极限、Curry-Howard-Lambek对应

### 2.5 同伦类型论 / Homotopy Type Theory

- [2.5 同伦类型论](2-lean-形式化理论基础/2.5-同伦类型论.md) - 路径类型与等价、单值性公理、高阶等价与∞-范畴

### 2.6 形式化验证与工程实践 / Formal Verification and Engineering Practice

- [2.6 形式化验证与工程实践](2-lean-形式化理论基础/2.6-形式化验证与工程实践.md) - 模型检查、定理证明、自动化验证、工程应用

## 规范标准 / Standards

### Lean 4（2025）规范对齐

- **语法扩展**：统一使用 `syntax`/`macro_rules`
- **战术系统**：`elab ... : tactic` 替代旧式 `meta def`
- **类型系统**：`Sort u`/`Type u` 层级、`Prop` 证据不可计算
- **终止性**：结构递归优先，必要时 `termination_by`/`decreasing_by`

### 版本兼容性

- Lean 3 → Lean 4 迁移要点
- mathlib4 依赖版本标注
- API 变更说明

### 工程实践

- 可编译代码示例
- 必要 `import` 语句
- 计算与性质分离
- 自动化规则配置

## 导航工具 / Navigation Tools

- [进度文档](CONTINUOUS_PROGRESS.md) - 处理进度与状态跟踪
- [统一模板](_TEMPLATE-WIKI-STYLE.md) - 维基风格+Lean4 2025规范模板
- [发布说明](RELEASE_NOTES.md) - 发布说明与版本信息
- [项目报告](PROJECT_COMPLETION_REPORT.md) - 项目完成报告与总结
- [批判分析](CRITICAL_ANALYSIS_REPORT.md) - 批判性分析报告与评价

## 参考资料 / References

- [Lean 4 Reference Manual](https://leanprover.github.io/lean4/doc/)
- [Mathlib4 文档](https://leanprover-community.github.io/mathlib4_docs/)
- [Lean 社区](https://leanprover-community.github.io/)

---

> 本文档库持续对齐 Wikipedia 风格与 Lean 4（2025）最新规范，支持本地跳转与交叉引用。
