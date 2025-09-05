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

### 2.7 前沿理论发展 / Advanced Theoretical Developments

- [2.7 前沿理论发展](2-lean-形式化理论基础/2.7-前沿理论发展.md) - 量子类型理论、时态类型理论、概率类型理论、AI辅助证明

### 2.8 跨学科应用 / Interdisciplinary Applications

- [2.8 跨学科应用](2-lean-形式化理论基础/2.8-跨学科应用.md) - 数学、物理学、计算机科学、生物学、经济学应用

### 2.9 工程实践指南 / Engineering Practice Guide

- [2.9 工程实践指南](2-lean-形式化理论基础/2.9-工程实践指南.md) - 项目规划、开发流程、质量保证、性能优化、团队协作

## 3. 学习路径指南 / Learning Path Guide

为不同层次的Lean语言学习者提供完整的学习路径指南，从初学者到高级专家。

### 3.1 初学者学习路径 / Beginner Learning Path

- [3.1 初学者学习路径](3-学习路径指南/3.1-初学者学习路径.md) - 基础概念、语法学习、简单证明、实践项目

### 3.2 中级学习路径 / Intermediate Learning Path

- [3.2 中级学习路径](3-学习路径指南/3.2-中级学习路径.md) - 高级类型系统、复杂证明、数据结构、算法分析

### 3.3 高级学习路径 / Advanced Learning Path

- [3.3 高级学习路径](3-学习路径指南/3.3-高级学习路径.md) - 依赖类型、同伦类型论、形式化验证、理论研究

### 3.4 专业方向指南 / Specialization Guide

- [3.4 专业方向指南](3-学习路径指南/3.4-专业方向指南.md) - 数学形式化、软件验证、类型理论、编译器设计

### 3.5 实践项目集 / Practice Projects

- [3.5 实践项目集](3-学习路径指南/3.5-实践项目集.md) - 从简单到复杂的实践项目，涵盖各个学习阶段

### 3.6 评估与认证 / Assessment and Certification

- [3.6 评估与认证](3-学习路径指南/3.6-评估与认证.md) - 学习成果评估、技能认证、能力测试

## 4. 索引系统 / Index System

提供完整的索引系统，帮助用户快速定位和查找所需信息。

### 4.1 主题索引 / Topic Index

- [4.1 主题索引](4-索引系统/4.1-主题索引.md) - 按主题分类组织所有文档，建立层次化主题结构

### 4.2 概念索引 / Concept Index

- [4.2 概念索引](4-索引系统/4.2-概念索引.md) - 按概念分类组织所有重要概念、定义、定理和术语

### 4.3 交叉引用索引 / Cross-Reference Index

- [4.3 交叉引用索引](4-索引系统/4.3-交叉引用索引.md) - 建立文档之间的关联关系，形成完整的知识网络

### 4.4 快速查找指南 / Quick Reference Guide

- [4.4 快速查找指南](4-索引系统/4.4-快速查找指南.md) - 提供多种查找方式，帮助用户快速定位所需信息

## 5. 工具集成指南 / Tool Integration Guide

提供完整的工具链集成指南，帮助用户高效地使用Lean语言进行开发和验证。

### 5.1 开发环境配置 / Development Environment Setup

- [5.1 开发环境配置](5-工具集成指南/5.1-开发环境配置.md) - 系统要求、安装步骤、环境配置和验证方法

### 5.2 IDE集成 / IDE Integration

- [5.2 IDE集成](5-工具集成指南/5.2-IDE集成.md) - VS Code、Vim、Emacs等编辑器的Lean集成配置

### 5.3 编译器配置 / Compiler Configuration

- [5.3 编译器配置](5-工具集成指南/5.3-编译器配置.md) - Lean编译器配置、优化选项、构建系统

### 5.4 包管理 / Package Management

- [5.4 包管理](5-工具集成指南/5.4-包管理.md) - Lake包管理器、依赖管理、版本控制

### 5.5 调试工具 / Debugging Tools

- [5.5 调试工具](5-工具集成指南/5.5-调试工具.md) - 调试器、性能分析、错误诊断

### 5.6 测试工具 / Testing Tools

- [5.6 测试工具](5-工具集成指南/5.6-测试工具.md) - 单元测试、集成测试、性能测试

### 5.7 部署工具 / Deployment Tools

- [5.7 部署工具](5-工具集成指南/5.7-部署工具.md) - 应用部署、容器化、CI/CD集成

## 6. 社区资源 / Community Resources

提供完整的社区资源，包括贡献指南、反馈系统、协作平台、社区活动等。

### 6.1 贡献指南 / Contribution Guide

- [6.1 贡献指南](6-社区资源/6.1-贡献指南.md) - 如何参与项目、贡献内容、代码规范、提交流程

### 6.2 反馈系统 / Feedback System

- [6.2 反馈系统](6-社区资源/6.2-反馈系统.md) - 问题报告、功能请求、改进建议、用户反馈

### 6.3 协作平台 / Collaboration Platform

- [6.3 协作平台](6-社区资源/6.3-协作平台.md) - 在线协作、版本控制、项目管理、团队协作

### 6.4 社区活动 / Community Events

- [6.4 社区活动](6-社区资源/6.4-社区活动.md) - 学习活动、技术分享、会议参与、培训课程

### 6.5 学习资源 / Learning Resources

- [6.5 学习资源](6-社区资源/6.5-学习资源.md) - 教程资源、示例代码、实践项目、学习路径

### 6.6 技术支持 / Technical Support

- [6.6 技术支持](6-社区资源/6.6-技术支持.md) - 问题解答、技术咨询、故障排除、最佳实践

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
