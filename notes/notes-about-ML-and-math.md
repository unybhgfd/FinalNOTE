## 数理逻辑

### 各种条件：

* **充分不必要条件**：$P$ 是 $Q$ 的这个条件，就是说 $P \Rightarrow Q$ 且 $Q \not\Rightarrow P$（**充分条件**）。

* **必要不充分条件**：$P$ 是 $Q$ 的这个条件，就是说 $P \not\Rightarrow Q$ 且 $Q \Rightarrow P$（**必要条件**）。

* **充分必要条件**：$P$ 是 $Q$ 的这个条件，就是说 $P \Rightarrow Q$ 且 $Q \Rightarrow P$（**充要条件**）。

* **不充分不必要条件**：$P$ 是 $Q$ 的这个条件，就是说 $P \not\Rightarrow Q$ 且 $Q \not\Rightarrow P$（**既不充分也不必要条件**）。

* 充分就是由 $P$ 能推出 $Q$，必要就是反过来可以。

* 这里 $P$ 和 $Q$ 都应该是小写，但是小写容易弄混故改成大写。

### 两个量词

定义略，这里只说格式。

* 全称量词：$\forall x \in M, p(x)$。
* 存在量词：$\exist x_0 \in M, p(x_0)$。
* 逗号和 $\in M$ 可选。

## 映射

### $X \to Y$

设集合 $X$、$Y$，则可以定义集合间的映射 $\varphi: X \to Y$，表示 $\varphi$ 将一个 $X$ 中元素映射到一个 $Y$ 中元素。

### $x \mapsto f(x)$

若输入 $x$ 到这个映射，则输出为 $f(x)$。

这和上面那个 $\to$ 箭头可以一起用，如：$\varphi: \mathbb{R} \to \mathbb{R}, x \mapsto x^2$。这个式子表示：
* 该映射将一个实数映射为一个实数。
* 具体映射的规则是将每个 $x$ 映射为 $x^2$。

### 单射、满射、双射

首先，我们有一个映射 $\varphi: X \to Y$。

