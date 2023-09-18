from collections import Counter

filename = "text.txt"
top_results=10

with open(filename, "r", encoding="utf8") as f:
    inp = f.read()
    f.close()
    
inp = inp.lower()
inp = inp.split()
double_words = []

for i in range(len(inp) - 1):
    double_words.append(inp[i] + " " + inp[i + 1])
    
Counter = Counter(double_words)
most_occur = Counter.most_common(top_results)

for i in range(top_results):
    print(most_occur[i])