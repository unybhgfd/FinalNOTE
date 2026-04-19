ML速查
by unybhgfd。
> 怎么个“速”呢？就是你用 Ctrl + F 全文搜索，输入“记号：”或者“定义：”，然后输入相关词就差不多能搜到。

# 机器学习

## 混淆矩阵

**定义：混淆矩阵**：这是分类问题中一个 $N \times N$ 的矩阵，其中 $N$ 是分类标签的个数。矩阵的一行是真实类别，

### 二分类问题中的混淆矩阵

我们首先把两个标签称为“正”和“负”，预测值为正就叫阳性，否则就是阴性，和真实值相符就是真阳性/真阴性，不符就是假阳性/假阴性。

# 数学

## 数理逻辑

### 各种条件：

* **定义：充分不必要条件**：$P$ 是 $Q$ 的这个条件，就是说 $P \Rightarrow Q$ 且 $Q \not\Rightarrow P$（**定义：充分条件**）。

* **定义：必要不充分条件**：$P$ 是 $Q$ 的这个条件，就是说 $P \not\Rightarrow Q$ 且 $Q \Rightarrow P$（**定义：必要条件**）。

* **定义：充分必要条件**：$P$ 是 $Q$ 的这个条件，就是说 $P \Rightarrow Q$ 且 $Q \Rightarrow P$（**定义：充要条件**）。

* **定义：不充分不必要条件**：$P$ 是 $Q$ 的这个条件，就是说 $P \not\Rightarrow Q$ 且 $Q \not\Rightarrow P$（**定义：既不充分也不必要条件**）。

* 充分就是由 $P$ 能推出 $Q$，必要就是反过来可以。

* 这里 $P$ 和 $Q$ 都应该是小写，但是小写容易弄混故改成大写。

### 两个量词

定义略，这里只说格式。

* 全称量词：$\forall x \in M, p(x)$。
* 存在量词：$\exist x_0 \in M, p(x_0)$。
* 逗号和 $\in M$ 可选。

## 映射

### 记号：$X \to Y$

设集合 $X$、$Y$，则可以定义集合间的映射 $\varphi: X \to Y$，表示 $\varphi$ 将一个 $X$ 中元素映射到一个 $Y$ 中元素。

### 记号：$x \mapsto f(x)$

若输入 $x$ 到这个映射，则输出为 $f(x)$。

这和上面那个 $\to$ 箭头可以一起用，如：$\varphi: \mathbb{R} \to \mathbb{R}, x \mapsto x^2$。这个式子表示：
* 该映射将一个实数映射为一个实数。
* 具体映射的规则是将每个 $x$ 映射为 $x^2$。

### 定义：单射、定义：满射、定义：双射

首先，我们有一个映射 $\varphi: X \to Y$。