单射：映射 $\varphi$ 满足：对于 $X$ 中任意两个元素 $x$ 和 $x'$，若 $x \neq x'$ 则 $\varphi(x) \neq \varphi(x')$。

满射：映射 $\varphi$ 满足：对于$Y$ 中任一元素 $y$ 一定能找到一个或多个 $X$ 中元素 $x$ 满足 $\varphi(x) = y$。

双射：$\varphi$ 既是单射也是满射。这意味着，$\varphi$ 在集合 $X$ 和 $Y$ 间建立了一个一一对应的关系。

### 逆映射

映射 $\varphi: X \to Y$ 的逆映射 $\varphi^{-1}: Y \to X$ 对 $X$ 中任一元素 $x$ 满足关系 $\varphi^{-1}(\varphi(x)) = x$。

### 复合映射、映射的复合

该运算符合结合律，不符合交换律。定义略。

## 多元微积分

### 偏导数

有多元标量函数 $f(\mathbf x)$，其中 $\mathbf x = (x_1, x_2, \dots, x_n)$。我们定义偏导数

$$
\frac{\partial f}{\partial x_i}(\mathbf{x}) = \lim_{h \to 0}{\frac{f(x_1, \dots, x_i + h, \dots, x_n) - f(\mathbf{x})}{h}}
$$

### 梯度、Nabla 算子

有多元标量函数 $f(\mathbf x)$，其中 $\mathbf x = (x_1, x_2, \dots, x_n)$。

$f$ 在 $\mathbf{x}$ 处的梯度：

$$
\nabla f(\mathbf x) = \left[
   \frac{\partial f}{\partial x_1}(\mathbf x),
   \dots,
   \frac{\partial f}{\partial x_n}(\mathbf x)
\right]^\top
$$

上面的 $\nabla$ 叫作 Nabla 算子。

梯度向量指向高处，所以梯度下降时我们要将梯度向量减去梯度乘学习率。

在约束优化，我们还会见到 $\nabla_\mathbf{x}\mathcal{L}(\mathbf{x}^*, \bm{\lambda}^*)$ 这种形式，首先函数 $\mathcal{L}(\mathbf{x}, \bm{\lambda})$ 两个输入都是向量，这个式子是说将 $\mathcal{L}$ 视为关于 $\mathbb{x}$ 的函数（参数 $\bm\lambda$ 固定，不再作为输入），对新的函数求偏导。

## 约束优化

### 约束优化的形式化表述

$$
\begin{aligned}
\min_{\mathbf{x} \in \mathbb{R}^n} \quad & f(\mathbf{x}) \\
\text{subject to:} \quad & g_i(\mathbf{x}) \le 0, \quad i = 1, \dots, m \\
& h_j(\mathbf{x}) = 0, \quad j = 1, \dots, p
\end{aligned} \\
$$

其中：
* （**目标函数**）$f(\mathbf{x})$ 是我们要**最小化**的目标函数。
* （**优化变量**）$\mathbf{x}$ 是 $n$ 维的优化变量。
* $g_i(\mathbf{x}) \le 0$ 是 $m$ 个不等式约束。
* $h_j(\mathbf{x})$ 是 $p$ 个等式约束。

注意，这里 $\mathbf x$ 一般是向量。

**s.t.**：subject to 后面是要满足的条件，subject to 也写作 $\text{s.t.}$（使得）。

**可行域**：所有满足这些约束条件的点 $\mathbb{x}$ 组成的集合被称为可行域，记作 $\mathcal{F} = \{ x \in \mathbb{R}^n \mid \forall i, g_i(x) \le 0 \,且\, \forall j, h_j(x) = 0 \}$。

约束优化就是在 $\mathcal{F}$ 中找到 $\argmin f(x)$。

### LICQ

> **线性无关约束规范** / **线性独立约束品性**。

LICQ 是相对于所有的等式/不等式约束和点 $\mathbf{x}^*$ 说的，它要求向量组

$$
\{\nabla g_i(\mathbf{x}^*)\mid i\in\mathcal{A}(\mathbf{x}^*)\}\cup\{\nabla h_j(\mathbf{x}^*)\mid j=1,\dots,p\}
$$

线性无关。其中：
* $\mathcal{A}(\mathbf{x}^*)=\{i\mid g_i(\mathbf{x}^*)=0\}$ 是所有起作用的不等式的“编号”集合，或者叫积极约束指标集。
* **起作用约束**：起作用约束是相对于所有不等式约束和点 $\mathbf{x}^*$ 说的，意思就是 $g_i(\mathbf{x}^*)=0$。

**正则点**：能使 LICQ 成立的点叫正则点。

可以将那个向量组看作点 $\mathbf{x}^*$ “碰到”的约束的“法向量”集合，对于不等式约束，法向量指向不可行区域。

### 拉格朗日乘子法（拉格朗日乘数法）

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
\mathcal{L}(\mathbf{x}, \bm{\lambda}) = f(\mathbf{x}) - \sum_{j=1}^p \lambda_j h_j(\mathbf{x}) \\
$$

其中：
* $\bm{\lambda}$是拉格朗日乘子向量。

我们发现，$\nabla_\mathbf{x}\mathcal{L}(\mathbf{x}^*, \bm{\lambda}^*) = \mathbf{0}$ 这个条件等价于上面的 $(1)$ 式，且 $\frac{\partial\mathcal{L}}{\partial\lambda_j}(\mathbf{x}^*, \bm{\lambda}^*) = 0$ 等价于 $h_j(\mathbf{x}^*) = 0$。这两个条件同时成立

## 信息论

这里 $\log$ 函数底数默认是 $2$。

对于随机变量，我们一般**只考虑**离散型随机变量。

### 自信息

对于一个**离散型**随机变量 $X$ 的一个特定取值 $x$，它的自信息定义为：

$$
I(x) = -\log P(x)
$$

其中 $P(x)$ 指的是事件 $X=x$ 发生的概率。

自信息可以理解为随机事件发生的“惊讶度”：概率为 $1$ 惊讶度为 $0$，概率越小惊讶度就越高，而不可能事件的发生有无限大的惊讶度。

### 熵（香农熵）

香农熵是随机事件的所谓“平均惊讶度”，即自信息的期望：

$$
H(X) = E[I(X)] = \sum_i I(x_i)P(x_i)
$$

### 交叉熵

对于事件 $X=x$（$x$ 所有可能的取值集合为 $\mathcal{X}$），我们有这个事件的真实概率（或者说真实的分布函数）$p(x)$ 和模型预测的概率$q(x)$，它们的交叉熵定义为：

$$
H(p, q) = -\sum_{x \in \mathcal{X}} p(x) \cdot \log q(x)
$$

### KL散度

假设对离散型随机变量 $X$，存在两个概率分布 $P$、$Q$，**从** $P$ **到** $Q$ 的 KL 散度定义的推导如下：

$$
\begin{aligned}
D_\text{KL}(P \Vert Q)
&= \sum_{x} \text{ExcessSurprise}(x) \cdot P(x)                                            &\text{ExcessSurprise 是分布 Q 下比分布 P 下多出的惊讶度} \\
&= \sum_{x} \left[ \text{Surprise}_Q(x) - \text{Surprise}_P(x) \right] \cdot P(x)          &\text{定义“额外惊讶度”为两分布下惊讶度的差} \\
&= \sum_{x} \left[ \left( -\log Q(x) \right) - \left( -\log P(x) \right) \right] \cdot P(x)&\text{“惊讶度”即自信息，定义为概率的负对数} \\
&= \sum_{x} \left[ \log P(x) - \log Q(x) \right] \cdot P(x)                                &\text{去括号化简} \\
&= \sum_{x} \log \frac{P(x)}{Q(x)} \cdot P(x)                                              &\text{利用对数的性质继续化简} \\
\end{aligned}
$$

它描述了用 $Q$ 近似 $P$ 时，“额外惊讶度”的期望，或者也可以理解为 $Q$ 到 $P$ 的“信息损失”。

性质：
* 非对称性：$D_\text{KL}(p \Vert q) \not= D_\text{KL}(q \Vert p)$。
* 非负性：若对于所有 $x$ 都存在 $p(x) = q(x)$ 则 $D_\text{KL}(p \Vert q) = 0$，否则 $D_\text{KL}(p \Vert q) > 0$

#### KL 散度与交叉熵、熵的关系

对随机变量 $X$ 存在两个概率分布 $p$、$q$，KL 散度可以拆解为交叉熵和熵的差：

$$
D_\text{KL}(p \Vert q) = H(p, q) - H(p)
$$

## 混淆矩阵

**混淆矩阵（Confusion Matrix）**：这是分类问题中一个 $N \times N$ 的矩阵，其中 $N$ 是分类标签的个数。矩阵的一行是真实类别，

### 二分类问题

我们首先把两个标签称为“正”和“负”，预测值为正就叫阳性，否则就是阴性，和真实值相符就是真阳性/真阴性，不符就是假阳性/假阴性。

### 多分类问题

对于多分类问题，阴性和阳性不是固定的，我们一般把一个标签定位阳性其他就都是阴性，这种方法被称为 One-vs-Rest 策略。

### 各种评估指标

### 准确率和错误率

**准确率（Accuracy）**、**正确率**：$\frac{TP + TN}{n}$，预测和真实值相符的比率，这里样本总数 $n=TP + TN + FP + FN$，下同。

**错误率（Error Rate）**：$\frac{FP + FN}{n}$，预测和真实值*不*符的比率，或者说 $1$ 减去准确率。

### 真阳率、真阴率、假阳率、假阴率

**精确率（Precision）**、**查准率**：$\frac{TP}{TP + FP}$，预测为正的样本中正确的比率.

**召回率（Recall）**、**查全率**：$\frac{TP}{TP + FN}$，所有真实值为正的样本中预测相符的比率

## 最大似然估计（MLE）

我们将模型表示为拟合真实数据分布 $p_\text{data}(\mathbf{x})$ 的函数 $p_\text{model}(\mathbf{x};\bm{\theta})$。这是个输入向量输出实数的函数，输入数据 $\mathbf{x}$ 预测它出现的概率（或概率密度），函数的具体行为由内部的算法以及参数 $\bm{\theta}$ 控制。

我们有m个 i.i.d.（独立同分布）样本的数据集（向量的集合） $\mathbb{X} = \{\bm{x}^{(1)}, \bm{x}^{(2)}, \dots, \bm{x}^{(m)}\}$，由 $p_\text{data}$ 生成。MLE 方法估计的“最佳”参数，即对 $\bm{\theta}$ 的最大似然估计定义为，能使得 $p_\text{model}$ 对 $\mathbb{X}$ 中预测的所有概率之积最大的参数：

$$
\bm\theta_\text{ML} = \argmax_{\bm\theta} p_\text{model}(\mathbb{X}; \bm\theta) \\
= \argmax_{\bm\theta} \prod_{i=1}^{m} p_\text{model}(\bm{x}^{(i)}; \bm\theta)
$$

连乘计算容易出现数值计算上的误差（下溢），我们加上个 $\log$ 函数让连乘变成求和，这样能降低误差，方便求导，同时不影响 $\argmax$：

$$
= \argmax_{\bm{\theta}} \log\left(
   \prod_{i=1}^{m} p_\text{model}(\bm{x}^{(i)}; \bm{\theta})
\right)
= \argmax_{\bm{\theta}} \sum_{i=1}^{m} \log p_\text{model}(\bm{x}^{(i)}; \bm{\theta})
$$

模型选择很重要，因为 MLE 只最大化训练样本的似然，并不直接约束模型对训练集外数据的预测。如果模型过于灵活，它很可能将训练集中未出现（但真实概率非零）的区域的概率推向 0，导致泛化能力弱。

## 最大后验估计（MAP）

相比于 MLE，MAP 将 $\bm{\theta}$ 视为参数空间上的随机变量，估计的是 $\bm{\theta}$ 在参数空间中的概率分布，而不是一个具体的值。除此之外，还加入了先验分布 $p(\bm\theta)$。先验分布一般偏好更“简单”的解。

和 MLE 的关系：

* 当样本数趋于无穷时，最大后验概率估计一般趋向于最大似然估计。

* 最大似然估计也可看作参数的先验概率密度函数服从均匀分布（相当于没有先验知识）的最大后验概率估计。

* 当参数的先验概率密度函数比较准确时，最大后验概率估计的小样本性质大大优于最大似然估计。

## 再生核希尔伯特空间（RKHS）

### 希尔伯特空间

这里只讨论由部分 $f: \mathbb{R}^N \to \mathbb R$ 构成的希尔伯特函数空间 $\mathcal H$。

如果说这些函数构成希尔伯特空间，则必须给出一个符合特定性质的内积运算，并且满足所有柯西序列收敛在空间内（完备性）。

内积：$$\left<f, g\right> = \int f(x)g(x) \,\mathrm d x$$

范数：$$\lVert f \rVert = \sqrt{\left< f, f \right>}$$

### RKHS

如果存在一个函数 $\kappa: \mathbb{R}^N \times \mathbb{R}^N \to \mathbb{R}$ 满足：

* 对于所有 $x \in \mathbb{R}^N$，$\kappa(\cdot, x) \in \mathcal H$；
* 对于所有 $f \in \mathcal H$ 和 $x \in \mathbb{R}^N$，$\left<f, \kappa(\cdot, x)\right> = f(x)$（可再生性）；

则称 $\mathcal H$ 为 RKHS，$\kappa$ 是 $\mathcal H$ 的再生核函数。

## 支持向量机（SVM）

超平面方程：

$$
\bm{w}^\top \bm{x} + b = 0
$$

支持向量机使用超平面（n 维空间中的 n - 1 维子空间）分类数据，平面一侧的点（$\bm{w}^\top \bm{x} + b > 0$）预测为正类，另一侧（$\bm{w}^\top \bm{x} + b < 0$）预测为负类。

性质：$\lVert\bm{w}\rVert$ 越大，更改 $b$ 值时平面移动的幅度越小（因为实质上这个方程是n+1维线性方程的截面，$\lVert\bm{w}\rVert$ 大时高维坡面更“陡峭”）。

线性可分：对于一个数据集，如果存在一个参数使得每个点，模型都能预测正确，则称这个数据集是线性可分的。

训练 SVM 时还需要两个平行的超平面：

* 正类边界：$\bm{w}^\top \bm{x} + b = 1$；
* 负类边界：$\bm{w}^\top \bm{x} + b = -1$。

训练时需要让正类不跑到两个边界之间（满足对于所有正类数据点 $\bm x$，$\bm{w}^\top \bm{x} + b >= 1$），负类同理

为了最大化模型的泛化能力，我们需要在不出错的情况下最大化这两个边界之间的距离（称作“间隔”，Margin）。根据超平面方程性质，就是最小化 $\lVert \bm w \rVert$。

最大化间隔后，正类/负类边界都会有数据点落在边界上，这些点就叫支持向量。

### SVM 的意义

Cover 定理指出，将复杂模式通过非线性映射投射到高维空间时，数据更容易线性可分。所以我们可以训练出那个非线性映射，映射后的数据点就可以运用 SVM 进行分类。

同时 SVM 的 loss 函数被证明是一个凸函数，所以只有一个最小值。
