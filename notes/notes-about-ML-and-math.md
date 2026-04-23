ML速查
by unybhgfd。
> 怎么个“速”呢？就是你用 Ctrl + F 全文搜索，输入“记号：”或者“定义：”，然后输入相关词就差不多能搜到。

# 机器学习

## 混淆矩阵

**定义：混淆矩阵（Confusion Matrix）**：这是分类问题中一个 $N \times N$ 的矩阵，其中 $N$ 是分类标签的个数。矩阵的一行是真实类别，

### 二分类问题

我们首先把两个标签称为“正”和“负”，预测值为正就叫阳性，否则就是阴性，和真实值相符就是真阳性/真阴性，不符就是假阳性/假阴性。

**定义：真阳性（True Positive，TP）**、**定义：真阴性（True Negetive，TN）**、**定义：假阳性（False Positive，FP）**、**定义：假阴性（False Negetive，FN）**。

### 多分类问题

对于多分类问题，阴性和阳性不是固定的，我们一般把一个标签定位阳性其他就都是阴性，这种方法被称为 One-vs-Rest 策略。（**定义：OvR策略**）

### 各种评估指标

### 准确率和错误率

**定义：准确率（Accuracy）**、**定义：正确率**：$\frac{TP + TN}{n}$，预测和真实值相符的比率，这里样本总数 $n=TP + TN + FP + FN$，下同。

**定义：错误率（Error Rate）**：$\frac{FP + FN}{n}$，预测和真实值*不*符的比率，或者说 $1$ 减去准确率。

### 真阳率、真阴率、假阳率、假阴率

TODO(unybhgfd)：真阴率是啥阴？

**定义：精确率（Precision）**、**定义：查准率**：$\frac{TP}{TP + FP}$，预测为正的样本中正确的比率.

**定义：召回率（Recall）**、**定义：查全率**：$\frac{TP}{TP + FN}$，所有真实值为正的样本中预测相符的比率

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

## 多元微积分

### 定义：偏导数

有多元标量函数 $f(\mathbf x)$，其中 $\mathbf x = (x_1, x_2, \dots, x_n)$。我们定义偏导数

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

在约束优化，我们还会见到 $\nabla_\mathbf{x}\mathcal{L}(\mathbf{x}^*, \boldsymbol{\lambda}^*)$ 这种形式，首先函数 $\mathcal{L}(\mathbf{x}, \boldsymbol{\lambda})$ 两个输入都是向量，这个式子是说将 $\mathcal{L}$ 视为关于 $\mathbb{x}$ 的函数（参数 $\boldsymbol\lambda$ 固定，不再作为输入），对新的函数求偏导。

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
* （**定义：目标函数**）$f(\mathbf{x})$ 是我们要**最小化**的目标函数。
* （**定义：优化变量**）$\mathbf{x}$ 是 $n$ 维的优化变量。
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
* $\mathcal{A}(\mathbf{x}^*)=\{i\mid g_i(\mathbf{x}^*)=0\}$ 是所有起作用的不等式的“编号”集合，或者叫积极约束指标集。
* **定义：起作用约束**：起作用约束是相对于所有不等式约束和点 $\mathbf{x}^*$ 说的，意思就是 $g_i(\mathbf{x}^*)=0$。（**定义：紧约束**、**定义：积极约束**、**定义：有效约束**）

**定义：正则点**：能使 LICQ 成立的点叫正则点。

> 名字真多...

可以将那个向量组看作点 $\mathbf{x}^*$ “碰到”的约束的“法向量”集合，对于不等式约束，法向量指向不可行区域。

### 定义：拉格朗日乘子法（定义：拉格朗日乘数法）

> 我们全程不考虑不等式约束。

我们首先考虑只有一个等式约束 $h(\mathbf x^*) = 0$ 的情况。在满足等式约束的局部最优解 $\mathbf{x}^*$ 处，$\nabla f(\mathbf{x}^*)$ 和 $\nabla h(\mathbf{x}^*)$ 必须是平行的。

既然平行，那么肯定 $\exist \lambda \in \mathbb{R}, \nabla f(\mathbf{x}^*) = \lambda \nabla h(\mathbf{x}^*)$。这个标量 $\lambda$ 就叫拉格朗日乘子

> 为什么一定平行呢？我们可以用反证法证明：
> 如果不平行，那么沿着可行域切线方向移动，目标函数 $f$ 就会发生变化（增加或减少），从而找到了一个比 $\mathbf{x}^*$ 更好的可行点，这与 $\mathbf{x}^*$ 是局部最优点矛盾。为了消除这种改进的可能性，那两个梯度向量必须平行。

如果现在有多个等式约束 $h_j(\mathbf{x}) = 0, \quad j = 1, \dots, p$ ，并且最优点 $\mathbf{x}^*$ 是正则点（符合 LICQ 的点），那么存在一组拉格朗日乘子 $\lambda_1, \dots, \lambda_p$，使得和等式约束梯度的线性组合为目标函数梯度，即：

$$
\nabla f(\mathbf{x}^*) = \sum_{j=1}^p \lambda_j \nabla h_j(\mathbf{x}^*)
$$

移项：

$$
\nabla f(\mathbf{x}^*) - \sum_{j=1}^p \lambda_j \nabla h_j(\mathbf{x}^*) = \mathbf{0}  \tag{1}
$$

其中右边其实是一个零向量，我们就把他写成 $\mathbf{0}$。

我们构造拉格朗日函数 $\mathcal{L}$：

$$
\mathcal{L}(\mathbf{x}, \boldsymbol{\lambda}) = f(\mathbf{x}) - \sum_{j=1}^p \lambda_j h_j(\mathbf{x}) \\
$$

其中：
* $\boldsymbol{\lambda}$是拉格朗日乘子向量。

> 上式中减号有时也写作加号。

我们发现，$\nabla_\mathbf{x}\mathcal{L}(\mathbf{x}^*, \boldsymbol{\lambda}^*) = \mathbf{0}$ 这个条件等价于上面的 $(1)$ 式，且 $\frac{\partial\mathcal{L}}{\partial\lambda_j}(\mathbf{x}^*, \boldsymbol{\lambda}^*) = 0$ 等价于 $h_j(\mathbf{x}^*) = 0$。这两个条件同时成立
