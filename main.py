def maior_substring(str1, str2):

    # criando a matrix
    matriz = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):

            if i == 0:
                matriz[i][j] = j
                
            elif j == 0:
                matriz[i][j] = i

            elif str1[i - 1] == str2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1] + 1

            else:
                s1 = matriz[i - 1][j]
                s2 = matriz[i][j - 1]

                # encontra o valor minimo e coloca na posição da matriz
                matriz[i][j] = min(s1 + 1, s2 + 1)

    return matriz[len(str1)][len(str2)]

# Exemplo de uso:
str1 = str(input("Digite uma palavra: "))
str2 = str(input("Digite uma palavra: "))

result = maior_substring(str1, str2)

print(result)
