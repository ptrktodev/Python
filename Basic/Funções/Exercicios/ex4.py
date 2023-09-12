def maior(list):
    sorted_numbers = sorted(list)
    maior = sorted_numbers[-1]
    print(f"O número maior é: {maior}.")


nums = int(input('Quantos numeros vai digitar: '))
list_nums = []

for c in range(nums):
    list_nums.append(int(input("Número: ")))

maior(list_nums)
