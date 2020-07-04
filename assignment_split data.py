text = 'geeks for geeks'
print(text.split()) 
word = 'geeks, for, geeks'
print(word.split(',')) 
word = 'geeks:for:geeks'
print(word.split(':'))
word = 'CatBatSatFatOr'
print([word[i:i+3] for i in range(0, len(word), 3)]) 