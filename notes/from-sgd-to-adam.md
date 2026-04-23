# SGD

这个是最简单的，每次更新都朝“下山”方向迈出一步。

$$
\theta := \theta - \eta\delta\theta
$$

其中：
* $\theta$ 是模型的某个参数；
* $\delta\theta$ 表示当前损失函数关于参数 $\theta$ 的偏导数，即 $\frac{\partial L}{\partial \theta}(当前参数)$；
* $\eta$ 是学习率，一般取 $0.01$ 这样的值。

# 动量（momentum）法

这个方法能够利用之前算出的梯度，将其与当前算出的梯度以某种比例混和：

$$
V := \beta V + (1-\beta)\delta\theta\\
\theta := \theta - \eta V
$$

其中：
* $\beta$ 就是刚刚提到的混合比例，一般取 $0.99$ 这样的值

# RMSprop

这个方法根据梯度向量的“长度”（也是和前几次的混合）动态更新学习率。

$$
S := \beta S + (1-\beta) (\delta\theta)^2\\
\theta := \theta - \eta\frac{\delta\theta}{\sqrt{S}}
$$

代码实现里分母那里会加上一个微小量 $\epsilon$ 防止除零。

# Adam

这个方法不仅组合了动量法和 RMSprop，还加入了偏差修正（Bias Correction）：

$$
\begin{align}
V := \frac{\beta_1 V + (1-\beta_1)\delta\theta}{1-{\beta_1}^t} \\
S := \frac{\beta_2 S + (1-\beta_2)(\delta\theta)^2}{1-{\beta_2}^t} \\
\theta := \theta - \frac{\eta V}{\sqrt S}
\end{align}
$$

其中：
* $(1)$ 式、$(2)$ 式里的分母就是偏差修正；

偏差修正是用来处理初值问题的。

假如没有这个修正，即分母为 $1$，我们先把 $V$、$S$ 初值 $V_0$、$S_0$ 都设为 $0$，那么我们带入第一步的 $(1)$ 式：V_1 =
