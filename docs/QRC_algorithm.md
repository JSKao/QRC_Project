**Generic Quantum System** $H = \sum_{i < j} J_{ij} \sigma_x^{(i)} \sigma_x^{(j)} + h \sum_{i} \sigma_z^{(i)} $

- $ J_{ij} $：隨機耦合強度，從 $[-J_s/2, J_s/2]$ 中均勻抽樣。
- h ：橫場強度。
- $ \sigma_x^{(i)}$ and $ \sigma_z^{(i)} $：第 (i) 個自旋的 Pauli 矩陣。

1. 通過哈密頓量 (H)，計算了時間演化算符： $ U(t) = e^{-i H t} $ 並使用 $U(t)$ 對量子態進行時間演化： $ \rho(t + \Delta t) = U(\Delta t) \rho(t) U^\dagger(\Delta t) $

2. 在每個時間間隔 $\Delta t$ 時，將隨機輸入 $s \in [0, 1]$ 編碼為量子態： $ \psi_{\text{inject}} = \sqrt{1-s} |0\rangle + \sqrt{s} |1\rangle $ 並將其與系統的其餘部分進行張量積，更新整個系統的量子態： $ \rho_{\text{new}} = \psi_{\text{inject}} \otimes \rho_{\text{reduced}} $

3. 計算每個自旋的可觀測量（例如 $\sigma_z$ 的期望值）： $ \langle \sigma_z^{(i)} \rangle = \text{Tr}(\rho \cdot \sigma_z^{(i)})$

4. 使用 Hilbert-Schmidt 距離來量化兩個量子態之間的差異： $ D(\rho_1, \rho_2) = \sqrt{\text{Tr}[(\rho_1 - \rho_2)^2]} $



# QRC analysis Tools

## Short-Term Memory, STM

是量化系統對過去輸入的記憶能力的指標。STM 的計算基於輸入序列和系統輸出的相關性。

公式： $$ MC = \sum_{\tau} \text{Corr}^2(y(t), x(t-\tau)) $$ 其中：

$ x(t) $：輸入序列

$ y(t) $：系統輸出

$ \tau $：延遲時間

$ \text{Corr} $：相關性

步驟 1：設計 STM 計算框架
我們需要以下幾個部分：

1. 生成隨機輸入序列 ( x(t) )
2. 模擬系統響應 ( y(t) )
3. 計算輸入與輸出之間的相關性

## Quantum Information Capacity

1. 糾纏熵的計算
分析系統中量子態的糾纏特性，計算部分跡後的 von Neumann 熵： $ S(\rho) = -\text{Tr}(\rho \log_2 \rho) $ 其中 $\rho$ 是對部分自旋取跡後的密度矩陣。

2. 量子通道的模擬
模擬量子通道（例如退極化通道）對量子態的影響： $ \mathcal{E}(\rho) = (1-p) \rho + p \frac{\mathbb{I}}{d} $ 其中 (p) 是噪聲強度，(d) 是系統的希爾伯特空間維度。

3. 量子測量的模擬
模擬對量子態進行投影測量的過程： $ P_k = |\psi_k\rangle \langle \psi_k|, \quad \rho_{\text{post}} = \frac{P_k \rho P_k}{\text{Tr}(P_k \rho)} $ 其中 $P_k$ 是測量算符，$\rho_{\text{post}}$ 是測量後的量子態。

4. 記憶能力的分析
計算系統的記憶容量，用於量化系統對過去輸入的記憶程度： $ MC = \sum_{\tau} \text{Corr}^2(y(t), x(t-\tau)) $ 其中 $\text{Corr}$ 是輸入 $x(t-\tau)$ 和輸出 $y(t)$ 的相關性，$\tau$ 是延遲。

5. 多樣性分析
分析系統狀態的多樣性，計算狀態分佈的熵： $ H = -\sum_{i} p_i \log_2 p_i $ 其中 $p_i$ 是系統狀態的概率分佈。

6. 輸入與輸出映射
設計輸入序列 (x(t)) 和輸出序列 (y(t))，並學習它們之間的映射： $ y(t) = f(x(t), x(t-1), \dots, x(t-\tau)) $ 其中 (f) 是由量子態的演化和測量結果決定的函數。
