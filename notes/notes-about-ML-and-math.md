## 数理逻辑

### 两个量词

* 全称量词：$\forall x \in M, p(x)$。
* 存在量词：$\exist x_0 \in M, p(x_0)$。

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

在约束优化，我们还会见到 $\nabla_\mathbf{x}\mathcal{L}(\mathbf{x}^*, \bm{\lambda}^*)$ 这种形式，首先函数 $\mathcal{L}(\mathbf{x}, \bm{\lambda})$ 两个输入都是向量，这个式子是说将 $\mathcal{L}$ 视为关于 $\mathbf{x}$ 的函数（参数 $\bm\lambda$ 固定，不再作为输入），对新的函数求偏导。

### 雅可比矩阵

对于一个非线性映射 $\bm f: \mathbb{R}^m \to \mathbb{R}^n$，对于点 $\bm x$ 和变换后的点 $\bm f(\bm x)$，我们定义类似导数的概念，将 $\bm x$ 附近的空间发生的变换（不关注空间发生的平移）近似为一个线性变换 $\bm{a} \mapsto \mathbf{J}\bm{a}$。这里的 $\mathbf J$ 就是 $\bm f$ 在 $\bm x$ 处的雅可比矩阵，定义为：

$$
J_{i, j} = \frac{\partial}{\partial x_j} \bm f(\bm x)_i
$$

### 海森矩阵

对于**向量到标量**的非线性映射 $f: \mathbb{R}^n \to \mathbb{R}$，定义海森矩阵，它扩展了二阶导的定义：

$$
\bm{H}(f)(\bm x)_{i, j} = \frac{\partial^2}{\partial x_j \partial x_i} f(\bm x)
$$

$\bm x$ 二阶偏导连续时，海森矩阵对称。

当点 $\bm x$ 处梯度为 0 时，可以用海森矩阵的特征值判定：
* 若所有特征值都大于 0，则为局部极小值；
* 若所有特征值都小于 0，则为局部极大值；
* 若存在正负混合，则为鞍点；
* 若有特征值为 0，需要更高阶分析或其他判定方法配合。

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

### 拉格朗日乘子法

> 我们全程不考虑不等式约束。

我们首先考虑只有一个等式约束 $h(\mathbf x^*) = 0$ 的情况。在满足等式约束的局部最优解 $\mathbf{x}^*$ 处，$\nabla f(\mathbf{x}^*)$ 和 $\nabla h(\mathbf{x}^*)$ 必须是平行的。

既然平行，那么肯定 $\exist \lambda \in \mathbb{R}, \nabla f(\mathbf{x}^*) = \lambda \nabla h(\mathbf{x}^*)$。这个标量 $\lambda$ 就叫拉格朗日乘子

> 为什么一定平行呢？我们可以用反证法证明：
> 如果不平行，那么沿着可行域切空间的某个方向移动，目标函数 $f$ 就会减少，从而找到了一个比 $\mathbf{x}^*$ 更好的可行点，这与 $\mathbf{x}^*$ 是局部最优点矛盾。为了消除这种改进的可能性，就必须平行。

如果现在有多个等式约束 $h_j(\mathbf{x}) = 0, \quad j = 1, \dots, p$ ，并且最优点 $\mathbf{x}^*$ 是正则点（符合 LICQ 的点），那么目标函数梯度向量方向一定和可行域切空间平行。就是说存在一组拉格朗日乘子 $\lambda_1, \dots, \lambda_p$，使得和等式约束梯度的线性组合为目标函数梯度，即：

$$
\nabla f(\mathbf{x}^*) = \sum_{j=1}^p \lambda_j \nabla h_j(\mathbf{x}^*)
$$

移项：

$$
\nabla f(\mathbf{x}^*) - \sum_{j=1}^p \lambda_j \nabla h_j(\mathbf{x}^*) = \mathbf{0}  \tag{1}
$$

我们构造拉格朗日函数 $\mathcal{L}$：

