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

这里的 $\beta$ 值一般也是一个接近 $1$ 的数。

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
* $(1)$ 式、$(2)$ 式里的分母就是偏差修正。

# 偏差修正

偏差修正是用来处理初值问题的。

为简单起见，我们考虑动量法：

$$
\begin{align*}
V := \beta V + (1-\beta)\delta\theta  \tag1\\
\theta := \theta - \eta V
\end{align*}
$$

人们之前会把 $V$ 初值 $V_0$ 设为 $0$，那么我们带入第一步的 $(1)$ 式：$V_1 = (1-\beta)\delta\theta$。因为 $\beta$ 接近 $1$，显然第一步的 $V$ 比 $\delta\theta$ 小很多。

那这样的话，我们的梯度下降会在训练一开始会走的比较慢，后面才会逐渐正常。或者换个表述，随着训练步数 $t$ 变大，$V_0$ 在 $V_t$ 中的“占比”会变小，比如我们展开第三步，此时

$$
V =
\underbrace{\beta^3V_0}_{
    \mathclap{初值项，在这个多项式中的占比变小}
} + \overbrace{
    (1-\beta)\beta^2\delta\theta_0
    + (1-\beta)\beta\delta\theta_1
    + (1-\beta)\delta\theta_2
}^{真正有用的项}
$$

不难知道这个多项式的系数和为 $1$，由于 $V_0$ 被设为 $0$，我们需要将 $V$ 除以某个数使除了 $V_0$ 以外的系数和为 $1$（或者说，指数加权移动平均的正确形式需对加权和做归一化），这就是偏差修正。
