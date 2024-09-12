#SERVIDOR JONATHAN ROSAS CEDILLO

def fibonachi(n: int) -> int:
    multiplicaicon = 1
    for value in range(1,n+1):
        multiplicaicon *= value
        
    return multiplicaicon

Resultado = fibonachi(5)
print(Resultado)
