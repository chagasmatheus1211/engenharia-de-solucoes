
print("========================================")
print("   SISTEMA DE TRIAGEM DE GLICEMIA")
print("========================================")

nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
glicose = float(input("Digite o nível de glicose (mg/dL): "))

print("\n========== RESULTADO DA TRIAGEM ==========")
print("Paciente:", nome)
print("Idade:", idade, "anos")
print("Glicose:", glicose, "mg/dL")

if glicose < 0:
    print("\nValor de glicose inválido. Verifique os dados informados.")

elif glicose > 300:
    print("\nALERTA: Glicose muito alta!")
    print("Encaminhamento prioritário para avaliação médica.")
    print("Solicite atendimento profissional imediato.")

else:
    print("\nO valor não ultrapassou o limite definido pelo sistema.")
    print("Siga o fluxo de atendimento da unidade de saúde.")

print("========================================")
print("Triagem finalizada.")