$$
\mathcal{L}(\mathbf{x}, \bm{\lambda}) = f(\mathbf{x}) - \sum_{j=1}^p \lambda_j h_j(\mathbf{x}) \\
$$

其中：
* $\bm{\lambda}$是拉格朗日乘子向量。

我们发现，$\nabla_\mathbf{x}\mathcal{L}(\mathbf{x}^*, \bm{\lambda}^*) = \mathbf{0}$ 这个条件等价于上面的 $(1)$ 式，且 $\frac{\partial\mathcal{L}}{\partial\lambda_j}(\mathbf{x}^*, \bm{\lambda}^*) = 0$ 等价于 $h_j(\mathbf{x}^*) = 0$。这两个条件同时成立时就能还原原来的等式约束条件。

所以，原始的等式约束优化问题的最优性条件通过拉格朗日函数可以转化为求解方程组：

$$
\nabla_\mathbf{x} \mathcal{L}(\mathbf{x}, \bm{\lambda}) = 0 \quad
\text{and} \quad
\nabla_{\bm{\lambda}} \mathcal{L}(\mathbf{x}, \bm{\lambda}) = 0
$$

方程解完还没结束，需要判断解是最小值、最大值还是鞍点。

### KKT 方法

KKT 方法是拉格朗日乘子法的推广，进一步考虑了不等式约束。

此时最优解可能在可行域边缘（存在一个或多个起作用的不等式约束）或在内部（$\forall i, g_i(\mathbf{x}) < 0$）。

如果 $\mathbf x^*$ 是局部最优解并且满足正则性条件，则存在一组 KKT 乘子：$\mu_1, \dots, \mu_m$ 对应不等式约束，$\lambda_1, \dots, \lambda_p$ 对应等式约束，满足以下四个条件：

#### 稳定性

$$
\nabla f(\mathbf x^*)
+ \sum_{i=1}^m \mu_i \nabla g_i(\mathbf x^*)
+ \sum_{j=1}^p \lambda_j \nabla h_i(\mathbf x^*)
$$

#### 原始可行性

$$
\mathbf x^* \in \mathcal F
$$

#### 互补松弛性

$$
\mu_i g_i(\mathbf x^*) = 0
$$

表示如果不等式约束不起作用时，需要让 $\mu_i = 0，$。

#### 对偶可行性

$$
\mu_i \ge 0
$$

稳定性条件表明，局部最优时目标函数的下降方向 $-\nabla f(\mathbf x^*)$ 是由约束梯度构成的。如果 $\mu_i < 0$，那么 $\mu_i g_i(\mathbf x^*)$ 指向可行域内部，可以证明此时存在一个可以让目标函数下降的方向，与 $\mathbf x^*$ 是局部最优点矛盾。

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

## 支持向量机（SVM）

超平面方程：

$$
\bm{w}^\top \bm{x} + b = 0
$$

支持向量机使用超平面（n 维空间中的 n - 1 维子空间）分类数据，平面一侧的点（$\bm{w}^\top \bm{x} + b > 0$）预测为正类，另一侧（$\bm{w}^\top \bm{x} + b < 0$）预测为负类。

性质：$\lVert\bm{w}\rVert$ 越大，更改 $b$ 值时平面移动的幅度越小（因为实质上这个方程是n+1维线性方程的截面，$\lVert\bm{w}\rVert$ 大时高维坡面更“陡峭”）。

线性可分：对于一个数据集，如果存在一个参数使得每个点，模型都能预测正确，则称这个数据集是线性可分的。我们假设数据集是线性可分的。

训练 SVM 时还需要两个平行的超平面：

* 正类边界：$\bm{w}^\top \bm{x} + b = 1$；
* 负类边界：$\bm{w}^\top \bm{x} + b = -1$。

训练时需要让正类不跑到两个边界之间（满足对于所有正类数据点 $\bm x$，$\bm{w}^\top \bm{x} + b >= 1$，负类同理）。

为了最大化模型的泛化能力，SVM 需要在不出错的情况下最大化这两个边界之间的距离（称作“间隔”，Margin）。根据超平面方程性质，就是最小化 $\lVert \bm w \rVert$。

