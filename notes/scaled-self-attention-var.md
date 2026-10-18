# 自注意力中的缩放系数推导

将查询参数矩阵视作随机变量 $\mathbf W^q$，同理其他随机变量有 $\mathbf W^k$、$\mathbf Q$、$\mathbf K$，记 $\mathbf S = \mathbf Q \mathbf K^\top$。输入 $\bm X$ 视为已经观测到的值，不是随机变量。

对于 $\mathbf W^q$ 和 $\mathbf W^k$，我们对其中每个元素（实数的随机变量），假设它们**相互独立，期望为零**，方差都为 $\sigma^2$。这些假设可以调整参数随机初始化策略来满足，不过训练了之后就不会再满足了。

展开矩阵求和：

$$
\begin{aligned}
\mathrm Q_{i, j} &= \bm X_{i, :}^\top \mathbf W^q_{:, j} && \text{(矩阵乘法展开)}\\
&= \sum_{a=1}^D X_{i, a} \mathrm W^q_{a, j} && \text{(点积展开)}\\
\end{aligned}
$$

计算 $\mathbf Q$ 元素的期望：

$$
\begin{aligned}
\mathbb E[\mathrm Q_{i, j}] &= \mathbb E[\sum_{a=1}^D X_{i, a} \mathrm W^q_{a, j}] && \text{(展开式代入)}\\
&= \sum_{a=1}^D \mathbb E[X_{i, a} \mathrm W^q_{a, j}] && \text{(期望值的线性性质)}\\
&= \sum_{a=1}^D \mathbb E[\mathrm W^q_{a, j}] X_{i, a} && \text{(常数移出括号)}\\
&= 0 && \text{(参数期望为零)}\\
\end{aligned}
$$

看看方差：

$$
\begin{aligned}
\operatorname{Var}(\mathrm Q_{i, j}) &= \mathbb E[(\mathrm Q_{i, j} - \mathbb E[\mathrm Q_{i, j}])^2] && \text{(方差定义)}\\
&= \mathbb E[\mathrm Q_{i, j}^2] && \text{(期望为零带入)}\\
&= \mathbb E[(\sum_{a=1}^D X_{i, a} \mathrm W^q_{a, j})(\sum_{b=1}^D X_{i, b} \mathrm W^q_{b, j})] && \text{(展开式带入)}\\
&= \sum_{a=1}^D \sum_{b=1}^D X_{i, a} X_{i, b} \,\mathbb E[\mathrm W^q_{a, j} \mathrm W^q_{b, j}] && \text{(整理)}
\end{aligned}
$$

> 给出随机变量 $\mathrm a$ 和 $\mathrm b$，根据协方差定义，有：
>
> $$
\operatorname{Cov}(\mathrm a, \mathrm b) = \mathbb E[\mathrm a \mathrm b] - \mathbb E[\mathrm a] \cdot \mathbb E[\mathrm b]
> $$
>
> 所以当两者独立（协方差始终为零）时，$\mathbb E[\mathrm a \mathrm b] = \mathbb E[\mathrm a] \cdot \mathbb E[\mathrm b]$。

这里当 $a \not= b$ 时，根据独立性，得到：

$$
\mathbb E[\mathrm W^q_{a, j} \mathrm W^q_{b, j}] = 0 \cdot 0 = 0
$$

> 对于随机变量 $\mathrm a$，根据方差定义，有：
>
> $$
\operatorname{Var}(\mathrm a) = \mathbb E[\mathrm a^2] - \mathbb E[\mathrm a]^2
> $$
>
> 由此可以通过期望和方差计算 $\mathbb E[\mathrm a^2]$。

所以方差：

$$
\begin{aligned}
\operatorname{Var}(\mathrm Q_{i, j}) &= \sum_{a=1}^D X_{i, a}^2 \,\mathbb E[(\mathrm W^q_{a, j})^2] && \text{(合并两个求和)}\\
&= \sum_{a=1}^D X_{i, a}^2 \operatorname{Var}(\mathrm W^q_{a, j}) + \mathbb E[\mathrm W^q_{a, j}]^2 && \text{(拆分平方的期望)}\\
&= \sum_{a=1}^D X_{i, a}^2 \sigma^2\\
&= \sigma^2 \sum_{a=1}^D X_{i, a}^2\\
&= \sigma^2 \lVert\bm X_{i, :}\rVert^2
\end{aligned}
$$

这些对于 $\mathbf K$ 同理。

现在可以看 $\mathbf S$ 了：

$$
\begin{aligned}
\mathrm S_{i, j} &= \mathbf Q_{i, :}^\top (\mathbf K^\top)_{:, j}\\
&= \mathbf Q_{i, :}^\top \mathbf K_{j, :}\\
&= \sum_{a=1}^{D_k} \mathrm Q_{i, a} \mathrm K_{j, a}
\end{aligned}
$$

期望：

$$
\begin{aligned}
\mathbb E[\mathrm S_{i, j}] &= \sum_{a=1}^{D_k} \mathbb E[\mathrm Q_{i, a} \mathrm K_{j, a}]\\
&= \sum_{a=1}^{D_k} \mathbb E[\mathrm Q_{i, a}] \, \mathbb E[\mathrm K_{j, a}] && \text{(根据独立性)}\\
&= 0 && \text{(已证期望为零)}
\end{aligned}
$$

方差：

$$
\begin{aligned}
\operatorname{Var}(\mathrm S_{i, j}) &= \mathbb E[\mathrm S_{i, j}^2] && \text{(期望为零)}\\
&= \sum_{a=1}^{D_k} \mathbb E[(\mathrm Q_{i, a} \mathrm K_{j, a})^2]\\
&= \sum_{a=1}^{D_k} \mathbb E[\mathrm Q_{i, a}^2]\, \mathbb E[\mathrm K_{j, a}^2] && \text{(独立性)}\\
&= \sum_{a=1}^{D_k} \sigma^2 \lVert\bm X_{i, :}\rVert^2 \cdot \sigma^2 \lVert\bm X_{j, :}\rVert^2 && \text{(方差带入)}\\
&= D_k \sigma^4 \lVert\bm X_{i, :}\rVert^2 \lVert\bm X_{j, :}\rVert^2 && \text{(拆开求和)}
\end{aligned}
$$
