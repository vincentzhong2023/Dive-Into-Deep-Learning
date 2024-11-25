import torch
from torch.distributions import multinomial
import matplotlib.pyplot as plt
from matplotlib_inline import backend_inline

fair_probs = torch.ones([6]) / 6
#fair_probs = torch.tensor([0.3, 0.3, 0.4, 0.5, 0.3, 0.3])
x1 = multinomial.Multinomial(1, fair_probs).sample()
#print(x1)

x2 = multinomial.Multinomial(10, fair_probs)
y2 = x2.sample()
#print(type(x2))

x3 = multinomial.Multinomial(1000, fair_probs).sample()
#print(x3/x3.sum(), fair_probs/fair_probs.sum())

counts = multinomial.Multinomial(10, fair_probs).sample((500,))
print(counts)

cum_counts = counts.cumsum(dim=0)

print(cum_counts)
estimates = cum_counts / cum_counts.sum(dim=1, keepdims=True)

print(estimates)
print(estimates[:, 1])


plt.figure(figsize=(6, 4.5))

for i in range(6):
    plt.plot(estimates[:, i].numpy(), label=("P(die=" + str(i + 1) + ")"))
    pass
plt.axhline(y=0.167, color='black', linestyle='dashed')
plt.gca().set_xlabel('Groups of experiments')
plt.gca().set_ylabel('Estimated probability')
plt.legend()

plt.show()