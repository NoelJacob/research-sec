# Steps

[x] download 10K, 10Q, 8K, 6K, DEF 14A using edgartools
[] do the omit based on [Gemini](https://gemini.google.com/share/7a40b7802ea7)
[x] convert it to markdown
[x] delete files older than 2009
[] do this [Gemini](https://gemini.google.com/app/94ce1281bc2e5448)

# Leads

- Use the normal prompt
- Use the normal prompt with the stateless clause

# Current Steps

### Tokens

find ./edgartools-data -type f -exec cat {} + | wc -c

### Files

find ./edgartools-data -type f | wc -l

244 charecters
