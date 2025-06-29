# 03. 代数结构 (Algebraic Structures)

## 概述

代数结构是数学的核心概念，为理解数学对象的运算和关系提供了系统性的框架。本章节基于 `/Matter/Mathematics` 目录下的内容，结合现代代数理论，构建完整的代数结构分析体系。

## 目录

1. [群论基础](#1-群论基础)
2. [环论与域论](#2-环论与域论)
3. [模论](#3-模论)
4. [代数几何](#4-代数几何)
5. [李代数](#5-李代数)
6. [代数拓扑](#6-代数拓扑)
7. [表示论](#7-表示论)
8. [代数数论](#8-代数数论)

---

## 1. 群论基础

### 1.1 群的定义

**定义 1.1.1** (群)
群G是一个集合，配备二元运算·，满足：
1. 结合律：(a·b)·c = a·(b·c)
2. 单位元：存在e ∈ G，使得e·a = a·e = a
3. 逆元：对每个a ∈ G，存在a⁻¹ ∈ G，使得a·a⁻¹ = a⁻¹·a = e

**形式化表示**：

```lean
-- 群的定义
structure Group where
  carrier : Type u
  mul : carrier → carrier → carrier
  one : carrier
  inv : carrier → carrier
  associativity : ∀ (a b c : carrier), mul (mul a b) c = mul a (mul b c)
  identity_law : ∀ (a : carrier), mul one a = a ∧ mul a one = a
  inverse_law : ∀ (a : carrier), mul a (inv a) = one ∧ mul (inv a) a = one

-- 群的阶
def group_order (G : Group) : Nat :=
  Cardinal.mk G.carrier

-- 元素的阶
def element_order {G : Group} (g : G.carrier) : Nat :=
  if g = G.one then 1 else
  Nat.find (λ n => mul_power G g n = G.one)
```

### 1.2 子群与正规子群

**定义 1.2.1** (子群)
群G的子群H是G的子集，在G的运算下构成群。

**定义 1.2.2** (正规子群)
子群N ⊴ G，如果对每个g ∈ G，gNg⁻¹ ⊆ N。

**形式化表示**：

```lean
-- 子群
structure Subgroup (G : Group) where
  carrier : Set G.carrier
  contains_one : G.one ∈ carrier
  closed_under_mul : ∀ (a b : G.carrier), a ∈ carrier → b ∈ carrier → G.mul a b ∈ carrier
  closed_under_inv : ∀ (a : G.carrier), a ∈ carrier → G.inv a ∈ carrier

-- 正规子群
def is_normal_subgroup {G : Group} (H : Subgroup G) : Prop :=
  ∀ (g : G.carrier) (h : G.carrier), h ∈ H.carrier → 
  G.mul (G.mul g h) (G.inv g) ∈ H.carrier

-- 商群
def quotient_group {G : Group} (N : Subgroup G) (h : is_normal_subgroup N) : Group :=
  { carrier := G.carrier // λ a b => G.mul a (G.inv b) ∈ N.carrier,
    mul := λ [a] [b] => [G.mul a b],
    one := [G.one],
    inv := λ [a] => [G.inv a],
    associativity := quotient_associativity,
    identity_law := quotient_identity_law,
    inverse_law := quotient_inverse_law }
```

### 1.3 群同态

**定义 1.3.1** (群同态)
群同态φ : G → H是保持群运算的函数：
φ(ab) = φ(a)φ(b)

**形式化表示**：

```lean
-- 群同态
structure GroupHomomorphism (G H : Group) where
  map : G.carrier → H.carrier
  preserves_mul : ∀ (a b : G.carrier), 
    map (G.mul a b) = H.mul (map a) (map b)
  preserves_one : map G.one = H.one

-- 同态的核
def kernel {G H : Group} (φ : GroupHomomorphism G H) : Subgroup G :=
  { carrier := { g : G.carrier | φ.map g = H.one },
    contains_one := φ.preserves_one,
    closed_under_mul := kernel_closed_under_mul φ,
    closed_under_inv := kernel_closed_under_inv φ }

-- 同态的像
def image {G H : Group} (φ : GroupHomomorphism G H) : Subgroup H :=
  { carrier := { h : H.carrier | ∃ g : G.carrier, φ.map g = h },
    contains_one := ⟨G.one, φ.preserves_one⟩,
    closed_under_mul := image_closed_under_mul φ,
    closed_under_inv := image_closed_under_inv φ }
```

---

## 2. 环论与域论

### 2.1 环的定义

**定义 2.1.1** (环)
环R是一个集合，配备两个二元运算+和·，满足：
1. (R, +)是阿贝尔群
2. (R, ·)是幺半群
3. 分配律：a·(b+c) = a·b + a·c 和 (a+b)·c = a·c + b·c

**形式化表示**：

```lean
-- 环的定义
structure Ring where
  carrier : Type u
  add : carrier → carrier → carrier
  mul : carrier → carrier → carrier
  zero : carrier
  one : carrier
  neg : carrier → carrier
  add_assoc : ∀ (a b c : carrier), add (add a b) c = add a (add b c)
  add_comm : ∀ (a b : carrier), add a b = add b a
  add_zero : ∀ (a : carrier), add a zero = a
  add_neg : ∀ (a : carrier), add a (neg a) = zero
  mul_assoc : ∀ (a b c : carrier), mul (mul a b) c = mul a (mul b c)
  mul_one : ∀ (a : carrier), mul a one = a ∧ mul one a = a
  distrib_left : ∀ (a b c : carrier), mul a (add b c) = add (mul a b) (mul a c)
  distrib_right : ∀ (a b c : carrier), mul (add a b) c = add (mul a c) (mul b c)

-- 环的特征
def ring_characteristic (R : Ring) : Nat :=
  if ∃ n : Nat, n > 0 ∧ ∀ a : R.carrier, mul_power R a n = R.zero then
    Nat.find (λ n => n > 0 ∧ ∀ a : R.carrier, mul_power R a n = R.zero)
  else 0
```

### 2.2 理想与商环

**定义 2.2.1** (理想)
环R的理想I是R的子集，满足：
1. (I, +)是(R, +)的子群
2. 对每个r ∈ R和i ∈ I，r·i ∈ I和i·r ∈ I

**形式化表示**：

```lean
-- 理想
structure Ideal (R : Ring) where
  carrier : Set R.carrier
  contains_zero : R.zero ∈ carrier
  closed_under_add : ∀ (a b : R.carrier), a ∈ carrier → b ∈ carrier → R.add a b ∈ carrier
  closed_under_neg : ∀ (a : R.carrier), a ∈ carrier → R.neg a ∈ carrier
  absorbs_mul_left : ∀ (r : R.carrier) (i : R.carrier), i ∈ carrier → R.mul r i ∈ carrier
  absorbs_mul_right : ∀ (r : R.carrier) (i : R.carrier), i ∈ carrier → R.mul i r ∈ carrier

-- 商环
def quotient_ring {R : Ring} (I : Ideal R) : Ring :=
  { carrier := R.carrier // λ a b => R.add a (R.neg b) ∈ I.carrier,
    add := λ [a] [b] => [R.add a b],
    mul := λ [a] [b] => [R.mul a b],
    zero := [R.zero],
    one := [R.one],
    neg := λ [a] => [R.neg a],
    add_assoc := quotient_add_assoc,
    add_comm := quotient_add_comm,
    add_zero := quotient_add_zero,
    add_neg := quotient_add_neg,
    mul_assoc := quotient_mul_assoc,
    mul_one := quotient_mul_one,
    distrib_left := quotient_distrib_left,
    distrib_right := quotient_distrib_right }
```

### 2.3 域的定义

**定义 2.3.1** (域)
域F是一个环，其中非零元素在乘法下构成群。

**形式化表示**：

```lean
-- 域的定义
structure Field extends Ring where
  mul_inv : ∀ (a : carrier), a ≠ zero → ∃ b : carrier, mul a b = one ∧ mul b a = one

-- 域的特征
def field_characteristic (F : Field) : Nat :=
  ring_characteristic F.toRing

-- 素域
def prime_field (F : Field) : Field :=
  if field_characteristic F = 0 then
    rational_field
  else
    finite_field (field_characteristic F)
```

---

## 3. 模论

### 3.1 模的定义

**定义 3.1.1** (模)
环R上的左模M是一个阿贝尔群，配备标量乘法R × M → M，满足：
1. (r+s)·m = r·m + s·m
2. r·(m+n) = r·m + r·n
3. (rs)·m = r·(s·m)
4. 1·m = m

**形式化表示**：

```lean
-- 左模
structure LeftModule (R : Ring) where
  carrier : Type u
  add : carrier → carrier → carrier
  zero : carrier
  neg : carrier → carrier
  scalar_mul : R.carrier → carrier → carrier
  add_assoc : ∀ (a b c : carrier), add (add a b) c = add a (add b c)
  add_comm : ∀ (a b : carrier), add a b = add b a
  add_zero : ∀ (a : carrier), add a zero = a
  add_neg : ∀ (a : carrier), add a (neg a) = zero
  scalar_distrib_left : ∀ (r s : R.carrier) (m : carrier), 
    scalar_mul (R.add r s) m = add (scalar_mul r m) (scalar_mul s m)
  scalar_distrib_right : ∀ (r : R.carrier) (m n : carrier), 
    scalar_mul r (add m n) = add (scalar_mul r m) (scalar_mul r n)
  scalar_assoc : ∀ (r s : R.carrier) (m : carrier), 
    scalar_mul (R.mul r s) m = scalar_mul r (scalar_mul s m)
  scalar_one : ∀ (m : carrier), scalar_mul R.one m = m

-- 自由模
def free_module (R : Ring) (X : Type u) : LeftModule R :=
  { carrier := X →₀ R.carrier,  -- 有限支持的函数
    add := λ f g => λ x => R.add (f x) (g x),
    zero := λ x => R.zero,
    neg := λ f => λ x => R.neg (f x),
    scalar_mul := λ r f => λ x => R.mul r (f x),
    add_assoc := free_module_add_assoc,
    add_comm := free_module_add_comm,
    add_zero := free_module_add_zero,
    add_neg := free_module_add_neg,
    scalar_distrib_left := free_module_scalar_distrib_left,
    scalar_distrib_right := free_module_scalar_distrib_right,
    scalar_assoc := free_module_scalar_assoc,
    scalar_one := free_module_scalar_one }
```

### 3.2 模同态

**定义 3.2.1** (模同态)
模同态φ : M → N是保持模运算的函数：
φ(rm + sn) = rφ(m) + sφ(n)

**形式化表示**：

```lean
-- 模同态
structure ModuleHomomorphism {R : Ring} (M N : LeftModule R) where
  map : M.carrier → N.carrier
  preserves_add : ∀ (m n : M.carrier), 
    map (M.add m n) = N.add (map m) (map n)
  preserves_zero : map M.zero = N.zero
  preserves_scalar : ∀ (r : R.carrier) (m : M.carrier), 
    map (M.scalar_mul r m) = N.scalar_mul r (map m)

-- 模的直和
def direct_sum {R : Ring} {ι : Type u} (M : ι → LeftModule R) : LeftModule R :=
  { carrier := (i : ι) → M i,
    add := λ f g => λ i => (M i).add (f i) (g i),
    zero := λ i => (M i).zero,
    neg := λ f => λ i => (M i).neg (f i),
    scalar_mul := λ r f => λ i => (M i).scalar_mul r (f i),
    add_assoc := direct_sum_add_assoc,
    add_comm := direct_sum_add_comm,
    add_zero := direct_sum_add_zero,
    add_neg := direct_sum_add_neg,
    scalar_distrib_left := direct_sum_scalar_distrib_left,
    scalar_distrib_right := direct_sum_scalar_distrib_right,
    scalar_assoc := direct_sum_scalar_assoc,
    scalar_one := direct_sum_scalar_one }
```

---

## 4. 代数几何

### 4.1 代数簇

**定义 4.1.1** (代数簇)
代数簇是多项式方程组的零点集。

**形式化表示**：

```lean
-- 仿射代数簇
def affine_variety (k : Field) (n : Nat) (S : Set (polynomial k n)) : 
  Set (vector k n) :=
  { x : vector k n | ∀ f ∈ S, polynomial_eval f x = k.zero }

-- 射影代数簇
def projective_variety (k : Field) (n : Nat) (S : Set (homogeneous_polynomial k n)) :
  Set (projective_space k n) :=
  { [x] : projective_space k n | ∀ f ∈ S, homogeneous_polynomial_eval f x = k.zero }

-- 簇的坐标环
def coordinate_ring {k : Field} {n : Nat} (V : Set (vector k n)) : Ring :=
  quotient_ring (vanishing_ideal V)
```

### 4.2 概形

**定义 4.2.1** (概形)
概形是代数几何的基本对象，局部同构于仿射概形。

**形式化表示**：

```lean
-- 仿射概形
def affine_scheme (R : Ring) : Scheme :=
  { underlying_space := Spec R,
    structure_sheaf := structure_sheaf_of_rings R,
    local_affine := λ x => ⟨R, affine_open_around x⟩ }

-- 概形的态射
structure SchemeMorphism (X Y : Scheme) where
  continuous_map : X.underlying_space → Y.underlying_space
  sheaf_morphism : sheaf_morphism Y.structure_sheaf 
    (pushforward_sheaf X.structure_sheaf continuous_map)
```

---

## 5. 李代数

### 5.1 李代数的定义

**定义 5.1.1** (李代数)
李代数g是一个向量空间，配备李括号[·,·]，满足：
1. 双线性性
2. 反对称性：[x,y] = -[y,x]
3. 雅可比恒等式：[x,[y,z]] + [y,[z,x]] + [z,[x,y]] = 0

**形式化表示**：

```lean
-- 李代数
structure LieAlgebra (k : Field) where
  carrier : Type u
  add : carrier → carrier → carrier
  scalar_mul : k.carrier → carrier → carrier
  bracket : carrier → carrier → carrier
  vector_space_axioms : vector_space_axioms k carrier add scalar_mul
  bracket_bilinear : ∀ (a b c : carrier) (r : k.carrier),
    bracket (add a b) c = add (bracket a c) (bracket b c) ∧
    bracket a (add b c) = add (bracket a b) (bracket a c) ∧
    bracket (scalar_mul r a) b = scalar_mul r (bracket a b) ∧
    bracket a (scalar_mul r b) = scalar_mul r (bracket a b)
  bracket_antisymmetric : ∀ (a b : carrier), bracket a b = neg (bracket b a)
  jacobi_identity : ∀ (a b c : carrier),
    add (bracket a (bracket b c)) 
        (add (bracket b (bracket c a)) (bracket c (bracket a b))) = zero

-- 李代数的表示
structure LieAlgebraRepresentation {k : Field} (g : LieAlgebra k) (V : vector_space k) where
  action : g.carrier → (V.carrier → V.carrier)
  linear_action : ∀ (x : g.carrier), linear_transformation V V (action x)
  bracket_action : ∀ (x y : g.carrier),
    action (g.bracket x y) = 
    compose_linear (action x) (action y) - compose_linear (action y) (action x)
```

---

## 6. 代数拓扑

### 6.1 同伦论

**定义 6.1.1** (同伦)
两个连续映射f,g : X → Y同伦，如果存在连续映射H : X × I → Y，
使得H(x,0) = f(x)和H(x,1) = g(x)。

**形式化表示**：

```lean
-- 同伦
def homotopy {X Y : TopologicalSpace} (f g : continuous_map X Y) : Prop :=
  ∃ (H : continuous_map (product_space X unit_interval) Y),
  ∀ (x : X.carrier), 
    H.map (x, 0) = f.map x ∧ H.map (x, 1) = g.map x

-- 同伦等价
def homotopy_equivalence {X Y : TopologicalSpace} : Prop :=
  ∃ (f : continuous_map X Y) (g : continuous_map Y X),
  homotopy (compose_continuous g f) (identity_map X) ∧
  homotopy (compose_continuous f g) (identity_map Y)

-- 基本群
def fundamental_group (X : TopologicalSpace) (x₀ : X.carrier) : Group :=
  { carrier := homotopy_classes_of_loops X x₀,
    mul := loop_concatenation,
    one := constant_loop x₀,
    inv := loop_inverse,
    associativity := loop_associativity,
    identity_law := loop_identity_law,
    inverse_law := loop_inverse_law }
```

### 6.2 同调论

**定义 6.2.1** (奇异同调)
奇异同调群H_n(X)是拓扑空间X的代数不变量。

**形式化表示**：

```lean
-- 奇异链群
def singular_chain_group (X : TopologicalSpace) (n : Nat) : AbelianGroup :=
  free_abelian_group (singular_simplices X n)

-- 边界算子
def boundary_operator {X : TopologicalSpace} (n : Nat) :
  group_homomorphism (singular_chain_group X n) (singular_chain_group X (n-1)) :=
  { map := singular_boundary_map,
    preserves_add := boundary_preserves_add,
    preserves_zero := boundary_preserves_zero }

-- 同调群
def homology_group (X : TopologicalSpace) (n : Nat) : AbelianGroup :=
  quotient_group (kernel (boundary_operator n)) (image (boundary_operator (n+1)))
```

---

## 7. 表示论

### 7.1 群表示

**定义 7.1.1** (群表示)
群G的表示是群同态ρ : G → GL(V)。

**形式化表示**：

```lean
-- 群表示
structure GroupRepresentation {k : Field} (G : Group) (V : vector_space k) where
  action : G.carrier → (V.carrier → V.carrier)
  linear_action : ∀ (g : G.carrier), linear_transformation V V (action g)
  group_action : ∀ (g h : G.carrier),
    action (G.mul g h) = compose_linear (action g) (action h)
  identity_action : action G.one = identity_linear V

-- 不可约表示
def irreducible_representation {k : Field} {G : Group} {V : vector_space k}
  (ρ : GroupRepresentation G V) : Prop :=
  ∀ (W : vector_subspace V), 
    (∀ (g : G.carrier) (w : W.carrier), ρ.action g w ∈ W) →
    W = zero_subspace ∨ W = full_subspace V

-- 表示的直和
def direct_sum_representation {k : Field} {G : Group} 
  {V₁ V₂ : vector_space k} 
  (ρ₁ : GroupRepresentation G V₁) (ρ₂ : GroupRepresentation G V₂) :
  GroupRepresentation G (direct_sum_vector_space V₁ V₂) :=
  { action := λ g => direct_sum_linear (ρ₁.action g) (ρ₂.action g),
    linear_action := direct_sum_linear_action,
    group_action := direct_sum_group_action,
    identity_action := direct_sum_identity_action }
```

---

## 8. 代数数论

### 8.1 代数数域

**定义 8.1.1** (代数数域)
代数数域是Q的有限扩张。

**形式化表示**：

```lean
-- 代数数域
structure AlgebraicNumberField where
  base_field : Field  -- 有理数域Q
  extension_field : Field
  embedding : field_embedding base_field extension_field
  finite_degree : finite_extension_degree base_field extension_field

-- 代数整数
def algebraic_integer (K : AlgebraicNumberField) : Set K.extension_field.carrier :=
  { α : K.extension_field.carrier | 
    ∃ (f : polynomial K.base_field.carrier), 
    monic_polynomial f ∧ polynomial_root f α }

-- 整环
def ring_of_integers (K : AlgebraicNumberField) : Ring :=
  { carrier := algebraic_integer K,
    add := λ a b => K.extension_field.add a b,
    mul := λ a b => K.extension_field.mul a b,
    zero := K.extension_field.zero,
    one := K.extension_field.one,
    neg := λ a => K.extension_field.neg a,
    add_assoc := ring_of_integers_add_assoc,
    add_comm := ring_of_integers_add_comm,
    add_zero := ring_of_integers_add_zero,
    add_neg := ring_of_integers_add_neg,
    mul_assoc := ring_of_integers_mul_assoc,
    mul_one := ring_of_integers_mul_one,
    distrib_left := ring_of_integers_distrib_left,
    distrib_right := ring_of_integers_distrib_right }
```

---

## 总结

代数结构为数学提供了系统性的框架，从基础的群、环、域到高级的代数几何、李代数、表示论等，形成了完整的代数理论体系。通过严格的公理化方法和形式化表示，代数结构为理解数学对象的运算和关系提供了深刻的洞察。

**关键贡献**：

1. **统一框架**：为数学对象提供统一的代数框架
2. **结构分类**：系统性地分类数学结构
3. **运算理论**：深入研究运算的性质和规律
4. **应用广泛**：在多个领域有重要应用

**理论价值**：

- 为现代数学提供理论基础
- 促进数学各分支的统一
- 推动跨学科研究发展
- 为计算机科学提供数学基础

---

**参考文献**：

1. Dummit, D. S., & Foote, R. M. (2004). Abstract Algebra. Wiley.
2. Lang, S. (2002). Algebra. Springer.
3. Hungerford, T. W. (1974). Algebra. Springer.
4. Artin, M. (2011). Algebra. Pearson.
5. Jacobson, N. (2009). Basic Algebra I. Dover Publications.

---

**相关链接**：

- [01_集合论基础](./01_Set_Theory_Foundation.md)
- [02_范畴论基础](./02_Category_Theory_Foundation.md)
- [04_拓扑学基础](./04_Topology_Foundation.md)
- [01_理论基础](../01_Theoretical_Foundation/README.md)

---

**最后更新**: 2024年12月19日  
**版本**: v1.0  
**维护者**: AI Assistant  
**状态**: 持续更新中 