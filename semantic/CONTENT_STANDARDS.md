# 内容与格式统一规范 / Content & Format Standards (v2025-01)

[返回目录](./CONTINUOUS_PROGRESS.md)

---

## 1. 文件头与编号 / Header & Numbering

- 标题必须包含严格编号与中英双语，如：`# 1.8 Curry-Howard 对应 / Curry-Howard Correspondence`。
- 页首导航统一：`[返回目录](../CONTINUOUS_PROGRESS.md) | [上一节: …](...) | [下一节: …](...)`。
- 章节编号从 0 开始用于导语与总述，主体从 1 起。

---

## 2. LaTeX 数学与符号 / LaTeX Math & Notation

- 行内：`\( ... \)`；行间：`\[ ... \]`。避免混用 `$`。
- 类型宇宙：`\(\mathrm{Type}_u\)`；命题层：`\(\mathrm{Prop}\)`；层级链：`\(\mathrm{Type}_0 : \mathrm{Type}_1 : \cdots\)`。
- Π/Σ：`\(\Pi_{x:A} B(x)\)`、`\(\Sigma_{x:A} B(x)\)`；函数：`\(A \to B\)`；等式：`\(=\)`；逻辑：`\(\land,\lor,\implies,\neg,\forall,\exists\)`。
- 证明风格：定理-引理-命题-定义分层；必要时给出“证明思路”。

---

## 3. 代码示例 / Code Examples

- 语言：Lean 4 为主；需要时可辅以 Haskell/Rust，但须标注语言。
- 示例须可编译；提供必要 `import`；避免伪接口；长示例折分为最小可运行单元。
- 证明与计算分离：`Prop` 证据不可计算；使用 `simp`、`aesop`、`linarith` 时给出上下文。

---

## 4. 维基结构 / Wiki Structure

- 强制章节：导语、术语、Lean4 对齐、语法、语义、示例、实践、兼容性、交叉引用、参考资料、变更记录。
- 图表使用 Mermaid；不得引用远程图片；只允许本地资源与数据 URI。
- 交叉引用使用相对路径与严格编号；避免冗余与重复内容，优先链接复用。

---

## 5. 交叉引用与索引 / Cross-refs & Index

- 每篇文档的“交叉引用”章节至少包含：上一节、下一节、上位主题、下位细分主题。
- 建立总索引 `INDEX.md`：以严格编号树展示全局结构；提供本地跳转。
- 根目录 `analysis/cross-reference-index.md` 作为外层汇总；语义内以 `INDEX.md` 为主。

---

## 6. 版本与发布 / Versioning & Release

- 统一在页尾给出：最后更新日期、版本号（如 `v2025-01`）、内容质量等级。
- 重大结构变更需在 `RELEASE_NOTES.md` 记录。

---

## 7. 质量基线 / Quality Baseline

- 结构完整性：强制包含 10 大章节。
- 可编译性：代码段在 Lean 4 编译通过。
- 一致性：术语、符号、风格与本规范一致。

---

## 8. 自动化约定 / Automation Conventions

- 后续将提供脚本，自动校验：编号、导航、交叉引用、LaTeX 与代码块格式。
- 生成/更新 `INDEX.md` 与各文件页首导航。
