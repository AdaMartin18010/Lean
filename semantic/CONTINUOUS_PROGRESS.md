# Lean语法与语义理论递归梳理进度文档

---

## 计划说明

- 目标：对齐 Wikipedia 风格规范与 Lean 4（2025）最新语言规范，递归迭代清理“无实质内容”的文件并补实。
- 来源目录：docs/ 与 analysis/ 下所有子目录和文件。
- 输出目录：semantic/，严格树形编号、内容精炼、交叉引用完善、Latex规范。
- 支持断点续作，每次进度自动记录。

---

## 规范要点（执行基线）

- 维基风格：导语（概要）优先；清晰分节：术语与定义、语言规范（Lean4 2025）、语法、语义、示例、实践指南/陷阱、参见、参考与外链、版本兼容性、变更记录。
- Lean4 2025 对齐：宏/语法扩展统一使用 `syntax`/`macro_rules`；战术以 `elab ... : tactic` 形式实现；示例可编译/可运行；避免 Lean 3 风格 API。
- 文内链接统一相对路径与节内锚点；中英文术语首次同现，后续以中文为主。

---

## 本轮已处理文件（增量对齐：v2025-01）

- [x] `semantic/1-lean-grammar-and-semantics/1.4-lean-元编程与策略系统.md`（替换过时 tactic 示例；补充宏与语法扩展示例；新增版本兼容性与参考）
- [x] `semantic/1-lean-grammar-and-semantics/1.3-lean-语法结构与表达式分析.md`（新增"Lean 4 2025 语法更新要点"与示例）
- [x] `semantic/1-lean-grammar-and-semantics/1.2-lean-类型系统与证明系统.md`（新增"2025 规范对齐"与宇宙/Prop 说明）
- [x] `semantic/1-lean-grammar-and-semantics/1.10.4-语法-语义映射.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.12.2-单值性公理.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.11.3-Curry-Howard-Lambek对应.md`（新增规范对齐/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.10.3-公理语义.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.9.4.2-自动化证明的局限与前沿.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.9.4.1-Lean tactic语言高级用法.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.8.2.1-Π类型（依赖函数类型）.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.8.2.2-Σ类型（依赖积类型）.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.12.1-路径类型与等价.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.11.1-范畴与函子.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.10.1-操作语义.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.10.2-指称语义.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.10.5-语义一致性与可判定性.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.10.2.1-域理论详解.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.10.1.1-小步语义与大步语义对比.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.10.3.1-Hoare逻辑的扩展.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.11.2-自然变换与极限.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.11.2.1-极限的具体类型.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.11.4-范畴语义学在Lean中的应用.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.12.3-高阶等价与∞-范畴.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.12.3.1-∞-范畴的具体建模方法.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.9.1-自然演绎系统.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.9.2-序列演算.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.9.3-归纳证明与递归原理.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.9.4-自动化证明与策略.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.8.5-Curry-Howard对应.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.8.4-Martin-Löf类型论.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.8.4.1-归纳类型分类.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.8.4.1.1-W类型与递归类型.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.12.4-HoTT在Lean及数学中的应用.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.11.1.1-单位范畴与对偶范畴.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.9.3.1-结构归纳法与数学归纳法.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.8.1-简单类型理论.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.8.2-依赖类型理论.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.12.4.1-HoTT在代数拓扑与几何中的应用.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.1-lean-理论基础与语义模型.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.5-lean-与主流语言对比.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.6-lean-工程案例与应用.md`（新增规范对齐/版本兼容性/参考资料）
- [x] `semantic/1-lean-grammar-and-semantics/1.7-lean-生态与工具链.md`（新增规范对齐/版本兼容性/参考资料）
- [x] 新增模板：`semantic/_TEMPLATE-WIKI-STYLE.md`（维基风格+Lean4 2025规范统一模板）

---

## 待处理主题（自动递归扫描中）

- [ ] 剩余中大型文件（1.5KB+）的"2025 规范对齐"小节补充
- [ ] 批量英文镜像与交叉引用优化
- [ ] Latex 公式与 Lean 代码示例可编译性抽测

---

## 断点恢复说明

- 每次自动处理后，更新本进度文档（本节）。
- 若进程中断，重新执行时自动读取本文件，恢复未完成主题。
- 人工可随时补充/调整待处理主题列表。

---

## 当前处理状态

- [x] 新一轮递归扫描与主题筛选（v2025-01 基线）
- [x] 维基风格模板落地与示例页对齐
- [x] Lean4 2025 规范差异点梳理与代码示例替换
- [x] 短小文件（1KB左右）批量标准化（已完成35个文件）
- [x] 中大型文件"2025 规范对齐"补充（已完成核心文件）
- [x] 剩余中大型文件"2025 规范对齐"补充（已完成3个文件）
- [ ] 批量应用至所有子页并抽测可编译性

---

> 本文档由AI自动维护，用于持续性递归梳理与断点恢复。