最大化间隔后，正类/负类边界都会有数据点落在边界上，这些点就叫支持向量。

形式化：

$$
\begin{aligned}
\min_{\bm{w}, b} \quad& \frac{1}{2} \lVert\bm{w}\rVert^2\\
\text{subject to:} \quad& \bm{w}^\top \bm{x}_i + b \ge y_i, \quad i = 1, \ldots, m
\end{aligned}
$$

其中 $\bm{x}_i$ 为第 $i$ 个点，该点分类为 $y_i \in \{-1, 1\}$。

### 软间隔（Soft-Margin）支持向量机

很多时候数据集并不是线性可分的。可以允许不满足约束的点存在，存在不满足约束的点时施加一定惩罚。我们可以添加松弛变量 $\xi_i \ge 0$ 让原本需要满足 $\bm{w}^\top \bm{x}_i + b \ge y_i$ 的点现在只需满足 $\bm{w}^\top \bm{x}_i + b \ge y_i - \xi_i$ 就行，问题变成：

$$
\begin{aligned}
\min_{\bm{w}, b, \xi} \quad& \frac{1}{2} \lVert\bm{w}\rVert^2 + C \sum_{i = 1}^{m} \xi_i\\
\text{subject to:} \quad& \bm{w}^\top \bm{x}_i + b \ge y_i - \xi_i\\
& \xi_i \ge 0\\
& i = 1, \ldots, m
\end{aligned}
$$

其中 $C$ 是一个超参数，大的时候对误分类的惩罚增大。

### 核技巧

Cover 定理指出，将复杂模式通过非线性映射 $\phi$ 投射到高维空间时，数据可以线性可分的概率会变大。所以我们可以训练出 $\phi$，然后将映射后的点运用 SVM 进行分类。

> $\phi: \mathcal X \to \mathcal Z$，其中 $\mathcal X$ 称为输入空间（原始空间），$\mathcal Z$ 称为特征空间。

因为分类前需要给输入映射一下，所以 $\bm{w}^\top \bm{x}^{(i)} + b$ 就变为 $\phi(\bm{w})^\top \phi(\bm{x}^{(i)}) + b$。问题在于，很多时候 $\phi$ 映射无法计算计算，我们需要一个更高效的方法。

不止 SVM，很多机器学习算法都可以写成样本间点积的形式，于是核技巧给出了一个间接计算 $\phi(\bm{w})^\top \phi(\bm{x}^{(i)})$ 的方法。

