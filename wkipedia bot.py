import wikipedia
content = input("Enter The Content to Search : ")
results = wikipedia.summary(content, sentences=2)
print(results)