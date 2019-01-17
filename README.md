# skpipes

Small hack to sklearn syntax, allowing a (imho) cleaner way to define pipelines and feature unions.

```python
import skpipes
from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn.linear_model import LogisticRegression

# this returns a pipeline, comprised of StandardScaler and LogisticRegression
pipe = StandardScaler() >> LogisticRegression() 

# a feature union of StandardScaler and Normaliser
union = StandardScaler() + Normalizer()
```