正定核函数：给出映射 $k: \mathcal{X} \times \mathcal{X} \to \mathbb{R}$，如果存在一个 $\phi: \mathcal X \to \mathcal Z$，使得对于任意 $\bm{x}, \bm{x}' \in \mathcal X$，都有 $k(\bm{x}, \bm{x}') = \left<\phi(\bm{x}), \phi(\bm{x}')\right>$，那么称 $k$ 是一个正定核函数，运算 $\left<\cdot, \cdot\right>$ 在 SVM 的例子中就是向量点积。

等价的定义：给出映射 $k: \mathcal{X} \times \mathcal{X} \to \mathbb{R}$，如果它满足下面两点则是正定核函数：

1. 对称性：$k(\bm{x}, \bm{z}) = k(\bm{z}, \bm{x})$

2. 正定性：给出任意 $N$ 个 $\mathcal X$ 中的元素 $\bm{x}^{(1)}, \dots, \bm{x}^{(N)}$，Gram 矩阵 $\bm{K}$ 是*半*正定的（所有特征值都非负），其中 $\bm{K}_{i, j} = k(\bm{x}^{(i)}, \bm{x}^{(j)})$

回到 SVM，由于 SVM 在无限维的特征空间中工作，训练时参数 $\bm{w}$ 无法直接计算或存储，所以把预测函数写成通过几个原始空间的样本计算的形式：

$$
\left<\phi(\bm{w}), \phi(\bm{x}^{(i)})\right> + b \quad\Rightarrow\quad
b + \sum_i \alpha_i k(\bm{x}, \bm{x}^{(i)})
$$

其中 $\bm{x}_i$ 是训练样本，$\bm\alpha$ 是系数向量

核函数一般使用[高斯核（RBF 核，径向基函数核）](https://www.zhihu.com/question/660270670/answer/2070153889739978723)。

## 多维高斯分布

$\mathcal N(\bm x; \bm\mu, \bm\Sigma)$，其中 $\bm\mu$ 是最高点坐标（均值），$\bm\Sigma$ 是分布的协方差矩阵，需要是对称正定的，这意味着它满秩并且所有特征值均为正数。

这里的 $\bm\Sigma$ 可以进行谱分解，即作用是以函数最高点为中心向 $N$ 个正交的方向拉伸分布。

计算时需要用到 $\bm\Sigma^{-1}$，但不需要 $\bm\Sigma$，所以我们使用精度矩阵代替：$\bm\beta = \bm\Sigma^{-1}$，分布记为 $\mathcal N(\bm x; \bm\mu, \bm\beta^{-1})$。

## 混合密度网络（MDN）

混合密度网络用于回归任务，它的输出单元和通常的神经网络不同，是一个概率分布。具有 $N$ 个分量，输出维数为 $D$ 的高斯混合输出为：

$$
p(\bm y, \bm x) = \sum_{i=1}^N p(\mathrm c = i | \bm x) \mathcal{N}(\bm y; \bm\mu^{(i)}(\bm x), \bm\Sigma^{(i)}(\bm x))
$$

神经网络需要输出：

1. 混合组件 $p(\mathrm c = i | \bm x)$，一个 $N$ 维向量。由于是离散概率分布，所以需要通过 $softmax$ 函数保证和为 1。

2. 高斯分布的均值 $\bm\mu^{(i)}(\bm x)$，总共是 $N$ 个 $D$ 维向量。

3. 协方差矩阵 $\bm\Sigma^{(i)}(\bm x)$（对称正定）。一般假设各维度独立，此时它是一个对角矩阵，相当于 $N$ 个 $D$ 维向量。需要保证每个元素为正，比如可以用 ELU 激活函数加上一个小常数。

## 激活函数

**logistic sigmoid**：以前经常用，输入绝对值较大时会饱和（导数接近 0）。

**tanh**：可以将 logistic sigmoid 平移缩放得到，当必须使用 sigmoid 激活函数时通常比 logistic sigmoid 好用，因为在 0 附近近似于 $g(z) = z$。

**ReLU**：比 sigmoid 好，计算成本较低，但是由于左侧导数为 0，学习率过大时输入远小于 0 导致权重很难更新，即死亡神经元。不过人的大脑也只有小部分的神经元活跃。另外一个缺点是没法输出负值。

**Leaky ReLU**：$g(x) = max\{\alpha x, x\}$，其中 $\alpha$ 是一个小的正数，比如 0.01。这样做能让函数左边导数不为 0，避免了死亡神经元问题。

**PReLU**：将 Leaky ReLU 的 $\alpha$ 作为一个可学习的参数，无约束，初值大于 0（一般是 0.25 或 0.3）。可以整层共用一个 $\alpha$（channel-shared）或者每个神经元单独一个（channel-wise，参数量多）。

**maxout**：maxout 单元将输入划分成 $k$ 段，每段取最大值，可以拟合 $k$ 段的分段线性的凸函数它跟 ReLU 一样不会饱和，但同时也不会有死亡神经元问题，不过参数量很多。

## 各种概念

**流形学习**：可能出现的数据一般被限制在一个高维空间中的高度非线性的低维流形。

**表示学习**：训练出一个非线性变换，使得后续任务更容易完成。

**迁移学习**：先得到一个对广泛问题拟合很好的模型，然后训练神经网络的最后几层用于特定的问题。

**对比学习**：在特征空间中，拉近同类点之间的距离，推远异类点之间的距离。

## 对比学习

我们在特征空间中选一个数据点 $\bm x_\text{anchor}$ 称为锚点，选一个数据点 $\bm x_+$ 称为正样本，选 $N$ 个样本 $\{\bm x_-^{(1)}, \dots, \bm x_-^{(N)}\}$ 称为负样本。

目标是改变原始空间到特征空间的映射，让锚点离正样本尽可能进，同时离负样本尽可能远，不关心负样本间的距离。

通常用 InfoNCE 损失函数：

$$
J = -\log \frac{
   \exp(\text{sim}(\bm{x}_\text{anchor}, \bm{x}_+))
}{
   \exp(\text{sim}(\bm{x}_\text{anchor}, \bm{x}_+))
   + \sum_{i=1}^N \exp(\text{sim}(\bm{x}_\text{anchor}, \bm{x}_-^{(i)}))
}
$$

其中 $\text{sim}$ 衡量向量相似度，一般定义为 $\text{sim}(\bm x, \bm z) = \bm{x}^\top \bm{z}$。

## 正则化

目的：防止模型过拟合，提升泛化能力。

### 参数范数惩罚

$$
\tilde{J}(\bm \theta; \bm X, \bm y) = J(\bm X, \bm y) + \alpha \Omega(\bm \theta)
$$

神经网络中，一般只对权重而不对偏置做惩罚。

$L^2$ 正则化：$\Omega(\bm w, b) = \frac{1}{2} \lVert\bm{w}\rVert^2$。

$L^1$ 正则化：$\Omega(\bm w, b) = \lVert\bm{w}\rVert_1 = \sum_i \lvert w_i\rvert$。具有稀疏性，到最优值附近时部分元素会变为 0。

需要最小化的是 $\tilde{J}(\dots)$，计算测试\训练\验证误差时只计算 $J(\dots)$ 就行。

### 数据增强

对数据做一些变换（旋转、平移、缩放、加噪声），在不改变类别（比如对于数字识别，数字 6 旋转半圈变成 9，这样改变了类别）的基础上制造出更多样本。

### 多任务学习

神经网络前几层通用，后面一个任务对应后面的隐藏层和输出层。

### 早停

有时候模型会过拟合，导致 loss 曲线先下降后升高。早停策略在发现验证集 loss 升高达到特定次数后停止训练，保留 loss 最低的参数。

可以用上述的算法训练样本，获得最佳的训练步数，再去训练样本（此时可以不需要验证集）。

或者是用该算法获得最佳的代价函数值和参数，然后参数不变，在所有数据上训练再次达到该值。

### 参数绑定与参数共享

如果有 A、B 两个模型，我们认为输入输出比较相似，那么参数也应该是相似的，我们可以构造正则化函数来利用这个信息，即 $\Omega(\bm{w}^{(A)}, \bm{w}^{(b)}) = \lVert\bm{w}^{(A)} - \bm{w}^{(b)}\rVert^2$。

我们还可以强迫某些参数相等，这样能够减小训练的参数数量，这种方法就叫做参数绑定。

卷积神经网络就是一种参数绑定的体现，由于我们知道图片内容有平移不变性，图像的每个区域就都共用相同的一组参数来计算。

### 稀疏表示

情况一般分为参数稀疏和表示的稀疏。

参数稀疏可以通过 $L^1$ 正则化实现。

表示指的是神经网络一层提取出的特征，如全连接层的输出 $\bm h$、卷积层的特征图。

对于全连接层，通过 $L^1$ 范数正则化使 $\bm h$ 更稀疏：$\Omega(\bm h) = \lVert \bm{h} \rVert_1$。

### 模型集成

对不同架构模型的输出取平均值得到最终输出。

### Dropout

Dropout 可以认为是模型集成的一种近似。

## 模型选择

训练集：参与训练，在训练集上最小化代价函数 $\tilde J$，只有这个需要正则化。

交叉验证集（验证集/开发集）：不直接参与训练。在训练集上训练若干步后在交叉验证集评估效果，并调整超参数。

测试集：不能参与训练或影响模型，只能用于评估模型效果。
