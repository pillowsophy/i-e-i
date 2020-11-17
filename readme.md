# I-E-I: Information of "Ethical Information"

Published by Luciano Floridi

## How the nodes are connected?
단어와 단어는 어떻게 관련되었다고 할 수 있을까요? 한 단어가 다른 단어와 '연결'되었다고 말할 수 있으려면, 특정한 기준이 필요합니다. 여기서는 문장(!,? .) 별로 글을 나누고, 각 문장 내에서도 특정한 간격만큼 나누어 단어의 관련도를 파악합니다. 이때, 이 특정한 간격을 **window** 라고 합니다.

> I love cat. <br>
Cat is the most adorable creature in the world. <br>
But cats mostly don't like me.

위와 같은 글이 있습니다. 먼저 온점(.) 에 따라 세 개의 문장으로 나뉩니다. window 가 3일 경우를 생각해보겠습니다. 첫 번째 문장 `I love cat` 에서 단어 `I`,`love`, `cat` 는 서로 연관이 있는 단어들입니다. 한편 두 번째 문장은 3 단어씩 잘리게 됩니다. `Cat is the`, `is the most`, `the most adorable`, `most adorable creature` ... 이런 식으로 연속으로 나온 3 단어는 서로 관련이 있는 것으로 봅니다.

## What does the size of nodes mean?



## What about the color of nodes?



## When you click a node...