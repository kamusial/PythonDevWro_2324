def woda(koszt_netto: float,
         podatek: int = 23,
         opakowanie: str = "plastik") -> float:
    print(opakowanie)
    return koszt_netto + koszt_netto * podatek / 100


koszt_brutto = woda(2.0, opakowanie="szkło")
# IDE podkreśla zły typ argumentu
koszt_brutto = woda(2.0, opakowanie=5)
print(koszt_brutto)
