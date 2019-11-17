numbers = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
            'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twelve')

first_input = int(input("Digite um numero entre 0 e 20: "))
while first_input < 0 or first_input > 20:
    first_input = int(input("Numero não está entre o 0 e 20, digite novamente: "))
    

print(numbers[first_input])