单射：映射 $\varphi$ 满足：对于 $X$ 中任意两个元素 $x$ 和 $x'$，若 $x \neq x'$ 则 $\varphi(x) \neq \varphi(x')$。

满射：映射 $\varphi$ 满足：对于$Y$ 中任一元素 $y$ 一定能找到一个或多个 $X$ 中元素 $x$ 满足 $\varphi(x) = y$。

双射：$\varphi$ 既是单射也是满射。这意味着，$\varphi$ 在集合 $X$ 和 $Y$ 间建立了一个一一对应的关系。

### 定义：逆映射

映射 $\varphi: X \to Y$ 的逆映射 $\varphi^{-1}: Y \to X$ 对 $X$ 中任一元素 $x$ 满足关系 $\varphi^{-1}(\varphi(x)) = x$。

### 定义：复合映射、定义：映射的复合

该运算符合结合律，不符合交换律。定义略。

## 线性代数

### 定义：线性空间

线性空间 $V$ 是对其元素（称为向量或矢量）定义了向量加法 $V+V \to V$ 与数乘 $P \times V \to V$）的集合，两个运算满足八条运算规律。

这里的 $P$ 是数域，参与数乘的数属于数域 $P$。$P$ 可以说实数域 $\mathbb{R}$（一般只会用到这个）或复数域 $\mathbb{C}$ 等。

**定义：实线性空间**：上面的 $P = \mathbb{R}$ 时这个线性空间就叫实线性空间，是 $\mathbb{C}$就叫复线性空间。

八条运算规律：下面对 $V$ 中元素 $u, v, w$ 和 $P$ 中元素 $p, q$ 均成立：
1. 矢量加法的交换律：$u+v = v+u$。
2. 矢量加法的结合律：$u+(v+w) = (u+v)+w$。
3. 存在零元（即矢量加法的单位元）$\vec{0} \in V$ 使得 $u+\vec{0}=u$。
4. 存在矢量加法的逆元 $-u \in V$ 使得 $-u + u = \vec{0}$。
5. 存在数乘的单位元 $1$ 使得：$1u=u$。
6. 数乘与数域乘法相容：$(pq)u = p(qu)$。
7. 数乘对数域加法的分配律：$(p+q)u = pu+qu$。
8. 数乘对矢量加法的分配律：$p(u+v) = pu + pv$。

## 多元微积分

### 定义：偏导数

有多元标量函数 $f(\mathbf x)$，其中 $\mathbf x = (x_1, x_2, \dots, x_n)$。$f$ 在 $\mathbf{x}$ 处的偏导数：

$$
\frac{\partial f}{\partial x_i}(\mathbf{x}) = \lim_{h \to 0}{\frac{f(x_1, \dots, x_i + h, \dots, x_n) - f(\mathbf{x})}{h}}
$$

### 定义：梯度、定义：Nabla 算子

有多元标量函数 $f(\mathbf x)$，其中 $\mathbf x = (x_1, x_2, \dots, x_n)$。

$f$ 在 $\mathbf{x}$ 处的梯度：

$$
\nabla f(\mathbf x) = \left[
   \frac{\partial f}{\partial x_1}(\mathbf x),
   \dots,
   \frac{\partial f}{\partial x_n}(\mathbf x)
\right]^T
$$

上面的 $\nabla$ 叫作 Nabla 算子。

梯度向量指向高处，所以梯度下降时我们要将梯度向量减去梯度乘学习率。

## 约束优化

### 定义：约束优化的形式化表述

$$
\begin{aligned}
\min_{\mathbf{x} \in \mathbb{R}^n} \quad & f(\mathbf{x}) \\
\text{subject to:} \quad & g_i(\mathbf{x}) \le 0, \quad i = 1, \dots, m \\
& h_j(\mathbf{x}) = 0, \quad j = 1, \dots, p
\end{aligned} \\
$$

其中：
* $f(\mathbf{x})$ 是我们要最小化的目标函数。
* $\mathbf{x}$ 是 $n$ 维的优化变量。
* $g_i(\mathbf{x}) \le 0$ 是 $m$ 个不等式约束。
* $h_j(\mathbf{x})$ 是 $p$ 个等式约束。

注意，这里 $\mathbf x$ 一般是向量。

**记号：s.t.**：subject to 后面是要满足的条件，subject to 也写作 $\text{s.t.}$（使得）。

**定义：可行域**（**定义：可行集**）：所有满足这些约束条件的点 $\mathbb{x}$ 组成的集合被称为可行域，记作 $\mathcal{F} = \{ x \in \mathbb{R}^n \mid \forall i, g_i(x) \le 0 \,且\, \forall j, h_j(x) = 0 \}$。

约束优化就是在 $\mathcal{F}$ 中找到 $\argmin f(x)$。

### 定义：LICQ

> **定义：线性无关约束规范**、**定义：线性无关约束规格**、**定义：线性无关约束品性**、**定义：线性独立约束规范**、**定义：线性独立约束规格**、**定义：线性独立约束品性**。
> “线性无关”和“线性独立”一个意思，“规格”、“规约”和“品性”也是一个意思，既然 LICQ 中文译名又多又长，还是叫它 LICQ 得了。

LICQ 是相对于所有的等式/不等式约束和点 $\mathbf{x}^*$ 说的，它要求向量组

$$
\{\nabla g_i(\mathbf{x}^*)\mid i\in\mathcal{A}(\mathbf{x}^*)\}\cup\{\nabla h_j(\mathbf{x}^*)\mid j=1,\dots,p\}
$$

线性无关。其中：
* $\mathcal{A}(\mathbf{x}^*)=\{i\mid g_i(\mathbf{x}^*)=0\}$ 是所有起作用的不等式的“编号”集合，或者叫积极约束指标集，不起作用叫非积极约束指标集（**定义：积极约束指标集**、**定义：非积极约束指标集**）。
* **定义：起作用约束**：起作用约束是相对于所有不等式约束和点 $\mathbf{x}^*$ 说的，意思就是 $g_i(\mathbf{x}^*)=0$。

**定义：正则点**：能使 LICQ 成立的点叫正则点。

> 名字真多...

可以将那个向量组看作点 $\mathbf{x}^*$ “碰到”的约束的“法向量”集合，对于不等式约束，法向量指向不可行区域。
